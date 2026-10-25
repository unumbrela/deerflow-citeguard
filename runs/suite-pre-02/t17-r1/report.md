# Systematic Literature Review: Parameter-Efficient Fine-Tuning

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on parameter-efficient fine-tuning (PEFT) from the past two years reveals a field in rapid evolution, driven by the need to adapt increasingly large foundation models without the prohibitive cost of full fine-tuning. The surveyed papers collectively demonstrate that PEFT methods have matured beyond simple low-rank adaptation approaches, with innovations spanning adaptive rank allocation, geometry-aware gradient projection, quantum-inspired parameterization, and architecture-specific adaptations for emerging model families like Mamba. A strong consensus emerges that leveraging pre-trained weight structure and enabling dynamic parameter allocation significantly improves efficiency and performance. However, critical gaps remain in privacy preservation for federated PEFT settings, scalability to ultra-large models, and comprehensive theoretical foundations for many proposed methods.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Rank Allocation and Dynamic Parameter Distribution

A prominent research direction focuses on moving beyond uniform parameter allocation across model layers. Multiple papers recognize that different layers or components have heterogeneous adaptation requirements, motivating dynamic allocation strategies. LAARA introduces Fisher-guided rank allocation that dynamically assigns adapter ranks per layer using lightweight diagonal Fisher estimates, demonstrating that uniform rank allocation is suboptimal (Tripathi et al., 2026). Similarly, FedARA extends this concept to federated learning settings, employing dynamic rank allocation to identify critical ranks progressively while using truncated SVD adaptation to handle data heterogeneity across clients (Wu et al., 2025). These approaches share the insight that static, one-size-fits-all parameter budgets waste capacity on layers that require less adaptation while starving layers that need more.

### Theme 2: Exploiting Pre-trained Weight Structure

Several methods leverage the geometric or structural information already encoded in pre-trained weights rather than learning updates independently. PiCa projects gradients onto the principal column space of pre-trained weights using SVD-based decomposition, providing theoretical guarantees that this inductive bias improves adaptation efficiency (Hwang et al., 2025). GenFT takes a complementary approach, using a deterministic weight generator conditioned on the pre-trained weights W0 to produce task-specific updates through row and column transformations with nonlinear activations (Xu et al., 2025). Both methods share the philosophy that pre-trained weights contain valuable structural information that should guide the fine-tuning process, rather than treating ΔW as independent of W0.

### Theme 3: Architecture-Specific PEFT for Emerging Model Families

As new model architectures challenge Transformer dominance, PEFT methods are being adapted to their unique characteristics. MambaPEFT conducts exploratory analysis of applying PEFT to Mamba, a State Space Model alternative to Transformers, finding that PEFT performs even more effectively for Mamba than Transformers when methods are properly adapted to the architecture (Yoshimura et al., 2024). Memba builds on this by introducing membrane-driven PEFT specifically designed for Mamba's temporal processing dynamics, using Leaky Integrate Membrane neurons as bio-inspired gating mechanisms that naturally accumulate potentials over time (Lee et al., 2025). This theme reflects the recognition that PEFT methods cannot be purely architecture-agnostic — the best adaptation strategies depend on the underlying model structure.

### Theme 4: Cross-Layer Information Flow and Representation Reuse

Beyond modifying weight updates within layers, recent work explores leveraging information flow across layers during fine-tuning. Echo-LoRA collects boundary hidden states from deeper layers, aggregates them into sample-level "echo" representations, and injects these signals into shallow LoRA modules via lightweight projection and gating networks (Peng et al., 2026). Crucially, the echo path is discarded after training, adding no inference-time overhead. This approach recognizes that intermediate representations formed during forward passes contain valuable information that standard PEFT methods leave unused, and that harvesting this information during training can improve adaptation without deployment costs.

### Theme 5: Ultra-Efficient Parameterization Through Novel Computational Paradigms

Pushing parameter efficiency to extremes, some work explores fundamentally different parameterization schemes. Quantum-PEFT leverages quantum unitary parameterization with Pauli parameterization, achieving parameter counts that grow logarithmically with dimension rather than linearly as in LoRA-based methods (Koike-Akino et al., 2025). While requiring quantum computing infrastructure, this approach demonstrates that dramatic parameter reductions are theoretically possible while maintaining competitive performance. This represents a more radical departure from conventional PEFT, questioning whether low-rank matrix decomposition is the optimal path to efficiency.

### Theme 6: Privacy and Security in Federated PEFT

As PEFT is increasingly deployed in federated learning settings, new vulnerabilities emerge. Gradient inversion attacks demonstrate that even when only adapter module gradients are shared, attackers can reconstruct fine-tuning data with high fidelity (Sami et al., 2025). This work highlights that PEFT's efficiency gains in federated settings come with previously underappreciated privacy risks, motivating the need for privacy-preserving mechanisms specifically designed for PEFT rather than simply applying standard federated learning defenses.

## Convergences and Disagreements

**Convergences**: The surveyed papers exhibit strong agreement on several points. First, there is universal consensus that leveraging pre-trained weight structure improves PEFT efficiency — whether through SVD-based projection (Hwang et al., 2025), W0-conditioned generation (Xu et al., 2025), or Fisher-guided allocation (Tripathi et al., 2026). Second, all empirical papers report that their methods match or exceed baseline LoRA performance while using fewer or comparable parameters, suggesting the field has moved beyond the question of "whether PEFT works" to "how to make PEFT work best." Third, papers addressing federated or distributed settings agree that heterogeneity across clients or devices requires adaptive rather than static parameter configurations (Wu et al., 2025).

**Disagreements**: The surveyed literature shows few direct contradictions, reflecting the early-stage nature of many proposed methods. However, implicit tensions exist between architecture-specific versus architecture-agnostic approaches. Mamba-focused papers argue that PEFT methods must be tailored to specific architectures (Yoshimura et al., 2024; Lee et al., 2025), while other methods like PiCa and GenFT are presented as general-purpose approaches applicable across NLP and vision tasks without architectural modification (Hwang et al., 2025; Xu et al., 2025). Additionally, Quantum-PEFT's claim that quantum parameterization is the path to ultra-efficiency (Koike-Akino et al., 2025) stands in tension with classical methods that achieve strong efficiency through algorithmic rather than hardware innovations.

## Gaps and Open Questions

Several critical gaps emerge from the collective limitations acknowledged across the surveyed papers. First, privacy preservation in federated PEFT remains largely unaddressed — while Sami et al. (2025) demonstrate gradient inversion attacks, no surveyed paper proposes comprehensive defenses, leaving a significant vulnerability in production deployments. Second, scalability to ultra-large models (hundreds of billions of parameters) is rarely evaluated; methods like GenFT's pilot study on LLaMA-7B (Xu et al., 2025) and Echo-LoRA's evaluation up to LLaMA3-8B (Peng et al., 2026) suggest most work targets modest model sizes. Third, theoretical foundations remain incomplete — while PiCa provides theoretical grounding for SVD-based projection (Hwang et al., 2025), many methods including LAARA's Fisher estimation and Memba's membrane mechanisms rely primarily on empirical validation. Fourth, computational overhead during training is often unreported; methods requiring SVD computation, Fisher estimation, or cross-layer communication may trade parameter efficiency for increased training time or memory. Finally, the survey paper by Zhang et al. (2025) notes that systematic understanding of which PEFT methods work best for which foundation model types remains fragmented, with adaptation strategies varying across language, vision, and multimodal models without clear design principles.

## Per-Paper Annotations

### Koike-Akino et al. (2025)

**Research question**: Can quantum computation enable more parameter-efficient fine-tuning than classical low-rank methods?
**Methodology**: Introduces Quantum-PEFT using quantum unitary parameterization with Pauli parameterization, where trainable parameters grow logarithmically with dimension instead of linearly as in LoRA-based methods.
**Key findings**:
- Quantum-PEFT achieves vanishingly smaller trainable parameters than lowest-rank LoRA as dimensions grow
- Parameter count grows logarithmically with ambient dimension versus linearly for LoRA-based methods
- Maintains competitive performance despite dramatically reduced parameter counts
- Demonstrated significant advantages on language and vision transfer learning benchmarks
**Limitations**: Requires quantum computing infrastructure which limits practical deployment; may have simulation overhead when run on classical hardware limiting real-world applicability.

### Lee et al. (2025)

**Research question**: How to address the unique temporal processing dynamics of State Space Models in PEFT for Mamba rather than simply applying Transformer-tailored methods?
**Methodology**: Proposes Memba with Leaky Integrate Membrane (LIM) neurons as bio-inspired gating mechanisms that accumulate membrane potentials over time, strategically combined with LoRA and cross-layer membrane transfer to enhance temporal modeling.
**Key findings**:
- LIM neurons enhance selective information retention through bio-inspired gating mechanisms
- Achieves substantial improvements over existing PEFT methods across both language and vision tasks
- Significantly improves Mamba's temporal modeling capabilities
- Strategic combination of LIM neurons with LoRA and cross-layer membrane transfer proves effective
**Limitations**: Abstract does not explicitly acknowledge limitations; computational overhead of LIM neurons not discussed.

### Peng et al. (2026)

**Research question**: How to improve LoRA-style PEFT methods by utilizing intermediate representations from deeper layers that are typically left unused?
**Methodology**: Collects boundary hidden states from deeper source layers, aggregates them into sample-level echo representations, and injects the signal into shallow LoRA/DoRA modules via lightweight projection and gating networks with answer-only masking, masked distillation, and stochastic routing for stability.
**Key findings**:
- Exceeds reported LoRA baselines by 5.7 percentage points on average across eight commonsense reasoning benchmarks
- Under reproduced baselines in unified implementation, achieves 3.0 points average gain
- When combined with DoRA, achieves additional 2.7 points improvement
- Echo path is discarded after training, adding no inference-time parameters or computation
- Works effectively across LLaMA-7B, LLaMA2-7B, and LLaMA3-8B models
**Limitations**: Evaluation limited to commonsense reasoning benchmarks; effectiveness on other task types not demonstrated in abstract.

### Sami et al. (2025)

**Research question**: How can the privacy of fine-tuning data in federated PEFT be compromised via malicious design of pretrained models and trainable adapter modules?
**Methodology**: Demonstrates gradient inversion attacks on adapter-based PEFT mechanism, showing that attackers can reconstruct local data samples of target users using only accessible adapter gradients shared with the server.
**Key findings**:
- Gradient inversion attacks can successfully reconstruct local data samples from adapter gradients alone
- Large batches of fine-tuning images can be retrieved with high fidelity
- Privacy vulnerabilities exist even when only lightweight adapter module gradients are shared
- Attack highlights critical need for privacy-preserving mechanisms specifically designed for PEFT in federated learning
**Limitations**: Focus specifically on adapter-based PEFT; effectiveness against other PEFT methods (LoRA, prompt tuning) not addressed in abstract.

### Tripathi et al. (2026)

**Research question**: How can we optimize rank allocation across transformer layers for parameter-efficient fine-tuning instead of using uniform rank allocation?
**Methodology**: They propose LAARA, a search-free framework that dynamically allocates ranks using lightweight diagonal Fisher estimates computed during training, combining projection-wise normalization, logarithmic compression, blended adapter importance estimation, and vote-to-change dampening mechanism.
**Key findings**:
- Uniform rank allocation is theoretically and empirically suboptimal for LoRA across transformer layers
- LAARA matches or outperforms LoRA, AdaLoRA, DyLoRA, and BitFit on GLUE and MathInstruct benchmarks
- LAARA achieves comparable performance while using significantly fewer trainable parameters than competing methods
- Fisher-guided rank allocation provides stable and efficient rank adaptation without search overhead
**Limitations**: The framework requires Fisher information matrix estimation which adds computational overhead during training; the anonymous code repository suggests the work may still be under review limiting reproducibility verification.

### Wu et al. (2025)

**Research question**: How to address privacy and efficiency challenges in federated parameter-efficient fine-tuning of pre-trained language models on resource-constrained devices with heterogeneous data?
**Methodology**: Proposes FedARA, a framework using truncated SVD adaptation for enhanced feature representation across clients, dynamic rank allocation to progressively identify critical ranks, and rank-based module pruning to automatically remove inactive modules.
**Key findings**:
- Outperforms baselines by 6.95% to 8.49% across various datasets and models under heterogeneous data conditions
- Improves communication efficiency by 2.40× compared to fixed parameter configurations
- Reduces total training time on edge devices by up to 48.90%
- Reduces energy consumption on edge devices by up to 46.95%
- Truncated SVD adaptation significantly mitigates adverse effects of data heterogeneity across clients
**Limitations**: Abstract does not explicitly acknowledge limitations; evaluation scope appears limited to specific datasets and model architectures tested.

### Xu et al. (2025)

**Research question**: How can we better leverage structural information in pretrained weights for parameter-efficient fine-tuning rather than learning updates independently?
**Methodology**: They propose GenFT, a W0-conditioned PEFT method using a deterministic weight generator with row and column transformations and nonlinear activations, plus shared-specific decomposition for cross-layer information reuse and layer-specific flexibility.
**Key findings**:
- Conditioning weight updates on pretrained weights (W0) improves performance over independent learning of updates
- GenFT achieves competitive or better average performance across NLP and computer vision benchmarks
- Shared-specific decomposition effectively balances cross-layer information reuse and layer-specific flexibility
- Feasible for generative models as demonstrated in LLaMA-7B pilot study
**Limitations**: Pilot study on LLaMA-7B is limited in scope; method may not scale well to larger models without further optimization and validation.

### Yoshimura et al. (2024)

**Research question**: How can existing PEFT methods for Transformers be adapted or modified to effectively fine-tune Mamba-based models?
**Methodology**: Conducts exploratory analysis of existing Transformer PEFT methods applied to Mamba, modifies methods to better align with Mamba architecture, and proposes new Mamba-specific PEFT methods leveraging Mamba's distinctive structure.
**Key findings**:
- PEFT performs more effectively for Mamba than for Transformers
- Existing Transformer PEFT methods can be adapted for Mamba with modifications
- New Mamba-specific PEFT methods leveraging distinctive Mamba structure show improved performance
- Combining multiple PEFT methods effectively produces a framework outperforming previous works
- Provides reproducible framework with code release planned after publication
**Limitations**: Exploratory analysis nature; abstract does not specify which PEFT methods underperformed or specific architectural challenges encountered.

### Zhang et al. (2025)

**Research question**: What are the current techniques, trends, and applications of PEFT across diverse foundation models?
**Methodology**: They provide a comprehensive survey systematically reviewing key categories and core mechanisms of PEFT across diverse foundation models, exploring recent applications and identifying future research directions.
**Key findings**:
- PEFT techniques vary significantly across different types of foundation models including language, vision, and multimodal models
- Systematic categorization reveals distinct adaptation strategies needed for different foundation model architectures
- PEFT has been successfully applied across various domains demonstrating broad versatility and practical utility
- Several promising research directions are identified for improving PEFT methods in terms of efficiency and performance
**Limitations**: As a survey paper, it does not propose new methods; coverage may not be exhaustive given the rapidly evolving PEFT field with new methods emerging frequently.

### Hwang et al. (2025)

**Research question**: How can we improve parameter-efficient fine-tuning by exploiting the geometry of pre-trained weights with solid theoretical grounding?
**Methodology**: They introduce PiCa which projects gradients onto the principal column space of pre-trained weights using SVD-based approach, with a novel weight-sharing strategy for enhanced parameter efficiency and theoretical proofs.
**Key findings**:
- Projecting gradients onto the principal column space of pre-trained weights provides effective inductive bias for adaptation
- PiCa consistently outperforms state-of-the-art baselines under comparable or smaller parameter budgets
- The method has solid theoretical foundation unlike prior SVD-based methods such as SVFT
- Effective across diverse NLP and vision tasks demonstrating generalizability
**Limitations**: SVD computation can be expensive for very large models; theoretical analysis may have assumptions that do not hold in all practical scenarios.

## References

Hwang, J., Cho, W., & Kim, T. (2025). PiCa: Parameter-efficient fine-tuning with column space projection. arXiv. https://arxiv.org/abs/2505.20211

Koike-Akino, T., Tonin, F., Wu, Y., Wu, F. Z., Candogan, L. N., & Cevher, V. (2025). Quantum-PEFT: Ultra parameter-efficient fine-tuning. arXiv. https://arxiv.org/abs/2503.05431

Lee, D., Li, Y., Yin, R., Xiao, S., & Panda, P. (2025). Memba: Membrane-driven parameter-efficient fine-tuning for Mamba. arXiv. https://arxiv.org/abs/2506.18184

Peng, Y., Jin, P., Gong, J., Chen, X., Xu, L., Su, N., & Ran, Y. (2026). Echo-LoRA: Parameter-efficient fine-tuning via cross-layer representation injection. arXiv. https://arxiv.org/abs/2605.08177

Sami, H. U., Sen, S., Roy-Chowdhury, A. K., Krishnamurthy, S. V., & Guler, B. (2025). Gradient inversion attacks on parameter-efficient fine-tuning. arXiv. https://arxiv.org/abs/2506.04453

Tripathi, A., Singh, S. D., Sahoo, P., & Saha, S. (2026). LAARA: Layer-aware adaptive rank allocation for parameter-efficient fine-tuning. arXiv. https://arxiv.org/abs/2607.19391

Wu, F., Hu, J., Min, G., & Wang, S. (2025). Adaptive rank allocation for federated parameter-efficient fine-tuning of language models. arXiv. https://arxiv.org/abs/2501.14406

Xu, G., Zhang, B., & Ng, M. K. (2025). GenFT: A generative parameter-efficient fine-tuning method for pretrained foundation models. arXiv. https://arxiv.org/abs/2506.11042

Yoshimura, M., Hayashi, T., & Maeda, Y. (2024). MambaPEFT: Exploring parameter-efficient fine-tuning for Mamba. arXiv. https://arxiv.org/abs/2411.03855

Zhang, D., Feng, T., Xue, L., Wang, Y., Dong, Y., & Tang, J. (2025). Parameter-efficient fine-tuning for foundation models. arXiv. https://arxiv.org/abs/2501.13787
