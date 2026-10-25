# Systematic Literature Review: Robot Manipulation with Foundation Models

**Search Strategy:** arXiv category cs.RO (Robotics)
**Date Range:** 2023-2025
**Number of Papers:** 10
**Report Date:** October 25, 2026

---

## Executive Summary

This systematic literature review examines recent advances in robot manipulation, focusing on learning-based approaches that leverage foundation models, world models, and large-scale pre-trained systems. The 10 papers analyzed reveal several key trends: (1) a shift from classical control to learning-based methods including reinforcement learning, imitation learning, and foundation model integration; (2) growing emphasis on generalization across visual, semantic, and behavioral dimensions; (3) innovative approaches to bridging simulation-to-reality gaps; and (4) increasing attention to fine-grained, part-level manipulation capabilities.

Key findings indicate that while foundation models and large language models show promise for robot manipulation, direct application faces stability challenges requiring specialized frameworks. World models, diffusion-based approaches, and parameter-efficient adaptation methods demonstrate significant improvements in generalization and real-world performance. However, limitations persist in fine-grained control, semantic understanding, and evaluation standardization.

---

## 1. Introduction

Robot manipulation has undergone a paradigm shift in recent years, transitioning from pre-programmed methods to learning-based approaches capable of adapting to uncertain environments. The emergence of foundation models—large-scale models pre-trained on diverse data—has opened new possibilities for robot learning, promising generalization across tasks, objects, and environments.

This review synthesizes 10 recent papers from arXiv category cs.RO (Robotics) published between 2023 and 2025, examining how foundation models, world models, and related approaches are advancing robot manipulation capabilities. The review addresses the following research questions:

1. How are foundation models being integrated into robot manipulation systems?
2. What approaches enable generalization across tasks, objects, and environments?
3. What are the key challenges and limitations in current methods?

---

## 2. Methodology

### 2.1 Search Strategy

Papers were retrieved from arXiv using the query "robot manipulation" with category filter cs.RO (Robotics), sorted by relevance. The search returned 10 papers published between February 2023 and November 2025.

### 2.2 Inclusion Criteria

- Papers focused on robot manipulation tasks
- Published in arXiv category cs.RO
- Employ learning-based methods (reinforcement learning, imitation learning, foundation models, world models, or related approaches)
- Include empirical evaluation or systematic analysis

### 2.3 Data Extraction

For each paper, the following information was extracted:
- Bibliographic information (authors, title, publication date)
- Research question
- Methodology
- Key findings (3-5 points)
- Limitations

---

## 3. Results

### 3.1 Paper Characteristics

The 10 papers span diverse approaches to robot manipulation:

| Paper ID | Title | Year | Approach |
|----------|-------|------|----------|
| 2511.22505 | RealD²iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion | 2025 | Diffusion models for sim2real |
| 2309.04687 | A Review on Robot Manipulation Methods in Human-Robot Interactions | 2023 | Review of RL and IL methods |
| 2312.01421 | RobotGPT: Robot Manipulation Learning from ChatGPT | 2023 | LLM-based decision framework |
| 2308.01600 | Active Acoustic Sensing for Robot Manipulation | 2023 | Novel sensing modality |
| 2310.03932 | Interpreting Behaviors and Geometric Constraints as Knowledge Graphs | 2023 | Knowledge graphs for control |
| 2306.11335 | Surfer: Progressive Reasoning with World Models | 2023 | World model-based framework |
| 2503.01238 | A Taxonomy for Evaluating Generalist Robot Manipulation Policies | 2025 | Evaluation taxonomy |
| 2505.21652 | PartInstruct: Part-level Instruction Following | 2025 | Fine-grained manipulation benchmark |
| 2302.02011 | Zero-Shot Robot Manipulation from Passive Human Videos | 2023 | Video-based learning |
| 2409.01083 | Affordance-based Robot Manipulation with Flow Matching | 2024 | Flow matching for policy learning |

### 3.2 Thematic Analysis

#### Theme 1: Foundation Models and Large Language Models

Two papers directly address integration of foundation models:

**RobotGPT** (Jin et al., 2023) demonstrates that direct use of ChatGPT for robot manipulation achieves only 38.5% success rate due to output inconsistency. However, training a dedicated agent using ChatGPT as an expert improves success rates to 91.5%, highlighting the importance of distillation rather than direct deployment.

**PartInstruct** (Yin et al., 2025) reveals that despite pre-training on internet-scale language datasets, vision-language-action models struggle with semantic generalization, particularly for fine-grained, part-level manipulation tasks.

#### Theme 2: World Models and Representation Learning

**Surfer** (Ren et al., 2023) introduces a world model-based framework that treats manipulation as visual scene state transfer, decoupling action and scene prediction. This explicit modeling achieves 54.74% success rate on progressive reasoning tasks, exceeding baselines by 7.1 percentage points.

**Zero-Shot from Videos** (Bharadhwaj et al., 2023) extracts agent-agnostic action representations from passive human videos, enabling zero-shot transfer to robot manipulation without any robot-specific training data.

#### Theme 3: Simulation-to-Reality Transfer

**RealD²iff** (Liang et al., 2025) addresses the visual sim2real gap using diffusion models to synthesize realistic sensor noise, enabling zero-shot sim2real transfer without real-world fine-tuning.

**PartInstruct** and **Surfer** both rely on simulator-generated data, acknowledging limitations in real-world transfer as a key constraint.

#### Theme 4: Evaluation and Benchmarking

**STAR-Gen** (Gao et al., 2025) proposes a comprehensive taxonomy for evaluating generalization across visual, semantic, and behavioral dimensions, addressing the fragmented state of robotics evaluation.

**PartInstruct** (Yin et al., 2025) introduces the first large-scale benchmark for fine-grained manipulation with 513 objects, 1,302 tasks, and over 10,000 demonstrations.

**SeaWave** (Ren et al., 2023) provides a benchmark with 4 levels of progressive reasoning tasks for systematic evaluation.

#### Theme 5: Alternative Learning Paradigms

**Flow Matching** (Zhang & Gienger, 2024) demonstrates that flow matching achieves more stable training and faster inference compared to diffusion policies, with marginal performance improvements.

**Knowledge Graphs** (Jiang et al., 2023) unify behavior trees and geometric constraints into semantic frameworks, enabling explainable manipulation control.

**Active Acoustic Sensing** (Lu & Culbertson, 2023) introduces a novel sensing modality complementary to vision and touch, capable of perceiving object internal states.

**Review of RL and IL** (Zhang et al., 2023) provides comprehensive comparison of reinforcement learning and imitation learning, noting that IL eliminates reward design while RL excels in unfamiliar environments.

---

## 4. Discussion

### 4.1 Key Trends

1. **Shift to Learning-Based Methods**: All papers employ learning-based approaches, with traditional control methods appearing only as baselines. This reflects a field-wide transition toward data-driven methods.

2. **Foundation Model Integration**: Rather than direct deployment, successful approaches distill foundation model knowledge into specialized agents (RobotGPT) or use parameter-efficient adaptation (prompt tuning in Flow Matching).

3. **Generalization as Central Challenge**: Multiple papers address different aspects of generalization—visual (RealD²iff), semantic (PartInstruct, STAR-Gen), and behavioral (STAR-Gen)—indicating this remains the primary open challenge.

4. **Benchmarking and Evaluation**: Three papers introduce new benchmarks or taxonomies, suggesting growing recognition of evaluation standardization needs.

5. **Multi-Modal Perception**: Beyond vision, papers explore acoustic sensing, depth sensors, and haptic integration, reflecting understanding that robust manipulation requires diverse sensory inputs.

### 4.2 Limitations and Open Challenges

Common limitations across papers include:

- **Simulator Dependence**: Multiple approaches (RealD²iff, PartInstruct, Surfer) rely heavily on simulation, with real-world validation limited to narrow task sets.

- **Fine-Grained Control**: Current methods struggle with part-level reasoning and long-horizon tasks requiring precise manipulation (PartInstruct).

- **Evaluation Fragmentation**: Despite proposed taxonomies, the field lacks standardized benchmarks enabling direct comparison across methods (STAR-Gen).

- **Scalability**: Knowledge graph and world model approaches face computational overhead challenges when scaling to complex, real-world scenarios.

- **Semantic Understanding**: Vision-language-action models show surprising deficits in semantic generalization despite internet-scale pre-training (PartInstruct, STAR-Gen).

### 4.3 Comparison to Prior Work

The reviewed papers build on earlier foundations in robot learning while introducing novel contributions:

- **Diffusion Models**: RealD²iff extends diffusion approaches from action generation to sensor noise modeling, a novel application.

- **Flow Matching**: Represents an alternative to diffusion policies with theoretical advantages in training stability and inference speed.

- **Knowledge Graphs**: Brings semantic reasoning techniques from AI to robot control, enabling explainability previously absent in learning-based methods.

---

## 5. Conclusion

This systematic literature review reveals a field in transition, with foundation models and related approaches reshaping robot manipulation research. Key takeaways include:

1. **Foundation models show promise but require adaptation**: Direct deployment of LLMs for manipulation fails due to instability, but distillation and parameter-efficient fine-tuning achieve strong results.

2. **Generalization remains the central challenge**: Despite advances, robots struggle to generalize across objects, tasks, and environments, particularly for fine-grained manipulation.

3. **Evaluation standardization is critical**: The field needs unified benchmarks and taxonomies to enable meaningful comparison and track progress.

4. **Multi-modal perception is essential**: Robust manipulation requires integrating vision, touch, acoustics, and other sensing modalities.

5. **Simulation-to-reality transfer is improving**: Novel methods like diffusion-based noise synthesis enable zero-shot transfer, reducing reliance on real-world data collection.

Future research should address: (1) development of standardized benchmarks enabling fair comparison; (2) methods for fine-grained, part-level manipulation; (3) approaches for semantic understanding grounded in physical interaction; and (4) scalable methods for real-world deployment across diverse robot platforms.

---

## References

Bharadhwaj, H., Gupta, A., Tulsiani, S., & Kumar, V. (2023). Zero-shot robot manipulation from passive human videos. *arXiv preprint arXiv:2302.02011*. https://arxiv.org/abs/2302.02011

Gao, J., Belkhale, S., Dasari, S., Balakrishna, A., Shah, D., & Sadigh, D. (2025). A taxonomy for evaluating generalist robot manipulation policies. *arXiv preprint arXiv:2503.01238*. https://arxiv.org/abs/2503.01238

Jin, Y., Li, D., A, Y., Shi, J., Hao, P., Sun, F., Zhang, J., & Fang, B. (2023). RobotGPT: Robot manipulation learning from ChatGPT. *arXiv preprint arXiv:2312.01421*. https://arxiv.org/abs/2312.01421

Jiang, C., Wang, A., & Jagersand, M. (2023). Interpreting behaviors and geometric constraints as knowledge graphs for robot manipulation control. *arXiv preprint arXiv:2310.03932*. https://arxiv.org/abs/2310.03932

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. *arXiv preprint arXiv:2511.22505*. https://arxiv.org/abs/2511.22505

Lu, S., & Culbertson, H. (2023). Active acoustic sensing for robot manipulation. *arXiv preprint arXiv:2308.01600*. https://arxiv.org/abs/2308.01600

Ren, P., Zhang, K., Zheng, H., Li, Z., Wen, Y., Zhu, F., Ma, M., & Liang, X. (2023). Surfer: Progressive reasoning with world models for robotic manipulation. *arXiv preprint arXiv:2306.11335*. https://arxiv.org/abs/2306.11335

Yin, Y., Han, Z., Aarya, S., Wang, J., Xu, S., Peng, J., Wang, A., Yuille, A., & Shu, T. (2025). PartInstruct: Part-level instruction following for fine-grained robot manipulation. *arXiv preprint arXiv:2505.21652*. https://arxiv.org/abs/2505.21652

Zhang, F., & Gienger, M. (2024). Affordance-based robot manipulation with flow matching. *arXiv preprint arXiv:2409.01083*. https://arxiv.org/abs/2409.01083

Zhang, H., Kebria, P. M., Mohamed, S., Yu, S., & Nahavandi, S. (2023). A review on robot manipulation methods in human-robot interactions. *arXiv preprint arXiv:2309.04687*. https://arxiv.org/abs/2309.04687

---

## Appendix: Search Methodology

**Database:** arXiv (https://arxiv.org)
**Search Query:** "robot manipulation"
**Category Filter:** cs.RO (Robotics)
**Sort By:** Relevance
**Results Retrieved:** 10 papers
**Date of Search:** October 25, 2026

**Inclusion Criteria:**
- Focus on robot manipulation tasks
- Employ learning-based methods
- Include empirical evaluation or systematic analysis

**Exclusion Criteria:**
- Purely theoretical papers without empirical validation
- Papers focused solely on hardware design
- Papers outside cs.RO category

---

*This systematic literature review was generated following the systematic-literature-review skill workflow, including structured metadata extraction and thematic synthesis.*
