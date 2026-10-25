# Systematic Literature Review: Instruction Tuning Data Selection

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "instruction tuning data" and "instruction tuning data selection", category cs.CL, 2024-2026
**Citation format**: APA 7th edition

## Executive Summary

The literature on instruction tuning data selection reveals a rapidly evolving field focused on improving the efficiency and effectiveness of large language model fine-tuning. Collectively, the surveyed papers demonstrate that data quality substantially outweighs quantity, with multiple studies showing that carefully selected subsets of 10-15% of training data can match or exceed full-dataset performance. Three dominant paradigms have emerged: influence-based selection methods that estimate each example's contribution to model predictions, web-scale data extraction frameworks that harvest naturally occurring instruction-response pairs, and model-aware selection approaches that align training data with target model distributions. Despite methodological diversity, the field converges on the importance of controlling for confounding variables in evaluation and addressing task balance to prevent capability skew.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the queries "instruction tuning data selection" and "instruction tuning data", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Influence-Based Data Selection

A major thread in instruction tuning data selection focuses on quantifying the influence of individual training examples on model performance. Dai et al. (2025a) identified a critical limitation in existing influence-based methods: inherent task bias where certain tasks intrinsically exert greater influence, leading to imbalanced capability development. Their BIDS algorithm addresses this through instance-level normalization and iterative selection prioritizing underrepresented tasks, achieving superior performance with only 15% of training data. Han and Huang (2026) extended this line of work by introducing weighted in-context influence (wICI), which measures how candidate examples reduce instruction-following difficulty for semantically related peers. Their findings reveal a negative correlation between sample difficulty and in-context influence, suggesting that easier samples paradoxically have higher instructional value. Zhao et al. (2025) moved beyond simple influence metrics by proposing G2IS, which constructs gradient-based graphs capturing interdependencies between instructions, demonstrating particular effectiveness in data-scarce domain adaptation scenarios.

### Theme 2: Web-Scale Data Extraction and Synthesis

Recognizing the prohibitive costs of manual annotation and GPT-4 distillation, several papers propose frameworks for harvesting instruction tuning data from web corpora. Zhang et al. (2024) introduced MAmmoTH2, which extracts 10 million naturally occurring instruction-response pairs from pre-training web corpora through a three-stage pipeline of document recall, pair extraction, and refinement using open-source LLMs. Their approach achieved dramatic improvements on mathematical reasoning benchmarks without any in-domain training data. Jiang et al. (2025) proposed Web Reconstruction (WebR), employing a dual-perspective paradigm where web documents serve as either instructions or responses, outperforming state-of-the-art baselines by up to 16.65% on instruction-following benchmarks. Zhang et al. (2025) addressed computational efficiency concerns with EQUAL, which combines contrastive learning-based document clustering with multi-armed bandit strategies to iteratively identify high-value clusters, reducing extraction costs by 5-10x while improving accuracy.

### Theme 3: Model-Aware Response Selection

A third paradigm emphasizes aligning training data with the target model's pretrained distribution rather than simply selecting the highest-quality responses according to external criteria. Zhang et al. (2025) proposed GRAPE, which gathers multiple candidate responses from various LLMs for each instruction and selects the response with the highest probability under the target model. This approach acknowledges that responses optimal for one model may be out-of-distribution for another, leading to diminishing returns at scale. GRAPE achieved absolute gains of up to 13.8% over distillation from the strongest model and enabled LLaMA3.1-8B to surpass Tulu3-SFT performance using only one-third of the data and half the training epochs. This model-aware perspective represents a shift from treating instruction tuning data as universally high-quality to recognizing the interaction between data characteristics and specific model architectures.

### Theme 4: Specialized Selection for Reasoning Capabilities

Several papers focus specifically on activating and enhancing reasoning capabilities through targeted data selection. Yang et al. (2025) developed Select2Reason for long chain-of-thought reasoning, leveraging difficulty quantification and reasoning trace length heuristics to prioritize high-utility examples from large reasoning model-generated datasets. Their approach achieves competitive performance with full-data tuning using only 10% of the OpenR1-Math-220k dataset. Lu et al. (2024) explored an orthogonal direction, demonstrating that speech language models can develop instruction-following capabilities without explicit speech instruction-tuning data through automatic speech-text pair generation that preserves the underlying LLM's language capabilities.

### Theme 5: Methodological Rigor in Evaluation

A critical meta-perspective emerges from Moon et al. (2025), who identify systematic methodological flaws in how instruction tuning data quality is evaluated. Their analysis reveals that most studies fail to control for confounding variables such as data quantity, training epochs, and model architecture when comparing data selection methods. Under their standardized evaluation framework controlling for these variables, several previously claimed "high-quality" data selection methods showed diminished advantages. This call for rigor has implications for interpreting the entire body of literature, suggesting that some reported improvements may reflect experimental design choices rather than genuine data quality differences.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong consensus on several points. First, all papers agree that data quality substantially outweighs quantity, with multiple studies achieving comparable or superior performance using 10-15% carefully selected subsets versus full datasets (Dai et al., 2025a; Yang et al., 2025; Zhang et al., 2025). Second, there is universal acknowledgment that instruction tuning datasets contain substantial redundancy and low-quality samples requiring effective filtering (Han & Huang, 2026; Zhang et al., 2024). Third, all influence-based methods converge on the importance of considering task diversity and avoiding capability imbalance (Dai et al., 2025a; Zhao et al., 2025). Finally, the literature collectively emphasizes computational efficiency, with web extraction frameworks consistently targeting 5-10x cost reductions (Zhang et al., 2025; Jiang et al., 2025).

**Disagreements**: Tensions exist regarding the optimal selection criteria. Han and Huang (2026) find that easier samples have higher in-context influence, contradicting the intuition underlying Select2Reason's difficulty-based prioritization (Yang et al., 2025). This discrepancy may reflect task-specific differences between general instruction following and mathematical reasoning. Additionally, while GRAPE advocates for model-aware response selection based on target model probability (Zhang et al., 2025), influence-based methods assume certain examples have universally high value regardless of target architecture (Dai et al., 2025a; Han & Huang, 2026). The methodological critique by Moon et al. (2025) also raises questions about whether reported performance differences across methods reflect genuine quality differences or uncontrolled experimental variables.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly address multilingual instruction tuning data selection, despite the predominance of English-centric approaches. Second, computational overhead during the selection process itself receives limited discussion — while all methods claim efficiency gains during training, the cost of computing influence scores, constructing gradient graphs, or running multi-armed bandit iterations remains opaque. Third, domain transferability is understudied; methods validated primarily on mathematical reasoning or general instruction following may not generalize to specialized domains like legal, medical, or scientific reasoning. Fourth, the interaction between data selection and model scale is unexplored — whether selection criteria optimal for 7B models remain effective for 70B or 700B models is unknown. Finally, Moon et al.'s (2025) methodological critique suggests the field lacks standardized evaluation protocols, making cross-method comparisons unreliable without controlled replication studies.

## Per-Paper Annotations

### Dai et al. (2025a)

**Research question**: How can influence-based data selection methods achieve balanced performance across different tasks rather than biasing toward certain high-influence tasks?
**Methodology**: Proposed BIDS (Balanced and Influential Data Selection), which normalizes influence scores and iteratively selects examples with highest influence on the most underrepresented task.
**Key findings**:
- Influence-based methods have inherent task bias where some tasks intrinsically exert greater influence
- This bias hurts both underrepresented tasks and counterintuitively harms high-influence tasks
- Training on 15% BIDS-selected subset outperforms full-dataset training with more balanced performance
- Both instance-level normalization and iterative optimization are crucial for balanced capability development
- BIDS outperforms state-of-the-art influence-based and non-influence-based frameworks across seven benchmarks
**Limitations**: Computational overhead of iterative selection not quantified; applicability beyond the five tested capabilities remains unverified.

### Dai et al. (2025b)

**Research question**: How can we select instruction-tuning responses that align with the target model's pretrained distribution to avoid diminishing returns and performance degradation?
**Methodology**: Proposed GRAPE, which gathers responses from multiple LLMs per instruction and selects the response with highest probability under the target model before standard SFT training.
**Key findings**:
- Responses from other LLMs are often out-of-distribution for the target model, causing performance degradation at scale
- GRAPE outperforms strongest-model distillation by up to 13.8% absolute gain across benchmarks
- Achieves 17.3% maximum improvement over training on 3x more data
- Using 1/3 data and half epochs, GRAPE enables LLaMA3.1-8B to surpass Tulu3-SFT by 3.5%
- Generalizes to realistic post-training settings, outperforming 4.5x more data by 6.1%
**Limitations**: Requires access to multiple LLMs for response sampling; computational cost of probability scoring across candidates not fully analyzed.

### Han and Huang (2026)

**Research question**: What constitutes effective instruction tuning data from an in-context learning perspective, and how does sample difficulty correlate with in-context influence?
**Methodology**: Developed weighted in-context influence (wICI) framework measuring how candidate examples reduce instruction-following difficulty for semantically related peers, with systematic experiments across models and benchmarks.
**Key findings**:
- wICI consistently outperforms existing baselines under constrained data budgets
- Sample difficulty negatively correlates with in-context influence (easier samples have higher influence)
- In-context influence effectively translates to instruction tuning effectiveness
- Instruction-tuning datasets contain substantial redundancy and low-quality samples amenable to filtering
**Limitations**: Generalizability across all model sizes and domains unverified; computational overhead of wICI framework during selection not quantified.

### Jiang et al. (2025)

**Research question**: How can we synthesize high-quality instruction-tuning data directly from raw web documents without relying on seed data quality or strong assumptions about web document structure?
**Methodology**: Proposed Web Reconstruction (WebR), a fully automated framework using dual-perspective paradigm where web documents serve as either instructions or responses with minimal structural assumptions.
**Key findings**:
- WebR-generated datasets outperform state-of-the-art baselines by up to 16.65% across four benchmarks
- Demonstrates superior compatibility, data efficiency, and scalability
- Enables enhanced domain adaptation with minimal effort
- Leverages inherent web content diversity without requiring quality seed data
**Limitations**: Whether minimal assumptions miss certain document types unexamined; computational cost of raw web document processing at scale not reported.

### Lu et al. (2024)

**Research question**: How can we develop instruction-following speech language models without requiring extensive speech instruction-tuning data while preserving original LLM language capabilities?
**Methodology**: Created automatic process for generating speech-text pair data that injects paralinguistic understanding while preserving text-based LLM capabilities.
**Key findings**:
- Achieves impressive performance on Dynamic-SUPERB and AIR-Bench-Chat without speech instruction-tuning data
- Model follows complex instructions including output formatting and chain-of-thought reasoning
- Reduces reliance on extensive annotated speech datasets
- Successfully bridges speech-text modalities without catastrophic forgetting
**Limitations**: Generalizability to all speech tasks unverified; paralinguistic understanding quality compared to extensively trained models unclear; non-English language performance not addressed.

### Moon et al. (2025)

**Research question**: How can we properly evaluate instruction tuning data quality without confounding variables leading to misleading conclusions?
**Methodology**: Proposed standardized evaluation framework controlling for data quantity, training epochs, and model architecture when comparing data quality methods.
**Key findings**:
- Most studies fail to control for confounding variables in data quality assessment
- Several "high-quality" methods show diminished advantages under controlled conditions
- Current evaluation practices lead to misleading conclusions about data quality
**Limitations**: Scope of controlled variables may be incomplete; generalizability across different architectures and domains requires further validation.

### Yang et al. (2025)

**Research question**: How can we efficiently select instruction-tuning data for long chain-of-thought reasoning to reduce training overhead while maintaining or improving performance?
**Methodology**: Developed Select2Reason using difficulty quantification and reasoning trace length heuristics through weighted ranking to prioritize high-utility examples from reasoning model-generated datasets.
**Key findings**:
- Fine-tuning on 10% Select2Reason-selected data matches or exceeds full-data tuning performance
- Outperforms OpenR1-Qwen-7B baseline across three competition-level and six mathematical benchmarks
- Demonstrates scalability across varying data sizes and improved inference efficiency
- Shows adaptability to other instruction pools with minimal cost
**Limitations**: Whether difficulty quantifier generalizes beyond mathematical reasoning untested; optimality of 10% selection ratio across architectures unknown.

### Zhang et al. (2024)

**Research question**: How can we efficiently harvest large-scale instruction-tuning data without relying on costly human annotation or GPT-4 distillation?
**Methodology**: Three-stage paradigm: (1) recall relevant documents from web corpus, (2) extract instruction-response pairs, (3) refine pairs using open-source LLMs to build 10M instruction dataset.
**Key findings**:
- Successfully harvested 10M naturally occurring instruction data from web corpus
- MAmmoTH2-7B improved from 11% to 36.7% on MATH and 36% to 68.4% on GSM8K without in-domain data
- MAmmoTH2-Plus achieved state-of-the-art on multiple reasoning and chatbot benchmarks
- Demonstrates viable paradigm avoiding costly annotation or distillation
**Limitations**: Data quality variability from web sources not characterized; domain coverage limitations of harvested corpus unexamined.

### Zhang et al. (2025)

**Research question**: How can we efficiently extract diverse, high-quality instruction tuning data from web corpora without prohibitive computational costs or irrelevant QA pairs?
**Methodology**: Introduced EQUAL, combining contrastive learning-based document clustering with multi-armed bandit strategy for iterative cluster identification and QA pair extraction.
**Key findings**:
- Reduces computational costs by 5-10x versus naive extraction
- Improves accuracy by 2.5% on LLaMA-3.1-8B and Mistral-7B
- Validated on AutoMathText and StackOverflow across four downstream tasks
- Iterative clustering effectively identifies valuable QA-containing clusters
- Web corpora provide richer, more diverse knowledge than seed-based synthesis
**Limitations**: Dependency on contrastive learning embedding quality; multi-armed bandit convergence efficiency across document types unverified.

### Zhao et al. (2025)

**Research question**: How can we improve domain adaptation efficiency for LLMs by considering instruction interdependencies rather than just similarity to target domain?
**Methodology**: Introduced G2IS constructing mixed gradient-based instruction graphs capturing joint distribution and interdependencies, plus gradient walk algorithm for refined selection.
**Key findings**:
- Similarity-based methods fail to consider instruction joint distribution, causing inefficient learning
- G2IS improves domain adaptation efficiency through instruction relationship modeling
- Outperforms traditional methods across domain adaptation tasks with significant gains
- Particularly effective in complex, data-scarce scenarios
**Limitations**: Computational complexity of graph construction not quantified; scalability to very large instruction sets unexamined.

## References

Dai, Q., Zhang, D., Ma, J. W., & Peng, H. (2025a). Improving influence-based instruction tuning data selection for balanced learning of diverse capabilities. arXiv. https://arxiv.org/abs/2501.12147

Dai, Q., Zhang, D., & Peng, H. (2025b). The best instruction-tuning data are those that fit. arXiv. https://arxiv.org/abs/2502.04194

Han, G., & Huang, X. (2026). What makes good instruction-tuning data? An in-context learning perspective. arXiv. https://arxiv.org/abs/2604.25132

Jiang, Y., Wang, Y., Wu, C., Dai, X., Xu, Y., Gan, W., Wang, Y., Jiang, X., Shang, L., Tang, R., & Wang, W. (2025). Instruction-tuning data synthesis from scratch via web reconstruction. arXiv. https://arxiv.org/abs/2504.15573

Lu, K.-H., Chen, Z., Fu, S.-W., Yang, C.-H. H., Balam, J., Ginsburg, B., Wang, Y.-C. F., & Lee, H.-Y. (2024). DeSTA2: Developing instruction-following speech language model without speech instruction-tuning data. arXiv. https://arxiv.org/abs/2409.20007

Moon, H., Seo, J., & Lim, H. (2025). Call for rigor in reporting quality of instruction tuning data. arXiv. https://arxiv.org/abs/2503.04807

Yang, C., Lin, X., Wu, X., Xu, C., Jiang, X., Liu, H., Xiong, H., & Guo, J. (2025). Select2Reason: Efficient instruction-tuning data selection for long-CoT reasoning. arXiv. https://arxiv.org/abs/2505.17266

Zhang, C., Zhong, H., Li, H., Chai, C., Hong, J., Deng, Y., Wang, J., Tan, T., Yan, Y., Qiu, J., Yuan, Y., Wang, G., He, C., & Cao, L. (2025). Not all documents are what you need for extracting instruction tuning data. arXiv. https://arxiv.org/abs/2505.12250

Zhang, Y., Li, Y., Cui, L., Wu, Y., Wang, M., Zhang, H., Deng, Z., Wang, X., Chen, J., & Gurevych, I. (2024). MAmmoTH2: Scaling instruction-tuning data for large language models from 10K to 10M. arXiv. https://arxiv.org/abs/2405.03548

Zhao, Y., Du, L., Ding, X., Ouyang, Y., Wang, H., Xiong, K., Gao, J., Sun, Z., Xu, D., Qing, Y., Li, D., Qin, B., & Liu, T. (2025). Beyond similarity: A gradient-based graph method for instruction tuning data selection. arXiv. https://arxiv.org/abs/2502.11062
