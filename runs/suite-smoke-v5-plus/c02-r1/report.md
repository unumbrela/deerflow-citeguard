# Systematic Literature Review: Latent Reasoning

**Date**: 2026-10-27  
**Papers surveyed**: 10  
**Scope**: arXiv search query "latent reasoning", category cs.CL, published between 2023-07-08 and 2025-07-07  
**Citation format**: APA 7th edition

## Executive Summary

The literature on latent reasoning reveals a rapidly evolving field exploring how large language models can perform reasoning through internal representations rather than explicit verbalized chains of thought. The surveyed papers collectively demonstrate that latent reasoning approaches—including continuous latent spaces, implicit chain-of-thought, pause tokens, and compressed representations—can achieve comparable or superior performance to explicit reasoning methods while offering significant efficiency gains. Key advances include Coconut's continuous latent space reasoning, DeepSeek-R1's reinforcement learning approach to incentivizing reasoning capabilities, and various implicit CoT methods that internalize reasoning steps in hidden states. However, limitations persist around interpretability, scalability, and the trade-off between transparency and efficiency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-07. Papers were sorted by co-citation relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; 0 papers had only an abstract), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Continuous Latent Space Reasoning

A prominent direction involves representing reasoning states in continuous latent spaces rather than discrete token sequences. Hao et al. (2024) introduced Coconut (Chain of Continuous Thought), which uses the last hidden state of the LLM as a representation of the reasoning state and feeds it back as the next input embedding directly in the continuous space [E8]. Hao et al. (2024) report that Coconut with continuous thoughts significantly outperforms No-CoT baseline on GSM8k math reasoning [E8]. Hao et al. (2024) further demonstrate that Coconut is more token-efficient than traditional CoT while achieving higher accuracy on logical reasoning tasks [E9]. Hao et al. (2024) show that continuous latent reasoning enables emergent BFS-like search over multiple reasoning paths [E10]. Similarly, Cheng and Van Durme (2024) proposed Compressed Chain-of-Thought (CCoT), generating contentful and continuous contemplation tokens as compressed representations of explicit reasoning chains [E23]. Cheng and Van Durme (2024) demonstrate that with compression ratio r=0.10, CCoT achieves a 9 point accuracy improvement over the baseline with no contemplation tokens, with only 0.4 second increase in generation time [E23]. Cheng and Van Durme (2024) further show that equipping a model with dense, contentful contemplation tokens produced by CCoT allows the model to reason better than having no contemplation tokens or using discrete noncontentful pause tokens [E24].

### Theme 2: Implicit Chain-of-Thought Internalization

Multiple papers explore methods to internalize explicit reasoning steps into implicit processes occurring within hidden states. Deng et al. (2024) proposed Stepwise Internalization, which starts with a model trained for explicit CoT reasoning and gradually removes intermediate steps while finetuning [E17]. Deng et al. (2024) report that this approach enables GPT-2 Small to solve 9×9 multiplication with 99% accuracy, far exceeding No CoT baselines [E17]. Deng et al. (2024) demonstrate that ICoT-SI achieves state-of-the-art accuracy on GSM8K among models that don't output intermediate reasoning steps [E18]. Deng et al. (2024) show that ICoT-SI offers 11x speedup over Explicit CoT while maintaining comparable accuracy on multiplication tasks [E19]. Deng et al. (2023) similarly distilled implicit reasoning steps from a teacher model trained on explicit chain-of-thought, with reasoning happening vertically among hidden states in different layers rather than horizontally through intermediate words [E25]. Deng et al. (2023) report that their implicit CoT enables solving tasks previously not solvable without explicit CoT, such as GPT-2 Medium achieving 96% accuracy on 5×5 multiplication compared to 2% with no CoT [E25]. Deng et al. (2023) further demonstrate that implicit CoT offers higher inference speed especially for tasks with many intermediate steps [E26].

### Theme 3: Training-Time Compute Delays and Pause Tokens

Several papers investigate the role of delayed computation through pause tokens and training-time compute allocation. Goyal et al. (2023) trained decoder-only models with learnable pause tokens appended to input sequences, delaying output generation until the last pause token [E20]. Goyal et al. (2023) report that pause-pretraining followed by pause-finetuning improves performance on eight tasks for the 1B model and six tasks for the 130M model compared to standard training [E20]. Goyal et al. (2023) show that the most prominent improvement is an 18% EM score gain on the SQuAD question-answering task for the 1B model [E21]. Goyal et al. (2023) reveal that pause-pretraining is crucial for delays to help in downstream inference-time, as standard-pretrained models have biases that prevent realizing benefits of inference-time delays [E22].

### Theme 4: Reinforcement Learning for Reasoning Emergence

DeepSeek-AI et al. (2025) demonstrate that reasoning capabilities can be incentivized through pure reinforcement learning without human-annotated reasoning trajectories. DeepSeek-R1 shows substantial improvements on reasoning-intensive benchmarks through RL training [E11], with advanced reasoning patterns like self-reflection and verification emerging organically from pure RL without human annotations [E12]. However, the approach faces limitations including suboptimal structured output capabilities, inability to leverage tools like search engines and calculators, token efficiency issues with overthinking, language mixing for non-Chinese/English queries, sensitivity to few-shot prompting, and limited improvement on software engineering benchmarks [E13].

### Theme 5: Test-Time Scaling and Budget Forcing

Muennighoff et al. (2025) explored simple test-time scaling approaches, curating s1K—a dataset of 1,000 questions with reasoning traces—and developing budget forcing to control test-time compute by terminating or extending the model's thinking process [E27]. The s1-32B model exceeds o1-preview on competition math questions by up to 27% on MATH and AIME24 benchmarks [E27]. Scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention, improving AIME24 accuracy from 50% to 57% [E28], demonstrating that supervised finetuning on only 1,000 examples suffices to build a competitive reasoning model matching o1-preview performance [E29]. However, budget forcing has two key limitations when scaling further: it eventually flattens out in performance gains, and the context window of the underlying language model constrains it.

### Theme 6: Latent Multi-Hop Reasoning Analysis

Yang et al. (2024) analyzed whether large language models latently perform multi-hop reasoning when processing complex prompts requiring multiple reasoning steps. Their analysis reveals that first-hop reasoning shows clear scaling trends with larger model sizes [E14], with strong latent multi-hop reasoning evidence existing for certain prompt types, used in over 80% of cases [E15]. However, second-hop and full multi-hop reasoning evidence is moderate overall, with strongest evidence for first hop only [E16]. Biran et al. (2024) explored limitations of LLMs on multi-hop queries, finding that the second hop is answered in the mid-upper layers only after the first hop is answered by the lower layers, indicating sequential latent reasoning [E4]. Biran et al. (2024) demonstrate that back-patching correctly answers between 32%-66% of previously incorrect cases while maintaining 100% accuracy on correct cases [E3]. Biran et al. (2024) reveal that MLP sublayers play a larger role in promoting the predicted token compared to attention sublayers [E2]. Su et al. (2025) proposed mixing latent tokens with text tokens for improved reasoning, achieving 17.5% performance gain over CoT baseline on the difficult ProsQA benchmark [E5]. Su et al. (2025) show that the latent approach shows an average 17% reduction in token numbers compared with CoT while surpassing it in prediction accuracy [E6]. Su et al. (2025) find that accuracy peaks at compression rate r=16 (28.1) and decreases at r=32 (27.9), indicating an optimal balance between compression and information preservation [E7].

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that latent reasoning approaches can match or exceed explicit CoT performance while offering efficiency gains. Multiple papers demonstrate that internalizing reasoning steps in hidden states enables solving complex tasks without explicit intermediate outputs (Deng et al., 2023; Deng et al., 2024; Hao et al., 2024). There is consensus that training-time compute allocation through pause tokens or continuous representations improves downstream task performance (Goyal et al., 2023; Cheng & Van Durme, 2024).

**Disagreements**: Papers differ on the trade-off between interpretability and efficiency. Deng et al. (2023) note that implicit CoT lacks transparency compared to explicit CoT, while Hao et al. (2024) emphasize the emergent search capabilities of continuous latent spaces without addressing interpretability concerns. DeepSeek-AI et al. (2025) acknowledge limitations in structured output generation, contrasting with the efficiency gains reported by Deng et al. (2024) in their Stepwise Internalization approach.

## Gaps and Open Questions

The collective literature reveals several unaddressed challenges. Hao et al. (2024) note that further research is needed to refine and scale latent reasoning to pretraining, which could improve generalization across a broader range of reasoning challenges. Goyal et al. (2023) highlight that the expense of pause-pretraining prevents studying generalization across more model sizes beyond 1B and 130M, encoder-decoder architectures, or other pretraining mixtures and objectives. Yang et al. (2024) acknowledge their analysis is based on LLaMA-2 family up to 70B parameters and uses approximations for internal entity recall based on logit lens which has shortcomings like representation drift, bias, and brittleness. Deng et al. (2024) identify high training costs due to finetuning required when removing each set of CoT tokens, with unstable training from aggressive removal values. DeepSeek-AI et al. (2025) face limitations including token efficiency issues with overthinking and inability to leverage external tools. Muennighoff et al. (2025) note that budget forcing eventually flattens out in performance gains and is constrained by context window limitations.

## Per-Paper Annotations

### Biran et al. (2024)

**Research question**: What are the limitations of large language models on multi-hop reasoning queries?  
**Methodology**: The authors explore LLM limitations on multi-hop queries through analysis of reasoning pathways and layer-wise information flow.  
**Key findings**:
- The second hop is answered in the mid-upper layers only after the first hop is answered by the lower layers, indicating sequential latent reasoning [E4]
- Back-patching correctly answers between 32%-66% of previously incorrect cases while maintaining 100% accuracy on correct cases [E3]
- MLP sublayers play a larger role in promoting the predicted token compared to attention sublayers [E2]
**Limitations**: The mechanistic methods used are approximations, the study examines only two-hop queries, and the back-patching method is not practical for inference without efficient source-target layer selection.

### Cheng and Van Durme (2024)

**Research question**: Can compressed representations of reasoning chains as dense contemplation tokens enable efficient reasoning with improved accuracy in language models?  
**Methodology**: The authors propose Compressed Chain-of-Thought (CCoT), a framework that generates contentful and continuous contemplation tokens of variable sequence length as compressed representations of explicit reasoning chains, evaluated on GSM8K with compression ratios r=[0.05, 0.10].  
**Key findings**:
- With compression ratio r=0.10, CCoT achieves a 9 point accuracy improvement over the baseline with no contemplation tokens, with only 0.4 second increase in generation time [E23]
- Equipping a model with dense, contentful contemplation tokens produced by CCoT allows the model to reason better than having no contemplation tokens or using discrete noncontentful pause tokens [E24]
**Limitations**: Not explicitly stated in the conclusion, though the paper notes that reasoning datasets like GSM8K require more sequential computations than parallel ones.

### DeepSeek-AI et al. (2025)

**Research question**: Can the reasoning abilities of large language models be incentivized through pure reinforcement learning without human-annotated reasoning trajectories?  
**Methodology**: The authors develop DeepSeek-R1-Zero and DeepSeek-R1 using large-scale reinforcement learning to incentivize reasoning behaviors, with sophisticated patterns like self-verification and reflection emerging organically during training.  
**Key findings**:
- DeepSeek-R1 shows substantial improvements on reasoning-intensive benchmarks through RL training [E11]
- Advanced reasoning patterns like self-reflection and verification emerge from pure RL without human annotations [E12]
- DeepSeek-R1 has limitations in structured output generation and tool use capabilities [E13]
**Limitations**: DeepSeek-R1 faces limitations including suboptimal structured output capabilities, inability to leverage tools like search engines and calculators, token efficiency issues with overthinking, language mixing for non-Chinese/English queries, sensitivity to few-shot prompting, and limited improvement on software engineering benchmarks.

### Deng et al. (2023)

**Research question**: Can language models perform implicit reasoning using internal hidden states distilled from explicit chain-of-thought reasoning, achieving comparable task-solving ability with faster inference?  
**Methodology**: The authors distill implicit reasoning steps from a teacher model trained on explicit chain-of-thought, with reasoning happening vertically among hidden states in different layers rather than horizontally through intermediate words, evaluated on multi-digit multiplication and GSM8K-Aug datasets.  
**Key findings**:
- Implicit CoT enables solving tasks previously not solvable without explicit CoT, such as GPT-2 Medium achieving 96% accuracy on 5×5 multiplication compared to 2% with no CoT [E25]
- Implicit CoT has higher inference speed compared to explicit CoT, especially for tasks with many intermediate steps like GSM8K-Aug and 5×5 multiplication [E26]
**Limitations**: Implicit CoT lacks transparency and interpretability compared to explicit CoT, as the internal processing within hidden states makes it challenging to understand how the model arrives at conclusions.

### Deng et al. (2024)

**Research question**: Can language models be taught to internalize explicit chain-of-thought reasoning steps while maintaining high performance?  
**Methodology**: The authors propose Stepwise Internalization, which starts with a model trained for explicit CoT reasoning and gradually removes intermediate steps while finetuning, allowing the model to internalize reasoning steps incrementally.  
**Key findings**:
- Stepwise Internalization enables GPT-2 Small to solve 9×9 multiplication with 99% accuracy, far exceeding No CoT [E17]
- ICoT-SI achieves state-of-the-art accuracy on GSM8K among models that don't output intermediate reasoning steps [E18]
- ICoT-SI offers 11x speedup over Explicit CoT while maintaining comparable accuracy on multiplication tasks [E19]
**Limitations**: The approach has high training cost due to finetuning required when removing each set of CoT tokens; training can be unstable with aggressive removal values; models lose interpretable intermediate steps; and explicit CoT still achieves higher accuracies compared to implicit CoT.

### Goyal et al. (2023)

**Research question**: Does delaying model computation via pause tokens help, hurt, or have no effect on language model performance, and does it matter whether delays are introduced during pretraining, finetuning, or both?  
**Methodology**: The authors trained decoder-only models (1B and 130M parameters) with learnable pause tokens appended to input sequences, delaying output generation until the last pause token. They evaluated four approaches: standard pretraining/finetuning, pause-pretraining only, pause-finetuning only, and both, across nine downstream tasks.  
**Key findings**:
- Pause-pretraining followed by pause-finetuning improves performance on eight tasks for the 1B model and six tasks for the 130M model compared to standard training [E20]
- The most prominent improvement is an 18% EM score gain on the SQuAD question-answering task for the 1B model [E21]
- Pause-pretraining is crucial for delays to help in downstream inference-time, as standard-pretrained models have biases that prevent realizing benefits of inference-time delays [E22]
**Limitations**: The expense of pause-pretraining prevents studying generalization across more model sizes beyond 1B and 130M, encoder-decoder architectures, or other pretraining mixtures and objectives.

### Hao et al. (2024)

**Research question**: Can large language models reason more effectively in a continuous latent space rather than being constrained to the language space?  
**Methodology**: The authors introduce Coconut (Chain of Continuous Thought), which uses the last hidden state of the LLM as a representation of the reasoning state and feeds it back as the next input embedding directly in the continuous space, enabling breadth-first search over reasoning paths.  
**Key findings**:
- Coconut with continuous thoughts significantly outperforms No-CoT baseline on GSM8k math reasoning [E8]
- Coconut is more token-efficient than traditional CoT while achieving higher accuracy on logical reasoning tasks [E9]
- Continuous latent reasoning enables emergent BFS-like search over multiple reasoning paths [E10]
**Limitations**: Further research is needed to refine and scale latent reasoning to pretraining, which could improve generalization across a broader range of reasoning challenges.

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance in language models?  
**Methodology**: The authors curated s1K, a dataset of 1,000 questions with reasoning traces, and developed budget forcing to control test-time compute by terminating or extending the model's thinking process. They supervised finetuned Qwen2.5-32B-Instruct on s1K and evaluated with budget forcing on reasoning benchmarks.  
**Key findings**:
- The s1-32B model exceeds o1-preview on competition math questions by up to 27% on MATH and AIME24 benchmarks [E27]
- Scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention, improving AIME24 accuracy from 50% to 57% [E28]
- Supervised finetuning on only 1,000 examples suffices to build a competitive reasoning model matching o1-preview performance [E29]
**Limitations**: Budget forcing has two key limitations when scaling further: it eventually flattens out in performance gains, and the context window of the underlying language model constrains it.

### Su et al. (2025)

**Research question**: Can mixing latent tokens with text tokens improve language model reasoning performance and efficiency?  
**Methodology**: The authors propose Token Assorted, which mixes latent tokens with text tokens for improved reasoning, evaluated on ProsQA benchmark with various compression rates.  
**Key findings**:
- The latent approach achieves 17.5% performance gain over CoT baseline on the difficult ProsQA benchmark [E5]
- The latent approach shows an average 17% reduction in token numbers compared with CoT while surpassing it in prediction accuracy [E6]
- Accuracy peaks at compression rate r=16 (28.1) and decreases at r=32 (27.9), indicating an optimal balance between compression and information preservation [E7]
**Limitations**: Not explicitly stated in the paper's conclusion.

### Yang et al. (2024)

**Research question**: Do large language models latently perform multi-hop reasoning when processing complex prompts that require multiple reasoning steps?  
**Methodology**: The authors analyze latent reasoning pathways using the TwoHopFact dataset, measuring internal entity recall (EntRec) for the first hop and consistency scores (CnstScore) for the second hop across LLaMA-2 models of different sizes.  
**Key findings**:
- First-hop reasoning shows clear scaling trends with larger model sizes [E14]
- Strong latent multi-hop reasoning evidence exists for certain prompt types, used in over 80% of cases [E15]
- Second-hop and full multi-hop reasoning evidence is moderate overall, with strongest evidence for first hop only [E16]
**Limitations**: The analysis is based on LLaMA-2 family up to 70B parameters; the study measures only one pathway for latent multi-hop reasoning and uses approximations for internal entity recall based on logit lens which has shortcomings like representation drift, bias, and brittleness.

## References

Biran, E., & Ravfogel, S. (2024). Hopping too late: Exploring the limitations of large language models on multi-hop queries. arXiv. https://arxiv.org/abs/2406.12775

Cheng, J., & Van Durme, B. (2024). Compressed chain of thought: Efficient reasoning through dense representations. arXiv. https://arxiv.org/abs/2412.13171

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X., Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., Liu, A., et al. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv. https://arxiv.org/abs/2501.12948

Deng, Y., Prasad, K., Fernandez, R., Smolensky, P., Chaudhary, V., & Shieber, S. (2023). Implicit chain of thought reasoning via knowledge distillation. arXiv. https://arxiv.org/abs/2311.01460

Deng, Y., Choi, Y., & Shieber, S. (2024). From explicit CoT to implicit CoT: Learning to internalize CoT step by step. arXiv. https://arxiv.org/abs/2405.14838

Goyal, S., Ji, Z., Rawat, A. S., Menon, A. K., Kumar, S., & Nagarajan, V. (2023). Think before you speak: Training language models with pause tokens. arXiv. https://arxiv.org/abs/2310.02226

Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). Training large language models to reason in a continuous latent space. arXiv. https://arxiv.org/abs/2412.06769

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Su, D., & Li, X. (2025). Token assorted: Mixing latent and text tokens for improved language model reasoning. arXiv. https://arxiv.org/abs/2502.03275

Yang, S., Gribovskaya, E., Kassner, N., Geva, M., & Riedel, S. (2024). Do large language models latently perform multi-hop reasoning? arXiv. https://arxiv.org/abs/2402.16837

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E8 | arXiv:2412.06769 | [5.3 Results and Discussion](https://arxiv.org/html/2412.06769#S5.SS3.p1) | “By using 6 continuous thoughts, Coconut achieves 34.1% accuracy on GSM8k, which significantly outperforms No-CoT (16.5%).” |
| E9 | arXiv:2412.06769 | [5.3 Results and Discussion](https://arxiv.org/html/2412.06769#S5.SS3.p4) | “Compared to traditional CoT, Coconut generates fewer tokens while achieving higher accuracy on ProntoQA and ProsQA.” |
| E10 | arXiv:2412.06769 | [6 Conclusion](https://arxiv.org/html/2412.06769#S6.p1) | “Reasoning in latent space gives rise to advanced emergent behaviors, where continuous thoughts can represent multiple alternative next steps.” |
| E23 | arXiv:2412.13171 | [5.2 Results and Discussion](https://arxiv.org/html/2412.13171#S5.SS2.p2) | “With a compression ratio of r=0.10, we see a 9 point improvement over the baseline with no contemplation tokens.” |
| E24 | arXiv:2412.13171 | [5.2 Results and Discussion](https://arxiv.org/html/2412.13171#S5.SS2.p2) | “Ultimately, our results show equipping a model with dense, contentful contemplation tokens produced by ccot allows the model to reason better” |
| E17 | arXiv:2405.14838 | [Stepwise Internalization is effective.](https://arxiv.org/html/2405.14838#S5.SS0.SSS0.Px1.p1) | “ICoT-SI enables a GPT-2 Small model to solve the 9×9 multiplication problem with an accuracy of 0.99, whereas the No CoT method fails on even 4×4 multiplication.” |
| E18 | arXiv:2405.14838 | [Stepwise Internalization is effective.](https://arxiv.org/html/2405.14838#S5.SS0.SSS0.Px1.p3) | “On the GSM8K dataset, ICoT-SI achieves a new state-of-the-art accuracy for models not using any intermediate steps.” |
| E19 | arXiv:2405.14838 | [Stepwise Internalization lags behind explicit CoT in accuracy but is faster.](https://arxiv.org/html/2405.14838#S5.SS0.SSS0.Px2.p1) | “On the 9×9 multiplication task, ICoT-SI is comparable in accuracy to Explicit CoT but is 11 times faster during inference.” |
| E25 | arXiv:2311.01460 | [5 Results](https://arxiv.org/html/2311.01460#S5.p1) | “Compared to no CoT, our approach enables solving tasks previously not solvable without explicit CoT” |
| E26 | arXiv:2311.01460 | [5 Results](https://arxiv.org/html/2311.01460#S5.p3) | “That being said, implicit CoT has a higher inference speed, especially for tasks with many intermediate steps such as GSM8K-Aug and 5×5 multiplication.” |
| E20 | arXiv:2310.02226 | [4.3 Results: Effect of pause-training](https://arxiv.org/html/2310.02226#S4.SS3.p2) | “Overall, this outperforms the standard baseline (StdPT_StdFT) on eight tasks for the 1B model, and on six tasks for the 130 M model” |
| E21 | arXiv:2310.02226 | [4.3 Results: Effect of pause-training](https://arxiv.org/html/2310.02226#S4.SS3.p2) | “Most prominently, for the 1B model on the SQuAD question-answering task, PausePT_PauseFT improves over StdPT_StdFT by an 18% EM score.” |
| E22 | arXiv:2310.02226 | [4.3 Results: Effect of pause-training](https://arxiv.org/html/2310.02226#S4.SS3.p6) | “Specifically, pause-pretraining appears crucial for delays to help in downstream inference-time.” |
| E11 | arXiv:2501.12948 | [4 Experiment](https://arxiv.org/html/2501.12948#S4.p2) | “DeepSeek-R1 Dev2 demonstrates marked performance enhancements on benchmarks that require advanced reasoning skills, including those focused on code generation, mathematical problem solving, and STEM-related tasks.” |
| E12 | arXiv:2501.12948 | [6 Conclusion, Limitation, and Future Work](https://arxiv.org/html/2501.12948#S6.p1) | “Sophisticated reasoning behaviors, such as self-verification and reflection, appeared to emerge organically during the reinforcement learning process.” |
| E13 | arXiv:2501.12948 | [6 Conclusion, Limitation, and Future Work](https://arxiv.org/html/2501.12948#S6.p3) | “Currently, the structural output capabilities of DeepSeek-R1 remain suboptimal compared to existing models.” |
| E27 | arXiv:2501.19393 | [Abstract](https://arxiv.org/html/2501.19393#abstract) | “our model s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24).” |
| E28 | arXiv:2501.19393 | [Abstract](https://arxiv.org/html/2501.19393#abstract) | “Further, scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention: from 50% to 57% on AIME24.” |
| E29 | arXiv:2501.19393 | [Models](https://arxiv.org/html/2501.19393#S6.SS1.SSS0.Px1.p1) | “We show that SFT on only 1,000 examples suffices to build a competitive reasoning model matching o1-preview” |
| E14 | arXiv:2402.16837 | [There is substantial evidence of the first hop of reasoning, which becomes stronger with increasing model size.](https://arxiv.org/html/2402.16837#S5.SS3.SSS0.Px1.p2) | “As model size increases from 7B to 13B and 70B, first-hop reasoning occurs more frequently for both entity substitution and relation substitution.” |
| E15 | arXiv:2402.16837 | [8 Discussion and Conclusion](https://arxiv.org/html/2402.16837#S8.p1) | “We find strong evidence of latent multi-hop reasoning for certain fact composition types with the reasoning pathway utilized in more than 80% of the cases.” |
| E16 | arXiv:2402.16837 | [8 Discussion and Conclusion](https://arxiv.org/html/2402.16837#S8.p1) | “The evidence of second and multi-hop reasoning across the whole set of prompts is rather moderate and only substantial in the first hop.” |
| E4 | arXiv:2406.12775 | [8 Conclusion](https://arxiv.org/html/2406.12775#S8.p1) | “the second hop is answered in the mid-upper layers only after the first hop is answered by the lower layers” |
| E3 | arXiv:2406.12775 | [6.3 Results](https://arxiv.org/html/2406.12775#S6.SS3.p1) | “correctly answering between 32%-66% of incorrect cases while keeping the correct cases at 100% across models and token positions” |
| E2 | arXiv:2406.12775 | [4.3 Results](https://arxiv.org/html/2406.12775#S4.SS3.p2) | “the MLP sublayers play a larger role in promoting the predicted token compared to that of the attention sublayers” |
| E5 | arXiv:2502.03275 | [Results](https://arxiv.org/html/2502.03275#S4.SS2.SSS1.Px2.p1) | “the latent approach achieves 17.5% performance gain” |
| E6 | arXiv:2502.03275 | [Tokens Efficiency Comparison](https://arxiv.org/html/2502.03275#S4.SS2.SSS2.Px3.p1) | “Our latent approach shows an average 17% reduction in token numbers compared with CoT while surpassing it in prediction accuracy” |
| E7 | arXiv:2502.03275 | [4.4 Ablations on the Latent parameters](https://arxiv.org/html/2502.03275#S4.SS4.p2) | “it further boosts up to 28.1 at r=16, and then it goes down to 27.9 when r=32” |

<!-- /evidence-appendix -->
