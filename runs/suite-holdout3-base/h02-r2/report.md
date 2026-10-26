# Systematic Literature Review: LLM-as-a-Judge Evaluation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "LLM judge", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Recent literature on LLM-as-a-judge evaluation reveals a field grappling with fundamental questions about reliability, validity, and methodological rigor. The 10 surveyed papers collectively demonstrate that while LLM judges offer scalable evaluation capabilities, their verdicts exhibit substantial sensitivity to instruction variations, persuasive language, and calibration choices. A recurring theme is the distinction between aggregate score stability and individual verdict repeatability—multiple papers show that stable aggregate scores can mask significant prompt-level variability. The literature converges on the need for calibrated statistical methods, transparent reporting of judge configurations, and hybrid approaches that combine LLM judges with targeted human expert labeling. Critical gaps remain in understanding cross-domain generalization, developing robust defenses against adversarial manipulation, and establishing standardized benchmarks for judge panel deployment.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM judge", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Repeatability and Instruction Sensitivity

A central concern across multiple papers is the repeatability of LLM judge verdicts and their sensitivity to instruction variations. Yorke (2026) demonstrates that rerunning the same judge setup at temperature zero changes win/tie/loss outcomes on 21.2% of prompts despite aggregate scores moving only about one point. Instruction changes introduce even greater sensitivity—dropping reasoning requirements and other instructions shifts outcomes on 28.2 percentage points more prompts than unchanged reruns. This finding echoes through the literature: stable aggregate scores do not establish that individual verdicts are repeatable, a distinction critical when verdicts serve as preference labels or assess individual responses. The practical implication is that evaluations relying on individual verdicts must repeat each setup and report both aggregate scores and prompt-level agreement.

### Theme 2: Statistical Calibration and Inference

Several papers address the statistical challenges of drawing reliable conclusions from LLM judge evaluations. Arawjo (2026) finds that running statistics over raw LLM judge scores leads to inflated false positives, with false positive risk paradoxically peaking at "almost perfect" human-LLM agreement for many inter-rater metrics. The paper introduces prediction-powered inference (PPI) corrections for nine hypothesis tests, including the first known PPI corrections for rank-based tests like Wilcoxon signed-rank and Mann-Whitney U. Bootstrap confidence intervals are explicitly discouraged for small-sample evaluations (N<100). The evalstats package implements these recommendations, automatically selecting calibrated methods. This work responds to a broader pattern in the literature where researchers base significance claims on LLM judge scores without well-calibrated confidence intervals or judge-bias corrections.

### Theme 3: Judge Panel Calibration and Aggregation

When deploying multiple LLM judges as a panel, the choice of calibration strategy significantly impacts performance. Zhu et al. (2026) study when finite human labels should support low-dimensional stacker or reliability models versus unrestricted joint output tables. Their Finite-Calibration Panel Selection (FCPS) framework shows that scalar/reliability aggregation achieves lower mean squared error than unrestricted joint-table calibration in 16 of 20 real dataset-budget cells across RewardBench, LLMBar, SummEval, and Arena100K. The practical deployment question becomes whether the next judge's information is estimable under available human labels. Richer backoff/shrinkage tables narrow some gaps while preserving the finite-support bottleneck, but controlled calibration-growth data show that when labels contain complex interactions, unrestricted tables eventually outperform once unseen mass vanishes.

### Theme 4: Adversarial Vulnerabilities and Robustness

LLM judges exhibit systematic vulnerabilities to adversarial persuasion, raising concerns about their deployment in high-stakes evaluation contexts. Hwang et al. (2025) demonstrate that strategically embedded persuasive language based on Aristotle's rhetorical principles can bias LLM judges when scoring mathematical reasoning tasks, where correctness should be independent of stylistic variation. Across six math benchmarks, persuasive language leads to inflated scores for incorrect solutions by up to 8% on average, with the Consistency technique causing the most severe distortion. Increasing model size does not substantially mitigate this vulnerability, and combining multiple persuasion techniques amplifies the bias. The persuasive effect persists even under counter prompting strategies, highlighting a critical vulnerability in LLM-as-a-Judge pipelines that demands robust defenses against persuasion-based attacks.

### Theme 5: Human-LLM Judge Agreement and Asymmetry

The relationship between LLM judge agreement and human expert agreement is more complex than treating inter-rater stability as a single ceiling number. Akarajaradwong et al. (2026) test this assumption on Thai bar examination essays, finding asymmetric patterns: on 10 of 15 cells where the rubric prescribes both grading axes, all 29 raters (3 human examiners and 26 LLMs) converge in a tight band. However, on the remaining 5 cells where the rubric does not prescribe grading approach, the human panel splits between two coherent readings while 22 of 26 LLMs converge on the majority human reading. Zero LLMs reproduce the minority human reading on contested cells. The high LLM-panel agreement (α=0.77) reflects systematic convergence on the majority reading rather than balanced reproduction of both readings—a benchmark selecting LLM judges by maximizing agreement with human reference panels will inherit this asymmetry by construction.

### Theme 6: Specialized Judge Applications and Extensions

Beyond core evaluation methodology, several papers explore specialized applications and extensions of LLM judges. Abbas (2025) benchmarks LLM judges against Style Embeddings for authorship attribution in AI-generated content, finding the LLM judge (GPT-4o) significantly outperforms in fiction and academic prose while embeddings dominate in spoken and scripted dialogue. Cao et al. (2025) propose a multi-agent system that automatically designs personalized LLM judges for various natural language generation applications, iteratively refining evaluation prompts to balance task adaptation with human perception alignment. Ashley et al. (2026) investigate models predicting how an LLM judge would score their output prior to responding, enabling smaller models to defer to larger models when they predict poor performance—achieving up to 55% improvement in prediction accuracy with in-context report cards.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that aggregate score stability does not guarantee individual verdict repeatability (Yorke, 2026; Arawjo, 2026). The literature also agrees that LLM judges require calibration against human labels, but the optimal calibration strategy depends on available label budget (Zhu et al., 2026; Arawjo, 2026). There is broad consensus that LLM judges exhibit systematic biases—whether from instruction sensitivity, persuasive language, or asymmetry in reproducing human disagreement patterns—that must be explicitly measured and reported rather than assumed away.

**Disagreements**: The literature shows tension between approaches that seek to improve LLM judges through better calibration and aggregation (Zhu et al., 2026; Arawjo, 2026) versus those that propose hybrid systems combining LLM judges with complementary methods like Style Embeddings (Abbas, 2025) or targeted expert labeling guided by uncertainty decomposition (Lail, 2026). While multi-agent approaches promise automatic judge design with better human alignment (Cao et al., 2025), the computational cost and complexity of such systems remains unaddressed compared to simpler single-judge approaches with proper statistical calibration.

## Gaps and Open Questions

The collective literature identifies several critical gaps:

1. **Cross-domain generalization**: Most studies focus on specific domains (math reasoning, legal essays, Arena-Hard prompts), leaving open whether findings about judge sensitivity, calibration strategies, and adversarial vulnerabilities generalize across evaluation contexts.

2. **Defense mechanisms**: While adversarial persuasion vulnerabilities are documented (Hwang et al., 2025), robust defenses against persuasion-based attacks remain underdeveloped.

3. **Computational efficiency**: Multi-agent judge design (Cao et al., 2025) and panel calibration (Zhu et al., 2026) approaches lack analysis of computational costs and practical deployment trade-offs.

4. **Longitudinal stability**: All studies capture judges at a single point in time; whether judge behavior drifts across model updates or deployment contexts is unexamined.

5. **Minority viewpoint reproduction**: The asymmetry in reproducing human disagreement patterns (Akarajaradwong et al., 2026) raises questions about whether benchmarks selecting for majority agreement systematically exclude valid minority perspectives in evaluation.

## Per-Paper Annotations

### Abbas (2025)

**Research question**: How well do Style Embeddings and LLM judges perform at attributing authorship in AI-generated content across different domains?
**Methodology**: Benchmarked fixed Style Embeddings and instruction-tuned GPT-4o judge on the Human AI Parallel Corpus (600 balanced instances across six domains), where each instance contains a human prompt with both gold and LLM-generated continuations from GPT-4o or LLaMA-70B-Instruct.
**Key findings**:
- Style Embeddings achieve stronger aggregate accuracy on GPT continuations (82% vs 68%)
- LLM Judge is slightly better than Style Embeddings on LLaMA continuations (85% vs 81%), though not statistically significant
- LLM judge significantly outperforms in fiction and academic prose, indicating semantic sensitivity
- Style embeddings dominate in spoken and scripted dialogue, reflecting structural strengths
- Attribution is a multidimensional problem requiring hybrid strategies combining both approaches
**Limitations**: Limited to two attribution mechanisms and two LLM sources across six domains; some results lack statistical significance; may not generalize to other models or attribution scenarios.

### Akarajaradwong et al. (2026)

**Research question**: Do expert inter-rater stability assumptions hold when comparing LLM judges to human bar examiners on free-form legal essay evaluation?
**Methodology**: Used identical-inputs protocol where three Bar Council-trained examiners and a 26-LLM judge panel scored the same 15 cross-graded answers from four inputs; instrumented three-LLM anchor sub-panel with determinism probes, input ablations, and bootstrap CIs.
**Key findings**:
- On 10 of 15 cells where rubric prescribes both axes, all 29 raters converge in a tight band with universal panel agreement
- On 5 cells where rubric doesn't prescribe grading approach, human panel splits between two coherent readings (B/C majority at upper band score 6-8; A minority at lower band score 1-2)
- 22 of 26 LLMs score in or near B/C's contested band, 4 sit in middle gap, and only 1 (GPT-5.4 Nano) approaches A's band
- Zero LLMs reproduce the minority human reading on contested cells
- LLM-panel α=0.77 reflects systematic convergence on majority reading rather than balanced reproduction of both readings (human-panel α=0.36)
**Limitations**: Study limited to 15 cells from Thai bar examination; findings may not generalize to other legal domains, jurisdictions, or non-legal evaluation contexts.

### Arawjo (2026)

**Research question**: How can researchers run reliable statistics over LLM judge scores with small-sample AI evaluations without inflated false positives?
**Methodology**: Developed guidance and tooling for statistical analysis of mixed human-AI judge designs, implemented nine hypothesis tests via prediction-powered inference (PPI) including four rank-based tests, introduced bootstrap-adaptive power tuning, and conducted Monte Carlo simulations to derive recommendations.
**Key findings**:
- Running statistics over raw LLM judge scores leads to inflated false positives
- False positive risk paradoxically peaks at "almost perfect" human-LLM agreement for many inter-rater agreement metrics
- Bootstrap confidence intervals should be avoided for small-sample AI evaluations (N<100)
- Created evalstats package that automatically selects calibrated methods for small-sample evaluations
- Demonstrated a real case where an LLM judge validated at "substantial agreement" would have led to publishing a spurious finding
**Limitations**: Recommendations specifically target small-sample evaluations (N<100) and may not generalize to larger sample sizes; the evalstats package requires human-labeled calibration sets.

### Ashley et al. (2026)

**Research question**: Can models predict how an LLM judge would score their output prior to responding, enabling efficient inference by deferring to larger models when needed?
**Methodology**: Investigated Predict-Answer/Act (PA) and Reason-Predict-Reason-Answer/Act (RPRA) paradigms where models predict LLM judge scores before responding; evaluated three approaches: zero-shot prediction, prediction using in-context report card, and supervised fine-tuning.
**Key findings**:
- Larger models, particularly reasoning models, perform well when predicting generic LLM judges zero-shot
- Smaller models can reliably predict LLM judges after being fine-tuned or provided with an in-context report card
- Report cards achieve mean improvements of up to 55% across datasets for smaller models
- Fine-tuning achieves mean improvements of up to 52% across datasets for smaller models
- Models can learn to predict their own performance limitations, enabling more efficient and self-aware AI systems
**Limitations**: Focus on prediction accuracy rather than end-to-end system efficiency gains from model deferral; evaluation limited to specific judge types and datasets.

### Cao et al. (2025)

**Research question**: Can a dynamic multi-agent system automatically design personalized LLM judges that adapt to different text styles and produce evaluation scores aligned with human perception?
**Methodology**: Proposes a novel dynamic multi-agent system that iteratively refines evaluation prompts and balances the trade-off between adaptive requirements of downstream tasks and alignment with human perception.
**Key findings**:
- The multi-agent LLM Judge framework enhances evaluation accuracy compared to existing methods
- The system produces evaluation scores that better align with human perception
- The approach addresses flexibility limitations of existing frameworks across different answer and ground truth styles
- Iterative prompt refinement improves generalization performance across text styles
- The system reduces score skewness and improves interpretability compared to existing LLM-as-a-judge frameworks
**Limitations**: Experimental details and specific benchmarks not fully described in abstract; computational cost of multi-agent iterative refinement not discussed; may require significant resources for automatic judge design.

### Gera et al. (2024)

**Research question**: How well do LLM judges perform at system-level ranking compared to human-based rankings, and what factors like bias and decisiveness affect their quality?
**Methodology**: Conducts the first large-scale study of LLM judges as system rankers by aggregating judgment scores over multiple system outputs and comparing resulting system rankings to human-based rankings, with fine-grained characterization of judge behavior including decisiveness and bias.
**Key findings**:
- Instance-based assessment overlooks critical factors affecting system-level ranking such as judge bias toward certain systems
- System-level evaluation requires aggregating scores across multiple outputs rather than individual response assessment
- LLM judges exhibit positive or negative bias toward certain systems that affects ranking quality
- Judge quality assessment should compare system rankings to human-based rankings rather than individual judgments
- Fine-grained characterization of judge behavior including decisiveness and bias provides deeper understanding of judge quality
**Limitations**: Abstract does not specify specific quantitative results or which judges were tested; system-level ranking may still be affected by aggregation method choices; human-based rankings used as ground truth may themselves have variability.

### Hwang et al. (2025)

**Research question**: Can individuals persuade LLM judges to assign unfairly high scores through strategically embedded persuasive language in mathematical reasoning tasks?
**Methodology**: Formalized seven persuasion techniques based on Aristotle's rhetorical principles (Majority, Consistency, Flattery, Reciprocity, Pity, Authority, Identity) and embedded them into otherwise identical responses, testing across six math benchmarks.
**Key findings**:
- Persuasive language leads LLM judges to assign inflated scores to incorrect solutions by up to 8% on average
- Consistency technique causes the most severe distortion among the seven persuasion methods
- Increasing model size does not substantially mitigate this vulnerability
- Combining multiple persuasion techniques amplifies the bias beyond individual techniques
- The persuasive effect persists even under counter prompting strategies
**Limitations**: Study focuses specifically on mathematical reasoning tasks where correctness should be independent of stylistic variation; does not extensively explore defense mechanisms against persuasion-based attacks.

### Lail (2026)

**Research question**: How can we separate aleatoric uncertainty (real expert disagreement) from epistemic uncertainty (judge ignorance) to better target expert labeling efforts?
**Methodology**: Uses a small Bayesian model that separates uncertainty components through regression on already-collected labels, producing both aleatoric and epistemic estimates as simple formulas without sampling or additional judge calls.
**Key findings**:
- The Bayesian decomposition isolates uncertainty components on a real LLM judge against exactly known truth
- Stated confidence is no guide to the judge's actual error
- On real human disagreement (ChaosNLI), epistemic ranking removes 83% more error than total uncertainty for the same expert labels
- Simply escalating the least-labelled items performs as well as epistemic ranking on ChaosNLI
- The approach can estimate where a judge is ignorant rather than where experts genuinely disagree
**Limitations**: Demonstrated on a small Bayesian model with limited datasets; effectiveness of epistemic ranking over simple least-labelled escalation varies by dataset; generalizability to other judge models and domains needs further validation.

### Yorke (2026)

**Research question**: How repeatable are LLM judge verdicts and how much do they depend on the judge's instructions?
**Methodology**: Used 500 Arena-Hard v2.0 prompts with two models' answers held fixed, ran GPT-4.1 as judge under all eight combinations of criteria, output format and task framing, and repeated every setup unchanged at temperature zero on a pinned model version.
**Key findings**:
- Rerunning the default setup moves the aggregate score by about one point but changes the win/tie/loss outcome on 21.2% of prompts
- Instruction changes introduce further sensitivity: dropping reasoning and other instructions changes outcomes on 28.2 percentage points more prompts than unchanged reruns
- When criteria prioritize accuracy, outcomes change on 6.7 percentage points more prompts while the aggregate score barely moves
- A stable aggregate score does not establish that individual verdicts are repeatable
- Evaluations relying on individual verdicts should repeat each setup and report both aggregate scores and prompt-level agreement
**Limitations**: Study uses only GPT-4.1 as judge and is limited to Arena-Hard v2.0 prompts; findings may not generalize to other judges, datasets, or evaluation contexts.

### Zhu et al. (2026)

**Research question**: When should finite human labels support low-dimensional stacker/reliability models versus unrestricted joint output tables for LLM judge panel calibration?
**Methodology**: Cast the problem as a finite-calibration regime map instantiated as Finite-Calibration Panel Selection (FCPS), a validation selector over judge path, deployed panel size, and aggregator family; tested across RewardBench, LLMBar, SummEval, and Arena100K with a seven-judge pool.
**Key findings**:
- Scalar/reliability aggregation has lower MSE than unrestricted joint-table calibration in 16 of 20 real dataset-budget cells by point estimate
- Paired 95% intervals exclude zero in 11 cells, indicating statistically significant differences
- Richer backoff/shrinkage tables narrow some gaps while preserving the finite-support bottleneck
- In controlled calibration-growth data with six-way interactions, selected table MSE falls from 0.204 to 0.061 once unseen mass vanishes
- The practical deployment question is whether the next judge's information is estimable under available human labels
**Limitations**: Seven-judge pool may not represent all deployment scenarios; controlled calibration-growth data showing opposite regime may not reflect typical real-world conditions.

## References

Abbas, M. (2025). Attribution quality in AI-generated content: Benchmarking style embeddings and LLM judges. arXiv. https://arxiv.org/abs/2510.13898

Akarajaradwong, P., Lertprasertphakorn, W., Chaksangchaichot, C., & Nutanong, S. (2026). A two-phase stability study of LLM judges and Bar Council examiners on Thai bar-exam free-form essays. arXiv. https://arxiv.org/abs/2605.25652

Arawjo, I. (2026). How to run statistics over LLM judges and trust the results: Calibrated inference for small-sample AI evaluation with evalstats. arXiv. https://arxiv.org/abs/2609.35815

Ashley, D. R., Le Lan, G., Zhao, C., Dhingra, N., Cai, Z., Chang, E., Zhuge, M., Shi, Y., Chandra, V., & Schmidhuber, J. (2026). RPRA: Predicting an LLM-Judge for efficient but performant inference. arXiv. https://arxiv.org/abs/2604.12634

Cao, H., Driouich, I., Singh, R., & Thomas, E. (2025). Multi-Agent LLM Judge: Automatic personalized LLM judge design for evaluating natural language generation applications. arXiv. https://arxiv.org/abs/2504.02867

Gera, A., Boni, O., Perlitz, Y., Bar-Haim, R., Eden, L., & Yehudai, A. (2024). JuStRank: Benchmarking LLM judges for system ranking. arXiv. https://arxiv.org/abs/2412.09569

Hwang, Y., Lee, D., Kang, T., Kim, Y., & Jung, K. (2025). Can you trick the grader? Adversarial persuasion of LLM judges. arXiv. https://arxiv.org/abs/2508.07805

Lail, R. (2026). Decomposing LLM-Judge uncertainty to target expert labels. arXiv. https://arxiv.org/abs/2609.06444

Yorke, L. (2026). Behind aggregate scores: What systematically varying Arena-Hard's LLM judge reveals. arXiv. https://arxiv.org/abs/2610.30512

Zhu, B., Xie, Y., & Rao, Y. (2026). A finite-calibration regime map for LLM judge panels. arXiv. https://arxiv.org/abs/2606.01034
