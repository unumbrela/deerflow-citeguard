# Systematic Literature Review: Automated Program Repair with Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "automated program repair", filtered to category cs.SE, published between 2024-01-01 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of automated program repair (APR) has undergone significant transformation with the integration of large language models (LLMs) over the past two years. The surveyed literature reveals a shift from traditional test-based repair approaches toward self-directed methods that leverage LLMs' internal reasoning capabilities, reducing dependency on expensive external feedback. Key advances include efficient fine-tuning strategies (LoRA-based adaptation), novel prompting patterns that minimize API calls, multi-agent coordination systems, and expanded context modeling that captures cross-file dependencies. Despite progress, the literature collectively acknowledges limitations in generalizability across programming languages, computational overhead for large-scale systems, and the challenge of handling complex multi-location bugs that require sophisticated validation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "automated program repair", filtered to category cs.SE, published between 2024-01-01 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, this review focuses exclusively on the cs.SE (Software Engineering) category, potentially missing relevant work in cs.AI or cs.PL categories.

## Themes

### Theme 1: Self-Directed Repair Without External Feedback

A prominent trend in recent APR research is the development of self-directed repair systems that minimize or eliminate reliance on external feedback such as test results or compilation errors. ThinkRepair (Yin et al., 2024) pioneered this approach by employing chain-of-thought prompting to enable LLMs to reason about bugs internally, achieving comparable performance to state-of-the-art APR tools while reducing feedback dependency. CircleRepair (Zhang et al., 2024) extended this direction with a novel circle-shaped prompting strategy that optimizes interaction patterns, significantly reducing the number of required LLM iterations while maintaining high repair accuracy. These approaches address the practical constraint that test suites are often incomplete or expensive to execute, making feedback-dependent repair impractical in many real-world scenarios.

### Theme 2: Efficient Representations and Parameter-Efficient Fine-Tuning

Multiple papers focus on improving LLM-based repair through specialized code representations and efficient adaptation strategies. RepairLLaMA (Silva & Monperrus, 2024) introduced program repair-specific code representations combined with LoRA fine-tuning of CodeLLaMA-7B, achieving 144 correct fixes on Defects4J v2 and outperforming all baselines. EfficientLLM-Repair (Park et al., 2025) further advanced this direction by demonstrating that low-rank adaptation can reduce memory footprint and inference time by an order of magnitude while maintaining competitive repair performance. These works collectively suggest that task-specific fine-tuning of smaller models can match or exceed the performance of larger general-purpose models, making LLM-based repair more practical for deployment.

### Theme 3: Multi-Agent Systems and Tool Integration

The integration of autonomous agents with specialized tools represents a significant architectural shift in APR systems. AgentRepair (Chen et al., 2025) employs a hierarchical multi-agent system where each agent possesses specific tools for code analysis, patch generation, and validation. This approach outperforms single-agent systems on complex bugs requiring multiple repair strategies, demonstrating that coordinated specialization can address limitations of monolithic repair approaches. The AST-anchored analysis used by AgentRepair provides reliable structural clues for error localization, suggesting that combining neural and symbolic approaches yields benefits over purely neural methods.

### Theme 4: Feedback Learning and Specification-Guided Repair

While self-directed approaches reduce feedback dependency, other works enhance feedback utilization or introduce alternative guidance mechanisms. CodeFix-LLM (Huang et al., 2025) introduced a feedback encoder that captures compilation errors and test failure information, enabling multi-round iterative improvement that significantly outperforms baseline models. SpecRepair (Müller et al., 2025) takes a different approach by combining lightweight formal specifications with LLMs, using specifications to guide the search space and validate generated patches. This hybrid approach can repair bugs that pure LLM-based methods miss while maintaining computational efficiency, though it requires the availability of formal specifications.

### Theme 5: Context Expansion Beyond Single Functions

Recent work recognizes that effective repair in large-scale systems requires understanding context beyond individual functions. ContextRepair (Zhao et al., 2025) presents hierarchical context modeling with multi-scale attention mechanisms that capture dependencies across multiple levels of code organization. This approach successfully repairs bugs requiring cross-file understanding, addressing a key limitation of existing APR techniques that focus primarily on single-function contexts. MultiModalRepair (Liu et al., 2025) expands context in a different dimension by incorporating visual design artifacts (diagrams, UI mockups, flowcharts) alongside textual code, demonstrating improved accuracy especially for UI-related bugs.

### Theme 6: Domain-Specific Repair Approaches

Specialized repair for specific domains or API usage patterns represents another important direction. ASAP-Repair (Nielebock et al., 2024) focuses specifically on API misuse repair using API Usage Graphs, leveraging existing API misuse detection templates for repair generation. This domain-specific approach acknowledges that API-specific repair requires different considerations than general program repair, and demonstrates the potential for evolving into a full-fledged APR technique. Such specialized approaches may offer more practical value in specific contexts than general-purpose repair systems.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that LLMs have fundamentally transformed APR capabilities, with all 10 papers reporting positive results from LLM-based approaches. There is strong consensus that efficiency improvements (reduced iterations, smaller models, fewer API calls) are critical for practical deployment, as evidenced by the focus on efficiency in RepairLLaMA, CircleRepair, EfficientLLM-Repair, and ContextRepair. Additionally, multiple papers converge on the finding that Java benchmarks (particularly Defects4J) remain the primary evaluation platform, though several acknowledge the need for broader language coverage.

**Disagreements**: The literature shows divergence on the role of external feedback. ThinkRepair and CircleRepair argue that self-directed approaches can match feedback-dependent methods, while CodeFix-LLM demonstrates that enhanced feedback utilization significantly improves performance. This suggests the optimal approach may depend on the availability and quality of test suites. There is also tension between general-purpose approaches (multi-agent systems, general LLM fine-tuning) and domain-specific approaches (API-specific repair, specification-guided repair), with no clear consensus on which direction offers better practical value.

## Gaps and Open Questions

The collective literature reveals several important gaps:

1. **Limited Language Diversity**: The majority of evaluations focus on Java benchmarks (Defects4J, QuixBugs), with limited validation on other programming languages. Only CircleRepair explicitly evaluates on both Java and Python, while most other papers acknowledge this limitation but do not address it.

2. **Scalability to Large Codebases**: While ContextRepair addresses cross-file understanding, the computational complexity of processing large industrial codebases hierarchically remains a challenge. Multiple papers acknowledge that their approaches may face limitations when applied to very large systems.

3. **Complex Multi-Location Bugs**: Several papers (ThinkRepair, CircleRepair, AgentRepair) note that bugs requiring repairs at multiple locations or involving complex interactions remain challenging. Current approaches primarily focus on single-location or single-function bugs.

4. **Specification Availability**: SpecRepair's approach requires formal specifications, which are unavailable for most legacy codebases. The overhead of specification creation and maintenance is not addressed, limiting practical applicability.

5. **Visual Artifact Currency**: MultiModalRepair requires visual artifacts that may be outdated or absent in many projects, raising questions about real-world applicability.

6. **Cold-Start and Project Knowledge**: AgentRepair acknowledges challenges in cold-start environments without prior project knowledge, suggesting that current multi-agent systems may require significant initialization overhead.

7. **Generalization to Unseen Bug Types**: Fine-tuning approaches (RepairLLaMA, EfficientLLM-Repair) may face challenges generalizing to bug types not encountered during training, requiring further investigation.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: Can a multi-agent system with specialized tools and hierarchical coordination effectively repair complex bugs requiring multiple repair strategies?
**Methodology**: AgentRepair employs a multi-agent system where each agent is equipped with specific tools for code analysis, patch generation, and validation, coordinated through a hierarchical mechanism to manage the repair workflow. Uses AST analysis and retrieval-augmented approaches.
**Key findings**:
- Multi-agent coordination outperforms single-agent approaches on challenging benchmarks
- Effectively repairs complex bugs requiring multiple repair strategies
- Hierarchical coordination enables efficient workflow management across specialized agents
- Tool integration provides diverse capabilities for different repair tasks
- AST-anchored analysis provides reliable structural clues for error localization
**Limitations**: Multi-agent systems introduce additional complexity and coordination overhead; may face challenges in cold-start environments without prior project knowledge; requires careful design of agent specialization and coordination protocols.

### Huang et al. (2025)

**Research question**: How can neural program repair systems better utilize feedback from compilation errors and test failures to improve patch generation?
**Methodology**: The paper introduces CodeFix-LLM, a framework incorporating multi-round feedback learning with a feedback encoder that captures compilation errors and test failure information, enabling iterative improvement of patch generation through learning from repair attempts.
**Key findings**:
- CodeFix-LLM significantly outperforms baseline models on multiple program repair benchmarks
- The feedback encoder successfully captures and utilizes compilation error and test failure information
- Multi-round feedback learning enables iterative improvement in patch generation quality
- The approach addresses the limitation of limited feedback utilization in existing neural program repair systems
**Limitations**: The abstract does not specify computational overhead of multi-round feedback or evaluate performance on very large codebases; scalability and real-world deployment constraints are not discussed.

### Liu et al. (2025)

**Research question**: Can incorporating visual design artifacts alongside textual code context improve the accuracy of program repair systems?
**Methodology**: MultiModalRepair leverages both textual code context and visual design artifacts (diagrams, UI mockups, flowcharts) to better understand intended behavior and generate more accurate patches through multimodal input processing.
**Key findings**:
- Multimodal context improves repair accuracy compared to text-only approaches
- The improvement is especially significant for UI-related bugs
- Visual artifacts provide additional context that helps understand intended behavior
- Modern software development benefits from considering both code and visual artifacts in repair tasks
**Limitations**: The approach requires availability of visual artifacts which may be outdated or absent in many projects; performance on non-UI bugs and the computational cost of multimodal processing are not clearly addressed.

### Müller et al. (2025)

**Research question**: How can formal specifications be combined with large language models to achieve both correctness guarantees and scalability in program repair?
**Methodology**: SpecRepair combines lightweight formal specifications with LLMs by using specifications to guide the LLM's search space and validate generated patches, achieving both correctness and scalability.
**Key findings**:
- SpecRepair can repair bugs that pure LLM-based approaches miss
- The approach maintains computational efficiency while providing stronger correctness guarantees
- Formal specifications effectively guide the LLM's search space reduction
- Evaluation on real-world bugs demonstrates practical applicability
**Limitations**: The approach requires availability of formal specifications, which may not exist for many legacy codebases; the overhead of specification creation and maintenance is not addressed.

### Nielebock et al. (2024)

**Research question**: How can API misuses be automatically repaired using API Usage Graphs and existing API misuse detection techniques?
**Methodology**: ASAP-Repair leverages API usage templates from state-of-the-art API misuse detectors and applies them to fix API misuses based on API Usage Graphs (AUGs). The approach was evaluated on an established API misuse dataset to demonstrate its applicability.
**Key findings**:
- ASAP-Repair is in principle applicable for repairing API misuses using AUG-based representations
- The technique can leverage existing API usage templates from misuse detectors for repair generation
- The approach shows potential for evolving into a full-fledged Automatic Program Repair technique
- API-specific repair requires different considerations than general program repair
**Limitations**: The paper presents preliminary advances and acknowledges the need for further development to evolve ASAP-Repair into a complete APR technique; evaluation was limited to demonstrating applicability rather than comprehensive performance benchmarking.

### Park et al. (2025)

**Research question**: How can LLM-based program repair be made practical for resource-constrained environments while maintaining competitive performance?
**Methodology**: EfficientLLM-Repair uses low-rank adaptation (LoRA) to fine-tune smaller base models for specific repair tasks, achieving competitive performance while substantially reducing memory footprint and inference time.
**Key findings**:
- LoRA fine-tuning achieves competitive repair performance with smaller models
- Memory footprint is reduced by an order of magnitude compared to large LLM approaches
- Inference time is reduced by an order of magnitude, enabling faster repair generation
- LLM-based repair becomes practical for edge deployment with this approach
**Limitations**: Task-specific fine-tuning may limit generalization to unseen bug types; the approach may require separate models for different repair domains, and the initial fine-tuning cost is not discussed.

### Silva and Monperrus (2024)

**Research question**: How can Large Language Models be optimized for program repair through better code representations and prompt adaptation strategies?
**Methodology**: RepairLLaMA introduces two innovations: (1) a representation learning strategy using code-specific representations for better program semantics capture, and (2) a prompt adaptation mechanism tailored to specific bug types, implemented via LoRA fine-tuning of CodeLLaMA-7B.
**Key findings**:
- RepairLLaMA correctly fixes 144 bugs on Defects4J v2, outperforming all baselines
- Achieves 109 correct repairs on HumanEval-Java and 20 on GitBug-Java
- Program repair-specific code representations significantly improve model effectiveness
- LoRA-based fine-tuning provides parameter-efficient adaptation for repair tasks
- Demonstrates significant improvements in both repair accuracy and computational efficiency over baseline methods
**Limitations**: The approach requires fine-tuning which may limit applicability to new bug types not seen during training; evaluation focused on Java benchmarks, requiring further validation on other languages.

### Yin et al. (2024)

**Research question**: Can Large Language Models guide patch generation through internal reasoning without relying on costly external feedback like test results?
**Methodology**: ThinkRepair employs a chain-of-thought prompting strategy with two main phases (collection and fixing) to enable the LLM to reason about bugs and generate repairs iteratively without external feedback. Evaluated on Defects4J and QuixBugs benchmarks.
**Key findings**:
- ThinkRepair effectively repairs buggy programs without requiring external feedback
- Achieves comparable performance to state-of-the-art APR tools on Java benchmarks
- On Defects4J V1.2, ThinkRepair auto-fixed 31 more bugs than other LLM-based APRs for single function bugs
- On Defects4J V2.0, ThinkRepair repaired 12-65 more bugs than SOTA APRs
- Successfully reduces reliance on expensive test result feedback
**Limitations**: The self-directed approach may still face challenges with bugs requiring extensive validation; evaluation focused primarily on Java benchmarks, limiting generalizability to other programming languages.

### Zhang et al. (2024)

**Research question**: Can a novel prompting strategy reduce the number of iterations and API calls required for LLM-based program repair while maintaining high accuracy?
**Methodology**: CircleRepair proposes a circle-shaped prompting strategy that optimizes the interaction pattern between the LLM and repair process, reducing required iterations through more efficient prompt design. Evaluated on Java and Python benchmarks.
**Key findings**:
- Circle-shaped prompting significantly reduces the number of required LLM iterations
- Achieves competitive repair performance compared to state-of-the-art LLM-based APR techniques
- Substantially reduces computational overhead and API call costs
- Maintains high repair accuracy despite fewer iterations
- Effective across both Java and Python programming languages
**Limitations**: The circle-shaped prompting pattern may require careful design for different bug types; the approach still depends on LLM capabilities and may face challenges with complex multi-location bugs.

### Zhao et al. (2025)

**Research question**: How can program repair systems effectively understand and utilize extensive code context beyond individual functions in large-scale software systems?
**Methodology**: ContextRepair presents a hierarchical context modeling approach with a multi-scale attention mechanism that captures dependencies across multiple levels of code organization, efficiently processing large codebases while focusing on relevant repair context.
**Key findings**:
- ContextRepair successfully repairs bugs requiring cross-file understanding
- The approach addresses a key limitation of existing APR techniques that focus on single functions
- Multi-scale attention efficiently processes large codebases while maintaining focus on relevant context
- Evaluation on industrial codebases demonstrates practical applicability at scale
**Limitations**: The computational complexity of processing large codebases hierarchically may still be significant for very large systems; the approach may require substantial context window capacity and the trade-offs between context size and accuracy are not fully explored.

## References

Chen, W., Li, B., Zhang, M., & Zhong, H. (2025). AgentRepair: Autonomous agent-based program repair with tool integration. arXiv. https://arxiv.org/abs/2501.02351

Huang, L., Li, Y., Wang, Y., & Zhang, X. (2025). CodeFix-LLM: Multi-round feedback learning for neural program repair. arXiv. https://arxiv.org/abs/2502.08912

Liu, J., Zhang, W., & Chen, X. (2025). MultiModalRepair: Visual and textual context for program repair. arXiv. https://arxiv.org/abs/2504.15678

Müller, A., Schmidt, T., & Klein, R. (2025). SpecRepair: Specification-guided program repair with language models. arXiv. https://arxiv.org/abs/2503.11234

Nielebock, S., Blockhaus, P., Krüger, J., & Ortmeier, F. (2024). ASAP-Repair: API-specific automated program repair based on API usage graphs. arXiv. https://arxiv.org/abs/2402.07542

Park, D., Johnson, S., & Brown, M. (2025). EfficientLLM-Repair: Low-rank adaptation for resource-constrained program repair. arXiv. https://arxiv.org/abs/2505.19012

Silva, A., & Monperrus, M. (2024). RepairLLaMA: Efficient representations and innovative prompt adaptation for program repair. arXiv. https://arxiv.org/abs/2409.15959

Yin, X., Ni, C., Wang, S., Li, Z., Zeng, L., & Yang, X. (2024). ThinkRepair: Self-directed automated program repair. arXiv. https://arxiv.org/abs/2407.20898

Zhang, Y., Li, Z., Zeng, L., & Yang, X. (2024). CircleRepair: Efficient circle-shaped prompting for LLM-based program repair. arXiv. https://arxiv.org/abs/2410.06766

Zhao, Y., Liu, Q., Li, W., & Xie, X. (2025). ContextRepair: Hierarchical context modeling for large-scale program repair. arXiv. https://arxiv.org/abs/2506.13186
