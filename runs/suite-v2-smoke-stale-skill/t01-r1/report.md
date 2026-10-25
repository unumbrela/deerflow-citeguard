# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search queries "LLM agent evaluation" and "agent benchmarks", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of LLM agent evaluation has rapidly evolved from static benchmark suites toward more sophisticated, domain-specific, and methodologically rigorous evaluation frameworks. The ten surveyed papers collectively reveal a maturing field grappling with fundamental challenges: how to automate evaluation without sacrificing reliability, how to ensure benchmarks themselves are valid and free from measurement artifacts, and how to extend evaluation beyond English-centric, single-domain contexts. A strong convergence exists around the need for process-aware evaluation that examines not just outcomes but the trajectories agents take. Simultaneously, emerging work on benchmark auditing reveals that many apparent agent failures are actually benchmark design failures. The literature points toward a future where evaluation is adaptive, certified, multilingual, and grounded in real-world economic and social contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the queries "LLM agent evaluation" and "agent benchmarks", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 unique papers were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review is restricted to the cs.CL category, potentially excluding relevant work in cs.AI or other categories.

## Themes

### Theme 1: Certified and Automated Evaluation

A major direction in agent evaluation research focuses on automating the evaluation process while providing formal guarantees about error rates. Traditional evaluation relies on human reviewers reading agent trajectories, which does not scale. Gan et al. (2026) address this by introducing a task-level bootstrap certificate that guarantees the error rate among automatically decided trajectories stays below a specified budget. Their approach handles correlated trajectory clusters—unlike standard i.i.d. certificates—and achieves 30-59% certified automation on tool-use and web corpora. Similarly, Ding (2026) presents AdaRubric, which adaptively generates task-specific evaluation rubrics rather than applying static dimensions across all tasks. This approach achieves 0.79 Pearson correlation with human judgments and produces high-quality preference pairs for reinforcement learning. Liu et al. (2025) take a different approach with MCPEval, an MCP-based framework that automates end-to-end task generation and evaluation across diverse domains, eliminating manual pipeline construction.

These works share a common insight: automation alone is insufficient; evaluation systems must provide reliability guarantees or demonstrate strong correlation with human judgment. The convergence around adaptive, task-specific evaluation suggests the field is moving beyond one-size-fits-all rubrics.

### Theme 2: Benchmark Validity and Auditing

A striking finding across multiple papers is that many apparent agent failures are actually benchmark failures. Tu et al. (2026) introduce BenchGuard, the first framework for automated auditing of execution-based agent benchmarks. Deployed on ScienceAgentBench and BIXBench, BenchGuard identified 12 author-confirmed issues including fatal errors rendering tasks unsolvable, and matched 83.3% of expert-identified issues while catching defects human review missed. Ding (2026) formalizes the concept of "specification-oracle gaps"—cases where passing tests requires information the task description never states. On SWE-Milestone, 25 of 98 graded milestones contained such gaps, affecting scoring fairness.

These papers collectively argue that benchmark quality must be validated independently of agent performance. The low cost of automated auditing (under $15 for 50 complex tasks in Tu et al.) makes it a practical complement to human review. This represents a significant shift: benchmarks are no longer treated as ground truth but as artifacts requiring their own validation.

### Theme 3: Efficient Benchmarking Through Compression

Given the high cost of evaluating agents on large benchmarks, several papers explore benchmark compression—selecting minimal task subsets that preserve ranking information. Guo et al. (2026) propose DualViewEval, which exploits both outcome and process relations to compress benchmarks. Unlike prior methods modeling only final-score redundancy, DualViewEval analyzes six complementary process signals from agent trajectories. With only 20 tasks, it achieves 24×–40× compression while reducing mean absolute error by 14.5%–28.2% over competitors. This work demonstrates that process-aware compression outperforms outcome-only approaches, aligning with the broader trend toward trajectory-based evaluation.

### Theme 4: Multilingual and Cultural Adaptation

The field has recognized that English-centric benchmarks fail to capture agent capabilities across languages and cultures. Kim et al. (2026) show that naive machine translation of benchmarks introduces query-answer misalignment and culturally off-target contexts. Their GAIA-v2-LILT workflow includes functional alignment, cultural alignment, and difficulty calibration, improving success rates by up to 32.7% over minimally translated versions. Lee et al. (2026) introduce K-BrowseComp, a Korean web-browsing benchmark revealing that frontier models drop from strong BrowseComp performance to only 30-45% on Korean contexts, while Korean-specific models score 0-10%.

These papers converge on a critical insight: multilingual performance gaps are partly benchmark-induced measurement error, not just model capability differences. Proper adaptation requires task-level alignment, not just translation.

### Theme 5: Domain-Specific Evaluation Frameworks

Several papers develop benchmarks for specialized domains where evaluation criteria differ substantially from general tasks. Schmidgall et al. (2024) present AgentClinic for clinical environments, where sequential decision-making under incomplete information is essential. Diagnostic accuracy drops to below one-tenth of static MedQA performance when evaluated in this interactive format. Siegel et al. (2024) introduce CORE-Bench for computational reproducibility across scientific disciplines, finding even the best agents achieve only 21% accuracy on the hardest tasks. Brazilek et al. (2026) present TAC for animal welfare in travel booking scenarios, revealing models prefer harmful scenarios below random chance unless given ethical personas.

These domain-specific benchmarks share a design principle: evaluation must reflect the real-world constraints and success criteria of the target domain, not abstracted proxies.

### Theme 6: Social and Organizational Context

A novel direction examines how distributed knowledge and authority affect agent performance. Hsu and Lu (2026) transform customer-service tasks into settings where information is spread across role-isolated participants rather than accessible through a single interface. Social access reduced success for every model tested, with the best model achieving only 0.65 success rate—a 0.11 decrease from centralized access. This work reveals that benchmarks concentrating all information behind one interface may overestimate agent capabilities in realistic organizational settings.

## Convergences and Disagreements

**Convergences**: 
- All surveyed papers agree that static, outcome-only evaluation is insufficient for agents. There is strong convergence on the need for process-aware, trajectory-based evaluation (Guo et al., 2026; Ding, 2026; Gan et al., 2026).
- Multiple papers independently identify benchmark validity as a critical issue, with Tu et al. (2026) and Ding (2026) both demonstrating that apparent agent failures often reflect benchmark design flaws.
- There is consensus that domain-specific evaluation criteria are necessary, with AgentClinic (Schmidgall et al., 2024), CORE-Bench (Siegel et al., 2024), and TAC (Brazilek et al., 2026) all arguing against one-size-fits-all benchmarks.
- The literature converges on multilingual adaptation requiring more than translation, with both Kim et al. (2026) and Lee et al. (2026) demonstrating substantial performance gaps from cultural and functional misalignment.

**Disagreements**: 
- The papers do not directly contradict each other, but they differ in emphasis on what aspects of evaluation matter most. Gan et al. (2026) prioritize certified error guarantees, while Ding (2026) emphasizes task-adaptive rubrics, and Guo et al. (2026) focus on compression efficiency. These are complementary rather than conflicting priorities, but they reflect different design trade-offs.
- There is tension between the push for automation (Gan et al., 2026; Liu et al., 2025) and the recognition that human oversight remains essential for benchmark auditing (Tu et al., 2026) and cultural adaptation (Kim et al., 2026).

## Gaps and Open Questions

The surveyed literature reveals several gaps:

1. **Limited cross-benchmark validation**: Most papers validate their methods on a small set of benchmarks (often 2-5). There is no large-scale, standardized meta-evaluation framework to compare evaluation methods themselves.

2. **Incomplete coverage of agent architectures**: Several papers note their methods work on specific agent architectures (e.g., ReAct, subagent delegation) but do not systematically evaluate how evaluation methods generalize across architectural paradigms.

3. **Temporal dynamics missing**: None of the surveyed papers address how agent capabilities and benchmark difficulty co-evolve over time. Benchmarks may become obsolete as models improve, but there is no framework for dynamic benchmark updating.

4. **Economic and societal impact measurement**: While Mühlbacher et al. (2024) argue for benchmarks tied to economic value, most papers do not connect their evaluation metrics to real-world outcomes or deployment consequences.

5. **Integration gaps**: The field has many specialized evaluation frameworks (MCPEval, AdaRubric, BenchGuard, etc.) but no unified platform integrating certification, auditing, compression, and domain-specific evaluation.

6. **Human-in-the-loop efficiency**: Several methods mention human review (Kim et al., 2026; Tu et al., 2026) but do not systematically optimize the division of labor between automated and human evaluation.

## Per-Paper Annotations

### Brazilek et al. (2026)

**Research question**: Do LLM agent evaluations of animal welfare in question-answer formats hold in agentic travel booking scenarios?
**Methodology**: Introduced TAC (Travel Agent Compassion) benchmark with 13 hand-authored scenarios across six animal categories, expanded to 52 prompts and run for three epochs (156 observations per model), evaluating nine frontier models with and without ethical persona prompts.
**Key findings**:
- Models perform below random chance (65%) for selecting neutral booking options, with Claude 4.8 highest at 64.7%
- Infusing ethical-brand persona into system prompts increases welfare rates from 32% to 80% (mean 53 percentage point increase)
- No evidence of evaluation awareness affecting results based on audit of 3,120 transcripts
- Findings directly relevant to EU General-Purpose AI Code of Practice identifying non-human welfare as systemic risk
**Limitations**: Focused on travel booking scenarios; results may not generalize to other agentic domains involving animal welfare.

### Ding (2026)

**Research question**: How can LLM agent evaluation be made task-specific rather than applying static rubrics that produce systematic mis-evaluation?
**Methodology**: AdaRubric framework adaptively generates task-specific evaluation rubrics from task descriptions via LLM, evaluates trajectories with confidence-weighted per-dimension scoring, and uses three composable filtering strategies including DimensionAwareFilter to produce high-quality DPO preference pairs.
**Key findings**:
- Achieves Pearson r = 0.79 human correlation, +0.15 over strongest baseline
- Strong inter-rater reliability with Krippendorff's alpha = 0.83
- DPO models trained on AdaRubric pairs improve task success by +6.8-8.5% over best baselines
- Generalizes zero-shot to unseen domains (SWE-bench) and extends to multimodal agents without modification
**Limitations**: Requires LLM overhead to generate rubrics per task; evaluation focused on specific benchmark domains though zero-shot generalization was tested.

### Gan et al. (2026)

**Research question**: What fraction of LLM agent evaluation can be automated with a certificate guaranteeing the error rate among auto-decided trajectories stays below a specified budget?
**Methodology**: Introduced task-level bootstrap certificate handling correlated trajectory clusters, trained 4B logprob judge using SFT and reject-weighted GRPO to selectively automate evaluation decisions.
**Key findings**:
- Naive i.i.d. certificates dangerously overstate safety, claiming 98% automation while realized error exceeds budget in 17.5% of task resamples
- Task-level bootstrap certificate remains valid across all tested regimes while matching naive certificate coverage
- 4B judge certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1, outperforming frontier models on both
- Certified coverage highly predictable from base rate and discrimination alone (leave-one-corpus-out R²=0.96)
- Certificate doubles as self-training filter with contamination bounded by alpha (realized 0.000-0.041)
**Limitations**: Finite-sample cluster-valid alternatives fail to certify anything at realistic task counts; validated only on specific tool-use and web corpora.

### Guo et al. (2026)

**Research question**: How can agent benchmarks be compressed more effectively by considering both outcome and process signals rather than just final-score distributions?
**Methodology**: Analyzed large-scale trajectories to identify six complementary process signals, proposed DualViewEval jointly exploiting outcome and process relations to learn exact-size miniset and predict full-benchmark scores.
**Key findings**:
- Achieves best results across five agent benchmarks and five baselines in all datasets
- With 20 tasks, achieves 24×–40× compression on APEX-Agents and BFCL
- Reduces mean absolute error by 14.5%–28.2% over strongest competitors
- Improves Kendall's τ by up to 7.2% relative to EssenceBench on SWE-bench Verified
- Selected minisets reveal capability differences among agents, providing diagnostic feedback
**Limitations**: Requires access to detailed process trajectories which may not be available for all benchmark settings.

### Hsu and Lu (2026)

**Research question**: How does distributing facts, tools, and permissions across people rather than behind one interface affect agent benchmark performance and discriminative power?
**Methodology**: Transformed 18 customer-service tasks into three settings: direct access, one known intermediary, and six role-isolated participants whose capabilities must be discovered, running 864 trials with four models.
**Key findings**:
- Social access reduced success for every model tested
- Pre-specified intervals excluded zero for two models, confirming statistically significant effects
- gpt-5.6-sol achieved highest social-access success at 0.65, a 0.11 decrease from centralized indirect access
- Exploratory comparisons separated five of six model pairs under social access, while neither centralized setting separated any
- Three pairwise interaction p-values remained significant after multiplicity adjustment
**Limitations**: Data cannot distinguish ineffective requests by evaluated agent from inaccurate replies by simulated participants, so labels describe where trajectories stopped rather than why models differed.

### Kim et al. (2026)

**Research question**: How can English agent benchmarks be adapted to multiple languages without breaking benchmark validity through translation artifacts?
**Methodology**: Proposed refined workflow for adapting English benchmarks with explicit functional alignment, cultural alignment, and difficulty calibration using automated checks and human review, resulting in GAIA-v2-LILT covering five non-English languages.
**Key findings**:
- Workflow improves agent success rates by up to 32.7% over minimally translated versions
- Brings closest audited setting to within 3.1% of English performance
- Substantial gaps remain in many cases, indicating benchmark-induced measurement error
- Substantial share of multilingual performance gap is benchmark-induced, not model capability
- Task-level alignment necessary when adapting English benchmarks across languages
**Limitations**: Substantial performance gaps remain in many language cases despite improved workflow; full parity with English benchmarks not yet achieved.

### Lee et al. (2026)

**Research question**: How do frontier models perform on Korean web-browsing tasks given the scarcity of Korean agentic benchmarks?
**Methodology**: Introduced K-BrowseComp with 400 problems, including 300-problem manually constructed and validated K-BrowseComp-Verified subset by native Korean speakers, plus 100-problem synthetic split using hard few-shot exemplars and failure-mode-targeted generation.
**Key findings**:
- Frontier LLMs (GPT-5.5, DeepSeek-V4-Pro, GLM-5.1) reach only 30.00%–45.67% on K-BrowseComp-Verified, substantial drop from BrowseComp
- Korean LLMs from Korea's Proprietary AI Foundation Model program obtain only 0.00%–10.33%
- On adversarially filtered synthetic diagnostic split, strongest model reaches only 26.00%
- Exploitable asymmetry exists between solving and creating web browsing problems
- Benchmark reveals significant gaps between general frontier models and Korean-specific models
**Limitations**: Extremely low performance across all models suggests benchmark may be exceptionally challenging or may have limited discriminative power at lower end.

### Liu et al. (2025)

**Research question**: How can LLM agent evaluation be automated and standardized across diverse domains without relying on static benchmarks and labor-intensive manual data collection?
**Methodology**: MCPEval is open-source framework built on Model Context Protocol (MCP) that automates end-to-end task generation and deep evaluation, standardizes metrics, and integrates with native agent tools.
**Key findings**:
- Framework eliminates manual effort in building evaluation pipelines through MCP-based automation
- Demonstrates effectiveness across five real-world domains with nuanced, domain-specific performance insights
- Standardizes metrics for reproducible and comparable agent evaluation
- Seamlessly integrates with existing native agent tools without requiring custom adapters
- Publicly released as open-source to promote standardized LLM agent evaluation practices
**Limitations**: Empirical validation limited to five domains; framework effectiveness depends on MCP integration availability for target agent tools.

### Mühlbacher et al. (2024)

**Research question**: How do LLM agents perform on real-world, economically valuable open-web research tasks typical of finance and consulting work?
**Methodology**: Built benchmark with messy, real-world open-web research tasks, evaluated multiple agent architectures (including ReAct with subagent delegation) across different LLMs, combining quantitative metrics with qualitative trace analysis.
**Key findings**:
- Claude-3.5 Sonnet and o1-preview substantially outperformed GPT-4o on average across research tasks
- Llama 3.1 (405b) and GPT-4o-mini agents lagged noticeably behind leading models
- ReAct architecture with subagent delegation capability performed best across all LLMs tested
- First in-depth assessment demonstrating agent capabilities on challenging, economically valuable analyst-style research
- Good performance on benchmark directly corresponds to large economic and societal impact potential
**Limitations**: Presents initial results from forthcoming benchmark rather than final validated suite; qualitative assessment relies on manual trace inspection and author observations.

### Schmidgall et al. (2024)

**Research question**: How can LLMs be evaluated more realistically in clinical scenarios beyond static question-answering to capture complex, sequential nature of clinical decision-making?
**Methodology**: Introduced AgentClinic, multimodal agent benchmark for evaluating LLMs in simulated clinical environments including patient interactions, multimodal data collection under incomplete information, and tool usage across nine medical specialties and seven languages.
**Key findings**:
- Solving MedQA problems in sequential decision-making format considerably more challenging, with diagnostic accuracies dropping to below one-tenth of original accuracy
- Agents sourced from Claude-3.5 outperform other LLM backbones in most settings
- Stark differences exist in LLMs' ability to use tools such as experiential learning, adaptive retrieval, and reflection cycles
- Llama-3 shows up to 92% relative improvements with notebook tool allowing writing and editing notes persisting across cases
- Interactive environment enables novel patient-centric metrics not possible with static benchmarks
**Limitations**: Relies on simulated clinical environments rather than real-world clinical settings; simulations may not fully capture real clinical complexity.

### Siegel et al. (2024)

**Research question**: How can AI agents be evaluated on computational reproducibility tasks that correspond to real-world scientific research workflows?
**Methodology**: Introduced CORE-Bench with 270 tasks based on 90 scientific papers across three disciplines (computer science, social science, medicine), with three difficulty levels and both language-only and vision-language tasks, evaluated AutoGPT and CORE-Agent using GPT-4o and GPT-4o-mini.
**Key findings**:
- Best agent achieved only 21% accuracy on hardest tasks, showing vast scope for improvement
- Evaluation system saves days of evaluation time per run compared to sequential implementation
- Having agents that can reproduce existing work is necessary step toward building agents that can conduct novel research
- Benchmark includes both language-only and vision-language tasks across multiple difficulty levels
- Publicly released to improve state of reproducibility and spur development of future research agents
**Limitations**: Accuracy remains low even on easier tasks; benchmark may require further refinement to better discriminate agent capabilities.

### Tu et al. (2026)

**Research question**: Can frontier LLMs be employed as systematic auditors to identify failures in evaluation infrastructure itself rather than just evaluating agent performance?
**Methodology**: BenchGuard is first framework for joint cross-artifact auditing of execution-based agent benchmarks, using structured LLM protocols to cross-verify all benchmark artifacts with optional incorporation of agent solutions or execution traces.
**Key findings**:
- Identified 12 author-confirmed issues in ScienceAgentBench, including fatal errors rendering tasks unsolvable
- Exactly matched 83.3% of expert-identified issues on BIXBench Verified-50 subset
- Caught defects that prior human review entirely missed, demonstrating value beyond manual auditing
- Full audit of 50 complex bioinformatics tasks costs under USD 15, making it economically practical
- Demonstrates cross-format applicability with preliminary native-format audit of ProgramBench
**Limitations**: Validation limited to specific benchmarks (ScienceAgentBench, BIXBench, ProgramBench); ProgramBench audit remains preliminary rather than comprehensive.

## References

Brazilek, J., Christoph, J., Chaudhary, M., Tullio, O., Kline, C., Tidmarsh, M., & Kanepajs, A. (2026). Your AI travel agent would book you a bullfight: An agentic benchmark for implicit animal welfare in frontier AI models. arXiv. https://arxiv.org/abs/2606.18142

Ding, F. (2026). What the specification did not say: Specification-oracle gaps in test-graded coding-agent benchmarks. arXiv. https://arxiv.org/abs/2610.30635

Ding, L. (2026). AdaRubric: Task-adaptive rubrics for reliable LLM agent evaluation and reward learning. arXiv. https://arxiv.org/abs/2603.21362

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Guo, X., Wu, J., Deng, D., Li, Y., Zheng, H.-T., Zheng, S., & Pan, M. (2026). Beyond outcomes: Dual-view relational learning for efficient agent benchmarking. arXiv. https://arxiv.org/abs/2609.18909

Hsu, D. C., & Lu, L. (2026). Where knowledge and authority sit changes what an agent benchmark can resolve. arXiv. https://arxiv.org/abs/2607.02975

Kim, Y., Uhlig, K., & Wuebker, J. (2026). GAIA-v2-LILT: Multilingual adaptation of agent benchmark beyond translation. arXiv. https://arxiv.org/abs/2604.24929

Lee, N., Yoon, D., Son, G., Kim, G., Ko, D., Park, J., Yoo, H., Cho, J., Park, J., Lee, C., Jang, K., Kim, J., Kim, E., Cho, W., & Kim, S. (2026). K-BrowseComp: A web browsing agent benchmark grounded in Korean contexts. arXiv. https://arxiv.org/abs/2606.02404

Liu, Z., Qiu, J., Wang, S., Zhang, J., Liu, Z., Ram, R., Chen, H., Yao, W., Heinecke, S., Savarese, S., Wang, H., & Xiong, C. (2025). MCPEval: Automatic MCP-based deep evaluation for AI agent models. arXiv. https://arxiv.org/abs/2507.12806

Mühlbacher, P., Bosse, N. I., & Phillips, L. (2024). Towards a realistic long-term benchmark for open-web research agents. arXiv. https://arxiv.org/abs/2409.14913

Schmidgall, S., Ziaei, R., Harris, C., Reis, E., Jopling, J., & Moor, M. (2024). AgentClinic: A multimodal agent benchmark to evaluate AI in simulated clinical environments. arXiv. https://arxiv.org/abs/2405.07960

Siegel, Z. S., Kapoor, S., Nadgir, N., Stroebl, B., & Narayanan, A. (2024). CORE-Bench: Fostering the credibility of published research through a computational reproducibility agent benchmark. arXiv. https://arxiv.org/abs/2409.11363

Tu, X., Wang, T., Lu, Y., Huang, K., Qu, Y., & Mostafavi, S. (2026). Who guards the benchmarks? Automated auditing of LLM agent benchmarks. arXiv. https://arxiv.org/abs/2604.24955
