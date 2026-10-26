# Systematic Literature Review: AI Scientists

**Date**: October 26, 2026

**Search Period**: October 27, 2023 – October 26, 2025

**Category**: cs.AI (arXiv)

**Format**: APA Style

---

## Executive Summary

This systematic literature review examines 10 recent papers (2023-2025) on AI Scientists—autonomous or semi-autonomous AI systems capable of conducting scientific research. The reviewed works span fully automated discovery systems, multi-agent collaborative frameworks, benchmark evaluations, and domain-specific applications in biomedical discovery and machine learning research. Key themes include: (1) end-to-end automated research pipelines, (2) human-AI collaboration models, (3) evaluation frameworks for AI research capabilities, and (4) scaling strategies for hypothesis generation and experimentation.

---

## References (APA Format)

1. Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A., Schwarz, J. R., Ektefaie, Y., Kondic, J., & Zitnik, M. (2024). Empowering biomedical discovery with AI agents. *arXiv preprint arXiv:2404.02831*. https://arxiv.org/abs/2404.02831v2

2. Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirkovic, P., Myaskovsky, A., Glowaty, G., Weissenberger, F., Orlandi, A., Popovici, D., Palepu, A., Rong, K., Tanno, R., Saab, K., Zhang, F., Blum, J., Carroll, A., Kulkarni, K., Tomasev, N., & Zverinski, D. (2025). Accelerating scientific discovery with Co-Scientist. *arXiv preprint arXiv:2502.18864*. https://arxiv.org/abs/2502.18864v2

3. Jansen, P., Tafjord, O., Radensky, M., Siangliulue, P., Hope, T., Mishra, B. D., Majumder, B. P., Weld, D. S., & Clark, P. (2025). CodeScientist: End-to-end semi-automated scientific discovery with code-based experimentation. *arXiv preprint arXiv:2503.22708*. https://arxiv.org/abs/2503.22708v1

4. Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). AIDE: AI-driven exploration in the space of code. *arXiv preprint arXiv:2502.13138*. https://arxiv.org/abs/2502.13138v1

5. Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). LAB-Bench: Measuring capabilities of language models for biology research. *arXiv preprint arXiv:2407.10362*. https://arxiv.org/abs/2407.10362v3

6. Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Zhao, D., Rong, Y., Feng, T., & Bing, L. (2024). Chain of Ideas: Revolutionizing research via novel idea development with LLM agents. *arXiv preprint arXiv:2410.13185*. https://arxiv.org/abs/2410.13185v5

7. Li, R., Patel, T., Wang, Q., & Du, X. (2024). MLR-Copilot: Autonomous machine learning research based on large language models agents. *arXiv preprint arXiv:2408.14033*. https://arxiv.org/abs/2408.14033v3

8. Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. *arXiv preprint arXiv:2408.06292*. https://arxiv.org/abs/2408.06292v3

9. Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., & Patwardhan, T. (2025). PaperBench: Evaluating AI's ability to replicate AI research. *arXiv preprint arXiv:2504.01848*. https://arxiv.org/abs/2504.01848v3

10. Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. *arXiv preprint arXiv:2504.08066*. https://arxiv.org/abs/2504.08066v1

---

## Annotated Bibliography

### 1. Gao et al. (2024) – Empowering Biomedical Discovery with AI Agents

**Citation**: Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A., Schwarz, J. R., Ektefaie, Y., Kondic, J., & Zitnik, M. (2024). Empowering biomedical discovery with AI agents. *arXiv preprint arXiv:2404.02831*. https://arxiv.org/abs/2404.02831v2

**Summary**: This position paper envisions "AI scientists" as collaborative systems that augment rather than replace human researchers in biomedical discovery. The authors propose a framework where AI agents integrate large language models, generative models, and biomedical tools to assist with hypothesis generation, workflow planning, and knowledge synthesis. Key capabilities include structured memory for continual learning, self-assessment mechanisms, and integration with experimental platforms.

**Key Contributions**:
- Conceptual framework for human-AI collaboration in scientific discovery
- Emphasis on AI agents as augmentative tools rather than autonomous replacements
- Integration of AI models with biomedical tools and experimental platforms
- Focus on applications ranging from virtual cell simulation to therapy development

**Relevance**: Provides foundational vision for AI scientist systems with emphasis on human-AI partnership rather than full automation.

---

### 2. Gottweis et al. (2025) – Accelerating Scientific Discovery with Co-Scientist

**Citation**: Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirkovic, P., Myaskovsky, A., Glowaty, G., Weissenberger, F., Orlandi, A., Popovici, D., Palepu, A., Rong, K., Tanno, R., Saab, K., Zhang, F., Blum, J., Carroll, A., Kulkarni, K., Tomasev, N., & Zverinski, D. (2025). Accelerating scientific discovery with Co-Scientist. *arXiv preprint arXiv:2502.18864*. https://arxiv.org/abs/2502.18864v2

**Summary**: Co-Scientist is a multi-agent AI system built on Gemini for structured scientific thinking and hypothesis generation. The system employs asynchronous task execution and tournament evolution processes for self-improving hypothesis generation. The authors demonstrate real-world validation in three biomedical applications: drug repurposing, novel target discovery, and explaining mechanisms of anti-microbial resistance. Notably, Co-Scientist identified new drug repurposing candidates and synergistic combination therapies for acute myeloid leukemia, validated through in vitro experiments.

**Key Contributions**:
- Multi-agent architecture with asynchronous task execution framework
- Tournament evolution process for iterative hypothesis refinement
- Test-time compute scaling demonstrates continued improvement in hypothesis quality
- Real-world experimental validation in biomedical applications

**Relevance**: Demonstrates practical multi-agent system with validated real-world scientific discoveries.

---

### 3. Jansen et al. (2025) – CodeScientist: End-to-End Semi-Automated Scientific Discovery with Code-based Experimentation

**Citation**: Jansen, P., Tafjord, O., Radensky, M., Siangliulue, P., Hope, T., Mishra, B. D., Majumder, B. P., Weld, D. S., & Clark, P. (2025). CodeScientist: End-to-end semi-automated scientific discovery with code-based experimentation. *arXiv preprint arXiv:2503.22708*. https://arxiv.org/abs/2503.22708v1

**Summary**: CodeScientist addresses two key limitations in autonomous scientific discovery (ASD) systems: constrained design spaces and inadequate code evaluation. The system frames ideation and experiment construction as genetic search over combinations of research articles and codeblocks defining common domain actions. CodeScientist conducted hundreds of automated experiments, returning 19 discoveries, 6 of which were judged as minimally sound and incrementally novel through multi-faceted evaluation including external review, code review, and replication attempts.

**Key Contributions**:
- Genetic search paradigm over research articles and codeblocks
- Multi-faceted evaluation beyond conference-style paper review
- Discoveries spanning new tasks, agents, metrics, and data
- Shift from benchmark optimization to broader discoveries

**Relevance**: Introduces rigorous evaluation methodology and demonstrates qualitative shift in discovery scope.

---

### 4. Jiang et al. (2025) – AIDE: AI-Driven Exploration in the Space of Code

**Citation**: Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). AIDE: AI-driven exploration in the space of code. *arXiv preprint arXiv:2502.13138*. https://arxiv.org/abs/2502.13138v1

**Summary**: AIDE frames machine learning engineering as a code optimization problem and formulates trial-and-error as tree search in the space of potential solutions. By strategically reusing and refining promising solutions, AIDE trades computational resources for enhanced performance. The system achieves state-of-the-art results on multiple machine learning engineering benchmarks, including Kaggle evaluations, OpenAI MLE-Bench, and METRs RE-Bench.

**Key Contributions**:
- Tree search formulation for ML engineering optimization
- Strategic solution reuse and refinement methodology
- State-of-the-art results on multiple ML engineering benchmarks
- Computational resource trading for performance enhancement

**Relevance**: Provides alternative optimization-focused approach to automated ML research.

---

### 5. Laurent et al. (2024) – LAB-Bench: Measuring Capabilities of Language Models for Biology Research

**Citation**: Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). LAB-Bench: Measuring capabilities of language models for biology research. *arXiv preprint arXiv:2407.10362*. https://arxiv.org/abs/2407.10362v3

**Summary**: LAB-Bench introduces over 2,400 multiple choice questions for evaluating AI systems on practical biology research capabilities. Unlike textbook-style benchmarks, LAB-Bench evaluates literature search, protocol planning, data analysis, figure interpretation, database navigation, and DNA/protein sequence manipulation. The benchmark provides a public subset for community use and establishes baseline comparisons against human expert biology researchers.

**Key Contributions**:
- Comprehensive benchmark dataset for practical biology research tasks
- Evaluation of literature search, protocol planning, and data analysis capabilities
- Baseline comparisons with human expert performance
- Public dataset release for community benchmarking

**Relevance**: Establishes evaluation framework for AI assistant capabilities in biological research.

---

### 6. Li et al. (2024) – Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents

**Citation**: Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Zhao, D., Rong, Y., Feng, T., & Bing, L. (2024). Chain of Ideas: Revolutionizing research via novel idea development with LLM agents. *arXiv preprint arXiv:2410.13185*. https://arxiv.org/abs/2410.13185v5

**Summary**: The Chain-of-Ideas (CoI) agent organizes relevant literature in a chain structure mirroring progressive development in research domains, facilitating LLMs to capture current advancements and enhance ideation capabilities. The authors introduce Idea Arena, an evaluation protocol comprehensively assessing idea generation methods from multiple perspectives aligned with human researcher preferences. CoI consistently outperforms other methods with comparable quality to humans at a minimum cost of $0.50 per candidate idea with experimental design.

**Key Contributions**:
- Chain structure organization of literature for ideation enhancement
- Idea Arena evaluation protocol aligned with human researcher preferences
- Cost-effective idea generation ($0.50 minimum per idea)
- Human-comparable quality in research idea generation

**Relevance**: Provides cost-effective ideation methodology with human-aligned evaluation.

---

### 7. Li et al. (2024) – MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents

**Citation**: Li, R., Patel, T., Wang, Q., & Du, X. (2024). MLR-Copilot: Autonomous machine learning research based on large language models agents. *arXiv preprint arXiv:2408.14033*. https://arxiv.org/abs/2408.14033v3

**Summary**: MLR-Copilot is an autonomous ML research framework powered by LLM agents, released concurrently with AI-Scientist in August 2024. The framework consists of three stages: idea generation (IdeaAgent powered by RL-tuned LLM), experiment implementation (ExperimentAgent leveraging retrieved prototype code), and code execution with iterative debugging. Evaluation on five ML research tasks demonstrates potential for facilitating ML research progress and innovation.

**Key Contributions**:
- Three-stage framework: idea generation, experiment implementation, code execution
- RL-tuned LLM for idea generation
- Prototype code retrieval and iterative debugging capabilities
- Concurrent development with AI-Scientist (August 2024)

**Relevance**: Demonstrates autonomous ML research framework with RL-tuned components.

---

### 8. Lu et al. (2024) – The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

**Citation**: Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. *arXiv preprint arXiv:2408.06292*. https://arxiv.org/abs/2408.06292v3

**Summary**: The AI Scientist presents the first comprehensive framework for fully automatic scientific discovery, enabling frontier LLMs to perform research independently. The system generates novel research ideas, writes code, executes experiments, visualizes results, writes full scientific papers, and runs simulated review processes. Applied to three ML subfields (diffusion modeling, transformer-based language modeling, learning dynamics), each idea is developed into a full paper at less than $15 per paper. An automated reviewer achieves near-human performance in evaluation, with generated papers exceeding acceptance thresholds at top ML conferences.

**Key Contributions**:
- First comprehensive framework for fully automatic scientific discovery
- End-to-end pipeline from idea generation to paper writing and review
- Cost-effective operation (<$15 per paper)
- Automated reviewer with near-human evaluation performance
- Open-source implementation

**Relevance**: Seminal work demonstrating fully automated end-to-end scientific discovery.

---

### 9. Starace et al. (2025) – PaperBench: Evaluating AI's Ability to Replicate AI Research

**Citation**: Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., & Patwardhan, T. (2025). PaperBench: Evaluating AI's ability to replicate AI research. *arXiv preprint arXiv:2504.01848*. https://arxiv.org/abs/2504.01848v3

**Summary**: PaperBench evaluates AI agents' ability to replicate 20 ICML 2024 Spotlight and Oral papers from scratch. The benchmark contains 8,316 individually gradable tasks with rubrics co-developed with original paper authors. An LLM-based judge automatically grades replication attempts, validated through a separate benchmark. The best-performing agent (Claude 3.5 Sonnet with open-source scaffolding) achieves 21.0% average replication score, not yet outperforming human ML PhDs on subset tasks.

**Key Contributions**:
- Comprehensive replication benchmark with 8,316 gradable tasks
- Author-co-developed rubrics for accuracy and realism
- LLM-based automatic judge with validated performance
- Human baseline comparison showing AI systems not yet surpassing human performance

**Relevance**: Establishes rigorous evaluation standard for AI research replication capabilities.

---

### 10. Yamada et al. (2025) – The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

**Citation**: Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. *arXiv preprint arXiv:2504.08066*. https://arxiv.org/abs/2504.08066v1

**Summary**: AI Scientist-v2 produces the first entirely AI-generated peer-review-accepted workshop paper. Compared to v1, it eliminates reliance on human-authored code templates, generalizes across diverse ML domains, and leverages progressive agentic tree-search methodology managed by a dedicated experiment manager agent. Enhanced AI reviewer integrates Vision-Language Model feedback for iterative figure refinement. Three fully autonomous manuscripts were submitted to an ICLR workshop, with one exceeding the average human acceptance threshold—marking the first fully AI-generated paper to navigate peer review successfully.

**Key Contributions**:
- First AI-generated peer-review-accepted workshop paper
- Agentic tree-search methodology with experiment manager agent
- Elimination of human-authored code template reliance
- VLM-enhanced reviewer for iterative figure refinement
- Successful peer review navigation

**Relevance**: Demonstrates breakthrough achievement in autonomous research with peer review acceptance.

---

## Thematic Synthesis

### Theme 1: End-to-End Automated Discovery Systems

Three papers present comprehensive end-to-end systems for autonomous scientific discovery:

- **The AI Scientist** (Lu et al., 2024) and **AI Scientist-v2** (Yamada et al., 2025) demonstrate fully automated pipelines from idea generation through paper writing and peer review
- **CodeScientist** (Jansen et al., 2025) introduces genetic search over research articles and codeblocks with multi-faceted evaluation

**Key Finding**: Fully automated systems can now produce peer-review-acceptable papers, though human oversight remains valuable for quality assurance.

### Theme 2: Multi-Agent Collaborative Frameworks

Two papers emphasize multi-agent architectures:

- **Co-Scientist** (Gottweis et al., 2025) employs asynchronous task execution and tournament evolution for hypothesis refinement
- **MLR-Copilot** (Li et al., 2024) uses specialized agents for ideation, experimentation, and code execution

**Key Finding**: Multi-agent systems enable scalable hypothesis generation and specialized task execution with demonstrated real-world validation.

### Theme 3: Evaluation Frameworks and Benchmarks

Three papers focus on evaluation methodologies:

- **LAB-Bench** (Laurent et al., 2024) provides 2,400+ questions for practical biology research capabilities
- **PaperBench** (Starace et al., 2025) evaluates AI replication of 20 ICML papers with 8,316 gradable tasks
- **Idea Arena** (Li et al., 2024) aligns idea evaluation with human researcher preferences

**Key Finding**: Comprehensive evaluation frameworks reveal AI systems have not yet surpassed human expert performance on complex research tasks.

### Theme 4: Human-AI Collaboration Models

**Gao et al. (2024)** present a vision for AI scientists as augmentative rather than replacement technologies, emphasizing:
- Integration of human creativity with AI's analytical capabilities
- Collaborative agents combining AI models with experimental platforms
- Structured memory for continual learning and self-assessment

**Key Finding**: Human-AI partnership models may offer more practical near-term benefits than full automation.

### Theme 5: Optimization and Search Methodologies

Two papers introduce novel search strategies:

- **AIDE** (Jiang et al., 2025) frames ML engineering as tree search in code optimization space
- **AI Scientist-v2** (Yamada et al., 2025) employs progressive agentic tree-search methodology

**Key Finding**: Tree search formulations enable strategic exploration-exploitation tradeoffs in research space navigation.

---

## Comparative Analysis

| System | Automation Level | Domain Focus | Cost per Idea/Paper | Key Innovation |
|--------|-----------------|--------------|---------------------|----------------|
| AI Scientist (Lu et al., 2024) | Fully automated | ML | <$15/paper | End-to-end pipeline with automated review |
| AI Scientist-v2 (Yamada et al., 2025) | Fully automated | ML | Not specified | Agentic tree search, peer-review acceptance |
| Co-Scientist (Gottweis et al., 2025) | Multi-agent collaborative | Biomedical | Not specified | Tournament evolution, in vitro validation |
| CodeScientist (Jansen et al., 2025) | Semi-automated | ML/Agents | Not specified | Genetic search, multi-faceted evaluation |
| MLR-Copilot (Li et al., 2024) | Autonomous | ML | Not specified | RL-tuned ideation, three-stage framework |
| Chain of Ideas (Li et al., 2024) | LLM agent-assisted | General | $0.50/idea | Literature chain organization |
| AIDE (Jiang et al., 2025) | Optimization-focused | ML Engineering | Not specified | Tree search in code space |

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Limited Domain Diversity**: 7 of 10 papers focus primarily on ML/CS domains, with only 3 addressing biomedical applications
2. **Evaluation Standardization**: Multiple competing benchmarks (LAB-Bench, PaperBench, Idea Arena) lack unified evaluation standards
3. **Reproducibility Concerns**: Only 3 papers provide open-source implementations with comprehensive documentation
4. **Long-term Validation**: Limited evidence of sustained research productivity beyond proof-of-concept demonstrations
5. **Ethical Considerations**: Minimal discussion of research integrity, authorship attribution, and quality control in automated systems

### Future Research Directions

1. **Cross-Domain Generalization**: Extend AI scientist systems beyond ML to physics, chemistry, materials science, and social sciences
2. **Benchmark Harmonization**: Develop unified evaluation frameworks comparable across systems
3. **Human-AI Interaction Design**: Investigate optimal collaboration patterns and interface designs
4. **Quality Assurance Mechanisms**: Develop automated detection of methodological flaws and reproducibility issues
5. **Ethical Frameworks**: Establish guidelines for authorship, credit attribution, and research integrity in AI-assisted discovery

---

## Conclusions

The literature from 2023-2025 demonstrates rapid advancement in AI scientist capabilities, with systems now achieving:

- **Fully automated discovery**: End-to-end pipelines generating peer-review-acceptable papers (Lu et al., 2024; Yamada et al., 2025)
- **Real-world validation**: In vitro experimental confirmation of AI-generated hypotheses (Gottweis et al., 2025)
- **Cost-effective operation**: Idea generation at $0.50-$15 per output (Li et al., 2024; Lu et al., 2024)
- **Rigorous evaluation**: Comprehensive benchmarks with human baseline comparisons (Starace et al., 2025; Laurent et al., 2024)

However, critical limitations remain:

- AI systems do not yet outperform human experts on complex research tasks (Starace et al., 2025)
- Domain coverage remains narrow, concentrated in ML/CS
- Standardized evaluation frameworks are lacking
- Ethical and quality assurance frameworks are underdeveloped

The field appears poised for expansion beyond proof-of-concept demonstrations toward practical deployment in diverse scientific domains, with human-AI collaboration models offering the most promising near-term pathway for augmenting scientific productivity.

---

## Methodology

**Search Strategy**: arXiv scholar search with phrase matching on "AI scientists" in cs.AI category

**Inclusion Criteria**:
- Published between October 27, 2023 and October 26, 2025
- Primary category cs.AI
- Focus on AI scientists, autonomous research systems, AI-driven scientific discovery, or AI agents conducting scientific research

**Screening Process**:
- Initial pool: 50 papers from arXiv search
- Citation expansion: 33 additional papers from references
- Shortlisted: 30 papers
- Final selection: 10 papers screened for centrality to topic

**Format**: APA 7th edition citation style

---

**Review Completed**: October 26, 2026
