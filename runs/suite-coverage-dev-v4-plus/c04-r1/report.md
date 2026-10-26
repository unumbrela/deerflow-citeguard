# Systematic Literature Review: LLM Mid-Training

**Date:** October 26, 2026

**Review Period:** October 27, 2023 – October 26, 2025

**Category:** cs.CL (Computational Linguistics)

---

## Executive Summary

This systematic literature review examines 10 key papers on LLM mid-training published between October 2023 and October 2025. Mid-training, also referred to as continued pre-training, domain adaptation, or intermediate training phases, has emerged as a critical technique for enhancing large language model capabilities. The reviewed papers reveal several important trends: (1) strategic data selection and curation significantly impact model performance, (2) multi-stage training approaches with specialized datasets yield superior results, (3) mid-training enables models to acquire domain-specific capabilities without catastrophic forgetting, and (4) the quality and format of mid-training data directly influences downstream reinforcement learning scalability.

---

## Methodology

### Search Strategy

A systematic search was conducted on arXiv for papers published between October 27, 2023, and October 26, 2025, in the cs.CL (Computational Linguistics) category. The search query focused on "LLM mid-training" and related terms including continued pre-training, domain adaptation, and intermediate training.

### Selection Criteria

Papers were included based on:
- Focus on mid-training techniques, methods, and approaches for large language models
- Coverage of continued pre-training, domain adaptation, and intermediate training phases
- Publication within the specified date range
- Primary category cs.CL

### Screening Process

The initial search identified 32 papers, with an additional 105 papers added through citation expansion, resulting in a shortlist of 30 papers. After screening based on relevance to mid-training, 10 papers were selected for this review.

---

## Annotated Bibliography (APA Format)

### 1. Direct Mid-Training Research

**Wang, Z., Zhou, F., Li, X., & Liu, P. (2025).** OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling. *arXiv preprint arXiv:2506.20512*. https://arxiv.org/abs/2506.20512v1

This is the only paper in our selection that explicitly focuses on mid-training as its primary research question. The authors investigate how mid-training strategies shape reinforcement learning dynamics across Qwen and Llama model families. Key findings include: (1) high-quality mathematical corpora significantly improve both base model and RL performance, (2) adding QA-style data with long chain-of-thought reasoning examples enhances RL outcomes, (3) long-CoT can induce verbosity and training instability, highlighting the importance of data formatting, and (4) scaling mid-training consistently leads to stronger downstream RL performance. The authors introduce a two-stage "Stable-then-Decay" mid-training strategy: first training on 200B tokens with constant learning rate, followed by 20B tokens across three CoT-focused branches with learning rate decay. This approach yields OctoThinker models with strong RL compatibility.

---

### 2. Continued Pre-Training for Domain Specialization

**Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024).** DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*. https://arxiv.org/abs/2402.03300v3

This paper demonstrates mid-training through continued pre-training of DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens. The approach combines mathematical data sourced from Common Crawl with natural language and code data. DeepSeekMath 7B achieved 51.7% on the MATH benchmark without external toolkits, approaching Gemini-Ultra and GPT-4 performance. The success is attributed to: (1) a meticulously engineered data selection pipeline harnessing publicly available web data, and (2) Group Relative Policy Optimization (GRPO) enhancing mathematical reasoning while optimizing PPO memory usage.

**Lu, Y., Zhu, W., Li, L., Qiao, Y., & Yuan, F. (2024).** LLaMAX: Scaling Linguistic Horizons of LLM by Enhancing Translation Capabilities Beyond 100 Languages. *arXiv preprint arXiv:2407.05975*. https://arxiv.org/abs/2407.05975v2

LLaMAX employs extensive multilingual continual pre-training on LLaMA series models to support translation across 100+ languages. The mid-training strategy includes vocabulary expansion and data augmentation without sacrificing generalization ability. LLaMAX achieves significantly higher translation performance (10+ spBLEU points) compared to existing open-source LLMs and performs on-par with specialized translation model M2M-100-12B on Flores-101 benchmark.

**Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., Peters, B., Rei, R., Fernandes, P., Agrawal, S., Colombo, P., de Souza, J. G. C., & Martins, A. F. T. (2024).** Tower: An Open Multilingual Large Language Model for Translation-Related Tasks. *arXiv preprint arXiv:2402.17733*. https://arxiv.org/abs/2402.17733v1

Tower employs continued pretraining on a multilingual mixture of monolingual and parallel data (TowerBase), followed by finetuning on translation-relevant instructions (TowerInstruct). This two-stage mid-training approach creates models that surpass open alternatives on translation workflow tasks and compete with closed general-purpose LLMs. The authors release the specialization dataset, evaluation framework, and model generations.

---

### 3. Multi-Stage Training with Data-Centric Approaches

**Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., & Yang, J. (2025).** Qwen3 Technical Report. *arXiv preprint arXiv:2505.09388*. https://arxiv.org/abs/2505.09388v1

Qwen3 represents a comprehensive series employing sophisticated multi-stage training. The approach includes scaled pre-training datasets (18 trillion tokens vs. 7 trillion in Qwen2.5), intricate supervised finetuning with 1M+ samples, and multistage reinforcement learning. Qwen3 introduces unified thinking/non-thinking modes and a thinking budget mechanism. The series spans 0.6B to 235B parameters in both dense and MoE architectures, achieving state-of-the-art results in code generation, mathematical reasoning, and agent tasks while expanding multilingual support from 29 to 119 languages.

**Qwen, An, Y., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., & Lin, J. (2024).** Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*. https://arxiv.org/abs/2412.15115v2

Qwen2.5 demonstrates significant improvements through enhanced pre-training and post-training stages. Pre-training scaled from 7T to 18T tokens, providing strong foundations for common sense, expert knowledge, and reasoning. Post-training implements intricate supervised finetuning with 1M+ samples and multistage reinforcement learning, enhancing human preference alignment, long text generation, structural data analysis, and instruction following. The flagship Qwen2.5-72B-Instruct performs competitively with Llama-3-405B-Instruct despite being 5× smaller.

**Ben Allal, L., Lozhkov, A., Bakouch, E., Blázquez, G. M., Penedo, G., Tunstall, L., Marafioti, A., Kydlíček, H., Lajarín, A. P., Srivastav, V., Lochner, J., Fahlgren, C., Nguyen, X.-S., Fourrier, C., Burtenshaw, B., Larcher, H., Zhao, H., Zakka, C., Morlon, M., & Raffel, C. (2025).** SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model. *arXiv preprint arXiv:2502.02737*. https://arxiv.org/abs/2502.02737v1

SmolLM2 demonstrates that small models (1.7B parameters) can achieve strong performance through overtraining on ~11T tokens using multi-stage training mixing web text with specialized math, code, and instruction-following data. The authors introduce new specialized datasets (FineMath, Stack-Edu, SmolTalk) and employ a manual refinement process updating dataset mixing rates at each stage based on previous performance. This data-centric mid-training approach enables SmolLM2 to outperform Qwen2.5-1.5B and Llama3.2-1B.

**Wei, Y., Wang, Z., Liu, J., Ding, Y., & Zhang, L. (2023).** Magicoder: Empowering Code Generation with OSS-Instruct. *arXiv preprint arXiv:2312.02120*. https://arxiv.org/abs/2312.02120v2

Magicoder introduces OSS-Instruct, a novel approach using open-source code snippets to generate diverse instruction data for code mid-training. Training on 75K synthetic instruction data mitigates LLM bias through open-source references, producing more realistic and controllable data. MagicoderS-CL-7B (based on CodeLlama) surpasses ChatGPT on HumanEval+ (66.5 vs. 65.9 pass@1), demonstrating the effectiveness of this mid-training data generation approach.

---

### 4. Data Selection and Quality Enhancement for Pre-Training

**Yu, Z., Das, S., & Xiong, C. (2024).** MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models. *arXiv preprint arXiv:2406.06046*. https://arxiv.org/abs/2406.06046v2

MATES introduces model-aware data selection where a data influence model continuously adapts to evolving data preferences during pretraining. Unlike static methods, MATES collects oracle data influence by locally probing the pretraining model and fine-tunes a small influence model to approximate it. The influence model predicts data influence over the entire corpus and selects the most influential data for each pretraining stage. Experiments show MATES significantly outperforms random selection, doubling gains from state-of-the-art reference model approaches and reducing total FLOPs by half to reach target performance.

**Nguyen, T., Li, Y., Golovneva, O., Zettlemoyer, L., Oh, S., Schmidt, L., & Li, X. (2025).** Recycling the Web: A Method to Enhance Pre-training Data Quality and Quantity for Language Models. *arXiv preprint arXiv:2506.04689*. https://arxiv.org/abs/2506.04689v3

REWIRE (REcycling the Web with guIded REwrite) addresses the "data wall" in pre-training scaling by transforming and recycling data discarded in filtering processes. The method enriches low-quality documents to make them useful for training, increasing synthetic data representation. Experiments at 1B, 3B, and 7B scales show mixing high-quality raw texts with rewritten texts improves performance by 1.0, 1.3, and 2.5 percentage points across 22 tasks compared to filtered web data alone. Training on raw-synthetic mixes outperforms having 2× web data, with 82% of mixed data coming from transformed low-quality documents.

---

## Synthesis and Key Findings

### Mid-Training Strategies Identified

1. **Continued Domain-Specific Pre-Training**: Multiple papers demonstrate the effectiveness of continued pre-training on domain-specific data (mathematics, translation, code) after initial general pre-training [Shao et al., 2024; Lu et al., 2024; Alves et al., 2024].

2. **Multi-Stage Training Pipelines**: Successful models employ sophisticated multi-stage approaches with distinct phases for different capabilities [Yang et al., 2025; Qwen et al., 2024; Ben Allal et al., 2025].

3. **Data-Centric Optimization**: The quality, selection, and formatting of mid-training data proves more critical than model architecture changes [Yu et al., 2024; Nguyen et al., 2025; Wei et al., 2023].

4. **RL-Compatible Foundation Models**: Mid-training strategies directly impact downstream reinforcement learning scalability, with specific data types and training schedules enhancing RL compatibility [Wang et al., 2025].

### Common Themes

**Data Quality Over Quantity**: While token counts remain important (ranging from 75K instruction data to 18T pre-training tokens), the emphasis has shifted toward strategic data selection and curation. MATES and REWIRE demonstrate that intelligent data selection can reduce compute requirements by 50% or outperform 2× data scaling.

**Specialized Datasets**: Multiple papers introduce domain-specific datasets (FineMath, Stack-Edu, SmolTalk, MegaMath-Web-Pro-Max) addressing gaps in existing resources, reflecting recognition that generic web data is insufficient for specialized capabilities.

**Iterative Refinement**: Successful approaches employ iterative processes, updating dataset mixing rates and training strategies based on intermediate performance evaluations rather than fixed pipelines.

**Format Matters**: Wang et al. (2025) highlight that data formatting, particularly for chain-of-thought reasoning, critically impacts training stability and downstream performance, suggesting mid-training requires attention beyond content selection.

### Performance Outcomes

The reviewed papers demonstrate that effective mid-training enables:
- Small models (1.7B) to outperform larger competitors through data-centric training [Ben Allal et al., 2025]
- General models to achieve specialist-level performance in domains like mathematics and translation [Shao et al., 2024; Lu et al., 2024]
- 7B models to surpass ChatGPT on specific benchmarks [Wei et al., 2023]
- RL training to scale more effectively with proper mid-training foundations [Wang et al., 2025]

---

## Limitations and Future Directions

### Current Limitations

1. **Limited Direct Mid-Training Research**: Only one paper (OctoThinker) explicitly focuses on mid-training as the primary research question, suggesting this area remains underexplored despite widespread adoption.

2. **Proprietary Data Sources**: Many papers reference carefully curated datasets without full disclosure of selection criteria or data composition, limiting reproducibility.

3. **Compute Requirements**: While MATES demonstrates compute reduction, most approaches still require massive token counts (11T-18T), limiting accessibility.

4. **Domain Specificity**: Most mid-training focuses on specific domains (math, code, translation), with less work on general capability enhancement.

### Future Research Directions

1. **Systematic Mid-Training Frameworks**: Development of generalizable frameworks for mid-training strategy selection based on target capabilities.

2. **Efficiency Improvements**: Research into reducing token requirements while maintaining performance gains from mid-training.

3. **RL Compatibility**: Further investigation into mid-training strategies that optimize for reinforcement learning scalability, as initiated by Wang et al. (2025).

4. **Catastrophic Forgetting**: More research on preventing capability loss during domain-specific mid-training.

5. **Automated Data Selection**: Extension of MATES-style approaches to automate data selection across diverse domains.

---

## Conclusion

LLM mid-training has emerged as a critical technique for enhancing model capabilities, with the 2023-2025 literature demonstrating diverse approaches from continued domain-specific pre-training to sophisticated multi-stage pipelines. The reviewed papers collectively show that strategic data selection, specialized datasets, and iterative refinement processes yield significant performance improvements, sometimes enabling smaller models to outperform larger competitors. While OctoThinker (Wang et al., 2025) provides the only explicit mid-training framework, the widespread adoption of mid-training techniques across all reviewed papers indicates its centrality to modern LLM development. Future research should focus on developing systematic frameworks, improving efficiency, and understanding the mechanisms by which mid-training enhances downstream capabilities, particularly for reinforcement learning applications.

---

## References

Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., Peters, B., Rei, R., Fernandes, P., Agrawal, S., Colombo, P., de Souza, J. G. C., & Martins, A. F. T. (2024). Tower: An open multilingual large language model for translation-related tasks. *arXiv preprint arXiv:2402.17733*. https://arxiv.org/abs/2402.17733v1

Ben Allal, L., Lozhkov, A., Bakouch, E., Blázquez, G. M., Penedo, G., Tunstall, L., Marafioti, A., Kydlíček, H., Lajarín, A. P., Srivastav, V., Lochner, J., Fahlgren, C., Nguyen, X.-S., Fourrier, C., Burtenshaw, B., Larcher, H., Zhao, H., Zakka, C., Morlon, M., & Raffel, C. (2025). SmolLM2: When Smol goes big -- Data-centric training of a small language model. *arXiv preprint arXiv:2502.02737*. https://arxiv.org/abs/2502.02737v1

Lu, Y., Zhu, W., Li, L., Qiao, Y., & Yuan, F. (2024). LLaMAX: Scaling linguistic horizons of LLM by enhancing translation capabilities beyond 100 languages. *arXiv preprint arXiv:2407.05975*. https://arxiv.org/abs/2407.05975v2

Nguyen, T., Li, Y., Golovneva, O., Zettlemoyer, L., Oh, S., Schmidt, L., & Li, X. (2025). Recycling the web: A method to enhance pre-training data quality and quantity for language models. *arXiv preprint arXiv:2506.04689*. https://arxiv.org/abs/2506.04689v3

Qwen, An, Y., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., & Lin, J. (2024). Qwen2.5 technical report. *arXiv preprint arXiv:2412.15115*. https://arxiv.org/abs/2412.15115v2

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*. https://arxiv.org/abs/2402.03300v3

Wang, Z., Zhou, F., Li, X., & Liu, P. (2025). OctoThinker: Mid-training incentivizes reinforcement learning scaling. *arXiv preprint arXiv:2506.20512*. https://arxiv.org/abs/2506.20512v1

Wei, Y., Wang, Z., Liu, J., Ding, Y., & Zhang, L. (2023). Magicoder: Empowering code generation with OSS-Instruct. *arXiv preprint arXiv:2312.02120*. https://arxiv.org/abs/2312.02120v2

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., & Yang, J. (2025). Qwen3 technical report. *arXiv preprint arXiv:2505.09388*. https://arxiv.org/abs/2505.09388v1

Yu, Z., Das, S., & Xiong, C. (2024). MATES: Model-aware data selection for efficient pretraining with data influence models. *arXiv preprint arXiv:2406.06046*. https://arxiv.org/abs/2406.06046v2

---

**Review Methodology Summary:**
- Initial pool: 32 papers from arXiv search
- Citation expansion: +105 papers
- Shortlisted: 30 papers
- Screened and selected: 10 papers
- Format: APA 7th Edition
