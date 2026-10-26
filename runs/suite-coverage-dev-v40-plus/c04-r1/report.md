# Systematic Literature Review: LLM Mid-Training

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: LLM mid-training, cs.CL, published between 2023-10-27 and 2025-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers (2023-2025) focused on mid-training techniques and pretraining strategies for large language models. The surveyed literature reveals a field increasingly focused on data-centric approaches, where the quality and strategic selection of training data proves as critical as model architecture improvements. Key trends include multi-stage training pipelines that progressively specialize models through carefully curated datasets, the emergence of mid-training as a distinct phase between base pretraining and fine-tuning, and growing emphasis on efficiency through knowledge distillation and model-aware data selection. Several papers demonstrate that smaller models trained with optimized data strategies can compete with significantly larger counterparts, suggesting diminishing returns from pure scale increases without corresponding improvements in training methodology.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM mid-training", filtered to category cs.CL, published between 2023-10-27 and 2025-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening process**: The search identified 32 papers by direct search, with an additional 104 papers added through citation expansion. From the resulting shortlist of 30 papers, 10 were selected based on centrality to the mid-training topic. The screening scores distributed as follows: 10 papers scored 0, 11 scored 1, 5 scored 2, and 4 scored 3, with the 10 highest-scoring papers included in this review.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, the search query "LLM mid-training" is relatively narrow, and some relevant papers using alternative terminology (e.g., "continued pretraining," "intermediate training") may not have been captured.

## Themes

### Theme 1: Data-Centric Training Strategies

A dominant theme across the surveyed literature is the shift from model-centric to data-centric improvements. Rather than solely increasing model parameters, researchers are investing substantial effort in curating and structuring training data to maximize learning efficiency. SmolLM2 exemplifies this approach, overtraining a 1.7B parameter model on approximately 11 trillion tokens through a multi-stage process combining web text with specialized math, code, and instruction-following datasets (Ben Allal et al., 2025). Similarly, MATES introduces a model-aware data selection framework where a data influence model continuously adapts to evolving data preferences during pretraining, significantly outperforming static selection methods (Yu et al., 2024). This theme reflects a maturing understanding that data quality and strategic mixing can compensate for, or even surpass, the benefits of raw model scale.

### Theme 2: Multi-Stage Training Pipelines

Closely related to data-centric approaches is the emergence of sophisticated multi-stage training pipelines. Rather than single-phase pretraining, modern LLMs increasingly employ staged approaches where different data types and learning objectives are introduced sequentially. Qwen2.5 implements intricate supervised fine-tuning with over 1 million samples followed by multistage reinforcement learning (Qwen et al., 2024). Gemma 3 employs a novel post-training recipe that significantly improves math, chat, instruction-following, and multilingual abilities (Gemma Team et al., 2025). OctoThinker explicitly investigates mid-training strategies, proposing a "Stable-then-Decay" two-stage approach with 200B tokens at constant learning rate followed by 20B tokens across three chain-of-thought-focused branches with learning rate decay (Wang et al., 2025). This staging allows models to build foundational knowledge before specializing, mirroring curriculum learning principles.

### Theme 3: Efficiency Through Knowledge Distillation

Several papers address the computational cost of LLM training through knowledge distillation, where smaller student models learn from larger teacher models. Gemma 2 trains its 2B and 9B models with knowledge distillation instead of next token prediction, delivering competitive performance against models 2-3 times larger (Gemma Team et al., 2024). This approach enables practical deployment of capable models on resource-constrained devices while maintaining quality. The distillation trend acknowledges that not all applications require frontier-model capabilities, and that targeted knowledge transfer can produce fit-for-purpose models at a fraction of the training cost.

### Theme 4: Specialized Domain Adaptation

Multiple papers focus on adapting general-purpose LLMs to specialized domains through continued pretraining or targeted data injection. Tower employs a two-stage recipe: continued pretraining on multilingual monolingual and parallel data to create TowerBase, followed by finetuning on translation-relevant instructions (Alves et al., 2024). LLaMAX conducts extensive multilingual continual pretraining with vocabulary expansion and data augmentation to support translation across more than 100 languages (Lu et al., 2024). DeepSeekMath continues pretraining a code-focused base model with 120B math-related tokens to achieve mathematical reasoning capabilities approaching GPT-4 level (Shao et al., 2024). This specialization trend reflects practical deployment needs where domain expertise matters more than general knowledge breadth.

### Theme 5: Architecture-Training Co-Design

Several works demonstrate that architectural modifications and training strategies are increasingly co-designed rather than treated independently. Gemma 2 applies several Transformer modifications including interleaving local-global attentions and group-query attention specifically to support efficient training at practical sizes (Gemma Team et al., 2024). Gemma 3 further modifies the architecture to reduce KV-cache memory by increasing the ratio of local to global attention layers, enabling longer context windows of at least 128K tokens (Gemma Team et al., 2025). Qwen3 integrates thinking and non-thinking modes into a unified framework with a thinking budget mechanism for adaptive computational resource allocation during inference (Yang et al., 2025). This co-design approach recognizes that architectural choices constrain and enable particular training strategies.

### Theme 6: Reinforcement Learning Integration

The integration of reinforcement learning (RL) with mid-training represents an emerging frontier. OctoThinker specifically investigates what makes a base language model suitable for RL, revealing that high-quality mathematical corpora and QA-style data with long chain-of-thought reasoning enhance RL outcomes (Wang et al., 2025). Qwen2.5 implements multistage reinforcement learning as part of its post-training pipeline to improve human preference alignment (Qwen et al., 2024). This theme suggests that mid-training prepares models not just with knowledge, but with structural capabilities that make subsequent RL more effective—certain data types and training approaches appear to create more "RL-eligible" base models.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers implicitly or explicitly endorse multi-stage training over single-phase approaches, suggesting this has become standard practice. Second, there is consensus that data quality and curation matter as much as or more than model scale—multiple papers demonstrate smaller models with optimized training matching or exceeding larger counterparts. Third, all technical reports release their models and often their datasets openly, reflecting a field norm of open science. Fourth, there is convergence on the value of domain specialization: general pretraining followed by targeted continued training outperforms attempting to learn everything simultaneously.

**Disagreements**: The literature shows limited direct disagreement, partly because most papers are technical reports rather than comparative studies. However, subtle tensions exist around the optimal training sequence. SmolLM2 emphasizes manual refinement of dataset mixing rates at each stage based on performance (Ben Allal et al., 2025), while MATES advocates for automated, model-aware data selection that adapts continuously (Yu et al., 2024)—these represent different philosophies about human intervention versus automation in training pipeline design. Additionally, while Gemma models emphasize knowledge distillation for efficiency, Qwen and DeepSeek papers focus more on scaling pretraining tokens (18T for Qwen2.5, 120B math tokens for DeepSeekMath), suggesting different beliefs about whether distillation or continued scaling offers better returns.

## Gaps and Open Questions

Several notable gaps emerge from the collective literature. First, none of the papers explicitly state limitations in their abstracts, which may reflect publication bias or insufficient self-critique in technical reports. Second, while multiple papers mention multi-stage training, there is limited systematic comparison of stage boundaries—when exactly should one transition from general to specialized data, and how do these decisions interact with learning rate schedules? Third, the computational cost of these sophisticated pipelines remains underdiscussed; MATES claims to reduce FLOPs by half compared to baseline data selection (Yu et al., 2024), but absolute costs of multi-stage training with manual refinement remain opaque. Fourth, the relationship between mid-training and downstream fine-tuning efficiency is rarely examined—does better mid-training reduce the amount of task-specific fine-tuning needed? Finally, most papers are industry technical reports rather than independent academic research, raising questions about reproducibility and whether proprietary advantages are being adequately disclosed.

## Per-Paper Annotations

### Alves et al. (2024)

**Research question**: How can open large language models be tailored to handle multiple tasks within translation workflows competitively with closed general-purpose LLMs?

**Methodology**: The authors propose a two-stage recipe: continued pretraining on a multilingual mixture of monolingual and parallel data to create TowerBase, followed by finetuning on instructions relevant for translation processes to create TowerInstruct.

**Key findings**:
- Tower surpasses open alternatives on several tasks relevant to translation workflows
- Tower is competitive with general-purpose closed LLMs on translation tasks
- The approach releases Tower models, a specialization dataset, an evaluation framework for LLMs focusing on translation, and a collection of model generations on their benchmark

**Limitations**: not stated in abstract

### Ben Allal et al. (2025)

**Research question**: How can a small language model (1.7B parameters) achieve state-of-the-art performance through data-centric training approaches?

**Methodology**: The authors overtrain SmolLM2 on approximately 11 trillion tokens using a multi-stage training process that combines web text with specialized math, code, and instruction-following data. They introduce new specialized datasets (FineMath, Stack-Edu, and SmolTalk) and perform small-scale ablations with manual refinement of dataset mixing rates at each training stage.

**Key findings**:
- SmolLM2 outperforms other recent small language models including Qwen2.5-1.5B and Llama3.2-1B
- Multi-stage training with specialized datasets improves performance over standard web text training
- Manual refinement of dataset mixing rates based on previous stage performance informs better design decisions
- The model and all prepared datasets are released to facilitate future research on small LM development

**Limitations**: not stated in abstract

### Gemma Team et al. (2024)

**Research question**: How can open language models deliver state-of-the-art performance at practical, lightweight model sizes?

**Methodology**: The authors introduce Gemma 2 with models ranging from 2B to 27B parameters, applying several technical modifications to the Transformer architecture including interleaving local-global attentions and group-query attention. They train the 2B and 9B models with knowledge distillation instead of next token prediction and release all models to the community.

**Key findings**:
- Gemma 2 models deliver the best performance for their size across the 2B to 27B parameter range
- The models offer competitive alternatives to models that are 2-3 times bigger
- Interleaving local-global attentions and group-query attention improve model efficiency
- Knowledge distillation training for 2B and 9B models provides effective alternatives to next token prediction
- All models are released openly to the community

**Limitations**: not stated in abstract

### Gemma Team et al. (2025)

**Research question**: How can open multimodal language models be improved to support vision understanding, multilingual capabilities, and longer context windows while maintaining efficiency?

**Methodology**: The authors introduce Gemma 3 as a multimodal family of models ranging from 1B to 27B parameters with vision understanding abilities, wider language coverage, and at least 128K token context. They modify the architecture to reduce KV-cache memory by increasing the ratio of local to global attention layers and keeping local attention spans short. Models are trained with distillation and use a novel post-training recipe.

**Key findings**:
- Gemma 3 introduces vision understanding abilities and supports longer context of at least 128K tokens
- The architecture modifications reduce KV-cache memory that tends to explode with long context
- Gemma3-4B-IT is competitive with Gemma2-27B-IT despite being significantly smaller
- Gemma3-27B-IT is comparable to Gemini-1.5-Pro across benchmarks
- The novel post-training recipe significantly improves math, chat, instruction-following and multilingual abilities

**Limitations**: not stated in abstract

### Lu et al. (2024)

**Research question**: How can large language models be enhanced to support translation across more than 100 languages, particularly improving performance on low-resource languages?

**Methodology**: The authors conduct extensive multilingual continual pre-training on LLaMA series models with training strategies including vocabulary expansion and data augmentation to develop LLaMAX, enabling translation support across more than 100 languages without sacrificing generalization ability.

**Key findings**:
- LLaMAX achieves significantly higher translation performance compared to existing open-source LLMs by more than 10 spBLEU points
- LLaMAX performs on-par with specialized translation model M2M-100-12B on the Flores-101 benchmark
- LLaMAX can serve as a robust multilingual foundation model
- The code and models are publicly available

**Limitations**: not stated in abstract

### Qwen et al. (2024)

**Research question**: How can large language models be improved through enhanced pre-training and post-training stages to meet diverse user needs?

**Methodology**: The authors scaled pre-training datasets from 7 trillion to 18 trillion tokens and implemented intricate supervised fine-tuning with over 1 million samples, along with multistage reinforcement learning. They present Qwen2.5 as a comprehensive series of LLMs in various sizes, including base and instruction-tuned models with quantized versions, plus two MoE variants (Qwen2.5-Turbo and Qwen2.5-Plus).

**Key findings**:
- Scaling pre-training to 18 trillion tokens provides a strong foundation for common sense, expert knowledge, and reasoning capabilities
- Post-training techniques enhance human preference alignment and improve long text generation, structural data analysis, and instruction following
- Qwen2.5-72B-Instruct outperforms many open and proprietary models and shows competitive performance to Llama-3-405B-Instruct despite being 5 times smaller
- Qwen2.5-Turbo and Qwen2.5-Plus offer superior cost-effectiveness while performing competitively against GPT-4o-mini and GPT-4o respectively
- Qwen2.5 models serve as foundations for specialized models like Qwen2.5-Math, Qwen2.5-Coder, QwQ, and multimodal models

**Limitations**: not stated in abstract

### Shao et al. (2024)

**Research question**: How can language models be improved to achieve better mathematical reasoning capabilities without relying on external toolkits?

**Methodology**: The authors introduce DeepSeekMath 7B by continuing pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, along with natural language and code data. They employ a meticulously engineered data selection pipeline and introduce Group Relative Policy Optimization (GRPO), a variant of PPO, to enhance mathematical reasoning while optimizing memory usage.

**Key findings**:
- DeepSeekMath 7B achieved 51.7% on the competition-level MATH benchmark without external toolkits or voting techniques
- Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH
- The performance approaches the level of Gemini-Ultra and GPT-4
- GRPO enhances mathematical reasoning abilities while concurrently optimizing PPO memory usage
- Publicly available web data can be harnessed effectively through careful data selection pipelines

**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: What makes a base language model suitable for reinforcement learning, and how do mid-training strategies shape RL dynamics across different model families?

**Methodology**: The authors investigate mid-training strategies across Qwen and Llama model families, revealing key insights about mathematical corpora, QA-style data, and long chain-of-thought reasoning. They introduce a two-stage 'Stable-then-Decay' mid-training strategy with 200B tokens at constant learning rate followed by 20B tokens across three CoT-focused branches with learning rate decay.

**Key findings**:
- High-quality mathematical corpora like MegaMath-Web-Pro significantly improve both base model and RL performance, while alternatives like FineMath-4plus fail to do so
- Adding QA-style data, particularly long chain-of-thought reasoning examples, enhances RL outcomes, with instruction data further unlocking this effect
- Long-CoT improves reasoning depth but can induce verbosity and instability in RL training, highlighting the importance of data formatting
- Scaling mid-training consistently leads to stronger downstream RL performance
- OctoThinker closes the performance gap with more RL-friendly model families like Qwen

**Limitations**: not stated in abstract

### Yang et al. (2025)

**Research question**: How can a unified framework integrate thinking and non-thinking modes in large language models to balance reasoning capability and response speed?

**Methodology**: The authors developed Qwen3, a series of LLMs with both dense and Mixture-of-Expert architectures ranging from 0.6 to 235 billion parameters. They introduced a thinking budget mechanism for adaptive computational resource allocation and evaluated the models across diverse benchmarks including code generation, mathematical reasoning, and agent tasks.

**Key findings**:
- Qwen3 integrates thinking mode (for complex multi-step reasoning) and non-thinking mode (for rapid responses) into a unified framework, eliminating the need to switch between different model types.
- The thinking budget mechanism allows users to adaptively allocate computational resources during inference, balancing latency and performance based on task complexity.
- Qwen3 achieves state-of-the-art results across diverse benchmarks including code generation, mathematical reasoning, and agent tasks, competing against larger MoE models and proprietary models.
- Multilingual support was expanded from 29 to 119 languages and dialects, enhancing cross-lingual understanding and generation capabilities.
- Knowledge from flagship models was leveraged to reduce computational resources required for smaller-scale models while maintaining competitive performance.

**Limitations**: The abstract does not explicitly state limitations of the Qwen3 models or the research methodology.

### Yu et al. (2024)

**Research question**: How can pretraining data selection be improved to capture evolving data preferences during model pretraining rather than relying on static selection methods?

**Methodology**: The authors introduce MATES, where a data influence model continuously adapts to the evolving data preferences of the pretraining model. They collect oracle data influence by locally probing the pretraining model, fine-tune a small data influence model to approximate it, and use it to predict data influence over the whole pretraining corpus to select the most influential data for each pretraining stage. Experiments were conducted pretraining 410M and 1B models on the C4 dataset.

**Key findings**:
- MATES significantly outperforms random data selection on extensive downstream tasks
- MATES doubles the gains achieved by state-of-the-art data selection approaches that leverage larger reference models
- MATES reduces the total FLOPs required to reach certain performances by half
- Locally probed oracle data influence effectively captures evolving data preferences during pretraining
- Small data influence models can accurately approximate oracle data influence

**Limitations**: not stated in abstract

## References

Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., Peters, B., Rei, R., Fernandes, P., Agrawal, S., Colombo, P., de Souza, J. G. C., & Martins, A. F. T. (2024). Tower: An open multilingual large language model for translation-related tasks. arXiv. https://arxiv.org/abs/2402.17733

Ben Allal, L., Lozhkov, A., Bakouch, E., Blázquez, G. M., Penedo, G., Tunstall, L., Marafioti, A., Kydlíček, H., Lajarín, A. P., Srivastav, V., Lochner, J., Fahlgren, C., Nguyen, X.-S., Fourrier, C., Burtenshaw, B., Larcher, H., Zhao, H., Zakka, C., Morlon, M., ... Rafel, C. (2025). SmolLM2: When Smol goes big -- Data-centric training of a small language model. arXiv. https://arxiv.org/abs/2502.02737

Gemma Team, Riviere, M., Pathak, S., Sessa, P. G., Hardin, C., Bhupatiraju, S., Hussenot, L., Mesnard, T., Shahriari, B., Ramé, A., Ferret, J., Liu, P., Tafti, P., Friesen, A., Casbon, M., Ramos, S., Kumar, R., Le Lan, C., Jerome, S., ... Tsitsulin, A. (2024). Gemma 2: Improving open language models at a practical size. arXiv. https://arxiv.org/abs/2408.00118

Gemma Team, Kamath, A., Ferret, J., Pathak, S., Vieillard, N., Merhej, R., Perrin, S., Matejovicova, T., Ramé, A., Rivière, M., Rouillard, L., Mesnard, T., Cideron, G., Grill, J.-b., Ramos, S., Yvinec, E., Casbon, M., Pot, E., Penchev, I., ... Liu, G. (2025). Gemma 3 technical report. arXiv. https://arxiv.org/abs/2503.19786

Lu, Y., Zhu, W., Li, L., Qiao, Y., & Yuan, F. (2024). LLaMAX: Scaling linguistic horizons of LLM by enhancing translation capabilities beyond 100 languages. arXiv. https://arxiv.org/abs/2407.05975

Qwen, Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin, J., ... (2024). Qwen2.5 technical report. arXiv. https://arxiv.org/abs/2412.15115

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv. https://arxiv.org/abs/2402.03300

Wang, Z., Zhou, F., Li, X., & Liu, P. (2025). OctoThinker: Mid-training incentivizes reinforcement learning scaling. arXiv. https://arxiv.org/abs/2506.20512

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., ... (2025). Qwen3 technical report. arXiv. https://arxiv.org/abs/2505.09388

Yu, Z., Das, S., & Xiong, C. (2024). MATES: Model-aware data selection for efficient pretraining with data influence models. arXiv. https://arxiv.org/abs/2406.06046
