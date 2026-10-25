# Systematic Literature Review: Robot Manipulation with Foundation Models

**Date**: 2025-10-25
**Papers surveyed**: 2
**Scope**: arXiv search query "robot manipulation foundation models", filtered to category cs.RO, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review surveyed recent arXiv papers on robot manipulation with foundation models in the cs.RO (Robotics) category. Only 2 papers were returned from the search, indicating that while foundation models for robotics is an emerging area, papers specifically addressing robot manipulation with foundation models in the cs.RO category over the last 2 years remain limited. The surveyed papers represent two distinct approaches: one focuses on automated scene generation for robot learning evaluation (Xu et al., 2026), while the other presents a large-scale Vision-Language-Action foundation model for robotic manipulation with emergent generalization capabilities (Yuan et al., 2026). Both papers demonstrate significant advances in scaling approaches and data generation methodologies for robot manipulation.

## Methodology

This review surveyed 2 arXiv papers retrieved on 2025-10-25 using the query "robot manipulation foundation models", filtered to category cs.RO, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Note on scope**: The search returned only 2 papers instead of the requested 10, suggesting that either (1) the field is still nascent with limited publications in cs.RO specifically, (2) relevant work may be published under adjacent categories (e.g., cs.AI, cs.CV, cs.LG), or (3) the specific query phrase may be too narrow. This limitation should be considered when interpreting the findings.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The small sample size limits the ability to identify robust thematic patterns across the literature.

## Themes

### Theme 1: Scaling and Data Generation for Foundation Models

Both papers address the critical challenge of scaling data and computation for foundation models in robotics. Yuan et al. (2026) present a comprehensive approach to building a large-scale Vision-Language-Action foundation model by creating a ~38,100-hour pretraining corpus through human-to-robot synthesis pipelines that convert egocentric hand demonstrations into robot trajectories across 15 platforms. This mirrors the scaling approaches that have proven successful in language and multimodal foundation models. Xu et al. (2026) tackle the complementary problem of generating diverse, high-quality training and evaluation data through automated scene generation, creating fine-grained functional object compositions that can be used for policy learning and robot manipulation evaluation. Together, these papers suggest that the field is recognizing data scale and diversity as fundamental bottlenecks for robot manipulation foundation models.

### Theme 2: Emergent Generalization Capabilities

A key finding across the surveyed literature is the emergence of generalization capabilities when scaling foundation models for robotics. Yuan et al. (2026) report that their Qwen-RobotManip model exhibits zero-shot instruction following, robustness to perturbations, reactive error recovery, and cross-embodiment transfer—capabilities that emerge from the large-scale pretraining rather than being explicitly programmed. This aligns with observations from language foundation models where scaling leads to emergent abilities. The model's substantial outperformance of prior state-of-the-art models across all out-of-distribution settings suggests that the scaling paradigm from language models may indeed transfer to robotic manipulation, as the research question posited.

## Convergences and Disagreements

**Convergences**: Both papers converge on the importance of scale and diversity in data for advancing robot manipulation capabilities. Both also emphasize the need for better evaluation frameworks—Yuan et al. (2026) explicitly note that standard benchmarks fail to capture pretraining quality and require out-of-distribution settings, while Xu et al. (2026) construct a benchmark spanning eight representative contact-geometry classes for evaluation.

**Disagreements**: The two papers take fundamentally different approaches to the problem. Xu et al. (2026) focus on the data generation side—creating better synthetic training environments and evaluation scenarios—while Yuan et al. (2026) focus on model architecture and pretraining pipelines. These are complementary rather than contradictory approaches, but they represent different investment priorities in the foundation model pipeline.

## Gaps and Open Questions

Based on the surveyed literature, several gaps emerge:

1. **Limited peer-reviewed validation**: Both papers are arXiv preprints without stated limitations in their abstracts, suggesting that detailed limitations analysis may appear only in the full papers or peer-reviewed versions.

2. **Evaluation benchmark standardization**: Yuan et al. (2026) explicitly note that standard benchmarks fail to capture pretraining quality, indicating a gap in standardized evaluation frameworks for robot manipulation foundation models.

3. **Cross-category coverage**: The narrow search results in cs.RO suggest that relevant work may be scattered across adjacent categories (cs.AI, cs.CV, cs.LG), indicating a need for more comprehensive multi-category reviews.

4. **Real-world deployment validation**: While Xu et al. (2026) mention real-world deployment and Yuan et al. (2026) validate on real-robot platforms, the extent of real-world validation across diverse environments remains unclear from the abstracts.

## Per-Paper Annotations

### Xu et al. (2026)

**Research question**: How can automated scene generation be improved to create fine-grained functional object compositions for robot manipulation evaluation and data generation?

**Methodology**: The authors present GIF, an agentic framework that treats the problem as disentangled reconstruction followed by relative pose recovery. CoGen produces instance-disentangled meshes with coarse initial poses using 2D and 3D generative models, while GPRM refines relative pose under geometric and physical guidance with a VLM verifier selecting the best candidate.

**Key findings**:
- GIF improves both asset quality and relation matching compared to state-of-the-art generators
- The framework reduces collision rate to below 1%
- A benchmark spanning eight representative contact-geometry classes was constructed for evaluation
- Synthesized data for policy learning reveals diversity scaling in both simulation and real-world deployment

**Limitations**: Not stated in abstract

### Yuan et al. (2026)

**Research question**: Can the scaling approach used in language and multimodality foundation models be applied to robotic manipulation to achieve genuine generalization?

**Methodology**: The authors present Qwen-RobotManip, a Vision-Language-Action foundation model built on Qwen-VL with unified alignment across representation, motion, and behavioral dimensions. A human-to-robot synthesis pipeline converts egocentric hand demonstrations into robot trajectories across 15 platforms, creating a ~38,100-hour pretraining corpus from open-source datasets and human videos.

**Key findings**:
- Qwen-RobotManip exhibits emergent generalization capabilities including zero-shot instruction following, robustness to perturbations, reactive error recovery, and cross-embodiment transfer
- The model substantially outperforms prior state-of-the-art models including π0.5 across all OOD settings
- Qwen-RobotManip ranks 1st in RoboChallenge with a 20% relative improvement
- Standard benchmarks fail to capture pretraining quality, requiring OOD settings like RoboCasa365, LIBERO-Plus, and EBench
- The model was validated on real-robot platforms including AgileX ALOHA, Franka, UR, and ARX

**Limitations**: Not stated in abstract

## References

Xu, L., Zhang, Z., Yan, M., Deng, S., Xia, C., Dong, M., Chen, J., Lyu, J., Gao, F., Zhang, Z., & Wang, H. (2026). GIF: Agentic generation of interactive and functional object compositions for robot learning. arXiv. https://arxiv.org/abs/2609.05927

Yuan, H., Liang, Z., Chen, A., Wang, Y., Li, H., Lin, P., Huang, Y., Lei, Z., Zhang, T., Zhang, J., Zhang, J., Fan, J., Zhou, G., Peng, Q., Lv, C., Chen, X., Yang, A., Huang, F., Lin, J., Liu, D., Zhou, J., Wu, C., & Chen, X.-H. (2026). Qwen-RobotManip technical report: Alignment unlocks scale for robotic manipulation foundation models. arXiv. https://arxiv.org/abs/2606.17846
