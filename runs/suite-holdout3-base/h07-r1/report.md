# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "offline reinforcement learning", cs.LG, 2024-01-01 to 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on offline reinforcement learning published between 2024 and 2026. The surveyed literature reveals a field maturing beyond algorithmic innovation toward practical deployment challenges, with strong emphasis on data efficiency, distributional shift mitigation, and real-world applicability. Key trends include novel approaches to handling multi-modal datasets through optimal transport and flow-based methods, increased focus on limited-data scenarios through regularization and reward imputation, and growing attention to robustness and generalization guarantees. The literature collectively demonstrates that offline RL is transitioning from controlled benchmark settings toward addressing the complexities of real-world deployment in domains such as autonomous driving and robotics, though significant gaps remain in theoretical understanding and robustness to adversarial conditions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Addressing Distributional Shift Through Advanced Policy Representations

A central challenge in offline RL remains the distributional shift problem: policies that take out-of-distribution (OOD) actions may fail catastrophically when deployed. Recent work has moved beyond simple behavioral constraints toward more sophisticated approaches that leverage generative models and optimal transport theory. Jiang et al. (2024) address OOD mode averaging in flow-based policy distillation by introducing Value-Rectified Distillation, which reformulates offline policy distillation as a value-guided generative trajectory alignment problem. Their approach uses dynamic coupling to decouple distinct behavioral modes, preventing action collapse into invalid OOD regions. Similarly, Asadulaev et al. (2024) reframe offline RL as an optimal transportation problem, enabling effective "stitching" of optimal behaviors from heterogeneous datasets containing demonstrations from experts with varying quality levels.

Hepburn et al. (2024) propose a complementary approach through state-constrained offline RL, which shifts focus from constraining state-action distributions to constraining only state distributions. This allows policies to take OOD actions that lead to in-distribution states, significantly broadening the learning horizon while maintaining safety. Their StaCQ algorithm achieves state-of-the-art performance on D4RL benchmarks by enabling effective combination of different trajectories from the dataset. These three papers collectively demonstrate a shift from conservative batch-constrained methods toward more flexible frameworks that maintain theoretical guarantees while expanding the space of learnable policies.

### Theme 2: Data Efficiency in Limited-Data Regimes

While much offline RL research assumes access to large-scale datasets with millions of transitions, many real-world applications face severe data scarcity. Recent work has addressed this gap through multiple complementary strategies. Arnob et al. (2025) identify that offline RL algorithms overfit on small datasets and introduce Sparse-Reg, a sparsity-based regularization technique that enables effective learning in limited-data settings, outperforming state-of-the-art baselines in continuous control tasks. Schmähling et al. (2026) tackle the related problem of learning from limited suboptimal trajectories through trajectory-level data augmentation that exploits task structure and geometric relationships between rewards and value functions.

Romeo and Bagdanov (2024) address a different aspect of data scarcity: the scarcity of reward annotations. Their reward imputation approach learns a reward model from only 1% of reward-labeled transitions, then imputes rewards for the remaining 99% of transitions, enabling performant agent learning despite minimal reward supervision. Together, these three papers demonstrate that offline RL can be adapted to data-scarce scenarios through careful regularization, augmentation, and reward modeling—critical advances for domains where data collection is expensive or constrained.

### Theme 3: Benchmark Development for Real-World Applications

The field is actively working to bridge the gap between synthetic benchmark tasks and real-world deployment scenarios. Lee et al. (2024) provide 19 autonomous driving datasets, including real-world human driver demonstrations, along with benchmarks for seven popular offline RL algorithms across three realistic driving scenarios. Their work addresses the limitation that most offline RL research still relies on game tasks with synthetic datasets, providing a unified decision-making framework that can operate across different driving scenarios.

This benchmark development reflects a broader trend toward practical applicability. The AD4RL benchmarks enable researchers to evaluate algorithms in contexts that better reflect the complexity and safety requirements of real-world autonomous driving, laying groundwork for collaboration between the RL community and autonomous driving researchers. Such domain-specific benchmarks are essential for validating that algorithmic advances translate to practical utility beyond controlled laboratory settings.

### Theme 4: Theoretical Foundations and Generalization Guarantees

A growing body of work provides theoretical foundations for offline RL, moving beyond empirical validation toward formal guarantees. Hoischen et al. (2025) link offline RL to the Hamilton-Jacobi-Bellman equation through an operator-theoretic approach, representing world models via infinitesimal generators of controlled diffusion processes in reproducing kernel Hilbert spaces. Their analysis establishes global convergence of the value function under sufficiently small generator-approximation error and derives explicit finite-sample guarantees with bounds tied to system properties such as smoothness and stability.

Wang et al. (2025) address the zero-shot generalization problem, where policies trained on data from multiple environments must perform well on unseen test environments. They propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), demonstrating that both methods can find near-optimal policies with zero-shot generalization properties. Their work provides the first theoretical understanding of generalization foundations in offline RL, showing that classical methods fail to generalize while pessimistic approaches succeed. These theoretical advances complement empirical progress by providing formal understanding of when and why offline RL algorithms succeed.

### Theme 5: Robustness and Safety in Real-World Deployment

As offline RL moves toward real-world applications, robustness to perturbations and failures has emerged as a critical concern. Ayabe et al. (2024) evaluate the robustness of existing offline RL methods for robot control against action perturbations simulating joint actuator faults. Their experiments with legged robots reveal that offline RL methods exhibit significant vulnerabilities to both random and adversarial perturbations, and are notably more vulnerable than online RL methods. This finding highlights a critical gap: while offline RL offers safety benefits by avoiding risky environment interaction during training, the resulting policies may be less robust to real-world disturbances than policies trained with online interaction.

This robustness concern connects to the broader theme of safe deployment. The vulnerability of offline RL to action perturbations suggests that additional safeguards—such as the state-constrained approaches of Hepburn et al. (2024) or the robustness-aware training objectives implicit in the pessimistic methods of Wang et al. (2025)—may be necessary for deployment in safety-critical applications like robotics and autonomous driving.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers acknowledge that distributional shift remains the central challenge in offline RL, though they propose different solutions. Second, there is consensus that offline RL must move beyond synthetic benchmarks toward real-world applications, as evidenced by the development of autonomous driving benchmarks (Lee et al., 2024) and robotics evaluations (Ayabe et al., 2024). Third, multiple papers converge on the insight that pessimistic or conservative approaches—whether through pessimistic policy evaluation (Wang et al., 2025), state constraints (Hepburn et al., 2024), or sparsity regularization (Arnob et al., 2025)—are effective for mitigating overfitting and improving generalization.

**Disagreements**: The literature reveals tension between flexibility and conservatism in handling distributional shift. State-constrained approaches (Hepburn et al., 2024) advocate allowing OOD actions that lead to in-distribution states, while flow-based distillation methods (Jiang et al., 2026) focus on preventing OOD action generation entirely through mode decoupling. Additionally, while most papers validate on D4RL benchmarks, there is implicit disagreement about the relevance of these benchmarks: some treat them as sufficient validation (Asadulaev et al., 2024; Romeo & Bagdanov, 2024), while others argue for domain-specific benchmarks that better reflect deployment contexts (Lee et al., 2024).

## Gaps and Open Questions

Several critical gaps emerge from this literature. First, robustness remains inadequately addressed: while Ayabe et al. (2024) demonstrate vulnerability to action perturbations, few papers propose concrete solutions beyond the call for "more robust approaches." Second, computational efficiency and scalability receive minimal attention—most papers focus on algorithmic novelty without discussing training time, memory requirements, or inference latency, which are critical for real-world deployment. Third, while theoretical guarantees are provided for specific methods (Hoischen et al., 2025; Wang et al., 2025), these guarantees often require assumptions (e.g., "sufficiently small generator-approximation error") that may not hold in practice.

Fourth, the literature shows limited attention to discrete action spaces—nearly all empirical validation focuses on continuous control, leaving open questions about applicability to domains with discrete decisions. Fifth, while several papers address data scarcity, none address the related problem of dataset quality assessment: how to automatically evaluate whether a given offline dataset is suitable for learning a target policy. Finally, the gap between benchmark performance and real-world deployment remains wide—while autonomous driving benchmarks (Lee et al., 2024) represent progress, actual deployment in safety-critical systems requires validation far beyond current benchmark evaluations.

## Per-Paper Annotations

### Arnob et al. (2025)

**Research question**: How can offline reinforcement learning avoid overfitting and achieve effective learning when working with considerably smaller datasets than typical benchmarks?
**Methodology**: Introduces Sparse-Reg, a regularization technique based on sparsity designed to mitigate overfitting in offline reinforcement learning, enabling effective learning in limited data settings for continuous control tasks.
**Key findings**:
- Offline RL algorithms overfit on small datasets, resulting in poor performance
- Sparse-Reg effectively mitigates overfitting in limited data settings
- Outperforms state-of-the-art baselines in continuous control tasks
- Enables effective learning with datasets considerably smaller than million-point benchmarks
**Limitations**: Primarily evaluated on continuous control tasks; effectiveness of sparsity regularization may vary across different task domains and dataset characteristics.

### Asadulaev et al. (2024)

**Research question**: How can we extract efficient policies from offline RL datasets containing demonstrations from various experts with varying levels of optimality?
**Methodology**: The authors reframe offline reinforcement learning as an optimal transportation problem and present an algorithm that finds a policy mapping states to a partial distribution of the best expert actions for each given state, enabling effective stitching of optimal behaviors from heterogeneous datasets.
**Key findings**:
- Optimal transport formulation enables effective stitching of best behaviors from mixed-quality datasets
- The algorithm maps states to partial distributions of optimal expert actions rather than full action distributions
- Demonstrated improvements over existing methods on continuous control problems
- Evaluated successfully on the D4RL benchmark suite
- The approach handles sub-optimal expert data by selectively extracting high-quality behaviors
**Limitations**: Evaluation is restricted to continuous control problems from the D4RL suite; applicability to discrete action spaces or other task domains is not explored. The abstract does not address computational complexity of the optimal transport solution or scalability to large state spaces.

### Ayabe et al. (2024)

**Research question**: How robust are existing offline reinforcement learning methods to real-world challenges such as joint actuator faults in robot control applications?
**Methodology**: Evaluates robustness of existing offline RL methods using legged robots from OpenAI Gym based on average episodic rewards, simulating failures through both random and adversarial perturbations to joint torque signals representing worst-case scenarios.
**Key findings**:
- Existing offline RL methods exhibit significant vulnerabilities to action perturbations
- Offline RL methods are more vulnerable to perturbations than online RL methods
- Both random and adversarial perturbations reveal critical robustness concerns
- Highlights urgent need for more robust offline RL approaches for real-world robot control
**Limitations**: Evaluation limited to legged robots in OpenAI Gym; focuses specifically on joint torque perturbations rather than other real-world failure modes.

### Hepburn et al. (2024)

**Research question**: How can offline RL overcome the limitation of being confined to specific state-action distributions in the dataset while still avoiding distributional shift?
**Methodology**: Introduces state-constrained offline RL framework that focuses solely on the dataset's state distribution rather than state-action distribution, allowing policies to take out-of-distribution actions that lead to in-distribution states, and implements StaCQ deep learning algorithm.
**Key findings**:
- State-constrained approach allows policies to take high-quality out-of-distribution actions leading to in-distribution states
- Significantly enhances learning potential compared to traditional batch-constrained methods
- Improves ability to combine different trajectories from the dataset effectively
- StaCQ achieves state-of-the-art performance on D4RL benchmark datasets
**Limitations**: Theoretical findings require further development for subsequent advancements; StaCQ performance needs validation beyond D4RL benchmarks.

### Hoischen et al. (2025)

**Research question**: How can we establish statistical guarantees for approximation errors when learning policies from offline datasets in continuous-time stochastic systems?
**Methodology**: Links reinforcement learning to the Hamilton-Jacobi-Bellman equation and proposes an operator-theoretic algorithm based on dynamic programming recursion, representing the world model via the infinitesimal generator of controlled diffusion processes learned in a reproducing kernel Hilbert space.
**Key findings**:
- Establishes global convergence of the value function under sufficiently small generator-approximation error
- Derives explicit finite-sample guarantees with bounds tied to system properties such as smoothness and stability
- Integrates statistical learning methods with operator theory for theoretical analysis
- Demonstrates that operator-based approaches show promise for solving offline RL using continuous-time optimal control
**Limitations**: Results are theoretical and proof-of-concept only, requiring sufficiently small generator-approximation error for convergence guarantees to hold.

### Jiang et al. (2026)

**Research question**: How can we address Out-of-Distribution (OOD) Mode Averaging that occurs when distilling Flow Matching based behavior policies in offline reinforcement learning?
**Methodology**: The authors propose Value-Rectified Distillation (VRD), which reformulates offline policy distillation as a value-guided generative trajectory alignment problem using a dynamic coupling mechanism to rectify flow dynamics and decouple distinct behavioral modes. VRD is instantiated through two complementary algorithms: VRD-Q (value-quantile behavior distillation to filter low-value behaviors) and VRD-R (latent space reorganization to geometrically isolate high-value trajectories).
**Key findings**:
- VRD successfully prevents action collapse into invalid OOD regions by explicitly decoupling distinct behavioral modes
- VRD improves existing generative baselines across diverse continuous control and planning tasks
- Performance gains are especially pronounced on multi-modal, non-expert datasets
- The framework was validated on D4RL, OGBench, and Minari benchmarks
- Dynamic coupling mechanism effectively isolates high-value actions from the behavior policy
**Limitations**: The evaluation is limited to continuous control and planning tasks; generalization to discrete action spaces or other domains is not demonstrated. The abstract does not discuss computational overhead or scalability considerations of the two-algorithm approach.

### Lee et al. (2024)

**Research question**: How can offline reinforcement learning research move beyond synthetic game-task datasets toward practical real-world applications?
**Methodology**: The authors provide 19 autonomous driving datasets (including real-world human driver data) and establish benchmarks using seven popular offline RL algorithms across three realistic driving scenarios, along with a unified decision-making process model that operates effectively across different scenarios.
**Key findings**:
- Created 19 datasets including real-world human driver demonstrations for autonomous driving
- Established benchmarks for seven popular offline RL algorithms across three realistic driving scenarios
- Provided a unified decision-making process model serving as a reference framework for algorithm design
- Addresses the limitation of offline RL research relying on game tasks with synthetic datasets
- Enables practical evaluation of existing RL methods in realistic autonomous driving contexts
**Limitations**: The benchmarks are specific to autonomous driving domains and may not generalize to other application areas. The abstract does not discuss dataset size, diversity of driving conditions, or potential safety considerations when deploying policies trained on these benchmarks in real-world settings.

### Romeo and Bagdanov (2024)

**Research question**: How can we apply offline reinforcement learning in data-scarce scenarios where very few demonstrations are annotated with ground-truth rewards?
**Methodology**: The authors propose a Reward Model that estimates reward signals from a very limited sample of reward-annotated environment transitions, then use this model to impute rewards for a large sample of reward-free transitions, enabling application of standard ORL techniques on the augmented dataset.
**Key findings**:
- The reward model successfully imputes rewards using only 1% of reward-labeled transitions from original datasets
- Performant agents can be learned from the 99% of transitions with imputed rewards
- The approach enables ORL application in scenarios where ground-truth rewards are scarce or costly to obtain
- Validated on several D4RL continuous locomotion tasks
- The simple reward modeling approach is effective despite minimal reward supervision
**Limitations**: The approach is demonstrated only on D4RL continuous locomotion tasks; generalization to other task types or domains is not shown. The quality of imputed rewards depends on the representativeness of the small labeled subset, which may introduce bias if the 1% sample is not well-distributed.

### Schmähling et al. (2026)

**Research question**: How can we enable effective training of off-policy models from a limited number of suboptimal trajectories in offline reinforcement learning?
**Methodology**: The authors introduce a trajectory-based augmentation technique that exploits task structure and the geometric relationship between rewards, value functions, and mathematical properties of logging policies. The approach provides theoretical justification for augmentation strategies that support suboptimal logging policies during data collection.
**Key findings**:
- Trajectory-level augmentation enables higher data quality even when logging policies are suboptimal
- The approach improves offline reinforcement learning performance with limited trajectory data
- Method works effectively across positioning tasks of varying dimensionality
- The augmentation technique remains effective under partial observability conditions
- Theoretical analysis provides justification for the proposed augmentation strategies
**Limitations**: The empirical validation is focused on positioning tasks, which may limit generalizability to other domains. The abstract does not specify the degree of suboptimality that can be tolerated or the minimum number of trajectories required for effective augmentation.

### Wang et al. (2025)

**Research question**: Can offline reinforcement learning achieve zero-shot generalization to unseen test environments when trained on data from multiple training environments?
**Methodology**: Proposes pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to guide policy learning and enhance generalization across environments.
**Key findings**:
- Both PERM and PPPO can find near-optimal policies with zero-shot generalization property
- Classical offline RL methods fail to generalize to new, unseen environments
- Pessimistic policy evaluation effectively guides policy learning for enhanced generalization
- Provides the first theoretical understanding of the foundation of generalization phenomena in offline RL
**Limitations**: Represents only a first step in understanding generalization in offline RL; theoretical assumptions about environment structure may limit practical applicability.

## References

Arnob, S. Y., Fujimoto, S., & Precup, D. (2025). Sparse-Reg: Improving sample complexity in offline reinforcement learning using sparsity. arXiv. https://arxiv.org/abs/2506.17155

Asadulaev, A., Korst, R., Korotin, A., Egiazarian, V., Filchenkov, A., & Burnaev, E. (2024). Rethinking optimal transport in offline reinforcement learning. arXiv. https://arxiv.org/abs/2410.14069

Ayabe, S., Otomo, T., Kera, H., & Kawamoto, K. (2024). Robustness evaluation of offline reinforcement learning for robot control against action perturbations. arXiv. https://arxiv.org/abs/2412.18781

Hepburn, C. A., Jin, Y., & Montana, G. (2024). State-constrained offline reinforcement learning. arXiv. https://arxiv.org/abs/2405.14374

Hoischen, N., Bevanda, P., Beier, M., Sosnowski, S., Houska, B., & Hirche, S. (2025). Infinitesimal operator world models: Finite-sample guarantees for offline reinforcement learning. arXiv. https://arxiv.org/abs/2511.10383

Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-rectified distillation for flow-based offline reinforcement learning. arXiv. https://arxiv.org/abs/2610.29075

Lee, D., Eom, C., & Kwon, M. (2024). AD4RL: Autonomous driving benchmarks for offline reinforcement learning with value-based dataset. arXiv. https://arxiv.org/abs/2404.02429

Romeo, C., & Bagdanov, A. D. (2024). Offline reinforcement learning with imputed rewards. arXiv. https://arxiv.org/abs/2407.10839

Schmähling, T., Burkhardt, M., & Windisch, T. (2026). Trajectory-level data augmentation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2605.13401

Wang, Z., Yang, C., Lui, J. C. S., & Zhou, D. (2025). Provable zero-shot generalization in offline reinforcement learning. arXiv. https://arxiv.org/abs/2503.07988
