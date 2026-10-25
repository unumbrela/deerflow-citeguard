# Systematic Literature Review: Parameter-Efficient Fine-Tuning

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "parameter-efficient fine-tuning", category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Parameter-efficient fine-tuning (PEFT) has emerged as a critical technology for adapting large foundation models to downstream tasks while minimizing computational costs and storage overhead. The surveyed literature from the past two years reveals a field in rapid evolution, with innovations spanning adaptive rank allocation strategies, architecture-specific adaptations for emerging models like Mamba, theoretically-grounded projection methods, and novel paradigms including quantum-inspired approaches. Collectively, these papers demonstrate that PEFT is no longer a one-size-fits-all solution but rather a diverse ecosystem of specialized techniques tailored to specific model architectures, deployment constraints, and application domains. The research shows strong convergence around the idea that leveraging pretrained weight structure and enabling dynamic adaptation during training yield superior performance with fewer parameters.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Rank Allocation and Dynamic Parameter Distribution

A dominant theme across multiple papers is the recognition that uniform parameter allocation across model layers is suboptimal. Tripathi et al. (2026) demonstrated theoretically and empirically that assigning the same adapter rank to every transformer layer fails to account for heterogeneous adaptation requirements. Their LAARA framework uses Fisher estimates to dynamically allocate ranks during training, achieving superior performance with fewer parameters. Similarly, Wu et al. (2025) addressed this challenge in the federated learning context with FedARA, which progressively identifies critical ranks and employs rank-based module pruning to reduce computational costs by up to 48.90% while improving communication efficiency by 2.40×. These approaches share a core insight: parameter efficiency is not just about minimizing total parameters, but about intelligent distribution based on layer-specific importance and task requirements.

### Theme 2: Architecture-Specific PEFT for Emerging Model Classes

As the foundation model landscape diversifies beyond Transformers, specialized PEFT methods have emerged for novel architectures. Yoshimura et al. (2024) conducted pioneering exploratory work on PEFT for Mamba, a State Space Model-based alternative to Transformers, finding that PEFT performs more effectively for Mamba than for Transformers when properly adapted. Building on this, Lee et al. (2025) introduced Memba, which incorporates bio-inspired Leaky Integrate Membrane neurons specifically designed to address Mamba's unique temporal processing dynamics. This theme reflects a broader trend: as new model architectures emerge, PEFT methods must evolve beyond Transformer-centric designs to leverage architecture-specific inductive biases and structural properties.

### Theme 3: Theoretical Foundations and Weight Geometry Exploitation

Several papers emphasize the importance of theoretical grounding for PEFT methods. Hwang et al. (2025) introduced PiCa, which provides theoretical proof that projecting gradients onto the principal column space of pretrained weights offers effective inductive bias for adaptation, addressing a gap in prior SVD-based methods like SVFT that lacked formal justification. Xu et al. (2025) similarly leveraged pretrained weight structure through GenFT, a W0-conditioned method that extracts structured patterns from pretrained weights via row and column transformations. These approaches share a shift from treating PEFT as purely empirical optimization toward methods grounded in linear algebra and weight geometry, suggesting that deeper theoretical understanding can yield practical improvements.

### Theme 4: Cross-Layer Information Flow and Representation Reuse

A recurring innovation involves exploiting information flow across layers during fine-tuning. Peng et al. (2026) proposed Echo-LoRA, which collects hidden states from deeper layers and injects them into shallow LoRA modules during training, achieving gains of 3.0-5.7 percentage points on commonsense reasoning benchmarks while maintaining zero inference-time overhead since the echo path is discarded after training. This approach challenges the conventional layer-isolated PEFT paradigm by recognizing that intermediate representations contain valuable signals for adaptation. The key insight is that training-time cross-layer communication can improve final performance without compromising the parameter efficiency benefits at deployment.

### Theme 5: Security and Privacy Vulnerabilities in PEFT

An emerging critical theme addresses security and privacy risks inherent in PEFT, particularly in federated learning contexts. Sami et al. (2025) demonstrated gradient inversion attacks on adapter-based PEFT, showing that malicious actors can reconstruct private training data with high fidelity using only adapter gradients shared during federated learning. This work reveals a fundamental tension: while PEFT reduces communication overhead and keeps most parameters frozen, the lightweight adapter gradients still leak sensitive information. This theme represents an important counterpoint to the efficiency-focused innovations, highlighting that privacy-preserving mechanisms specifically designed for PEFT are urgently needed before widespread deployment in sensitive applications.

### Theme 6: Ultra-Efficient Paradigms Beyond Low-Rank Adaptation

Pushing the boundaries of parameter efficiency, Koike-Akino et al. (2025) introduced Quantum-PEFT, which leverages quantum unitary parameterization where trainable parameters scale logarithmically with dimension rather than linearly as in LoRA. This approach achieves vanishingly smaller parameter counts than even the lowest-rank LoRA while maintaining competitive performance. While practical deployment requires quantum computing infrastructure or simulation, this work demonstrates that fundamental rethinking of the parameterization paradigm—not just incremental improvements to low-rank methods—can yield orders-of-magnitude efficiency gains. This theme suggests that future PEFT research may increasingly explore alternative mathematical frameworks beyond classical linear algebra.

## Convergences and Disagreements

**Convergences**: The surveyed papers strongly converge on several points. First, all methods agree that leveraging pretrained weight structure—whether through column space projection (Hwang et al., 2025), W0-conditioned generation (Xu et al., 2025), or Fisher-based importance estimation (Tripathi et al., 2026)—yields better performance than treating updates independently. Second, there is consensus that dynamic adaptation during training outperforms static parameter allocation, as evidenced by adaptive rank methods (Tripathi et al., 2026; Wu et al., 2025) and cross-layer injection (Peng et al., 2026). Third, multiple papers demonstrate that PEFT can achieve comparable or superior performance to full fine-tuning while using orders of magnitude fewer parameters across both NLP and vision tasks.

**Disagreements**: The literature shows less disagreement than diversity of focus. However, there is an implicit tension between methods targeting specific architectures (Yoshimura et al., 2024; Lee et al., 2025) versus general-purpose approaches (Koike-Akino et al., 2025). Architecture-specific methods argue that domain knowledge yields superior performance, while general methods prioritize broad applicability. Additionally, while most papers focus on efficiency gains, Sami et al. (2025) uniquely highlight that efficiency comes with privacy costs that remain largely unaddressed—a disagreement about whether current PEFT methods are ready for deployment in privacy-sensitive contexts.

## Gaps and Open Questions

Several critical gaps emerge from the surveyed literature:

1. **Privacy-Preserving PEFT**: Only one paper (Sami et al., 2025) addresses security vulnerabilities, and defensive mechanisms are identified as future work rather than implemented solutions. This represents a significant gap given the growing adoption of PEFT in federated and distributed settings.

2. **Computational Overhead Transparency**: Multiple papers (Tripathi et al., 2026; Hwang et al., 2025; Xu et al., 2025) do not quantify the computational cost of their proposed mechanisms (Fisher estimation, SVD projections, weight generators) during training, making it difficult to assess true efficiency gains when accounting for all overhead.

3. **Scalability to Extreme Model Sizes**: Most evaluations focus on models up to 7B-8B parameters (LLaMA variants), with limited discussion of how methods scale to 70B+ parameter models or trillion-parameter regimes where PEFT benefits would be most valuable.

4. **Cross-Domain Transferability**: While papers evaluate on both NLP and vision tasks, few investigate whether PEFT methods optimized for one domain transfer effectively to fundamentally different domains (e.g., from language to robotics or scientific computing).

5. **Standardized Evaluation Benchmarks**: The literature lacks unified benchmarking protocols, with papers using different task subsets, parameter budgets, and baseline comparisons, complicating cross-paper performance assessment.

6. **Quantum PEFT Practicality**: While Quantum-PEFT (Koike-Akino et al., 2025) shows theoretical promise, no paper addresses practical deployment pathways, quantum simulation overhead, or noise sensitivity in realistic settings.

## Per-Paper Annotations

### Tripathi et al. (2026)

**Research question**: How can we optimize rank allocation across transformer layers for parameter-efficient fine-tuning instead of using suboptimal uniform rank allocation?

**Methodology**: Proposes LAARA, a search-free framework that dynamically allocates ranks using lightweight diagonal Fisher estimates computed during training, combining projection-wise normalization, logarithmic compression, blended adapter importance estimation, and vote-to-change dampening mechanism.

**Key findings**:
- Uniform rank allocation is theoretically and empirically suboptimal due to heterogeneous adaptation requirements across transformer layers
- LAARA consistently matches or outperforms state-of-the-art approaches (LoRA, AdaLoRA, DyLoRA, Bitfit) on GLUE and MathInstruct benchmarks
- Achieves superior performance while using significantly fewer trainable parameters than competing methods
- Fisher-guided rank allocation provides a principled and effective foundation for stable and efficient adaptive parameter-efficient fine-tuning

**Limitations**: Evaluation limited to GLUE and MathInstruct benchmarks; the abstract does not explicitly discuss computational overhead of Fisher estimation or potential limitations in very large-scale models.

### Zhang et al. (2025)

**Research question**: What is the current state of Parameter-Efficient Fine-Tuning techniques across diverse Foundation Models, and what are the key trends, applications, and future directions?

**Methodology**: Comprehensive survey systematically reviewing key categories and core mechanisms of PEFT across diverse foundation models (language, generative, multimodal), exploring recent applications, and identifying potential research and development directions.

**Key findings**:
- PEFT is a cost-effective technique that minimizes parameters and computational complexity while striving for optimal downstream task performance
- The diversity of foundation models (ChatGPT, DALL-E, LLaVA, etc.) guides various adaptation strategies for PEFT
- Survey provides comprehensive understanding of PEFT trends across language understanding, generative tasks, and multimodal tasks
- Identifies potential research and development directions for improving PEFT methods in the future

**Limitations**: As a survey paper, it synthesizes existing work rather than proposing novel methods; the comprehensive nature means individual techniques may not be covered in sufficient technical depth for implementation.

### Hwang et al. (2025)

**Research question**: How can we improve parameter-efficient fine-tuning with solid theoretical grounding by exploiting the geometry of pre-trained weights through column space projection?

**Methodology**: Introduces PiCa that projects gradients onto the principal column space of pre-trained weights with theoretical proof, and enhances parameter efficiency through a novel weight-sharing strategy.

**Key findings**:
- Projecting gradients onto the principal column space of pre-trained weights provides an effective inductive bias for adaptation
- PiCa consistently outperforms state-of-the-art baselines (including SVFT) under comparable or smaller parameter budgets
- Provides theoretical foundation that prior SVD-based methods like SVFT lacked
- Demonstrates both theoretical rigor and practical effectiveness across diverse NLP and vision tasks

**Limitations**: The abstract does not explicitly discuss limitations; theoretical guarantees may rely on assumptions about weight matrix properties that may not hold in all scenarios, and computational cost of SVD-based projections is not addressed.

### Xu et al. (2025)

**Research question**: How can we better leverage the structural information encoded in pretrained weights for parameter-efficient fine-tuning rather than learning updates independently?

**Methodology**: Proposes GenFT, a W0-conditioned PEFT method using a deterministic weight generator that performs row and column transformations with nonlinear activations to extract structured patterns from pretrained weights, with shared-specific decomposition for cross-layer information reuse and layer-specific flexibility.

**Key findings**:
- W0-conditioned approach effectively leverages structural information encoded in pretrained weights compared to methods that learn updates independently
- Achieves competitive or better average performance across NLP and CV benchmarks
- Simple and parameter-efficient design with shared-specific decomposition balancing information reuse and flexibility
- Pilot study demonstrates feasibility for generative models (tested on LLaMA-7B)

**Limitations**: Pilot study on LLaMA-7B suggests limited validation on larger-scale generative models; the abstract does not discuss computational overhead of the weight generator or potential limitations in specific task domains.

### Koike-Akino et al. (2025)

**Research question**: Can quantum computations enable ultra parameter-efficient fine-tuning with logarithmic parameter scaling instead of linear scaling?

**Methodology**: Introduces Quantum-PEFT leveraging quantum unitary parameterization with Pauli parameterization, where the number of trainable parameters grows logarithmically with ambient dimension rather than linearly as in LoRA-based methods.

**Key findings**:
- Quantum-PEFT achieves vanishingly smaller number of trainable parameters than lowest-rank LoRA as dimensions grow
- Exploits full-rank quantum unitary parameterization that is surprisingly parameter-efficient
- Maintains competitive performance while enhancing parameter efficiency significantly
- Demonstrates significant advantages in parameter efficiency on several transfer learning benchmarks in language and vision

**Limitations**: Requires quantum computing infrastructure or quantum simulation which may introduce practical deployment challenges; the abstract does not discuss quantum hardware requirements, simulation overhead, or noise sensitivity in practical implementations.

### Wu et al. (2025)

**Research question**: How can federated parameter-efficient fine-tuning address privacy and efficiency challenges while overcoming performance degradation from heterogeneous data and communication inefficiency from fixed parameter configurations?

**Methodology**: Proposes FedARA, an adaptive rank allocation framework for federated PEFT that employs truncated SVD adaptation for enhanced feature representation across clients, dynamic rank allocation to identify critical ranks progressively, and rank-based module pruning to remove inactive modules.

**Key findings**:
- FedARA consistently outperforms baselines by 6.95% to 8.49% across various datasets and models under heterogeneous data conditions
- Communication efficiency improves by 2.40× compared to baseline methods
- Total training time decreases by up to 48.90% on edge devices
- Energy consumption reduces by up to 46.95% on various edge devices
- Truncated SVD adaptation significantly mitigates adverse effects of data heterogeneity across clients

**Limitations**: The abstract does not explicitly acknowledge limitations; evaluation appears limited to specific datasets and model architectures tested, with no discussion of scalability to very large model sizes or extreme heterogeneity scenarios.

### Peng et al. (2026)

**Research question**: How can LoRA-style PEFT methods be improved by utilizing intermediate representations from deeper layers that are typically left unused in current approaches?

**Methodology**: Echo-LoRA collects boundary hidden states from deeper source layers during training, aggregates them into sample-level echo representations, and uses lightweight projection and gating networks to inject the signal into shallow LoRA or DoRA modules with answer-only masking, masked distillation, and stochastic routing for stability.

**Key findings**:
- Echo-LoRA exceeds reported LoRA baselines by 5.7 percentage points on average across eight commonsense reasoning benchmarks
- Under reproduced LoRA baselines in unified implementation, achieves 3.0 percentage points average gain
- When combined with DoRA, achieves additional 2.7 percentage points improvement
- The echo path is discarded after training, maintaining original low-rank LoRA/DoRA form with no inference-time overhead
- Performance gains demonstrated across LLaMA-7B, LLaMA2-7B, and LLaMA3-8B model variants

**Limitations**: The auxiliary echo path exists only during training and is discarded at inference, meaning benefits are confined to the training phase; evaluation limited to commonsense reasoning benchmarks without broader task coverage.

### Yoshimura et al. (2024)

**Research question**: How can existing PEFT methods be effectively applied or adapted to Mamba (State Space Model-based) architecture as an alternative to Transformers?

**Methodology**: Conducts exploratory analysis investigating effectiveness of existing Transformer PEFT methods when applied to Mamba, modifies methods to better align with Mamba architecture, and proposes new Mamba-specific PEFT methods leveraging Mamba's distinctive structure with a framework for combining multiple PEFT methods.

**Key findings**:
- PEFT performs more effectively for Mamba than for Transformer-based models
- Existing PEFT methods for Transformers can be adapted to Mamba with architectural modifications
- New Mamba-specific PEFT methods leveraging the distinctive SSM structure show promise
- Multiple PEFT methods can be effectively combined to outperform previous works
- Provides a reproducible framework with code release planned after publication

**Limitations**: This is an exploratory analysis rather than a comprehensive solution; code was not yet released at time of publication, limiting immediate reproducibility and broader validation.

### Lee et al. (2025)

**Research question**: How can PEFT methods for Mamba address the unique temporal processing dynamics of State Space Models rather than simply applying Transformer-tailored approaches?

**Methodology**: Proposes Memba, a membrane-driven PEFT approach introducing Leaky Integrate Membrane (LIM) neurons as bio-inspired gating mechanisms that accumulate membrane potentials over time, strategically combined with LoRA and cross-layer membrane transfer to enhance temporal modeling capabilities.

**Key findings**:
- Memba achieves substantial improvements over existing PEFT methods across both language and vision tasks
- LIM neurons enhance selective information retention through bio-inspired membrane potential accumulation
- Cross-layer membrane transfer improves Mamba's temporal modeling capabilities
- Strategic combination of LIM neurons with LoRA addresses SSM-specific temporal processing dynamics
- Code publicly available at https://github.com/Intelligent-Computing-Lab-Yale/Memba

**Limitations**: The abstract does not explicitly acknowledge limitations; evaluation scope across specific language and vision tasks is not detailed, and computational overhead of LIM mechanisms during training is not quantified.

### Sami et al. (2025)

**Research question**: Can user privacy in federated learning with PEFT be compromised through malicious design of pretrained models and trainable adapter modules via gradient inversion attacks?

**Methodology**: Demonstrates gradient inversion attacks on the adapter PEFT mechanism in federated learning, reconstructing local data samples of target users using only accessible adapter gradients exchanged with the server while the backbone model remains frozen.

**Key findings**:
- Gradient inversion attacks can successfully reconstruct local data samples using only adapter gradients shared in federated PEFT
- Large batches of fine-tuning images can be retrieved with high fidelity from adapter gradients
- Privacy vulnerabilities exist even when only lightweight adapter module gradients (not full model gradients) are shared
- Malicious design of pretrained models and trainable adapters can compromise fine-tuning data privacy
- Highlights critical need for privacy-preserving mechanisms specifically designed for PEFT in federated learning

**Limitations**: Attack demonstration focuses specifically on the adapter PEFT mechanism rather than other PEFT methods like LoRA; defensive countermeasures are identified as future work rather than implemented solutions.

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
