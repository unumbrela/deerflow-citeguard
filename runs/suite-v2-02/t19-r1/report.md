# Systematic Literature Review: Federated Learning

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "federated learning", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers (2024-2025) in the cs.LG category focusing on federated learning. The surveyed literature reveals a field maturing beyond foundational algorithms to address practical deployment challenges. Three dominant research directions emerge: (1) incentive mechanisms and rational client participation, (2) handling data heterogeneity and client selection strategies, and (3) robustness against adversarial attacks and evaluation methodologies. The collective work demonstrates that federated learning is transitioning from theoretical frameworks to real-world applications in domains like healthcare (infant movement analysis) and traffic forecasting. However, significant challenges remain in ensuring sustainable participation, managing non-IID data distributions, and providing reliable performance evaluation without centralized test data.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "federated learning", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Incentive Mechanisms and Rational Client Participation

A critical challenge in federated learning is ensuring sustained client participation when clients are rational agents who may prioritize local utility over global model performance. Hewa Kaluannakkage and Buyya (2025) identify that participating entities are often unwilling to contribute unless they receive benefits, or may free-ride on others' contributions. They propose that well-designed incentive mechanisms are essential components for practical success, not optional features, drawing from economics, game theory, blockchain, and deep reinforcement learning.

Yashwanth et al. (2026) formalize this problem through FedUCA, a framework that addresses client attrition in cross-silo environments where statistical heterogeneity causes rational clients to opt out when perceived benefits fail to meet local utility thresholds. Their utility-constrained stochastic aggregation approach achieves significantly higher client retention and superior global model performance by prioritizing participation feasibility. This theme reflects a growing recognition that federated learning systems must account for the economic and strategic behavior of participants, not just algorithmic efficiency.

### Theme 2: Managing Data Heterogeneity Through Client Selection

Statistical data heterogeneity remains a fundamental challenge in federated learning, with multiple papers proposing client selection strategies to mitigate its effects. Németh et al. (2025) characterize heterogeneity using six metrics covering global and client attribute imbalance, class imbalance, and spurious correlations. Their FEDDIVERSE algorithm promotes collaboration between clients with complementary data distributions, enhancing performance and robustness while maintaining low communication and computational overhead.

Düsing and Cimiano (2025) extend this approach by proposing distribution-controlled client selection that aligns active clients' label distributions with either a balanced distribution or the federation's combined label distribution. Their empirical validation shows that alignment with a balanced distribution yields the greatest improvements when facing local imbalance, while alignment with the federation's combined distribution is superior for addressing global imbalance. Sen et al. (2025) provide a comprehensive review of partial client participation challenges, noting that existing research has focused more on full participation assumptions, leaving practical deployment scenarios underexplored.

### Theme 3: Robustness, Privacy, and Evaluation

The third major theme addresses the need for robust, private, and reliably evaluated federated learning systems. Kritharakis et al. (2025) develop a loss-based client clustering approach that functions effectively with only two honest participants (the server and one client) without prior knowledge of malicious client count. Their algorithm significantly outperforms standard and robust FL baselines under various Byzantine attack strategies including label flipping, sign flipping, and Gaussian noise addition.

Xia et al. (2025) propose Fed-DPRoC, a unified framework that jointly provides differential privacy, Byzantine robustness, and communication efficiency without compromising any property. Their RobAJoL instantiation integrates Johnson-Lindenstrauss-based compression with robust averaging, substantially reducing communication overhead while preserving robustness and utility.

Stricker et al. (2026) address evaluation challenges, demonstrating that common aggregation strategies like weighted averaging based on local samples do not produce results consistent with centralized evaluation. Their FLAM method yields the same results as centralized evaluation without requiring a global test dataset, addressing a critical gap in federated learning benchmarking.

### Theme 4: Application-Specific Federated Learning

Recent work extends federated learning to specialized domains with unique requirements. Ho (2026) presents the first federated learning framework for automated infant movement analysis using skeletal motion data, addressing privacy and data-sharing constraints that make centralized training impractical in clinical settings. Their Uncertainty-Aware Federated Averaging (UA-FedAvg) strategy incorporates predictive entropy into the aggregation process, achieving performance approaching centralized training.

Banik et al. (2025) propose a lightweight graph-aware FL approach for traffic forecasting that captures spatial relationships between clients while remaining computationally efficient. Their method blends FedAvg simplicity with graph learning principles, applying neighbourhood aggregation to guide parameter updates by weighting client models based on graph connectivity, achieving competitive performance on METR-LA and PEMS-BAY benchmarks.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that data heterogeneity is a fundamental challenge requiring active management rather than passive acceptance. Multiple papers (Németh et al., 2025; Düsing & Cimiano, 2025; Yashwanth et al., 2026) converge on the finding that client selection and participation mechanisms must be explicitly designed rather than assumed. There is also broad agreement that evaluation methodologies must evolve beyond simple accuracy metrics to account for privacy, robustness, and communication efficiency simultaneously.

**Disagreements**: While there is consensus on the importance of incentive mechanisms, papers differ in their approach: Hewa Kaluannakkage and Buyya (2025) emphasize economic and game-theoretic foundations, while Yashwanth et al. (2026) focus on utility-constrained optimization without explicit economic modeling. Similarly, for handling heterogeneity, Németh et al. (2025) promote diversity-driven selection, whereas Düsing and Cimiano (2025) advocate distribution alignment strategies—both effective but with different theoretical foundations and implementation requirements.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the papers explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints. Second, while multiple papers address partial client participation (Sen et al., 2025; Yashwanth et al., 2026), there is limited empirical validation in real-world cross-silo deployments with actual rational agents. Third, the evaluation gap identified by Stricker et al. (2026) suggests that many existing FL benchmarks may not accurately reflect true model performance. Finally, the application-specific papers (Ho, 2026; Banik et al., 2025) point to a need for more domain-specific federated learning frameworks that account for unique constraints in healthcare, transportation, and other critical sectors.

## Per-Paper Annotations

### Banik et al. (2025)

**Research question**: How can federated learning approaches capture spatial relationships between clients in traffic prediction tasks while remaining computationally efficient?
**Methodology**: The authors propose a lightweight graph-aware FL approach that blends FedAvg simplicity with graph learning principles, applying neighbourhood aggregation to guide parameter updates by weighting client models based on graph connectivity, evaluated on METR-LA and PEMS-BAY datasets.
**Key findings**:
- The graph-aware approach captures spatial relationships between clients effectively
- The method achieves competitive performance compared to standard baselines and recent graph-based federated learning techniques
- The approach remains computationally efficient compared to full Federated Graph Learning methods
**Limitations**: Not stated in abstract

### Düsing and Cimiano (2025)

**Research question**: How can client selection methods in federated learning mitigate the detrimental effects of data imbalance on shared model performance?
**Methodology**: The authors propose an extension to existing FL strategies that selects active clients based on aligning their label distribution with either a balanced distribution or the federation's combined label distribution, empirically validated on three common FL strategies and two datasets.
**Key findings**:
- Aligning the label distribution with a balanced distribution yields the greatest improvements when facing local imbalance
- Alignment with the federation's combined label distribution is superior for addressing global imbalance
- Distribution-controlled client selection improves shared model performance compared to existing FL strategies
**Limitations**: Not stated in abstract

### Hewa Kaluannakkage and Buyya (2025)

**Research question**: How can incentive mechanisms be designed to address the participation dilemma in federated learning systems?
**Methodology**: The chapter identifies fundamental challenges in designing incentive mechanisms and examines how concepts from economics and game theory can be applied to federated learning, alongside technology-driven solutions like blockchain and deep reinforcement learning, presenting a comprehensive taxonomy covering both centralized and decentralized architectures.
**Key findings**:
- Participating entities in federated learning are often unwilling to contribute unless they receive benefits, or may pretend to participate and free-ride on others
- Foundational concepts from economics and game theory can be applied to federated learning alongside blockchain and deep reinforcement learning solutions
- Well-designed incentive mechanisms are essential components for the practical success of federated learning, not merely optional features
- The analysis reveals both promising solutions that have emerged and significant challenges remaining in building sustainable, fair, and robust federated learning ecosystems
**Limitations**: Not stated in abstract

### Ho (2026)

**Research question**: How can federated learning be applied to automated infant movement analysis while addressing privacy and data-sharing constraints in clinical settings?
**Methodology**: The paper presents the first federated learning framework for automated infant movement analysis using skeletal motion data, evaluated on fidgety movement classification with Monte Carlo Dropout for uncertainty estimation and an Uncertainty-Aware Federated Averaging (UA-FedAvg) strategy, using a cross-subject evaluation protocol under a three-client federated learning setting.
**Key findings**:
- Federated learning substantially improves classification performance compared with independently trained local models
- Federated learning achieves performance approaching that of centralized training
- UA-FedAvg and its variant incorporating validation loss generally outperform conventional FedAvg across evaluated data-split configurations
- The framework addresses privacy, governance, and data-sharing constraints that make centralized training impractical in clinical settings
**Limitations**: Not stated in abstract

### Kritharakis et al. (2025)

**Research question**: How can federated learning maintain model quality when clients are subject to adversarial Byzantine attacks without prior knowledge of the number of malicious clients?
**Methodology**: The authors develop an approach requiring only two honest participants (the server and one client) to function effectively, using loss-based client clustering, with theoretical analysis demonstrating bounded optimality gaps and experimental validation on MNIST, FMNIST, and CIFAR-10 using the Flower framework under various attack strategies.
**Key findings**:
- The algorithm functions effectively with only two honest participants without prior knowledge of malicious client count
- Theoretical analysis demonstrates bounded optimality gaps even under strong Byzantine attacks
- The algorithm significantly outperforms standard and robust FL baselines (Mean, Trimmed Mean, Median, Krum, Multi-Krum) under various attack strategies including label flipping, sign flipping, and Gaussian noise addition
**Limitations**: Not stated in abstract

### Németh et al. (2025)

**Research question**: How can statistical data heterogeneity in federated learning be characterized and managed to improve model generalization and convergence?
**Methodology**: The paper characterizes statistical data heterogeneity using 6 metrics of global and client attribute imbalance, class imbalance, and spurious correlations, creates seven computer vision datasets for federated learning covering a broad range of statistical data heterogeneity, and proposes FEDDIVERSE, a diversity-driven client selection algorithm that promotes collaboration between clients with complementary data distributions.
**Key findings**:
- Statistical data heterogeneity can be characterized by 6 metrics of global and client attribute imbalance, class imbalance, and spurious correlations
- Seven new federated learning datasets were created and shared that cover a broad range of statistical data heterogeneity
- FEDDIVERSE enhances performance and robustness of various FL methods while having low communication and computational overhead
- The algorithm manages data heterogeneity by promoting collaboration between clients with complementary data distributions
**Limitations**: Not stated in abstract

### Sen et al. (2025)

**Research question**: What are the practical and theoretical challenges of partial client participation in federated learning, and what methods exist to address them?
**Methodology**: This survey paper provides an extensive review of existing FL methods designed to cope with partial client participation, offering comprehensive analysis supported by theoretical insights and empirical findings, along with a structured categorization of these methods highlighting their advantages and disadvantages.
**Key findings**:
- Partial client participation is common in real-world scenarios but has received limited attention compared to full client participation assumptions
- Existing research has focused more on addressing generalization, robustness, and fairness caused by data heterogeneity under full client participation assumptions
- The survey provides in-depth review of FL methods designed for partial client participation with theoretical and empirical support
- The paper offers a structured categorization of methods with their respective advantages and disadvantages
**Limitations**: Not stated in abstract

### Stricker et al. (2026)

**Research question**: How can performance evaluation in federated learning produce results consistent with centralized evaluation across different metrics beyond accuracy?
**Methodology**: The authors examine the reasons for discrepancies between participant-based and centralized evaluation in FL, then propose FLAM, a performance evaluation method based on aggregatable measures that yields the same results as centralized evaluation without requiring a global test dataset.
**Key findings**:
- Common aggregation strategies like weighted averaging based on local samples do not always produce the same results as centralized evaluation
- Existing performance evaluation definitions tailored to accuracy do not generalize to other metrics, leading to inconsistencies
- FLAM produces results matching centralized evaluation without needing a global test dataset
**Limitations**: Not stated in abstract

### Xia et al. (2025)

**Research question**: How can federated learning frameworks jointly provide differential privacy, Byzantine robustness, and communication efficiency without compromising any of these properties?
**Methodology**: The authors propose Fed-DPRoC, a framework introducing robust-compatible compression that reduces bi-directional communication overhead without undermining aggregation robustness, instantiated as RobAJoL integrating Johnson-Lindenstrauss-based compression with robust averaging, with theoretical analysis and simulations on CIFAR-10, Fashion MNIST, and FEMNIST.
**Key findings**:
- JL transform is compatible with robust averaging, maintaining both robustness guarantees and differential privacy
- RobAJoL substantially reduces communication overhead while preserving robustness and utility
- RobAJoL outperforms existing methods in robustness and utility under different Byzantine attacks
**Limitations**: Not stated in abstract

### Yashwanth et al. (2026)

**Research question**: How can federated learning sustain client participation when clients are rational agents who may prioritize local utility over global model performance?
**Methodology**: The authors introduce FedUCA, a framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation through utility-constrained stochastic aggregation, substantiated through extensive experiments on standard datasets.
**Key findings**:
- Clients in real-world cross-silo environments are often rational agents who may prioritize local model performance over global model performance
- In settings with significant statistical heterogeneity, rational clients may opt out of the federation if perceived benefits fail to meet local utility thresholds
- Client attrition degrades global model performance and can lead to the collapse of the federated training process
- FedUCA achieves significantly higher client retention and superior global model performance by prioritizing participation feasibility
**Limitations**: Not stated in abstract

## References

Banik, A., de Carvalho, G. H. S., & Dividino, R. (2025). Federated learning with graph-based aggregation for traffic forecasting. arXiv. https://arxiv.org/abs/2507.09805

Düsing, C., & Cimiano, P. (2025). Distribution-controlled client selection to improve federated learning strategies. arXiv. https://arxiv.org/abs/2509.20877

Hewa Kaluannakkage, C. A. S., & Buyya, R. (2025). Incentive-based federated learning: Architectural elements and future directions. arXiv. https://arxiv.org/abs/2510.14208

Ho, E. S. L. (2026). Uncertainty-aware federated learning for infant movement analysis. arXiv. https://arxiv.org/abs/2609.31463

Kritharakis, E., Jakovetic, D., Makris, A., & Tserpes, K. (2025). Robust federated learning under adversarial attacks via loss-based client clustering. arXiv. https://arxiv.org/abs/2508.12672

Németh, G. D., Fanì, E., Ng, Y. J., Caputo, B., Lozano, M. Á., Oliver, N., & Quadrianto, N. (2025). FedDiverse: Tackling data heterogeneity in federated learning with diversity-driven client selection. arXiv. https://arxiv.org/abs/2504.11216

Sen, M., Aparna, S., Agarwal, R., & Mohan, C. K. (2025). Overcoming challenges of partial client participation in federated learning: A comprehensive review. arXiv. https://arxiv.org/abs/2506.02887

Stricker, F., Peregrina, J. A., Bermbach, D., & Zirpins, C. (2026). FLAM: Evaluating model performance with aggregatable measures in federated learning. arXiv. https://arxiv.org/abs/2605.07962

Xia, Y., Jahani-Nezhad, T., & Bitar, R. (2025). Beyond trade-offs: A unified framework for privacy, robustness, and communication efficiency in federated learning. arXiv. https://arxiv.org/abs/2508.12978

Yashwanth, M., Singh, A., Nayak, A., Bulusu, S. K., & Chakraborty, A. (2026). Federated learning by utility-constrained stochastic aggregation for improving rational participation. arXiv. https://arxiv.org/abs/2605.18020
