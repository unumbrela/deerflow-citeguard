# Systematic Literature Review: Towards Open World Detection

**Search Parameters:**
- **Database:** arXiv
- **Category:** cs.CV (Computer Vision)
- **Publication Period:** August 22, 2023 – August 21, 2025
- **Total Papers:** 10

---

## References (APA Format)

1. Chen, Z., Luo, Y., Wang, Z., Wang, Z., Yu, X., & Huang, Z. (2023). Open-CRB: Towards Open World Active Learning for 3D Object Detection. *arXiv preprint arXiv:2310.10391*. https://arxiv.org/abs/2310.10391

2. Guan, Y., Sun, C., Fu, C., Huang, Z., Yuan, C., & Li, C. (2025). Text-guided Visual Prompt DINO for Generic Segmentation. *arXiv preprint arXiv:2508.06146*. https://arxiv.org/abs/2508.06146

3. Kong, F., Chen, Y., Cai, J., & Modolo, D. (2024). Hyperbolic Learning with Synthetic Captions for Open-World Detection. *arXiv preprint arXiv:2404.05016*. https://arxiv.org/abs/2404.05016

4. Liang, M., Su, J.-C., Schulter, S., Garg, S., Zhao, S., Wu, Y., & Chandraker, M. (2024). AIDE: An Automatic Data Engine for Object Detection in Autonomous Driving. *arXiv preprint arXiv:2403.17373*. https://arxiv.org/abs/2403.17373

5. Mullappilly, S. S., Gehlot, A. S., Anwer, R. M., Khan, F. S., & Cholakkal, H. (2024). Semi-supervised Open-World Object Detection. *arXiv preprint arXiv:2402.16013*. https://arxiv.org/abs/2402.16013

6. Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024). DINO-X: A Unified Vision Model for Open-World Object Detection and Understanding. *arXiv preprint arXiv:2411.14347*. https://arxiv.org/abs/2411.14347

7. Rocky, A., & Wu, Q. M. J. (2025). SAM2Auto: Auto Annotation Using FLASH. *arXiv preprint arXiv:2506.07850*. https://arxiv.org/abs/2506.07850

8. Wei, G., Liu, Y., Yuan, X., Xue, X., Guo, L., Yang, Y., Zhao, C., Bai, Z., Zhang, H., & Xiao, R. (2025). OS-W2S: An Automatic Labeling Engine for Language-Guided Open-Set Aerial Object Detection. *arXiv preprint arXiv:2505.03334*. https://arxiv.org/abs/2505.03334

9. Yavuz, M., & Güney, F. (2024). O1O: Grouping of Known Classes to Identify Unknown Objects as Odd-One-Out. *arXiv preprint arXiv:2410.07514*. https://arxiv.org/abs/2410.07514

10. Yu, Y., Zhou, T., Sun, J., Qiao, L., Ding, L., Yuan, Y., & Wang, G. (2025). LAVA: Language Driven Scalable and Versatile Traffic Video Analytics. *arXiv preprint arXiv:2507.19821*. https://arxiv.org/abs/2507.19821

---

## Thematic Analysis

### 1. Foundation Models and Vision-Language Integration

**Kong et al. (2024)** introduced HyperLearner, which leverages hyperbolic learning with synthetic captions generated from vision-language models (VLMs). Their approach addresses the cost of manual annotation by bootstrapping dense synthetic captions and imposing hierarchical structure between visual and caption embeddings in hyperbolic space. This method achieved state-of-the-art performance on COCO, LVIS, ODinW, and RefCOCO benchmarks, outperforming GLIP, GLIPv2, and Grounding DINO.

**Ren et al. (2024)** presented DINO-X, a unified Transformer-based encoder-decoder architecture supporting text, visual, and customized prompts. Their Grounding-100M dataset with 100 million grounding samples enabled superior long-tailed object detection, achieving 56.0 AP on COCO and 63.3 AP on rare LVIS classes—a 5.8 AP improvement over previous SOTA.

**Guan et al. (2025)** proposed Prompt-DINO with three innovations: early fusion mechanism for unified text/visual prompts, order-aligned query selection for DETR architectures, and a generative data engine producing 0.5B training instances with 80.5% reduced label noise compared to conventional approaches.

### 2. Automatic Data Annotation and Labeling Engines

**Liang et al. (2024)** developed AIDE (Automatic Data Engine) for autonomous driving perception, leveraging VLMs and LLMs to automatically identify issues, curate data, improve models through auto-labeling, and verify via diverse scenario generation. Their iterative self-improvement process addresses the long-tailed distribution challenge in road object detection.

**Rocky & Wu (2025)** introduced SAM2Auto, the first fully automated video annotation pipeline requiring no human intervention. Their SMART-OD component combines automatic mask generation with open-world detection, while FLASH maintains consistent object tracking across video frames despite intermittent detection gaps. The system achieves manual annotation accuracy while eliminating labor costs.

**Wei et al. (2025)** created OS-W2S, an automatic labeling engine for language-guided open-set aerial object detection. Their MI-OAD dataset contains 163,023 images and 2 million image-caption pairs (40× larger than comparable datasets), spanning word-to-phrase-to-sentence language guidance levels. Training on MI-OAD improved Grounding DINO by +31.1 AP₅₀ and +34.7 Recall@10 under zero-shot transfer.

### 3. Novel Detection Paradigms and Cognitive Approaches

**Yavuz & Güney (2024)** proposed O1O (Odd-One-Out), drawing inspiration from human cognition research. By grouping known classes into superclasses and identifying similarities within groups, unknown objects are detected through odd-one-out scoring. This geometric cue-based approach significantly improves unknown recall without compromising known class performance, addressing the confusion introduced by noisy pseudo-labels.

**Mullappilly et al. (2024)** introduced SS-OWOD (Semi-supervised Open-World Detection), a more realistic formulation reducing annotation costs by casting incremental learning stages in a semi-supervised manner. Their SS-OWFormer detector uses feature-alignment schemes and pseudo-labeling for unknown detection, demonstrating effectiveness across MS COCO, PASCAL, Objects365, and DOTA datasets.

### 4. Domain-Specific Applications

**Chen et al. (2023)** investigated Open World Active Learning for 3D Object Detection (OWAL-3D), proposing Open Label Conciseness (OLC) to mine novel 3D objects with minimal annotation costs. Their Open-CRB framework integrates OLC with CRB active learning, supporting 15 baseline methods, 2 detector types (SECOND, PV-RCNN), and 3 datasets (KITTI, nuScenes, Waymo).

**Yu et al. (2025)** developed LAVA for language-driven traffic video analytics, enabling flexible natural language queries over petabyte-scale video databases. Their system includes multi-armed bandit sampling, video-specific open-world detection, and long-term trajectory extraction. LAVA improved F₁-scores by 14%, reduced MPAE by 0.39, achieved 86% top-k precision, and processed videos 9.6× faster than the most accurate baseline.

---

## Key Trends and Insights

### 1. Vision-Language Model Integration (2024-2025)
The field has shifted toward leveraging pre-trained VLMs for automatic caption generation and knowledge transfer, reducing reliance on expensive manual annotation. Hyperbolic embedding spaces and early fusion mechanisms have emerged as critical techniques for mitigating VLM hallucination noise.

### 2. Automated Annotation Pipelines (2024-2025)
Four papers (AIDE, SAM2Auto, OS-W2S, Prompt-DINO's data engine) focus on eliminating human annotation costs through fully automated pipelines. These systems generate datasets ranging from 0.5B to 2M samples, demonstrating scalability previously unattainable with manual labeling.

### 3. Cognitive and Geometric Approaches (2024)
O1O's human cognition-inspired superclass grouping represents a paradigm shift from purely appearance-based detection to geometric cue utilization, achieving unknown recall improvements without known class performance degradation.

### 4. Semi-supervised and Active Learning Formulations (2023-2024)
SS-OWOD and Open-CRB address practical deployment constraints by reducing oracle dependency. These formulations acknowledge that real-world systems cannot rely on continuous human intervention for incremental learning.

### 5. Domain Specialization (2023-2025)
Applications span autonomous driving (AIDE), aerial imagery (OS-W2S/MI-OAD), 3D point clouds (Open-CRB), and traffic video analytics (LAVA), indicating open-world detection's maturation beyond benchmark datasets to real-world operational scenarios.

---

## Performance Benchmarks Summary

| Paper | Key Metric | Improvement | Benchmark |
|-------|------------|-------------|-----------|
| HyperLearner (Kong et al., 2024) | Outperforms GLIP/GLIPv2/Grounding DINO | Consistent SOTA | COCO, LVIS, ODinW, RefCOCO |
| DINO-X (Ren et al., 2024) | 63.3 AP (rare classes) | +5.8 AP | LVIS-minival |
| Prompt-DINO (Guan et al., 2025) | Label noise reduction | 80.5% decrease | Open-world detection |
| MI-OAD (Wei et al., 2025) | +31.1 AP₅₀, +34.7 Recall@10 | Zero-shot transfer | Language-guided aerial detection |
| LAVA (Yu et al., 2025) | F₁-score, processing speed | +14%, 9.6× faster | Traffic video analytics |
| O1O (Yavuz & Güney, 2024) | Unknown recall | Significant improvement | Open-world detection |

---

## Research Gaps and Future Directions

1. **Hallucination Mitigation:** While hyperbolic learning (Kong et al., 2024) and dual-path verification (Guan et al., 2025) address VLM hallucination, more robust mechanisms are needed for production deployment.

2. **Cross-Domain Generalization:** Most methods are domain-specific (autonomous driving, aerial, 3D). Transfer learning between domains remains underexplored.

3. **Real-Time Performance:** Only LAVA (Yu et al., 2025) and SAM2Auto (Rocky & Wu, 2025) explicitly address computational efficiency. Production systems require further optimization.

4. **Long-Term Adaptation:** SS-OWOD (Mullappilly et al., 2024) and AIDE (Liang et al., 2024) propose iterative improvement, but long-term stability and catastrophic forgetting prevention need investigation.

5. **Evaluation Standardization:** The field lacks unified benchmarks comparing all approaches under identical conditions, making direct performance comparison challenging.

---

## Conclusion

The 2023-2025 literature demonstrates open-world detection's evolution from theoretical formulations to practical, deployment-ready systems. Key advances include vision-language model integration, fully automated annotation pipelines, cognitive-inspired detection mechanisms, and domain-specific applications. The field is transitioning from "detecting unknown objects" to "continuously adapting perception systems" that minimize human intervention while maximizing scalability and real-world applicability.

---

**Review Date:** October 26, 2026  
**Search Strategy:** arXiv cs.CV category, phrase match for "open world detection"  
**Inclusion Criteria:** Peer-reviewed preprints published between August 22, 2023 and August 21, 2025
