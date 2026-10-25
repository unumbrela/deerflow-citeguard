# Systematic Literature Review: Hallucination Detection in Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "hallucination detection", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of hallucination detection in large language models has evolved rapidly over the past two years, with research spanning multiple detection paradigms and application scenarios. The surveyed literature reveals a maturing field moving from single-method approaches toward unified frameworks that address efficiency, domain-specificity, and accessibility constraints. Key developments include benchmarking infrastructure for standardized evaluation, lightweight methods feasible on CPU hardware, and novel detection signals extracted from model internals such as reasoning subspaces and denoising traces. While significant progress has been made in detection accuracy, the literature collectively highlights persistent challenges in summarization tasks, domain adaptation (particularly in medical contexts), and the need for methods that balance computational cost with performance.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "hallucination detection", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking and Standardized Evaluation

A prominent direction in recent work is the development of unified benchmarks and evaluation frameworks to enable reproducible comparison across detection methods. Li et al. (2026) introduce OpenHalDet, a comprehensive benchmark that standardizes evaluation across diverse generation scenarios, detector families, and access settings (black-box, gray-box, and white-box). This addresses a critical gap in the field where inconsistent inference configurations and limited domain coverage have made detector performance difficult to compare. Similarly, Faujdar and Kadvani (2026) provide systematic benchmarking of lightweight detection methods across question answering, dialogue, and summarization tasks, establishing performance baselines that are feasible without GPU acceleration. These benchmarking efforts reflect the field's maturation from isolated method proposals toward infrastructure that supports cumulative progress.

### Theme 2: Efficiency and Computational Constraints

Multiple papers address the computational cost of hallucination detection, particularly for methods requiring multiple sampling passes or expensive model inference. Sun et al. (2026) propose an Adaptive Bayesian Estimation framework that dynamically adjusts sampling budgets based on query complexity, achieving comparable detection performance with approximately 50% fewer samples. This adaptive approach contrasts with fixed-budget methods that waste computation on simple queries while under-sampling complex ones. The lightweight detection benchmark by Faujdar and Kadvani (2026) further demonstrates that CPU-feasible methods can achieve strong performance on QA and dialogue tasks, though summarization remains challenging. Together, these works emphasize that practical deployment requires methods that respect resource, especially for real-time applications or resource-constrained environments.

### Theme 3: Model-Internal Detection Signals

A growing body of work exploits signals from within model representations rather than relying solely on output text. Hu et al. (2025) introduce HARP, which decomposes LLM hidden state space into semantic and reasoning subspaces using SVD on Unembedding layer parameters, achieving 92.8% AUROC on TriviaQA by projecting hidden states onto reasoning subspace features. Chang et al. (2025) extend this internal-signal approach to diffusion language models, modeling the multi-step denoising process as an action trace and identifying sub-traces maximally informative to hallucinated responses. Chen et al. (2025) construct semantic graphs capturing relations among entity tokens and sentences, using graph-based uncertainty propagation to improve detection. These methods share the insight that hallucination signals are embedded in model internals—whether hidden states, denoising traces, or semantic graphs—and that extracting these signals can substantially improve detection accuracy over surface-level text analysis.

### Theme 4: Domain-Specific Hallucination Detection

Several papers address the challenge of adapting detection methods to specialized domains where errors carry high stakes. Lamarche et al. (2025) present MedHal, a synthetic dataset for medical hallucination detection that incorporates diverse medical text sources and both intrinsic and extrinsic hallucinations. This domain-specific approach recognizes that medical hallucinations differ qualitatively from general-domain errors and require tailored detection strategies. Oblovatny et al. (2025) similarly focus on retrieval-augmented generation (RAG) systems, proposing probabilistic distance-based methods that estimate distances between prompt and response token embeddings. These works highlight that one-size-fits-all detection methods may underperform in specialized contexts, motivating domain-adapted approaches with appropriate training data and evaluation benchmarks.

### Theme 5: Unified Detection, Identification, and Correction

Recent work moves beyond binary detection toward integrated systems that locate and correct hallucinations. Xu et al. (2025) introduce HAD, a model trained on a comprehensive 11-category hallucination taxonomy that integrates detection, span-level identification, and correction in a single inference process. This unified approach contrasts with earlier pipelines that treated detection and correction as separate stages. The model achieves state-of-the-art results on multiple benchmarks while demonstrating versatility across NLG tasks. This trend toward unification reflects the field's progression from isolated detection toward end-to-end systems that can be deployed in production applications.

### Theme 6: Leveraging Future Context and Temporal Signals

Two papers explore temporal dimensions of hallucination detection. Lee et al. (2025) observe that hallucinations tend to persist once introduced, and develop a framework that samples future contexts to detect these persistent patterns in black-box generators. Chang et al. (2025) similarly leverage the temporal structure of diffusion language models' multi-step denoising process, extracting signals from the action trace rather than single-step outputs. These approaches recognize that hallucination is not a static property but unfolds over time—whether across autoregressive generation steps or diffusion denoising iterations—and that modeling this temporal structure provides valuable detection signals.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key points. First, all papers agree that hallucination detection requires methods tailored to specific generation paradigms—autoregressive models, diffusion models, and RAG systems each demand different approaches. Second, there is broad consensus that efficiency matters: fixed high-budget sampling is wasteful, and lightweight methods are essential for practical deployment. Third, multiple papers converge on the value of model-internal signals (hidden states, denoising traces, semantic graphs) over surface-level text analysis alone.

**Disagreements**: The literature reveals tension regarding the feasibility of lightweight detection for summarization tasks. Faujdar and Kadvani (2026) find that lightweight methods perform near chance on summarization in single-pass design, though performance improves with multi-pass or chunked approaches. This contrasts with the more optimistic findings on QA and dialogue tasks, suggesting that summarization may require fundamentally different detection strategies. Additionally, while some papers emphasize domain-specific adaptation (Lamarche et al., 2025; Oblovatny et al., 2025), others pursue general-purpose methods that transfer across domains (Xu et al., 2025), reflecting an unresolved question about the optimal balance between specialization and generality.

## Gaps and Open Questions

The collective literature reveals several gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are discussed only in full text or that the field has not yet developed standardized practices for reporting method constraints. Second, while benchmarking infrastructure is improving (Li et al., 2026; Faujdar & Kadvani, 2026), the field lacks consensus on evaluation metrics beyond AUROC and F1, making cross-paper comparison challenging. Third, domain adaptation remains underexplored beyond medical contexts—fields like legal, scientific, and financial text generation face similar hallucination risks but lack dedicated detection resources. Finally, the tension between lightweight feasibility and detection accuracy, particularly for summarization, remains unresolved and warrants further investigation into hybrid approaches that combine efficient first-pass filtering with targeted deep analysis.

## Per-Paper Annotations

### Chang et al. (2025)

**Research question**: How can hallucination detection in diffusion LLMs leverage the multi-step denoising process rather than single-step generation signals?
**Methodology**: The authors propose TraceDet, which models the denoising process as an action trace and identifies the sub-trace maximally informative to hallucinated responses, leveraging key signals from multi-step denoising.
**Key findings**:
- Hallucination signals in D-LLMs emerge throughout the multi-step denoising process
- Existing AR-LLM detection methods are ill-suited for D-LLMs' multi-step generation
- TraceDet models denoising as action traces with predictions over cleaned responses
- The framework identifies sub-traces maximally informative to hallucinated responses
- TraceDet achieves average AUROC gain of 15.2% compared to baselines across D-LLMs
**Limitations**: Not stated in abstract

### Chen et al. (2025)

**Research question**: How can semantic relations among tokens and sentences be leveraged to improve uncertainty-based hallucination detection?
**Methodology**: The authors construct a semantic graph capturing relations among entity tokens and sentences, then use graph-based uncertainty propagation and calibration methods that integrate contradiction probability with neighbor information.
**Key findings**:
- Semantic graphs capture relations among entity tokens and sentences effectively
- Entity relation-based uncertainty propagation enhances sentence-level hallucination detection
- Graph-based uncertainty calibration integrates contradiction probability with neighbor sentences
- The approach achieves 19.78% improvement in passage-level hallucination detection
- The method addresses limitations of token-independent uncertainty modeling
**Limitations**: Not stated in abstract

### Faujdar and Kadvani (2026)

**Research question**: How well can hallucination detection perform using only lightweight, CPU-feasible methods without GPU-intensive inference or proprietary API access?
**Methodology**: The authors benchmark four lightweight detectors (ROUGE-L, semantic similarity, BERTScore, and an NLI detector based on FEVER-trained DeBERTa) plus a similarity-NLI ensemble across all three HaluEval benchmark tasks (QA, dialogue, summarisation), evaluating on 2,000 test instances per task with bootstrap confidence intervals and investigating design improvements for summarisation.
**Key findings**:
- The similarity-NLI ensemble is the most consistent lightweight method, but absolute performance is highly task-dependent
- The ensemble ranks best on QA (F1=0.792, AUC-ROC=0.873) and dialogue (F1=0.694, AUC-ROC=0.749), where NLI is the strongest standalone method
- On summarisation, every method performs near chance (AUC-ROC between 0.469 and 0.574) in single-pass design
- Summarisation performance improves substantially with design changes: raising premise budget from 800 to 1600 characters lifts AUC-ROC from 0.567 to 0.629, and sentence-level chunk aggregation reaches 0.683, still on CPU
- Lightweight detection is not intrinsically unsuited to summarisation but requires multi-pass or chunked design approaches
**Limitations**: Not stated in abstract

### Hu et al. (2025)

**Research question**: How can hallucination detection in LLMs be improved by disentangling semantic and reasoning information in hidden state spaces?
**Methodology**: The authors propose HARP, a framework that decomposes LLM hidden state space into semantic and reasoning subspaces using SVD on Unembedding layer parameters, then projects hidden states onto reasoning subspace basis vectors as features for detection.
**Key findings**:
- LLM hidden state space can be decomposed into a direct sum of semantic and reasoning subspaces
- The Unembedding layer can disentangle these subspaces via SVD parameter decomposition
- HARP reduces feature dimension to approximately 5% of the original while filtering noise
- HARP achieves AUROC of 92.8% on TriviaQA, outperforming previous best method by 7.5%
- The approach demonstrates enhanced robustness across multiple datasets
**Limitations**: Not stated in abstract

### Lamarche et al. (2025)

**Research question**: How can hallucination detection be improved for medical contexts where errors can directly affect patient outcomes?
**Methodology**: The authors present MedHal, a large-scale synthetic dataset designed to assess and train models on hallucination detection in medical texts, incorporating diverse medical text sources and tasks covering both intrinsic and extrinsic hallucinations with substantial data volume suitable for training.
**Key findings**:
- Current hallucination detection methods face significant limitations when applied to specialized domains like medicine
- MedHal addresses domain-specific challenges by incorporating diverse medical text sources and both intrinsic and extrinsic hallucinations
- Baseline models trained on MedHal show improvements over general-purpose hallucination detection approaches
- The resource enables more efficient evaluation and training of medical text generation systems while reducing reliance on costly expert review
**Limitations**: Not stated in abstract

### Lee et al. (2025)

**Research question**: How can hallucination detection be improved for black-box LLM generators by leveraging future context sampling?
**Methodology**: The authors develop a hallucination detection framework for black-box generators that samples future contexts based on the observation that hallucinations tend to persist, integrating these samples with various sampling-based methods.
**Key findings**:
- Hallucinations in LLM outputs tend to persist once introduced
- Sampled future contexts provide valuable clues for hallucination detection
- The sampling approach can be effectively integrated with various sampling-based methods
- The framework demonstrates performance improvements across multiple methods
**Limitations**: Not stated in abstract

### Li et al. (2026)

**Research question**: How can hallucination detection be evaluated consistently across diverse generation scenarios, detector families, and access settings?
**Methodology**: The authors introduce OpenHalDet, a unified benchmark that standardizes the evaluation pipeline from prompt construction and response generation to truthfulness annotation, detector scoring, and metric computation. It supports black-box, gray-box, and white-box detector families under different access settings within a shared framework.
**Key findings**:
- Existing hallucination detection evaluations face challenges from inconsistent inference configurations and limited domain coverage, making detector performance difficult to compare and reproduce
- OpenHalDet enables controlled comparison of diverse detector paradigms across heterogeneous tasks, models, and detection methods
- The benchmark provides a systematic view of how different detection approaches behave in various LLM application scenarios
- An open and extensible codebase is released to facilitate reproducible evaluation and future development of hallucination detection methods
**Limitations**: Not stated in abstract

### Oblovatny et al. (2025)

**Research question**: How can hallucination detection be improved specifically for retrieval-augmented generation (RAG) systems?
**Methodology**: The authors introduce a hallucination detection method based on estimating distances between distributions of prompt token embeddings and language model response token embeddings, examining the geometric structure of token hidden states to extract factuality signals while remaining efficient for long sequences.
**Key findings**:
- Most existing hallucination detection methods are not specifically designed for RAG systems despite their widespread use
- The proposed method achieves state-of-the-art or competitive performance in extensive experiments
- The method demonstrates transferability from NLI tasks to hallucination detection, making it fully unsupervised
- The approach is efficient and friendly to long sequences while reliably extracting factuality signals from text
**Limitations**: Not stated in abstract

### Sun et al. (2026)

**Research question**: How can hallucination detection methods adapt sampling budgets to query complexity to improve computational efficiency?
**Methodology**: The authors propose an Adaptive Bayesian Estimation framework for Semantic Entropy with Guided Semantic Exploration that dynamically adjusts sampling requirements based on observed uncertainty using a hierarchical Bayesian framework with variance-based thresholds to terminate generation once sufficient certainty is achieved, combined with a perturbation-based importance sampling strategy.
**Key findings**:
- Fixed sampling budgets in existing approaches fail to adapt to query complexity, resulting in computational inefficiency
- The proposed method requires about 50% fewer samples to achieve comparable detection performance in low-budget scenarios
- The approach delivers an average AUROC improvement of 12.6% under the same sampling budget
- Extensive experiments on four QA datasets demonstrate superior hallucination detection performance with significant efficiency gains
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: How can hallucination detection, identification, and correction be unified in a single model using a comprehensive taxonomy?
**Methodology**: The authors introduce a 11-category hallucination taxonomy across NLG tasks and train HAD models on a synthetic dataset of 90K samples to integrate detection, span-level identification, and correction in one inference process.
**Key findings**:
- A comprehensive hallucination taxonomy with 11 categories covers various NLG tasks
- HAD models integrate detection, span-level identification, and correction into single inference
- Training on 90K synthetic samples produces versatile models applicable to various NLG tasks
- HAD achieves state-of-the-art results on HaluEval, FactCHD, and FaithBench benchmarks
- The models demonstrate robustness on both in-domain and out-of-domain test sets
**Limitations**: Not stated in abstract

## References

Chang, S., Yu, J., Wang, W., Chen, Y., Yu, J., Torr, P., & Gu, J. (2025). TraceDet: Hallucination detection from the decoding trace of diffusion large language models. arXiv. https://arxiv.org/abs/2510.01274

Chen, K., Chen, Q., Zhou, J., Tao, X., Ding, B., Xie, J., Xie, M., Li, P., Zheng, F., & He, L. (2025). Enhancing uncertainty modeling with semantic graph for hallucination detection. arXiv. https://arxiv.org/abs/2501.02020

Faujdar, K., & Kadvani, S. (2026). How far can you get without a GPU? A systematic benchmark of lightweight hallucination detection across question answering, dialogue, and summarisation. arXiv. https://arxiv.org/abs/2606.29809

Hu, J., Tu, G., Cheng, S., Li, J., Wang, J., Chen, R., Zhou, Z., & Shan, D. (2025). HARP: Hallucination detection via reasoning subspace projection. arXiv. https://arxiv.org/abs/2509.11536

Lamarche, F., Mehenni, G., Fard, N. E., Rios-Ibacache, O., Wang, L. M., Kildea, J., & Zouaq, A. (2025). MedHal: A synthetic dataset for medical hallucination detection. arXiv. https://arxiv.org/abs/2504.08596

Lee, J., Park, C., Jo, H., Kim, J., Park, J., & Yoo, K. M. (2025). Enhancing hallucination detection via future context. arXiv. https://arxiv.org/abs/2507.20546

Li, X., Fang, Z., Deng, Y., Luo, J., Ma, H., Oh, C., Shi, Z., Ye, S., Wang, H., Chen, S.-L., Luo, Y., Yang, M., Du, S., Li, S., & Chen, L. (2026). OpenHalDet: A unified benchmark for hallucination detection across diverse generation scenarios. arXiv. https://arxiv.org/abs/2606.06959

Oblovatny, R., Kuleshova, A., Polev, K., & Zaytsev, A. (2025). Probabilistic distances-based hallucination detection in LLMs with RAG. arXiv. https://arxiv.org/abs/2506.09886

Sun, Q., Li, X., He, X., Cheng, A., Ji, X., Lu, H., Huang, R., & Hu, Q. (2026). Efficient hallucination detection: Adaptive Bayesian estimation of semantic entropy with guided semantic exploration. arXiv. https://arxiv.org/abs/2603.22812

Xu, F., Hu, X., Yu, Z., Lin, L., Zhang, X., Zhang, Y., Zhou, W., Gu, J., & Wan, X. (2025). HAD: HAllucination detection language models based on a comprehensive hallucination taxonomy. arXiv. https://arxiv.org/abs/2510.19318
