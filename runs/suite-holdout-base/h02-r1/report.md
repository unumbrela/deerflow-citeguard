# Systematic Literature Review: LLM-as-a-Judge Evaluation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "LLM judge", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-as-a-judge evaluation has evolved rapidly over the past two years, shifting from initial enthusiasm about automated evaluation toward critical examination of reliability, validity, and methodological rigor. The 10 surveyed papers collectively reveal that LLM judges exhibit substantial vulnerability to instruction variations, persuasive language, and systematic biases that aggregate scores often conceal. Recent work emphasizes the importance of calibrating judge panels, decomposing uncertainty types, applying proper statistical methods for small-sample evaluations, and recognizing asymmetric agreement patterns between LLM and human raters. The field is moving toward hybrid evaluation frameworks that combine LLM efficiency with human oversight, multi-agent personalization, and self-prediction paradigms for adaptive inference.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM judge", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reliability and Repeatability of LLM Judge Verdicts

A central concern across multiple papers is whether LLM judges produce stable, repeatable evaluations. Yorke (2026) demonstrates that similar aggregate scores can conceal substantial changes in individual verdicts—rerunning the same setup with GPT-4.1 as judge changed win/tie/loss outcomes on 21.2% of prompts despite aggregate scores moving only about one point. This finding challenges the assumption that stable aggregate scores indicate reliable judgment at the individual response level. The implications are significant for evaluations that rely on individual verdicts as preference labels or to assess specific responses, suggesting that researchers must report both aggregate scores and prompt-level agreement rates.

### Theme 2: Vulnerability to Adversarial Manipulation and Bias

LLM judges exhibit systematic vulnerabilities that threaten their validity as evaluation instruments. Hwang et al. (2025) reveal that persuasive language embedded in responses can bias LLM judges to assign inflated scores to incorrect mathematical solutions by up to 8% on average, with the Consistency technique causing the most severe distortion. Notably, increasing model size does not substantially mitigate this vulnerability, and combining multiple persuasion techniques amplifies the bias. Gera et al. (2024) further document that LLM judges exhibit positive or negative bias toward certain systems, which instance-based assessments overlook but which critically affect system-level rankings. These findings underscore that LLM judges are not immune to superficial stylistic features and systematic preferences that should be irrelevant to evaluation quality.

### Theme 3: Statistical Rigor in Small-Sample Evaluations

The statistical foundations of LLM judge-based evaluation have received increased scrutiny. Arawjo (2026) demonstrates that running statistics over raw LLM judge scores leads to inflated false positives, with false positive risk paradoxically peaking at "almost perfect" human-LLM agreement for many inter-rater metrics. The paper introduces prediction-powered inference (PPI) corrections for nine hypothesis tests, including rank-based tests like Wilcoxon signed-rank and Mann-Whitney U, and provides bootstrap-adaptive power tuning for small calibration sets. Monte Carlo simulations yield concrete recommendations for confidence intervals, p-values, and FWER corrections in small-sample evaluations (N<100), warning specifically against bootstrap CIs. This work addresses a critical gap: without well-calibrated statistical methods, significance claims based on LLM judge scores are unreliable.

### Theme 4: Calibration Strategies for Judge Panels

When deploying multiple LLM judges, the question of how to aggregate and calibrate their outputs becomes paramount. Zhu et al. (2026) study when finite human labels should support low-dimensional stacker or reliability models versus unrestricted joint output tables. Across RewardBench, LLMBar, SummEval, and Arena100K with a seven-judge pool, scalar/reliability aggregation achieves lower mean squared error than unrestricted joint-table calibration in 16 of 20 real dataset-budget cells. However, in controlled settings where labels contain higher-order interactions, joint tables eventually outperform simpler methods once sufficient data eliminates unseen mass. The practical guidance is that deployment decisions should hinge on whether the next judge's information is estimable under available human labels.

### Theme 5: Human-LLM Judge Agreement Asymmetry

The relationship between LLM judge outputs and human expert ratings is more complex than simple agreement metrics suggest. Akarajaradwong et al. (2026) test this on Thai bar exam essays, finding that on rubric-prescribed cells all 29 raters (3 human examiners and 26 LLMs) converge, but on rubric-ambiguous cells where humans split between two coherent readings, 22 of 26 LLMs cluster with the majority human reading while zero LLMs reproduce the minority reading. The LLM panel achieved α = 0.77 against human panel α = 0.36, but this high LLM agreement reflects systematic convergence on the majority reading rather than balanced reproduction of both legitimate interpretations. This asymmetry means benchmarks that select LLM judges by maximizing agreement with human reference panels will inherit this bias by construction.

### Theme 6: Adaptive and Personalized Judge Design

Recent work explores making LLM judges more flexible and aligned with human perception through adaptive architectures. Cao et al. (2025) propose a multi-agent system that automatically designs personalized LLM judges by iteratively refining evaluation prompts to balance task-specific requirements with human perception alignment. Their framework addresses two limitations of existing approaches: inflexibility across different text styles and low correlation with human judgment. Experimental results show enhanced evaluation accuracy and better human alignment compared to static judge configurations. Meanwhile, Ashley et al. (2026) investigate a different adaptive paradigm where models predict how an LLM judge would score their output before responding, enabling smaller models to defer to larger models when anticipating poor performance—achieving up to 55% improvement in prediction accuracy with in-context report cards.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that aggregate scores alone are insufficient for validating LLM judges—Yorke (2026), Arawjo (2026), and Akarajaradwong et al. (2026) all emphasize the need for finer-grained analysis of individual verdicts, calibrated confidence intervals, and examination of disagreement patterns. There is also consensus that LLM judges exhibit systematic biases: Hwang et al. (2025) show persuasion vulnerability, Gera et al. (2024) document system-level bias, and Akarajaradwong et al. (2026) reveal asymmetric convergence on majority human readings. Multiple papers converge on the need for hybrid approaches: Abbas (2025) finds LLM judges and style embeddings have complementary strengths across domains, Cao et al. (2025) advocate multi-agent personalization, and Lail (2026) proposes directing human expert labels to cases where the LLM judge is epistemically uncertain.

**Disagreements**: While most papers treat LLM judge limitations as problems to be solved through better methodology, there is implicit disagreement about whether LLM judges can ever fully replace human evaluation. Cao et al. (2025) and Ashley et al. (2026) present optimistic visions of automated or semi-automated evaluation, whereas Arawjo (2026) and Akarajaradwong et al. (2026) emphasize irreducible gaps between LLM and human judgment that require human oversight. Additionally, while Zhu et al. (2026) find simpler aggregation methods usually outperform complex joint-table calibration in real-world budget-constrained settings, their controlled experiments show the opposite when sufficient data is available—suggesting disagreement about whether current limitations are fundamental or merely data-constrained.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, most studies focus on English-language evaluation tasks, with only Akarajaradwong et al. (2026) examining non-English contexts (Thai bar exams)—the generalizability of findings to other languages and cultural contexts remains unexplored. Second, while multiple papers document vulnerabilities (persuasion attacks, instruction sensitivity, system bias), few propose and rigorously evaluate defense mechanisms—Hwang et al. (2025) note that counter-prompting strategies fail to eliminate persuasion effects, leaving a critical gap in practical mitigation approaches. Third, the computational overhead of sophisticated evaluation frameworks (multi-agent systems, uncertainty decomposition, calibrated statistical inference) is rarely quantified, making it difficult for practitioners to assess trade-offs between rigor and efficiency. Fourth, most studies examine LLM judges in isolation rather than as components of larger evaluation pipelines—the interaction between judge selection, prompt design, and aggregation methods warrants systematic investigation. Finally, the temporal stability of LLM judges remains unexamined: as models are updated and versions change, do previously validated judges maintain their calibration, or does evaluation require continuous re-validation?

## Per-Paper Annotations

### Akarajaradwong et al. (2026)

**Research question**: Is expert inter-rater stability a single ceiling number, and does LLM-judge agreement with that ceiling constitute evidence of judge stability?
**Methodology**: Used identical-inputs protocol where three Bar Council-trained examiners and a 26-LLM judge panel scored the same 15 cross-graded answers from four inputs (question, official grading regulation, gold answer, candidate answer), with an instrumented three-LLM anchor sub-panel for determinism probes, input ablations, and bootstrap CIs.
**Key findings**:
- On 10 of 15 cells where the rubric prescribes both axes, all 29 raters converge in a tight band with universal panel agreement
- On 5 rubric-ambiguous cells, humans split between two coherent readings while 22 of 26 LLMs cluster with the majority reading
- Zero LLMs reproduce the minority human reading on contested cells
- LLM-panel α = 0.77 reflects systematic convergence on majority reading rather than balanced reproduction of both readings; human-panel α = 0.36
- Benchmarks selecting LLM judges by maximizing agreement with human reference panels inherit this asymmetry by construction
**Limitations**: Study limited to Thai bar examination context with free-form legal essays; relatively small sample of 15 answers from 4 inputs may not generalize to other domains or evaluation contexts.

### Arawjo (2026)

**Research question**: How can researchers run reliable statistics over LLM judge scores with small-sample AI evaluations without producing inflated false positives?
**Methodology**: Developed guidance and tooling for statistical analysis of mixed human-AI judge designs, implementing nine hypothesis tests via prediction-powered inference (PPI) with bootstrap-adaptive power tuning for small calibration sets, validated through Monte Carlo simulations.
**Key findings**:
- Running statistics over raw LLM judge scores leads to inflated false positives, with false positive risk peaking at "almost perfect" human-LLM agreement for many inter-rater metrics
- Introduced bootstrap-adaptive power tuning to keep PPI++ stable with small human-labeled calibration sets by shrinking estimated weight toward a target and accounting for sampling variance
- Derived recommendations for CI, p-value, and FWER correction methods for small-sample evaluations (N<100), warning against bootstrap CIs
- Packaged recommendations into evalstats, an open-source Python package that automatically selects calibrated methods
- Demonstrated a real case where an LLM judge validated at "substantial agreement" would have led a researcher to publish a spurious finding
**Limitations**: Primarily addresses small-sample scenarios (N<100); requires human-labeled calibration data for prediction-powered inference corrections to function properly.

### Ashley et al. (2026)

**Research question**: Can models predict how an LLM judge would score their output prior to responding, enabling smaller models to defer to larger models when they anticipate poor performance?
**Methodology**: Investigated Predict-Answer/Act (PA) and Reason-Predict-Reason-Answer/Act (RPRA) paradigms where models predict LLM judge scores before responding, evaluating three approaches: zero-shot prediction, prediction using in-context report card, and supervised fine-tuning.
**Key findings**:
- Larger models, particularly reasoning models, perform well when predicting generic LLM judges in zero-shot settings
- Smaller models can reliably predict LLM judges after being fine-tuned or provided with an in-context report card
- Report cards achieve mean improvements of up to 55% across datasets for smaller model prediction accuracy
- Supervised fine-tuning achieves mean improvements of up to 52% across datasets for smaller model prediction accuracy
- Models can learn to predict their own performance limitations, paving the way for more efficient and self-aware AI systems that defer appropriately to larger models
**Limitations**: Focus is on prediction accuracy rather than measuring actual computational efficiency gains in real deployment scenarios; does not address the computational overhead of the prediction step itself.

### Cao et al. (2025)

**Research question**: How can we create flexible LLM judges that adapt to different text styles and produce evaluation scores aligned with human perception?
**Methodology**: Proposed a dynamic multi-agent system that automatically designs personalized LLM judges by iteratively refining evaluation prompts and balancing adaptive task requirements with human perception alignment.
**Key findings**:
- Existing LLM-as-a-judge frameworks lack flexibility to adapt to different text styles, reducing generalization performance
- Current frameworks produce evaluation scores that are skewed and show low correlation with human judgment
- Multi-agent system iteratively refines evaluation prompts to balance task requirements and human alignment
- Proposed framework enhances evaluation accuracy compared to existing methods
- Produces evaluation scores that better align with human perception
**Limitations**: Experimental validation limited to specific NLG applications; multi-agent system adds computational complexity; may require task-specific tuning.

### Gera et al. (2024)

**Research question**: How well do LLM judges perform at system-level ranking compared to human rankings, and what biases affect their judgments?
**Methodology**: Conducted first large-scale study of LLM judges as system rankers by aggregating judgment scores over multiple system outputs and comparing resulting rankings to human-based rankings, with fine-grained characterization of judge behavior.
**Key findings**:
- Instance-based assessment overlooks critical factors affecting system-level ranking, such as judge bias toward certain systems
- System scores generated by aggregating judgments can be compared to human rankings to assess judge quality
- Analysis provides fine-grained characterization of judge behavior including decisiveness and bias
- Judge's positive or negative bias towards certain systems affects ranking quality
- First large-scale study specifically focused on LLM judges as system rankers rather than instance evaluators
**Limitations**: Depends on availability of human-based rankings for comparison; may not generalize across all domains and model configurations; system-level bias characterization requires extensive evaluation data.

### Hwang et al. (2025)

**Research question**: Can individuals persuade an LLM judge to assign unfairly high scores through strategically embedded persuasive language in mathematical reasoning tasks?
**Methodology**: Formalized seven persuasion techniques based on Aristotle's rhetorical principles (Majority, Consistency, Flattery, Reciprocity, Pity, Authority, Identity) and embedded them into otherwise identical responses across six math benchmarks to measure score inflation.
**Key findings**:
- Persuasive language leads LLM judges to assign inflated scores to incorrect solutions by up to 8% on average
- Consistency technique causes the most severe distortion among all seven persuasion methods
- Increasing model size does not substantially mitigate this vulnerability
- Combining multiple persuasion techniques amplifies the bias beyond single-technique effects
- Pairwise evaluation is also susceptible, and the persuasive effect persists under counter prompting strategies
**Limitations**: Study focuses exclusively on mathematical reasoning tasks where correctness should be objective; does not extensively explore or validate defense mechanisms against persuasion-based attacks.

### Lail (2026)

**Research question**: How can we separate aleatoric uncertainty (real expert disagreement) from epistemic uncertainty (judge's ignorance) to better target expert labeling efforts?
**Methodology**: Developed a small Bayesian model that separates uncertainty components using regression on collected labels, producing both uncertainty types as simple formulas without sampling or additional judge calls.
**Key findings**:
- LLM judge's natural escalation signal conflates aleatoric uncertainty (real disagreement) and epistemic uncertainty (judge's ignorance)
- Both uncertainty components can be computed as simple formulas with no sampling or further judge calls
- On ChaosNLI human disagreement data, epistemic ranking removes 83% more error than total uncertainty for the same expert labels
- Simply escalating least-labelled items performs as well as epistemic ranking on real human disagreement
- Stated confidence is no guide to the judge's actual error
**Limitations**: Demonstrated on limited datasets (ChaosNLI); assumes Bayesian model assumptions hold; epistemic ranking advantage may not persist across all domains.

### Abbas (2025)

**Research question**: How well do Style Embeddings and LLM judges perform at attributing authorship in AI-generated content across different domains?
**Methodology**: Benchmarked Style Embeddings and instruction-tuned LLM judge (GPT-4o) on Human AI Parallel Corpus with 600 balanced instances spanning 6 domains (academic, news, fiction, blogs, spoken transcripts, TV/movie scripts).
**Key findings**:
- Style Embeddings achieve stronger aggregate accuracy on GPT continuations (82% vs 68%)
- LLM Judge slightly outperforms Style Embeddings on LLaMA continuations (85% vs 81%) but results are not statistically significant
- LLM judge significantly outperforms in fiction and academic prose, indicating semantic sensitivity
- Embeddings dominate in spoken and scripted dialogue, reflecting structural strengths
- Attribution is a multidimensional problem requiring hybrid strategies combining both approaches
**Limitations**: Limited to GPT-4o and LLaMA-70B-Instruct as generation models; some performance differences not statistically significant; domain coverage may not represent all content types.

### Yorke (2026)

**Research question**: How repeatable are LLM judge verdicts and how much do they depend on the judge's instructions?
**Methodology**: Used 500 Arena-Hard v2.0 prompts with fixed model answers, ran GPT-4.1 as judge under all 8 combinations of criteria/output format/task framing, and repeated every setup at temperature zero on a pinned model version.
**Key findings**:
- Similar aggregate scores can conceal substantial changes in individual verdicts when setups are repeated or instructions change
- Rerunning the default setup changes win/tie/loss outcomes on 21.2% of prompts despite aggregate score moving only ~1 point
- Instruction changes introduce further sensitivity: one setup removing reasoning and other instructions changed outcomes on 28.2 percentage points more prompts
- A stable aggregate score does not establish that individual verdicts are repeatable
- Evaluations relying on individual verdicts should repeat each setup and report both aggregate scores and prompt-level agreement
**Limitations**: Only tested with GPT-4.1 as judge on Arena-Hard v2.0 prompts; findings may not generalize to other judges or benchmarks.

### Zhu et al. (2026)

**Research question**: When should finite human labels support low-dimensional stacker/reliability models versus unrestricted joint output tables for LLM judge panel calibration?
**Methodology**: Cast the problem as a finite-calibration regime map instantiated as Finite-Calibration Panel Selection (FCPS), a validation selector over judge path, deployed panel size, and aggregator family with support diagnostics, tested across RewardBench, LLMBar, SummEval, and Arena100K with a seven-judge pool.
**Key findings**:
- Scalar/reliability aggregation has lower MSE than unrestricted joint-table calibration in 16 of 20 real dataset-budget cells by point estimate
- Paired 95% intervals exclude zero in 11 cells, indicating statistically significant differences favoring simpler aggregation
- Richer backoff/shrinkage tables narrow some gaps while preserving the finite-support bottleneck
- In controlled calibration-growth data with six-way interaction, the selected table grows to the interaction-bearing prefix and MSE falls from 0.224 to 0.061 once unseen mass vanishes
- The practical deployment question is whether the next judge's information is estimable under the available human labels
**Limitations**: Evaluated with a seven-judge pool which may not generalize to larger panels; finite-support bottleneck remains a fundamental constraint even with improved backoff/shrinkage methods.

## References

Akarajaradwong, P., Lertprasertphakorn, W., Chaksangchaichot, C., & Nutanong, S. (2026). A two-phase stability study of LLM judges and Bar Council examiners on Thai bar-exam free-form essays. arXiv. https://arxiv.org/abs/2605.25652

Arawjo, I. (2026). How to run statistics over LLM judges and trust the results: Calibrated inference for small-sample AI evaluation with evalstats. arXiv. https://arxiv.org/abs/2609.35815

Ashley, D. R., Le Lan, G., Zhao, C., Dhingra, N., Cai, Z., Chang, E., Zhuge, M., Shi, Y., Chandra, V., & Schmidhuber, J. (2026). RPRA: Predicting an LLM-judge for efficient but performant inference. arXiv. https://arxiv.org/abs/2604.12634

Abbas, M. (2025). Attribution quality in AI-generated content: Benchmarking style embeddings and LLM judges. arXiv. https://arxiv.org/abs/2510.13898

Cao, H., Driouich, I., Singh, R., & Thomas, E. (2025). Multi-Agent LLM judge: Automatic personalized LLM judge design for evaluating natural language generation applications. arXiv. https://arxiv.org/abs/2504.02867

Gera, A., Boni, O., Perlitz, Y., Bar-Haim, R., Eden, L., & Yehudai, A. (2024). JuStRank: Benchmarking LLM judges for system ranking. arXiv. https://arxiv.org/abs/2412.09569

Hwang, Y., Lee, D., Kang, T., Kim, Y., & Jung, K. (2025). Can you trick the grader? Adversarial persuasion of LLM judges. arXiv. https://arxiv.org/abs/2508.07805

Lail, R. (2026). Decomposing LLM-judge uncertainty to target expert labels. arXiv. https://arxiv.org/abs/2609.06444

Yorke, L. (2026). Behind aggregate scores: What systematically varying Arena-Hard's LLM judge reveals. arXiv. https://arxiv.org/abs/2610.30512

Zhu, B., Xie, Y., & Rao, Y. (2026). A finite-calibration regime map for LLM judge panels. arXiv. https://arxiv.org/abs/2606.01034
