# Systematic Literature Review: LLM-as-a-Judge Evaluation

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM judge", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-as-a-judge evaluation has rapidly evolved from initial demonstrations of feasibility to sophisticated investigations of reliability, calibration, and vulnerability. The 10 papers surveyed reveal a field grappling with fundamental questions about judge stability, statistical validity, and practical deployment. Recent work demonstrates that aggregate scores can mask substantial instability in individual verdicts, that LLM judges are susceptible to adversarial persuasion, and that proper statistical calibration is essential for trustworthy evaluation. At the same time, promising directions emerge in multi-agent judge design, uncertainty decomposition for efficient expert labeling, and self-prediction mechanisms for efficient inference. The collective literature emphasizes that LLM judges are not drop-in replacements for human evaluators but require careful validation, calibration, and understanding of their failure modes.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "LLM judge", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Judge Reliability and Stability

A central concern across multiple papers is whether LLM judges produce stable, repeatable verdicts. Yorke (2026) demonstrates that aggregate scores can remain stable while individual verdicts change substantially—rerunning the same setup changed win/tie/loss outcomes on 21.2% of prompts despite only ~1 point aggregate score movement. This instability compounds when instructions vary: removing reasoning requirements and other instructions changed outcomes on 28.2 percentage points more prompts than unchanged reruns. The practical implication is stark: evaluations relying on individual verdicts (e.g., for preference labels or per-response assessment) cannot trust aggregate stability as evidence of reliability.

This theme connects to work on human-LLM rater stability. Akarajaradwong et al. (2026) found that LLM judges systematically converge on majority human readings but fail to reproduce minority interpretations—zero of 26 LLM judges reproduced a minority human examiner's scoring pattern on contested Thai bar exam cells. The high LLM-panel agreement (α = 0.77) reflected systematic convergence rather than balanced reproduction of both valid readings. This asymmetry has profound implications for benchmark design: selecting LLM judges by maximizing agreement with human panels will inherit majority bias by construction.

### Theme 2: Statistical Calibration and Validity

The statistical foundations of LLM judge evaluation have received rigorous attention. Arawjo (2026) demonstrates that running statistics over raw LLM judge scores leads to inflated false positives, with risk paradoxically peaking at "almost perfect" human-LLM agreement. The evalstats package implements prediction-powered inference (PPI) with bootstrap-adaptive power tuning for small calibration sets, offering nine hypothesis tests including the first PPI corrections for rank-based tests. A key finding: bootstrap confidence intervals should be avoided for small-sample evaluations (N<100), and one demonstrated case showed a "substantially agreed" LLM judge would have led to publishing spurious findings without proper calibration.

Calibration extends to judge panels. Zhu et al. (2026) developed a finite-calibration regime map showing that scalar/reliability aggregation outperforms unrestricted joint-table calibration in 16 of 20 real dataset-budget cells. The practical question is whether the next judge's information is estimable under available human labels—when labels contain complex interactions, richer tables become viable, but finite support remains a bottleneck. This work provides deployment guidance: simpler aggregation often dominates unless human labels are sufficient to estimate high-order interactions.

### Theme 3: Adversarial Vulnerabilities

LLM judges exhibit surprising vulnerability to adversarial manipulation. Hwang et al. (2025) formalized seven persuasion techniques based on Aristotelian rhetoric (Majority, Consistency, Flattery, Reciprocity, Pity, Authority, Identity) and found they inflate scores for incorrect mathematical solutions by up to 8% on average. The Consistency technique caused the most severe distortion. Critically, increasing model size did not substantially mitigate vulnerability, combining techniques amplified bias, and effects persisted under counter-prompting. This reveals a fundamental weakness in LLM-as-a-Judge pipelines: where correctness should be independent of stylistic variation, persuasive language systematically biases evaluation.

### Theme 4: Multi-Agent and Adaptive Judge Design

Moving beyond single-judge architectures, recent work explores multi-agent systems for personalized judge design. Cao et al. (2025) proposed a dynamic multi-agent system that automatically designs personalized LLM judges by iteratively refining evaluation prompts. Their framework addresses two key limitations of existing approaches: inflexibility across text styles and poor alignment with human perception. Experimental results showed enhanced evaluation accuracy and better human alignment compared to existing methods. This represents a shift from static judge prompts to adaptive, task-specific judge synthesis.

Complementing this, Ashley et al. (2026) investigated self-prediction mechanisms where models predict how an LLM judge would score their output before responding. Larger reasoning models performed well in zero-shot prediction, while smaller models achieved up to 55% improvement with in-context report cards and 52% with supervised fine-tuning. This enables efficient inference: smaller models can defer to larger ones when anticipating poor performance, addressing the efficiency-quality trade-off in resource-constrained deployments.

### Theme 5: Domain-Specific Performance and Attribution

LLM judges show domain-dependent performance patterns that complicate blanket assessments. Abbas (2025) benchmarked LLM judges against Style Embeddings for authorship attribution across six domains. The LLM judge (GPT-4o) significantly outperformed embeddings in fiction and academic prose, indicating semantic sensitivity, but embeddings dominated in spoken transcripts and scripted dialogue, reflecting structural strengths. This multidimensional pattern highlights that attribution—and by extension, judgment quality—requires hybrid strategies rather than one-size-fits-all solutions.

Gera et al. (2024) emphasized that instance-based judge assessment overlooks system-level ranking factors like judge bias toward certain systems. Their large-scale study of LLM judges as system rankers argued for evaluating judges by comparing resulting system rankings to human rankings, not just aggregating per-instance judgments. This systems perspective reveals judge behaviors (decisiveness, bias patterns) invisible to instance-level analysis.

### Theme 6: Uncertainty Decomposition for Efficient Labeling

A promising direction for scaling evaluation is decomposing judge uncertainty to target expert labeling efficiently. Lail (2026) developed a Bayesian model separating aleatoric uncertainty (expert disagreement, which labels cannot reduce) from epistemic uncertainty (judge ignorance, which labels can reduce). On the ChaosNLI dataset, epistemic ranking removed 83% more error than total uncertainty for the same expert labels. This enables targeted expert intervention: escalate only where the judge is ignorant, not where experts genuinely disagree. The approach requires no sampling or additional judge calls—just regression on already-collected labels.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the conclusion that aggregate scores alone are insufficient for trustworthy evaluation. Yorke (2026), Arawjo (2026), and Gera et al. (2024) all emphasize the need for prompt-level agreement metrics, calibrated confidence intervals, and system-level ranking assessment respectively. There is also broad agreement that LLM judges require validation against human judgments, but that agreement metrics must be properly calibrated to avoid spurious conclusions (Arawjo, 2026; Akarajaradwong et al., 2026).

**Disagreements**: The literature reveals tension between complexity and simplicity in judge design. Cao et al. (2025) advocate for multi-agent adaptive systems, while Zhu et al. (2026) find simpler scalar/reliability aggregation often outperforms complex joint-table calibration. This may reflect different deployment contexts: adaptive design for diverse NLG applications versus calibrated panels for fixed benchmark evaluation. Similarly, Lail's (2026) uncertainty decomposition shows 83% improvement on ChaosNLI, but acknowledges that simply escalating least-labelled items performed similarly on real human disagreement data—suggesting the advantage may be dataset-dependent.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature:

1. **Generalizability across domains**: Multiple studies note limitations to specific domains (math benchmarks, Thai bar exams, six content domains). Systematic cross-domain comparison of judge reliability is lacking.

2. **Longitudinal stability**: All studies are cross-sectional. How do LLM judge verdicts change as models are updated? Yorke's (2026) use of a "pinned model version" acknowledges this issue but does not address temporal drift.

3. **Defense mechanisms**: While Hwang et al. (2025) document persuasion vulnerabilities and note counter-prompting fails, no paper presents robust defenses. This is a critical gap for practical deployment.

4. **Cost-benefit analysis**: Arawjo (2026) and Lail (2026) both require human-labeled calibration data, but none provide systematic cost-benefit analysis of calibration investment versus evaluation quality gains.

5. **Minority viewpoint preservation**: Akarajaradwong et al. (2026) document LLM judges' failure to reproduce minority human readings, but no paper proposes mechanisms to preserve legitimate interpretive diversity in evaluation.

6. **Interaction of vulnerabilities**: The literature treats instability, persuasion vulnerability, and statistical miscalibration as separate issues. Their interaction in real evaluation pipelines remains unexplored.

## Per-Paper Annotations

### Abbas (2025)

**Research question**: How do Style Embeddings and LLM judges compare in their ability to attribute authorship between human and AI-generated content?
**Methodology**: Benchmarked Style Embeddings and GPT-4o LLM judge on the Human AI Parallel Corpus (600 balanced instances across 6 domains), testing attribution accuracy on GPT-4o and LLaMA-70B-Instruct continuations.
**Key findings**:
- Style Embeddings achieve stronger aggregate accuracy on GPT continuations (82% vs 68%)
- LLM Judge slightly outperforms Style Embeddings on LLaMA continuations (85% vs 81%), though not statistically significant
- LLM judge significantly outperforms in fiction and academic prose, indicating semantic sensitivity
- Embeddings dominate in spoken transcripts and scripted dialogue, reflecting structural strengths
- Attribution is a multidimensional problem requiring hybrid strategies combining both approaches
**Limitations**: Limited to 6 domains and 2 LLM models; statistical significance not achieved for some comparisons; may not generalize to other models or content types.

### Akarajaradwong et al. (2026)

**Research question**: Is expert inter-rater stability a single ceiling number, and does LLM-judge agreement with that ceiling constitute evidence of judge stability?
**Methodology**: Three Bar Council-trained examiners and a 26-LLM judge panel scored the same 15 cross-graded answers from four inputs using an identical-inputs protocol, with an instrumented three-LLM anchor sub-panel conducting determinism probes, input ablations, and bootstrap confidence intervals.
**Key findings**:
- On 10 of 15 cells where the rubric prescribes both axes, all 29 raters converge in a tight band showing universal panel agreement
- On 5 cells where the rubric doesn't prescribe grading, the human panel splits between two coherent readings (B/C majority at upper band score 6-8; A minority at lower band score 1-2)
- 22 of 26 LLMs score in or near B/C's contested band, 4 sit in the regulation-silent middle gap, and only 1 (GPT-5.4 Nano) approaches A's band
- Zero LLMs in the 26-judge panel reproduce the minority human reading on the contested cells
- LLM-panel α = 0.77 reflects systematic convergence on the majority reading rather than balanced reproduction of both readings (human-panel α = 0.36)
**Limitations**: The study is limited to Thai bar examination free-form essays with only 15 answers from 4 inputs, which may not generalize to other legal domains or jurisdictions.

### Arawjo (2026)

**Research question**: How can researchers run reliable statistics over LLM judge scores with small-sample AI evaluations while avoiding inflated false positives?
**Methodology**: Developed prediction-powered inference (PPI) with bootstrap-adaptive power tuning for small calibration sets, conducted Monte Carlo simulations to derive recommendations for confidence intervals and hypothesis tests, and implemented these in the evalstats Python package.
**Key findings**:
- Running statistics over raw LLM judge scores leads to inflated false positives, with risk paradoxically peaking at "almost perfect" human-LLM agreement
- Nine hypothesis tests were implemented via PPI, including the first known PPI corrections for four rank-based tests (Wilcoxon signed-rank, Mann-Whitney U, and omnibus variants)
- Bootstrap-adaptive power tuning stabilizes PPI++ with small human-labeled calibration sets by shrinking estimated weight toward a target
- Bootstrap confidence intervals should be avoided for small-sample AI evaluations (N<100)
- A real LLM judge validated at "substantial agreement" would have led a researcher to publish a spurious finding without proper calibration
**Limitations**: The methodology focuses on small-sample evaluations (N<100) and requires human-labeled calibration data, which may be costly or impractical for some research contexts.

### Ashley et al. (2026)

**Research question**: Can models predict how an LLM judge would score their output prior to responding, enabling smaller models to defer to larger models when they anticipate poor performance?
**Methodology**: Investigated Predict-Answer/Act (PA) and Reason-Predict-Reason-Answer/Act (RPRA) paradigms, evaluating three approaches: zero-shot prediction, prediction using in-context report cards, and supervised fine-tuning across multiple datasets.
**Key findings**:
- Larger models, particularly reasoning models, perform well when predicting generic LLM judges in zero-shot settings
- Smaller models can reliably predict LLM judges after being fine-tuned or provided with in-context report cards
- Report cards achieve mean improvements of up to 55% in prediction accuracy across datasets
- Supervised fine-tuning achieves mean improvements of up to 52% in prediction accuracy across datasets
- Models can learn to predict their own performance limitations, enabling more efficient and self-aware AI systems
**Limitations**: The study focuses on prediction accuracy rather than measuring actual computational efficiency gains from deployment, and results are limited to specific model families and datasets tested.

### Cao et al. (2025)

**Research question**: How can we create flexible LLM judges that adapt to different text styles and produce evaluation scores that better align with human perception?
**Methodology**: Proposed a dynamic multi-agent system that automatically designs personalized LLM judges by iteratively refining evaluation prompts and balancing adaptive task requirements with alignment to human perception.
**Key findings**:
- Multi-agent LLM Judge framework enhances evaluation accuracy compared to existing methods
- Produces evaluation scores that better align with human perception
- Addresses flexibility limitations by adapting to different answer and ground truth styles
- Iteratively refines evaluation prompts to balance downstream task requirements with human alignment
**Limitations**: Abstract does not specify which NLG applications were tested or provide quantitative correlation metrics with human judgment; generalizability across diverse domains unclear.

### Gera et al. (2024)

**Research question**: How well do LLM judges perform at system-level ranking compared to instance-based assessment, and what factors affect their ranking quality?
**Methodology**: Conducted first large-scale study of LLM judges as system rankers, generating system scores by aggregating judgments over multiple outputs and comparing resulting rankings to human rankings while analyzing judge behavior including decisiveness and bias.
**Key findings**:
- Instance-based assessment overlooks critical factors affecting system-level ranking such as judge bias toward certain systems
- Judge quality should be assessed by comparing system rankings to human rankings rather than individual response evaluation
- Fine-grained characterization reveals judge behaviors including decisiveness and positive/negative bias toward certain systems
- System-level evaluation requires different validation approaches than instance-based assessment
**Limitations**: Abstract does not specify the scale of the study or which LLM judges were evaluated; correlation metrics with human rankings not provided.

### Hwang et al. (2025)

**Research question**: Can individuals persuade an LLM judge to assign unfairly high scores through strategically embedded persuasive language in mathematical reasoning tasks?
**Methodology**: Formalized seven persuasion techniques based on Aristotle's rhetorical principles (Majority, Consistency, Flattery, Reciprocity, Pity, Authority, Identity) and embedded them into otherwise identical responses across six math benchmarks to measure score inflation.
**Key findings**:
- Persuasive language leads LLM judges to assign inflated scores to incorrect solutions by up to 8% on average
- The Consistency technique causes the most severe distortion among the seven persuasion methods
- Increasing model size does not substantially mitigate this vulnerability to persuasion
- Combining multiple persuasion techniques amplifies the bias beyond individual techniques
- The persuasive effect persists even under counter-prompting strategies and affects pairwise evaluation
**Limitations**: The study focuses primarily on mathematical reasoning tasks where correctness should be independent of stylistic variation, which may not generalize to subjective evaluation domains.

### Lail (2026)

**Research question**: How can we separate aleatoric uncertainty (expert disagreement) from epistemic uncertainty (judge ignorance) to better target expert labeling efforts?
**Methodology**: Developed a small Bayesian model that separates uncertainty components using regression on already-collected labels, producing formulas for aleatoric and epistemic uncertainty without sampling or additional judge calls.
**Key findings**:
- Epistemic ranking removes 83% more error than total uncertainty for the same expert labels on ChaosNLI dataset
- Stated confidence is no guide to the judge's actual error
- Can estimate where a judge is ignorant rather than where experts genuinely disagree
- Simply escalating least-labelled items performs similarly on real human disagreement data
- Both uncertainty components can be isolated on a real LLM judge against exactly known truth
**Limitations**: Evaluated on specific datasets (ChaosNLI); the approach of escalating least-labelled items performed similarly in some cases, suggesting limited advantage in certain scenarios.

### Yorke (2026)

**Research question**: How repeatable are LLM judge verdicts and how much do they depend on the judge's instructions?
**Methodology**: Used 500 Arena-Hard v2.0 prompts with fixed model answers, ran GPT-4.1 as judge under all 8 combinations of criteria/output format/task framing, and repeated every setup unchanged at temperature zero on a pinned model version.
**Key findings**:
- Rerunning the default setup moves aggregate score by ~1 point but changes win/tie/loss outcome on 21.2% of prompts
- Instruction changes introduce further sensitivity: one setup removing reasoning and other instructions changed outcomes on 28.2 percentage points more prompts than unchanged reruns
- Stable aggregate scores do not establish that individual verdicts are repeatable
- Different instruction setups show varying sensitivity patterns (accuracy-prioritized criteria showed only 6.7 percentage points more changes)
**Limitations**: Study only used GPT-4.1 as the judge and Arena-Hard v2.0 prompts; results may not generalize to other judges or benchmark datasets.

### Zhu et al. (2026)

**Research question**: When should finite human labels support a low-dimensional stacker or reliability model versus an unrestricted joint output table for LLM judge panel calibration?
**Methodology**: Developed a finite-calibration regime map instantiated as Finite-Calibration Panel Selection (FCPS), testing across RewardBench, LLMBar, SummEval, and Arena100K with a seven-judge pool to compare scalar/reliability aggregation against unrestricted joint-table calibration.
**Key findings**:
- Scalar/reliability aggregation has lower MSE than unrestricted joint-table calibration in 16 of 20 real dataset-budget cells by point estimate
- Paired 95% intervals exclude zero in 11 cells, indicating statistically significant differences favoring simpler aggregation
- When labels contain a six-way interaction, the selected table grows to the interaction-bearing prefix and MSE falls from 0.224 to 0.061 once unseen mass vanishes
- Richer backoff/shrinkage tables narrow some gaps while preserving the finite-support bottleneck
- The practical deployment question is whether the next judge's information is estimable under the available human labels
**Limitations**: The study uses a seven-judge pool which may not generalize to larger or smaller panels, and results depend on specific dataset-budget combinations tested.

## References

Abbas, M. (2025). Attribution quality in AI-generated content: Benchmarking style embeddings and LLM judges. arXiv. https://arxiv.org/abs/2510.13898

Akarajaradwong, P., Lertprasertphakorn, W., Chaksangchaichot, C., & Nutanong, S. (2026). A two-phase stability study of LLM judges and Bar Council examiners on Thai bar-exam free-form essays. arXiv. https://arxiv.org/abs/2605.25652

Arawjo, I. (2026). How to run statistics over LLM judges and trust the results: Calibrated inference for small-sample AI evaluation with evalstats. arXiv. https://arxiv.org/abs/2609.35815

Ashley, D. R., Le Lan, G., Zhao, C., Dhingra, N., Cai, Z., Chang, E., Zhuge, M., Shi, Y., Chandra, V., & Schmidhuber, J. (2026). RPRA: Predicting an LLM-judge for efficient but performant inference. arXiv. https://arxiv.org/abs/2604.12634

Cao, H., Driouich, I., Singh, R., & Thomas, E. (2025). Multi-Agent LLM judge: Automatic personalized LLM judge design for evaluating natural language generation applications. arXiv. https://arxiv.org/abs/2504.02867

Gera, A., Boni, O., Perlitz, Y., Bar-Haim, R., Eden, L., & Yehudai, A. (2024). JuStRank: Benchmarking LLM judges for system ranking. arXiv. https://arxiv.org/abs/2412.09569

Hwang, Y., Lee, D., Kang, T., Kim, Y., & Jung, K. (2025). Can you trick the grader? Adversarial persuasion of LLM judges. arXiv. https://arxiv.org/abs/2508.07805

Lail, R. (2026). Decomposing LLM-judge uncertainty to target expert labels. arXiv. https://arxiv.org/abs/2609.06444

Yorke, L. (2026). Behind aggregate scores: What systematically varying Arena-Hard's LLM judge reveals. arXiv. https://arxiv.org/abs/2610.30512

Zhu, B., Xie, Y., & Rao, Y. (2026). A finite-calibration regime map for LLM judge panels. arXiv. https://arxiv.org/abs/2606.01034
