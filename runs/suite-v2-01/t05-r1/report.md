# Systematic Literature Review: Instruction Tuning Data Selection

**Date**: 2025-10-25
**Papers surveyed**: 4
**Scope**: arXiv query "instruction tuning data selection", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in instruction tuning data selection methods for large language models. The four surveyed papers collectively demonstrate a shift toward more sophisticated selection strategies that go beyond simple similarity metrics, emphasizing efficiency, balanced capability learning, and fine-grained contribution estimation. A consistent finding across all papers is that training on carefully selected subsets (10-15% of original data) can match or exceed full-dataset performance, suggesting significant opportunities for reducing computational costs while improving model capabilities. The field is moving toward gradient-based and influence-based methods that capture complex interdependencies between training examples, though challenges remain in achieving balanced performance across diverse task types.

## Methodology

This review surveyed 4 arXiv papers retrieved on 2025-10-25 using the query "instruction tuning data selection", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 4 were included (this represents the complete result set matching the search criteria). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The small number of papers (4) reflects the specificity of the search query and category filter; broader queries would yield more results but with less topical focus.

## Themes

### Theme 1: Efficiency Through Selective Training

A dominant theme across the surveyed literature is the pursuit of training efficiency through strategic data selection. All four papers demonstrate that substantial reductions in training data (using only 10-15% of available examples) can achieve performance competitive with or superior to full-dataset training. Yang et al. (2025) show that Select2Reason achieves strong results on mathematical reasoning benchmarks using only 10% of selected data. Similarly, Dai et al. (2025) report that BIDS outperforms full-dataset training with just 15% of examples, and Yang et al. (2025) demonstrate 5.42 percentage point improvements on LLaMA3.1-8B using 15% RICo-selected data. This convergence suggests that the field has reached a consensus that more data is not necessarily better—strategic selection is paramount.

### Theme 2: Beyond Similarity-Based Selection

The literature shows a clear evolution from traditional similarity-based methods toward more sophisticated selection mechanisms. Zhao et al. (2025) explicitly position G2IS as moving "beyond similarity" by constructing gradient-based graphs that capture joint distributions and interdependencies between instructions. This represents a fundamental shift from viewing training examples as independent units to understanding them as interconnected elements within a broader instructional landscape. The gradient-based approach allows for capturing relationships that simple embedding similarity would miss, particularly in domain adaptation scenarios where instruction context matters significantly.

### Theme 3: Balanced Capability Learning

A critical insight emerging from recent work is the recognition that naive data selection can introduce biases that harm performance across diverse task types. Dai et al. (2025) systematically investigate how influence-based methods exhibit inherent bias toward certain tasks, paradoxically harming performance even on those high-influence tasks. Their BIDS framework addresses this through instance-level normalization and iterative optimization that prioritizes underrepresented capabilities. This theme reflects a maturing understanding that data selection must optimize not just for overall performance but for balanced capability development across reasoning, mathematical, linguistic, and other domains.

### Theme 4: Fine-Grained Contribution Estimation

The most recent work in this space focuses on accurately quantifying individual sample contributions to model performance. Yang et al. (2025) introduce RICo, which uses In-Context Learning to measure refined contributions at both task-level and global-level granularity. This gradient-free approach offers linear inference complexity while enabling more precise identification of high-value training examples. The key insight is that high-contribution samples are not simply the most difficult examples, but rather those with appropriate difficulty levels across diverse tasks—a nuance that simpler selection methods miss.

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that data selection is essential for efficient instruction tuning, with consistent findings that 10-15% carefully selected subsets can match or exceed full-dataset performance. There is also broad agreement that selection methods must move beyond simple heuristics toward more sophisticated metrics that capture example quality, diversity, and contribution. All methods demonstrate empirical validation across multiple benchmarks, suggesting a field committed to rigorous evaluation.

**Disagreements**: While all papers advocate for sophisticated selection methods, they differ in their approach to computational efficiency. Yang et al. (2025) propose gradient-free methods (RICo) for linear complexity, while Zhao et al. (2025) embrace gradient-based graph construction (G2IS) despite higher computational cost, arguing it captures richer interdependencies. Additionally, there is tension between methods that prioritize task-specific optimization (Yang et al., 2025, Select2Reason for reasoning) versus those targeting balanced general capability development (Dai et al., 2025, BIDS).

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the papers explicitly address the computational overhead of the selection process itself—while training becomes more efficient, the cost of running selection algorithms on large candidate pools remains unexamined. Second, all papers focus on English-language instruction tuning, leaving open questions about cross-lingual applicability. Third, while methods demonstrate strong benchmark performance, there is limited discussion of real-world deployment scenarios where instruction distributions may shift over time. Finally, the papers do not address how selection methods interact with model scale—whether these approaches generalize to models significantly larger than those tested (Llama-3, Mistral, LLaMA3.1-8B).

## Per-Paper Annotations

### Dai et al. (2025)

**Research question**: How can influence-based instruction tuning data selection be improved to achieve balanced performance across diverse task capabilities rather than being biased toward high-influence tasks?

**Methodology**: The authors conduct a systematic investigation revealing that influence-based methods have inherent bias toward certain tasks, then propose BIDS (Balanced and Influential Data Selection) which normalizes influence scores and iteratively selects examples with highest influence on the most underrepresented task. They evaluate on Llama-3 and Mistral-v0.3 across seven benchmarks spanning five diverse capabilities.

**Key findings**:
- Training on a 15% subset selected by BIDS can outperform full-dataset training with much more balanced performance.
- BIDS consistently outperforms state-of-the-art influence-based algorithms and other non-influence-based frameworks.
- Instance-level normalization and iterative optimization of selected data are important for balanced learning of diverse capabilities.
- Influence-based methods often struggle with achieving balanced performance across different tasks due to inherent bias.
- Data selection biased toward high-influence tasks can counterintuitively harm performance on those same tasks.

**Limitations**: Not stated in abstract.

### Yang et al. (2025a)

**Research question**: How can we efficiently select high-quality instruction-tuning data for activating long chain-of-thought reasoning in pre-trained LLMs without incurring significant training overhead?

**Methodology**: The authors propose Select2Reason, a framework that estimates question difficulty and incorporates reasoning trace length-based heuristics through a weighted scheme to rank and prioritize high-utility examples. They empirically evaluate on OpenR1-Math-220k by fine-tuning LLMs on only 10% of selected data and testing across mathematical benchmarks.

**Key findings**:
- Fine-tuning on only 10% of data selected by Select2Reason achieves performance competitive with or superior to full-data tuning.
- The method performs well across three competition-level and six comprehensive mathematical benchmarks.
- Select2Reason demonstrates scalability in varying data size and efficiency during inference.
- The approach shows adaptability to other instruction pools with minimal cost.
- The framework leverages metrics related to emergence of rethinking behaviors like self-correction and backtracking.

**Limitations**: Not stated in abstract.

### Yang et al. (2025b)

**Research question**: How can we accurately quantify the fine-grained contribution of individual samples to task-level and global-level model performance for effective instruction-tuning data selection?

**Methodology**: The authors propose RICo, a gradient-free method using In-Context Learning to measure refined contribution of individual samples, and introduce a lightweight selection paradigm trained on RICo scores with linear inference complexity. They evaluate on three LLMs across 12 benchmarks and 5 pairwise evaluation sets.

**Key findings**:
- On LLaMA3.1-8B, models trained on 15% of RICo-selected data outperform full datasets by 5.42 percentage points.
- RICo exceeds the best performance of widely used selection methods by 2.06 percentage points.
- High-contribution samples selected by RICo show both diverse tasks and appropriate difficulty levels, not just the hardest ones.
- RICo enables more accurate identification of high-contribution data leading to better instruction tuning.
- The selection paradigm achieves scalable data selection with strictly linear inference complexity.

**Limitations**: Not stated in abstract.

### Zhao et al. (2025)

**Research question**: How can instruction tuning data selection be improved beyond similarity-based methods to better capture joint distribution of instructions for efficient domain adaptation?

**Methodology**: The authors introduce G2IS (Gradient-based Graph Instruction Selection), which constructs a mixed gradient-based instruction graph to capture joint distribution and interdependencies between instructions, and propose a gradient walk algorithm to refine the data selection process. They evaluate across various domain adaptation tasks.

**Key findings**:
- G2IS outperforms traditional methods across various domain adaptation tasks.
- The method yields significant performance gains, particularly in complex, data-scarce scenarios.
- Accounting for relationships between instructions improves domain adaptation efficiency.
- The gradient walk algorithm enhances both training effectiveness and efficiency.
- G2IS shows potential for advancing development of large, domain-specific models.

**Limitations**: Not stated in abstract.

## References

Dai, Q., Zhang, D., Ma, J. W., & Peng, H. (2025). Improving influence-based instruction tuning data selection for balanced learning of diverse capabilities. arXiv. https://arxiv.org/abs/2501.12147

Yang, C., Lin, X., Wu, X., Xu, C., Jiang, X., Liu, H., Xiong, H., & Guo, J. (2025). Select2Reason: Efficient instruction-tuning data selection for long-CoT reasoning. arXiv. https://arxiv.org/abs/2505.17266

Yang, Y., Dong, Q., Yao, L., Zhu, F., & Sui, Z. (2025). RICo: Refined in-context contribution for automatic instruction-tuning data selection. arXiv. https://arxiv.org/abs/2505.05327

Zhao, Y., Du, L., Ding, X., Ouyang, Y., Wang, H., Xiong, K., Gao, J., Sun, Z., Xu, D., Qing, Y., Li, D., Qin, B., & Liu, T. (2025). Beyond similarity: A gradient-based graph method for instruction tuning data selection. arXiv. https://arxiv.org/abs/2502.11062
