# Systematic Literature Review: Federated Learning

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "federated learning", category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers (2025-2026) on federated learning (FL) within the cs.LG category. The surveyed literature reveals a field maturing beyond foundational algorithms toward addressing practical deployment challenges. Key research directions include incentive mechanisms for sustainable participation, handling data heterogeneity through intelligent client selection, robustness against adversarial attacks, and domain-specific applications in healthcare and traffic forecasting. The collective work demonstrates that successful FL systems require careful attention to participant rationality, statistical heterogeneity, privacy-robustness-communication trade-offs, and evaluation methodologies that align with centralized benchmarks. Notably, recent work increasingly focuses on real-world constraints such as partial client participation, Byzantine attacks with minimal trusted parties, and uncertainty quantification in sensitive domains.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "federated learning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Incentive Mechanisms and Rational Participation

A prominent thread across recent FL research addresses the fundamental challenge of sustaining client participation when clients are rational agents who may prioritize local utility over global model performance. Hewa Kaluannakkage and Buyya (2025) establish that participating entities are often unwilling to contribute to federated learning unless they receive benefits, or they may free-ride on others' contributions. Their comprehensive taxonomy examines incentive mechanisms drawing from economics, game theory, and technology-driven solutions like blockchain and deep reinforcement learning, arguing that well-designed incentive mechanisms are essential components for practical FL success, not merely optional features.

Building on this foundation, Yashwanth et al. (2026) introduce FedUCA, a framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation. Their work demonstrates that in settings with significant statistical heterogeneity, rational clients may opt out of the federation if perceived benefits fail to meet their local utility thresholds, leading to client attrition that degrades global model performance and can cause the federated training process to collapse. By prioritizing participation feasibility, FedUCA achieves significantly higher client retention and superior global model performance.

### Theme 2: Managing Data Heterogeneity Through Client Selection

Statistical data heterogeneity—where client data is non-identically distributed and imbalanced—represents a core challenge impacting generalization, slowing convergence, and reducing performance in FL. Németh et al. (2025) propose characterizing this heterogeneity using 6 metrics of global and client attribute imbalance, class imbalance, and spurious correlations. Their FEDDIVERSE algorithm manages and leverages data heterogeneity across clients by promoting collaboration between clients with complementary data distributions, achieving improvements with low communication and computational overhead.

Düsing and Cimiano (2025) extend this line of work by proposing distribution-controlled client selection that aligns active clients' label distributions with either a balanced distribution or the federation's combined label distribution. Their empirical validation reveals that aligning with a balanced distribution yields the greatest improvements when facing local imbalance, while alignment with the federation's combined label distribution is superior for handling global imbalance. Together, these works establish client selection as a critical lever for managing heterogeneity.

### Theme 3: Robustness Against Adversarial Attacks

As FL deployments expand, robustness against Byzantine attacks has become increasingly critical. Xia et al. (2025) propose Fed-DPRoC, a unified framework that jointly provides differential privacy, Byzantine robustness, and communication efficiency without trade-offs. Their instantiation, RobAJoL, integrates Johnson-Lindenstrauss-based compression with robust averaging, maintaining robustness guarantees while satisfying differential privacy requirements and substantially reducing communication overhead.

Kritharakis et al. (2025) push robustness further by proposing a loss-based client clustering approach that requires only two honest participants (the server and one client) to function effectively against Byzantine attacks, without prior knowledge of the number of malicious clients. Their theoretical analysis demonstrates bounded optimality gaps even under strong Byzantine attacks, and their algorithm significantly outperforms standard and robust FL baselines (Mean, Trimmed Mean, Median, Krum, Multi-Krum) under various attack strategies including label flipping, sign flipping, and Gaussian noise addition.

### Theme 4: Domain-Specific Applications and Evaluation Methods

Recent FL research increasingly addresses domain-specific challenges and evaluation methodologies. Ho (2026) presents the first federated learning framework for automated infant movement analysis using skeletal motion data, employing Monte Carlo Dropout to estimate predictive uncertainty and proposing Uncertainty-Aware Federated Averaging (UA-FedAvg) that incorporates predictive entropy into the federated aggregation process. This work demonstrates that FL substantially improves classification performance compared with independently trained local models while achieving performance approaching centralized training, addressing privacy and data-sharing constraints that make centralized training impractical in clinical settings.

For traffic forecasting, Banik et al. (2025) propose a lightweight graph-aware FL approach that blends Federated Averaging with graph learning principles, applying neighborhood aggregation to guide parameter updates by weighting client models based on graph connectivity. Their method captures spatial relationships between clients effectively while remaining computationally efficient.

On evaluation methodology, Stricker et al. (2026) examine discrepancies between participant-based and centralized evaluation in FL, proposing FLAM, a performance evaluation method based on aggregatable measures that yields the same results as centralized evaluation without requiring a global test dataset. Their work addresses a critical gap: common aggregation strategies like weighted averaging do not always produce the same results as centralized evaluation, and existing performance evaluation definitions are largely tailored to accuracy and do not generalize to other metrics.

### Theme 5: Partial Client Participation

While much existing FL research focuses on data heterogeneity under full client participation, Sen et al. (2025) highlight that partial client participation is common in real-world scenarios and presents distinct practical and theoretical challenges. Their comprehensive review provides a structured categorization of existing FL methods designed to cope with partial client participation, offering analysis supported by theoretical insights and empirical findings. This work establishes that limited attention has been given to challenges arising from partial participation relative to the extensive work on data heterogeneity, marking an important direction for future research.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key points. First, multiple papers establish that client participation cannot be assumed—clients are rational agents who require incentives or sufficient local utility to remain engaged (Hewa Kaluannakkage & Buyya, 2025; Yashwanth et al., 2026). Second, there is consensus that statistical heterogeneity fundamentally impacts FL performance and requires explicit management through client selection or aggregation strategies (Németh et al., 2025; Düsing & Cimiano, 2025). Third, the literature agrees that robustness and privacy must be addressed jointly rather than in isolation (Xia et al., 2025; Kritharakis et al., 2025). Finally, multiple works converge on the importance of evaluation methods that align with centralized benchmarks (Stricker et al., 2026).

**Disagreements**: The surveyed papers do not exhibit fundamental disagreements but rather focus on different aspects of FL challenges. The primary divergence lies in approach: some works emphasize incentive design and participation feasibility (Hewa Kaluannakkage & Buyya, 2025; Yashwanth et al., 2026), while others focus on algorithmic robustness (Xia et al., 2025; Kritharakis et al., 2025) or heterogeneity management (Németh et al., 2025; Düsing & Cimiano, 2025). These represent complementary rather than conflicting perspectives.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are not a focus of current FL research communication or that they are discussed only in full paper text. Second, while robustness against Byzantine attacks receives significant attention, the intersection of robustness with domain-specific constraints (e.g., clinical settings with strict privacy requirements) remains underexplored beyond Ho's (2026) work on infant movement analysis. Third, the evaluation gap identified by Stricker et al. (2026)—that common aggregation strategies do not match centralized evaluation—suggests that many existing FL benchmarks may not reflect true performance, raising questions about the validity of prior comparative studies. Finally, Sen et al.'s (2025) observation that partial participation receives limited attention relative to full-participation scenarios indicates a significant gap between research assumptions and real-world deployment conditions.

## Per-Paper Annotations

### Banik et al. (2025)

**Research question**: How can federated learning methods be improved for traffic prediction tasks where spatial relationships between clients are important?
**Methodology**: The authors propose a lightweight graph-aware FL approach that blends Federated Averaging (FedAvg) with graph learning principles, applying neighborhood aggregation to guide parameter updates by weighting client models based on graph connectivity, evaluated on METR-LA and PEMS-BAY datasets.
**Key findings**:
- The graph-aware FL approach captures spatial relationships between clients effectively
- The method achieves competitive performance compared to standard baselines and recent graph-based federated learning techniques
- The approach remains computationally efficient while introducing graph-based aggregation
**Limitations**: Not stated in abstract

### Düsing and Cimiano (2025)

**Research question**: How can client selection methods in federated learning be improved to mitigate the detrimental effects of data imbalance among clients?
**Methodology**: The authors propose an extension to existing FL strategies that selects active clients based on aligning their label distribution with either a balanced distribution or the federation's combined label distribution, empirically validated on three common FL strategies and two datasets.
**Key findings**:
- Aligning the label distribution with a balanced distribution yields the greatest improvements when facing local imbalance
- Alignment with the federation's combined label distribution is superior for handling global imbalance
- The proposed client selection method enhances existing FL strategies by addressing data imbalance issues
**Limitations**: Not stated in abstract

### Hewa Kaluannakkage and Buyya (2025)

**Research question**: How can incentive mechanisms be designed to address the participation dilemma in federated learning systems?
**Methodology**: This work presents a comprehensive taxonomy covering both centralized and decentralized architectures based on foundational concepts from economics, game theory, and technology-driven solutions like blockchain and deep reinforcement learning, examined from an application perspective.
**Key findings**:
- Participating entities are often unwilling to contribute to federated learning unless they receive benefits, or they may free-ride on others' contributions
- Foundational concepts from economics and game theory can be applied alongside technology-driven solutions such as blockchain and deep reinforcement learning to design incentive mechanisms
- Well-designed incentive mechanisms are essential components for the practical success of federated learning, not merely optional features
- The analysis reveals both promising solutions that have emerged and significant challenges remaining in building sustainable, fair, and robust federated learning ecosystems
**Limitations**: Not stated in abstract

### Ho (2026)

**Research question**: How can federated learning be applied to automated infant movement analysis while addressing privacy constraints and quantifying model confidence?
**Methodology**: The paper presents the first federated learning framework for automated infant movement analysis using skeletal motion data, employing Monte Carlo Dropout to estimate predictive uncertainty and proposing an Uncertainty-Aware Federated Averaging (UA-FedAvg) strategy that incorporates predictive entropy into the federated aggregation process.
**Key findings**:
- Federated learning substantially improves classification performance compared with independently trained local models while achieving performance approaching that of centralized training
- UA-FedAvg and its variant incorporating validation loss generally outperform conventional FedAvg across the evaluated data-split configurations
- The framework addresses privacy, governance, and data-sharing constraints that make centralized training impractical in clinical settings
- Monte Carlo Dropout enables quantification of model confidence by estimating predictive uncertainty during inference
**Limitations**: Not stated in abstract

### Kritharakis et al. (2025)

**Research question**: How can federated learning remain robust against adversarial (Byzantine) attacks when only minimal trusted participants are available?
**Methodology**: The authors propose a loss-based client clustering approach that requires only two honest participants (the server and one client) to function effectively, without prior knowledge of the number of malicious clients, with theoretical analysis demonstrating bounded optimality gaps and evaluation across MNIST, FMNIST, and CIFAR-10 benchmarks using the Flower framework.
**Key findings**:
- The approach requires only two honest participants to function effectively against Byzantine attacks
- Theoretical analysis demonstrates bounded optimality gaps even under strong Byzantine attacks
- The algorithm significantly outperforms standard and robust FL baselines (Mean, Trimmed Mean, Median, Krum, Multi-Krum) under various attack strategies including label flipping, sign flipping, and Gaussian noise addition
**Limitations**: Not stated in abstract

### Németh et al. (2025)

**Research question**: How can statistical data heterogeneity in federated learning be characterized and managed to improve model generalization and convergence?
**Methodology**: The authors propose characterizing statistical data heterogeneity using 6 metrics of global and client attribute imbalance, class imbalance, and spurious correlations; create and share 7 computer vision datasets covering a broad range of heterogeneity; and propose FEDDIVERSE, a client selection algorithm designed to manage and leverage data heterogeneity by promoting collaboration between clients with complementary data distributions.
**Key findings**:
- Client data in real-world FL settings is often non-identically distributed and imbalanced, resulting in statistical data heterogeneity that impacts generalization, slows convergence, and reduces performance
- FEDDIVERSE is designed to manage and leverage data heterogeneity across clients by promoting collaboration between clients with complementary data distributions
- Experiments on seven proposed FL datasets demonstrate FEDDIVERSE's effectiveness in enhancing the performance and robustness of various FL methods
- FEDDIVERSE achieves its improvements while having low communication and computational overhead
**Limitations**: Not stated in abstract

### Sen et al. (2025)

**Research question**: What are the practical and theoretical challenges arising from partial client participation in federated learning, and how do existing methods address them?
**Methodology**: This survey provides an extensive review of existing FL methods designed to cope with partial client participation, offering comprehensive analysis supported by theoretical insights and empirical findings, along with a structured categorization highlighting respective advantages and disadvantages.
**Key findings**:
- While much existing research focuses on data heterogeneity issues under full client participation, limited attention has been given to challenges arising from partial client participation
- Partial client participation is common in real-world scenarios and presents distinct practical and theoretical challenges
- The survey provides a structured categorization of existing FL methods designed to cope with partial client participation
- The analysis highlights the respective advantages and disadvantages of different approaches to handling partial client participation
**Limitations**: Not stated in abstract

### Stricker et al. (2026)

**Research question**: How can performance evaluation in federated learning be improved to produce results consistent with centralized evaluation across different metrics?
**Methodology**: The authors examine the reasons for discrepancies between participant-based and centralized evaluation in FL, and propose FLAM, a performance evaluation method based on aggregatable measures that yields the same results as centralized evaluation without requiring a global test dataset.
**Key findings**:
- Common aggregation strategies like weighted averaging do not always produce the same results as centralized evaluation
- Existing performance evaluation definitions are largely tailored to accuracy and do not generalize to other metrics
- FLAM provides aggregatable measures that match centralized evaluation results without needing a global test dataset
**Limitations**: Not stated in abstract

### Xia et al. (2025)

**Research question**: How can federated learning jointly provide differential privacy, Byzantine robustness, and communication efficiency without trade-offs?
**Methodology**: The authors propose Fed-DPRoC, a framework based on robust-compatible compression that reduces bi-directional communication overhead without undermining robustness, instantiated as RobAJoL integrating Johnson-Lindenstrauss-based compression with robust averaging, validated through theoretical analysis and simulations on CIFAR-10, Fashion MNIST, and FEMNIST.
**Key findings**:
- RobAJoL maintains robustness guarantees while satisfying differential privacy requirements
- The framework substantially reduces communication overhead compared to existing methods
- RobAJoL outperforms state-of-the-art communication-efficient and robust FL schemes in terms of robustness and utility under different Byzantine attacks
**Limitations**: Not stated in abstract

### Yashwanth et al. (2026)

**Research question**: How can federated learning sustain client participation when clients are rational agents who may prioritize their local utility over global model performance?
**Methodology**: The authors introduce FedUCA, a framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation, and substantiate it through extensive experiments on standard datasets.
**Key findings**:
- In real-world cross-silo environments, clients are often rational agents who may prioritize local model performance over global model performance
- In settings with significant statistical heterogeneity, rational clients may opt out of the federation if perceived benefits fail to meet their local utility thresholds
- Client attrition degrades global model performance and can lead to the collapse of the federated training process
- By prioritizing participation feasibility, FedUCA achieves significantly higher client retention and superior global model performance
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
