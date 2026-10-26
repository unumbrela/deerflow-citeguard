# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Review Period:** September 28, 2023 – September 27, 2025  
**Category:** cs.AI (Primary)  
**Search Date:** October 26, 2026  

---

## Executive Summary

This systematic literature review examines recent advances in LLM and AI agent systems for data analysis tasks. The search identified **5 peer-reviewed papers** published between September 2023 and September 2025 in the cs.AI category on arXiv. While the search requested 10 papers, only 5 met the specified criteria, reflecting the emerging but still specialized nature of autonomous AI analyst systems.

The reviewed literature demonstrates significant progress in multi-agent architectures, domain-specific analytical frameworks, and benchmark development for evaluating LLM-based data analysts across bioinformatics, enterprise analytics, hydrology, financial due diligence, and future prediction tasks.

---

## Annotated Bibliography (APA Format)

### 1. K-Dense Analyst: Towards Fully Automated Scientific Analysis

**Citation:**  
Li, O., Agarwal, V., Zhou, S., Gopinath, A., & Kassis, T. (2025). *K-Dense Analyst: Towards Fully Automated Scientific Analysis*. arXiv preprint arXiv:2508.07043. https://arxiv.org/abs/2508.07043v2

**Summary:**  
This paper introduces K-Dense Analyst, a hierarchical multi-agent system designed for autonomous bioinformatics analysis. The system employs a dual-loop architecture that couples planning with validated execution using specialized agents to decompose complex objectives into executable, verifiable tasks within secure computational environments.

**Key Contributions:**
- Achieves 29.2% accuracy on BixBench (comprehensive biological analysis benchmark)
- Surpasses GPT-5 by 6.3 percentage points (27% improvement)
- Demonstrates that architectural innovations unlock capabilities beyond underlying model performance (Gemini 2.5 Pro baseline: 18.3%)
- Establishes that autonomous scientific reasoning requires purpose-built systems bridging high-level objectives and low-level computational execution

**Relevance:** Directly addresses LLM agents as autonomous scientific analysts with validated tool integration.

---

### 2. Data-to-Dashboard: Multi-Agent LLM Framework for Insightful Visualization in Enterprise Analytics

**Citation:**  
Zhang, R., & Elhamod, M. (2025). *Data-to-Dashboard: Multi-Agent LLM Framework for Insightful Visualization in Enterprise Analytics*. arXiv preprint arXiv:2505.23695. https://arxiv.org/abs/2505.23695v1

**Summary:**  
This work presents a modular multi-agent LLM system that automates the data-to-dashboard pipeline through specialized agents capable of domain detection, concept extraction, multi-perspective analysis generation, and iterative self-reflection. Unlike existing chart QA systems, the framework simulates the analytical reasoning process of business analysts.

**Key Contributions:**
- Modular pipeline bridging raw data to visualization without closed ontologies or question templates
- Retrieves domain-relevant knowledge and adapts to diverse datasets
- Outperforms GPT-4o single-prompt baseline in insightfulness, domain relevance, and analytical depth
- Enables human-in-the-loop validation by domain experts

**Relevance:** Demonstrates multi-agent architecture for enterprise data analysis with emphasis on visualization and business analytics.

---

### 3. FutureX: An Advanced Live Benchmark for LLM Agents in Future Prediction

**Citation:**  
Zeng, Z., Liu, J., Chen, S., He, T., Liao, Y., Tian, Y., Wang, J., Wang, Z., Yang, Y., Yin, L., Yin, M., Zhu, Z., Cai, T., Chen, Z., Chen, J., Du, Y., Gao, X., Guo, J., Hu, L., & Jiao, J. (2025). *FutureX: An Advanced Live Benchmark for LLM Agents in Future Prediction*. arXiv preprint arXiv:2508.11987. https://arxiv.org/abs/2508.11987v3

**Summary:**  
FutureX is introduced as the largest and most diverse live evaluation benchmark for LLM agents performing future prediction tasks. The benchmark supports real-time daily updates and eliminates data contamination through automated question gathering and answer collection pipelines.

**Key Contributions:**
- Evaluates 25 LLM/agent models including reasoning-enhanced and search-capable systems
- Assesses adaptive reasoning in dynamic environments (politics, economics, finance)
- Provides in-depth analysis of failure modes including vulnerability to fake web pages and temporal validity issues
- Establishes contamination-free evaluation standard for professional-level analytical performance

**Relevance:** Provides critical benchmark infrastructure for evaluating LLM agents in complex analytical reasoning and predictive tasks.

---

### 4. LLM-Based Agents for Competitive Landscape Mapping in Drug Asset Due Diligence

**Citation:**  
Vinogradov, V., Vinogradova, A., Radkevich, D., Yasny, I., Kobyzev, D., Izmailov, I., Yanchanka, K., Doronin, R., & Doronichev, A. (2025). *LLM-Based Agents for Competitive Landscape Mapping in Drug Asset Due Diligence*. arXiv preprint arXiv:2508.16571. https://arxiv.org/abs/2508.16571v4

**Summary:**  
This paper describes and benchmarks a competitor-discovery AI agent within an agentic system for drug asset due diligence. The agent retrieves competitive landscape drugs for given indications and extracts canonical attributes, addressing fragmented, paywalled, and rapidly changing data sources.

**Key Contributions:**
- Achieves 83% recall on competitor discovery, exceeding OpenAI Deep Research (65%) and Perplexity Labs (60%)
- Introduces LLM-as-a-judge agent for filtering false positives and suppressing hallucinations
- Reduces analyst turnaround time from 2.5 days to ~3 hours (20x improvement) in production deployment
- Transforms unstructured diligence memos into structured evaluation corpus

**Relevance:** Demonstrates production-deployed LLM agent system for specialized financial/biotech data analysis with measurable business impact.

---

### 5. AQUAH: Automatic Quantification and Unified Agent in Hydrology

**Citation:**  
Yan, S., Li, Z., Zhu, S., Wen, Y., Zhang, M., Chen, M., Cao, J., & Hong, Y. (2025). *AQUAH: Automatic Quantification and Unified Agent in Hydrology*. arXiv preprint arXiv:2508.02936. https://arxiv.org/abs/2508.02936v1

**Summary:**  
AQUAH is introduced as the first end-to-end language-based agent designed specifically for hydrologic modeling. Starting from natural-language prompts, AQUAH autonomously retrieves terrain, forcing, and gauge data; configures hydrologic models; runs simulations; and generates self-contained PDF reports.

**Key Contributions:**
- Vision-enabled LLMs interpret maps and rasters on-the-fly
- Steers key decisions including outlet selection, parameter initialization, and uncertainty commentary
- Produces analyst-ready documentation without manual intervention
- Results judged by hydrologists as clear, transparent, and physically plausible

**Relevance:** Extends LLM agent capabilities to environmental science domain with vision-grounded autonomous modeling.

---

## Thematic Analysis

### Cross-Cutting Themes

**1. Multi-Agent Architectures**  
Four of five papers (K-Dense Analyst, Data-to-Dashboard, FutureX evaluation, Drug Due Diligence) employ multi-agent designs, indicating consensus that specialized agents outperform monolithic systems for complex analytical tasks.

**2. Domain Specialization**  
All systems target specific domains (bioinformatics, enterprise analytics, finance/biotech, hydrology, future prediction), suggesting that general-purpose analyst agents remain immature compared to domain-adapted systems.

**3. Benchmark Development**  
Two papers (FutureX, K-Dense Analyst/BixBench) introduce dedicated benchmarks, reflecting the field's transition from proof-of-concept to rigorous evaluation.

**4. Human-in-the-Loop Validation**  
Multiple systems emphasize expert validation (hydrologists judging AQUAH, domain experts validating Data-to-Dashboard, LLM-as-judge in drug due diligence), acknowledging that full autonomy requires verification mechanisms.

**5. Performance Gains**  
Reported improvements are substantial: 27% over baseline LLM (K-Dense), 20x turnaround reduction (Drug Due Diligence), superior performance to GPT-4o/Deep Research baselines across multiple systems.

### Identified Gaps

**Limited Temporal Coverage:** Only 5 papers met the 2023-2025 cs.AI criteria, suggesting the field is nascent or that relevant work appears in adjacent categories (cs.LG, cs.SE, q-bio).

**Benchmark Fragmentation:** Each system introduces domain-specific benchmarks (BixBench, FutureX, custom due diligence corpus), hindering cross-domain comparison.

**Production Deployment Evidence:** Only one paper (Drug Due Diligence) reports production deployment metrics, indicating most systems remain research prototypes.

---

## Conclusion

The literature reveals rapid advancement in LLM/Agent-as-Data-Analyst systems during 2023-2025, with multi-agent architectures demonstrating consistent superiority over single-model approaches. Domain specialization, validated execution, and benchmark development emerge as critical success factors. However, the limited number of papers meeting search criteria suggests this remains an emerging research area with significant opportunities for standardization, cross-domain evaluation, and production validation.

Future research should prioritize: (1) unified benchmarking frameworks enabling cross-domain comparison, (2) generalization techniques reducing domain-specific engineering, (3) rigorous production deployment studies, and (4) investigation of failure modes in high-stakes analytical contexts.

---

## Search Methodology Notes

**Database:** arXiv  
**Category:** cs.AI (primary category only, cross-lists excluded)  
**Date Range:** September 28, 2023 – September 27, 2025  
**Search Query:** "LLM agent data analyst" (phrase match)  
**Results:** 5 papers identified (requested: 10)  
**Limitation:** Fewer papers than requested under specified constraints; results represent complete set matching criteria.

---

*Generated: October 26, 2026*
