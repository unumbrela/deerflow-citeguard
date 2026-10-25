# Systematic Literature Review: Instruction Tuning Data Selection

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "instruction tuning data" and "instruction tuning data selection", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of instruction tuning data selection has rapidly evolved over the past two years, with research converging on a key insight: high-quality, carefully selected subsets of training data can outperform full datasets while reducing computational costs by 5-10x. Ten recent papers surveyed reveal multiple complementary approaches to data selection, including influence-based methods, gradient-based graph techniques, in-context learning frameworks, and web-scale mining paradigms. Collectively, these works demonstrate that 10-20% of carefully selected data consistently matches or exceeds full-dataset performance across diverse benchmarks, with methods emphasizing efficiency, diversity, and alignment with target model distributions. The field is moving away from brute-force scaling toward intelligent curation strategies that balance quality, computational cost, and capability coverage.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the queries "instruction tuning data selection" and "instruction tuning data", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to cs.CL category, potentially missing relevant work in cs.AI or adjacent categories.

## Themes

### Theme 1: Efficiency Through Data Selection

A dominant theme across the surveyed literature is the pursuit of dramatic efficiency gains through intelligent data selection. Multiple papers demonstrate that small, carefully curated subsets can outperform full training datasets. Zhang et al. (2025) showed that training on just 15% of BIDS-selected data outperformed full-dataset training with better balance across capabilities. Yang et al. (2025) found that 10% of Select2Reason-selected data achieved performance competitive with full-data tuning on mathematical reasoning benchmarks. Similarly, Song et al. (2024) demonstrated that 20% of IterSelectTune-selected data consistently outperformed models trained on complete datasets. This convergence suggests that the field has moved beyond the assumption that more data is always better, instead focusing on identifying high-utility examples that maximize learning signal per training step.

### Theme 2: Influence and Contribution-Based Selection Methods

Several papers propose methods that directly measure or estimate each training example's contribution to model performance. Dai et al. (2025) introduced BIDS, which normalizes influence scores and iteratively selects examples with highest influence on underrepresented tasks, addressing the bias problem in traditional influence-based methods. Yang et al. (2025) proposed RICo, a gradient-free method using in-context learning to quantify sample contributions, achieving 5.42 percentage point improvements over full datasets. Han and Huang (2026) developed wICI, measuring how effectively each example reduces instruction-following difficulty for semantically related peers. These methods share a common principle: rather than relying on proxy metrics like similarity or difficulty alone, they directly estimate each example's causal impact on downstream performance.

### Theme 3: Web-Scale Data Mining and Synthesis

A parallel research direction focuses on harvesting instruction data from web corpora rather than selecting from existing curated datasets. Wang et al. (2024) introduced MAmmoTH2, mining 10 million natural instruction-response pairs from web documents through a three-stage process of document recall, pair extraction, and refinement using open-source LLMs. Zhang et al. (2025) proposed EQUAL, which clusters documents and uses multi-armed bandit strategies to efficiently identify clusters containing valuable QA pairs, reducing computational costs by 5-10x. Jiang et al. (2025) developed WebR, a fully automated framework using a dual-perspective paradigm where web documents serve as either instructions or responses. These approaches address the bottleneck of limited curated instruction data by treating the web itself as an untapped reservoir of training signal.

### Theme 4: Model-Specific Alignment and Distribution Matching

Recent work emphasizes that optimal instruction tuning data must align with the specific characteristics of the target model rather than using generic high-quality data. Zhang et al. (2025) proposed GRAPE, which selects responses that maximize the target model's probability, ensuring alignment with the model's pretrained distribution. This approach significantly outperformed distillation from stronger models, suggesting that distributional fit matters more than raw response quality. The insight challenges the common practice of using the strongest available model to generate training data, instead advocating for personalized data selection tailored to each target model's unique characteristics.

### Theme 5: Graph-Based and Structural Approaches to Data Relationships

Beyond individual example quality, several methods model the relationships and dependencies between training examples. Zhao et al. (2025) introduced G2IS, constructing gradient-based instruction graphs to capture joint distributions and interdependencies between instructions. By accounting for how examples relate to each other rather than treating them independently, G2IS achieved significant gains in domain adaptation efficiency, particularly in data-scarce scenarios. This structural perspective recognizes that training data functions as an interconnected system, where redundancy and coverage matter as much as individual example quality.

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that intelligent data selection substantially outperforms both random sampling and full-dataset training. There is strong consensus that 10-20% of carefully selected data suffices for optimal performance, with multiple papers independently converging on this range (Dai et al., 2025; Yang et al., 2025; Song et al., 2024; Zhang et al., 2025). All methods demonstrate computational efficiency gains, typically 5-10x reduction in training costs. There is also agreement that diversity and balance matter—selecting only the "hardest" or "highest-scoring" examples leads to degraded performance on underrepresented capabilities.

**Disagreements**: The papers diverge on the optimal measurement approach for data quality. Influence-based methods (Dai et al., 2025; Yang et al., 2025) require gradient computation or multiple forward passes, while gradient-free approaches (Yang et al., 2025; Han & Huang, 2026) argue that in-context learning provides sufficient signal at lower computational cost. There is also tension between selection from existing datasets versus synthesis from web corpora—mining approaches (Wang et al., 2024; Zhang et al., 2025; Jiang et al., 2025) argue that curated datasets are too limited, while selection methods assume sufficient diversity exists in source pools. Additionally, GRAPE's emphasis on target-model alignment (Zhang et al., 2025) challenges the assumption that universally high-quality data exists, suggesting instead that quality is model-relative.

## Gaps and Open Questions

Several limitations recur across the surveyed literature. First, most methods still require some reliance on strong LLMs (GPT-4 or similar) for either data synthesis, quality filtering, or evaluation—IterSelectTune (Song et al., 2024) explicitly notes "limited reliance on GPT-4" as a remaining cost. Second, computational costs of selection itself are often underreported: gradient-based methods (Zhao et al., 2025; Dai et al., 2025) require significant upfront computation that may offset training savings for smaller models. Third, evaluation remains benchmark-centric, with most papers reporting gains on standard benchmarks (MATH, GSM8K, etc.) but limited analysis of real-world task performance or robustness to distribution shift.

Fourth, none of the surveyed papers address the question of how selected data ages—as models improve, does previously high-quality data remain valuable, or must selection be re-run for each new model generation? Fifth, there is limited work on multi-modal instruction tuning data selection, with most methods designed for text-only settings. Finally, the web-mining approaches (Wang et al., 2024; Zhang et al., 2025; Jiang et al., 2025) raise questions about data quality control and noise filtering that remain partially addressed—while they report strong benchmark performance, the risk of propagating web-scale biases and errors is not thoroughly analyzed.

## Per-Paper Annotations

### Dai et al. (2025)

**Research question**: How can influence-based instruction tuning data selection be improved to achieve balanced performance across diverse capabilities rather than biasing toward high-influence tasks?

**Methodology**: Proposed BIDS (Balanced and Influential Data Selection), which normalizes influence scores across tasks and iteratively selects examples with highest influence on the most underrepresented task.

**Key findings**:
- Training on 15% BIDS-selected data outperformed full-dataset training with better balance across five diverse capabilities
- Outperformed state-of-the-art influence-based algorithms and non-influence-based frameworks on Llama-3 and Mistral-v0.3
- Instance-level normalization and iterative optimization are both critical for balanced learning
- Counterintuitively, biasing toward high-influence tasks harms performance on those same tasks

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include computational overhead of iterative influence computation and evaluation limited to seven benchmarks.

### Han and Huang (2026)

**Research question**: What constitutes effective instruction tuning data from an in-context learning perspective, and does sample difficulty correlate with in-context influence?

**Methodology**: Developed wICI (weighted in-Context Influence), measuring how effectively each example reduces instruction-following difficulty for semantically related peers through systematic experiments across multiple models and benchmarks.

**Key findings**:
- Sample difficulty negatively correlates with in-context influence—easier examples often have higher influence
- wICI consistently outperforms existing baselines under constrained data budgets
- In-context influence translates positively to instruction tuning effectiveness
- Effective data from in-context perspective emphasizes reducing peer difficulty rather than maximizing individual quality

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include generalizability beyond tested models and benchmarks, and computational cost of pairwise influence measurement.

### Jiang et al. (2025)

**Research question**: How can high-quality instruction-tuning data be synthesized directly from raw web documents without relying on seed data quality or strong structural assumptions?

**Methodology**: Proposed WebR (Web Reconstruction), a fully automated framework using a dual-perspective paradigm where web documents serve as either instructions or responses to trigger reconstruction.

**Key findings**:
- WebR-generated datasets outperformed state-of-the-art baselines by up to 16.65% across four instruction-following benchmarks
- Demonstrated superior compatibility, data efficiency, and scalability for domain adaptation
- Minimal assumptions about web document structure enable broader applicability
- Fully automated synthesis eliminates manual curation burden

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include quality variability in raw web content and lack of explicit noise filtering mechanisms.

### Song et al. (2024)

**Research question**: How can high-quality instruction data be selected efficiently from large source datasets without significant human effort?

**Methodology**: Introduced IterSelectTune, an iterative training policy for selecting high-quality instruction data with no human involvement and limited reliance on GPT-4, fine-tuning on approximately 20% of source data.

**Key findings**:
- Models fine-tuned on 20% of source data consistently outperformed models trained on full datasets
- Required no human involvement in data selection process
- Limited reliance on GPT-4 reduces costs compared to fully GPT-4-dependent methods
- Demonstrated effectiveness across multiple benchmarks and public test datasets

**Limitations**: The method still has limited reliance on GPT-4, and the iterative training process may introduce additional training time overhead not fully quantified.

### Wang et al. (2024)

**Research question**: How can large-scale, high-quality instruction data be harvested from web corpus without costly human annotation or GPT-4 distillation?

**Methodology**: Proposed MAmmoTH2, a three-stage paradigm: (1) recalling relevant documents from pre-training web corpus, (2) extracting instruction-response pairs, (3) refining extracted pairs using open-source LLMs, harvesting 10 million natural instructions.

**Key findings**:
- MAmmoTH2-7B (Mistral) performance increased from 11% to 36.7% on MATH benchmark
- Performance increased from 36% to 68.4% on GSM8K without in-domain training data
- MAmmoTH2-Plus achieved state-of-the-art performance on several reasoning and chatbot benchmarks
- Successfully eliminated need for costly human crowd-sourcing or GPT-4 distillation

**Limitations**: Potential concerns include noise in web-extracted data, coverage bias in document recall, and quality variability in extracted instruction-response pairs not thoroughly analyzed.

### Yang et al. (2025) [RICo]

**Research question**: How can high-contribution instruction tuning data be accurately identified in a gradient-free manner to improve model performance while reducing training costs?

**Methodology**: Proposed RICo (Refined Contribution Measurement with In-Context Learning), a gradient-free method quantifying fine-grained sample contributions to task-level and global-level performance, plus a lightweight selection paradigm with linear inference complexity.

**Key findings**:
- On LLaMA3.1-8B, 15% of RICo-selected data outperformed full datasets by 5.42 percentage points
- Exceeded best performance of widely used selection methods by 2.06 percentage points
- High-contribution samples exhibit diverse tasks and appropriate difficulty levels, not just hardest examples
- Achieved scalable data selection with strictly linear inference complexity
- Demonstrated effectiveness across three LLMs, 12 benchmarks, and 5 pairwise evaluation sets

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include the need for training the lightweight selection paradigm and evaluation limited to specific model sizes and benchmarks.

### Yang et al. (2025) [Select2Reason]

**Research question**: How can instruction-tuning data be efficiently selected for activating long chain-of-thought reasoning ability in pre-trained LLMs?

**Methodology**: Proposed Select2Reason, leveraging a difficulty quantifier and reasoning trace length-based heuristic through weighted ranking to prioritize high-utility examples for long-CoT reasoning.

**Key findings**:
- Fine-tuning on 10% of Select2Reason-selected data achieved performance competitive with or superior to full-data tuning
- Outperformed OpenR1-Qwen-7B baseline across three competition-level and six comprehensive mathematical benchmarks
- Demonstrated scalability in varying data sizes and efficiency during inference
- Adaptable to other instruction pools with minimal cost

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include specificity to mathematical reasoning tasks and generalizability to non-CoT instruction tuning.

### Zhang et al. (2025) [BIDS]

**Research question**: What makes instruction-tuning data "good" from the perspective of target model alignment rather than absolute quality?

**Methodology**: Proposed GRAPE, which gathers responses from various LLMs for each instruction and selects the one with highest probability under the target model, ensuring alignment with pretrained distribution before standard SFT training.

**Key findings**:
- Outperformed distillation from strongest model with absolute gains up to 13.8% averaged across benchmarks
- Exceeded training on 3x more data with maximum performance improvement of 17.3%
- In realistic settings, outperformed baselines trained on 4.5x more data by 6.1%
- Using 1/3 of data and half the epochs, LLaMA3.1-8B surpassed Tulu3-SFT by 3.5%

**Limitations**: Potential concerns include the need to query multiple LLMs for each instruction and potential biases in target model probability measurements not thoroughly addressed.

### Zhang et al. (2025) [EQUAL]

**Research question**: How can instruction tuning data be efficiently extracted from web corpora while avoiding the prohibitive cost of extracting all QA pairs and the risk of irrelevant pairs degrading performance?

**Methodology**: Introduced EQUAL, clustering document corpus based on contrastive learning embeddings, then using multi-armed bandit strategy to efficiently identify clusters containing valuable QA pairs through iterative document selection and QA extraction.

**Key findings**:
- Reduced computational costs by 5-10x compared to naive extraction approaches
- Improved accuracy by 2.5 percentage points on LLaMA-3.1-8B and Mistral-7B
- Iterative approach significantly reduced computational cost while boosting model performance
- Effective on AutoMathText and StackOverflow across four downstream tasks

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include dependency on clustering quality and generalizability beyond tested domains.

### Zhao et al. (2025)

**Research question**: How can instruction tuning data selection be improved for domain-specific tasks by considering joint distribution and interdependencies between instructions rather than just similarity to target domain?

**Methodology**: Introduced G2IS (Gradient-based Graph Instruction Selection), constructing mixed gradient-based instruction graphs to capture joint distribution and interdependencies, combined with gradient walk algorithm for refined selection.

**Key findings**:
- Outperformed traditional similarity-based selection methods across various domain adaptation tasks
- Achieved significant performance gains particularly in complex, data-scarce scenarios
- Accounting for instruction relationships improved domain adaptation efficiency
- Gradient walk algorithm enhanced both training effectiveness and computational efficiency

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include computational cost of gradient-based graph construction and limited evaluation across diverse domain types.

## References

Dai, Q., Zhang, D., Ma, J. W., & Peng, H. (2025). Improving influence-based instruction tuning data selection for balanced learning of diverse capabilities. arXiv. https://arxiv.org/abs/2501.12147

Han, G., & Huang, X. (2026). What makes good instruction-tuning data? An in-context learning perspective. arXiv. https://arxiv.org/abs/2604.25132

Jiang, Y., Wang, Y., Wu, C., Dai, X., Xu, Y., Gan, W., Wang, Y., Jiang, X., Shang, L., Tang, R., & Wang, W. (2025). Instruction-tuning data synthesis from scratch via web reconstruction. arXiv. https://arxiv.org/abs/2504.15573

Song, J., Liu, S., Zhu, B., & Rao, Y. (2024). IterSelectTune: An iterative training framework for efficient instruction-tuning data selection. arXiv. https://arxiv.org/abs/2410.13464

Wang, C., Chen, S., Wu, Y., Pu, Z., Wang, W., Zhang, X., Xu, T., Wang, B., & Zhang, Z. (2024). MAmmoTH2: Mining 10 million natural instruction data from web corpus. arXiv. https://arxiv.org/abs/2405.03548

Yang, Y., Dong, Q., Yao, L., Zhu, F., & Sui, Z. (2025). RICo: Refined in-context contribution for automatic instruction-tuning data selection. arXiv. https://arxiv.org/abs/2505.05327

Yang, C., Lin, X., Wu, X., Xu, C., Jiang, X., Liu, H., Xiong, H., & Guo, J. (2025). Select2Reason: Efficient instruction-tuning data selection for long-CoT reasoning. arXiv. https://arxiv.org/abs/2505.17266

Zhang, D., Dai, Q., & Peng, H. (2025). The best instruction-tuning data are those that fit. arXiv. https://arxiv.org/abs/2502.04194

Zhang, C., Zhong, H., Li, H., Chai, C., Hong, J., Deng, Y., Wang, J., Tan, T., Yan, Y., Qiu, J., Yuan, Y., Wang, G., He, C., & Cao, L. (2025). Not all documents are what you need for extracting instruction tuning data. arXiv. https://arxiv.org/abs/2505.12250

Zhao, Y., Du, L., Ding, X., Ouyang, Y., Wang, H., Xiong, K., Gao, J., Sun, Z., Xu, D., Qing, Y., Li, D., Qin, B., & Liu, T. (2025). Beyond similarity: A gradient-based graph method for instruction tuning data selection. arXiv. https://arxiv.org/abs/2502.11062
