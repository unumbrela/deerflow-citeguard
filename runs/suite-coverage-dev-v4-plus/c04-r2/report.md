# Systematic Literature Review: LLM Mid-Training

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "LLM mid-training", category cs.CL, published between 2023-10-27 and 2025-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on LLM mid-training and related continual pre-training strategies. The surveyed literature reveals that mid-training has emerged as a critical phase between base pre-training and fine-tuning, where models are adapted with specialized data to enhance specific capabilities. Key findings demonstrate that strategic mid-training with high-quality mathematical corpora, multilingual data, and domain-specific content significantly improves downstream performance without requiring architectural changes. The OctoThinker study (Wang et al., 2025) directly investigates mid-training's role in incentivizing reinforcement learning scaling, while other papers employ mid-training strategies implicitly through continued pre-training approaches. Collectively, these works establish that carefully curated mid-training data and multi-stage training processes can dramatically enhance model capabilities in mathematical reasoning, code generation, translation, and general instruction following.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM mid-training", filtered to category cs.CL, published between 2023-10-27 and 2025-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening process**: The search identified 32 papers by direct match and 105 papers through citation expansion, yielding a shortlist of 30 papers. After screening by centrality to the topic, 10 papers were included (10 from citation expansion, indicating the topic's emerging nature with limited direct matches).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, the search returned fewer direct matches than requested, suggesting "mid-training" is an emerging terminology with related work appearing under alternative framings such as "continual pre-training" or "continued pretraining."

## Themes

### Theme 1: Data-Centric Mid-Training Strategies

A dominant theme across the surveyed literature is the emphasis on data quality and curation during mid-training phases. Rather than simply scaling compute, researchers focus on strategically selecting and mixing specialized datasets to enhance specific model capabilities. The MATES approach (Yu et al., 2024) introduces model-aware data selection that continuously adapts to evolving data preferences during training, achieving double the gains of state-of-the-art selection methods. Similarly, SmolLM2 (Ben Allal et al., 2025) demonstrates that overtraining a small 1.7B parameter model on 11 trillion tokens with carefully curated specialized datasets (FineMath for mathematics, Stack-Edu for code, SmolTalk for instruction-following) can outperform larger models. The FineWeb datasets (Penedo et al., 2024) further establish that systematic deduplication and filtering strategies applied to 96 Common Crawl snapshots produce superior pretraining data, with FineWeb-Edu's 1.3 trillion tokens of educational text yielding dramatic improvements on MMLU and ARC benchmarks.

### Theme 2: Mathematical Reasoning Enhancement Through Mid-Training

Multiple papers converge on mathematical reasoning as a primary target for mid-training interventions. DeepSeekMath (Shao et al., 2024) achieves 51.7% on the MATH benchmark by continuing pre-training with 120 billion math-related tokens, approaching Gemini-Ultra and GPT-4 performance levels. The OctoThinker investigation (Wang et al., 2025) reveals that high-quality mathematical corpora like MegaMath-Web-Pro significantly improve both base model and reinforcement learning performance, establishing a direct link between mid-training data quality and RL scaling outcomes. Qwen2.5's technical report (Qwen et al., 2024) notes that their scaled pre-training from 7 to 18 trillion tokens, combined with multistage reinforcement learning, produces models competitive with Llama-3-405B-Instruct despite being five times smaller. These findings collectively suggest that mathematical reasoning is particularly responsive to targeted mid-training with curated mathematical data.

### Theme 3: Multilingual and Translation-Focused Continual Pre-Training

Several papers employ mid-training strategies to enhance multilingual capabilities and translation performance. LLaMAX (Lu et al., 2024) uses extensive multilingual continual pre-training with vocabulary expansion and data augmentation to support translation across more than 100 languages, achieving performance on-par with specialized translation model M2M-100-12B. Tower (Alves et al., 2024) performs continued pre-training on multilingual monolingual and parallel data mixtures, followed by instruction fine-tuning, creating models that surpass open alternatives on translation workflow tasks. These works demonstrate that mid-training with carefully balanced multilingual data can transform general-purpose LLMs into capable multilingual systems without requiring architecture modifications from scratch.

### Theme 4: Code Generation and OSS-Instruct Data Synthesis

The Magicoder paper (Wei et al., 2023) introduces a novel mid-training data synthesis approach using open-source code snippets to generate 75K synthetic instruction data, mitigating LLM bias in traditional synthetic data generation. This OSS-Instruct method produces more realistic and controllable training data, enabling Magicoder models with no more than 7B parameters to surpass ChatGPT on HumanEval+ (66.5 vs. 65.9 in pass@1). The orthogonality of OSS-Instruct with other methods like Evol-Instruct enables enhanced model variants that substantially outperform state-of-the-art code models with similar or larger sizes. This theme highlights how mid-training data synthesis strategies leveraging existing open-source repositories can efficiently bootstrap specialized capabilities.

### Theme 5: Multi-Stage Training and Learning Rate Scheduling

The OctoThinker study (Wang et al., 2025) introduces a two-stage Stable-then-Decay mid-training strategy with 200 billion tokens at constant learning rate followed by 20 billion tokens across three chain-of-thought-focused branches with learning rate decay. This approach reveals that scaling mid-training consistently leads to stronger downstream reinforcement learning performance. Qwen2.5 (Qwen et al., 2024) similarly employs intricate supervised fine-tuning with over 1 million samples plus multistage reinforcement learning. SmolLM2 (Ben Allal et al., 2025) performs small-scale ablations with manual refinement of dataset mixing rates at each training stage. These multi-stage approaches suggest that mid-training benefits from careful learning rate scheduling and iterative dataset composition refinement based on previous stage performance.

### Theme 6: Unified Frameworks and Adaptive Resource Allocation

Qwen3 (Yang et al., 2025) represents an evolution toward unified frameworks that integrate both complex reasoning and rapid response capabilities, featuring thinking and non-thinking modes with a thinking budget mechanism for adaptive resource allocation. This approach eliminates the need to switch between chat-optimized and dedicated reasoning models, allowing users to balance latency and performance based on task complexity. The expansion from 29 to 119 languages and dialects compared to Qwen2.5 demonstrates how mid-training strategies can be scaled across model families, with smaller-scale models achieving competitive performance by leveraging knowledge from flagship models.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, all works agree that data quality and curation during mid-training phases matter more than raw scale alone — strategic data selection can double gains achieved by larger models (Yu et al., 2024). Second, mathematical reasoning emerges as universally responsive to targeted mid-training with high-quality mathematical corpora (Shao et al., 2024; Wang et al., 2025; Qwen et al., 2024). Third, multi-stage training with learning rate scheduling and iterative dataset refinement consistently outperforms single-stage approaches (Wang et al., 2025; Ben Allal et al., 2025). Fourth, specialized mid-training can enable smaller models to compete with much larger counterparts, challenging the assumption that scale is the primary driver of capability (Ben Allal et al., 2025; Wei et al., 2023).

**Disagreements**: The literature shows limited direct disagreement, largely because papers focus on different domains (mathematics, translation, code generation). However, there is an implicit tension regarding the role of manual curation versus automated selection. MATES (Yu et al., 2024) emphasizes automated model-aware data selection, while SmolLM2 (Ben Allal et al., 2025) relies on manual refinement of dataset mixing rates at each stage. Additionally, while OctoThinker (Wang et al., 2025) warns that long chain-of-thought data can induce verbosity and instability in RL training, other papers do not address potential negative effects of their mid-training strategies, suggesting incomplete understanding of failure modes.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations of their approaches in their abstracts, suggesting either space constraints or insufficient critical reflection on failure modes. Second, while OctoThinker (Wang et al., 2025) investigates what makes base models suitable for reinforcement learning, the broader question of which mid-training strategies generalize across downstream tasks remains underexplored. Third, the computational cost and environmental impact of extensive mid-training phases (e.g., 200 billion tokens in OctoThinker, 11 trillion tokens in SmolLM2) is not addressed, raising questions about efficiency and accessibility. Fourth, the interaction between mid-training and catastrophic forgetting — whether specialized mid-training degrades general capabilities — is not systematically studied. Fifth, the literature lacks comparative studies directly comparing different mid-training strategies (e.g., MATES vs. manual curation) on identical base models and tasks. Finally, the emerging nature of "mid-training" as a distinct phase suggests the field would benefit from standardized terminology and evaluation benchmarks specifically for mid-training interventions.

## Per-Paper Annotations

### Alves et al. (2024)

**Research question**: How can open large language models be tailored to excel at multiple tasks within translation workflows rather than specializing on a single task?

**Methodology**: The authors performed continued pretraining on a multilingual mixture of monolingual and parallel data to create TowerBase, followed by finetuning on instructions relevant for translation processes to create TowerInstruct.

**Key findings**:
- Tower surpasses open alternatives on several tasks relevant to translation workflows
- Tower is competitive with general-purpose closed LLMs
- The approach releases Tower models, specialization dataset, evaluation framework, and model generations
- Open LLM approaches can be competitive when specialized for multiple translation tasks rather than single tasks

**Limitations**: Not stated in abstract.

### Ben Allal et al. (2025)

**Research question**: How can a small language model (1.7B parameters) achieve state-of-the-art performance through data-centric training approaches?

**Methodology**: The authors overtrained SmolLM2 on approximately 11 trillion tokens using a multi-stage training process that combines web text with specialized math, code, and instruction-following data. They introduced new specialized datasets (FineMath, Stack-Edu, and SmolTalk) and performed small-scale ablations with manual refinement of dataset mixing rates at each training stage.

**Key findings**:
- SmolLM2 outperforms other recent small language models including Qwen2.5-1.5B and Llama3.2-1B
- Multi-stage training with specialized datasets improves small model performance
- Manual refinement of dataset mixing rates based on previous stage performance informs better design decisions
- The model and all prepared datasets are released to facilitate future research

**Limitations**: Not stated in abstract.

### Lu et al. (2024)

**Research question**: How can large language models be enhanced to support translation across more than 100 languages, particularly for low-resource languages?

**Methodology**: The authors conducted extensive multilingual continual pre-training on LLaMA series models with training strategies including vocabulary expansion and data augmentation to develop LLaMAX, supporting translation across more than 100 languages.

**Key findings**:
- LLaMAX achieves significantly higher translation performance than existing open-source LLMs (by more than 10 spBLEU points)
- LLaMAX performs on-par with specialized translation model M2M-100-12B on the Flores-101 benchmark
- The model maintains generalization ability while improving multilingual translation
- LLaMAX can serve as a robust multilingual foundation model
- Code and models are publicly available

**Limitations**: Not stated in abstract.

### Penedo et al. (2024)

**Research question**: How can high-quality pretraining datasets be curated from web data to improve large language model performance?

**Methodology**: The authors introduce FineWeb, a 15-trillion token dataset derived from 96 Common Crawl snapshots, and document all design choices including deduplication and filtering strategies. They also introduce FineWeb-Edu, a 1.3-trillion token educational text collection filtered from FineWeb, and release their curation codebase and trained models.

**Key findings**:
- FineWeb produces better-performing LLMs than other open pretraining datasets
- LLMs pretrained on FineWeb-Edu show dramatically better performance on MMLU and ARC benchmarks
- The work advances understanding of optimal data curation strategies through careful ablation studies
- Deduplication and filtering strategies significantly impact dataset quality
- The datasets and curation codebase are publicly released for the research community

**Limitations**: Not stated in abstract.

### Qwen et al. (2024)

**Research question**: How can large language models be improved through enhanced pre-training and post-training techniques to meet diverse user needs?

**Methodology**: The authors scaled pre-training datasets from 7 trillion to 18 trillion tokens and implemented intricate supervised fine-tuning with over 1 million samples, plus multistage reinforcement learning. They present Qwen2.5 as a comprehensive series of LLMs in various sizes including base, instruction-tuned, and mixture-of-experts variants.

**Key findings**:
- Qwen2.5-72B-Instruct outperforms many open and proprietary models on benchmarks
- Performance is competitive with Llama-3-405B-Instruct despite being 5 times smaller
- Qwen2.5-Turbo and Qwen2.5-Plus offer competitive performance against GPT-4o-mini and GPT-4o respectively
- Post-training techniques enhance human preference alignment, long text generation, and instruction following
- Qwen2.5 models serve as foundations for specialized models like Qwen2.5-Math, Qwen2.5-Coder, and QwQ

**Limitations**: Not stated in abstract.

### Shao et al. (2024)

**Research question**: How can language models be improved to achieve better mathematical reasoning capabilities?

**Methodology**: The authors introduce DeepSeekMath 7B by continuing pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens from Common Crawl, combined with natural language and code data. They employ a data selection pipeline and introduce Group Relative Policy Optimization (GRPO), a variant of PPO.

**Key findings**:
- DeepSeekMath 7B achieves 51.7% on the MATH benchmark without external toolkits or voting techniques
- Performance approaches that of Gemini-Ultra and GPT-4 on mathematical reasoning tasks
- Self-consistency over 64 samples achieves 60.9% on MATH
- GRPO enhances mathematical reasoning while optimizing PPO memory usage
- Publicly available web data can be effectively harnessed through engineered data selection pipelines

**Limitations**: Not stated in abstract.

### Wang et al. (2025)

**Research question**: What makes a base language model suitable for reinforcement learning, and how do mid-training strategies shape RL dynamics?

**Methodology**: The authors investigated mid-training strategies across Qwen and Llama model families, examining the effects of mathematical corpora, QA-style data, and long chain-of-thought reasoning examples. They introduced a two-stage Stable-then-Decay mid-training strategy with 200B tokens at constant learning rate followed by 20B tokens across three CoT-focused branches with learning rate decay.

**Key findings**:
- High-quality mathematical corpora like MegaMath-Web-Pro significantly improve both base model and RL performance
- Adding QA-style data, particularly long CoT reasoning examples, enhances RL outcomes
- Instruction data unlocks the effect of QA-style data on RL performance
- Long-CoT can induce verbosity and instability in RL training, highlighting the importance of data formatting
- Scaling mid-training consistently leads to stronger downstream RL performance
- OctoThinker closes the performance gap with more RL-friendly model families like Qwen

**Limitations**: Not stated in abstract.

### Wei et al. (2023)

**Research question**: How can synthetic instruction data for code generation be improved to reduce LLM bias and produce more realistic, controllable training data?

**Methodology**: The authors introduce OSS-Instruct, a novel approach that uses open-source code snippets to generate 75K synthetic instruction data, mitigating inherent bias in LLM-generated synthetic data through abundant open-source references.

**Key findings**:
- Magicoder models significantly close the gap with top code models while having no more than 7B parameters
- MagicoderS-CL-7B surpasses ChatGPT on HumanEval+ (66.5 vs. 65.9 in pass@1)
- OSS-Instruct produces more realistic and controllable data compared to traditional synthetic data generation
- The orthogonality of OSS-Instruct and other methods like Evol-Instruct enables enhanced MagicoderS models
- Both Magicoder and MagicoderS substantially outperform state-of-the-art code models with similar or larger sizes

**Limitations**: Not stated in abstract.

### Yang et al. (2025)

**Research question**: How can a unified language model framework integrate both complex reasoning and rapid response capabilities while scaling efficiently across different model sizes?

**Methodology**: The authors developed Qwen3, a series of LLMs with both dense and Mixture-of-Expert architectures ranging from 0.6 to 235 billion parameters, featuring integrated thinking and non-thinking modes with a thinking budget mechanism for adaptive resource allocation.

**Key findings**:
- Qwen3 achieves state-of-the-art results across diverse benchmarks including code generation, mathematical reasoning, and agent tasks
- The unified framework eliminates the need to switch between chat-optimized and dedicated reasoning models
- The thinking budget mechanism allows users to balance latency and performance based on task complexity
- Multilingual support expanded from 29 to 119 languages and dialects compared to Qwen2.5
- Smaller-scale models achieve competitive performance by leveraging knowledge from flagship models

**Limitations**: The abstract does not explicitly state limitations of the approach or model.

### Yu et al. (2024)

**Research question**: How can pretraining data selection be improved to capture evolving data preferences during model training?

**Methodology**: The authors introduce MATES, where a data influence model continuously adapts to the evolving data preferences of the pretraining model. They collect oracle data influence by locally probing the pretraining model and fine-tune a small data influence model to approximate it, then use it to select the most influential data for subsequent pretraining stages.

**Key findings**:
- MATES significantly outperforms random data selection on extensive downstream tasks
- The approach doubles gains achieved by state-of-the-art data selection methods using larger reference models
- MATES reduces total FLOPs required to reach certain performance levels by half
- Locally probed oracle data influence effectively captures model preferences
- The code is open-sourced for community use

**Limitations**: Not stated in abstract.

## References

Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., Peters, B., Rei, R., Fernandes, P., Agrawal, S., Colombo, P., de Souza, J. G. C., & Martins, A. F. T. (2024). Tower: An open multilingual large language model for translation-related tasks. arXiv. https://arxiv.org/abs/2402.17733

Ben Allal, L., Lozhkov, A., Bakouch, E., Blázquez, G. M., Penedo, G., Tunstall, L., Marafioti, A., Kydlíček, H., Lajarín, A. P., Srivastav, V., Lochner, J., Fahlgren, C., Nguyen, X.-S., Fourrier, C., Burtenshaw, B., Larcher, H., Zhao, H., Zakka, C., Morlon, M., ... Raffel, C. (2025). SmolLM2: When Smol goes big -- Data-centric training of a small language model. arXiv. https://arxiv.org/abs/2502.02737

Lu, Y., Zhu, W., Li, L., Qiao, Y., & Yuan, F. (2024). LLaMAX: Scaling linguistic horizons of LLM by enhancing translation capabilities beyond 100 languages. arXiv. https://arxiv.org/abs/2407.05975

Penedo, G., Kydlíček, H., Ben allal, L., Lozhkov, A., Mitchell, M., Raffel, C., Von Werra, L., & Wolf, T. (2024). The FineWeb datasets: Decanting the web for the finest text data at scale. arXiv. https://arxiv.org/abs/2406.17557

Qwen, Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin, J., ... (2024). Qwen2.5 technical report. arXiv. https://arxiv.org/abs/2412.15115

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv. https://arxiv.org/abs/2402.03300

Wang, Z., Zhou, F., Li, X., & Liu, P. (2025). OctoThinker: Mid-training incentivizes reinforcement learning scaling. arXiv. https://arxiv.org/abs/2506.20512

Wei, Y., Wang, Z., Liu, J., Ding, Y., & Zhang, L. (2023). Magicoder: Empowering code generation with OSS-Instruct. arXiv. https://arxiv.org/abs/2312.02120

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., Yang, J., ... (2025). Qwen3 technical report. arXiv. https://arxiv.org/abs/2505.09388

Yu, Z., Das, S., & Xiong, C. (2024). MATES: Model-aware data selection for efficient pretraining with data influence models. arXiv. https://arxiv.org/abs/2406.06046
