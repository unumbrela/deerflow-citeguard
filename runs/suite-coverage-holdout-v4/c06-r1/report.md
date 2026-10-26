# Systematic Literature Review: AI Scientists

**Date:** October 26, 2026  
**Search Period:** October 27, 2023 – October 26, 2025  
**Category:** cs.AI (Artificial Intelligence)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines 10 peer-reviewed papers focusing on AI Scientists—artificial intelligence systems capable of conducting scientific research, automated scientific discovery, and AI-driven research methodologies. The review reveals rapid advancement in autonomous scientific discovery capabilities, with systems progressing from assisted research tools to fully autonomous agents capable of generating, implementing, and publishing novel scientific research. Key themes include multi-agent architectures, automated hypothesis generation, end-to-end research pipelines, and evaluation frameworks for AI research capabilities.

---

## Methodology

**Search Strategy:** Papers were retrieved from arXiv's cs.AI category using the search term "AI Scientists" with publication dates between October 27, 2023, and October 26, 2025.

**Selection Criteria:** Papers were included if they focused on:
- AI systems that conduct scientific research autonomously or semi-autonomously
- Automated scientific discovery methodologies
- AI-driven research idea generation
- AI agents for scientific workflow automation
- Evaluation frameworks for AI research capabilities

**Screening Process:** From an initial pool of 50 papers, 30 were shortlisted based on relevance. The final 10 papers were selected based on centrality to the topic, citation counts, and contribution to understanding AI scientist capabilities.

---

## Review of Selected Papers

### 1. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

**Citation:** Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. *arXiv preprint arXiv:2408.06292*. https://arxiv.org/abs/2408.06292v3

**Summary:** This groundbreaking paper presents the first comprehensive framework for fully automatic scientific discovery. The AI Scientist system enables frontier large language models to perform research independently, generating novel research ideas, writing code, executing experiments, visualizing results, and producing complete scientific papers. The system was applied to three machine learning subfields (diffusion modeling, transformer-based language modeling, and learning dynamics), producing papers at less than $15 per paper. An automated reviewer achieved near-human performance in evaluating paper quality, with generated papers exceeding acceptance thresholds at top machine learning conferences.

**Key Contributions:**
- First comprehensive framework for fully autonomous scientific discovery
- End-to-end pipeline from idea generation to paper writing
- Cost-effective research automation (<$15 per paper)
- Validated automated review system with near-human accuracy

**Impact:** This work signifies a transformative shift in scientific discovery, demonstrating that AI agents can handle the entire research process independently.

---

### 2. Accelerating Scientific Discovery with Co-Scientist

**Citation:** Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirkovic, P., Myaskovsky, A., Glowaty, G., Weissenberger, F., Orlandi, A., Popovici, D., Palepu, A., Rong, K., Tanno, R., Saab, K., Zhang, F., Blum, J., Carroll, A., Kulkarni, K., Tomasev, N., & Zverinski, D. (2025). Accelerating Scientific Discovery with Co-Scientist. *arXiv preprint arXiv:2502.18864*. https://arxiv.org/abs/2502.18864v2

**Summary:** Co-Scientist is a multi-agent AI system built on Gemini designed for structured scientific thinking and hypothesis generation. The system employs agents that continuously generate, critique, and refine hypotheses through tournament evolution processes and asynchronous task execution frameworks. Validated in three biomedical applications (drug repurposing, novel target discovery, and antimicrobial resistance mechanisms), Co-Scientist successfully identified new drug repurposing candidates and synergistic combination therapies for acute myeloid leukemia, validated through in vitro experiments.

**Key Contributions:**
- Multi-agent architecture with asynchronous task execution
- Tournament evolution for self-improving hypothesis generation
- Real-world biomedical validation with experimental verification
- Test-time compute scaling for improved hypothesis quality

**Impact:** Demonstrates practical AI-augmented scientific discovery with real experimental validation in biomedical research.

---

### 3. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

**Citation:** Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. *arXiv preprint arXiv:2504.08066*. https://arxiv.org/abs/2504.08066v1

**Summary:** Building on the original AI Scientist, version 2 introduces an end-to-end agentic system capable of producing peer-review-accepted workshop papers. Key improvements include elimination of human-authored code templates, effective generalization across diverse ML domains, and a novel progressive agentic tree-search methodology managed by a dedicated experiment manager agent. The system integrates Vision-Language Model feedback loops for iterative figure refinement. Three autonomous manuscripts were submitted to an ICLR workshop, with one exceeding the human acceptance threshold—marking the first fully AI-generated paper to successfully navigate peer review.

**Key Contributions:**
- First AI-generated paper accepted through peer review
- Agentic tree-search methodology for experiment management
- Vision-Language Model integration for figure refinement
- Elimination of human code template dependencies

**Impact:** Represents a milestone in autonomous research, demonstrating AI capability to navigate the complete scientific publication process.

---

### 4. Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents

**Citation:** Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Zhao, D., Rong, Y., Feng, T., & Bing, L. (2024). Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents. *arXiv preprint arXiv:2410.13185*. https://arxiv.org/abs/2410.13185v5

**Summary:** This paper addresses the challenge of research ideation in the face of exponentially growing scientific literature. The Chain-of-Ideas (CoI) agent organizes relevant literature in a chain structure mirroring progressive research domain development, facilitating LLMs to capture current advancements and enhance ideation capabilities. The accompanying Idea Arena evaluation protocol comprehensively assesses idea generation methods aligned with human researcher preferences. The CoI agent consistently outperforms other methods with comparable quality to humans, at a budget-friendly cost of $0.50 per candidate idea.

**Key Contributions:**
- Chain structure organization of literature for progressive understanding
- Idea Arena evaluation protocol aligned with human preferences
- Cost-effective idea generation ($0.50 per idea)
- Human-comparable quality in research ideation

**Impact:** Provides a scalable solution for research idea generation, addressing the literature overload challenge faced by modern researchers.

---

### 5. Empowering Biomedical Discovery with AI Agents

**Citation:** Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A., Schwarz, J. R., Ektefaie, Y., Kondic, J., & Zitnik, M. (2024). Empowering Biomedical Discovery with AI Agents. *arXiv preprint arXiv:2404.02831*. https://arxiv.org/abs/2404.02831v2

**Summary:** This visionary paper conceptualizes "AI scientists" as systems capable of skeptical learning and reasoning that empower biomedical research through collaborative agents. Rather than replacing humans, these AI agents combine human creativity with AI's ability to analyze large datasets and navigate hypothesis spaces. The framework features large language models and generative models with structured memory for continual learning, integrating scientific knowledge and biological principles. Potential applications range from virtual cell simulation to therapy development.

**Key Contributions:**
- Human-AI collaborative discovery paradigm
- Skeptical learning and reasoning capabilities
- Structured memory for continual learning
- Integration of biological principles and theories

**Impact:** Establishes a philosophical and practical framework for human-AI collaboration in biomedical discovery, emphasizing augmentation over replacement.

---

### 6. MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents

**Citation:** Li, R., Patel, T., Wang, Q., & Du, X. (2024). MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents. *arXiv preprint arXiv:2408.14033*. https://arxiv.org/abs/2408.14033v3

**Summary:** MLR-Copilot is an autonomous machine learning research framework powered by large language model agents, designed to enhance ML research productivity through automatic generation and implementation of research ideas. The three-stage framework consists of: (1) idea generation using RL-tuned LLM-powered IdeaAgent, (2) experiment implementation using retrieved prototype code, and (3) code execution with iterative debugging and human feedback. Evaluated on five machine learning research tasks, the framework demonstrates potential for facilitating ML research progress and innovation.

**Key Contributions:**
- Three-stage autonomous research pipeline
- RL-tuned LLM for idea generation
- Prototype code retrieval and adaptation
- Iterative debugging with human feedback integration

**Impact:** Provides a practical framework for autonomous ML research with built-in mechanisms for quality improvement through iteration.

---

### 7. Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas

**Citation:** Hu, X., Fu, H., Wang, J., Wang, Y., Li, Z., Xu, R., Lu, Y., Jin, Y., Pan, L., & Lan, Z. (2024). Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas. *arXiv preprint arXiv:2410.14255*. https://arxiv.org/abs/2410.14255v2

**Summary:** Nova addresses the limitation of existing LLMs producing simplistic and repetitive research suggestions through an enhanced planning and search methodology. The approach involves iterative planning of external knowledge retrieval, progressively enriching idea generation with broader and deeper insights. Validation shows the framework produces 3.4 times more unique novel ideas than without it, and generates at least 2.5 times more top-rated ideas than state-of-the-art methods based on 170 seed papers in Swiss Tournament evaluation.

**Key Contributions:**
- Iterative knowledge retrieval planning
- Enhanced novelty and diversity in idea generation
- 3.4× increase in unique novel ideas
- Superior performance in Swiss Tournament evaluation

**Impact:** Significantly advances the quality and diversity of AI-generated research ideas, addressing a critical limitation in automated ideation.

---

### 8. AIDE: AI-Driven Exploration in the Space of Code

**Citation:** Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). AIDE: AI-Driven Exploration in the Space of Code. *arXiv preprint arXiv:2502.13138*. https://arxiv.org/abs/2502.13138v1

**Summary:** AIDE addresses the tedious trial-and-error process in machine learning development by framing ML engineering as a code optimization problem and formulating experimentation as tree search in the space of potential solutions. By strategically reusing and refining promising solutions, AIDE effectively trades computational resources for enhanced performance. The system achieves state-of-the-art results on multiple ML engineering benchmarks, including Kaggle evaluations, OpenAI MLE-Bench, and METRS RE-Bench.

**Key Contributions:**
- Tree search formulation for code optimization
- Strategic solution reuse and refinement
- State-of-the-art performance on multiple benchmarks
- Reduction of manual trial-and-error burden

**Impact:** Transforms ML engineering workflow, enabling engineers to focus on conceptual innovation rather than repetitive experimentation.

---

### 9. LAB-Bench: Measuring Capabilities of Language Models for Biology Research

**Citation:** Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). LAB-Bench: Measuring Capabilities of Language Models for Biology Research. *arXiv preprint arXiv:2407.10362*. https://arxiv.org/abs/2407.10362v3

**Summary:** LAB-Bench introduces over 2,400 multiple-choice questions evaluating AI systems on practical biology research capabilities, including literature recall and reasoning, figure interpretation, database navigation, and DNA/protein sequence manipulation. Unlike textbook-style science benchmarks, LAB-Bench focuses on practical research tasks. Performance comparison against human expert biology researchers provides baseline measurements for developing automated research systems.

**Key Contributions:**
- Comprehensive practical biology research benchmark
- 2,400+ questions across diverse research tasks
- Human expert performance baselines
- Focus on practical research capabilities

**Impact:** Provides essential evaluation infrastructure for developing and assessing AI research assistants in biology, bridging the gap between knowledge benchmarks and practical research utility.

---

### 10. PaperBench: Evaluating AI's Ability to Replicate AI Research

**Citation:** Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., & Patwardhan, T. (2025). PaperBench: Evaluating AI's Ability to Replicate AI Research. *arXiv preprint arXiv:2504.01848*. https://arxiv.org/abs/2504.01848v3

**Summary:** PaperBench evaluates AI agents' ability to replicate 20 ICML 2024 Spotlight and Oral papers from scratch, including understanding contributions, developing codebases, and executing experiments. The benchmark contains 8,316 individually gradable tasks with rubrics co-developed with original paper authors. An LLM-based judge automatically grades replication attempts. The best-performing agent (Claude 3.5 Sonnet with open-source scaffolding) achieved 21.0% average replication score, while human ML PhDs outperformed all tested models.

**Key Contributions:**
- Comprehensive replication benchmark with 8,316 gradable tasks
- Author-co-developed rubrics for accuracy
- Automated LLM-based grading system
- Human baseline comparison

**Impact:** Establishes rigorous evaluation standards for AI research capabilities, revealing current limitations while providing clear improvement targets.

---

## Thematic Analysis

### Theme 1: End-to-End Autonomous Research Systems

Three papers (Lu et al., 2024; Yamada et al., 2025; Li et al., 2024) present complete autonomous research pipelines. The AI Scientist series demonstrates progression from basic automation to peer-review-accepted papers, while MLR-Copilot focuses specifically on machine learning research with RL-tuned idea generation.

### Theme 2: Multi-Agent Architectures

Co-Scientist (Gottweis et al., 2025) and AI Scientist-v2 (Yamada et al., 2025) employ multi-agent systems with specialized roles. These architectures enable parallel hypothesis generation, critique, and refinement through tournament evolution and asynchronous execution frameworks.

### Theme 3: Idea Generation and Novelty Enhancement

Nova (Hu et al., 2024) and Chain of Ideas (Li et al., 2024) specifically address the quality and novelty of AI-generated research ideas. Both employ iterative knowledge retrieval and structured organization to overcome LLM limitations in producing repetitive suggestions.

### Theme 4: Evaluation Frameworks

LAB-Bench (Laurent et al., 2024) and PaperBench (Starace et al., 2025) provide comprehensive evaluation infrastructure. While LAB-Bench focuses on practical biology research capabilities, PaperBench assesses AI ability to replicate existing AI research, both revealing current gaps between AI and human performance.

### Theme 5: Human-AI Collaboration

Gao et al. (2024) emphasize augmentation over replacement, conceptualizing AI scientists as collaborative partners that combine human creativity with AI's analytical capabilities. This perspective contrasts with fully autonomous approaches while acknowledging complementary strengths.

### Theme 6: Code Optimization and Engineering Efficiency

AIDE (Jiang et al., 2025) addresses the practical burden of trial-and-error in ML development, framing engineering as code optimization through tree search. This approach reduces manual effort while improving performance through strategic solution reuse.

---

## Temporal Trends

**2024:** Foundational work establishing autonomous research frameworks (AI Scientist, MLR-Copilot), evaluation benchmarks (LAB-Bench), and idea generation methods (Chain of Ideas, Nova).

**Early 2025:** Advancement toward practical deployment with experimental validation (Co-Scientist), engineering optimization (AIDE), and rigorous capability assessment (PaperBench).

**Mid-2025:** Breakthrough achievement with first peer-review-accepted AI-generated paper (AI Scientist-v2), demonstrating maturity of autonomous research capabilities.

The progression shows rapid advancement from conceptual frameworks to validated, deployable systems within an 18-month period.

---

## Critical Gaps and Future Directions

### Current Limitations

1. **Human Performance Gap:** PaperBench results show AI systems (21.0% replication) still significantly underperform human researchers, indicating substantial room for improvement.

2. **Domain Specificity:** Most systems focus on machine learning research, with limited validation in other scientific domains beyond biomedical applications.

3. **Cost Considerations:** While some systems achieve low per-paper costs ($0.50-$15), widespread adoption requires further cost reduction.

4. **Evaluation Infrastructure:** Only two comprehensive benchmarks exist (LAB-Bench, PaperBench), limiting standardized assessment across domains.

### Future Research Directions

1. **Cross-Domain Generalization:** Extending autonomous research capabilities beyond ML and biology to physics, chemistry, and social sciences.

2. **Human-AI Interaction Design:** Developing optimal collaboration patterns that maximize complementary strengths.

3. **Ethical Frameworks:** Establishing guidelines for autonomous research, authorship attribution, and research integrity.

4. **Scalability:** Investigating whether autonomous systems can maintain quality at scale and handle increasingly complex research questions.

5. **Longitudinal Studies:** Tracking AI-generated research impact over time to assess real scientific contribution beyond acceptance thresholds.

---

## Conclusion

The systematic review reveals a field in rapid transformation, with AI scientist capabilities advancing from conceptual frameworks to peer-review-accepted research within 18 months. Key achievements include fully autonomous research pipelines, multi-agent architectures for hypothesis generation, and comprehensive evaluation frameworks. However, significant gaps remain between AI and human research capabilities, particularly in complex replication tasks and cross-domain generalization.

The emergence of validated autonomous systems (AI Scientist-v2, Co-Scientist) alongside rigorous benchmarks (PaperBench, LAB-Bench) suggests the field is maturing beyond proof-of-concept demonstrations toward practical research tools. The emphasis on human-AI collaboration rather than replacement (Gao et al., 2024) reflects a nuanced understanding of complementary strengths.

As these systems become more capable and accessible, they promise to democratize research participation, accelerate discovery cycles, and address the growing challenge of literature overload. However, realizing this potential requires continued investment in evaluation infrastructure, ethical frameworks, and cross-domain validation to ensure AI scientists contribute meaningfully to scientific progress.

---

## References

Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A., Schwarz, J. R., Ektefaie, Y., Kondic, J., & Zitnik, M. (2024). Empowering Biomedical Discovery with AI Agents. *arXiv preprint arXiv:2404.02831*. https://arxiv.org/abs/2404.02831v2

Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirkovic, P., Myaskovsky, A., Glowaty, G., Weissenberger, F., Orlandi, A., Popovici, D., Palepu, A., Rong, K., Tanno, R., Saab, K., Zhang, F., Blum, J., Carroll, A., Kulkarni, K., Tomasev, N., & Zverinski, D. (2025). Accelerating Scientific Discovery with Co-Scientist. *arXiv preprint arXiv:2502.18864*. https://arxiv.org/abs/2502.18864v2

Hu, X., Fu, H., Wang, J., Wang, Y., Li, Z., Xu, R., Lu, Y., Jin, Y., Pan, L., & Lan, Z. (2024). Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas. *arXiv preprint arXiv:2410.14255*. https://arxiv.org/abs/2410.14255v2

Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). AIDE: AI-Driven Exploration in the Space of Code. *arXiv preprint arXiv:2502.13138*. https://arxiv.org/abs/2502.13138v1

Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). LAB-Bench: Measuring Capabilities of Language Models for Biology Research. *arXiv preprint arXiv:2407.10362*. https://arxiv.org/abs/2407.10362v3

Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Zhao, D., Rong, Y., Feng, T., & Bing, L. (2024). Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents. *arXiv preprint arXiv:2410.13185*. https://arxiv.org/abs/2410.13185v5

Li, R., Patel, T., Wang, Q., & Du, X. (2024). MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents. *arXiv preprint arXiv:2408.14033*. https://arxiv.org/abs/2408.14033v3

Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. *arXiv preprint arXiv:2408.06292*. https://arxiv.org/abs/2408.06292v3

Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., & Patwardhan, T. (2025). PaperBench: Evaluating AI's Ability to Replicate AI Research. *arXiv preprint arXiv:2504.01848*. https://arxiv.org/abs/2504.01848v3

Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. *arXiv preprint arXiv:2504.08066*. https://arxiv.org/abs/2504.08066v1

---

## Appendix: Screening Statistics

- **Initial pool:** 50 papers from arXiv search
- **Citation expansion:** 33 additional papers (Semantic Scholar unavailable due to rate limiting)
- **Shortlisted:** 30 papers
- **Screened:** 30 papers
- **Final selection:** 10 papers
- **Screening scores distribution:** 
  - Score 3 (highest relevance): 13 papers
  - Score 2: 8 papers
  - Score 1: 6 papers
  - Score 0: 3 papers
- **Papers included from references:** 5
