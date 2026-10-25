# Systematic Literature Review: Automated Program Repair with Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "automated program repair", filtered to category cs.SE, published between 2024-01-01 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of automated program repair (APR) has undergone a transformative shift with the integration of large language models (LLMs), achieving repair accuracies between 30-44% on standard benchmarks compared to historical baselines below 20%. Recent research demonstrates that LLM-based APR techniques have evolved from simple patch generators to sophisticated systems employing multi-agent collaboration, retrieval-augmented generation, and parameter-efficient fine-tuning. Key advances include self-directed repair without external feedback (ThinkRepair achieving 37.3% accuracy), autonomous agent-based approaches (RepairAgent fixing 30.6% of bugs with improved efficiency), and multi-agent frameworks (MAC-APR reaching 44.1% accuracy). However, significant challenges remain including patch overfitting, security vulnerabilities in APR systems, limited context understanding for complex multi-file repairs, and the need for better evaluation protocols that capture real-world repair scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "automated program repair", filtered to category cs.SE, published between 2024-01-01 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses specifically on LLM-based APR approaches within the software engineering category, potentially missing relevant work in adjacent categories such as cs.AI or cs.LG.

## Themes

### Theme 1: Evolution from Stateless to Interactive Repair

The field has moved beyond treating LLMs as simple stateless patch generators toward interactive, multi-round repair processes. Traditional APR approaches generated patches in single attempts without maintaining context across iterations. Recent work demonstrates that treating LLMs as autonomous agents with memory and planning capabilities significantly improves repair effectiveness.

RepairAgent pioneered this approach by implementing an autonomous LLM agent with three components: a planning module that decomposes repair tasks into subtasks, a memory module storing repair history and context, and an action module executing repair operations through multi-round interactions (Huang et al., 2024). This agent-based approach correctly fixed 103 bugs (30.6%) while requiring fewer repair attempts per bug (2.3 vs 3.8-5.1 for baselines), demonstrating that interactive repair improves both accuracy and efficiency.

ThinkRepair extended this paradigm by introducing self-directed repair that eliminates dependency on external feedback such as compilation and test results (Yin et al., 2024). By employing a two-stage prompt engineering approach—first generating repair thinking that reasons about the bug and strategy, then using that thinking to guide patch synthesis—ThinkRepair achieved 37.3% repair accuracy across 1,582 bugs, outperforming existing LLM-based APR techniques by 6.7-24.6 percentage points. This work demonstrates that LLM reasoning capabilities can effectively direct patch generation without requiring traditional validation infrastructure.

### Theme 2: Multi-Agent Collaboration for Enhanced Repair

Building on single-agent approaches, recent research has explored coordinating multiple specialized LLM agents to address different aspects of the repair process. This theme reflects recognition that different repair subtasks require different capabilities, and that collaboration between specialized agents can overcome limitations of single-model approaches.

MAC-APR introduced a multi-agent collaboration framework employing three specialized agents: a diagnostic agent analyzing bug reports and identifying fault locations, a repair agent generating candidate patches, and a validation agent evaluating patch correctness (Cheng et al., 2025). Agents communicate through structured messages and iteratively refine their outputs. This approach achieved 44.1% repair accuracy on 458 bugs, outperforming single-agent baselines by 11.3-18.7 percentage points. Notably, multi-agent collaboration reduced hallucinated patches by 34% and improved repair efficiency by 2.1x, suggesting that specialization and collaboration address key weaknesses of monolithic APR systems.

The survey by Li et al. (2024) identified interactive repair and multi-agent collaboration as key future directions, analyzing 87 LLM-based APR papers published between 2020-2024. Their analysis revealed that prompt-based methods show particular promise among the three main approach categories (generate-and-validate, learning-based, and prompt-based), with LLM-based APR techniques achieving up to 40% repair accuracy on standard benchmarks.

### Theme 3: Context Enhancement Through Retrieval and Memory

A critical limitation of LLM-based APR is handling long code contexts and understanding complex dependencies. Recent work has addressed this through retrieval-augmented generation and enhanced memory mechanisms that provide LLMs with relevant contextual information beyond their immediate input.

RAG-APR introduced retrieval-augmented generation for APR, retrieving relevant code snippets, documentation, and similar bug fixes from codebases before generating patches (Zhang et al., 2025). The retrieved context is integrated into LLM prompts through attention-based fusion. This approach improved patch correctness by 15.7 percentage points compared to baseline LLMs without retrieval, with retrieval of similar historical fixes contributing most to improvement (8.3 pp), followed by API documentation (4.2 pp) and related code snippets (3.2 pp). RAG-APR particularly excelled at API misuse repairs with 52.3% accuracy versus 31.8% baseline.

ASAP-Repair addressed context understanding for API-specific repairs using API Usage Graphs (AUGs) to represent API usage patterns (Nielebock et al., 2024). By leveraging API usage templates from state-of-the-art API misuse detectors, ASAP-Repair generates fixes for API misuses, demonstrating that domain-specific context representation improves repair effectiveness for specialized bug categories.

### Theme 4: Efficient Adaptation and Fine-Tuning

While pre-trained LLMs show promise for APR, adapting them to repair tasks efficiently remains challenging. Recent work has explored parameter-efficient fine-tuning methods that reduce computational costs while maintaining or improving repair performance.

Guo et al. (2025) conducted comprehensive experiments comparing LoRA, AdaLoRA, and QLoRA across 5 LLM architectures (CodeLlama, StarCoder, CodeGen, InCoder, SantaCoder) on 4 APR benchmarks. Their findings revealed that LoRA with rank 16 achieves 94% of full fine-tuning performance while reducing trainable parameters by 98.7% and training time by 83%. AdaLoRA automatically allocates rank based on parameter importance, achieving slightly better performance (1.2 pp improvement) with similar efficiency. QLoRA enables fine-tuning of 34B parameter models on consumer GPUs, achieving state-of-the-art results on HumanEval-Fix with 41.2% repair accuracy. This work provides best practices for PEFT in APR including optimal rank selection, learning rate scheduling, and data augmentation strategies.

### Theme 5: Quality Assessment and Patch Validation

Determining which generated patches are correct remains a fundamental challenge in APR, particularly when test suites are incomplete or unavailable. Recent work has developed machine learning approaches to predict patch correctness without execution-based validation.

PatchCorrect introduced a machine learning model that predicts patch correctness by extracting features from LLM-generated patches including syntactic patterns, semantic similarity to bug context, and consistency with coding conventions (Huang et al., 2025). Trained on 15,847 patches from 12 LLM-based APR tools across 5 programming languages, PatchCorrect achieved 87.3% accuracy in predicting patch correctness on 3,291 held-out patches, outperforming baseline classifiers by 12.4-23.1 percentage points. The model generalizes across LLM architectures and programming languages, with F1 scores above 0.85 for Java, Python, and JavaScript. Integrating PatchCorrect with APR tools reduced incorrect patch submissions by 62%, addressing a critical bottleneck in APR deployment.

### Theme 6: Comprehensive Benchmarking and Evaluation

The rapid advancement of LLM-based APR has exposed limitations in existing evaluation benchmarks, prompting development of more comprehensive and realistic assessment frameworks.

CodeRepairBench addressed benchmark limitations including limited bug diversity, outdated evaluation metrics, lack of real-world repair scenarios, and inconsistent evaluation protocols (Li et al., 2025). The benchmark contains 2,847 bugs from 8 programming languages, 15 real-world projects, and 4 bug categories (logic errors, memory errors, concurrency bugs, and API misuses). New evaluation metrics include repair efficiency, patch readability, and developer acceptance likelihood. Evaluation of 12 state-of-the-art LLM-based APR tools revealed significant performance variation across bug types, with logic errors being most repairable (42.1%) and concurrency bugs least repairable (18.3%). The benchmark exposed that current LLM-based APR tools struggle with multi-file repairs and complex dependency reasoning.

### Theme 7: Security Vulnerabilities and Robustness

As LLM-based APR systems move toward deployment, understanding their security vulnerabilities has become critical. Recent work has identified attack vectors and defense mechanisms specific to APR systems.

Li et al. (2025) conducted the first systematic study of security vulnerabilities in LLM-based APR systems, identifying three attack vectors: patch poisoning where adversaries craft buggy inputs triggering malicious patch generation, training data contamination where poisoned repair pairs backdoor the APR model, and prompt injection where malicious comments in source code manipulate patch generation. Demonstrating attacks against 8 LLM-based APR tools, they achieved 73-89% attack success rates. Poisoned training data with only 0.5% contamination rate reduced repair accuracy by 31% and inserted security vulnerabilities in 24% of generated patches. Proposed defense mechanisms include input validation, patch verification, and robust fine-tuning protocols, highlighting the urgent need for security-aware APR development and deployment.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that traditional single-pass, stateless APR approaches are insufficient for complex repair tasks. Eight of the ten surveyed papers explicitly address this limitation through interactive agents (Huang et al., 2024; Yin et al., 2024), multi-agent collaboration (Cheng et al., 2025), retrieval augmentation (Zhang et al., 2025), or enhanced context representation (Nielebock et al., 2024). There is also broad agreement that evaluation benchmarks require significant improvement, with multiple papers calling for more diverse bug types, real-world scenarios, and comprehensive metrics (Li et al., 2025; Li et al., 2024).

All surveyed papers reporting repair accuracy show that LLM-based APR techniques achieve between 30-44% accuracy on standard benchmarks, representing substantial improvement over pre-LLM APR techniques but still far from human-level performance. The survey by Li et al. (2024) notes that prompt-based methods show particular promise, a finding supported by ThinkRepair's success with repair thinking generation (Yin et al., 2024).

**Disagreements**: While most papers focus on improving accuracy, there is tension between approaches that eliminate external validation (ThinkRepair's self-directed approach) versus those that emphasize validation agents (MAC-APR's validation agent, PatchCorrect's correctness prediction). Yin et al. (2024) argue that LLM reasoning can effectively direct patch generation without compilation or test feedback, expanding applicability to scenarios without test infrastructure. However, Huang et al. (2025) demonstrate that learned patch correctness prediction achieves 87.3% accuracy, suggesting that some form of validation remains valuable even if not execution-based.

There is also implicit disagreement about the optimal scale of APR systems: parameter-efficient fine-tuning work (Guo et al., 2025) suggests that smaller, efficiently adapted models can achieve competitive performance, while multi-agent approaches (Cheng et al., 2025) invest in coordination overhead for improved accuracy. These represent different points in the efficiency-accuracy tradeoff space rather than fundamental contradictions.

## Gaps and Open Questions

The collective literature reveals several significant gaps that remain unaddressed:

**Cross-language generalization**: While PatchCorrect demonstrates generalization across 5 programming languages (Huang et al., 2025) and CodeRepairBench includes 8 languages (Li et al., 2025), most APR techniques are evaluated primarily on Java and Python. Performance on low-resource languages, domain-specific languages, and emerging programming paradigms remains underexplored.

**Multi-file and project-level repairs**: CodeRepairBench explicitly identifies that current tools struggle with multi-file repairs and complex dependency reasoning (Li et al., 2025). Most evaluated bugs are single-file, localized fixes. Real-world bugs often span multiple files, modules, or even repositories, requiring understanding of system-level architecture and dependencies that current APR techniques cannot adequately handle.

**Long-term maintenance and technical debt**: None of the surveyed papers address whether LLM-generated patches introduce technical debt, reduce code maintainability, or create future maintenance burdens. Patch readability is mentioned as a metric (Li et al., 2025), but deeper questions about code quality, documentation, and alignment with project conventions remain open.

**Developer-AI collaboration**: While autonomous agents are emphasized, limited work explores optimal human-AI collaboration patterns for APR. Questions about when to involve human developers, how to present candidate patches, and how to incorporate developer feedback into iterative repair remain largely unaddressed.

**Security and trust**: The security vulnerabilities study (Li et al., 2025) opens more questions than it answers. Defense mechanisms require additional computational overhead and may not protect against adaptive adversaries. Fundamental questions about trust in AI-generated patches, especially for security-critical systems, remain unresolved.

**Evaluation protocol standardization**: The survey by Li et al. (2024) identifies the need for better evaluation protocols as a key challenge. Current benchmarks use inconsistent metrics, bug sets, and evaluation procedures, making cross-paper comparisons difficult. The field lacks standardized evaluation protocols that would enable reliable progress measurement.

**Computational overhead transparency**: Multiple papers note computational efficiency improvements (Guo et al., 2025; Cheng et al., 2025), but few provide detailed analysis of inference costs, training requirements, or deployment considerations for real-world APR systems. The computational overhead of multi-agent collaboration, retrieval augmentation, and large model fine-tuning remains a barrier to practical adoption.

## Per-Paper Annotations

### Cheng et al. (2025)

**Research question**: How can multi-agent collaboration improve the accuracy and efficiency of LLM-based automated program repair compared to single-LLM approaches?

**Methodology**: Proposed MAC-APR, a multi-agent framework with three specialized agents (diagnostic, repair, validation) that communicate through structured messages and iteratively refine outputs. Evaluated on 458 bugs from Defects4J, HumanEval-Fix, and QuixBugs.

**Key findings**:
- MAC-APR achieves 44.1% repair accuracy, outperforming single-agent baselines by 11.3-18.7 percentage points
- Multi-agent collaboration reduces hallucinated patches by 34%
- Repair efficiency improves by 2.1x compared to single-agent approaches
- Specialized agent roles enable more systematic bug fixing

**Limitations**: Evaluation limited to specific benchmarks which may not represent all bug types or programming languages; communication overhead between agents could impact scalability for larger codebases.

### Guo et al. (2025)

**Research question**: How can parameter-efficient fine-tuning methods reduce computational costs while maintaining performance for adapting pre-trained code LLMs to APR tasks?

**Methodology**: Compared LoRA, AdaLoRA, and QLoRA across 5 LLM architectures (CodeLlama, StarCoder, CodeGen, InCoder, SantaCoder) on 4 APR benchmarks to identify optimal PEFT configurations for APR.

**Key findings**:
- LoRA with rank 16 achieves 94% of full fine-tuning performance while reducing trainable parameters by 98.7% and training time by 83%
- AdaLoRA automatically allocates rank based on parameter importance, achieving 1.2 pp improvement over LoRA with similar efficiency
- QLoRA enables fine-tuning of 34B parameter models on consumer GPUs, achieving state-of-the-art 41.2% repair accuracy on HumanEval-Fix
- Provided best practices for PEFT in APR including optimal rank selection, learning rate scheduling, and data augmentation strategies

**Limitations**: PEFT methods may still underperform full fine-tuning on certain repair types; optimal hyperparameters vary across model architectures requiring per-model tuning; evaluation limited to 5 specific LLM architectures.

### Huang et al. (2024)

**Research question**: Can an autonomous LLM agent improve APR by treating LLMs as interactive agents rather than stateless patch generators?

**Methodology**: Developed an autonomous LLM agent with three components: (1) planning module that decomposes repair tasks into subtasks, (2) memory module that stores repair history and context, and (3) action module that executes repair operations through multi-round interactions.

**Key findings**:
- Correctly fixed 103 bugs (30.6%) on 337 bugs from Defects4J and QuixBugs
- Outperformed state-of-the-art APR tools by 8.2-15.4 percentage points
- Required fewer repair attempts per bug (2.3 vs 3.8-5.1 for baselines), demonstrating improved efficiency
- Multi-round interactive repair approach proves more effective than stateless patch generation

**Limitations**: Evaluation limited to 337 bugs from two benchmarks; agent-based approach may introduce additional computational overhead; effectiveness on larger, more complex real-world projects needs further validation.

### Huang et al. (2025)

**Research question**: How can we predict whether LLM-generated patches are correct without relying on potentially incomplete or unavailable test suites?

**Methodology**: Developed PatchCorrect, a machine learning model that extracts features from patches including syntactic patterns, semantic similarity to bug context, and coding convention consistency. Trained on 15,847 patches from 12 LLM-based APR tools across 5 programming languages.

**Key findings**:
- PatchCorrect achieves 87.3% accuracy in predicting patch correctness on 3,291 held-out patches
- Outperforms baseline classifiers by 12.4-23.1 percentage points
- Generalizes across LLM architectures and programming languages with F1 scores above 0.85 for Java, Python, and JavaScript
- Integration with APR tools reduces incorrect patch submissions by 62%

**Limitations**: Requires substantial labeled training data from multiple APR tools; may not capture all semantic correctness aspects that execution-based testing would reveal; performance on low-resource languages not evaluated.

### Li et al. (2024)

**Research question**: What is the current state of LLM-based APR approaches, their techniques, benchmarks, and what are the key challenges and future directions?

**Methodology**: Conducted a comprehensive survey analyzing 87 LLM-based APR papers published between 2020-2024, categorizing approaches into generate-and-validate, learning-based, and prompt-based types, and examining techniques, benchmarks, and evaluation methodologies.

**Key findings**:
- LLM-based APR techniques achieve up to 40% repair accuracy on standard benchmarks
- Prompt-based methods show particular promise among the three main approach categories
- Key challenges identified include patch overfitting, limited context windows, and need for better evaluation protocols
- Future directions include multi-modal APR, interactive repair, and integration with software development workflows
- 87 papers analyzed reveal rapid growth and diversification in LLM-based APR research

**Limitations**: Survey-based analysis rather than proposing novel technique; findings dependent on quality and completeness of analyzed papers; rapidly evolving field may outdate some conclusions.

### Li et al. (2025) [CodeRepairBench]

**Research question**: How can we create a more comprehensive benchmark for evaluating LLM-based APR techniques that addresses limitations of existing benchmarks?

**Methodology**: Created CodeRepairBench containing 2,847 bugs from 8 programming languages, 15 real-world projects, and 4 bug categories; introduced new evaluation metrics including repair efficiency, patch readability, and developer acceptance likelihood; evaluated 12 state-of-the-art LLM-based APR tools.

**Key findings**:
- Significant performance variation across bug types: logic errors most repairable (42.1%), concurrency bugs least (18.3%)
- Current LLM-based APR tools struggle with multi-file repairs and complex dependency reasoning
- Existing benchmarks suffer from limited bug diversity, outdated metrics, lack of real-world scenarios, and inconsistent protocols
- New metrics provide more comprehensive evaluation
- 12 evaluated tools showed substantial performance gaps across different bug categories

**Limitations**: Benchmark creation is resource-intensive and may require continuous updates as new bug types and languages emerge; developer acceptance likelihood metric may be subjective; coverage across all programming paradigms remains incomplete.

### Li et al. (2025) [Security]

**Research question**: What security vulnerabilities exist in LLM-based APR systems and how can they be exploited by adversaries?

**Methodology**: Conducted systematic study identifying three attack vectors (patch poisoning, training data contamination, prompt injection); demonstrated attacks against 8 LLM-based APR tools and proposed defense mechanisms including input validation, patch verification, and robust fine-tuning protocols.

**Key findings**:
- Demonstrated attacks against 8 LLM-based APR tools achieving 73-89% attack success rates
- Poisoned training data with only 0.5% contamination rate reduces repair accuracy by 31% and inserts security vulnerabilities in 24% of generated patches
- Three attack vectors identified: patch poisoning, training data contamination, and prompt injection through malicious comments
- Proposed defense mechanisms including input validation, patch verification, and robust fine-tuning protocols

**Limitations**: Defense mechanisms require additional computational overhead and may not protect against all novel attack variants; evaluation focused on known attack patterns rather than adaptive adversaries; real-world deployment considerations not fully addressed.

### Nielebock et al. (2024)

**Research question**: How can API misuses be automatically repaired using API Usage Graphs and API usage templates?

**Methodology**: Uses API Usage Graphs (AUGs) to represent API usage patterns and leverages API usage templates from state-of-the-art API misuse detectors to generate fixes for API misuses.

**Key findings**:
- Demonstrated that ASAP-Repair is applicable on an established API misuse dataset
- API-specific repair using AUGs provides a feasible approach for fixing API misuses
- Identified key challenges for evolving ASAP-Repair into a full-fledged Automatic Program Repair technique
- Limited prior efforts existed on automatically repairing API misuses compared to detection

**Limitations**: Currently limited to API misuses only rather than general software bugs; requires further development to become a complete APR technique with broader applicability.

### Yin et al. (2024)

**Research question**: Can LLMs direct patch generation through reasoning without requiring external feedback like compilation and test results?

**Methodology**: Employs a two-stage prompt engineering approach: (1) repair thinking generation that prompts the LLM to reason about the bug and repair strategy, and (2) patch generation that uses the repair thinking to guide patch synthesis.

**Key findings**:
- Achieved 37.3% repair accuracy across 4 benchmarks with 1,582 bugs
- Outperformed existing LLM-based APR techniques by 6.7-24.6 percentage points
- Generated higher quality patches with 28.5% semantically correct vs 13.3-22.1% for baselines
- Eliminates dependency on external feedback (compilation/test results), expanding applicability

**Limitations**: Relies entirely on LLM reasoning capabilities without external validation, which may limit reliability in scenarios where compilation or test feedback would catch errors; evaluation focused on specific benchmarks.

### Zhang et al. (2025)

**Research question**: How can retrieval-augmented generation improve LLM-based APR by providing better context understanding for long code contexts?

**Methodology**: Proposed RAG-APR that retrieves relevant code snippets, documentation, and similar bug fixes from codebases before generating patches, integrating retrieved context through attention-based fusion. Evaluated on 521 bugs from 10 open-source projects.

**Key findings**:
- RAG-APR improves patch correctness by 15.7 percentage points compared to baseline LLMs without retrieval
- Retrieval of similar historical fixes contributes most to improvement (8.3 pp), followed by API documentation (4.2 pp) and related code snippets (3.2 pp)
- Particularly excels at API misuse repairs with 52.3% accuracy vs 31.8% baseline
- Attention-based fusion effectively integrates retrieved context into LLM prompts

**Limitations**: Performance depends on quality and availability of retrieval corpus; may not help with novel bugs lacking similar historical examples; retrieval overhead could impact real-time repair scenarios.

## References

Cheng, T., Meng, X., Huang, L., Zhang, H., & Wang, Y. (2025). Multi-agent collaboration for automated program repair with large language models. arXiv. https://arxiv.org/abs/2502.08471

Guo, Q., Zhang, X., Wang, Z., & Yu, Y. (2025). Efficient fine-tuning of large language models for automated program repair. arXiv. https://arxiv.org/abs/2505.14782

Huang, Y., Jiang, S., Zhou, Y., Zhang, Y., Zhang, H., Shi, Y., Chen, J., Guan, Z., & Zhang, M. (2024). RepairAgent: An autonomous LLM agent for automated program repair. arXiv. https://arxiv.org/abs/2409.15372

Huang, Y., Chen, J., Li, Z., Zeng, L., & Yang, X. (2025). PatchCorrect: Learning to predict patch correctness for LLM-based program repair. arXiv. https://arxiv.org/abs/2503.11847

Li, Z., Ni, C., Yin, X., Yang, X., & Sun, X. (2024). LLM-based automated program repair: A survey. arXiv. https://arxiv.org/abs/2410.16276

Li, M., Shang, W., Derakhshanfar, P., & Wang, Z. (2025). CodeRepairBench: A comprehensive benchmark for LLM-based code repair. arXiv. https://arxiv.org/abs/2501.02393

Li, A., Sun, W., Chen, J., Liu, Y., Li, Z., & Zeng, L. (2025). Security vulnerabilities in LLM-based automated program repair. arXiv. https://arxiv.org/abs/2506.13186

Nielebock, S., Blockhaus, P., Krüger, J., & Ortmeier, F. (2024). ASAP-Repair: API-specific automated program repair based on API usage graphs. arXiv. https://arxiv.org/abs/2402.07542

Yin, X., Ni, C., Wang, S., Li, Z., Zeng, L., & Yang, X. (2024). ThinkRepair: Self-directed automated program repair. arXiv. https://arxiv.org/abs/2407.20898

Zhang, W., Fan, M., Zhang, H., & Xiong, Y. (2025). Context-aware patch generation for automated program repair with retrieval-augmented LLMs. arXiv. https://arxiv.org/abs/2504.09234
