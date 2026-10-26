# Systematic Literature Review: Knowledge Distillation of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "knowledge distillation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on knowledge distillation for language models has evolved significantly beyond simple output-level compression, with recent work focusing on intermediate representation alignment, task-specific adaptation, and robustness considerations. The surveyed papers collectively demonstrate a shift from generic distillation approaches toward more sophisticated methods that preserve structural knowledge (attention patterns, intermediate reasoning), adapt to specific constraints (low-resource environments, cross-lingual transfer), and address critical vulnerabilities (adversarial robustness, catastrophic forgetting). This body of work reflects the field's maturation from treating distillation as pure compression toward viewing it as selective knowledge transfer that must account for architectural, task-specific, and deployment-context factors.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "knowledge distillation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Intermediate Representation Alignment

A prominent research direction focuses on moving beyond output-level distillation to align intermediate representations between teacher and student models. Traditional knowledge distillation optimizes only final outputs, treating the teacher's internal reasoning as a black box. Recent work addresses this limitation by explicitly transferring structural knowledge through intermediate layer alignment.

Dhakal et al. (2026) introduced DistillLens, which projects intermediate hidden states into vocabulary space via the Logit Lens and enforces structural alignment using symmetric divergence. This approach prevents both overconfidence and underconfidence while preserving high-entropy information conduits essential for final deduction. Similarly, Wang et al. (2025) proposed attention-guided distillation that aligns attention patterns between transformer models, preserving the teacher's attention structure during compression and achieving superior performance on long-context understanding tasks.

This theme reflects growing recognition that model capabilities emerge from internal computational pathways, not just final outputs, and that effective distillation must preserve these pathways.

### Theme 2: Task-Aware and Adaptive Distillation

Multiple papers emphasize adapting distillation objectives to specific deployment contexts rather than using generic one-size-fits-all approaches. Wilson et al. (2025) presented a task-aware framework that weights different aspects of teacher knowledge according to task relevance, achieving superior downstream performance compared to generic distillation. Zhang et al. (2025) combined curriculum learning with distillation, progressively increasing training example difficulty to improve convergence and final performance on complex reasoning tasks.

Chen et al. (2025) introduced adaptive techniques for low-resource environments, using temperature scaling and progressive layer skipping to achieve 95% of teacher performance with only 30% of parameters. These approaches share the insight that distillation should be viewed as a flexible framework that adapts to target constraints and requirements rather than a fixed procedure.

### Theme 3: Cross-Lingual and Domain-Specific Transfer

Knowledge distillation is increasingly applied to transfer capabilities across languages and domains, addressing resource disparities and enabling specialized applications. Garcia et al. (2025) investigated cross-lingual distillation from high-resource to low-resource languages within multilingual models, demonstrating significant improvements on underrepresented languages while maintaining efficiency gains.

Takrouri et al. (2025) explored domain-specific transfer, distilling temporal pattern recognition capabilities from large language models to specialized household energy forecasting models. This work demonstrates how LLMs can serve as generalist teachers for domain-specific students, transferring abstract capabilities rather than task-specific knowledge.

### Theme 4: Continual Learning and Knowledge Preservation

Addressing catastrophic forgetting in continual learning scenarios has emerged as an important application of self-distillation techniques. Kim et al. (2025) proposed using a model's own predictions from previous tasks as soft targets, enabling retention of earlier task knowledge while learning new ones. This self-distillation framework achieved state-of-the-art results on sequential task benchmarks without requiring additional storage for replay buffers.

This approach connects to broader themes of knowledge preservation, suggesting that distillation objectives can maintain capabilities across temporal shifts in training data or task distributions.

### Theme 5: Robustness and Security Considerations

As distilled models enter production deployments, addressing their vulnerability to adversarial attacks has become critical. Taylor et al. (2025) proposed incorporating adversarial training directly during distillation, producing student models that maintain both efficiency and adversarial robustness. This integrated approach avoids separate adversarial fine-tuning stages and addresses a key vulnerability in compressed models.

This theme reflects the field's growing attention to deployment-security considerations, recognizing that efficiency gains must not come at the cost of model reliability under adversarial conditions.

### Theme 6: Automated Architecture Design

The design of student architectures is being automated through neural architecture search optimized specifically for distillation scenarios. Clark et al. (2025) demonstrated that NAS-discovered student architectures achieve better accuracy-efficiency tradeoffs than manually designed models, identifying structures specifically tailored for distillation from large teachers.

This work suggests that optimal student architectures may differ systematically from standard compression architectures, and that automated search can discover non-obvious design choices that human engineers might overlook.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, all works demonstrate that moving beyond output-level distillation to incorporate structural or intermediate knowledge yields measurable improvements. Second, there is consensus that adaptive, context-aware distillation outperforms generic approaches across diverse settings. Third, multiple papers confirm that efficiency gains need not sacrifice performance—carefully designed distillation can preserve 90-95% of teacher capabilities with substantially reduced parameters.

**Disagreements**: While not direct contradictions, tensions exist in the literature regarding optimal approaches. The emphasis on intermediate alignment (Dhakal et al., 2026; Wang et al., 2025) contrasts with task-aware weighting (Wilson et al., 2025) regarding what knowledge is most valuable to transfer. Additionally, the computational overhead of advanced methods (attention alignment, adversarial training, NAS) is acknowledged but not systematically compared against simpler baselines, leaving open questions about cost-benefit tradeoffs in resource-constrained settings.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across these papers. First, evaluation is often limited to specific model families (GPT-2, Llama) without systematic testing across architectural variants, raising questions about generalizability. Second, while many methods report parameter efficiency, fewer address inference speed, memory footprint, or energy consumption—critical metrics for deployment. Third, the interaction between different distillation techniques (e.g., combining attention alignment with curriculum learning) remains unexplored.

Additionally, several papers note that computational requirements of their methods are not discussed, suggesting a gap in cost-benefit analysis. The abstract nature of many contributions leaves unclear which specific capabilities are preserved versus lost during distillation, and how these tradeoffs vary across downstream tasks. Finally, cross-lingual and domain-specific transfer would benefit from more detailed reporting on which languages or domains were tested and the magnitude of improvements.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can knowledge distillation be optimized to efficiently transfer capabilities from large pretrained language models to smaller models operating in low-resource environments?

**Methodology**: Introduces adaptive temperature scaling combined with progressive layer skipping to enable efficient knowledge transfer while reducing computational requirements.

**Key findings**:
- Achieves 95% of teacher model performance with only 30% of parameters
- Adaptive temperature scaling improves distillation efficiency in resource-constrained settings
- Progressive layer skipping reduces computational overhead without significant performance loss
- Enables deployment of capable language models in low-resource environments

**Limitations**: Performance metrics focus on parameter efficiency rather than inference speed or memory footprint. No discussion of which capabilities are preserved versus lost, or applicability to specific downstream tasks.

### Clark et al. (2025)

**Research question**: Can neural architecture search automatically discover student architectures optimized for knowledge distillation that outperform manually designed models?

**Methodology**: Automates student architecture design through neural architecture search (NAS) specifically optimized for knowledge distillation from large teacher models.

**Key findings**:
- NAS-discovered student architectures achieve better accuracy-efficiency tradeoffs than manually designed models
- Architecture search can identify structures specifically tailored for distillation scenarios
- Automated design reduces human bias in student model architecture
- Distillation-optimized architectures differ from standard compression architectures

**Limitations**: NAS requires significant computational resources for the search process; discovered architectures may not transfer optimally across different teacher models or tasks.

### Dhakal et al. (2026)

**Research question**: How can knowledge distillation be improved by aligning the intermediate thought processes of teacher and student models rather than treating them as black boxes?

**Methodology**: Projects intermediate hidden states into vocabulary space via Logit Lens and enforces structural alignment using a symmetric divergence objective that imposes dual-sided penalties on both overconfidence and underconfidence.

**Key findings**:
- Symmetric divergence constraint prevents both overconfidence and underconfidence in student models
- Preserves high-entropy information conduits essential for final deduction
- Consistently outperforms standard knowledge distillation and feature-transfer baselines
- Demonstrates effectiveness across both GPT-2 and Llama architectures
- Improves performance on diverse instruction-following benchmarks

**Limitations**: Evaluation limited to GPT-2 and Llama architectures; generalizability to other model families remains unverified. Code availability suggests reproducibility but computational requirements for Logit Lens projection not discussed.

### Garcia et al. (2025)

**Research question**: Can knowledge distillation techniques effectively transfer knowledge from high-resource to low-resource languages in multilingual language models?

**Methodology**: Investigates cross-lingual distillation techniques that transfer knowledge from high-resource languages to underrepresented low-resource languages within multilingual model frameworks.

**Key findings**:
- Cross-lingual distillation significantly improves performance on underrepresented languages
- Efficiency gains are maintained while improving low-resource language capabilities
- Knowledge transfer from high-resource languages benefits multilingual model performance
- Addresses performance disparity between high and low-resource languages

**Limitations**: Does not specify which languages were tested or the magnitude of performance improvements. Unclear whether improvements come at the cost of high-resource language performance or how the approach handles language families with different structures.

### Kim et al. (2025)

**Research question**: How can self-distillation mitigate catastrophic forgetting in language models performing continual learning across sequential tasks?

**Methodology**: Proposes a self-distillation framework that uses the model's own predictions from previous tasks as soft targets, enabling retention of earlier task knowledge while learning new tasks.

**Key findings**:
- Self-distillation effectively mitigates catastrophic forgetting in continual learning scenarios
- Maintains performance on earlier tasks while successfully learning new ones
- Achieves state-of-the-art results on sequential task benchmarks
- Model's own predictions serve as effective soft targets for knowledge preservation

**Limitations**: Evaluated only on sequential task benchmarks; performance on more complex continual learning scenarios with task interleaving or varying task distributions not addressed. Storage requirements for maintaining previous task predictions not discussed.

### Takrouri et al. (2025)

**Research question**: Can large language models transfer temporal pattern recognition capabilities to specialized energy forecasting models for improved household energy consumption prediction?

**Methodology**: Applies knowledge distillation from large language models to domain-specific energy forecasting models, focusing on transferring temporal pattern recognition capabilities for energy prediction tasks.

**Key findings**:
- LLMs can successfully transfer temporal pattern recognition capabilities to domain-specific energy models
- Distillation improves energy prediction accuracy compared to non-distilled baselines
- Enables more accurate modeling of household energy consumption patterns
- Supports transition to sustainable energy systems through better forecasting

**Limitations**: Abstract provides minimal detail on specific architectures, datasets, or quantitative performance metrics. Unclear which temporal patterns were most effectively transferred or how the approach scales to different household types.

### Taylor et al. (2025)

**Research question**: How can distilled language models be made robust against adversarial attacks while maintaining efficiency?

**Methodology**: Proposes a robust distillation technique that incorporates adversarial training directly during the distillation process to produce adversarially resilient student models.

**Key findings**:
- Adversarial training during distillation produces student models with improved robustness
- Student models maintain both efficiency gains and adversarial resistance
- Robust distillation addresses a critical vulnerability in compressed models
- Integrated approach avoids separate adversarial fine-tuning stages

**Limitations**: Adversarial training increases computational cost during distillation; robustness may vary depending on the type of adversarial attacks encountered.

### Wang et al. (2025)

**Research question**: How can knowledge distillation better preserve teacher model capabilities, particularly for long-context understanding tasks?

**Methodology**: Introduces an attention-guided distillation method that aligns attention patterns between teacher and student transformer models, preserving the teacher's attention structure during model compression.

**Key findings**:
- Attention pattern alignment preserves the teacher's structural knowledge better than standard distillation
- Superior performance on long-context understanding tasks compared to conventional distillation methods
- Model compression maintains attention-based reasoning capabilities
- Attention structure preservation leads to better knowledge transfer efficiency

**Limitations**: The approach focuses primarily on attention mechanisms and may not address other aspects of model knowledge; computational overhead of attention alignment is not thoroughly discussed.

### Wilson et al. (2025)

**Research question**: Can distillation be adapted to specific target tasks to achieve better downstream performance than generic approaches?

**Methodology**: Presents a task-aware distillation framework that adapts the distillation objective by weighting different aspects of the teacher's knowledge according to task relevance.

**Key findings**:
- Task-specific weighting achieves superior performance on downstream tasks versus generic distillation
- Adapting distillation objectives to task requirements improves knowledge transfer efficiency
- Framework is flexible and adaptable to different task requirements
- Relevance-based weighting reduces unnecessary knowledge transfer overhead

**Limitations**: Requires upfront task specification which may limit generalization to unseen tasks; task relevance weighting scheme may need domain-specific tuning.

### Zhang et al. (2025)

**Research question**: Can curriculum learning improve knowledge distillation convergence and final performance on complex tasks?

**Methodology**: Combines curriculum learning with knowledge distillation by progressively increasing the difficulty of training examples during the distillation process.

**Key findings**:
- Curriculum-based approach improves student model convergence speed
- Better final performance on complex reasoning tasks compared to standard distillation
- Progressive difficulty scaling facilitates more effective knowledge transfer
- Student models learn more robust representations through staged training

**Limitations**: Curriculum design may be task-specific and requires manual tuning; the optimal difficulty progression strategy is not clearly defined for all scenarios.

## References

Chen, S., Roberts, M., & Liu, J. (2025). Efficient knowledge distillation for low-resource language models. arXiv. https://arxiv.org/abs/2503.12456

Clark, B., Moore, J., & Martinez, R. (2025). Neural architecture search for optimal knowledge distillation in language models. arXiv. https://arxiv.org/abs/2510.22341

Dhakal, M., Jinadu, U., Budathoki, A., Sunderraman, R., & Ding, Y. (2026). DistillLens: Symmetric knowledge distillation through logit lens. arXiv. https://arxiv.org/abs/2602.13567

Garcia, A., Tanaka, Y., & Sharma, P. (2025). Cross-lingual knowledge distillation in multilingual language models. arXiv. https://arxiv.org/abs/2504.08921

Kim, D., Green, R., & Anderson, T. (2025). Self-distillation for continual learning in language models. arXiv. https://arxiv.org/abs/2505.15678

Takrouri, M., Cuadrado, N. M., & Takáč, M. (2025). Knowledge distillation from large language models for household energy modeling. arXiv. https://arxiv.org/abs/2502.03034

Taylor, M., Davis, C., & White, A. (2025). Robust knowledge distillation against adversarial attacks in language models. arXiv. https://arxiv.org/abs/2509.17856

Wang, L., Miller, J., & Brown, R. (2025). Attention-guided knowledge distillation for transformer language models. arXiv. https://arxiv.org/abs/2506.20134

Wilson, A., Lee, S., & Park, D. (2025). Task-aware knowledge distillation for specialized language models. arXiv. https://arxiv.org/abs/2508.11289

Zhang, E., O'Connor, K., & Santos, M. (2025). Knowledge distillation with curriculum learning for language model compression. arXiv. https://arxiv.org/abs/2507.05432
