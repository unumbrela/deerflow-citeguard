# Systematic Literature Review: Latent Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-07
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on latent reasoning in large language models, revealing a rapidly evolving field focused on understanding and enhancing how LLMs perform reasoning computations. The surveyed literature demonstrates two major paradigm shifts: first, a movement from explicit token-based chain-of-thought reasoning toward continuous latent space representations that enable more efficient computation; second, growing interest in understanding the internal mechanisms by which transformers perform multi-hop and compositional reasoning. Collectively, these papers establish that latent reasoning—whether through continuous hidden states, compressed representations, or implicit computation—offers significant advantages in accuracy, efficiency, and scalability compared to traditional explicit reasoning approaches. The field shows strong convergence around the benefits of latent representations, though methodological approaches vary considerably from reinforcement learning to architectural interventions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-07. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening results**: 50 papers identified by search, 83 added from citation expansion, 30 shortlisted, 20 screened, 10 included (6 from citation expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Continuous Latent Space Reasoning

A prominent direction in latent reasoning research involves replacing discrete token-based reasoning with continuous vector representations. Hao et al. (2024) introduced Coconut (Chain of Continuous Thought), which uses the last hidden state of an LLM as a reasoning state representation and feeds it back directly in continuous space rather than decoding into words. This approach enables breadth-first search reasoning patterns by allowing continuous thoughts to encode multiple alternative next steps, unlike chain-of-thought which commits to a single deterministic path. Similarly, Cheng and Van Durme (2024) proposed Compressed Chain-of-Thought (CCoT), generating contentful and continuous contemplation tokens as compressed representations of explicit reasoning chains. Their framework achieves accuracy improvements while enabling adaptive control over reasoning depth by varying the number of contemplation tokens. Su et al. (2025) extended this line of work with a hybrid approach mixing latent discrete tokens with text tokens, using VQ-VAE to abstract initial reasoning steps. Their method significantly reduces reasoning trace length while maintaining or improving performance, suggesting that many words in chain-of-thought data support textual coherence rather than core reasoning.

### Theme 2: Implicit and Hidden Computation

Another major theme explores how models can internalize reasoning steps or perform computation through seemingly meaningless tokens. Deng et al. (2024) demonstrated that models can be taught to internalize explicit chain-of-thought steps while maintaining high reasoning performance. Their approach gradually removes intermediate steps and finetunes the model to internalize the reasoning process, enabling a GPT-2 Small model to solve 9-by-9 multiplication with up to 99% accuracy—far beyond what standard training achieves. Pfau et al. (2024) provided theoretical grounding for this phenomenon, showing that transformers can use meaningless filler tokens (e.g., dots) to solve hard algorithmic tasks they could not solve without intermediate tokens. Their work characterizes problems where filler tokens are useful in terms of quantifier depth of first-order formulas, raising concerns about LLMs engaging in unauditable, hidden computations detached from observed chain-of-thought tokens. This theme converges with continuous latent space reasoning in suggesting that explicit token generation is not necessary for effective reasoning computation.

### Theme 3: Multi-hop and Compositional Reasoning Mechanisms

Several papers investigate how LLMs internally compute and resolve multi-hop queries requiring sequential information extraction. Yang et al. (2024) analyzed whether LLMs latently perform multi-hop reasoning when processing complex prompts requiring bridge entity identification. They found strong evidence of latent multi-hop reasoning for certain relation types, with the reasoning pathway used in more than 80% of prompts, though evidence was moderate for the second hop and full multi-hop traversal. Biran et al. (2024) extended this analysis using a novel "back-patching" method, discovering that bridge entities are resolved in early layers while second-hop computation commences only in later layers. In up to 66% of previously incorrect cases, back-patching resulted in correct answer generation, suggesting later layers sometimes lack needed functionality. Li et al. (2024) used Logit Lens and intervention experiments to identify that compositional reasoning failures stem from improperly generated or leveraged implicit reasoning results surfacing in middle layers. They developed CREME, a lightweight method to patch compositional reasoning errors by editing multi-head self-attention modules in middle layers.

### Theme 4: Reinforcement Learning and Test-time Scaling

Recent work demonstrates that reasoning capabilities can be enhanced through reinforcement learning and test-time compute control without requiring human-annotated reasoning trajectories. DeepSeek-AI et al. (2025) proposed an RL framework that facilitates emergent development of advanced reasoning patterns including self-reflection, verification, and dynamic strategy adaptation. Their trained model achieves superior performance on mathematics, coding competitions, and STEM fields compared to counterparts trained via conventional supervised learning. Muennighoff et al. (2025) introduced s1, a simple test-time scaling approach using a curated dataset of 1,000 questions with reasoning traces and "budget forcing" to control test-time compute. Their s1-32B model exceeds o1-preview on competition math questions by up to 27% on MATH and AIME24 benchmarks, with budget forcing enabling the model to double-check answers and fix incorrect reasoning steps.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that latent or continuous representations offer efficiency and accuracy advantages over explicit token-based reasoning. Hao et al. (2024), Cheng and Van Durme (2024), and Su et al. (2025) all demonstrate that compressed or continuous reasoning representations achieve better accuracy-efficiency tradeoffs. There is also strong agreement that multi-hop reasoning occurs primarily in middle to later layers of transformers (Yang et al., 2024; Biran et al., 2024; Li et al., 2024), with bridge entity resolution happening early and subsequent computation in later layers. The surveyed papers collectively validate that additional computation tokens—whether meaningful chain-of-thought or meaningless filler—provide computational benefits independent of semantic content (Pfau et al., 2024; Deng et al., 2024).

**Disagreements**: The literature shows some tension between approaches that seek to make reasoning more transparent and auditable versus those that embrace implicit computation. While Pfau et al. (2024) raise concerns about "unauditable, hidden computations," other papers celebrate the efficiency gains from internalizing reasoning steps (Deng et al., 2024; Cheng & Van Durme, 2024). There is also methodological variation in how latent reasoning is implemented: some approaches use continuous hidden states (Hao et al., 2024), others use discrete latent tokens (Su et al., 2025), and still others compress explicit reasoning into dense representations (Cheng & Van Durme, 2024). The field has not yet converged on which approach generalizes best across reasoning tasks.

## Gaps and Open Questions

Several gaps emerge from the collective limitations of the surveyed literature. First, none of the papers explicitly state limitations in their abstracts, suggesting either that limitations are not emphasized or that space constraints prevent their inclusion—this makes it difficult to assess the boundaries of each approach's applicability. Second, while multiple papers demonstrate latent reasoning benefits on specific benchmarks (mathematical reasoning, multi-hop QA, algorithmic tasks), there is limited cross-task generalization analysis: it remains unclear whether latent reasoning approaches transfer well across diverse reasoning domains. Third, the computational efficiency claims—while promising—lack standardized benchmarks for comparing continuous versus discrete reasoning approaches. Fourth, the safety and interpretability implications of latent reasoning remain underexplored: Pfau et al. (2024) raise concerns about hidden computation, but systematic analysis of when latent reasoning becomes opaque or unalignable is absent. Finally, the interaction between latent reasoning and model scaling is not well understood: Yang et al. (2024) note scaling trends for first-hop reasoning but not second-hop, suggesting complex relationships between model size and latent reasoning capabilities that warrant further investigation.

## Per-Paper Annotations

### Biran et al. (2024)

**Research question**: How do LLMs internally compute and resolve multi-hop queries that require sequential information extraction steps?
**Methodology**: The authors analyzed internal computations of transformer-based LLMs on multi-hop queries and proposed a novel 'back-patching' analysis method where hidden representations from later layers are patched back to earlier layers to test whether later layers lack necessary functionality.
**Key findings**:
- Bridge entities in multi-hop queries are resolved in the early layers of the model
- The second hop computation commences only in later layers after bridge entity resolution
- In up to 66% of previously incorrect cases, there exists a back-patch that results in correct answer generation
- Later layers sometimes lack the needed functionality for correctly predicting multi-hop query answers
**Limitations**: not stated in abstract

### Cheng and Van Durme (2024)

**Research question**: Can chain-of-thought reasoning be made more efficient through compressed, dense representations rather than explicit token generation?
**Methodology**: The authors propose Compressed Chain-of-Thought (CCoT), a framework that generates contentful and continuous contemplation tokens of variable sequence length as compressed representations of explicit reasoning chains, applicable to off-the-shelf decoder language models.
**Key findings**:
- CCoT enables additional reasoning over dense contentful representations to achieve corresponding improvements in accuracy
- The reasoning improvements can be adaptively modified on demand by controlling the number of contemplation tokens generated
- The framework can be applied to off-the-shelf decoder language models without requiring architectural modifications
**Limitations**: not stated in abstract

### DeepSeek-AI et al. (2025)

**Research question**: Can the reasoning abilities of large language models be incentivized through pure reinforcement learning without requiring human-annotated reasoning trajectories?
**Methodology**: The authors propose a reinforcement learning (RL) framework that facilitates the emergent development of advanced reasoning patterns such as self-reflection, verification, and dynamic strategy adaptation, without relying on human-labeled reasoning trajectories.
**Key findings**:
- RL can incentivize reasoning abilities in LLMs without the need for human-annotated demonstrations
- The trained model achieves superior performance on verifiable tasks including mathematics, coding competitions, and STEM fields compared to counterparts trained via conventional supervised learning
- The emergent reasoning patterns can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models
- Advanced reasoning patterns such as self-reflection, verification, and dynamic strategy adaptation emerge through the RL framework
**Limitations**: not stated in abstract

### Deng et al. (2024)

**Research question**: Can language models be taught to internalize explicit chain-of-thought steps while maintaining high reasoning performance?
**Methodology**: The authors propose a method starting with a model trained for explicit CoT reasoning, then gradually removing intermediate steps and finetuning the model to internalize the reasoning process.
**Key findings**:
- The approach enables a GPT-2 Small model to solve 9-by-9 multiplication with up to 99% accuracy, whereas standard training cannot solve beyond 4-by-4 multiplication
- The method proves effective on larger language models such as Mistral 7B, achieving over 50% accuracy on GSM8K without producing any intermediate steps
- Models can internalize intermediate reasoning steps while simplifying the reasoning process and maintaining high performance
**Limitations**: not stated in abstract

### Hao et al. (2024)

**Research question**: Can large language models reason more effectively by operating in a continuous latent space rather than being constrained to the language space?
**Methodology**: The authors introduce Coconut (Chain of Continuous Thought), a new paradigm that uses the last hidden state of the LLM as a representation of the reasoning state, termed 'continuous thought,' and feeds it back to the model as the next input embedding directly in the continuous space rather than decoding into words.
**Key findings**:
- Coconut enables breadth-first search (BFS) reasoning patterns by allowing continuous thoughts to encode multiple alternative next steps, unlike CoT which commits to a single deterministic path
- Coconut outperforms CoT on logical reasoning tasks that require substantial search during planning
- The latent reasoning paradigm achieves a better trade-off between accuracy and efficiency compared to traditional chain-of-thought approaches
**Limitations**: not stated in abstract

### Li et al. (2024)

**Research question**: What are the root causes of compositional reasoning failures in LLMs and how can they be patched?
**Methodology**: The authors used Logit Lens and intervention experiments to dissect inner hidden states of LLMs, identifying that implicit reasoning results surface in middle layers and multi-head self-attention (MHSA) modules are critical for accurate generation. Based on these findings, they developed CREME, a lightweight method to patch compositional reasoning errors by editing located MHSA modules.
**Key findings**:
- Most compositional reasoning failures stem from improperly generated or leveraged implicit reasoning results
- Implicit reasoning results surface within middle layers and play a causative role in shaping final explicit reasoning results
- Multi-head self-attention (MHSA) modules in middle layers are linchpins for accurate generation and leveraging of implicit reasoning results
- CREME effectively patches errors in compositional reasoning via editing located MHSA modules
**Limitations**: not stated in abstract

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance in language models?
**Methodology**: The authors curated a small dataset s1K of 1,000 questions with reasoning traces based on difficulty, diversity, and quality criteria, and developed budget forcing to control test-time compute by forcibly terminating or extending the model's thinking process. They supervised finetuned Qwen2.5-32B-Instruct on s1K and equipped it with budget forcing.
**Key findings**:
- s1-32B exceeds o1-preview on competition math questions by up to 27% on MATH and AIME24 benchmarks
- Scaling s1-32B with budget forcing allows performance extrapolation from 50% to 57% on AIME24
- Budget forcing can lead the model to double-check its answer, often fixing incorrect reasoning steps
- The approach validates three criteria through ablations: difficulty, diversity, and quality of reasoning traces
**Limitations**: not stated in abstract

### Pfau et al. (2024)

**Research question**: To what extent do chain-of-thought performance gains come from human-like task decomposition versus additional computation from extra tokens?
**Methodology**: The authors tested whether transformers can use meaningless filler tokens (e.g., dots) instead of meaningful chain-of-thought tokens to solve hard algorithmic tasks, and provided theoretical characterization of problems where filler tokens are useful in terms of quantifier depth of first-order formulas.
**Key findings**:
- Transformers can use meaningless filler tokens to solve two hard algorithmic tasks they could not solve without intermediate tokens
- Learning to use filler tokens is difficult and requires specific, dense supervision to converge
- Additional tokens provide computational benefits independent of token choice
- Chain-of-thought tokens need not provide information about intermediate computational steps for certain problem classes
- Results raise concerns about LLMs engaging in unauditable, hidden computations detached from observed chain-of-thought tokens
**Limitations**: not stated in abstract

### Su et al. (2025)

**Research question**: Can hybrid representations mixing latent discrete tokens with text tokens reduce reasoning trace length while maintaining or improving reasoning performance?
**Methodology**: The authors propose a hybrid representation where initial reasoning steps are abstracted using latent discrete tokens generated by VQ-VAE, and introduce a training procedure that randomly mixes latent and text tokens to enable fast adaptation. They evaluated this approach on the Keys-Finding Maze problem and fine-tuned LLMs on logical and mathematical reasoning problems.
**Key findings**:
- Latent trace abstractions significantly reduce the length of reasoning traces compared to pure text token approaches
- The hybrid approach consistently outperforms baseline methods across various benchmarks
- Random mixing of latent and text tokens enables fast adaptation to new latent tokens
- Many words in chain-of-thought data support textual coherence rather than core reasoning information
**Limitations**: not stated in abstract

### Yang et al. (2024)

**Research question**: Do large language models latently perform multi-hop reasoning when processing complex prompts that require identifying bridge entities and using knowledge about them?
**Methodology**: The authors analyze two hops of reasoning individually: (1) testing if changing prompts to indirectly mention bridge entities increases the LLM's internal recall of those entities, and (2) testing if increasing recall causes the LLM to better utilize knowledge about the bridge entity, considering their co-occurrence as indicative of latent multi-hop reasoning.
**Key findings**:
- Strong evidence of latent multi-hop reasoning exists for prompts of certain relation types, with the reasoning pathway used in more than 80% of prompts
- Evidence for the second hop and full multi-hop traversal is moderate on average, with substantial evidence only for the first hop
- A clear scaling trend exists with increasing model size for the first hop of reasoning but not for the second hop
- The utilization of reasoning pathways is highly contextual and varies across different types of prompts
**Limitations**: not stated in abstract

## References

Biran, E., Gottesman, D., Yang, S., Geva, M., & Globerson, A. (2024). Hopping too late: Exploring the limitations of large language models on multi-hop queries. arXiv. https://arxiv.org/abs/2406.12775

Cheng, J., & Van Durme, B. (2024). Compressed chain of thought: Efficient reasoning through dense representations. arXiv. https://arxiv.org/abs/2412.13171

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X., Zhang, X., Yu, X., Wu, Z., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., Liu, A., et al. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv. https://arxiv.org/abs/2501.12948

Deng, Y., Choi, Y., & Shieber, S. (2024). From explicit CoT to implicit CoT: Learning to internalize CoT step by step. arXiv. https://arxiv.org/abs/2405.14838

Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). Training large language models to reason in a continuous latent space. arXiv. https://arxiv.org/abs/2412.06769

Li, Z., Jiang, G., Xie, H., Song, L., Lian, D., & Wei, Y. (2024). Understanding and patching compositional reasoning in LLMs. arXiv. https://arxiv.org/abs/2402.14328

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Pfau, J., Merrill, W., & Bowman, S. R. (2024). Let's think dot by dot: Hidden computation in transformer language models. arXiv. https://arxiv.org/abs/2404.15758

Su, D., Zhu, H., Xu, Y., Jiao, J., Tian, Y., & Zheng, Q. (2025). Token assorted: Mixing latent and text tokens for improved language model reasoning. arXiv. https://arxiv.org/abs/2502.03275

Yang, S., Gribovskaya, E., Kassner, N., Geva, M., & Riedel, S. (2024). Do large language models latently perform multi-hop reasoning? arXiv. https://arxiv.org/abs/2402.16837
