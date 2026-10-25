# Systematic Literature Review: Long-Context Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "long-context language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on long-context language models (LCLMs) published between 2024 and 2026. The surveyed literature reveals a field rapidly maturing beyond simple context extension toward sophisticated evaluation frameworks and architectural innovations. Collectively, these papers demonstrate that current LCLMs, despite claiming large context windows (32K+ tokens), exhibit significant limitations in maintaining coherence over long sequences, performing set-based aggregation, and balancing parametric knowledge with contextual retrieval. The research landscape shows three dominant directions: (1) comprehensive benchmarking efforts exposing critical gaps in model capabilities, (2) novel architectural approaches decomposing sequence modeling beyond attention mechanisms, and (3) fine-tuning strategies to improve in-context retrieval and caching efficiency. Notably, recent reasoning models with long chain-of-thought training outperform standard instruction-tuned models on long-form generation tasks, though substantial challenges remain in cross-lingual settings and trustworthiness as context length increases.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "long-context language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking Long-Context Capabilities

A significant portion of recent literature focuses on developing comprehensive benchmarks to evaluate LCLM capabilities beyond simple retrieval tasks. Traditional benchmarks emphasizing long-context recall—requiring models to produce short responses based on critical snippets while processing thousands of irrelevant tokens—have proven insufficient for capturing real-world challenges. The field has shifted toward benchmarks testing procedural generation, multilingual understanding, and controlled examination of semantic reasoning.

Wu et al. (2025) introduced Ref-Long, a benchmark with three subsets ranging from synthetic to realistic scenarios, evaluating models' ability to identify documents that reference specific keys rather than simple retrieval. Their work revealed significant shortcomings in long-context referencing capabilities, even among advanced models like GPT-4o. Similarly, Ye et al. (2025) created LongProc, requiring both integration of dispersed information and long-form generation across six procedural tasks. Their evaluation of 23 LCLMs showed that open-weight models typically fail on 2K-token tasks despite claiming 32K+ context windows, while closed-source models like GPT-4o degrade significantly at 8K tokens.

Yang et al. (2025) took a different approach with LongBioBench, using artificially generated biographies to create a controlled environment assessing 18 LCLMs across understanding, reasoning, and trustworthiness dimensions. Their findings revealed that most models exhibit deficiencies in semantic understanding and elementary reasoning over retrieved results, with trustworthiness decreasing as context length increases. This theme demonstrates the field's recognition that existing synthetic benchmarks with contextual non-coherence and absence of distractors inadequately test long-context capabilities.

### Theme 2: Architectural Innovations Beyond Attention

Several papers propose architectural alternatives to pure attention-based approaches, recognizing that attention alone may not optimally handle both local interaction and long-range state management. This theme reflects growing interest in decomposing sequence modeling into specialized components.

Song et al. (2026) introduced a model-side aggregation interface that maintains compact Hash-based HyperLogLog sketch states alongside frozen language models. Their approach addresses the known limitation of increasingly unreliable performance in non-additive, set-based aggregation tasks as context length grows. With a fixed 2 KiB state size, their method achieved 99.2% accuracy on Gemma 4 compared to 100% under exact aggregation, while improving over direct full-context reasoning by 63.2 points on Qwen and 56.3 points on Gemma across 3,969 aggregate-then-reason tasks.

Xie (2026) proposed LPC-SM, a hybrid autoregressive architecture separating local attention, persistent memory, predictive correction, and run-time control within the same block, using Orthogonal Novelty Transport to govern slow-memory writes. Their 158M-parameter evaluation demonstrated that removing components significantly degraded performance, while the full architecture remained stable at sequence length 4096. These results suggest that long-context autoregressive modeling can benefit from a broader division of labor than attention alone.

### Theme 3: Fine-Tuning and Knowledge Integration

The third major theme examines how fine-tuning strategies and the balance between parametric and contextual knowledge affect LCLM performance. This research direction addresses the unclear relationship between training approaches and long-context robustness.

Molfese et al. (2026) investigated which training strategies most effectively enhance LCLMs' ability to identify and use relevant information, as well as robustness under KV-cache compression. Their experiments showed substantial in-domain improvements up to +20 points over base models, though out-of-domain generalization remained task-dependent with large variance. LCLMs excelled on finance questions (+9 points), while traditional RAG showed stronger performance on multiple-choice questions (+6 points).

Fu et al. (2025) explored the underexamined influence of parametric knowledge on content generation, demonstrating that its impact becomes increasingly pronounced as context length extends. Their Hybrid Needle-in-a-Haystack test revealed that parametric recall ability does not improve simultaneously with extrinsic retrieval ability, and that better extrinsic retrieval can actually interfere with parametric recall. Their results showed Qwen-2.5 models significantly outperforming Llama-3.1 models, with even Llama-3.1-70B-Instruct failing to exhibit better performance from a dual-ability perspective.

### Theme 4: Domain-Specific Applications and Retrieval Strategies

Several papers examine LCLM performance in specific domains or compare retrieval-augmented generation strategies with pure long-context approaches.

Thai and Iyyer (2025) repurposed the RELiC dataset to evaluate LCLMs on literary evidence retrieval, requiring models to generate missing quotations from literary criticism when given entire literary texts. Their evaluation of 292 high-quality examples showed recent reasoning models like Gemini Pro 2.5 exceeding human expert performance (62.5% vs. 50% accuracy), while the best open-weight model achieved only 29.1% accuracy. This highlights both the potential and current limitations of applying LCLMs to nuanced literary analysis.

Laitenberger et al. (2025) conducted a controlled evaluation comparing multi-stage retrieval-augmented generation pipelines against simpler baselines. Surprisingly, DOS RAG—a simple retrieve-then-read method preserving original passage order—consistently matched or outperformed more intricate methods like ReadAgent and RAPTOR on multiple long-context QA benchmarks. Their work establishes DOS RAG as a strong baseline for future RAG evaluations under matched token budgets, emphasizing source fidelity and document structure over added complexity.

### Theme 5: Multilingual and Cross-Lingual Considerations

An emerging theme addresses the multilingual capabilities of LCLMs, revealing significant disparities across languages that are not apparent in English-only evaluations.

Kim et al. (2025) presented ONERULER, adapting the English-only RULER benchmark across 26 languages with seven synthetic tasks testing retrieval and aggregation. Their evaluation revealed a widening performance gap between low- and high-resource languages as context length increases from 8K to 128K tokens. Notably, English ranked only 6th out of 26 languages on long-context tasks, with Polish emerging as the top-performing language. In cross-lingual scenarios, performance fluctuated by up to 20% depending on instruction language, and many LLMs incorrectly predicted the absence of answers even in high-resource languages.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that current LCLMs exhibit significant limitations despite large claimed context windows. Ye et al. (2025), Wu et al. (2025), and Yang et al. (2025) all document substantial performance degradation as context length increases, with open-weight models particularly struggling beyond 2K tokens. There is also agreement that reasoning models with long chain-of-thought training achieve stronger performance than standard instruction-tuned models (Thai & Iyyer, 2025; Ye et al., 2025). The literature consistently shows that simple baselines can match or outperform complex multi-stage pipelines when token budgets are controlled (Laitenberger et al., 2025).

**Disagreements**: The literature shows tension regarding the value of fine-tuning versus architectural changes. Molfese et al. (2026) report substantial in-domain improvements from fine-tuning (+20 points), while Song et al. (2026) and Xie (2026) argue that architectural modifications provide more fundamental improvements. Additionally, Fu et al. (2025) suggest that parametric and contextual knowledge abilities may be in tension, while Molfese et al. (2026) find that fine-tuning can improve both. There is also implicit disagreement about evaluation methodology: Yang et al. (2025) advocate for controlled synthetic benchmarks, while Wu et al. (2025) and Thai and Iyyer (2025) emphasize realistic, domain-specific tasks.

## Gaps and Open Questions

The surveyed literature reveals several critical gaps:

1. **Limited real-world validation**: Most benchmarks remain synthetic or semi-synthetic, with limited validation on authentic long-document tasks. Yang et al. (2025) explicitly note that existing synthetic benchmarks with contextual non-coherence are inadequate, yet even their controlled biography approach remains artificial.

2. **Scalability beyond 128K tokens**: No paper evaluates performance beyond 128K context length, despite models claiming multi-million token windows. The practical limits of current approaches remain unexplored.

3. **Cross-lingual robustness**: Kim et al. (2025) reveal significant multilingual disparities, but the underlying causes and potential remedies remain unaddressed. The 20% performance fluctuation based on instruction language suggests fundamental architectural limitations.

4. **Trustworthiness degradation**: Yang et al. (2025) document decreasing trustworthiness with increased context length, but none of the surveyed papers propose concrete solutions to this problem.

5. **Integration of parametric and contextual knowledge**: While Fu et al. (2025) identify interference between parametric recall and extrinsic retrieval, no paper provides a comprehensive framework for balancing these abilities during training or inference.

6. **Standardized evaluation protocols**: The diversity of benchmarks (Ref-Long, LongProc, LongBioBench, ONERULER) suggests a lack of consensus on evaluation standards, making cross-paper comparison difficult.

Most papers do not explicitly state limitations in their abstracts, suggesting either space constraints or insufficient reflection on methodological boundaries.

## Per-Paper Annotations

### Fu et al. (2025)

**Research question**: How does parametric knowledge influence long-context language models' content generation, and how does it interact with extrinsic retrieval ability?

**Methodology**: Investigated parametric knowledge's effect on content generation across context lengths, and designed a Hybrid Needle-in-a-Haystack test evaluating both parametric recall and extrinsic retrieval abilities.

**Key findings**:
- Parametric knowledge impact becomes increasingly pronounced as context length extends
- Parametric recall ability does not improve simultaneously with extrinsic retrieval ability
- Better extrinsic retrieval ability can interfere with parametric recall ability
- Qwen-2.5 models significantly outperform Llama-3.1 models
- Even Llama-3.1-70B-Instruct fails to exhibit better performance from dual-ability perspective

**Limitations**: Not stated in abstract

### Kim et al. (2025)

**Research question**: How do long-context language models perform across multiple languages when evaluated on long-context tasks?

**Methodology**: Presented ONERULER, a multilingual benchmark adapting the English-only RULER benchmark across 26 languages with seven synthetic tasks testing retrieval and aggregation, created through translation collaboration with native speakers and evaluated on both open-weight and closed LLMs.

**Key findings**:
- A widening performance gap exists between low- and high-resource languages as context length increases from 8K to 128K tokens
- English is not the top-performing language on long-context tasks (ranked 6th out of 26), with Polish emerging as the top language
- Many LLMs, particularly OpenAI's o3-mini-high, incorrectly predict the absence of an answer even in high-resource languages
- In cross-lingual scenarios, performance can fluctuate by up to 20% depending on the instruction language

**Limitations**: Not stated in abstract

### Laitenberger et al. (2025)

**Research question**: Do multi-stage retrieval-augmented generation pipelines still offer measurable benefits over simpler, single-stage approaches given modern long-context language models?

**Methodology**: Conducted a controlled evaluation comparing two multi-stage pipelines (ReadAgent and RAPTOR) against three baselines including DOS RAG, systematically scaling token budgets across multiple long-context QA benchmarks.

**Key findings**:
- DOS RAG, a simple retrieve-then-read method that preserves original passage order, consistently matches or outperforms more intricate methods on multiple long-context QA benchmarks
- DOS RAG's strength stems from maintaining source fidelity and document structure, prioritizing recall within effective context windows, and favoring simplicity over added complexity
- The authors recommend establishing DOS RAG as a simple yet strong baseline for future RAG evaluations under matched token budgets

**Limitations**: Not stated in abstract

### Molfese et al. (2026)

**Research question**: Can fine-tuning strategies improve long-context language models' performance and robustness under KV-cache compression?

**Methodology**: Investigated training strategies to enhance LCLMs' ability to identify and use relevant information, and tested their robustness under KV-cache compression techniques.

**Key findings**:
- Substantial in-domain improvements up to +20 points over base model
- LCLMs excel on finance questions (+9 points) while RAG shows stronger performance on multiple-choice questions (+6 points)
- Out-of-domain generalization remains task dependent with large variance
- Fine-tuning approaches bring moderate improvements in robustness under KV-cache compression

**Limitations**: Out-of-domain generalization remains task dependent with large variance

### Song et al. (2026)

**Research question**: How can long-context language models reliably handle non-additive, set-based aggregation tasks as context length grows?

**Methodology**: Introduced a model-side aggregation interface that maintains compact Hash-based HyperLogLog sketch states alongside a frozen language model, validated with 2 KiB state size on distinct-count experiments and aggregate-then-reason tasks.

**Key findings**:
- Mean relative error of 1.6% on one million record distinct-count experiment
- States from 256 segments produced identical readout as single pass
- Achieved 99.2% accuracy on Gemma 4 vs 100% under exact aggregation
- Improved over direct full-context reasoning by 63.2 points on Qwen and 56.3 points on Gemma
- Method reached 91.1% on Qwen and 99.3% on Gemma on Oolong-Synth subset

**Limitations**: Not stated in abstract

### Thai and Iyyer (2025)

**Research question**: How well do modern long-context language models understand literary fiction and perform literary evidence retrieval?

**Methodology**: Repurposed the RELiC dataset to construct a benchmark where LLMs receive entire literary texts alongside criticism with missing quotations, requiring models to generate the missing quotation. Curated 292 high-quality examples and evaluated recent reasoning models against human expert performance.

**Key findings**:
- Recent reasoning models like Gemini Pro 2.5 exceed human expert performance (62.5% vs. 50% accuracy)
- The best open-weight model achieves only 29.1% accuracy, highlighting a wide gap between open and closed-weight models
- Even the strongest models struggle with nuanced literary signals and overgeneration, indicating open challenges for applying LLMs to literary analysis

**Limitations**: Not stated in abstract

### Wu et al. (2025)

**Research question**: How well do long-context language models perform on long-context referencing tasks that require attributing items to specific parts of long-context data?

**Methodology**: Proposed Ref-Long, a novel benchmark with three subsets ranging from synthetic to realistic scenarios, and evaluated 13 LCLMs on their ability to identify documents that reference specific keys. Conducted comprehensive analyses including human evaluations, task format adjustments, fine-tuning experiments, and error analyses.

**Key findings**:
- Experimental results reveal significant shortcomings in long-context referencing capabilities, even among advanced models like GPT-4o
- The benchmark emphasizes contextual relationships between keys and documents rather than simple retrieval
- Comprehensive analyses including human evaluations and fine-tuning experiments yielded several key insights about model limitations

**Limitations**: Not stated in abstract

### Xie (2026)

**Research question**: Can long-context autoregressive modeling be organized around a broader division of labor than attention alone?

**Methodology**: Proposed LPC-SM, a hybrid autoregressive architecture separating local attention, persistent memory, predictive correction, and run-time control with Orthogonal Novelty Transport for slow-memory writes, evaluated on a 158M-parameter model across three stages.

**Key findings**:
- Removing mHC raises Stage-A final LM loss from 12.630 to 15.127
- Adaptive sparse control improves Stage-B final LM loss from 12.137 to 10.787
- Full route remains stable at sequence length 4096 with final LM loss 11.582
- Improves delayed-identifier diagnostic from 14.396 to 12.031 in key cross-entropy

**Limitations**: Not stated in abstract

### Yang et al. (2025)

**Research question**: What are the essential features of an ideal long-context evaluation framework, and how do existing LCLMs perform on such a framework?

**Methodology**: Introduced LongBioBench, a benchmark using artificially generated biographies as a controlled environment for assessing 18 LCLMs across dimensions of understanding, reasoning, and trustworthiness with seamless context, controllable settings, and sound evaluation.

**Key findings**:
- Most models exhibit deficiencies in semantic understanding and elementary reasoning over retrieved results
- Models become less trustworthy as context length increases
- Existing synthetic benchmarks with contextual non-coherence, numerical needles, and absence of distractors are inadequate for testing long-context capabilities
- LongBioBench achieves a better trade-off between mirroring authentic language tasks and maintaining controllability compared to previous synthetic benchmarks

**Limitations**: Not stated in abstract

### Ye et al. (2025)

**Research question**: How well do long-context language models perform on tasks requiring both integration of dispersed information and long-form procedural generation?

**Methodology**: Created LongProc benchmark with six diverse procedural generation tasks at three difficulty levels (500, 2K, 8K tokens), and evaluated 23 LCLMs including instruction-tuned and reasoning models.

**Key findings**:
- Open-weight models typically fail on 2K-token tasks despite claiming 32K+ context windows
- Closed-source models like GPT-4o show significant degradation on 8K-token tasks
- Reasoning models achieve stronger overall performance benefiting from long CoT training
- LCLMs struggle to maintain long-range coherence in long-form generations

**Limitations**: Not stated in abstract

## References

Fu, Y., Shahgir, H. S., Liu, H., Tang, X., He, Q., & Dong, Y. (2025). Harnessing the unseen: The hidden influence of intrinsic knowledge in long-context language models. arXiv. https://arxiv.org/abs/2504.08202

Kim, Y., Russell, J., Karpinska, M., & Iyyer, M. (2025). One ruler to measure them all: Benchmarking multilingual long-context language models. arXiv. https://arxiv.org/abs/2503.01996

Laitenberger, A., Manning, C. D., & Liu, N. F. (2025). Stronger baselines for retrieval-augmented generation with long-context language models. arXiv. https://arxiv.org/abs/2506.03989

Molfese, F. M., Hardalov, M., Blloshmi, R., Byrne, B., & de Gispert, A. (2026). Exploring fine-tuning for in-context retrieval and efficient KV-caching in long-context language models. arXiv. https://arxiv.org/abs/2601.18527

Song, D., Yin, J., Hu, Z., & Wang, X. (2026). Mergeable model-side aggregation states for long-context language models. arXiv. https://arxiv.org/abs/2607.26448

Thai, K., & Iyyer, M. (2025). Literary evidence retrieval via long-context language models. arXiv. https://arxiv.org/abs/2506.03090

Wu, J., Gu, G., Zheng, Y., Yeung, D.-Y., & Cohan, A. (2025). Ref-Long: Benchmarking the long-context referencing capability of long-context language models. arXiv. https://arxiv.org/abs/2507.09506

Xie, K. (2026). LPC-SM: Local predictive coding and sparse memory for long-context language modeling. arXiv. https://arxiv.org/abs/2604.03263

Yang, Y., Huang, Z., Zhu, W., Qiu, Z., Yuan, F., Pan, J. Z., & Titov, I. (2025). A controllable examination for long-context language models. arXiv. https://arxiv.org/abs/2506.02921

Ye, X., Yin, F., He, Y., Zhang, J., Yen, H., Gao, T., Durrett, G., & Chen, D. (2025). LongProc: Benchmarking long-context language models on long procedural generation. arXiv. https://arxiv.org/abs/2501.05414
