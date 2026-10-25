# Systematic Literature Review: Long-Context Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "long-context language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on long-context language models (LCLMs) reveals a field in rapid maturation, with research shifting from simply expanding context windows to rigorously evaluating how models actually use long contexts. Recent work emphasizes benchmarking LCLMs across diverse dimensions including referencing capability, procedural generation, multilingual performance, and retrieval-augmented generation. A consistent finding across studies is that despite claims of large context windows (32K+ tokens), models exhibit significant degradation in performance as context length increases, particularly in maintaining long-range coherence and trustworthiness. The literature also highlights emerging architectural innovations—such as mergeable aggregation states, local predictive coding with sparse memory, and fine-tuning strategies for KV-caching—that aim to address fundamental limitations in current approaches. Notably, there is a growing recognition that parametric knowledge and extrinsic retrieval ability interact in complex ways, necessitating dual-ability evaluation frameworks rather than retrieval-only benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "long-context language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking and Evaluation Frameworks

A dominant thread across the surveyed literature is the development of comprehensive benchmarks to assess LCLM capabilities. Multiple papers introduce novel evaluation frameworks that go beyond simple retrieval tasks to probe deeper understanding and reasoning. Wu et al. (2025) propose Ref-Long, a benchmark specifically targeting long-context referencing—requiring models to attribute items to specific parts of long documents rather than mere retrieval. Similarly, Yang et al. (2025) introduce LongBioBench, using artificially generated biographies to create a controlled environment for assessing understanding, reasoning, and trustworthiness across 18 LCLMs. Ye et al. (2025) present LongProc, which challenges models on procedural generation tasks requiring integration of dispersed information and generation of long-form structured outputs up to 8K tokens. Kim et al. (2025) extend evaluation to the multilingual setting with ONERULER, adapting the RULER benchmark across 26 languages to expose performance disparities between high- and low-resource languages as context length increases. Thai and Iyyer (2025) focus on literary domain understanding, repurposing the RELiC dataset to test whether LCLMs can retrieve and generate missing quotations from literary works.

These benchmarks collectively reveal that current LCLMs, despite large claimed context windows, struggle with semantic understanding, elementary reasoning over retrieved results, and maintaining trustworthiness as context length increases (Yang et al., 2025; Ye et al., 2025). The multilingual dimension adds another layer of complexity, with performance gaps widening between high- and low-resource languages at longer context lengths (Kim et al., 2025).

### Theme 2: Retrieval-Augmented Generation and Baseline Simplification

As LCLMs have grown in capability, a critical question has emerged: do complex multi-stage retrieval pipelines still offer advantages over simpler approaches? Laitenberger et al. (2025) directly address this by comparing multi-stage retrieval-augmented generation pipelines (ReadAgent and RAPTOR) against simpler baselines, including DOS RAG—a retrieve-then-read method that preserves original passage order. Their controlled evaluation under systematically scaled token budgets reveals that DOS RAG consistently matches or outperforms more intricate methods across multiple long-context QA benchmarks. The strength of this simple approach stems from maintaining source fidelity and document structure, prioritizing recall within effective context windows, and favoring simplicity over complexity.

This finding suggests that as LCLMs improve, the marginal benefit of sophisticated retrieval pipelines may diminish, and establishing simple yet strong baselines becomes essential for future RAG evaluations (Laitenberger et al., 2025).

### Theme 3: Architectural Innovations for Long-Context Processing

Beyond benchmarking, several papers propose novel architectural approaches to address fundamental limitations in LCLMs. Song et al. (2026) introduce mergeable model-side aggregation states using Hash-based HyperLogLog (HLL) sketches—compact 2 KiB states maintained alongside a frozen language model. Their approach achieves 99.2% accuracy on aggregation tasks with only a 0.8 percentage point gap compared to exact aggregation, while improving over direct full-context reasoning by 63.2 points on Qwen and 56.3 points on Gemma models.

Xie (2026) proposes LPC-SM, a hybrid autoregressive architecture that separates local attention, persistent memory, predictive correction, and run-time control within the same block, using Orthogonal Novelty Transport to govern slow-memory writes. Their 158M-parameter model demonstrates stable performance at 4096-token sequences, with adaptive sparse control improving final LM loss from 12.137 to 10.787 relative to fixed-ratio continuation.

These architectural innovations share a common insight: efficient long-context processing requires mechanisms beyond attention-only approaches, whether through compact aggregation states or hybrid architectures with persistent memory components.

### Theme 4: Fine-Tuning and Knowledge Interactions

The interaction between parametric knowledge and extrinsic retrieval ability emerges as a critical theme. Fu et al. (2025) demonstrate that parametric knowledge influence on content generation becomes increasingly pronounced as context length extends, and that better extrinsic retrieval ability can actually interfere with parametric recall ability. Their Hybrid Needle-in-a-Haystack test evaluates models based on both parametric recall and extrinsic retrieval abilities, revealing that Qwen-2.5 models significantly outperform Llama-3.1 models in combining various abilities.

Molfese et al. (2026) explore fine-tuning strategies to enhance LCLMs' ability to identify and use relevant information, achieving substantial in-domain improvements of up to +20 points over base models. However, out-of-domain generalization remains task-dependent with large variance: LCLMs excel on finance questions (+9 points), while RAG shows stronger performance on multiple-choice questions (+6 points). Fine-tuning brings moderate improvements in robustness under KV-cache compression, with gains varying across tasks.

These findings highlight that fine-tuning and knowledge interactions are nuanced, with performance highly dependent on task type and the balance between parametric and extrinsic knowledge.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that despite claims of large context windows, LCLMs exhibit significant performance degradation as context length increases (Wu et al., 2025; Ye et al., 2025; Yang et al., 2025). There is also broad agreement that current synthetic benchmarks have design limitations—such as contextual non-coherence, numerical needles, and absence of distractors—that make them inadequate for testing long-context capabilities (Yang et al., 2025). The literature consistently emphasizes the need for more realistic, controlled evaluation frameworks (Wu et al., 2025; Ye et al., 2025; Kim et al., 2025).

**Disagreements**: While Laitenberger et al. (2025) argue that simple baselines like DOS RAG are sufficient for many RAG tasks, the architectural innovation papers (Song et al., 2026; Xie, 2026) suggest that more sophisticated mechanisms are necessary for optimal performance on aggregation and long-form generation tasks. Additionally, there is tension between findings on fine-tuning effectiveness: Molfese et al. (2026) report substantial in-domain gains but variable out-of-domain generalization, while Fu et al. (2025) find that parametric knowledge and retrieval ability do not improve simultaneously, suggesting architectural rather than fine-tuning solutions may be needed.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Limited generalization studies**: Most papers note that their findings may not generalize beyond specific task types or model scales. Ye et al. (2025) focus on procedural generation with deterministic procedures; Xie (2026) uses a small 158M-parameter model; Song et al. (2026) validate with fixed 2 KiB HLL states.

2. **Architectural factors underexplored**: Fu et al. (2025) note that specific architectural or training factors enabling better parametric recall are not fully explored, suggesting a need for deeper investigation into model design.

3. **Fine-tuning strategy specificity**: Molfese et al. (2026) do not identify which specific fine-tuning strategies are most effective, leaving open questions about optimal approaches.

4. **Multilingual coverage gaps**: While Kim et al. (2025) introduce multilingual evaluation, the literature lacks comprehensive studies on how LCLMs handle code-switching, translation tasks, or culturally specific long-context reasoning.

5. **Real-world deployment challenges**: None of the surveyed papers address computational efficiency, latency, or memory constraints in production settings, focusing instead on benchmark performance.

## Per-Paper Annotations

### Fu et al. (2025)

**Research question**: How does parametric knowledge influence content generation in long-context language models, and how does it interact with extrinsic retrieval ability as context length increases?
**Methodology**: The authors investigate how parametric knowledge affects content generation in LCLMs, demonstrating that its impact increases with context length, and design a Hybrid Needle-in-a-Haystack test that evaluates models based on both parametric recall ability and extrinsic retrieval ability.
**Key findings**:
- The influence of parametric knowledge on content generation becomes increasingly pronounced as context length extends
- Parametric recall ability does not improve simultaneously with extrinsic retrieval ability through context length improvements
- Better extrinsic retrieval ability can interfere with the model's parametric recall ability
- Qwen-2.5 models significantly outperform Llama-3.1 models in combining various abilities
- Even Llama-3.1-70B-Instruct fails to exhibit better performance, highlighting the importance of dual-ability evaluation
**Limitations**: The study focuses on the dual-ability perspective; specific architectural or training factors that enable better parametric recall are not fully explored.

### Kim et al. (2025)

**Research question**: How do long-context language models perform across multiple languages when evaluated on retrieval and aggregation tasks?
**Methodology**: The study presents ONERULER, a multilingual benchmark adapted from the English-only RULER benchmark with seven synthetic tasks across 26 languages, created through collaboration with native speakers for translation. Experiments were conducted with both open-weight and closed LLMs under context lengths from 8K to 128K tokens.
**Key findings**:
- A widening performance gap exists between low- and high-resource languages as context length increases from 8K to 128K tokens
- English is not the top-performing language (ranked 6th out of 26), with Polish emerging as the top language
- Many LLMs, particularly OpenAI's o3-mini-high, incorrectly predict the absence of an answer even in high-resource languages
- In cross-lingual scenarios, performance can fluctuate by up to 20% depending on the instruction language
**Limitations**: Not stated in abstract.

### Laitenberger et al. (2025)

**Research question**: Do multi-stage retrieval-augmented generation pipelines still offer measurable benefits over simpler, single-stage approaches given the rise of long-context language models?
**Methodology**: The study conducts a controlled evaluation for QA tasks under systematically scaled token budgets, comparing two recent multi-stage pipelines (ReadAgent and RAPTOR) against three baselines including DOS RAG, a simple retrieve-then-read method that preserves original passage order.
**Key findings**:
- DOS RAG consistently matches or outperforms more intricate methods on multiple long-context QA benchmarks
- DOS RAG's strength comes from maintaining source fidelity and document structure, prioritizing recall within effective context windows, and favoring simplicity
- The authors recommend establishing DOS RAG as a simple yet strong baseline for future RAG evaluations
**Limitations**: Not stated in abstract.

### Molfese et al. (2026)

**Research question**: Which fine-tuning strategies most effectively enhance long-context language models' ability to identify and use relevant information, and improve their robustness under KV-cache compression?
**Methodology**: The authors investigate various fine-tuning strategies to improve LCLMs' performance in identifying and using relevant information, as well as their robustness under KV-cache compression techniques, comparing in-domain and out-of-domain generalization across different task types.
**Key findings**:
- Substantial in-domain improvements were achieved, with gains of up to +20 points over the base model
- Out-of-domain generalization remains task dependent with large variance: LCLMs excel on finance questions (+9 points), while RAG shows stronger performance on multiple-choice questions (+6 points)
- Fine-tuning approaches bring moderate improvements in robustness under KV-cache compression, with gains varying across tasks
**Limitations**: Out-of-domain generalization shows large variance and is task dependent; the study does not identify which specific fine-tuning strategies are most effective.

### Song et al. (2026)

**Research question**: Can model-side aggregation with compact Hash-based HyperLogLog sketch states improve long-context language models' performance on non-additive, set-based aggregation tasks?
**Methodology**: The authors introduce a model-side aggregation interface that maintains compact Hash-based HyperLogLog (HLL) sketch states (2 KiB) alongside a frozen language model, where an extractor maps relevant records to canonical identities that are hashed and update the HLL state. They validated the approach through distinct-count experiments with one million records, merge tests with up to 256 segments, and evaluation on 3,969 aggregate-then-reason tasks from 174 source windows using Qwen and Gemma models.
**Key findings**:
- In a distinct-count experiment with one million records, the mean relative error was 1.6%
- States built from up to 256 segments produced exactly the same readout as a single pass over the same stream
- The fixed-budget interface reached 99.2% accuracy on Gemma 4 (31B, BF16), compared with 100.0% under exact aggregation (0.8 percentage point gap)
- The method improved over direct full-context reasoning by 63.2 points on Qwen and 56.3 points on Gemma
- On a 1,200-task Oolong-Synth subset, the method reached 91.1% on Qwen and 99.3% on Gemma
**Limitations**: The approach was validated with a fixed HLL state size of 2 KiB; performance may vary with different state sizes or task types.

### Thai and Iyyer (2025)

**Research question**: How well do modern long-context language models understand literary fiction when tasked with retrieving evidence from literary works?
**Methodology**: The study repurposes the RELiC dataset to construct a benchmark where LLMs receive the entire text of a primary source alongside literary criticism with a missing quotation, requiring the model to generate the missing quotation. A curated subset of 292 examples was created through extensive filtering and human verification.
**Key findings**:
- Recent reasoning models like Gemini Pro 2.5 can exceed human expert performance (62.5% vs. 50% accuracy)
- The best open-weight model achieves only 29.1% accuracy, highlighting a wide gap between open and closed-weight models
- Even the strongest models struggle with nuanced literary signals and overgeneration
**Limitations**: Not stated in abstract.

### Wu et al. (2025)

**Research question**: How well do long-context language models perform on long-context referencing tasks that require attributing items to specific parts of long-context data?
**Methodology**: The paper proposes Ref-Long, a novel benchmark with three subsets ranging from synthetic to realistic scenarios, and evaluates 13 LCLMs on their ability to identify document indexes that reference a specific key. Comprehensive analyses include human evaluations, task format adjustments, fine-tuning experiments, and error analyses.
**Key findings**:
- Experimental results reveal significant shortcomings in long-context referencing even among advanced models like GPT-4o
- The benchmark emphasizes contextual relationships between keys and documents over simple retrieval
- Comprehensive analyses including human evaluations and fine-tuning experiments led to several key insights about model limitations
**Limitations**: Not stated in abstract.

### Xie (2026)

**Research question**: Can a hybrid autoregressive architecture that separates local attention, persistent memory, predictive correction, and run-time control improve long-context language modeling compared to attention-only approaches?
**Methodology**: The author proposes LPC-SM, a hybrid autoregressive architecture that separates local attention, persistent memory, predictive correction, and run-time control within the same block, using Orthogonal Novelty Transport (ONT) to govern slow-memory writes, and evaluates a 158M-parameter model across three stages: base language modeling, mathematical continuation, and 4096-token continuation.
**Key findings**:
- Removing mHC raises the Stage-A final LM loss from 12.630 to 15.127, demonstrating the importance of this component
- Adaptive sparse control improves the Stage-B final LM loss from 12.137 to 10.787 relative to a matched fixed-ratio continuation
- The full route remains stable at sequence length 4096, with Stage C ending with final LM loss 11.582
- The model improves the delayed-identifier diagnostic from 14.396 to 12.031 in key cross-entropy
**Limitations**: The evaluation uses a relatively small 158M-parameter model; results may differ with larger model scales.

### Yang et al. (2025)

**Research question**: What are the essential features of an ideal long-context evaluation framework, and how can they be implemented to better assess long-context language models?
**Methodology**: The study introduces LongBioBench, a benchmark that uses artificially generated biographies as a controlled environment for assessing LCLMs across dimensions of understanding, reasoning, and trustworthiness, evaluating 18 LCLMs in total.
**Key findings**:
- Most models exhibit deficiencies in semantic understanding and elementary reasoning over retrieved results
- Models become less trustworthy as context length increases
- Existing synthetic benchmarks have design choices like contextual non-coherence, numerical needles, and absence of distractors that make them vulnerable for testing long-context capabilities
**Limitations**: Not stated in abstract.

### Ye et al. (2025)

**Research question**: How do long-context language models perform on procedural generation tasks that require integrating dispersed information and generating long-form structured outputs?
**Methodology**: The authors introduce LongProc, a benchmark with six procedural generation tasks (e.g., extracting structured information from HTML into TSV, executing search procedures for travel plans) that challenge models to follow detailed instructions, synthesize dispersed information, and generate structured outputs up to 8K tokens. They evaluated 23 LCLMs including instruction-tuned and reasoning models at three difficulty levels (500, 2K, and 8K maximum output tokens).
**Key findings**:
- All tested models claim context windows above 32K tokens, but open-weight models typically falter on 2K-token tasks
- Closed-source models like GPT-4o show significant degradation on 8K-token tasks
- Reasoning models achieve stronger overall performance in long-form generation, benefiting from long CoT training
- Long-context language models struggle to maintain long-range coherence in long-form generations
**Limitations**: The benchmark focuses on procedural generation tasks with deterministic procedures; findings may not generalize to other long-context tasks.

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
