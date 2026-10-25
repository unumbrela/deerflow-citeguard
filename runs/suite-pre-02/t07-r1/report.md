# Systematic Literature Review: Code Generation with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "code generation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on code generation with large language models from 2024-2026 reveals a field rapidly maturing beyond basic functionality toward specialized capabilities and rigorous evaluation. The surveyed papers collectively demonstrate a shift from asking "can LLMs generate code?" to addressing more nuanced questions around security, version control, multimodal inputs, domain-specific applications, and instruction-following precision. Researchers are increasingly developing comprehensive benchmarks that capture real-world complexity, including concurrent programming, library versioning, geospatial tasks, and security vulnerabilities. A notable trend is the move toward multi-agent systems and retrieval-augmented approaches that enable LLMs to adapt to dynamic knowledge requirements. Despite significant progress, gaps remain in handling evolving software dependencies, integrating visual design specifications, and ensuring generated code is both correct and secure.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "code generation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Retrieval-Augmented and Context-Aware Code Generation

A significant research direction focuses on enhancing code generation by incorporating external knowledge and contextual information. EVOR (Su et al., 2024) addresses the limitation of static knowledge bases in retrieval-augmented code generation by introducing synchronous evolution of both queries and diverse knowledge bases. This approach achieves two to four times improvement in execution accuracy compared to methods like Reflexion and DocPrompting. Similarly, Huang et al. (2024) emphasize the importance of multi-modal context in computational notebooks, proposing CoCoMine to extract contextualized data-wrangling examples and DataCoder to encode data context separately from code and textual contexts. Both lines of work recognize that code generation cannot rely solely on the LLM's parametric knowledge but must dynamically incorporate relevant external information structured appropriately for the task at hand.

### Theme 2: Security and Correctness in Code Generation

As LLMs are increasingly deployed for code synthesis, ensuring generated code is both functionally correct and secure has become a critical concern. Wang et al. (2024) introduce CodeSecEval, an execution-based benchmark comprising 255 Python tasks spanning 77 CWE categories, along with SecAwareCoder, an agent-based framework that performs task-adaptive threat modeling to guide secure-by-construction synthesis. Yang et al. (2025) take a different approach with IFEvalCode, a multilingual benchmark of 1.6K samples across seven programming languages that decouples correctness from instruction-following capabilities, revealing that closed-source models outperform open-source ones in controlled code generation. Huang et al. (2026) address yet another dimension with CONCUR, a benchmark specifically designed for concurrent code generation that captures unique bugs like deadlocks and race conditions absent from sequential code. Together, these works demonstrate that "correctness" in code generation is multidimensional, encompassing functional accuracy, security robustness, instruction adherence, and concurrency safety.

### Theme 3: Multimodal and Multilingual Code Generation

Real-world software development involves more than text-only inputs, prompting research into multimodal and multilingual code generation systems. Chai et al. (2025) introduce MM-Coder, which integrates visual design inputs including UML diagrams and flowcharts with textual instructions, along with MMc-Instruct, a multimodal instruction-tuning dataset, and MMEval for evaluation. Their work reveals that while multimodal integration enhances architectural alignment, significant challenges remain in precise visual information capture. Gupta et al. (2025) apply causal analysis to understand how different prompt modalities influence code generation, finding that input-output examples significantly affect outputs beyond natural language instructions. In the multilingual space, Saadi et al. (2025) present a multi-agent system for Bangla-to-Python code generation that achieved first place in the BLP-2025 Shared Task with a Pass@1 score of 95.4, demonstrating that low-resource language support is feasible through targeted architectural innovations.

### Theme 4: Domain-Specific Code Generation

The literature shows increasing specialization of code generation systems for particular domains and use cases. Gramacki et al. (2024) focus on geospatial code generation, creating a benchmark that tests spatial reasoning, spatial data processing, and geospatial tools usage, arguing that this domain poses distinct challenges from general-purpose code generation. Wu et al. (2024) address the dynamic nature of software development with VersiCode, introducing version-specific code completion and version-aware code migration tasks along with the Critical Diff Check metric to assess code generation against evolving API requirements. Their evaluation reveals that version-controllable code generation remains challenging even for GPT-4o and other frontier models. These domain-specific approaches recognize that one-size-fits-all code generation is insufficient for specialized applications requiring deep domain knowledge or adaptation to changing requirements.

### Theme 5: Benchmarking and Evaluation Methodologies

A unifying theme across the surveyed literature is the emphasis on creating comprehensive, execution-based benchmarks rather than relying on static evaluation metrics. Six of the ten papers introduce new benchmarks: EVOR-BENCH (Su et al., 2024), CodeSecEval (Wang et al., 2024), IFEvalCode (Yang et al., 2025), CONCUR (Huang et al., 2026), the geospatial benchmark (Gramacki et al., 2024), CoCoNote (Huang et al., 2024), MMEval (Chai et al., 2025), and VersiCode (Wu et al., 2024). This proliferation of benchmarks reflects recognition that existing evaluation frameworks fail to capture real-world complexity. Common features include executable test cases, domain-specific task designs, and metrics that go beyond simple pass/fail to capture nuances like security robustness, instruction adherence, and version compatibility. The field is moving toward evaluation paradigms that better predict real-world deployment success.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers acknowledge that basic code generation capabilities have matured to the point where research must focus on specialized challenges beyond functional correctness. Second, there is consensus that execution-based evaluation with automated test cases provides more reliable assessment than static metrics or human evaluation alone. Third, multiple papers converge on the finding that current frontier models, including GPT-4o, still struggle significantly with real-world code generation challenges, particularly in domains requiring dynamic knowledge adaptation or specialized reasoning.

**Disagreements**: The literature shows less direct disagreement, partly because papers focus on different evaluation dimensions. However, there is implicit tension between approaches that emphasize scaling model capabilities versus those that focus on architectural innovations like multi-agent systems or retrieval augmentation. Papers like Saadi et al. (2025) demonstrate that targeted architectural designs can achieve state-of-the-art results without necessarily requiring the largest models, while benchmark-focused papers implicitly assume that model improvement is the primary path forward. Additionally, there is variation in how papers conceptualize "instruction-following" — some treat it as adherence to structural constraints (Yang et al., 2025), while others focus on semantic alignment with visual or multimodal specifications (Chai et al., 2025).

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, while multiple papers address version control and library updates (Wu et al., 2024), the solutions remain evaluation-focused rather than providing deployable systems that handle real-world software evolution. Second, multimodal code generation (Chai et al., 2025; Gupta et al., 2025) acknowledges significant challenges in precise visual information capture, suggesting current models lack robust visual reasoning capabilities for complex software specifications. Third, security-focused approaches (Wang et al., 2024) note the difficulty of balancing security with correctness, but do not fully resolve how to optimize for both simultaneously in production settings. Fourth, domain-specific benchmarks (Gramacki et al., 2024) raise questions about generalizability — whether models trained on specialized domains can transfer capabilities or whether entirely separate systems are needed for each domain. Finally, while retrieval-augmented approaches (Su et al., 2024; Huang et al., 2024) show promise, the design principles for effective knowledge base construction and query evolution remain underexplored, with most papers focusing on specific implementations rather than generalizable frameworks.

## Per-Paper Annotations

### Chai et al. (2025)

**Research question**: Can integrating visual design inputs (UML diagrams and flowcharts) with textual instructions improve code generation accuracy and architectural alignment compared to text-only models?

**Methodology**: Introduced MM-Coder, a multilingual multimodal model that integrates Visual Workflow inputs (UML diagrams and flowcharts) with textual instructions; developed MMc-Instruct, a diverse multimodal instruction-tuning dataset; created MMEval benchmark for evaluating multimodal code generation.

**Key findings**:
- MM-Coder successfully synthesizes textual and graphical information similar to human developers
- Created MMc-Instruct dataset for visual-workflow-based code generation instruction tuning
- MMEval benchmark addresses limitations of existing text-only evaluation approaches
- Multimodal approach enhances code generation accuracy and architectural alignment
- Significant challenges remain in precise visual information capture and instruction following

**Limitations**: Evaluations reveal significant remaining challenges for models in precise visual information capture, instruction following, and advanced programming knowledge; the approach may require substantial training data for effective multimodal integration.

### Gramacki et al. (2024)

**Research question**: How well do existing code generation LLMs perform on geospatial coding tasks, and can we create a benchmark to evaluate them?

**Methodology**: Constructed an evaluation benchmark by categorizing geospatial tasks based on complexity and required tools, creating a dataset with specific coding problems and test scenarios for automatic correctness checking, then tested existing code generation LLMs on these tasks.

**Key findings**:
- Created a high-quality dataset of geospatial coding problems with manually crafted test scenarios
- Categorized geospatial tasks by complexity and required tools for systematic evaluation
- Tested multiple existing code generation LLMs on geospatial domain tasks
- Dataset and evaluation code made publicly available as a benchmark for future LLM development
- Identified the need for models specifically tailored to geospatial applications

**Limitations**: The abstract does not explicitly acknowledge limitations; however, the scope appears limited to Python code generation for geospatial tasks, and the manual creation of problems may limit dataset scale.

### Gupta et al. (2025)

**Research question**: What are the causal effects of different prompt modalities (natural language, code, input-output examples) on multi-modal code generation performance in LLMs?

**Methodology**: Proposed CodeSCM, a Structural Causal Model that applies interventions to measure causal effects of different prompt modalities; introduced latent mediator variables to separate code and natural language semantics; applied Causal Mediation Analysis to quantify direct effects representing spurious model leanings.

**Key findings**:
- CodeSCM successfully quantifies causal effects of different prompt modalities on code generation
- Input-output examples significantly influence code generation beyond natural language instructions
- Latent mediator variables effectively separate code and natural language semantics
- Causal Mediation Analysis reveals spurious model leanings in multi-modal code generation
- Natural language instructions are not the only significant factor affecting code generation output

**Limitations**: The abstract does not explicitly acknowledge limitations; the causal model may be constrained by the specific modalities tested and may not generalize to all code generation scenarios or model architectures.

### Huang et al. (2024)

**Research question**: How can we improve data wrangling code generation by better utilizing the rich multi-modal contextual information present in computational notebooks?

**Methodology**: Proposed CoCoMine, an automated approach using data flow analysis to identify data wrangling code blocks and extract contextualized examples through notebook tracing and replaying; created CoCoNote dataset with 58,221 examples; proposed DataCoder model that encodes data context and code/textual contexts separately.

**Key findings**:
- Constructed CoCoNote dataset containing 58,221 contextualized data-wrangling code generation examples
- CoCoMine successfully mines examples with clear multi-modal contextual dependency from notebooks
- Incorporating data context significantly improves data-wrangling code generation performance
- DataCoder model effectively encodes separate contexts to enhance code generation accuracy
- Fine-tuned models and prompted LLMs demonstrated effectiveness on the proposed task

**Limitations**: The abstract does not explicitly state limitations; potential constraints may include the quality of mined examples depending on notebook structure and the generalizability beyond Python computational notebooks.

### Huang et al. (2026)

**Research question**: How can we effectively evaluate LLMs' capability to generate concurrent code, which exhibits unique complexity and bug types like deadlocks and race conditions?

**Methodology**: Designed CONCUR benchmark specifically for evaluating concurrent code generation, consisting of 43 concurrency problems from a standard textbook plus 72 validated mutant variants (115 total problems), then evaluated a range of LLMs on the benchmark.

**Key findings**:
- Created first benchmark specifically designed for concurrent code generation evaluation
- Base problems provide semantic core while mutants expand linguistic and structural diversity
- Evaluation of multiple LLMs highlighted significant limitations in current models' concurrent code capabilities
- Concurrent code exhibits unique bug types not present in sequential code generation
- Existing sequential code benchmarks are inadequate for evaluating concurrent code generation

**Limitations**: The abstract does not explicitly acknowledge limitations; the benchmark is derived from textbook problems which may not fully capture real-world concurrent programming challenges, and evaluation was limited to a specific set of LLMs.

### Saadi et al. (2025)

**Research question**: How can multi-agent systems improve code generation from Bangla instructions to achieve high accuracy in low-resource language settings?

**Methodology**: Proposed a multi-agent-based pipeline where a code-generation agent produces initial solutions from Bangla instructions, then only failing test cases are forwarded to a debugger agent that extracts error traces and generates revised solutions conditioned on error messages and test cases.

**Key findings**:
- Multi-agent debugging approach achieved first place in BLP-2025 Shared Task
- Achieved Pass@1 score of 95.4 on Bangla-to-Python code generation
- Selective debugging (only forwarding failing cases) improves efficiency over full re-generation
- Multi-agent architecture enables specialized handling of generation versus correction
- Code and methodology made publicly available for replication

**Limitations**: The abstract does not explicitly acknowledge limitations; the approach is specific to Bangla-to-Python translation and may require adaptation for other language pairs or programming languages.

### Su et al. (2024)

**Research question**: How can retrieval-augmented code generation pipelines overcome the limitations of static knowledge bases with single sources to better adapt to domains with insufficient LLM knowledge?

**Methodology**: Developed EVOR pipeline employing synchronous evolution of both queries and diverse knowledge bases; compiled EVOR-BENCH with four new datasets for frequently updated libraries and long-tail programming languages; evaluated against baselines including Reflexion and DocPrompting.

**Key findings**:
- EVOR achieves two to four times execution accuracy improvement over existing methods
- Synchronous evolution of queries and documents provides significant benefits
- Diverse information sources in knowledge base enhance adaptation capabilities
- EVOR is flexible and can be combined with other methods for further improvement
- Static knowledge bases fundamentally limit LLM adaptation to new domains

**Limitations**: The abstract does not explicitly acknowledge limitations; the approach requires maintaining multiple knowledge bases and may incur computational overhead for query and document evolution.

### Wang et al. (2024)

**Research question**: How can we bridge the gap between functional correctness and security in LLM code generation through execution-based benchmarking and task-adaptive vulnerability modeling?

**Methodology**: Created CodeSecEval benchmark with 255 Python tasks spanning 77 CWE categories, each with paired insecure and secure implementations plus executable functional and security tests; proposed SecAwareCoder framework performing task-adaptive threat modeling, constraint-aware generation, and execution-based refinement.

**Key findings**:
- CodeSecEval provides precise, reproducible evaluation of secure code generation with 255 tasks across 77 CWE categories
- SecAwareCoder consistently improves Pass@1 and security robustness over prompting and analyzer-driven baselines
- Task-adaptive threat modeling effectively identifies security-sensitive regions in code generation tasks
- Execution-based evaluation with paired implementations enables measurement of security-correctness tradeoffs
- Agent-based secure-by-construction synthesis narrows the security-correctness gap

**Limitations**: The abstract does not explicitly acknowledge limitations; the benchmark is limited to Python and may not generalize to other programming languages with different security patterns and vulnerability types.

### Wu et al. (2024)

**Research question**: How can code generation models account for the dynamic nature of software development with frequent library updates and evolving API requirements?

**Methodology**: Proposed two novel tasks: version-specific code completion (VSCC) and version-aware code migration (VACM); introduced VersiCode, a comprehensive Python dataset for evaluating these tasks; developed Critical Diff Check (CDC@1) metric to assess code generation against evolving API requirements.

**Key findings**:
- Version-controllable code generation is a significant challenge even for GPT-4o and frontier models
- Created VersiCode dataset specifically designed for version-aware code generation evaluation
- CDC@1 metric effectively assesses code generation against evolving API requirements
- VSCC and VACM tasks address critical gaps in existing code generation research
- Current LLMs struggle with library updates and version-specific API requirements

**Limitations**: The task remains significantly challenging even for state-of-the-art models like GPT-4o; the dataset is limited to Python, which may not generalize to other programming languages with different versioning patterns.

### Yang et al. (2025)

**Research question**: How can Code LLMs be improved to adhere to detailed requirements such as coding style, line count, and structural constraints beyond mere functional correctness?

**Methodology**: Introduced forward and backward constraints generation to improve instruction-following capabilities; created IFEvalCode benchmark with 1.6K test samples across seven programming languages with Chinese and English queries; decoupled evaluation into correctness and instruction-following metrics.

**Key findings**:
- Closed-source models outperform open-source ones in controllable code generation
- Significant gap exists between models' ability to generate correct code versus instruction-following code
- Forward and backward constraints generation improves instruction-following capabilities
- Multilingual benchmark reveals consistent patterns across seven programming languages
- Decoupled evaluation metrics enable more nuanced assessment of Code LLM capabilities

**Limitations**: The abstract does not explicitly acknowledge limitations; the instruction-following gap suggests fundamental architectural limitations in current Code LLMs that may require more than constraint-based approaches to resolve.

## References

Chai, L., Yang, J., Liu, S., Zhang, W., Wang, L., Jin, K., Sun, T., Liu, C., Zhang, C., Zhu, H., Liu, J., Wu, X., Zhang, G., Liu, T., & Li, Z. (2025). Multilingual multimodal software developer for code generation. arXiv. https://arxiv.org/abs/2507.08719

Gramacki, P., Martins, B., & Szymański, P. (2024). Evaluation of Code LLMs on geospatial code generation. arXiv. https://arxiv.org/abs/2410.04617

Gupta, M., Bhatt, N., & Jana, S. (2025). CodeSCM: Causal analysis for multi-modal code generation. arXiv. https://arxiv.org/abs/2502.05150

Huang, J., Guo, D., Wang, C., Gu, J., Lu, S., Inala, J. P., Yan, C., Gao, J., Duan, N., & Lyu, M. R. (2024). Contextualized data-wrangling code generation in computational notebooks. arXiv. https://arxiv.org/abs/2409.13551

Huang, J., Mahmud, T., Pasareanu, C., & Yang, G. (2026). CONCUR: Benchmarking LLMs for concurrent code generation. arXiv. https://arxiv.org/abs/2603.03683

Saadi, H. S., Alam, F., Sanz-Guerrero, M., Bui, M. D., Mager, M., & von der Wense, K. (2025). NALA_MAINZ at BLP-2025 Task 2: A multi-agent approach for Bangla instruction to Python code generation. arXiv. https://arxiv.org/abs/2511.16787

Su, H., Jiang, S., Lai, Y., Wu, H., Shi, B., Liu, C., Liu, Q., & Yu, T. (2024). EVOR: Evolving retrieval for code generation. arXiv. https://arxiv.org/abs/2402.12317

Wang, J., Cao, L., Luo, X., Cao, Y., Li, Z., Xiao, Y., Zhao, M., Jatowt, A., & Cai, Y. (2024). Toward secure code generation: Bridging correctness and security via task-adaptive vulnerability modeling and execution-based benchmarking. arXiv. https://arxiv.org/abs/2407.02395

Wu, T., Wu, W., Wang, X., Xu, K., Ma, S., Jiang, B., Yang, P., Xing, Z., Li, Y.-F., & Haffari, G. (2024). VersiCode: Towards version-controllable code generation. arXiv. https://arxiv.org/abs/2406.07411

Yang, J., Zhang, W., Liu, S., Chai, L., Tan, Y., Liu, J., Zhang, G., Zhou, W., Niu, G., Li, Z., Hui, B., & Lin, J. (2025). IFEvalCode: Controlled code generation. arXiv. https://arxiv.org/abs/2507.22462
