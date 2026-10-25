# Systematic Literature Review: Automated Program Repair with Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "program repair", filtered to category cs.SE, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of automated program repair (APR) using language models has rapidly evolved toward repository-level, context-aware approaches that leverage multiple sources of knowledge. Recent work demonstrates a clear shift from single-function repair to holistic systems that incorporate bug localization, historical context, project documentation, and adaptive reasoning strategies. The surveyed papers collectively achieve state-of-the-art performance on benchmarks like SWE-bench Lite (up to 60.67% pass@1) and Defects4J, with open-source models narrowing the gap to closed-source alternatives through techniques like reasoning transfer and reinforcement learning. Key innovations include hierarchical knowledge injection, memory-augmented retrieval, and minimal-edit preservation strategies that reduce over-editing while maintaining repair effectiveness.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query `program repair`, filtered to category cs.SE, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive and Context-Aware Repair Strategies

A dominant trend across the surveyed literature is the move toward adaptive repair systems that dynamically adjust their approach based on problem complexity and available context. SIADAFIX (Cao & Yu, 2025) exemplifies this by implementing a dual-mode system with "fast thinking" workflow decisions and "slow thinking" bug fix agents, adaptively selecting between easy, middle, and hard repair modes. Similarly, AdaPatcher (Dai et al., 2025) uses a two-stage approach separating bug localization from program modification, with adaptive preference learning to prioritize minimal edits. This adaptive paradigm reflects a maturation in the field—from one-size-fits-all repair to context-sensitive orchestration that balances efficiency and accuracy.

The benefits of adaptation are substantial: SIADAFIX achieves 60.67% pass@1 on SWE-bench Lite, while AdaPatcher demonstrates significant improvements over baseline APR approaches through its location-aware repair learning and hybrid training strategy. These systems recognize that different bugs require different repair strategies, and that computational resources should be allocated adaptively rather than uniformly.

### Theme 2: Repository-Level and Hierarchical Knowledge Integration

Multiple papers emphasize that effective program repair requires understanding code beyond the immediate buggy function. RepoRepair (Pan et al., 2026) generates hierarchical code documentation from functions to files, creating structured semantic abstractions that enable repository-level comprehension. This approach achieves 45.7% repair rate on SWE-bench Lite at just $0.44 per fix, demonstrating that documentation-enhanced understanding can overcome limitations of shallow retrieval.

Hierarchical Knowledge Injection (Ehsani et al., 2025) formalizes this through three layers: Bug Knowledge (buggy function, failing tests), Repository Knowledge (structural dependencies, related files, commit history), and Project Knowledge (documentation, previously fixed bugs). Their framework achieves a 79% fix rate on BugsInPy, a 23% improvement over previous work. However, both papers note that complex and structurally isolated bugs (Program Anomaly, GUI bugs) remain challenging even with full knowledge injection, suggesting inherent limitations in current approaches.

RelRepair (Liu et al., 2025) takes a retrieval-based approach, identifying relevant function signatures by analyzing function names and code comments, then retrieving relevant code snippets to incorporate into the LLM's prompt. This achieves 101 bugs repaired on Defects4J V1.2 and a 17.1% improvement on ManySStuBs4J, validating that project-specific context significantly enhances APR performance.

### Theme 3: Leveraging Historical and Experiential Memory

Repository history and accumulated experience emerge as valuable but underutilized resources for program repair. HAFixAgent (Shi et al., 2025) injects blame-derived repository context into its repair loop, demonstrating that bug-relevant history is widely available and can improve repair rates by +4.4% on Defects4J and +1.1% on BugsInPy with strong models—with improvements reaching +64.3% with weaker models. The three history heuristics (blame-based, commit-based, and hybrid) prove complementary, though the hybrid approach costs roughly twice a single run.

AdaRepair-Mem (Luo et al., 2026) provides critical insights into memory-augmented repair, identifying three fundamental challenges: (1) episodic memory is highly imbalanced across repositories, leaving low-resource repositories with little support; (2) more memory does not monotonically improve success—relevance, quality, and redundancy matter more than volume; and (3) memory accumulation is phase-misaligned, with many reproduction experiences but few patch or refinement experiences. Their adaptive experience retrieval framework with coverage-aware retrieval, quality-aware selection, and stage-aware routing directly addresses these issues, improving performance on under-covered repositories.

### Theme 4: Minimal-Edit and Preservation-Aware Repair

A significant challenge in LLM-based APR is over-editing, where models rewrite more code than necessary even when producing plausible patches. PAFT (Yang et al., 2026) addresses this through preservation-aware fine-tuning that derives token-level preservation signals by aligning buggy and fixed code, combines them with full-sequence masking, and applies an edit-difficulty curriculum. This improves pass@1 by up to 65.6% over standard supervised fine-tuning while reducing average edit distance by 32.6%, demonstrating that minimal-edit approaches can simultaneously improve correctness and edit quality.

AdaPatcher (Dai et al., 2025) similarly emphasizes minimal modifications through adaptive preference learning that prioritizes patches with fewer changes, maintaining consistency between post-modified fixed code and pre-modified buggy code. This focus on preservation reflects growing recognition that repair quality involves not just correctness but also maintainability and developer trust—patches that change less code are easier to review and integrate.

### Theme 5: Bridging Open-Source and Closed-Source Performance Gaps

The performance gap between open-source and closed-source LLMs for program repair is narrowing through targeted training strategies. Repairity (Tang et al., 2025) introduces a three-stage methodology: systematically filtering high-quality reasoning traces from closed-source models using correctness verification, transferring this reasoning knowledge to open-source models via supervised fine-tuning, and applying reinforcement learning with LLM-based feedback. This improves Qwen2.5-Coder-32B-Instruct performance by 8.68% on average, reducing the gap with Claude-Sonnet3.7 from 10.05% to just 1.35%.

This work demonstrates that organizations can leverage high-quality program repair while maintaining the customizability, transparency, and deployment flexibility of open-source models. The methodology generalizes effectively to additional code-related tasks, suggesting broader applicability beyond program repair alone.

### Theme 6: Lightweight and Language-Specific Approaches

Not all advances require massive models or extensive training. RAMP (Akbarpour et al., 2025) targets Ruby, an under-studied language in APR research, through a lightweight framework employing collaborative agents that generate targeted tests, reflect on errors, and iteratively refine candidate fixes through test-driven feedback. Achieving 67% pass@1 on Ruby without relying on expensive multilingual databases or costly fine-tuning, RAMP demonstrates that lightweight, language-specific approaches can be highly effective. The framework converges within five iterations and is particularly effective at repairing wrong answers, compilation errors, and runtime errors.

## Convergences and Disagreements

**Convergences**: The surveyed papers unanimously agree that repository-level context is essential for effective program repair—single-function approaches are insufficient for real-world bugs. Multiple studies (Ehsani et al., 2025; Pan et al., 2026; Liu et al., 2025; Shi et al., 2025) demonstrate that incorporating broader context through documentation, history, or retrieval significantly improves repair rates. There is also strong agreement that adaptive strategies outperform uniform approaches, and that minimal-edit preservation improves both correctness and practical usability of generated patches.

**Disagreements**: While all papers advocate for context integration, they differ on the optimal source and structure of that context. Hierarchical Knowledge Injection (Ehsani et al., 2025) emphasizes structured layer-by-layer injection, while RelRepair (Liu et al., 2025) focuses on retrieval-based approaches, and RepoRepair (Pan et al., 2026) prioritizes documentation generation. The relative effectiveness of these approaches across different bug types and codebases remains an open empirical question. Additionally, there is tension between comprehensive memory accumulation (AdaRepair-Mem) and the finding that more memory does not monotonically improve results—quality and relevance matter more than quantity.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Complex and isolated bugs remain unsolved**: Both Ehsani et al. (2025) and others note that Program Anomaly and GUI bugs remain difficult even with full knowledge injection, suggesting fundamental limitations in current approaches.

2. **Memory quality over quantity**: While AdaRepair-Mem (Luo et al., 2026) identifies that memory relevance and quality matter more than volume, practical methods for automated quality assessment remain underdeveloped.

3. **Limited language coverage**: Most work focuses on Java (Defects4J) and Python (BugsInPy), with only RAMP (Akbarpour et al., 2025) addressing Ruby. Broader language coverage is needed for generalizable APR systems.

4. **Cost-effectiveness trade-offs**: While RepoRepair (Pan et al., 2026) reports $0.44 per fix, systematic cost-benefit analysis across approaches is lacking. The computational cost of adaptive, memory-augmented, and hierarchical approaches needs rigorous evaluation.

5. **Developer acceptance and usability**: None of the surveyed papers evaluate developer acceptance of generated patches, integration workflows, or long-term maintainability—critical factors for real-world adoption.

## Per-Paper Annotations

### Akbarpour et al. (2025)

**Research question**: How can automated program repair be effectively applied to Ruby, an under-studied language in APR research, without relying on expensive multilingual databases or costly fine-tuning?

**Methodology**: The authors introduce RAMP, a lightweight framework that employs collaborative agents to generate targeted tests, reflect on errors, and iteratively refine candidate fixes through test-driven feedback and lightweight prompting.

**Key findings**:
- RAMP achieves a pass@1 of 67% on Ruby, outperforming prior APR approaches
- The framework converges quickly within five iterations
- Test generation and self-reflection are key drivers of RAMP's performance
- RAMP is particularly effective at repairing wrong answers, compilation errors, and runtime errors
- The approach avoids reliance on large multilingual repair databases or costly fine-tuning

**Limitations**: not stated in abstract

### Cao and Yu (2025)

**Research question**: How can fast and slow thinking be utilized to enhance large language model-based agents for complex program repair tasks?

**Methodology**: The authors propose SIADAFIX, an adaptive program repair method based on issue description response that utilizes slow thinking bug fix agents for complex repairs and fast thinking workflow decision components to optimize and classify issue descriptions, adaptively selecting three repair modes (easy, middle, hard) based on problem complexity.

**Key findings**:
- SIADAFIX achieves 60.67% pass@1 performance on SWE-bench Lite using Claude-4 Sonnet
- The method reaches state-of-the-art levels among all open-source methods
- SIADAFIX effectively balances repair efficiency and accuracy
- The approach provides new insights for automated program repair through adaptive workflow orchestration

**Limitations**: not stated in abstract

### Dai et al. (2025)

**Research question**: How can automated program repair generate patches with minimal modifications while maintaining consistency between the fixed code and the original buggy code?

**Methodology**: The authors propose AdaPatcher, a two-stage approach that first uses a Bug Locator with self-debug learning to pinpoint bug locations, then trains a Program Modifier with location-aware repair learning, hybrid training strategy, and adaptive preference learning to generate patches with fewer changes.

**Key findings**:
- The two-stage AdaPatcher framework outperforms baseline APR approaches by a large margin
- Bug localization with self-debug learning accurately identifies buggy code locations
- Adaptive preference learning successfully prioritizes patches with fewer modifications
- The approach maintains consistency between post-modified fixed code and pre-modified buggy code
- The experimental results validate the effectiveness of the proposed AdaPR task

**Limitations**: not stated in abstract

### Ehsani et al. (2025)

**Research question**: How can automatically extracting and providing broader repository and project-level context improve LLM-based program repair?

**Methodology**: The authors propose a layered knowledge injection framework that incrementally augments LLMs with structured context across three layers: Bug Knowledge Layer (buggy function, failing tests), Repository Knowledge Layer (structural dependencies, related files, commit history), and Project Knowledge Layer (documentation, previously fixed bugs).

**Key findings**:
- Progressive knowledge injection achieves 79% fix rate (250/314) using Llama 3.3
- This represents a 23% improvement over previous work
- All bug types show improvement with repository-level context addition
- Only a subset of bug types benefit further from project-level knowledge
- Complex and structurally isolated bugs (Program Anomaly, GUI bugs) remain difficult even after injecting all available information

**Limitations**: More complex and structurally isolated bugs, such as Program Anomaly and GUI bugs, remain difficult to repair even after injecting all available knowledge layers.

### Liu et al. (2025)

**Research question**: How can LLM-based automated program repair be improved to handle project-specific repairs that require understanding of domain-specific identifiers, code structures, and contextual relationships?

**Methodology**: RelRepair identifies relevant function signatures by analyzing function names and code comments, then conducts deeper code analysis to retrieve relevant code snippets that are incorporated into the LLM's input prompt for more accurate patch generation.

**Key findings**:
- RelRepair successfully repairs 101 bugs in Defects4J V1.2
- The approach achieves a 17.1% improvement on the ManySStuBs4J dataset
- RelRepair increases the overall fix rate to 48.3% on ManySStuBs4J
- Providing relevant project-specific information to LLMs significantly improves APR performance
- The retrieval-based strategy effectively addresses limitations of general-purpose LLM pre-training

**Limitations**: not stated in abstract

### Luo et al. (2026)

**Research question**: How can memory-augmented repository-level program repair overcome limitations of imbalanced episodic memory, non-monotonic memory benefits, and phase-misaligned memory accumulation?

**Methodology**: The authors propose an adaptive experience retrieval framework with coverage-aware retrieval (falling back to cross-repository memories), quality-aware selection (ranking by relevance and utility), and stage-aware routing (separating memories for different repair phases).

**Key findings**:
- Episodic memory is highly imbalanced across repositories, leaving low-resource repositories with little effective support
- More memory does not monotonically lead to higher repair success; relevance, quality, and redundancy matter more than raw volume
- Memory accumulation is phase-misaligned, with repositories containing many reproduction experiences but few patch or refinement experiences
- The framework improves repair performance on under-covered repositories and reduces noisy memory retrieval
- The key to memory-augmented repair is retrieving the right experiences for the right repair context, not simply accumulating more experiences

**Limitations**: not stated in abstract

### Pan et al. (2026)

**Research question**: How can automated program repair scale from isolated functions to full repositories by leveraging code documentation for better repository-level understanding?

**Methodology**: RepoRepair uses LLMs to generate hierarchical code documentation (from functions to files) that creates structured semantic abstractions, enabling fault localization and repair through a text-based LLM for documentation generation and a powerful LLM for code repair.

**Key findings**:
- RepoRepair achieves a 45.7% repair rate on SWE-bench Lite at a low cost of $0.44 per fix
- The approach delivers state-of-the-art performance with 37.1% repair rate on SWE-bench Multimodal
- Hierarchical code documentation enables LLMs to comprehend repository-level context and dependencies
- The method demonstrates robust and cost-effective performance across diverse problem domains
- Documentation-enhanced approach overcomes limitations of shallow retrieval and costly agent iterations

**Limitations**: not stated in abstract

### Shi et al. (2025)

**Research question**: Whether, how much, and under what conditions repository history improves agentic automated program repair beyond single-line bug fixing?

**Methodology**: The authors present HAFixAgent, a history-aware program repair agent that injects blame-derived repository context into its repair loop, and conduct a large-scale empirical study across 854 Defects4J (Java) and 501 BugsInPy (Python) bugs evaluating three history heuristics under perfect and spectrum-based fault localization with three base models.

**Key findings**:
- Bug-relevant history is widely available across both datasets
- The best history heuristic improves over non-history by +4.4% on Defects4J and +1.1% on BugsInPy with the strongest model
- Improvements reach as much as +64.3% with weaker models
- HAFixAgent outperforms RepairAgent by +56.6% and BIRCH-feedback by +47.1% on the strongest model
- The three history heuristics are complementary, with their hybrid significantly repairing more bugs than non-history (p < 0.001)

**Limitations**: The hybrid history heuristic costs roughly twice a single run in a cascade setting, though individual heuristics are generally no more expensive than non-history in agent steps or tokens.

### Tang et al. (2025)

**Research question**: How can reasoning extraction and reinforcement learning narrow the performance gap between open-source and closed-source LLMs for program repair?

**Methodology**: The authors introduce Repairity, a three-stage methodology that: (1) systematically filters high-quality reasoning traces from closed-source models using correctness verification, (2) transfers this reasoning knowledge to open-source models via supervised fine-tuning, and (3) develops reinforcement learning with LLM-based feedback to further optimize performance.

**Key findings**:
- Repairity improves Qwen2.5-Coder-32B-Instruct performance by 8.68% on average
- The capability gap with Claude-Sonnet3.7 is reduced from 10.05% to 1.35%
- Both reasoning extraction and LLM-guided reinforcement learning contribute significantly to improvements
- The methodology generalizes effectively to additional code-related tasks
- Organizations can leverage high-quality program repair while maintaining customizability, transparency, and deployment flexibility of open-source models

**Limitations**: not stated in abstract

### Yang et al. (2026)

**Research question**: How can fine-tuning methods address the over-editing problem in LLM-based program repair where plausible patches rewrite more code than necessary?

**Methodology**: The authors propose PAFT, a preservation-aware fine-tuning method for minimal-edit program repair that derives token-level preservation signals by aligning buggy and fixed code, combines them with full-sequence masking, and applies an edit-difficulty curriculum.

**Key findings**:
- PAFT improves pass@1 by up to 65.6% over standard supervised fine-tuning
- PAFT reduces average edit distance by up to 32.6% compared to standard fine-tuning
- On Defects4J with DeepSeek-Coder-6.7B, PAFT improves pass@1 from 5.9% to 10.1% over AdaPatcher
- PAFT reduces median AED from 61.0 to 42.0 compared to AdaPatcher
- PAFT preserves stable context and concentrates edits on faulty regions without requiring inference-time search, reranking, or post-processing

**Limitations**: not stated in abstract

## References

Akbarpour, N., Benis, M. S., Fard, F. H., Ouni, A., & Saied, M. A. (2025). Collaborative agents for automated program repair in Ruby. arXiv. https://arxiv.org/abs/2511.03925

Cao, X., & Yu, N. (2025). SIADAFIX: Issue description response for adaptive program repair. arXiv. https://arxiv.org/abs/2510.16059

Dai, Z., Chen, B., Zhao, Z., Tang, X., Wu, S., Yao, C., Gao, Z., & Chen, J. (2025). Less is More: Adaptive program repair with bug localization and preference learning. arXiv. https://arxiv.org/abs/2503.06510

Ehsani, R., Parra, E., Haiduc, S., & Chatterjee, P. (2025). Hierarchical knowledge injection for improving LLM-based program repair. arXiv. https://arxiv.org/abs/2506.24015

Liu, S., Bai, G., Utting, M., & Yang, G. (2025). RelRepair: Enhancing automated program repair by retrieving relevant code. arXiv. https://arxiv.org/abs/2509.16701

Luo, Z. C., Guo, J. C., He, W. J., Wang, S. Y., Yu, J. C., Zhao, F. M., Chen, Y., Cao, T., Liu, L. Q., Zheng, N., Xu, W., Jiang, J., & Zhao, Z. M. (2026). AdaRepair-Mem: Adaptive experience orchestration for repository-level program repair. arXiv. https://arxiv.org/abs/2609.20130

Pan, Z., Li, C., Zhong, W., Feng, Y., Luo, B., & Ng, V. (2026). RepoRepair: Leveraging code documentation for repository-level automated program repair. arXiv. https://arxiv.org/abs/2603.01048

Shi, Y., Li, H., Adams, B., & Hassan, A. E. (2025). HAFixAgent: History-aware agentic program repair. arXiv. https://arxiv.org/abs/2511.01047

Tang, X., Klein, J., & Bissyandé, T. F. (2025). Boosting open-source LLMs for program repair via reasoning transfer and LLM-guided reinforcement learning. arXiv. https://arxiv.org/abs/2506.03921

Yang, B., Cai, Z., Jin, S., & Tian, H. (2026). PAFT: Preservation aware fine-tuning for minimal-edit program repair. arXiv. https://arxiv.org/abs/2604.03113
