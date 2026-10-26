# Systematic Literature Review: AI Scientists

**Date:** October 26, 2026

**Search Period:** October 27, 2023 – October 26, 2025

**Category:** cs.AI (Computer Science - Artificial Intelligence)

**Number of Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in AI scientists and autonomous scientific discovery systems. The reviewed papers, published between October 2023 and October 2025, demonstrate significant progress in developing AI systems capable of conducting independent scientific research, from hypothesis generation to experimental validation and paper writing. Key themes include fully automated research frameworks, multi-agent collaborative systems, and evaluation benchmarks for AI research capabilities.

---

## Methodology

**Search Strategy:** Papers were retrieved from arXiv's cs.AI category using the search query "AI Scientists" with publication dates between October 27, 2023, and October 26, 2025. The initial pool consisted of 50 papers, expanded through citation analysis to 83 papers, with 30 papers shortlisted for screening.

**Selection Criteria:** Papers were selected based on their focus on:
- AI scientists and autonomous research systems
- AI-driven scientific discovery
- Automated research methodologies
- Machine learning research automation
- Evaluation frameworks for AI research capabilities

**Screening Process:** Each paper was scored for relevance to the topic, with the top 10 most central papers selected for this review.

---

## Annotated Bibliography (APA Format)

### 1. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). *The AI Scientist: Towards fully automated open-ended scientific discovery*. arXiv preprint arXiv:2408.06292. https://arxiv.org/abs/2408.06292v3

**Summary:** This pioneering work presents the first comprehensive framework for fully automatic scientific discovery. The AI Scientist enables frontier large language models to independently generate novel research ideas, write code, execute experiments, visualize results, and produce complete scientific papers. The system was evaluated across three ML subfields (diffusion modeling, transformer-based language modeling, and learning dynamics), with each paper generated at a cost of less than $15. An automated reviewer achieved near-human performance in evaluating paper quality, with generated papers exceeding top ML conference acceptance thresholds.

**Key Contributions:**
- First end-to-end framework for autonomous scientific discovery
- Demonstrated ability to produce conference-quality papers
- Open-source implementation available at https://github.com/SakanaAI/AI-Scientist
- Cost-effective research generation (<$15 per paper)

**Citations:** 14

---

### 2. Accelerating Scientific Discovery with Co-Scientist

Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirkovic, P., Myaskovsky, A., Glowaty, G., Weissenberger, F., Orlandi, A., Popovici, D., Palepu, A., Rong, K., Tanno, R., Saab, K., Zhang, F., Blum, J., Carroll, A., Kulkarni, K., Tomasev, N., & Zverinski, D. (2025). *Accelerating scientific discovery with Co-Scientist*. arXiv preprint arXiv:2502.18864. https://arxiv.org/abs/2502.18864v2

**Summary:** Co-Scientist is a multi-agent AI system built on Gemini for structured scientific thinking and hypothesis generation. The system employs asynchronous task execution and tournament evolution processes for self-improving hypothesis generation. Validated in three biomedical applications (drug repurposing, novel target discovery, and antimicrobial resistance mechanisms), Co-Scientist successfully identified new drug repurposing candidates and synergistic combination therapies for acute myeloid leukemia, validated through in vitro experiments.

**Key Contributions:**
- Multi-agent architecture with asynchronous task execution
- Tournament evolution for hypothesis refinement
- Real-world experimental validation in biomedical domain
- Scalable test-time compute benefits

**Citations:** 7

---

### 3. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). *The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search*. arXiv preprint arXiv:2504.08066. https://arxiv.org/abs/2504.08066v1

**Summary:** Building on the original AI Scientist, v2 introduces an end-to-end agentic system that produced the first entirely AI-generated peer-review-accepted workshop paper. Key improvements include elimination of human-authored code templates, effective generalization across diverse ML domains, and a novel progressive agentic tree-search methodology. The system incorporates a Vision-Language Model feedback loop for iterative figure refinement. One manuscript submitted to an ICLR workshop exceeded the human acceptance threshold, marking a historic milestone in autonomous research.

**Key Contributions:**
- First AI-generated paper accepted at peer-reviewed workshop
- Agentic tree search for experiment management
- VLM-enhanced figure refinement
- Generalization across ML domains without code templates

**Citations:** 6

---

### 4. Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents

Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Zhao, D., Rong, Y., Feng, T., & Bing, L. (2024). *Chain of Ideas: Revolutionizing research via novel idea development with LLM agents*. arXiv preprint arXiv:2410.13185. https://arxiv.org/abs/2410.13185v5

**Summary:** The Chain-of-Ideas (CoI) agent addresses the challenge of research ideation by organizing relevant literature in a chain structure that mirrors progressive research domain development. This organization enables LLMs to capture current advancements and enhance ideation capabilities. The Idea Arena evaluation protocol comprehensively assesses idea generation from multiple perspectives. The CoI agent consistently outperforms other methods, showing comparable quality to human researchers at a budget-friendly cost of $0.50 per candidate idea.

**Key Contributions:**
- Chain structure for literature organization
- Idea Arena evaluation protocol
- Human-comparable idea generation quality
- Cost-effective ideation ($0.50 per idea)

**Citations:** 4

---

### 5. Empowering Biomedical Discovery with AI Agents

Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A., Schwarz, J. R., Ektefaie, Y., Kondic, J., & Zitnik, M. (2024). *Empowering biomedical discovery with AI agents*. arXiv preprint arXiv:2404.02831. https://arxiv.org/abs/2404.02831v2

**Summary:** This vision paper conceptualizes AI scientists as systems capable of skeptical learning and reasoning that empower biomedical research through collaborative agents. Rather than replacing humans, biomedical AI agents combine human creativity with AI's ability to analyze large datasets and navigate hypothesis spaces. The framework incorporates large language models with structured memory for continual learning, integrating scientific knowledge and biological principles. Potential applications range from virtual cell simulation to developing new therapies.

**Key Contributions:**
- Human-AI collaborative framework
- Structured memory for continual learning
- Integration of scientific knowledge and principles
- Broad biomedical application potential

**Citations:** 3

---

### 6. MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents

Li, R., Patel, T., Wang, Q., & Du, X. (2024). *MLR-Copilot: Autonomous machine learning research based on large language model agents*. arXiv preprint arXiv:2408.14033. https://arxiv.org/abs/2408.14033v3

**Summary:** MLR-Copilot is an autonomous ML research framework consisting of three stages: idea generation, experiment implementation, and code execution. IdeaAgent, powered by an RL-tuned LLM, generates feasible research ideas from existing papers. ExperimentAgent converts plans into executable code using retrieved prototype code and optionally retrieves candidate models and data from HuggingFace. The framework supports iterative debugging and human feedback for improved outcomes, evaluated on five ML research tasks.

**Key Contributions:**
- Three-stage autonomous research pipeline
- RL-tuned LLM for idea generation
- Integration with HuggingFace for model/data retrieval
- Human-in-the-loop debugging capability

**Citations:** 3

---

### 7. Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas

Hu, X., Fu, H., Wang, J., Wang, Y., Li, Z., Xu, R., Lu, Y., Jin, Y., Pan, L., & Lan, Z. (2024). *Nova: An iterative planning and search approach to enhance novelty and diversity of LLM generated ideas*. arXiv preprint arXiv:2410.14255. https://arxiv.org/abs/2410.14255v2

**Summary:** Nova addresses the limitation of existing LLMs producing simplistic and repetitive suggestions through an enhanced planning and search methodology. The iterative process purposely plans external knowledge retrieval, progressively enriching idea generation with broader and deeper insights. Automated and human assessments show the framework generates 3.4 times more unique novel ideas than without it, and 2.5 times more top-rated ideas than state-of-the-art methods based on 170 seed papers.

**Key Contributions:**
- Iterative knowledge retrieval planning
- 3.4x increase in unique novel ideas
- Swiss Tournament evaluation methodology
- Superior novelty and diversity metrics

**Citations:** 3

---

### 8. AIDE: AI-Driven Exploration in the Space of Code

Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). *AIDE: AI-driven exploration in the space of code*. arXiv preprint arXiv:2502.13138. https://arxiv.org/abs/2502.13138v1

**Summary:** AIDE frames machine learning engineering as a code optimization problem, formulating trial-and-error as a tree search in the space of potential solutions. By strategically reusing and refining promising solutions, AIDE trades computational resources for enhanced performance. The system achieves state-of-the-art results on multiple ML engineering benchmarks, including Kaggle evaluations, OpenAI MLE-Bench, and METRS RE-Bench.

**Key Contributions:**
- Tree search formulation for code optimization
- Strategic solution reuse and refinement
- State-of-the-art benchmark performance
- Computational resource trade-off strategy

**Citations:** 3

---

### 9. LAB-Bench: Measuring Capabilities of Language Models for Biology Research

Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). *LAB-Bench: Measuring capabilities of language models for biology research*. arXiv preprint arXiv:2407.10362. https://arxiv.org/abs/2407.10362v3

**Summary:** LAB-Bench introduces over 2,400 multiple choice questions evaluating AI systems on practical biology research capabilities, including literature recall and reasoning, figure interpretation, database navigation, and DNA/protein sequence comprehension. Unlike textbook-style benchmarks, LAB-Bench focuses on tasks required for actual scientific research. Performance comparisons with human expert biology researchers establish baselines for automated research system development.

**Key Contributions:**
- 2,400+ practical biology research questions
- Focus on real research tasks vs. textbook knowledge
- Human expert performance baselines
- Public dataset availability on HuggingFace

**Citations:** 2

---

### 10. PaperBench: Evaluating AI's Ability to Replicate AI Research

Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., & Patwardhan, T. (2025). *PaperBench: Evaluating AI's ability to replicate AI research*. arXiv preprint arXiv:2504.01848. https://arxiv.org/abs/2504.01848v3

**Summary:** PaperBench evaluates AI agents' ability to replicate 20 ICML 2024 Spotlight and Oral papers from scratch, including understanding contributions, developing codebases, and executing experiments. The benchmark contains 8,316 individually gradable tasks with rubrics co-developed with original paper authors. An LLM-based judge automatically grades replication attempts. The best-performing agent (Claude 3.5 Sonnet with open-source scaffolding) achieved 21.0% average replication score, not yet outperforming human ML PhDs.

**Key Contributions:**
- 8,316 gradable replication tasks
- Author-validated evaluation rubrics
- LLM-based automated judging system
- Human baseline comparisons

**Citations:** 2

---

## Thematic Analysis

### Theme 1: Fully Automated Research Systems

Three papers present end-to-end autonomous research frameworks: The AI Scientist (Lu et al., 2024), The AI Scientist-v2 (Yamada et al., 2025), and MLR-Copilot (Li et al., 2024). These systems demonstrate the feasibility of completely automated research pipelines, from ideation to paper writing. The AI Scientist-v2 achieved a historic milestone by producing the first AI-generated paper accepted at a peer-reviewed workshop.

### Theme 2: Multi-Agent Collaborative Approaches

Co-Scientist (Gottweis et al., 2025) and the framework proposed by Gao et al. (2024) emphasize multi-agent architectures where specialized agents collaborate on different aspects of research. These systems incorporate asynchronous task execution and tournament-based evolution for continuous improvement, demonstrating superior performance through agent collaboration.

### Theme 3: Idea Generation and Novelty Enhancement

Chain of Ideas (Li et al., 2024) and Nova (Hu et al., 2024) specifically address the research ideation challenge. Both systems employ innovative strategies for organizing and retrieving knowledge to enhance idea novelty and diversity. Nova's 3.4x improvement in unique idea generation highlights the potential for systematic approaches to overcome LLM limitations in creative tasks.

### Theme 4: Evaluation Benchmarks

Two papers focus on evaluation frameworks: LAB-Bench (Laurent et al., 2024) for biology research capabilities and PaperBench (Starace et al., 2025) for AI research replication. These benchmarks establish crucial baselines for measuring AI research capabilities and tracking progress toward more capable autonomous scientists.

### Theme 5: Code Optimization and Engineering

AIDE (Jiang et al., 2025) frames ML engineering as a code optimization problem, demonstrating how tree search strategies can systematically explore solution spaces. This approach complements the broader research automation efforts by focusing on the implementation and experimentation phase.

---

## Key Findings

1. **Feasibility Demonstrated:** Multiple systems have demonstrated the feasibility of autonomous research, with AI-generated papers meeting peer-review standards.

2. **Cost Effectiveness:** Automated research can be highly cost-effective, with idea generation costing as little as $0.50 and full papers under $15.

3. **Human-AI Collaboration:** The most promising approaches combine human creativity with AI's analytical capabilities rather than attempting full automation.

4. **Domain Specificity:** While general frameworks exist, domain-specific adaptations (particularly in biomedical research) show enhanced performance.

5. **Evaluation Gap:** Current AI systems (21.0% replication score on PaperBench) have not yet surpassed human researcher performance, indicating significant room for improvement.

6. **Iterative Improvement:** Systems employing iterative refinement, tree search, and tournament evolution consistently outperform single-pass approaches.

---

## Research Gaps and Future Directions

1. **Generalization:** Current systems show limited generalization across domains; future work should address cross-domain adaptability.

2. **Creativity Enhancement:** While novelty has improved, truly groundbreaking discoveries remain elusive; enhancing creative reasoning is a key challenge.

3. **Human-in-the-Loop:** Optimal human-AI collaboration patterns require further investigation to maximize complementary strengths.

4. **Ethical Considerations:** Autonomous research raises questions about authorship, accountability, and research integrity that require systematic study.

5. **Scalability:** While individual systems demonstrate capability, scaling to research community-level impact remains unexplored.

6. **Long-term Planning:** Current systems focus on single-paper research; multi-project, long-term research programs represent an open challenge.

---

## Conclusion

The literature from 2023-2025 reveals rapid progress in AI scientists and autonomous research systems. From foundational frameworks like The AI Scientist to sophisticated multi-agent systems like Co-Scientist, the field has demonstrated that AI can meaningfully contribute to all stages of scientific discovery. Evaluation benchmarks like LAB-Bench and PaperBench provide crucial metrics for tracking progress, while current limitations highlight opportunities for future research. The transition from human-assisted to fully autonomous research is underway, with profound implications for scientific productivity and discovery acceleration.

---

## References

Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A., Schwarz, J. R., Ektefaie, Y., Kondic, J., & Zitnik, M. (2024). Empowering biomedical discovery with AI agents. *arXiv preprint arXiv:2404.02831*. https://arxiv.org/abs/2404.02831v2

Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirkovic, P., Myaskovsky, A., Glowaty, G., Weissenberger, F., Orlandi, A., Popovici, D., Palepu, A., Rong, K., Tanno, R., Saab, K., Zhang, F., Blum, J., Carroll, A., Kulkarni, K., Tomasev, N., & Zverinski, D. (2025). Accelerating scientific discovery with Co-Scientist. *arXiv preprint arXiv:2502.18864*. https://arxiv.org/abs/2502.18864v2

Hu, X., Fu, H., Wang, J., Wang, Y., Li, Z., Xu, R., Lu, Y., Jin, Y., Pan, L., & Lan, Z. (2024). Nova: An iterative planning and search approach to enhance novelty and diversity of LLM generated ideas. *arXiv preprint arXiv:2410.14255*. https://arxiv.org/abs/2410.14255v2

Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). AIDE: AI-driven exploration in the space of code. *arXiv preprint arXiv:2502.13138*. https://arxiv.org/abs/2502.13138v1

Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). LAB-Bench: Measuring capabilities of language models for biology research. *arXiv preprint arXiv:2407.10362*. https://arxiv.org/abs/2407.10362v3

Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Zhao, D., Rong, Y., Feng, T., & Bing, L. (2024). Chain of Ideas: Revolutionizing research via novel idea development with LLM agents. *arXiv preprint arXiv:2410.13185*. https://arxiv.org/abs/2410.13185v5

Li, R., Patel, T., Wang, Q., & Du, X. (2024). MLR-Copilot: Autonomous machine learning research based on large language model agents. *arXiv preprint arXiv:2408.14033*. https://arxiv.org/abs/2408.14033v3

Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. *arXiv preprint arXiv:2408.06292*. https://arxiv.org/abs/2408.06292v3

Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., & Patwardhan, T. (2025). PaperBench: Evaluating AI's ability to replicate AI research. *arXiv preprint arXiv:2504.01848*. https://arxiv.org/abs/2504.01848v3

Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. *arXiv preprint arXiv:2504.08066*. https://arxiv.org/abs/2504.08066v1

---

**Review Generated:** October 26, 2026

**Total Papers Reviewed:** 10

**Search Database:** arXiv (cs.AI category)

**Publication Window:** October 27, 2023 – October 26, 2025
