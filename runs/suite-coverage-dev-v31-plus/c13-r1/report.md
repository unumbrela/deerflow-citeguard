# Systematic Literature Review: Generative Recommendation - Data, Model, and Tasks

**Date:** 2026-10-26  
**Retrieved on:** 2026-10-26  
**Published between:** 2023-10-31 and 2025-10-30  
**Category:** cs.IR (Information Retrieval)  
**Format:** APA 7th Edition

---

## Executive Summary

Generative recommendation (GR) has emerged as a transformative paradigm in recommender systems, leveraging large language models (LLMs) and generative architectures to predict user preferences through autoregressive token generation. This systematic literature review synthesizes 10 recent arXiv papers (published between October 2023 and October 2025) in the cs.IR category, focusing on three critical dimensions: **data representation** (item tokenization, multimodal integration), **model architecture** (generative frameworks, fusion strategies), and **task formulation** (multi-behavior prediction, inductive recommendation, transfer learning).

The literature reveals converging trends toward (1) sophisticated item tokenization methods that bridge collaborative filtering signals with semantic representations, (2) multimodal late fusion architectures that integrate diverse information sources while preserving modality-specific semantics, and (3) expanded task scopes beyond next-item prediction to include behavior-type forecasting, cross-domain transfer, and inductive recommendation of unseen items. Key innovations include position-routed sparse architectures for efficient scaling, residual quantized VAEs for semantic regularization, and drafter-verifier frameworks for inductive generalization. Performance improvements range from 5-20% across benchmark datasets, with notable advances in handling long-term user interests, multi-granular semantic relationships, and cross-domain knowledge transfer.

---

## Thematic Analysis

### Theme 1: Item Tokenization and Representation Learning

**Core Challenge:** Transforming recommendation data into language space while preserving both semantic hierarchies and collaborative filtering signals.

**Key Approaches:**
- **LETTER** (Wang et al., 2024) integrates hierarchical semantics, collaborative signals, and code assignment diversity using Residual Quantized VAE with contrastive alignment loss
- **UTGRec** (Zheng et al., 2025) employs multimodal LLMs with tree-structured codebooks for domain-transferable tokenization
- **MQL4GRec** (Zhai et al., 2025) transforms items into unified quantitative language using quantitative translators for cross-domain knowledge transfer

**Convergence:** All three approaches recognize that simple ID-based or textual tokenization is insufficient; effective tokenization must encode both semantic content and collaborative relationships while maintaining diversity in code assignments to avoid bias.

### Theme 2: Multimodal Integration and Late Fusion

**Core Challenge:** Effectively leveraging multiple modalities (text, images, collaborative signals) without modality interference or information loss.

**Key Approaches:**
- **MGR-LF++** (Zhu et al., 2025) uses contrastive modality alignment and special tokens, achieving 20%+ improvement over single-modality alternatives
- **GRAM** (Lee et al., 2025) introduces semantic-to-lexical translation with multi-granular late fusion, delaying fusion until decoding stage
- **DMRec** (Zhang et al., 2025) employs probabilistic meta-network with three cross-space distribution matching processes

**Convergence:** Late fusion consistently outperforms early fusion; preserving modality-specific encodings until the decoding stage while using alignment mechanisms to bridge semantic gaps proves critical for performance gains of 11-20%.

### Theme 3: Multi-Behavior and Multi-Task Learning

**Core Challenge:** Moving beyond single next-item prediction to model complex user intentions across multiple behavior types.

**Key Approach:**
- **MBGen** (Liu et al., 2024) proposes two-step generative framework: first predict behavior type, then predict items given target behavior, using position-routed sparse architecture for efficient scaling

**Convergence:** Explicitly modeling user intention through behavior-type prediction before item prediction enables better multi-task capability and significantly outperforms models focusing solely on next-item prediction.

### Theme 4: Inductive Recommendation and Unseen Items

**Core Challenge:** GR models predominantly generate items seen during training; enabling recommendation of new/unseen items remains open.

**Key Approach:**
- **SpecGR** (Ding et al., 2024) uses drafter-verifier architecture where inductive drafter proposes candidates (including new items) and GR model verifies, with guided re-drafting for efficiency

**Convergence:** The drafter-verifier paradigm with guided re-drafting represents a promising direction for inductive generalization, though this remains an emerging area with limited prior work.

### Theme 5: Long-Term Interest Modeling and Memory

**Core Challenge:** LLM context windows limit modeling to recent interactions; capturing long-term user interests requires external memory.

**Key Approach:**
- **AutoMR** (Wang et al., 2024) stores long-term interests in memory and retrieves relevant information for next-item generation, overcoming limited context windows

**Convergence:** Memory retrieval frameworks address a critical architectural limitation of LLM-based GR, though integration strategies and memory update mechanisms require further investigation.

### Theme 6: Benchmarking and Reproducibility

**Core Challenge:** Varied modeling techniques, hyperparameters, and experimental setups make direct comparisons challenging; lack of unified frameworks hinders systematic benchmarking.

**Key Approach:**
- **GRID** (Ju et al., 2025) provides modular, open-source framework for GR with semantic IDs, enabling component swapping and systematic ablation studies

**Convergence:** The community recognizes the need for standardized benchmarks and modular frameworks; overlooked architectural components substantially impact performance, necessitating systematic evaluation.

---

## Per-Paper Annotations

### 1. Liu, Z., Hou, Y., & McAuley, J. (2024). Multi-Behavior Generative Recommendation

**Research Question:** How can multi-behavior sequential recommendation be improved by integrating target behavior type into the learning objective rather than focusing solely on next-item prediction?

**Methodology:** MBGen uses a two-step generative framework that first predicts the next behavior type to frame user intention, then predicts next items given item sequences and target behavior type. Both behaviors and items are tokenized into interleaved token sequences and learned autoregressively with a position-routed sparse architecture for efficient scaling.

**Key Findings:**
- MBGen significantly outperforms existing multi-behavior sequential recommendation models across multiple tasks
- The two-step process of predicting behavior type before items enables better modeling of user intention
- Position-routed sparse architecture efficiently scales up models by exploiting heterogeneous token sequences
- Unified generative paradigm naturally enables multi-task capability

**Limitations:** Not stated in abstract.

---

### 2. Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable Item Tokenization for Generative Recommendation

**Research Question:** How can item tokenization be improved to better transform recommendation data into the language space of LLMs for generative recommendation?

**Methodology:** LETTER is a learnable tokenizer that integrates hierarchical semantics, collaborative signals, and code assignment diversity using Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias, plus ranking-guided generation loss.

**Key Findings:**
- LETTER addresses limitations of ID, textual, and codebook-based identifiers in encoding semantic information and incorporating collaborative signals
- The approach integrates hierarchical semantics, collaborative signals, and code assignment diversity
- Experiments on three datasets validate superiority over state-of-the-art in LLM-based generative recommendation
- Ranking-guided generation loss theoretically augments ranking ability

**Limitations:** Not stated in abstract.

---

### 3. Zhang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). Towards Distribution Matching between Collaborative and Language Spaces for Generative Recommendation

**Research Question:** How can the mismatch between generative models and language models be addressed to achieve optimal alignment in the feature space for generative recommendation?

**Methodology:** DMRec is a model-agnostic framework with a probabilistic meta-network bridging language model outputs with user interactions, plus three cross-space distribution matching processes that maximize shared information while preserving unique semantics and filtering irrelevant information.

**Key Findings:**
- DMRec effectively enhances recommendation performance of generative models
- The framework shows significant advantages over mainstream language model-enhanced recommendation methods
- The approach is model-agnostic and applicable to three different types of generative recommendation methods
- Distribution matching processes successfully bridge outputs of language models with user interactions

**Limitations:** Not stated in abstract.

---

### 4. Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). Universal Item Tokenization for Transferable Generative Recommendation

**Research Question:** How can item tokenization and generative recommendation be made transferable across domains rather than remaining domain-specific?

**Methodology:** UTGRec uses a universal item tokenizer with multimodal large language model and tree-structured codebooks to discretize content representations, dual lightweight decoders for text and image reconstruction, and co-occurrence alignment for collaborative knowledge integration with joint learning for pre-training and adaptation.

**Key Findings:**
- UTGRec demonstrates superiority over both traditional and generative recommendation baselines
- Universal item tokenizer successfully encodes rich item semantics across multiple domains
- Dual lightweight decoders effectively reconstruct item text and images from discrete representations
- Co-occurrence alignment and reconstruction successfully integrate collaborative signals

**Limitations:** Not stated in abstract.

---

### 5. Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). Leveraging Memory Retrieval to Enhance LLM-based Generative Recommendation

**Research Question:** How can long-term user interests from longer interaction histories be utilized in LLM-based generative recommendation despite limited context windows?

**Methodology:** AutoMR is an automatic memory-retrieval framework that stores long-term interests in memory and extracts relevant information for next-item generation within LLMs, overcoming the limitation of focusing only on recent user interactions.

**Key Findings:**
- AutoMR effectively utilizes long-term interests for generative recommendation
- The framework successfully stores long-term interests in memory for retrieval
- Extensive experimental results on two real-world datasets demonstrate effectiveness
- The approach addresses the limited context window problem in LLMs

**Limitations:** Not stated in abstract.

---

### 6. Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). Beyond Unimodal Boundaries: Generative Recommendation with Multimodal Semantics

**Research Question:** How can generative recommendation models effectively leverage multiple modalities given their sensitivity to modality choices and the multimodal nature of real-world data?

**Methodology:** The authors evaluate design strategies for leveraging multiple modalities in generative recommendation and introduce MGR-LF++, an enhanced late fusion framework that employs contrastive modality alignment and special tokens to denote different modalities.

**Key Findings:**
- Generative recommendation models are particularly sensitive to different modalities
- Previous research treating modalities in isolation is a significant limitation given the rich, multimodal nature of real-world data
- MGR-LF++ achieves a performance improvement of over 20% compared to single-modality alternatives
- Contrastive modality alignment and special tokens for denoting different modalities are effective design strategies

**Limitations:** Not stated in abstract.

---

### 7. Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). Inductive Generative Recommendation via Retrieval-based Speculation

**Research Question:** How can generative recommendation models be enabled to recommend unseen (new) items in an inductive setting rather than only generating items seen during training?

**Methodology:** SpecGR is a plug-and-play framework that uses a drafter model with inductive capability to propose candidate items (including both existing and new items), with the GR model acting as a verifier that accepts or rejects candidates while retaining its ranking capabilities.

**Key Findings:**
- GR models predominantly generate items seen during training and struggle to recommend unseen items
- SpecGR exhibits strong inductive recommendation ability by using a drafter-verifier architecture
- Guided re-drafting technique improves verification efficiency by making proposed candidates more aligned with GR model outputs
- SpecGR achieves the best overall performance among compared methods on three real-world datasets

**Limitations:** Not stated in abstract.

---

### 8. Lee, S., Choi, M., Choi, E., Kim, H.-y., & Lee, J. (2025). GRAM: Generative Recommendation via Semantic-aware Multi-granular Late Fusion

**Research Question:** How can generative recommendation models better incorporate implicit item relationships and utilize rich yet lengthy item information?

**Methodology:** GRAM introduces semantic-to-lexical translation to encode implicit hierarchical and collaborative item relationships into the vocabulary space of LLMs, and multi-granular late fusion that employs separate encoders for multi-granular prompts with fusion delayed until the decoding stage.

**Key Findings:**
- GRAM outperforms eight state-of-the-art generative recommendation models on four benchmark datasets
- GRAM achieves significant improvements of 11.5-16.0% in Recall@5
- GRAM achieves significant improvements of 5.3-13.6% in NDCG@5
- Semantic-to-lexical translation effectively encodes implicit item relationships into LLM vocabulary space

**Limitations:** Not stated in abstract.

---

### 9. Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). Generative Recommendation with Semantic IDs: A Practitioner's Handbook

**Research Question:** How can the generative recommendation community overcome challenges in comparing GR proposals and enable systematic benchmarking through an open-source, unified framework?

**Methodology:** The authors introduce and open-source GRID, a modular framework for Generative Recommendation with semantic ID designed for easy component swapping, and systematically experiment with and ablate different components of GR models with SIDs on public benchmarks.

**Key Findings:**
- Varied modeling techniques, hyper-parameters, and experimental setups in existing literature make direct comparisons between GR proposals challenging
- The absence of an open-source, unified framework hinders systematic benchmarking and extension
- Many overlooked architectural components in GR models with SIDs substantially impact performance
- GRID enables modular component swapping to accelerate idea iteration

**Limitations:** Not stated in abstract.

---

### 10. Zhai, J., Mai, Z.-F., Wang, C.-D., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). Multimodal Quantitative Language for Generative Recommendation

**Research Question:** How can recommendation knowledge be efficiently transferred from pre-trained language models to recommendation systems while accommodating differences between general linguistic knowledge and specific recommendation needs?

**Methodology:** MQL4GRec transforms items from different domains and modalities into a unified quantitative language using quantitative translators, designs quantitative language generation tasks to enrich semantic information, and achieves knowledge transfer through pre-training and fine-tuning.

**Key Findings:**
- Existing methods often fail to accommodate differences between PLM linguistic knowledge and recommendation system needs
- Existing methods rarely consider complementary knowledge between multimodal information of items
- Quantitative language serves as a bridge for transferring recommendation knowledge across domains and modalities
- MQL4GRec achieves 11.18%, 14.82%, and 7.95% improvements on the NDCG metric across three different datasets

**Limitations:** Not stated in abstract.

---

## References

Zhang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). *Towards Distribution Matching between Collaborative and Language Spaces for Generative Recommendation*. arXiv:2504.07363. https://arxiv.org/abs/2504.07363

Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). *Inductive Generative Recommendation via Retrieval-based Speculation*. arXiv:2410.02939. https://arxiv.org/abs/2410.02939

Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). *Generative Recommendation with Semantic IDs: A Practitioner's Handbook*. arXiv:2507.22224. https://arxiv.org/abs/2507.22224

Lee, S., Choi, M., Choi, E., Kim, H.-y., & Lee, J. (2025). *GRAM: Generative Recommendation via Semantic-aware Multi-granular Late Fusion*. arXiv:2506.01673. https://arxiv.org/abs/2506.01673

Liu, Z., Hou, Y., & McAuley, J. (2024). *Multi-Behavior Generative Recommendation*. arXiv:2405.16871. https://arxiv.org/abs/2405.16871

Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). *Leveraging Memory Retrieval to Enhance LLM-based Generative Recommendation*. arXiv:2412.17593. https://arxiv.org/abs/2412.17593

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). *Learnable Item Tokenization for Generative Recommendation*. arXiv:2405.07314. https://arxiv.org/abs/2405.07314

Zhai, J., Mai, Z.-F., Wang, C.-D., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). *Multimodal Quantitative Language for Generative Recommendation*. arXiv:2504.05314. https://arxiv.org/abs/2504.05314

Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). *Universal Item Tokenization for Transferable Generative Recommendation*. arXiv:2504.04405. https://arxiv.org/abs/2504.04405

Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). *Beyond Unimodal Boundaries: Generative Recommendation with Multimodal Semantics*. arXiv:2503.23333. https://arxiv.org/abs/2503.23333

---

## Methodology

**Search Strategy:** This systematic literature review searched arXiv for papers in the cs.IR (Information Retrieval) category published between 2023-10-31 and 2025-10-30 using the query "generative recommendation" with a maximum result count of 10 papers. The search was conducted on 2026-10-26 using the DeerFlow scholar plugin.

**Inclusion Criteria:**
- Primary arXiv category: cs.IR (Information Retrieval)
- Publication date: Between 2023-10-31 and 2025-10-30
- Topic: Generative recommendation systems
- Language: English

**Extraction Process:** Metadata extraction was performed via parallel subagent processing of two batches (5 papers each). For each paper, the following fields were extracted: arXiv ID, title, authors, publication date, research question, methodology, key findings, and limitations. All extraction was performed strictly from the arXiv search results without external web searches or manual additions.

**Synthesis Approach:** Thematic analysis identified six recurring research directions across the paper set: (1) item tokenization and representation learning, (2) multimodal integration and late fusion, (3) multi-behavior and multi-task learning, (4) inductive recommendation and unseen items, (5) long-term interest modeling and memory, and (6) benchmarking and reproducibility. Convergences, disagreements, and gaps were identified based on the extracted metadata.

**Citation Format:** APA 7th Edition format was used for all references, with arXiv papers cited as electronic preprints including arXiv ID and URL.

---

**Report Generated:** 2026-10-26  
**Total Papers Reviewed:** 10  
**Search Category:** cs.IR  
**Time Window:** 2023-10-31 to 2025-10-30
