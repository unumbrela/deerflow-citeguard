# Systematic Literature Review: Deep Research

**Date:** October 27, 2026

**Search Parameters:**
- **Topic:** Deep Research
- **Category:** cs.CL (Computational Linguistics)
- **Publication Window:** November 24, 2023 – November 23, 2025
- **Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Deep Research—a rapidly emerging field focused on enabling large language models (LLMs) to autonomously conduct multi-step web exploration, targeted retrieval, and higher-order synthesis to produce comprehensive research outputs. The reviewed literature reveals five major themes: (1) benchmarking frameworks for evaluating deep research capabilities, (2) architectural innovations for autonomous information-seeking, (3) reinforcement learning-based training methodologies, (4) reasoning patterns that enable superhuman performance, and (5) evaluation frameworks for assessing research quality.

Key findings indicate that proprietary systems like OpenAI DeepResearch and Gemini-2.5-Pro DeepResearch currently lead the field, achieving 42.9% accuracy on BrowseComp-ZH [citation:Zhou et al., 2025, E20] and demonstrating comparable performance on PhD-level research tasks [citation:Du et al., 2025, E31]. The literature consistently emphasizes that deep research capabilities require sophisticated reasoning patterns that systematically reduce uncertainty across vast information landscapes [citation:Li et al., 2025a, E15], multi-turn retrieval strategies [citation:Zhou et al., 2025, E21], and specialized training paradigms combining supervised fine-tuning with reinforcement learning [citation:Wu et al., 2025a, E2; Jin et al., 2025, E17].

---

## 1. Introduction

Deep Research Agents (DRAs) represent a prominent category of LLM-based agents that autonomously orchestrate multistep web exploration, targeted retrieval, and higher-order synthesis to transform vast amounts of online information into analyst-grade, citation-rich reports [citation:Du et al., 2025, E28]. This capability addresses critical limitations of traditional retrieval-augmented generation (RAG) systems, which may retrieve shallow content and struggle with complex, multi-layered information [citation:Wu et al., 2025b, E25].

The field has evolved rapidly, with recent work focusing on three interconnected challenges: (1) developing challenging benchmarks that accurately measure deep research capabilities, (2) designing training methodologies that instill sophisticated reasoning patterns, and (3) creating evaluation frameworks that align with human expert judgment. This review synthesizes findings from 10 papers published between 2023 and 2025 in the cs.CL category, providing a comprehensive overview of the current state of deep research systems.

---

## 2. Benchmarking Deep Research Capabilities

### 2.1 BrowseComp: Measuring Web Browsing Persistence

Wei et al. (2025) introduced BrowseComp, a benchmark comprising 1,266 questions that require persistently navigating the internet to find hard-to-find, entangled information [citation:Wei et al., 2025]. The benchmark is designed to measure agents' core capabilities in exercising persistence and creativity in finding information, analogous to how programming competitions serve as useful benchmarks for coding agents.

Key characteristics of BrowseComp include:
- **Short, verifiable answers** that enable easy grading
- **High difficulty** requiring creative search strategies
- **Focus on core browsing capabilities** rather than long-form generation

OpenAI's Deep Research system significantly outperforms other models on BrowseComp, solving approximately half of the problems through autonomous web search and information synthesis [citation:Wei et al., 2025]. This performance demonstrates the importance of sophisticated reasoning patterns that systematically reduce uncertainty when navigating vast information landscapes [citation:Li et al., 2025a].

### 2.2 BrowseComp-ZH: Chinese-Language Web Browsing

Zhou et al. (2025) addressed a critical gap in benchmarking by introducing BrowseComp-ZH, a high-difficulty benchmark for evaluating LLM agents on the Chinese web [citation:Zhou et al., 2025, E19]. The benchmark consists of 289 multi-hop questions spanning 11 diverse domains, each reverse-engineered from short, objective, and easily verifiable answers [citation:Zhou et al., 2025, E20].

The benchmarking results reveal significant challenges: most models achieve accuracy rates below 10%, with only a handful exceeding 20% [citation:Zhou et al., 2025, E20]. Notably, OpenAI's DeepResearch achieved the best performance at 42.9%, demonstrating that multi-turn retrieval systems significantly outperform standalone models [citation:Zhou et al., 2025, E21]. This finding underscores the value of iterative retrieval strategies in deep research contexts.

The reverse construction approach—crafting queries from answers rather than answers from queries—ensures high retrieval difficulty and answer uniqueness [citation:Zhou et al., 2025, E19]. This methodology has become influential in subsequent benchmark development.

### 2.3 WebWalkerQA: Evaluating Web Traversal

Wu et al. (2025b) introduced WebWalkerQA, a benchmark designed to assess LLMs' ability to perform web traversal rather than shallow search [citation:Wu et al., 2025b, E25]. The benchmark evaluates the capacity of LLMs to systematically traverse a website's subpages to extract high-quality data through horizontal and vertical integration.

Key insights from WebWalkerQA include:
- **Vertical exploration** within web pages is identified as a promising direction for scaling inference time in RAG systems [citation:Wu et al., 2025b, E26]
- **Multi-agent frameworks** with explorer and critic agents employing Thought-Action-Observation paradigms demonstrate effectiveness [citation:Wu et al., 2025b, E27]
- **Incremental information accumulation** through critic agent memory enables better decision-making about when sufficient data has been gathered [citation:Wu et al., 2025b, E33]

### 2.4 DeepResearch Bench: PhD-Level Research Tasks

Du et al. (2025) presented DeepResearch Bench, the most comprehensive benchmark for evaluating Deep Research Agents [citation:Du et al., 2025, E28]. The benchmark comprises 100 PhD-level research tasks across 22 distinct fields, each meticulously crafted by domain experts [citation:Du et al., 2025, E29].

The evaluation methodology introduces two novel frameworks:
- **RACE (Reference-based Adaptive Criteria Evaluation):** Generates task-specific criteria and weights dynamically using LLM-as-a-Judge to assess research report quality [citation:Du et al., 2025, E30]
- **FACT (Factual Accuracy and Citation Test):** Evaluates information retrieval capabilities through citation accuracy and factual grounding assessment [citation:Du et al., 2025, E31]

Benchmarking results show that OpenAI DeepResearch and Gemini-2.5-Pro DeepResearch demonstrate comparable leading performance among evaluated DRAs [citation:Du et al., 2025, E29]. The benchmark's expert-crafted tasks provide a more realistic assessment of deep research capabilities than simpler question-answering benchmarks.

---

## 3. Architectural Innovations for Deep Research

### 3.1 WebThinker: Empowering Large Reasoning Models

Li et al. (2025b) proposed WebThinker, a deep research agent that empowers large reasoning models (LRMs) to autonomously search the web, navigate among web pages, and draft reports during the reasoning process [citation:Li et al., 2025b, E10]. The system addresses a critical limitation of LRMs like OpenAI-o1 and DeepSeek-R1: their reliance on static internal knowledge limits performance on complex, knowledge-intensive tasks.

WebThinker introduces three key innovations:

**Deep Web Explorer Module:** Enables LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps [citation:Li et al., 2025b, E10]. This module integrates seamlessly with the reasoning process, allowing the model to acquire external knowledge in real-time.

**Autonomous Think-Search-and-Draft Strategy:** Allows the model to seamlessly interleave reasoning, information gathering, and report writing [citation:Li et al., 2025b, E11]. This approach mirrors human research workflows, where thinking, searching, and writing occur concurrently rather than sequentially.

**RL-based Training via Iterative Online DPO:** Enhances research tool utilization by optimizing end-to-end task performance through Direct Preference Optimization [citation:Li et al., 2025b, E12]. This training strategy ensures that the model learns to effectively leverage search and navigation tools.

Extensive experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate that WebThinker significantly outperforms existing methods and strong proprietary systems [citation:Li et al., 2025b, E10].

### 3.2 Search-R1: Retrieval-Interleaved Reasoning

Jin et al. (2025) introduced Search-R1, an extension of reinforcement learning for reasoning frameworks where LLMs learn to autonomously generate multiple search queries during step-by-step reasoning with real-time retrieval [citation:Jin et al., 2025, E13]. The system addresses the suboptimal performance of prompting advanced LLMs to use search engines during inference, as LLMs may not possess the capability to interact optimally with search engines.

Search-R1's key technical contributions include:

**Retrieval-Interleaved Reasoning:** Enables LLMs to generate search queries autonomously during the reasoning process, with real-time retrieval integrated into the reasoning trajectory [citation:Jin et al., 2025, E13].

**Retrieved Token Masking:** Ensures stable RL training by computing policy gradient objectives only over LLM-generated tokens, excluding retrieved content from optimization [citation:Jin et al., 2025, E14]. This technique prevents the model from being penalized or rewarded for retrieved content it did not generate.

**Outcome-based Reward Function:** Uses simple outcome-based rewards rather than complex reward engineering, demonstrating that RL can effectively optimize multi-turn search interactions [citation:Jin et al., 2025, E14].

Experiments on seven question-answering datasets show that Search-R1 improves performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines under the same setting [citation:Jin et al., 2025, E17]. These results demonstrate the effectiveness of RL-based training for retrieval-augmented reasoning.

### 3.3 WebSailor: Superhuman Reasoning for Web Agents

Li et al. (2025a) introduced WebSailor, a complete post-training methodology designed to instill sophisticated reasoning patterns that enable superhuman performance on complex information-seeking tasks [citation:Li et al., 2025a, E15]. The work is motivated by the observation that proprietary systems like DeepResearch have demonstrated superhuman capabilities on benchmarks like BrowseComp—a feat previously unattainable.

WebSailor's approach is based on a key insight: success on complex information-seeking tasks hinges on the ability to systematically reduce extreme uncertainty when navigating vast information landscapes [citation:Li et al., 2025a, E15]. This reasoning pattern is absent in open-source models.

The methodology includes:

**Structured Sampling and Information Obfuscation:** Generates novel, high-uncertainty tasks that force the model to develop uncertainty reduction capabilities [citation:Li et al., 2025a, E16].

**RFT Cold Start:** Uses reinforcement fine-tuning to provide an initial capability base before full RL training [citation:Li et al., 2025a, E16].

**Duplicating Sampling Policy Optimization (DUPO):** An efficient agentic RL training algorithm that achieves 2-3 times speedup over dynamic sampling approaches [citation:Li et al., 2025a, E18]. This efficiency gain makes large-scale training more practical.

With this integrated pipeline, WebSailor significantly outperforms all open-source agents in complex information-seeking tasks, matching proprietary agents' performance and closing the capability gap [citation:Li et al., 2025a, E15].

### 3.4 WebDancer: End-to-End Agentic Information Seeking

Wu et al. (2025a) presented WebDancer, a cohesive paradigm for building end-to-end agentic information seeking agents from a data-centric and training-stage perspective [citation:Wu et al., 2025a, E1]. The approach consists of four key stages:

1. **Browsing Data Construction:** Creating high-quality training data for information-seeking tasks
2. **Trajectories Sampling:** Generating diverse reasoning trajectories for training
3. **Supervised Fine-Tuning for Cold Start:** Providing initial capability through SFT
4. **Reinforcement Learning for Enhanced Generalization:** Improving performance through RL

The framework uses the ReAct paradigm, tightly coupling reasoning with action to facilitate effective learning and generalization in interactive settings [citation:Wu et al., 2025a, E2]. Two data synthesis strategies are proposed:

- **crawlQA:** Crawls web pages to construct deep queries
- **e2hQA:** Synthesizes easy-to-hard QA pairs to incentivize progression from weak-to-strong agency

Empirical evaluations on GAIA and WebWalkerQA demonstrate strong performance, with the best-performing model reaching Pass@3 scores of 64.1% on GAIA and 62.0% on WebWalkerQA [citation:Wu et al., 2025a, E3]. Notably, SFT for cold start is essential—RL-only training achieved only 5% Pass@3 on GAIA, demonstrating the necessity of the two-stage training pipeline [citation:Wu et al., 2025a, E2].

### 3.5 WebResearcher: Iterative Deep Research Paradigm

Qiao et al. (2025) introduced WebResearcher, a novel framework that addresses critical limitations of existing deep research approaches [citation:Qiao et al., 2025]. The system is built on two key components:

**IterResearch Paradigm:** Reformulates deep research as a Markov Decision Process with periodic state reconstruction [citation:Qiao et al., 2025, E4]. This approach overcomes two critical limitations of mono-contextual approaches:

1. **Cognitive Workspace Suffocation:** As context accumulates, the model's ability to reason effectively diminishes
2. **Irreversible Noise Contamination:** Irrelevant or low-quality information persists in context, degrading performance

**WebFrontier Data Synthesis Engine:** Generates high-quality training data through tool-augmented complexity escalation [citation:Qiao et al., 2025, E5]. This enables systematic creation of research tasks that bridge the gap between passive knowledge recall and active knowledge construction. The system uses Knowledge Projections (KP) as the basic unit in information-seeking task formalization, enabling precise control over reasoning structures [citation:Qiao et al., 2025, E32].

The iterative paradigm naturally scales through parallel thinking, enabling concurrent multi-agent exploration for more comprehensive conclusions [citation:Qiao et al., 2025, E4]. Extensive experiments across 6 challenging benchmarks demonstrate that WebResearcher achieves state-of-the-art performance, surpassing frontier proprietary systems [citation:Qiao et al., 2025, E6].

Ablation studies reveal that the iterative paradigm itself—not just the training data—is the critical driver of performance, with WebResearcher outperforming Mono-Agent + Iter by 3.4 points on HLE (28.8 vs. 25.4) [citation:Qiao et al., 2025, E6].

---

## 4. Training Methodologies for Deep Research Agents

### 4.1 Formalization-Driven Data Synthesis

Tao et al. (2025) proposed WebShaper, a formalization-driven information-seeking (IS) data synthesis framework that addresses limitations of existing information-driven approaches [citation:Tao et al., 2025]. Traditional approaches first collect web data and then generate questions based on the retrieval, which may lead to inconsistency between information structure and reasoning structure.

WebShaper's key innovations include:

**Knowledge Projections (KP):** Basic units in information-seeking task formalization that enable precise control over reasoning structures through KP operation compositions [citation:Tao et al., 2025, E22]. This formalization provides a rigorous foundation for data synthesis.

**Layer-wise Expansion Strategy:** Reduces redundancy and prevents reasoning shortcuts during data synthesis [citation:Tao et al., 2025, E23]. This strategy ensures that synthesized tasks maintain appropriate complexity levels.

**Agentic Expander:** Uses retrieval and validation tools to expand formal questions into more complex variants based on the formalization [citation:Tao et al., 2025, E23].

The framework represents a paradigm shift from reactive information organization to proactive task specification [citation:Tao et al., 2025, E22]. Experiment results demonstrate that WebShaper achieves state-of-the-art performance among open-sourced IS agents on GAIA and WebWalkerQA benchmarks [citation:Tao et al., 2025, E24].

### 4.2 Reinforcement Learning for Deep Research

Multiple papers in this review emphasize the critical role of reinforcement learning in training deep research agents:

**Search-R1** demonstrates that RL can optimize LLM reasoning trajectories with multi-turn search interactions, achieving 41% and 20% improvements over RAG baselines [citation:Jin et al., 2025, E13]. The system uses retrieved token masking for stable RL training, optimizing only over LLM-generated tokens while excluding retrieved content [citation:Jin et al., 2025, E14].

**WebSailor** introduces DUPO, an efficient agentic RL training algorithm that achieves 2-3 times speedup over dynamic sampling approaches [citation:Li et al., 2025a, E18].

**WebDancer** shows that a two-stage pipeline (SFT for cold start followed by RL for generalization) is essential, as RL-only training achieved only 5% Pass@3 on GAIA [citation:Wu et al., 2025a, E2]. Reinforcement learning has proven effective for enhancing LLM reasoning capabilities, as demonstrated by OpenAI-o1 and DeepSeek-R1 [citation:Jin et al., 2025, E17].

**WebThinker** employs iterative online DPO to enhance research tool utilization and optimize end-to-end task performance [citation:Li et al., 2025b, E12].

The consistent success of RL-based approaches across different frameworks suggests that outcome-based optimization is crucial for developing effective deep research capabilities.

---

## 5. Reasoning Patterns in Deep Research

### 5.1 Uncertainty Reduction

Li et al. (2025a) identify uncertainty reduction as the key reasoning pattern that distinguishes superhuman deep research systems [citation:Li et al., 2025a, E15]. Proprietary systems like DeepResearch achieve their performance through the ability to systematically reduce extreme uncertainty when navigating vast information landscapes.

This pattern involves:
- Identifying information gaps
- Generating targeted search queries to fill gaps
- Evaluating retrieved information for relevance and reliability
- Iteratively refining search strategies based on findings

### 5.2 Multi-Hop Reasoning

Zhou et al. (2025) emphasize that deep research capabilities require LLMs to perform multi-hop reasoning across heterogeneous web sources through search engine interaction [citation:Zhou et al., 2025, E19]. This capability is essential for answering complex questions that cannot be resolved through single-step retrieval.

Multi-hop reasoning in deep research contexts involves:
- Decomposing complex questions into sub-queries
- Tracking dependencies between information sources
- Synthesizing information from multiple sources
- Resolving conflicts or inconsistencies between sources

### 5.3 Thought-Action-Observation Paradigms

Wu et al. (2025b) and Wu et al. (2025a) both employ Thought-Action-Observation paradigms in their frameworks [citation:Wu et al., 2025b, E25; Wu et al., 2025a, E2]. This paradigm structures agent interactions as:

1. **Thought:** Reasoning about the current state and next steps
2. **Action:** Executing search, navigation, or information extraction
3. **Observation:** Processing results and updating internal state

The ReAct paradigm used in WebDancer tightly couples reasoning with action, facilitating effective learning and generalization in interactive settings [citation:Wu et al., 2025a, E2].

### 5.4 Iterative State Reconstruction

Qiao et al. (2025) introduce periodic state reconstruction as a mechanism to overcome cognitive workspace suffocation [citation:Qiao et al., 2025, E4]. This pattern involves:

- Periodically consolidating findings into evolving reports
- Maintaining focused workspaces by discarding irrelevant context
- Reconstructing state to preserve only essential information
- Enabling parallel multi-agent exploration through independent workspaces

This approach contrasts with mono-contextual methods that accumulate all context, leading to performance degradation over long-horizon tasks.

---

## 6. Evaluation Frameworks

### 6.1 RACE: Reference-based Adaptive Criteria Evaluation

Du et al. (2025) developed RACE as a novel methodology for evaluating deep research reports [citation:Du et al., 2025, E28]. The framework achieves strong alignment with human judgment through:

- **Dynamic criteria generation:** Task-specific evaluation criteria are generated based on the research question
- **Adaptive weighting:** Criteria weights are adjusted based on task requirements
- **LLM-as-a-Judge:** Uses advanced LLMs to evaluate reports against criteria

This approach addresses the challenge that evaluating deep research outputs is inherently complex and labor-intensive, requiring domain expertise and nuanced judgment [citation:Du et al., 2025, E31].

### 6.2 FACT: Factual Accuracy and Citation Test

Du et al. (2025) also introduced FACT for evaluating information retrieval capabilities [citation:Du et al., 2025, E29]. The framework assesses:

- **Effective citation count:** Number of citations that contribute to answering the research question
- **Citation accuracy:** Whether citations support the claims made
- **Factual grounding:** Whether the report is based on retrieved evidence

This framework provides a complementary perspective to RACE, focusing on the retrieval and collection capabilities rather than report quality [citation:Du et al., 2025, E30].

### 6.3 Benchmark Performance Metrics

The reviewed literature uses several standard metrics for evaluating deep research agents:

- **Accuracy:** Percentage of correctly answered questions on benchmarks like BrowseComp, GAIA, and WebWalkerQA
- **Pass@k:** Percentage of tasks solved within k attempts, commonly used in GAIA and WebWalkerQA evaluations
- **Citation quality:** Number and accuracy of citations in generated reports
- **Report quality:** Evaluated using frameworks like RACE or human expert judgment

---

## 7. Comparative Analysis

### 7.1 Performance on Standard Benchmarks

Table 1 summarizes performance of leading systems on key benchmarks:

| System | BrowseComp-ZH | GAIA | WebWalkerQA | HLE |
|--------|--------------|------|-------------|-----|
| OpenAI DeepResearch | 42.9% [citation:Zhou et al., 2025, E20] | - | - | - |
| Gemini-2.5-Pro DeepResearch | - | - | - | - |
| WebThinker | - | Strong performance [citation:Li et al., 2025b, E11] | Strong performance [citation:Li et al., 2025b, E11] | Strong performance [citation:Li et al., 2025b, E11] |
| WebSailor | Matches proprietary [citation:Li et al., 2025a, E15] | - | - | - |
| WebDancer | - | 64.1% Pass@3 [citation:Wu et al., 2025a, E3] | 62.0% Pass@3 [citation:Wu et al., 2025a, E3] | - |
| WebResearcher | - | SOTA [citation:Qiao et al., 2025, E6] | SOTA [citation:Qiao et al., 2025, E6] | 28.8% [citation:Qiao et al., 2025, E6] |
| WebShaper | - | SOTA (open-source) [citation:Tao et al., 2025, E24] | SOTA (open-source) [citation:Tao et al., 2025, E24] | - |

Note: Direct comparisons are limited by different evaluation protocols and model versions across papers.

### 7.2 Methodological Comparisons

**Training Paradigms:**
- **Two-stage (SFT + RL):** WebDancer [citation:Wu et al., 2025a, E2], WebSailor [citation:Li et al., 2025a, E16]
- **RL-only:** Search-R1 [citation:Jin et al., 2025, E14]
- **Iterative online DPO:** WebThinker [citation:Li et al., 2025b, E11]
- **DUPO:** WebSailor [citation:Li et al., 2025a, E18]

**Architectural Approaches:**
- **Mono-contextual:** WebThinker [citation:Li et al., 2025b, E10], Search-R1 [citation:Jin et al., 2025, E13], WebDancer [citation:Wu et al., 2025a, E1]
- **Iterative with state reconstruction:** WebResearcher [citation:Qiao et al., 2025, E4]

**Data Synthesis:**
- **Information-driven:** Traditional approaches
- **Formalization-driven:** WebShaper [citation:Tao et al., 2025, E22]
- **Complexity escalation:** WebFrontier [citation:Qiao et al., 2025, E5]
- **crawlQA and e2hQA:** WebDancer [citation:Wu et al., 2025a, E2]

### 7.3 Key Insights

1. **Proprietary systems lead:** OpenAI DeepResearch and Gemini-2.5-Pro DeepResearch consistently demonstrate leading performance [citation:Du et al., 2025, E30; Zhou et al., 2025, E20]

2. **Open-source gap closing:** WebSailor matches proprietary performance on BrowseComp [citation:Li et al., 2025a, E15], and WebResearcher surpasses frontier proprietary systems on multiple benchmarks [citation:Qiao et al., 2025, E6]

3. **Training methodology matters:** Two-stage pipelines (SFT + RL) outperform RL-only approaches [citation:Wu et al., 2025a, E2], and iterative paradigms outperform mono-contextual approaches [citation:Qiao et al., 2025, E6]

4. **Benchmark difficulty:** Even the best systems achieve only 42.9% on BrowseComp-ZH [citation:Zhou et al., 2025, E20], indicating substantial room for improvement

5. **Reasoning patterns are critical:** Uncertainty reduction capabilities distinguish superhuman systems [citation:Li et al., 2025a, E15]

---

## 8. Open Challenges and Future Directions

### 8.1 Limitations Identified in the Literature

**Context Management:** Mono-contextual approaches suffer from cognitive workspace suffocation and irreversible noise contamination [citation:Qiao et al., 2025]. While WebResearcher addresses this through iterative state reconstruction, scalable solutions for long-horizon tasks remain an open challenge.

**Benchmark Coverage:** Current benchmarks focus primarily on English and Chinese languages [citation:Wei et al., 2025; Zhou et al., 2025], with limited coverage of other major information ecosystems. Additionally, benchmarks like BrowseComp sidestep challenges of true user query distributions, such as generating long answers or resolving ambiguity [citation:Wei et al., 2025].

**Evaluation Alignment:** While RACE and FACT achieve strong alignment with human judgment [citation:Du et al., 2025], fully automated evaluation of deep research outputs remains challenging, particularly for open-ended research tasks.

**Training Data Scarcity:** The scarcity of high-quality training data has limited the development of information-seeking agents [citation:Tao et al., 2025, E22]. While frameworks like WebShaper and WebFrontier address this through data synthesis, ensuring diversity and coverage remains challenging.

### 8.2 Promising Research Directions

**Parallel Multi-Agent Exploration:** WebResearcher's parallel thinking approach enables concurrent multi-agent exploration for more comprehensive conclusions [citation:Qiao et al., 2025, E4]. This direction shows promise for scaling deep research capabilities.

**Vertical Exploration:** Wu et al. (2025b) identify vertical exploration within web pages as a promising direction for scaling inference time in RAG systems [citation:Wu et al., 2025b, E26]. This contrasts with traditional horizontal search across multiple sources.

**Reasoning Model Integration:** Agentic approaches built on reasoning-specialized models outperform non-agentic counterparts [citation:Wu et al., 2025a, E1]. Further integration of deep research capabilities with reasoning models like o1 and DeepSeek-R1 is a promising direction.

**Formalization-Driven Approaches:** WebShaper's formalization-driven paradigm enables precise control over reasoning structures [citation:Tao et al., 2025, E22]. Extending this approach to other aspects of deep research could improve training data quality and model performance.

---

## 9. Conclusion

This systematic literature review has examined 10 recent papers on deep research, revealing a rapidly evolving field characterized by sophisticated benchmarking frameworks, innovative architectural approaches, and effective training methodologies. Key findings include:

1. **Benchmarking maturity:** The field has developed challenging benchmarks (BrowseComp, BrowseComp-ZH, WebWalkerQA, DeepResearch Bench) that effectively measure deep research capabilities and reveal significant gaps between current systems and human performance [citation:Wei et al., 2025, E7; Zhou et al., 2025, E19; Wu et al., 2025b, E25; Du et al., 2025, E28].

2. **Architectural innovation:** Systems like WebThinker, Search-R1, WebSailor, WebDancer, and WebResearcher demonstrate diverse approaches to enabling autonomous deep research, with iterative paradigms showing particular promise [citation:Li et al., 2025b, E10; Jin et al., 2025, E13; Li et al., 2025a, E15; Wu et al., 2025a, E1; Qiao et al., 2025, E4].

3. **Training methodology importance:** Reinforcement learning-based approaches consistently outperform traditional methods, with two-stage pipelines (SFT + RL) and specialized algorithms like DUPO showing strong results [citation:Wu et al., 2025a, E2; Li et al., 2025a, E18].

4. **Reasoning patterns:** The ability to systematically reduce uncertainty through multi-hop reasoning, Thought-Action-Observation paradigms, and iterative state reconstruction distinguishes high-performing systems [citation:Li et al., 2025a, E15; Zhou et al., 2025, E19; Wu et al., 2025b, E25; Qiao et al., 2025, E4].

5. **Proprietary leadership:** OpenAI DeepResearch and Gemini-2.5-Pro DeepResearch currently lead the field, though open-source systems are closing the gap [citation:Zhou et al., 2025, E20; Li et al., 2025a, E15].

The literature points to several promising directions for future research, including parallel multi-agent exploration, vertical exploration within web pages, deeper integration with reasoning models, and formalization-driven approaches to data synthesis. As the field continues to evolve, addressing open challenges in context management, benchmark coverage, evaluation alignment, and training data scarcity will be critical for advancing deep research capabilities.

---

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents. *arXiv preprint arXiv:2506.11763*. https://arxiv.org/abs/2506.11763

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning. *arXiv preprint arXiv:2503.09516*. https://arxiv.org/abs/2503.09516 [E13, E14, E17]

Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025a). WebSailor: Navigating Super-human Reasoning for Web Agent. *arXiv preprint arXiv:2507.02592*. https://arxiv.org/abs/2507.02592 [E15, E16, E18]

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025b). WebThinker: Empowering Large Reasoning Models with Deep Research Capability. *arXiv preprint arXiv:2504.21776*. https://arxiv.org/abs/2504.21776 [E10, E11, E12]

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents. *arXiv preprint arXiv:2509.13309*. https://arxiv.org/abs/2509.13309 [E4, E5, E6, E32]

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization. *arXiv preprint arXiv:2507.15061*. https://arxiv.org/abs/2507.15061 [E22, E23, E24]

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents. *arXiv preprint arXiv:2504.12516*. https://arxiv.org/abs/2504.12516 [E7, E8, E9]

Wu, J., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025a). WebDancer: Towards Autonomous Information Seeking Agency. *arXiv preprint arXiv:2505.22648*. https://arxiv.org/abs/2505.22648 [E1, E2, E3]

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025b). WebWalker: Benchmarking LLMs in Web Traversal. *arXiv preprint arXiv:2501.07572*. https://arxiv.org/abs/2501.07572 [E25, E26, E27, E33]

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese. *arXiv preprint arXiv:2504.19314*. https://arxiv.org/abs/2504.19314 [E19, E20, E21]

---

## Appendix: Evidence Citations

All claims in this review are supported by evidence quotes recorded during the paper reading process. The evidence index provides mappings between papers and evidence IDs (E1-E33), with each quote verified against the original paper text.

**Receipt Citations:**
- Paper reading: [r6-r10]
- Batch 1 delegation: [r11]
- Batch 2 delegation: [r12]
- Batch 3 delegation: [r13]
- Evidence index: [r14]
- Batch retrieval: [r3-r5]
