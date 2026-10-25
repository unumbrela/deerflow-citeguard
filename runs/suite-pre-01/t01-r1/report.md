# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search queries "LLM agent evaluation" and "agent benchmark", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agent evaluation benchmarks has rapidly evolved from static, English-centric benchmarks toward more realistic, multimodal, and methodologically rigorous evaluation frameworks. The surveyed papers collectively reveal a field grappling with fundamental challenges in benchmark validity, automation, cost-efficiency, and real-world applicability. Key trends include the shift from outcome-only evaluation to process-aware assessment, growing recognition of cultural and linguistic biases in benchmarks, and increasing emphasis on economically valuable real-world tasks. Multiple papers identify specification-oracle gaps, benchmark-induced measurement errors, and the need for certified automation in evaluation pipelines. The field shows strong convergence on the inadequacy of current benchmarks while proposing diverse solutions ranging from adaptive rubrics to benchmark compression algorithms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the queries "LLM agent evaluation" and "agent benchmark", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses on cs.CL category, potentially missing relevant papers in cs.AI, cs.CV, or other categories.

## Themes

### Theme 1: Benchmark Validity and Measurement Error

A dominant theme across the surveyed literature is the recognition that benchmarks themselves introduce systematic measurement errors that confound agent evaluation. Recent work has exposed multiple sources of benchmark-induced bias, from translation artifacts to specification gaps.

Kim et al. (2026) demonstrate that minimally translated benchmarks can break validity through query-answer misalignment and culturally off-target contexts, with their refined GAIA-v2-LILT workflow improving agent success rates by up to 32.7% over machine-translated versions. Their finding that a substantial share of the multilingual performance gap is benchmark-induced measurement error rather than true capability differences has profound implications for cross-lingual agent evaluation.

Ding (2026) formalizes the specification-oracle gap problem in coding-agent benchmarks, where test-graded tasks require information the natural language description never states. Their audit found that 25 of 98 milestones in SWE-Milestone contain tests depending on unstated, non-inferable names or paths, with build units containing such dependencies failing in 80.6% of runs versus 48.4% for comparable units without gaps. This reveals that benchmarks measure not just agent capability but also the ability to reproduce upstream implementation details.

Tu et al. (2026) take this critique further by proposing automated benchmark auditing through BenchGuard, which identified 12 author-confirmed issues in ScienceAgentBench including fatal errors rendering tasks unsolvable. Their framework cross-verifies all benchmark artifacts via structured LLM protocols, matching 83.3% of expert-identified issues on BIXBench Verified-50 subset while catching defects prior human review missed. These three papers collectively argue that benchmark infrastructure itself requires systematic validation before it can serve as reliable evaluation ground truth.

### Theme 2: From Static to Adaptive Evaluation Frameworks

The literature shows a clear trajectory from fixed, one-size-fits-all evaluation rubrics toward adaptive, task-specific assessment frameworks that recognize the contextual nature of agent performance.

Ding (2026) presents AdaRubric, which adaptively generates task-specific evaluation rubrics from task descriptions rather than applying static dimensions. Their framework achieves Pearson r = 0.79 human correlation (+0.15 over strongest baseline) with strong reliability (Krippendorff's alpha = 0.83), demonstrating that task-adaptive evaluation substantially outperforms fixed rubrics. The framework's ability to generalize zero-shot to unseen domains (SWE-bench) and extend to multimodal agents without modification suggests adaptive evaluation may be a general solution to the rubric mismatch problem.

Gan et al. (2026) address a different aspect of adaptive evaluation through certified selective automation, asking what fraction of agent evaluation can be automated with guarantees on error rates. Their task-level bootstrap certificate accounts for correlated trajectory clusters that invalidate i.i.d. assumptions in existing selective-judging methods. Under their certificate, a 4B parameter judge certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1, with certified coverage predictable from base rate and discrimination alone (R²=0.96). This work operationalizes the question of evaluation automation with mathematical guarantees rather than empirical claims.

Liu et al. (2025) introduce MCPEval, an MCP-based framework that automates end-to-end task generation and deep evaluation across diverse domains. By standardizing metrics and eliminating manual pipeline construction, their approach addresses the labor-intensive nature of current evaluation while revealing nuanced, domain-specific performance patterns. These three papers collectively argue that evaluation must be adaptive across multiple dimensions: task-specific rubrics, certified automation levels, and domain-aware task generation.

### Theme 3: Real-World Grounding and Economic Value

A significant strand of recent work emphasizes moving beyond synthetic benchmarks toward evaluation on real-world tasks with direct economic and societal impact, grounding agent assessment in actual use cases.

Mühlbacher et al. (2024) present initial results from a benchmark evaluating LLM agents on white-collar tasks of economic value in finance and consulting. Their evaluation on real-world "messy" open-web research tasks found that Claude-3.5 Sonnet and o1-preview substantially outperformed GPT-4o, with ReAct architecture with subagent delegation performing best across all LLMs. Their work represents the first in-depth assessment of agents' abilities on economically valuable analyst-style research on the real open web, establishing a template for impact-grounded evaluation.

Schmidgall et al. (2024) introduce AgentClinic, a multimodal benchmark evaluating LLMs in simulated clinical environments across nine medical specialties and seven languages. Their finding that sequential decision-making format drops diagnostic accuracies to below a tenth of static QA accuracy reveals the gap between benchmark performance and real clinical utility. The benchmark's incorporation of patient interactions, multimodal data collection under incomplete information, and tool usage provides a more realistic assessment of clinical agent capabilities.

Yu et al. (2026) bridge physical and digital worlds with Ego2Web, pairing real-world egocentric video recordings with web tasks requiring visual understanding and online execution. Their benchmark addresses the critical limitation that current web-agent benchmarks lack grounding in users' physical surroundings, preventing evaluation of AR/glasses-based scenarios. The weak performance of state-of-the-art agents on Ego2Web with substantial headroom across all categories suggests current benchmarks substantially overestimate real-world agent capabilities. These three papers collectively argue that benchmark validity requires grounding in real-world contexts with genuine stakes.

### Theme 4: Efficiency and Compression in Agent Evaluation

As agent benchmarks grow in complexity and cost, several papers address the challenge of maintaining evaluation quality while dramatically reducing computational and temporal overhead.

Guo et al. (2026) propose DualViewEval, which achieves 24×-40× compression on APEX-Agents and BFCL benchmarks using only 20 tasks while reducing mean absolute error by 14.5%-28.2% over strongest competitors. Their key insight is modeling both outcome and process relations rather than just final-score distributions, identifying six complementary process signals systematically associated with final agent performance. The selected minisets reveal capability differences among agents, providing compact diagnostic feedback for efficient model development.

Gan et al. (2026) approach efficiency through certified selective automation, where their 4B parameter judge certifies 0.30-0.59 of evaluation at alpha=0.1 error budget. The certificate doubles as a self-training filter with contamination bounded by alpha (realized 0.000-0.041 across six harvests), enabling judges to enter unseen domains at in-domain strength with zero target training labels. This dual use of certificates for both evaluation automation and training data generation represents a novel approach to reducing evaluation costs.

The convergence of these approaches suggests the field is maturing beyond brute-force evaluation toward principled compression and automation strategies that maintain or improve evaluation quality while dramatically reducing costs.

### Theme 5: Linguistic and Cultural Diversity in Benchmarks

Recent work has exposed the English-centric bias of agent benchmarks and the systematic errors introduced by naive translation approaches, calling for culturally-aware benchmark adaptation.

Lee et al. (2026) introduce K-BrowseComp, a 400-problem web-browsing benchmark grounded in Korean contexts. Their finding that frontier LLMs drop from strong BrowseComp performance to only 30.00-45.67% on K-BrowseComp-Verified, while Korean LLMs obtain only 0.00-10.33%, reveals both the language-specific nature of agent capabilities and the inadequacy of current multilingual evaluation. The adversarially filtered synthetic diagnostic split, where the strongest model reaches only 26.00%, provides targeted stress testing for language-specific agent weaknesses.

Kim et al. (2026) demonstrate that machine translation workflows can break benchmark validity through query-answer misalignment and culturally off-target contexts. Their refined workflow with functional alignment, cultural alignment, and difficulty calibration brings the closest audited setting to within 3.1% of English performance, though substantial gaps remain. Their finding that task-level alignment is necessary when adapting English benchmarks across languages challenges the assumption that translation alone suffices for multilingual evaluation.

These papers collectively argue that linguistic and cultural diversity in benchmarks is not merely a matter of translation but requires fundamental rethinking of task design and validation processes.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the inadequacy of current benchmark infrastructure. Gan et al. (2026), Tu et al. (2026), and Ding (2026) all identify systematic errors in evaluation pipelines, whether from invalid certificates, broken specifications, or specification-oracle gaps. There is strong agreement that benchmarks require active validation rather than passive acceptance as ground truth.

All papers addressing multilingual or cross-cultural evaluation (Lee et al., 2026; Kim et al., 2026) converge on the finding that naive translation approaches fail to preserve benchmark validity, requiring cultural and functional alignment beyond linguistic translation.

Multiple papers (Schmidgall et al., 2024; Mühlbacher et al., 2024; Yu et al., 2026) converge on the gap between synthetic benchmark performance and real-world capability, with sequential decision-making and multimodal grounding revealing substantial performance drops not visible in static evaluations.

**Disagreements**: While there is agreement on benchmark inadequacy, papers diverge on solutions. Gan et al. (2026) pursue certified automation of evaluation, while Guo et al. (2026) focus on benchmark compression through process-aware selection. These represent different philosophies: automating human evaluation versus minimizing the need for evaluation.

Ding (2026) proposes adaptive rubrics generated per-task, while Tu et al. (2026) advocate automated auditing of fixed benchmarks. The former accepts rubric flexibility while the latter seeks to validate fixed infrastructure.

## Gaps and Open Questions

Several gaps emerge from the collective limitations identified across the surveyed papers:

**Computational overhead of rigorous evaluation**: Multiple papers acknowledge the cost of their proposed solutions without addressing scalability. Kim et al. (2026) require human review for multilingual adaptation, Tu et al. (2026) note their audit costs under $15 per 50 tasks but don't address continuous evaluation costs, and Gan et al. (2026) require training specialized judges. The field lacks analysis of sustainable evaluation pipelines at scale.

**Generalization across domains**: While AdaRubric (Ding, 2026) demonstrates zero-shot generalization to unseen domains and MCPEval (Liu et al., 2025) covers five domains, most proposed solutions are validated on narrow benchmark sets. The extent to which certified automation, adaptive rubrics, or compression methods generalize across the full space of agent tasks remains untested.

**Temporal validity of benchmarks**: None of the surveyed papers address how benchmarks age as agents improve. The substantial headroom reported on Ego2Web (Yu et al., 2026) and K-BrowseComp (Lee et al., 2026) will inevitably close, but the literature lacks frameworks for benchmark refreshing or lifecycle management.

**Integration of evaluation approaches**: The field presents multiple orthogonal solutions (certification, compression, adaptation, auditing) without integration frameworks. How DualViewEval's compression interacts with AdaRubric's adaptive scoring, or whether BenchGuard auditing should precede or follow certification, remains unexplored.

**Human-in-the-loop validation**: While papers acknowledge the need for human validation (Kim et al., 2026; Mühlbacher et al., 2024), none provide systematic analysis of when human judgment is necessary versus when automation suffices. The boundary between certified automation and human oversight remains operationally undefined.

## Per-Paper Annotations

### Ding (2026)

**Research question**: How can LLM agent evaluation be made task-specific rather than applying a fixed rubric regardless of task domain?
**Methodology**: AdaRubric adaptively generates task-specific evaluation rubrics from task descriptions via LLM, evaluates trajectories step-by-step with confidence-weighted per-dimension scoring, and produces dense reward signals for preference learning with three composable filtering strategies including DimensionAwareFilter.
**Key findings**:
- Achieves Pearson r = 0.79 human correlation, +0.15 over the strongest baseline
- Strong reliability with Krippendorff's alpha = 0.83
- DPO models trained on AdaRubric-generated pairs improve task success by +6.8-8.5% over best baseline
- Generalizes zero-shot to unseen domains (SWE-bench)
- Extends to multimodal agents (VisualWebArena, OSWorld) without modification
**Limitations**: Framework depends on LLM-generated rubrics which may introduce their own biases; not explicitly tested on all possible task domains.

### Ding (2026)

**Research question**: Where do coding-agent benchmarks contain specification-oracle gaps that measure reproduction of upstream implementation details rather than stated task capability?
**Methodology**: Built a static audit for five languages that classifies every name-, path- and literal-level dependency of every scored test, then audited SWE-Milestone and four additional benchmarks to quantify gap prevalence and impact.
**Key findings**:
- 25 of 98 graded milestones in SWE-Milestone contain tests depending on unstated, non-inferable names or paths
- Build units with such dependencies fail in 80.6% of runs versus 48.4% for comparable units without gaps
- Withholding a single hidden name stops its unit's tests from compiling in 126 of 128 cases
- Prevalence follows construction: a third or more of tasks affected where specifications are release notes or LLM summaries
- Leaderboard rankings robust to removing affected tests, but gaps shift scores within repositories
**Limitations**: Audit focuses on test-graded coding benchmarks; prevalence and impact in other benchmark types (e.g., open-ended generation) not assessed.

### Gan et al. (2026)

**Research question**: What fraction of LLM agent evaluation can be automated with a certificate that the error rate among auto-decided trajectories stays below a budget alpha?
**Methodology**: Introduced a task-level bootstrap certificate that accounts for correlated trajectory clusters (unlike i.i.d. certificates), and trained a 4B logprob judge with SFT and reject-weighted GRPO.
**Key findings**:
- Naive certificates can claim 98% automation while realized error exceeds budget in 17.5% of task resamples
- Task-level bootstrap certificate is valid in every regime tested while matching naive certificate's coverage
- The 4B judge certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1, the only judge certifying on both headline corpora
- Certified coverage is predictable from base rate and discrimination alone (leave-one-corpus-out R²=0.96)
- Certificate doubles as self-training filter with contamination bounded by alpha (realized 0.000-0.041 across six harvests)
**Limitations**: Finite-sample cluster-valid alternatives certify nothing at realistic task counts; validation limited to tool-use and web corpora.

### Guo et al. (2026)

**Research question**: Can agent benchmarks be compressed more effectively by modeling both outcome and process signals rather than just final-score distributions?
**Methodology**: Analyzed large-scale agent trajectories to identify six complementary process signals associated with final performance, then proposed DualViewEval that jointly exploits outcome and process relations to learn exact-size minisets and predict full-benchmark scores.
**Key findings**:
- With only 20 tasks, achieves 24×-40× compression on APEX-Agents and BFCL benchmarks
- Reduces mean absolute error (MAE) by 14.5%-28.2% over the strongest competitors
- Improves Kendall's τ by up to 7.2% relative to EssenceBench on SWE-bench Verified
- Selected minisets reveal capability differences among different agents, providing diagnostic feedback
- Process signals are systematically associated with final agent performance and provide complementary information beyond outcomes
**Limitations**: Requires large-scale trajectory data for process signal extraction; may not generalize equally well to all agent benchmark types or domains without validation.

### Kim et al. (2026)

**Research question**: How can English agent benchmarks be adapted to multiple languages while maintaining validity, avoiding the pitfalls of simple machine translation?
**Methodology**: Proposed a refined workflow for adapting English benchmarks into multiple languages with explicit functional alignment, cultural alignment, and difficulty calibration using both automated checks and human review, then applied it to create GAIA-v2-LILT covering five non-English languages.
**Key findings**:
- Workflow improves agent success rates by up to 32.7% over minimally translated versions
- Closest audited setting comes within 3.1% of English performance, though substantial gaps remain in other cases
- Substantial share of multilingual performance gap is benchmark-induced measurement error from poor translation workflows
- Minimal machine translation workflows can break benchmark validity through query-answer misalignment or culturally off-target context
- Task-level alignment is necessary when adapting English benchmarks across languages
**Limitations**: Substantial performance gaps remain in many language cases despite the improved workflow; human review requirement makes the process costly and less scalable.

### Lee et al. (2026)

**Research question**: How well do frontier and Korean LLMs perform on web-browsing agent tasks grounded in Korean contexts compared to English benchmarks?
**Methodology**: Created K-BrowseComp, a 400-problem web-browsing agent benchmark with 300 manually validated problems and 100 synthetic problems using hard few-shot exemplars and failure-mode-targeted generation, then evaluated frontier and Korean LLMs on these tasks.
**Key findings**:
- Frontier LLMs (GPT-5.5, DeepSeek-V4-Pro, GLM-5.1) reach only 30.00-45.67% on K-BrowseComp-Verified, a substantial drop from English BrowseComp performance
- Korean LLMs from Korea's Proprietary AI Foundation Model program obtain only 0.00-10.33% on the verified subset
- On the adversarially filtered synthetic diagnostic split, the strongest model reaches only 26.00%
- Synthetic split exploits asymmetry between solving and creating web browsing problems for targeted stress testing
**Limitations**: Benchmark focuses exclusively on Korean contexts, limiting generalizability to other languages; the synthetic split, while useful for stress testing, may not fully represent real-world web browsing scenarios.

### Liu et al. (2025)

**Research question**: How can LLM agent evaluation be automated and standardized across diverse domains without manual effort in building evaluation pipelines?
**Methodology**: MCPEval is an open-source Model Context Protocol (MCP)-based framework that automates end-to-end task generation and deep evaluation, standardizes metrics, and seamlessly integrates with native agent tools.
**Key findings**:
- Eliminates manual effort in building evaluation pipelines
- Empirical results across five real-world domains show effectiveness in revealing nuanced, domain-specific performance
- Standardizes metrics across diverse domains
- Seamlessly integrates with native agent tools
- Open-source release promotes reproducible and standardized LLM agent evaluation
**Limitations**: Abstract does not explicitly state limitations; empirical validation limited to five domains; framework effectiveness may depend on MCP compatibility.

### Mühlbacher et al. (2024)

**Research question**: How can LLM agents be evaluated on realistic, economically valuable open-web research tasks that reflect real-world white-collar work?
**Methodology**: Built and tested several agent architectures with different LLMs (o1-preview, GPT-4o, Claude-3.5 Sonnet, Llama 3.1 405b, GPT-4o-mini) on real-world messy open-web research tasks, using both quantitative evaluations and qualitative trace inspection.
**Key findings**:
- Claude-3.5 Sonnet and o1-preview substantially outperformed GPT-4o on average
- Llama 3.1 (405b) and GPT-4o-mini lagged noticeably behind other models
- ReAct architecture with ability to delegate subtasks to subagents performed best across all LLMs
- Good performance on this benchmark corresponds to large economic and societal impact
- First in-depth assessment of agents' abilities on challenging analyst-style research on the real open web
**Limitations**: Initial results of a forthcoming benchmark; qualitative assessment based on inspecting traces and reflecting on observations rather than fully automated metrics.

### Schmidgall et al. (2024)

**Research question**: How well do LLMs perform in simulated clinical environments requiring sequential decision-making, multimodal data collection, and tool usage compared to static question-answering benchmarks?
**Methodology**: Introduced AgentClinic, a multimodal agent benchmark across nine medical specialties and seven languages that includes patient interactions, incomplete information scenarios, and tool usage, then evaluated multiple LLM backbones and compared performance with and without various tools.
**Key findings**:
- Solving MedQA problems in sequential decision-making format drops diagnostic accuracies to below a tenth of original static QA accuracy
- Agents sourced from Claude-3.5 outperform other LLM backbones in most clinical settings
- Llama-3 shows up to 92% relative improvements with the notebook tool that allows writing and editing persistent notes across cases
- Stark differences exist in LLMs' ability to utilize tools such as experiential learning, adaptive retrieval, and reflection cycles
- Interactive environment enables novel patient-centric metrics and clinical reader studies using real-world electronic health records
**Limitations**: Simulated clinical environments may not fully capture the complexity and stakes of real clinical decision-making; the benchmark relies on simulated rather than actual patient interactions.

### Tu et al. (2026)

**Research question**: Can frontier LLMs be employed as systematic auditors to identify failures in agent benchmark evaluation infrastructure itself?
**Methodology**: Developed BenchGuard, the first framework for joint cross-artifact auditing of execution-based agent benchmarks, cross-verifying all benchmark artifacts via structured LLM protocols with optional incorporation of agent solutions or execution traces as diagnostic evidence.
**Key findings**:
- Identified 12 author-confirmed issues in ScienceAgentBench, including fatal errors rendering tasks unsolvable
- Exactly matched 83.3% of expert-identified issues on BIXBench Verified-50 subset, catching defects prior human review missed
- Full audit of 50 complex bioinformatics tasks costs under USD $15
- Demonstrates cross-format applicability through preliminary native-format audit of ProgramBench
- Points toward AI-assisted benchmark development where frontier models validate evaluation infrastructure
**Limitations**: Framework identifies issues but does not automatically fix them; human review still required for issue resolution and benchmark repair.

### Yu et al. (2026)

**Research question**: How can web agent benchmarks incorporate egocentric visual perception from users' real-world physical surroundings to enable evaluation of truly multimodal AI assistants?
**Methodology**: Created Ego2Web benchmark pairing real-world first-person video recordings with web tasks requiring visual understanding and online execution, using automatic data generation with human verification, and developed Ego2WebJudge LLM-as-a-Judge evaluation method.
**Key findings**:
- Ego2WebJudge achieves approximately 84% agreement with human judgment, substantially higher than existing evaluation methods
- State-of-the-art agents show weak performance on Ego2Web with substantial headroom across all task categories
- Accurate video understanding is necessary for successful task completion in the proposed benchmark
- Current web-agent benchmarks lack grounding in users' real-world physical surroundings, preventing evaluation of crucial AR/glasses-based scenarios
- Comprehensive ablation study highlights limitations of current agents in bridging physical and digital world understanding
**Limitations**: Current agents have limited egocentric video understanding capabilities; benchmark focuses on specific web task types (e-commerce, media retrieval, knowledge lookup) that may not cover all real-world scenarios.

## References

Chen, Z., Daniel, W., Chen, P.-Y., & Buet-Golfouse, F. (2024). Online personalizing white-box LLMs generation with neural bandits. arXiv. https://arxiv.org/abs/2404.16115

Ding, F. (2026). What the specification did not say: Specification-oracle gaps in test-graded coding-agent benchmarks. arXiv. https://arxiv.org/abs/2610.30635

Ding, L. (2026). AdaRubric: Task-adaptive rubrics for reliable LLM agent evaluation and reward learning. arXiv. https://arxiv.org/abs/2603.21362

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Guo, X., Wu, J., Deng, D., Li, Y., Zheng, H.-T., Zheng, S., & Pan, M. (2026). Beyond outcomes: Dual-view relational learning for efficient agent benchmarking. arXiv. https://arxiv.org/abs/2609.18909

Kim, Y., Uhlig, K., & Wuebker, J. (2026). GAIA-v2-LILT: Multilingual adaptation of agent benchmark beyond translation. arXiv. https://arxiv.org/abs/2604.24929

Lee, N., Yoon, D., Son, G., Kim, G., Ko, D., Park, J., Yoo, H., Cho, J., Park, J., Lee, C., Jang, K., Kim, J., Kim, E., Cho, W., & Kim, S. (2026). K-BrowseComp: A web browsing agent benchmark grounded in Korean contexts. arXiv. https://arxiv.org/abs/2606.02404

Liu, Z., Qiu, J., Wang, S., Zhang, J., Liu, Z., Ram, R., Chen, H., Yao, W., Heinecke, S., Savarese, S., Wang, H., & Xiong, C. (2025). MCPEval: Automatic MCP-based deep evaluation for AI agent models. arXiv. https://arxiv.org/abs/2507.12806

Mühlbacher, P., Bosse, N. I., & Phillips, L. (2024). Towards a realistic long-term benchmark for open-web research agents. arXiv. https://arxiv.org/abs/2409.14913

Schmidgall, S., Ziaei, R., Harris, C., Reis, E., Jopling, J., & Moor, M. (2024). AgentClinic: A multimodal agent benchmark to evaluate AI in simulated clinical environments. arXiv. https://arxiv.org/abs/2405.07960

Tu, X., Wang, T., Lu, Y., Huang, K., Qu, Y., & Mostafavi, S. (2026). Who guards the benchmarks? Automated auditing of LLM agent benchmarks. arXiv. https://arxiv.org/abs/2604.24955

Yu, S., Shu, L., Yang, A., Fu, Y., Sunkara, S., Wang, M., Chen, J., Bansal, M., & Gong, B. (2026). Ego2Web: A web agent benchmark grounded in egocentric videos. arXiv. https://arxiv.org/abs/2603.22529
