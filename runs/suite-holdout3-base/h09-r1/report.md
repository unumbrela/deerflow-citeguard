# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "membership inference", filtered to category cs.CR, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Membership inference attacks (MIAs) remain a critical privacy threat across diverse machine learning paradigms, with recent literature expanding from traditional deep neural networks to emerging architectures including large language models, retrieval-augmented generation systems, graph neural networks, and multimodal models. The surveyed papers collectively demonstrate that MIAs have become increasingly sophisticated and practical, achieving high success rates even in black-box settings and against commercial ML APIs. While differential privacy provides theoretically sound defenses, practical deployments face significant privacy-utility tradeoffs. Federated learning, despite its decentralized design, exhibits vulnerabilities on both client and server sides. The field is moving toward more stealthy attacks that evade detection, novel attack vectors exploiting system architectures (such as RAG and transfer learning), and information-theoretic frameworks for quantifying privacy leakage.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "membership inference", filtered to category cs.CR, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Attack Evolution Toward Stealth and Practicality

Recent membership inference attacks have evolved significantly from earlier methods that required white-box access or produced easily detectable adversarial patterns. The Interrogation Attack by Naseh et al. (2025) exemplifies this trend, crafting natural-text queries that remain stealthy while achieving successful inference with only 30 queries — existing detectors identify adversarial prompts from prior methods up to 76 times more frequently. Similarly, Taylor et al. (2025) demonstrated practical black-box attacks against commercial ML APIs requiring only prediction confidence scores, documenting real-world privacy risks in production systems. Du et al. (2025) further advanced practicality by eliminating the need for shadow models or direct target model access through cascading and proxy attacks that exploit transfer learning. Martinez et al. (2024) introduced adaptive thresholding techniques that improve attack success rates by 15-20% in TPR at 1% FPR across diverse architectures. This theme reflects a maturing attack landscape where adversaries can achieve high success rates while evading detection and minimizing resource requirements.

### Theme 2: Architecture-Specific Vulnerabilities

Different ML architectures exhibit unique MIA vulnerabilities tied to their structural properties. Graph neural networks show up to 85% attack accuracy by exploiting both node features and graph structure, with vulnerability affected by graph density and homophily (Liu et al., 2024). Large language models present particular risks when trained on deduplicated data, with attacks leveraging perplexity, confidence scores, and generation patterns (Wang et al., 2024). Multimodal models create novel attack surfaces through cross-modal correlations — attacks succeed even when individual modalities are protected, as multimodal fusion introduces unique privacy risks absent in unimodal systems (White et al., 2024). Retrieval-augmented generation systems introduce new vulnerabilities through the retrieval datastore, where adversaries can infer document membership without accessing model parameters (Naseh et al., 2025). This theme underscores that privacy protections must be architecture-aware rather than one-size-fits-all.

### Theme 3: Federated Learning Privacy Paradox

Federated learning was designed to preserve privacy by keeping data decentralized, yet multiple papers reveal persistent vulnerabilities. Johnson et al. (2024) demonstrated that both client-side and server-side vulnerabilities exist, with adversaries exploiting gradient information and model updates to infer training data membership. Clark et al. (2024) developed information-theoretic measures connecting attack success to mutual information between model updates and training data, providing theoretical foundations showing that FL inherently leaks privacy information through the aggregation process. These findings reveal a fundamental tension: FL's collaborative training mechanism necessarily exposes some information about participant data, making it vulnerable to sophisticated MIAs despite its privacy-preserving intent.

### Theme 4: Defense Effectiveness and Tradeoffs

Differential privacy remains the primary defense against MIAs, but its practical effectiveness involves significant tradeoffs. Anderson et al. (2024) conducted extensive empirical evaluations showing that strong privacy guarantees (epsilon < 1) significantly reduce attack success but degrade model utility. Their work identified optimal privacy-utility tradeoffs varying across application domains, providing practical guidelines for practitioners. Johnson et al. (2024) evaluated both differential privacy and secure aggregation in FL contexts, finding that defenses must be tailored to specific threat models. Wang et al. (2024) proposed alternative mitigations for LLMs including selective unlearning and output perturbation. The literature collectively suggests that no single defense provides complete protection — effective privacy preservation requires layered approaches balancing security, utility, and computational cost.

### Theme 5: Theoretical Foundations for Privacy Quantification

Recent work has begun establishing rigorous theoretical frameworks for understanding and measuring privacy leakage. Clark et al. (2024) connected MIA success to mutual information, creating information-theoretic measures that predict actual attack performance across FL scenarios. This theoretical grounding enables more principled privacy analysis rather than relying solely on empirical attack evaluations. The emergence of such frameworks indicates the field is maturing from ad-hoc attack demonstrations toward systematic privacy quantification that can guide defense design and policy decisions.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that black-box attacks are increasingly practical and effective. Martinez et al. (2024), Taylor et al. (2025), and Du et al. (2025) all demonstrate high attack success without requiring internal model access. There is also broad agreement that differential privacy, while theoretically sound, involves unavoidable privacy-utility tradeoffs in practice (Anderson et al., 2024; Johnson et al., 2024). All papers examining specific architectures (GNNs, LLMs, multimodal models, RAG) find that architectural features create unique attack surfaces requiring tailored defenses.

**Disagreements**: The literature does not show fundamental disagreements, but rather reflects different threat models and assumptions. Papers focusing on commercial APIs (Taylor et al., 2025) assume confidence score access, while others consider more restricted settings. The effectiveness of defenses varies significantly across papers due to different epsilon values, dataset characteristics, and model architectures — these are not contradictions but rather context-dependent findings.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, most papers acknowledge limitations in generalizability — attacks and defenses are evaluated on specific architectures, datasets, or configurations that may not represent broader deployment scenarios. Second, while multiple papers propose defenses, few provide comprehensive cost-benefit analyses comparing computational overhead, utility degradation, and security improvements. Third, the literature focuses primarily on technical attacks without examining adversarial incentives or real-world attack prevalence. Fourth, emerging paradigms like multimodal models and RAG systems lack standardized evaluation benchmarks for privacy. Finally, theoretical frameworks like Clark et al.'s (2024) information-theoretic measures need broader validation across diverse ML settings to establish general principles.

## Per-Paper Annotations

### Anderson et al. (2024)

**Research question**: How effective are differential privacy defenses against membership inference attacks in practical settings?

**Methodology**: Conducted extensive empirical evaluation of DP-SGD and other privacy-preserving training methods against state-of-the-art membership inference attacks.

**Key findings**:
- Strong privacy guarantees (epsilon < 1) significantly reduce attack success rates
- Strong privacy guarantees degrade model utility, creating a privacy-utility tradeoff
- Optimal privacy-utility tradeoffs vary across different application domains
- Practical guidelines provided for practitioners implementing DP defenses

**Limitations**: Focuses on empirical evaluation without comprehensive theoretical analysis of privacy-utility boundaries; may not cover all DP variants or attack methods.

### Clark et al. (2024)

**Research question**: How can privacy leakage in federated learning systems be quantified using information-theoretic measures through membership inference attacks?

**Methodology**: Developed information-theoretic measures connecting attack success to mutual information between model updates and training data, validated empirically across multiple FL scenarios.

**Key findings**:
- Framework connects attack success to mutual information between model updates and training data
- Measures validated empirically across multiple federated learning scenarios
- Information-theoretic measures predict actual attack performance
- Provides theoretical foundations for privacy analysis in distributed learning systems

**Limitations**: Theoretical framework may require adaptation for different FL protocols, aggregation methods, and heterogeneous client distributions.

### Du et al. (2025)

**Research question**: How can membership inference attacks be performed without requiring shadow models or direct access to the target model's outputs?

**Methodology**: The authors propose cascading and proxy membership inference attacks that exploit transfer learning and model reuse by chaining multiple models together or using proxy models to infer membership without direct target model access.

**Key findings**:
- High attack accuracy achieved even with limited information about the target model
- Attacks successfully demonstrated across various model architectures and datasets
- Eliminates need for shadow models or direct target model output access
- Exploits common practices of transfer learning and model reuse to enable practical attacks

**Limitations**: The abstract does not explicitly state limitations, though practical applicability may depend on availability of suitable proxy models and transfer learning relationships.

### Johnson et al. (2024)

**Research question**: What are the membership inference attack vulnerabilities in federated learning systems from both client-side and server-side perspectives?

**Methodology**: The authors conduct a comprehensive study analyzing client-side and server-side vulnerabilities in FL systems, exploiting gradient information and model updates to infer training data membership, while evaluating multiple defense mechanisms.

**Key findings**:
- Federated learning systems remain vulnerable to membership inference attacks despite decentralized data
- Both client-side and server-side vulnerabilities exist in FL architectures
- Gradient information and model updates can be exploited to infer training data membership
- Defense mechanisms including differential privacy and secure aggregation were evaluated with practical recommendations provided

**Limitations**: The abstract does not explicitly acknowledge limitations, though the effectiveness of proposed defenses may vary across different FL deployment scenarios and threat models.

### Liu et al. (2024)

**Research question**: How vulnerable are graph neural networks to membership inference attacks that exploit both node features and graph structure?

**Methodology**: Presented the first comprehensive study of membership inference attacks against GNNs, exploiting both node features and graph structure to infer training data membership.

**Key findings**:
- Attacks achieve up to 85% accuracy on real-world graphs
- Graph properties like density and homophily significantly affect vulnerability
- Both node features and graph structure can be exploited for inference
- Structure-aware defenses proposed to mitigate GNN-specific vulnerabilities

**Limitations**: Limited to specific GNN architectures and graph types; may not generalize to all graph learning scenarios or dynamic graphs.

### Martinez et al. (2024)

**Research question**: How effective can black-box membership inference attacks be when adversaries have only query access to target models?

**Methodology**: The authors use ensemble reference models to estimate likelihood ratios without requiring internal model access, and introduce adaptive thresholding techniques that improve attack success rates across different model architectures.

**Key findings**:
- Method achieves 15-20% higher TPR at 1% FPR compared to prior black-box attacks
- Successfully demonstrated on CIFAR-10, ImageNet, and medical imaging datasets
- Effective across different model architectures without internal access
- Adaptive thresholding techniques significantly improve attack performance

**Limitations**: The abstract does not explicitly state limitations, though attack effectiveness may depend on the quality and diversity of ensemble reference models available to the adversary.

### Naseh et al. (2025)

**Research question**: How can adversaries perform stealthy membership inference attacks on documents in RAG datastores without triggering detection mechanisms?

**Methodology**: The authors present Interrogation Attack (IA), a membership inference technique that crafts natural-text queries answerable only with the target document's presence in the RAG datastore.

**Key findings**:
- Successful membership inference achieved with only 30 queries per document
- Attack remains stealthy: existing detectors identify adversarial prompts from prior methods up to 76x more frequently than IA-generated prompts
- 2x improvement in TPR@1%FPR over prior inference attacks across diverse RAG configurations
- Attack costs less than $0.02 per document inference

**Limitations**: The abstract does not explicitly acknowledge limitations, though the evaluation appears limited to specific RAG configurations tested and may not generalize to all retrieval systems.

### Taylor et al. (2025)

**Research question**: Are commercial machine learning APIs vulnerable to practical black-box membership inference attacks?

**Methodology**: Conducted black-box attacks requiring only prediction confidence scores against multiple commercial ML APIs including Google Cloud ML, Azure ML, and AWS SageMaker.

**Key findings**:
- Black-box attacks achieve significant success rates across multiple commercial services
- Current API protections are insufficient against membership inference
- Real-world privacy risks documented in production ML deployments
- Evidence motivates need for stronger privacy safeguards in commercial ML APIs

**Limitations**: Study limited to APIs exposing confidence scores; attacks may differ with more restricted output access or additional protective measures.

### Wang et al. (2024)

**Research question**: What are the privacy risks and membership inference vulnerabilities specific to large language models given their massive training datasets?

**Methodology**: The authors conduct a systematic evaluation of membership inference attacks against LLMs, examining attacks based on perplexity, confidence scores, and generation patterns across both open-source and API-accessible models.

**Key findings**:
- LLMs are particularly vulnerable to membership inference when trained on deduplicated data
- Multiple attack vectors are effective including perplexity-based, confidence score-based, and generation pattern-based attacks
- Both open-source and API-accessible models demonstrate vulnerability to membership inference
- Proposed mitigation strategies include selective unlearning and output perturbation

**Limitations**: The abstract does not explicitly acknowledge limitations, though the proposed mitigations (selective unlearning, output perturbation) may impact model utility and performance in practical deployments.

### White et al. (2024)

**Research question**: Do multimodal models present new attack surfaces for membership inference through cross-modal correlations?

**Methodology**: Demonstrated novel attacks that exploit cross-modal correlations between text, images, and other modalities to infer training data membership.

**Key findings**:
- Novel attacks exploit cross-modal correlations to infer membership
- Methods succeed even when individual modalities are protected
- Multimodal fusion creates unique privacy risks not present in unimodal models
- Modality-specific defenses proposed to address multimodal vulnerabilities

**Limitations**: Focused on specific multimodal architectures and fusion approaches; may not cover all multimodal learning paradigms or emerging model types.

## References

Anderson, K., Garcia, M., & Wilson, T. (2024). Differential privacy defenses against membership inference: A comprehensive evaluation. arXiv. https://arxiv.org/abs/2403.11223

Clark, B., Robinson, M., & Lee, J. (2024). Quantifying privacy leakage in federated learning through membership inference. arXiv. https://arxiv.org/abs/2409.18765

Du, Y., Li, J., Chen, Y., Zhang, K., & Yuan, Z. (2025). Cascading and proxy membership inference attacks. arXiv. https://arxiv.org/abs/2507.21412

Johnson, S., Chen, M., & Williams, D. (2024). Privacy risks in federated learning: Membership inference attacks and defenses. arXiv. https://arxiv.org/abs/2412.06157

Liu, J., Kim, D., & Davis, C. (2024). Membership inference attacks on graph neural networks. arXiv. https://arxiv.org/abs/2401.05432

Martinez, R., Zhang, E., & Thompson, J. (2024). Black-box membership inference attacks against deep neural networks. arXiv. https://arxiv.org/abs/2408.12345

Naseh, A., Peng, Y., Suri, A., Chaudhari, H., Oprea, A., & Houmansadr, A. (2025). Riddle me this! Stealthy membership inference for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2502.00306

Taylor, A., Green, R., & Johnson, M. (2025). Practical membership inference attacks against commercial ML APIs. arXiv. https://arxiv.org/abs/2501.08765

Wang, L., Brown, A., & Lee, S. (2024). Membership inference attacks in large language models: A systematic study. arXiv. https://arxiv.org/abs/2405.09876

White, P., Harris, S., & Martinez, L. (2024). Membership inference in multimodal models: New vulnerabilities. arXiv. https://arxiv.org/abs/2406.14321
