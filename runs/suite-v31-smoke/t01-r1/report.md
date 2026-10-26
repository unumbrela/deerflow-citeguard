# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "agent evaluation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agent evaluation benchmarks reveals a rapidly evolving field grappling with the tension between automation and realism. Recent work emphasizes moving beyond static benchmarks toward dynamic, multi-step evaluation frameworks that capture the complexity of real-world agent interactions. A dominant theme is the automation of evaluation itself, with multiple papers proposing AI-driven evaluators that can reduce human annotation burden while maintaining reliability. Simultaneously, researchers are developing more realistic benchmarks that account for cultural diversity, long-horizon tasks, and native runtime environments. The surveyed papers collectively suggest that effective agent evaluation requires balancing scalability with authenticity, and that multi-agent frameworks with human-in-the-loop mechanisms offer promising paths forward.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "agent evaluation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Automation of the Evaluation Process

A significant research direction focuses on automating agent evaluation to reduce reliance on human annotators. Zhou et al. (2026) introduced EvalAgent, which encodes evaluation domain expertise as procedural skills, achieving a dramatic improvement in first-run execution success from 17.5% to 65%. Their work demonstrates that simply prompting coding assistants is insufficient, as frontier models tend to produce over-engineered evaluations without domain-specific knowledge. Similarly, Wang et al. (2026) proposed DeepResearchEval, which automates both task construction and evaluation through a persona-driven pipeline and active fact-checking mechanism that verifies statements via web search without requiring citations. Gan et al. (2026) addressed the certification problem, asking what fraction of evaluation can be safely automated with guaranteed error bounds. Their task-level bootstrap certificate achieves 30-59% certified coverage at a 10% error budget, revealing that standard i.i.d. certificates dangerously overstate safe automation rates.

### Theme 2: User Simulation for Dynamic Evaluation

Rather than static benchmarks, several papers advocate for user simulation approaches that capture the interactive, multi-turn nature of agent behavior. Lu et al. (2026) proposed VISTA, a toolkit with six metrics for measuring realism and capability coverage of simulated interactions. Their hybrid simulator integrates both UI-based and API-based interactions, addressing the limitation of frameworks restricted to单一 interaction modes. Shea et al. (2025) introduced SAGE, which grounds user simulation in domain-specific knowledge through top-down customer profiles and bottom-up product catalogs. Their framework identifies 33% more agent errors than generic simulators, demonstrating that business-context grounding significantly improves evaluation sensitivity. Both papers emphasize that realistic user behavior modeling requires moving beyond scripted interactions toward dynamic, knowledge-grounded simulations.

### Theme 3: Realistic Benchmark Design

A third theme emphasizes creating benchmarks that reflect real-world complexity rather than simplified sandbox environments. Ding et al. (2026) created WildClawBench, featuring 60 human-authored tasks running in reproducible Docker containers with actual CLI tools and real environments. Their finding that even the best model (Claude Opus 4.7) achieved only 62.2% success rate reveals that long-horizon, native-runtime agent evaluation remains unsolved. Almeida et al. (2025) addressed cultural and linguistic diversity with Ticket-Bench, simulating soccer ticket purchases across six languages with localized content. Their work exposes notable cross-lingual performance disparities even in top models, challenging the monolingual bias prevalent in existing benchmarks. Both benchmarks share a commitment to authenticity: WildClawBench through native runtime environments, Ticket-Bench through genuine multilingual and regional content.

### Theme 4: Multi-Agent Evaluation Frameworks

Several papers explore multi-agent dynamics in evaluation, recognizing that evaluation itself can benefit from agent collaboration and disagreement. Yang et al. (2026) proposed JuryFlow, which treats inter-judge disagreement as a signal for uncertainty rather than noise. Their framework decomposes responses into atomic claims, builds disagreement graphs scored by verdict entropy, and uses minimal human intervention to resolve focal disagreements. Choi et al. (2026) systematically analyzed authority bias in multi-agent evaluation, finding that expert and referent power roles exert stronger influence than legitimate power roles. Zhang et al. (2025) introduced DITING for web novel translation evaluation, combining expert-annotated dimensions with AgentEval, a reasoning-driven multi-agent framework that achieves the highest correlation with human judgments among tested metrics. These works collectively suggest that heterogeneous judge ensembles with structured disagreement resolution outperform single-judge approaches.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, there is broad agreement that static benchmarks are insufficient for capturing dynamic, multi-step agentic behavior (Lu et al., 2026; Ding et al., 2026). Second, multiple papers emphasize that automation without domain-specific knowledge produces suboptimal results (Zhou et al., 2026; Wang et al., 2026). Third, there is consensus that evaluation frameworks must account for diversity—whether linguistic (Almeida et al., 2025), cultural (Almeida et al., 2025), or interaction modality (Lu et al., 2026). Finally, several papers agree that human involvement remains critical, whether for certification (Gan et al., 2026), disagreement resolution (Yang et al., 2026), or preference evaluation (Zhou et al., 2026).

**Disagreements**: The literature shows less explicit disagreement, partly because papers target different evaluation contexts. However, there is tension between the automation-focused papers (Zhou et al., 2026; Wang et al., 2026; Gan et al., 2026) and the realism-focused papers (Ding et al., 2026; Almeida et al., 2025) regarding the primary bottleneck: whether evaluation scalability or evaluation authenticity is the more pressing challenge. Additionally, while JuryFlow (Yang et al., 2026) treats disagreement as informative, the certification approach of Gan et al. (2026) seeks to minimize uncertainty through statistical guarantees, representing different philosophical stances on handling evaluator disagreement.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, multiple papers note limitations in generalizability: WildClawBench focuses on CLI-based harnesses (Ding et al., 2026), DITING targets Chinese-English translation (Zhang et al., 2025), and Ticket-Bench covers six major languages but excludes many others (Almeida et al., 2025). Second, the certification work by Gan et al. (2026) reveals that finite-sample alternatives certify nothing at realistic task counts, indicating a fundamental limitation in current certification approaches. Third, several papers do not state limitations in their abstracts, suggesting either space constraints or insufficient self-critical analysis. Fourth, the authority bias study by Choi et al. (2026) focused on 12-turn conversations, leaving open questions about longer or more complex multi-agent interactions. Finally, there is a notable gap in cross-benchmark validation: no paper systematically compares their framework against multiple competing approaches on shared tasks, making it difficult to assess relative merits.

## Per-Paper Annotations

### Almeida et al. (2025)

**Research question**: How can agent evaluation benchmarks better account for cultural and linguistic diversity in multilingual, task-oriented scenarios?
**Methodology**: Introduced Ticket-Bench, a benchmark simulating soccer ticket purchases across six languages using localized teams, cities, and user profiles, evaluating commercial and open-source LLMs by measuring function-calling accuracy and consistency.
**Key findings**:
- Existing agent evaluations largely overlook cultural and linguistic diversity, often relying on monolingual or naively translated benchmarks
- Reasoning-oriented models dominate performance in multilingual function-calling tasks
- Even top models exhibit notable cross-lingual disparities in performance
- Ticket-Bench provides higher realism through localized content across six major languages
**Limitations**: Not stated in abstract

### Choi et al. (2026)

**Research question**: How does role-based authority bias affect agent interactions in free-form multi-agent evaluation frameworks?
**Methodology**: Systematic analysis using ChatEval across 12-turn conversations, applying French and Raven's power-based theory to classify authoritative roles into legitimate, referent, and expert types.
**Key findings**:
- Expert and referent power roles exert stronger influence than legitimate power roles
- Authority bias emerges through authoritative roles maintaining positions while general agents demonstrate flexibility
- Authority influence requires clear position statements; neutral responses fail to generate bias
- First systematic analysis of role-based authority bias in multi-agent evaluation
**Limitations**: Focuses on 12-turn conversations; may not capture dynamics in longer or more complex interactions

### Ding et al. (2026)

**Research question**: Whether AI agents can complete realistic long-horizon work in native runtime environments rather than synthetic sandboxes.
**Methodology**: Created WildClawBench with 60 human-authored, bilingual, multimodal tasks in reproducible Docker containers with actual CLI agent harnesses and real tools, using hybrid deterministic and LLM/VLM grading.
**Key findings**:
- Best model achieved only 62.2% overall success rate under OpenClaw harness
- All other tested models scored below 60%
- Switching agent harness alone can shift performance by up to 18 percentage points
- Tasks average roughly 8 minutes of wall-clock time and over 20 tool calls each
**Limitations**: Focuses on CLI-based harnesses; may not generalize to other interaction paradigms; hybrid grading requires careful calibration

### Gan et al. (2026)

**Research question**: What fraction of agent evaluation can an automatic judge take over with a certificate guaranteeing the error rate stays below a specified budget?
**Methodology**: Introduced task-level bootstrap certificate valid under correlated trajectory clusters, trained 4B logprob judge using SFT and reject-weighted GRPO, evaluated certified coverage at alpha=0.1 error budget.
**Key findings**:
- Standard i.i.d. certificates overstate safe automation, claiming 98% while realized error exceeds budget in 17.5% of resamples
- Task-level bootstrap certificate certifies 0.30-0.59 of evaluation on tool-use and web corpora
- Certified coverage predictable before training from base rate and discrimination alone
- Certificate serves as self-training filter with contamination bounded by alpha
**Limitations**: Finite-sample cluster-valid alternatives certify nothing at realistic task counts

### Lu et al. (2026)

**Research question**: How can user-simulation-based evaluation better capture the dynamic, multi-step nature of agentic behavior and expose meaningful failure modes?
**Methodology**: Proposed VISTA toolkit with six metrics for measuring realism, capability coverage, and interaction effectiveness; developed hybrid user simulator integrating UI-based and API-based interactions.
**Key findings**:
- Existing evaluation methods rely on static benchmarks failing to capture dynamic, multi-step agentic behavior
- Current user simulation frameworks provide limited mechanisms for evaluating quality and comprehensiveness
- Most frameworks restricted to either UI-only or API-only actions
- VISTA produces more realistic and comprehensive evaluations in e-commerce and customer service settings
**Limitations**: Not stated in abstract

### Shea et al. (2025)

**Research question**: How can user simulation for multi-turn agent evaluation be improved by incorporating domain-specific knowledge from business contexts?
**Methodology**: Proposed SAGE framework integrating top-down knowledge (customer profiles, business logic) and bottom-up knowledge (product catalogs, FAQs, knowledge bases) to generate realistic user interactions.
**Key findings**:
- SAGE produces interactions more realistic and diverse compared to existing approaches
- Framework identifies up to 33% more agent errors than generic user simulators
- Top-down knowledge grounds user behavior in realistic customer personas
- Bottom-up knowledge allows simulator to reflect users' information needs and expectations
**Limitations**: Not stated in abstract

### Wang et al. (2026)

**Research question**: How can deep research systems be evaluated automatically without requiring annotation-intensive task construction or reliable citations?
**Methodology**: Introduced DeepResearchEval with persona-driven pipeline for generating research tasks using two-stage filter, and agentic evaluation pipeline with adaptive point-wise quality evaluation and active fact-checking via web search.
**Key findings**:
- Addresses gaps in existing benchmarks: annotation-intensive construction, static dimensions, unreliable fact verification
- Persona-driven pipeline generates diverse, complex research tasks anchored in user profiles
- Two-stage filter retains only tasks requiring multi-source evidence integration and external retrieval
- Active fact-checking autonomously verifies statements via web search without requiring citations
**Limitations**: Not stated in abstract

### Yang et al. (2026)

**Research question**: How can inter-judge disagreement in multi-agent evaluation be leveraged as a signal for uncertainty rather than discarded as noise?
**Methodology**: JuryFlow decomposes responses into atomic claims, has heterogeneous judges assign per-claim verdicts, builds disagreement graph scored by verdict entropy, uses human as structural guide to select which disagreement to resolve.
**Key findings**:
- Improves agreement with gold labels over single-judge and majority-vote panel baselines
- Treating disagreement as claim-level signal enables precise identification of evaluation uncertainty
- Human acts as structural guide selecting which disagreement to resolve rather than re-labeling entire responses
- Corrections propagate along graph edges and to historically similar cases, making evaluator self-refining
**Limitations**: Automatic configuration uses entropy ranking, which may not always identify most impactful disagreements

### Zhang et al. (2025)

**Research question**: How can machine translation quality for web novels be evaluated beyond surface-level metrics to capture narrative and cultural fidelity?
**Methodology**: Introduced DITING framework assessing six dimensions with over 18K expert-annotated Chinese-English sentence pairs, plus AgentEval multi-agent evaluation framework and MetricAlign meta-evaluation dataset.
**Key findings**:
- AgentEval achieves highest correlation with human judgments among seven tested automatic metrics
- Chinese-trained LLMs surpass larger foreign counterparts in web novel translation quality
- DeepSeek-V3 delivers most faithful and stylistically coherent translations
- Existing benchmarks relying on surface-level metrics fail to capture distinctive traits of web novel genre
**Limitations**: Focuses on Chinese-English web novel translation; may require adaptation for other language pairs or literary genres

### Zhou et al. (2026)

**Research question**: Can frontier coding assistants reliably automate the agent evaluation process?
**Methodology**: Introduced EvalAgent that encodes evaluation domain expertise as evaluation skills to automate end-to-end agent evaluation pipeline; evaluated using meta-evaluation framework with AgentEvalBench and proposed Eval@1 metric.
**Key findings**:
- Simply prompting coding assistants achieves only 30% execution success rate
- Frontier coding assistants produce over-engineered evaluations averaging 12+ metrics without domain knowledge
- EvalAgent improves Eval@1 from 17.5% to 65% using evaluation skills
- EvalAgent achieves 79.5% human expert preference over baseline approaches
- Removing evaluation skills causes Eval@1 to drop from 65% to 30%
**Limitations**: Not stated in abstract

## References

Almeida, T. S., Santos, J. G. A., Laitz, T., & Bonás, G. K. (2025). Ticket-Bench: A kickoff for multilingual and regionalized agent evaluation. arXiv. https://arxiv.org/abs/2509.14477

Choi, J., Kwon, J., Kim, H., Cho, H., Jung, H., Min, S., & Kim, B. (2026). Belief in authority: Impact of authority in multi-agent evaluation framework. arXiv. https://arxiv.org/abs/2601.04790

Ding, S., Dai, X., Xing, L., Ding, S., Liu, Z., JingYi, Y., Yang, P., Zhang, Z., Wei, X., Fang, X., Ma, Y., Duan, H., Shao, J., Wang, J., Lin, D., Chen, K., & Zang, Y. (2026). WildClawBench: A benchmark for real-world, long-horizon agent evaluation. arXiv. https://arxiv.org/abs/2605.10912

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Lu, Y., Shea, R., Zhang, Y., & Yu, Z. (2026). VISTA: A versatile interactive user simulation toolkit for agent evaluation. arXiv. https://arxiv.org/abs/2606.11079

Shea, R., Lu, Y., Qiu, L., & Yu, Z. (2025). SAGE: A top-down bottom-up knowledge-grounded user simulator for multi-turn agent evaluation. arXiv. https://arxiv.org/abs/2510.11997

Wang, Y., Wang, L., Deng, Y., Wu, K., Xiao, Y., Yao, H., Kang, L., Ye, H., Jing, Y., & Bing, L. (2026). DeepResearchEval: An automated framework for deep research task construction and agentic evaluation. arXiv. https://arxiv.org/abs/2601.09688

Yang, M., Yu, J., & Ding, Y. (2026). JuryFlow: Disagreement-guided human-in-the-loop multi-agent evaluation. arXiv. https://arxiv.org/abs/2609.40103

Zhang, E., Wang, J., Xiao, M., Liu, J., Kuang, Z., Dong, R., Dong, E., Ananiadou, S., Peng, M., & Xie, Q. (2025). DITING: A multi-agent evaluation framework for benchmarking web novel translation. arXiv. https://arxiv.org/abs/2510.09116

Zhou, K., Woo, S., Ding, H., Ramnath, K., Chidambaram, S., Feng, A., Arannil, V., Kim, M., Singh, I., Wang, D., Xu, Z., Gandhi, M., Prabhu, N., Mishra, S. S., Dhakecha, S., Singh, V., Pandeshwar, G., Cheong, L. L., & et al. (2026). An empirical study of automating agent evaluation. arXiv. https://arxiv.org/abs/2605.11378
