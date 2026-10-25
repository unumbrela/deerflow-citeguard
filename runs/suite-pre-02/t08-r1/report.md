# Systematic Literature Review: Chain-of-Thought Reasoning in Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "chain of thought", category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on chain-of-thought (CoT) reasoning in language models from 2024-2026 reveals a field maturing from initial demonstrations of capability toward deeper theoretical understanding and practical refinements. The surveyed papers collectively indicate that while CoT has proven effective for complex reasoning tasks, significant challenges remain in efficiency, robustness, and hallucination mitigation. Recent work has focused on three main directions: developing theoretical frameworks to explain why CoT works, proposing architectural innovations to address limitations like error accumulation and computational cost, and comparing CoT against alternative reasoning approaches. The field shows convergence on the view that long CoT enables more complex problem-solving than short CoT, though this comes with trade-offs in efficiency and potential for overthinking. Key open questions include how to balance reasoning depth with computational cost, how to verify CoT outputs reliably, and how to internalize reasoning capabilities rather than relying on explicit prompting.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "chain of thought", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Understanding of CoT Mechanisms

A significant thread in recent literature seeks to explain why CoT reasoning works rather than simply demonstrating that it works. Hu et al. (2024) introduce a novel framework grounded in the Hopfieldian view of cognition from neuroscience, conceptualizing CoT reasoning as movement between representation spaces. This theoretical perspective enables fine-grained control and error localization in reasoning processes. Complementing this, Yehudai et al. (2025) provide theoretical analysis comparing the expressive power of transformers with CoT against RNNs and standard transformers on compositional reasoning tasks, proving that each architecture requires different resources to solve the same problems. These theoretical works represent a shift from purely empirical demonstrations toward mechanistic understanding of CoT reasoning capabilities and limitations.

### Theme 2: Efficiency and Long CoT

As CoT methods have evolved toward longer reasoning chains, efficiency has emerged as a critical concern. Chen et al. (2025) provide a comprehensive survey distinguishing Long CoT from traditional Short CoT, identifying three key characteristics: deep reasoning, extensive exploration, and feasible reflection. Their survey highlights phenomena like "overthinking" and inference-time scaling as active areas of investigation. Addressing efficiency directly, Yang et al. (2024) propose Markov Chain of Thought (MCoT), which compresses previous reasoning steps into simplified questions, enabling longer reasoning paths without excessive KV cache dependency. The efficiency theme reflects growing recognition that naive scaling of CoT length is unsustainable, prompting development of more sophisticated approaches to maintain reasoning quality while reducing computational overhead.

### Theme 3: Novel CoT Architectures and Frameworks

Multiple papers propose architectural innovations to address specific CoT limitations. Cao et al. (2026) introduce DiffCoT, which reformulates CoT reasoning as an iterative denoising process inspired by diffusion models, enabling retrospective correction of intermediate reasoning steps to address error accumulation. Jin and Lu (2024) propose ECHO (Self-Harmonized Chain of Thought), which uses iterative refinement to harmonize automatically generated demonstrations into consistent reasoning patterns, addressing inconsistency in Auto-CoT approaches. Nguyen et al. (2025) present HoT (Highlighted Chain of Thought), which uses XML tags to ground facts to input-provided information, reducing hallucination rates. These architectural innovations demonstrate the field's movement beyond simple prompting toward structured frameworks that address specific failure modes.

### Theme 4: Architecture Comparisons and Alternatives

Several papers examine CoT in comparison to alternative approaches. Ren et al. (2024) analyze Mamba's capabilities for CoT reasoning, finding that while Mamba offers constant inference size advantages for some tasks, it struggles with COPY operations and shows limitations compared to transformers on CoT tasks unless its size scales with input length. Chen (2026) compares structured criteria extraction against CoT prompting for depression severity assessment, finding that criteria extraction does not consistently outperform CoT and may miss more severe cases. Yehudai et al. (2025) theoretically compare transformers with CoT, RNNs, and standard transformers, showing none is strictly superior for compositional reasoning. These comparative studies provide important context for understanding when CoT is the appropriate approach versus alternatives.

### Theme 5: Domain-Specific CoT Applications

CoT methods are being adapted for specific application domains with unique requirements. Yuen et al. (2024) address speech-to-speech conversational LLMs by internalizing ASR chain of thought implicitly into speech LLMs, reducing latency compared to traditional ASR-to-TTS pipelines. Chen (2026) examines CoT in the clinical context of depression severity assessment from social media posts, revealing limitations in both CoT and structured extraction approaches for detecting severe cases. These domain-specific applications highlight how CoT must be adapted to meet domain-specific constraints like latency requirements in speech processing or auditability needs in clinical assessment.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the view that Long CoT enables more complex problem-solving than Short CoT but introduces efficiency challenges (Chen et al., 2025; Yang et al., 2024). There is broad agreement that error accumulation and propagation are critical vulnerabilities in autoregressive CoT reasoning (Cao et al., 2026; Jin & Lu, 2024). Several papers independently identify the need for mechanisms to verify, correct, or ground CoT outputs (Hu et al., 2024; Nguyen et al., 2025; Chen, 2026). The surveyed literature also converges on the view that CoT is not universally superior—its effectiveness depends on task characteristics and alternative approaches may be preferable in specific contexts (Ren et al., 2024; Yehudai et al., 2025; Chen, 2026).

**Disagreements**: There is tension between papers proposing increasingly sophisticated CoT frameworks and those questioning whether explicit CoT is always necessary. While Cao et al. (2026) and Jin and Lu (2024) propose enhanced CoT frameworks, Chen (2026) finds that structured criteria extraction can match or exceed CoT performance in specific clinical assessment contexts when properly calibrated. The speech processing work by Yuen et al. (2024) suggests internalizing reasoning implicitly may be preferable to explicit CoT chains for latency-sensitive applications. Additionally, while Nguyen et al. (2025) present HoT as improving verifiability, they acknowledge the surprising finding that highlights can mislead users into trusting incorrect answers, raising questions about whether grounding mechanisms actually improve human oversight.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, while multiple papers propose efficiency improvements (Yang et al., 2024; Chen et al., 2025), there is limited work on principled methods for determining optimal reasoning depth for specific tasks—when should a model use Long CoT versus Short CoT? Second, verification and trustworthiness remain problematic: Nguyen et al. (2025) demonstrate that even fact-grounding mechanisms can mislead users, and Chen (2026) shows that structured approaches may miss critical cases despite better auditability. Third, domain adaptation is underexplored—most work focuses on mathematical and logical reasoning, with limited investigation of CoT in specialized domains requiring expert knowledge. Fourth, the theoretical work by Yehudai et al. (2025) and Ren et al. (2024) raises questions about when CoT is the appropriate architectural choice, but practical guidance for practitioners is lacking. Finally, several papers note limitations in evaluation scope, with most experiments limited to standard benchmarks rather than real-world deployment scenarios.

## Per-Paper Annotations

### Cao et al. (2026)

**Research question**: How can we address exposure bias and error accumulation in Chain-of-Thought reasoning where early mistakes propagate irreversibly through autoregressive decoding?
**Methodology**: The authors propose DiffCoT, a diffusion-styled CoT framework that reformulates CoT reasoning as an iterative denoising process with a sliding-window mechanism and causal diffusion noise schedule.
**Key findings**:
- DiffCoT enables unified generation and retrospective correction of intermediate reasoning steps
- The framework preserves token-level autoregression while allowing step-level corrections
- DiffCoT consistently outperforms existing CoT preference optimization methods across three benchmarks
- The approach yields improved robustness and error-correction capability in CoT reasoning
**Limitations**: The abstract does not explicitly acknowledge limitations; computational overhead of the iterative denoising process and applicability to non-mathematical reasoning tasks are not discussed.

### Chen (2026)

**Research question**: Does criteria extraction approach (marking clinical criteria then applying rules) outperform direct Chain-of-Thought prompting for LLM-based depression severity rating from social media posts?
**Methodology**: The author compares direct prompting, CoT, and criteria extraction approaches on two Reddit corpora using three LLMs (9B to frontier scale) and two questionnaires (PHQ-9, BDI-II), measuring agreement with quadratic weighted kappa under both fixed and recalibrated thresholds.
**Key findings**:
- Criteria extraction shows no significant gain over CoT when decision thresholds are fixed a priori from PHQ-9 criteria
- For frontier models, criteria extraction scores above CoT on one corpus only when thresholds are fitted on labeled data
- The 9B model behaves differently on depression community corpus, labeling most posts as severe regardless of prompting method
- PHQ-9 criteria extraction misses most severe posts, and moving from direct prompting to CoT to extraction increases misses
**Limitations**: The study is limited to Reddit corpora and specific questionnaires (PHQ-9, BDI-II); generalizability to clinical settings and other mental health assessment contexts remains untested.

### Chen et al. (2025)

**Research question**: What distinguishes Long Chain-of-Thought from traditional Short CoT and what are its key characteristics, phenomena, and research directions?
**Methodology**: The authors conduct a comprehensive survey offering a unified perspective on Long CoT, introducing a novel taxonomy to categorize current reasoning paradigms and exploring key characteristics, phenomena, and research gaps through systematic literature analysis.
**Key findings**:
- Long CoT is distinguished from Short CoT by three key characteristics: deep reasoning, extensive exploration, and feasible reflection
- Long CoT enables models to handle more complex tasks and produce more efficient, coherent outcomes compared to Short CoT
- Key phenomena include the emergence of overthinking and inference-time scaling in Long CoT
- Significant research gaps exist in multi-modal reasoning integration, efficiency improvements, and enhanced knowledge frameworks
**Limitations**: As a survey paper, it is limited by the scope of existing literature coverage; the rapidly evolving nature of the field means some recent developments may not be captured.

### Hu et al. (2024)

**Research question**: What are the fundamental factors behind Chain-of-Thought's success and how can we build a comprehensive framework to explain and understand CoT reasoning?
**Methodology**: The authors introduce a novel perspective grounded in the Hopfieldian view of cognition from cognitive neuroscience, establishing connections between CoT reasoning and cognitive elements such as stimuli, actions, neural populations, and representation spaces, and propose the Representation-of-Thought (RoT) framework.
**Key findings**:
- CoT reasoning can be understood as movement between representation spaces from the Hopfieldian view
- The RoT framework improves the robustness of the reasoning process in CoTs
- RoT enhances interpretability of CoT reasoning
- The approach offers fine-grained control over the reasoning process and enables localization of reasoning errors
**Limitations**: The abstract does not explicitly acknowledge limitations; experimental validation scope and generalizability beyond tested scenarios are not detailed.

### Jin and Lu (2024)

**Research question**: How can we address reasoning errors in Zero-shot-CoT and the labor-intensive manual demonstration requirements of Few-shot-CoT?
**Methodology**: The authors propose ECHO (Self-Harmonized Chain of Thought), which uses an iterative process to refine and harmonize automatically generated demonstrations into consistent reasoning patterns.
**Key findings**:
- ECHO unifies diverse solution paths into consistent and effective reasoning patterns
- The iterative refinement process mitigates inconsistent reasoning patterns from Auto-CoT's diversity
- ECHO outperforms Auto-CoT by an average of 2.8% across arithmetic, commonsense, and symbolic reasoning tasks
- The method reduces labor-intensive manual demonstration requirements while maintaining reasoning quality
**Limitations**: The improvement over Auto-CoT is modest at 2.8% average; the iterative harmonization process may add computational overhead; evaluation is limited to arithmetic, commonsense, and symbolic reasoning task categories.

### Nguyen et al. (2025)

**Research question**: How can we combat LLM hallucination and make it easier for humans to verify factual statements in LLM responses?
**Methodology**: The authors propose HoT (Highlighted Chain-of-Thought Prompting), which prompts LLMs to generate responses with XML tags that ground facts to those provided in the input question.
**Key findings**:
- HoT reduces hallucination rate compared to vanilla chain of thought prompting
- HoT improves LLM accuracy consistently across 22+ tasks including arithmetic, reading comprehension, and logical reasoning
- XML tag highlights help time-limited human verifiers more accurately and efficiently recognize when LLMs are correct
- When LLMs are wrong, HoT highlights tend to fool users into believing that answers are correct
**Limitations**: The highlighting can paradoxically mislead users into trusting incorrect answers when LLMs are wrong; effectiveness depends on LLMs properly formatting XML tags and the quality/completeness of facts provided in the input.

### Ren et al. (2024)

**Research question**: Can Mamba always bring computational savings while achieving performance comparable to Transformers?
**Methodology**: The authors analyze Mamba's expressive ability for COPY operations and Chain of Thought reasoning by drawing connections between Mamba and linear attention, and testing on Dynamic Programming problems.
**Key findings**:
- Constant-sized Mamba struggles to perform COPY operations while Transformers handle them more easily
- When Mamba's size grows linearly with input sequence length, it can accurately perform COPY but loses overhead savings
- For arbitrary Dynamic Programming problems, Mamba's total cost is comparable to standard Transformers
- Mamba can provide overhead savings for DP problems with favorable properties such as locality
**Limitations**: The analysis focuses on specific task types (COPY and CoT/DP problems) and may not generalize to all sequence modeling scenarios; theoretical analysis may not capture all practical deployment conditions.

### Yang et al. (2024)

**Research question**: How can we make long Chain-of-Thought reasoning more efficient while maintaining accuracy, given that excessive reasoning steps exceed token limits and increase computational demands?
**Methodology**: The authors conceptualize multi-step CoT as Markov Chain of Thought (MCoT) inspired by "derive, then reduce" human cognition logic, defining reasoning steps as text with Python code snippets, enabling self-correction through code interpreter interactions, and compressing previous steps into simplified questions.
**Key findings**:
- MCoT significantly enhances efficiency compared to standard long CoT
- MCoT maintains comparable accuracy to traditional CoT approaches
- The approach enables longer reasoning paths through self-correction via code interpreter interactions
- MCoT reduces dependency on lengthy KV cache by compressing previous reasoning steps
**Limitations**: The authors acknowledge that much remains to be explored; the approach is currently limited to mathematical reasoning tasks and requires code interpreter integration.

### Yehudai et al. (2025)

**Research question**: Is there always a single best architecture for a given task, specifically for Compositional Reasoning Questions?
**Methodology**: The authors compare the expressive power of transformers, RNNs, and transformers with CoT tokens on CRQ tasks, proving hardness results under standard assumptions and providing constructions for solving CRQs with each architecture.
**Key findings**:
- None of the three architectures can solve CRQs unless a hyperparameter grows with input size (under standard hardness assumptions)
- Transformers require depth logarithmic in problem size to solve CRQs
- RNNs need logarithmic embedding dimension (necessary and sufficient) when inputs are provided in a certain order
- Transformers with CoT require n CoT tokens for input size n; each architecture has different strengths and weaknesses
**Limitations**: Results are based on standard hardness assumptions that may not hold in all practical settings; RNNs require specific input ordering which is a significant constraint; theoretical results may not directly translate to empirical performance.

### Yuen et al. (2024)

**Research question**: How can speech-based LLMs handle direct speech-to-speech conversations more efficiently without relying on ASR-to-TTS pipelines?
**Methodology**: The authors propose a method that implicitly internalizes ASR chain of thought into a speech LLM to enhance native speech understanding capabilities, and release a large-scale synthetic conversational dataset for research.
**Key findings**:
- Current speech LLMs rely on ASR-to-TTS CoT pipelines that introduce latency and lose audio features
- Implicitly internalizing ASR CoT enhances the model's native speech understanding capabilities
- The approach reduces latency compared to traditional ASR-to-TTS pipeline approaches
- The method enables more efficient and natural real-time audio interactions
**Limitations**: The approach relies on synthetic data which may not fully capture real-world speech variations and acoustic conditions; effectiveness across diverse accents, languages, and noisy environments is not thoroughly explored.

## References

Cao, S., Lin, H., Gu, Y., Luo, Z., & Ma, J. (2026). DiffCoT: Diffusion-styled Chain-of-Thought Reasoning in LLMs. arXiv. https://arxiv.org/abs/2601.03559

Chen, Q., Qin, L., Liu, J., Peng, D., Guan, J., Wang, P., Hu, M., Zhou, Y., Gao, T., & Che, W. (2025). Towards reasoning era: A survey of long chain-of-thought for reasoning large language models. arXiv. https://arxiv.org/abs/2503.09567

Chen, X. (2026). Structure vs. Chain-of-Thought: Evaluating LLM criteria extraction for depression severity. arXiv. https://arxiv.org/abs/2609.39049

Hu, L., Liu, L., Yang, S., Chen, X., Tan, Z., Ali, M. A., Li, M., & Wang, D. (2024). Understanding reasoning in Chain-of-Thought from the Hopfieldian View. arXiv. https://arxiv.org/abs/2410.03595

Jin, Z., & Lu, W. (2024). Self-Harmonized Chain of Thought. arXiv. https://arxiv.org/abs/2409.04057

Nguyen, T., Bolton, L., Taesiri, M. R., Bui, T., & Nguyen, A. T. (2025). HoT: Highlighted Chain of Thought for Referencing Supporting Facts from Inputs. arXiv. https://arxiv.org/abs/2503.02003

Ren, R., Li, Z., & Liu, Y. (2024). Exploring the Limitations of Mamba in COPY and CoT Reasoning. arXiv. https://arxiv.org/abs/2410.03810

Yang, W., Liao, M., & Fan, K. (2024). Markov Chain of Thought for Efficient Mathematical Reasoning. arXiv. https://arxiv.org/abs/2410.17635

Yehudai, G., Amsel, N., & Bruna, J. (2025). Compositional Reasoning with Transformers, RNNs, and Chain of Thought. arXiv. https://arxiv.org/abs/2503.01544

Yuen, R. S.-H., Tse, T. T.-L., & Zhu, J. (2024). Internalizing ASR with Implicit Chain of Thought for Efficient Speech-to-Speech Conversational LLM. arXiv. https://arxiv.org/abs/2409.17353
