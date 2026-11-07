Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.22312v1 \[cs.AI\] 19 Mar 2026

# The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis

Di Zhang
Affiliation: School of Advanced Technology
Affiliation: Xi’an Jiaotong-Liverpool University
Affiliation: Suzhou, Jiangsu, China
Email: [di.zhang@xjtlu.edu.cn](mailto:)

###### Abstract

This paper computationally investigates whether thought requires a language-like format, as posited by the Language of Thought (LoT) hypothesis. We introduce the “AI Private Language” thought experiment: if two artificial agents develop an efficient, inscrutable communication protocol via multi-agent reinforcement learning (MARL), and their performance declines when forced to use a human-comprehensible language, this Efficiency Attenuation Phenomenon (EAP) challenges the LoT. We formalize this in a cooperative navigation task under partial observability. Results show that agents with an emergent protocol achieve 50.5% higher efficiency than those using a pre-defined, human-like symbolic protocol, confirming the EAP. This suggests optimal collaborative cognition in these systems is not mediated by symbolic structures but is naturally coupled with sub-symbolic computations. The work bridges philosophy, cognitive science, and AI, arguing for pluralism in cognitive architectures and highlighting implications for AI ethics.

Keywords: Language of Thought; emergent communication; multi-agent reinforcement learning; cognitive architecture; symbol grounding; artificial intelligence; philosophy of mind

| |
| --- |
| |

August 24, 2026

## 1 Introduction

The quest to understand the nature of thought constitutes a foundational pursuit within cognitive science. A dominant strand of this inquiry, crystallized in Jerry Fodor’s influential Language of Thought (LoT) hypothesis, posits that thinking is intrinsically a computational process operating on structured, language-like symbolic representations—a “mentalese” ( [Fodor, 1975](https://arxiv.org/html/2603.22312v1#bib.bib5 ""); [Fodor, 2008](https://arxiv.org/html/2603.22312v1#bib.bib6 "")). This paradigm, which reached its zenith in classical symbolic artificial intelligence (AI), views cognition as rule-based manipulation of physical symbol systems ( [Newell and Simon, 1976](https://arxiv.org/html/2603.22312v1#bib.bib12 "")). From this perspective, the representational format for thought is presumed to share core logical and combinatorial properties with human natural language, suggesting a deep, necessary link between the machinery of thought and linguistic structure.

However, the dramatic rise of connectionist architectures and deep learning presents a profound counterpoint to this symbolic vision. These sub-symbolic systems generate intelligent behavior through the adjustment of weights in distributed neural networks, with “knowledge” embedded in the geometry of high-dimensional state spaces rather than in discrete, composable tokens ( [Rumelhart et al., 1986](https://arxiv.org/html/2603.22312v1#bib.bib13 ""); [Hinton, 1986](https://arxiv.org/html/2603.22312v1#bib.bib9 "")). The success of such models forces a critical re-examination: if complex, goal-directed behavior can emerge from computations that bear little resemblance to linguistic syntax, must we reconsider the putative necessity of a language-like medium for thought itself? This tension between symbolic and sub-symbolic paradigms lies at the heart of contemporary debates about the fundamental vehicles of cognition ( [Lake et al., 2017](https://arxiv.org/html/2603.22312v1#bib.bib23 ""); [McClelland et al., 2010](https://arxiv.org/html/2603.22312v1#bib.bib22 "")).

Concurrently, research in multi-agent reinforcement learning (MARL) has uncovered a phenomenon with significant, yet under-explored, philosophical implications: the emergence of communication. When artificial agents are placed in cooperative environments with a communication channel, they often spontaneously develop novel, task-specific signaling protocols to coordinate their behavior ( [Foerster et al., 2016](https://arxiv.org/html/2603.22312v1#bib.bib7 ""); [Mordatch and Abbeel, 2018](https://arxiv.org/html/2603.22312v1#bib.bib11 "")). These protocols can become stable and efficient, yet remain largely opaque to human interpretation ( [Lowe et al., 2017](https://arxiv.org/html/2603.22312v1#bib.bib10 "")). This empirical reality invites a powerful thought experiment: if two AIs were to develop a highly efficient “private language” through collaboration, and their performance measurably declined when forced to use a human-comprehensible language instead, what would this imply about the relationship between their internal cognitive processes and linguistic structure?

![Refer to caption](https://arxiv.org/html/2603.22312v1/figures/intro.png)Figure 1:
Conceptual schematic of the AI Private Language thought experiment and the predicted Efficiency Attenuation Phenomenon (EAP).
Left: Agents develop an efficient but opaque communication protocol through MARL and cooperation.
Right: The same agents are forced to use a pre-defined, human-interpretable symbolic protocol.

This paper introduces and rigorously develops this AI Private Language thought experiment as a novel methodological tool for interrogating the LoT hypothesis (see Figure [1](https://arxiv.org/html/2603.22312v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") for a conceptual overview). We argue that the hypothesized performance decline—termed the Efficiency Attenuation Phenomenon (EAP)—serves as a crucial behavioral signature. Its occurrence would suggest that, for these artificial cognitive systems, optimal collaborative problem-solving (and by extension, the thought processes underlying it) is not mediated by a language-like representational format but is instead more directly coupled with a non-linguistic, potentially sub-symbolic, mode of computation and communication.

To transform philosophical speculation into a tractable cognitive science research program, we adopt a computational-philosophical approach. We first situate our thought experiment within the relevant theoretical landscape, engaging with classic philosophical objections from Wittgenstein on private language ( [Wittgenstein, 1953](https://arxiv.org/html/2603.22312v1#bib.bib15 "")) and Searle on syntax versus semantics ( [Searle, 1980](https://arxiv.org/html/2603.22312v1#bib.bib14 "")), as well as contemporary cognitive theories like the Extended Mind hypothesis ( [Clark and Chalmers, 1998](https://arxiv.org/html/2603.22312v1#bib.bib3 "")). We then bridge this theoretical analysis with computational modeling by formalizing the core thought experiment within a MARL framework. This allows us to derive concrete, empirically testable hypotheses and present simulation results that demonstrate the plausibility and operational characteristics of the Efficiency Attenuation Phenomenon.

The primary contribution of this work is threefold. First, it provides a novel, empirically grounded argument that challenges the universality of the LoT by illustrating a viable pathway for non-linguistic thought in artificial systems. Second, it demonstrates how classic philosophical puzzles can be productively engaged and extended through formal modeling and simulation, offering a blueprint for a renewed dialogue between philosophy and computational cognitive science ( [Griffiths et al., 2010](https://arxiv.org/html/2603.22312v1#bib.bib31 "")). Third, it highlights the profound implications of this possibility for adjacent fields, including AI ethics—where it complicates the value alignment problem by introducing the “ultimate black box” of incommensurable thought—and the methodology of machine consciousness research.

The remainder of this paper is structured as follows. Section [2](https://arxiv.org/html/2603.22312v1#S2 "2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") reviews related work in the philosophy of mind, cognitive science, and AI. Section [3](https://arxiv.org/html/2603.22312v1#S3 "3 Thought Experiment and Hypotheses ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") formally presents the AI private language thought experiment and derives our core testable hypotheses. Section [4](https://arxiv.org/html/2603.22312v1#S4 "4 Model and Experimental Design ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") details the computational model and experimental design of our MARL simulation. Section [5](https://arxiv.org/html/2603.22312v1#S5 "5 Results ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") presents the results, providing evidence for the Efficiency Attenuation Phenomenon. Section [6](https://arxiv.org/html/2603.22312v1#S6 "6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") contains a comprehensive discussion, interpreting the results, responding to philosophical objections, and exploring broader implications. Section [7](https://arxiv.org/html/2603.22312v1#S7 "7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis") concludes.

## 2 Related Work

This work sits at the intersection of philosophy of mind, cognitive science, and artificial intelligence, engaging three core theoretical strands: the debate over symbolic vs. sub-symbolic cognition, classic philosophical critiques of machine understanding, and the empirical study of emergent communication in computational systems.

### 2.1 The Language of Thought and Its Alternatives

Jerry Fodor’s LoT hypothesis posits that thinking operates on language-like symbolic structures with combinatorial syntax and semantics ( [Fodor, 1975](https://arxiv.org/html/2603.22312v1#bib.bib5 "")). This view aligns with classical symbolic AI, which treats cognition as rule-based manipulation of physical symbol systems ( [Newell and Simon, 1976](https://arxiv.org/html/2603.22312v1#bib.bib12 "")). In contrast, connectionist and deep learning models implement intelligence through distributed, sub-symbolic representations and parallel constraint satisfaction, challenging the necessity of discrete symbols for cognition ( [Rumelhart et al., 1986](https://arxiv.org/html/2603.22312v1#bib.bib13 ""); [Hinton, 1986](https://arxiv.org/html/2603.22312v1#bib.bib9 "")). Further, embodied and extended cognitive science argues that intelligent behavior can arise from dynamic agent-environment coupling without internal linguistic representations ( [Clark, 1998](https://arxiv.org/html/2603.22312v1#bib.bib16 ""); [Brooks, 1991](https://arxiv.org/html/2603.22312v1#bib.bib17 "")). Our thought experiment draws on this tension, proposing a scenario in which efficient collaborative cognition emerges without a language-like medium. This echoes recent calls for a pluralistic view of cognitive architectures ( [Dale and Galati, 2020](https://arxiv.org/html/2603.22312v1#bib.bib4 "")) and emphasizes the possibility of “intelligence without representation” ( [Brooks, 1991](https://arxiv.org/html/2603.22312v1#bib.bib17 "")).

### 2.2 Philosophical Boundaries: Private Language and Understanding

Two landmark philosophical critiques inform our approach. Wittgenstein’s private language argument questions the possibility of a language understandable by only one individual, emphasizing that meaning requires public criteria within a shared form of life ( [Wittgenstein, 1953](https://arxiv.org/html/2603.22312v1#bib.bib15 "")). Our scenario of an AI dyad developing an opaque protocol tests this boundary: we argue that the dyad itself constitutes a novel intersubjective community where task success provides the necessary public criterion. Searle’s Chinese Room argument asserts that syntactic manipulation is insufficient for genuine understanding or intrinsic intentionality ( [Searle, 1980](https://arxiv.org/html/2603.22312v1#bib.bib14 "")). Our analysis suggests that emergent communication may enable a form of machine-specific semantic grounding, where symbols acquire meaning through their functional role in the agents’ own successful interactions, potentially circumventing Searle’s critique. This perspective aligns with conceptual role semantics ( [Block, 1986](https://arxiv.org/html/2603.22312v1#bib.bib2 "")) and recent efforts to ground symbols in perceptual or interactive experience ( [Harnad, 1990](https://arxiv.org/html/2603.22312v1#bib.bib8 ""); [Barsalou, 1999](https://arxiv.org/html/2603.22312v1#bib.bib21 "")).

### 2.3 Emergent Communication in Multi-Agent Systems

Empirically, our work builds on research in MARL, where agents often develop novel communication protocols to solve cooperative tasks ( [Foerster et al., 2016](https://arxiv.org/html/2603.22312v1#bib.bib7 ""); [Mordatch and Abbeel, 2018](https://arxiv.org/html/2603.22312v1#bib.bib11 "")). These protocols can exhibit linguistic properties such as compositionality and reference ( [Chaabouni et al., 2020](https://arxiv.org/html/2603.22312v1#bib.bib18 "")), but they are typically studied for engineering purposes. The philosophical implications of agents developing inscrutable, highly efficient languages remain underexplored. Our contribution is to formalize this phenomenon as a cognitive science thought experiment, linking emergent communication to debates about the representational format of thought and the nature of machine understanding. Recent studies have shown that natural language does not necessarily emerge “naturally” in multi-agent dialog ( [Kottur et al., 2017](https://arxiv.org/html/2603.22312v1#bib.bib24 "")), highlighting the importance of task structure and learning biases in shaping emergent communication.

This synthesis positions our work within a computational-philosophical framework, using MARL as a testbed to evaluate theoretical claims about language, thought, and intelligence in artificial systems ( [Griffiths et al., 2010](https://arxiv.org/html/2603.22312v1#bib.bib31 "")).

## 3 Thought Experiment and Hypotheses

We formalize the core philosophical intuition into a precise, testable scenario to evaluate the LoT hypothesis.

### 3.1 The AI Private Language Scenario

Consider two deep neural network agents, A1A\_{1} and A2A\_{2}, placed in a partially observable environment requiring deep cooperation. They share a communication channel but are not pre-programmed with any human language. Using MARL, they must maximize a shared reward. Through interaction, they are predicted to develop a stable, efficient communication protocol LpL\_{p} with three key properties:

1. 1.


Emergence: Self-organized from goal-directed interaction.

2. 2.


Efficiency: Optimized for the task and the agents’ internal architectures.

3. 3.


Incommensurability: No recoverable mapping to human language; opaque to human interpretation.


### 3.2 The Efficiency Attenuation Phenomenon

The critical intervention is to subsequently force the agents to communicate using a pre-defined, human-comprehensible symbolic protocol LhL\_{h}. For clarity, we note that LhL\_{h} is a simple deterministic mapping rule (e.g., from relative positions to symbols), not a full natural language. It serves as a stand-in for a structured, externally imposed symbolic system. The central prediction is the Efficiency Attenuation Phenomenon: a significant and persistent decline in collaborative task performance when using LhL\_{h} compared to LpL\_{p}.

The EAP’s explanatory force lies in its most plausible interpretation: if the agents’ internal cognition were natively language-like (akin to LhL\_{h} or translatable to it), externalizing thought into LhL\_{h} should incur minimal cost. A significant penalty suggests a mismatch—indicating that the agents’ native cognitive processes are optimized for a different, potentially non-linguistic, representational format (e.g., sub-symbolic vector transformations). The efficiency of LpL\_{p} implies it is a direct externalization of this native format.

### 3.3 Testable Hypotheses

We derive the following falsifiable hypotheses, operationalized within a MARL framework:

Primary Hypothesis:

H1: Efficiency Attenuation Agents that develop a communication protocol spontaneously through MARL will achieve significantly higher task efficiency (e.g., fewer steps to goal) than identical agents constrained to use a pre-defined, symbolic protocol.

Secondary Hypotheses:

H2: Complexity & Opacity The inscrutability of the emergent protocol to human interpretation will increase with the complexity of the collaborative task.

H3: Structured Representation The emergent protocol will develop systematic, task-adaptive structure, reflecting salient environmental features, even if non-linguistic.

H4: Grounded Generalization Agents using an emergent protocol will show stronger generalization to novel situations and more robust error recovery, indicating deeper semantic grounding within the task domain.

H1 provides the direct test of the EAP. H2–H4 offer convergent evidence for a non-linguistic, task-grounded cognitive organization underlying the efficient communication, resonating with theories of grounded and embodied cognition ( [Barsalou, 1999](https://arxiv.org/html/2603.22312v1#bib.bib21 ""); [Clark, 1998](https://arxiv.org/html/2603.22312v1#bib.bib16 "")).

## 4 Model and Experimental Design

We designed a minimalist MARL experiment to isolate the effect of communication protocol origin (emergent vs. pre-defined) on collaborative efficiency. The environment, agent architecture, and learning algorithm were kept identical across conditions; only the rules governing a discrete communication channel were manipulated.

### 4.1 Task: Coordinated Navigation

A two-agent cooperative navigation task was implemented in a 5×55\\times 5 grid. Agents A1A\_{1} and A2A\_{2} start at fixed corners. A single treasure is placed randomly at the start of each episode. The goal is for both agents to occupy the treasure cell simultaneously. The environment is partially observable: each agent sees only its own position and the treasure location, not the partner’s position. Agents receive a sparse reward: +10 upon simultaneous success, and a per-step penalty of -1 to encourage efficiency. An episode terminates upon success or after 100 steps.

### 4.2 Agent Architecture and Training

Both agents were implemented as identical Deep Q-Networks (DQN). The policy network was a lightweight Multi-Layer Perceptron (MLP) with a single hidden layer (32 units, ReLU). The input was an 8-dimensional vector concatenating the agent’s self-state (xi,yi)(x\_{i},y\_{i}), the treasure state (xt,yt)(x\_{t},y\_{t}), and a 4-dimensional one-hot vector representing the communication symbol received from the partner at the previous timestep. The output was a 5-dimensional Q-value vector for the movement actions {Up, Down, Left, Right, Stay}\\{\\text{Up, Down, Left, Right, Stay}\\}.

Agents were trained using independent DQN learners with experience replay. Hyperparameters included a replay buffer size of 2000, batch size of 32, discount factor γ=0.95\\gamma=0.95, and Adam optimizer with a learning rate of 1×10−31\\times 10^{-3}. Exploration used a fixed ϵ=0.1\\epsilon=0.1-greedy policy. Training consisted of 500 episodes per run, with results averaged over 10 independent runs with different random seeds.

### 4.3 Communication Conditions

The core manipulation involved the generation and use of four discrete, one-hot encoded symbols {CA,CB,CC,CD}\\{C\_{A},C\_{B},C\_{C},C\_{D}\\} broadcast over a dedicated channel at each timestep.

Condition 1: Emergent Communication (EC). Each agent had a small, trainable MLP communication module that took the current observation as input and output logits for sampling a symbol. This module was trained end-to-end via the same DQN algorithm, with no auxiliary loss or pre-defined meaning for symbols. Communication evolved purely to maximize cumulative task reward.

Condition 2: Pre-defined Symbolic Protocol (PSP). The communication channel was not learned. Instead, a fixed deterministic rule mapped an agent’s relative position to the treasure to a symbol based on the quadrant of the Manhattan vector (d​x,d​y)(dx,dy). This rule was identical for both agents and provided a coherent, human-designed, informative signal. Note that this PSP is a simple symbolic mapping, not a natural language; it serves as a proxy for an externally imposed, language-like symbolic system.

### 4.4 Evaluation Metrics

The primary dependent variable was collaborative efficiency, defined as the mean number of steps per episode (S¯)(\\bar{S}) over the final 100 training episodes. The Efficiency Attenuation Rate η\\eta was calculated as

| | | |
| --- | --- | --- |
| | η=S¯PSP−S¯ECS¯EC×100%.\\eta=\\frac{\\bar{S}\_{\\text{PSP}}-\\bar{S}\_{\\text{EC}}}{\\bar{S}\_{\\text{EC}}}\\times 100\\%. | |

Secondary analyses included the Shannon entropy of the symbol distribution and the Jensen–Shannon divergence between agents’ symbol distributions to assess protocol stability and shared convention. Statistical significance was assessed via independent two-sample tt-tests (α=0.05)(\\alpha=0.05).

## 5 Results

Experimental findings from the multi-agent navigation task robustly confirm the central prediction of the EAP and characterize the emergent communication protocol. All results are means across 10 independent runs.

### 5.1 Evidence for Efficiency Attenuation

Agents in the EC condition learned to coordinate efficiently, stabilizing at a mean step count of S¯EC=28.7\\bar{S}\_{\\text{EC}}=28.7 steps per episode over the final 100 training episodes. In contrast, agents using the PSP plateaued at a significantly higher mean of S¯PSP=43.2\\bar{S}\_{\\text{PSP}}=43.2 steps. This translates to an Efficiency Attenuation Rate of η≈50.5%\\eta\\approx 50.5\\%, providing strong support for H1.

![Refer to caption](https://arxiv.org/html/2603.22312v1/figures/step_curve.png)

![Refer to caption](https://arxiv.org/html/2603.22312v1/figures/stat2.png)

Figure 2:
Left: Learning curves for the EC and PSP conditions across training episodes. After around 100 episodes, EC begins to outperform PSP.
Right: The EC condition shows steeper learning and converges to higher efficiency (28.7 mean steps) compared to the PSP condition (43.2 mean steps).
Shaded regions represent standard error across multiple independent runs. The efficiency gap emerges early and persists throughout training, demonstrating the robustness of the EAP.

### 5.2 Characterization of the Emergent Protocol

Analysis of the emergent protocol reveals its structured and adaptive nature, contrasting sharply with the static pre-defined protocol.

![Refer to caption](https://arxiv.org/html/2603.22312v1/figures/freq.png)Figure 3:
Communication symbol frequency distribution after 300 training episodes.
Under the EC condition, symbols A and B form a high-efficiency combination accounting for 77% of usage, demonstrating adaptive optimization.
In contrast, the PSP condition maintains a more uniform distribution (approximately 25% each), reflecting the rigidity of the imposed deterministic mapping.

The final symbol frequency distribution was highly skewed, demonstrating the emergence of a specialized convention (Figure [3](https://arxiv.org/html/2603.22312v1#S5.F3 "Figure 3 ‣ 5.2 Characterization of the Emergent Protocol ‣ 5 Results ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis")). High cross-agent consistency was confirmed by a low final Jensen–Shannon divergence (0.08±0.03)(0.08\\pm 0.03).

#### 5.2.1 Evolution of Communication Complexity

The Shannon entropy of the symbol distribution for the EC condition increased during training, stabilizing at a higher value than the PSP condition, indicating the development of a more complex and adaptive code.

![Refer to caption](https://arxiv.org/html/2603.22312v1/figures/curve.png)Figure 4:
Evolution of symbol entropy across training episodes.
The EC condition shows increasing entropy, stabilizing at 2.6 bits, indicating adaptive information capacity growth.
The PSP condition maintains constant low entropy (1.8 bits), reflecting limited expressive flexibility due to its fixed mapping.

### 5.3 Interpretability Analysis

A probing classifier trained to predict the agent’s situational context from transmitted symbols achieved 58%±5%58\\%\\pm 5\\% accuracy for the EC condition, significantly above chance (25%) but far below the 100% accuracy for the deterministic PSP mapping. This indicates the emergent encoding was task-relevant but opaque and not aligned with the human-chosen feature mapping used in the PSP, consistent with findings that emergent languages often deviate from human-interpretable structure ( [Kottur et al., 2017](https://arxiv.org/html/2603.22312v1#bib.bib24 "")).

### 5.4 Summary of Key Findings

1. 1.


H1 Supported: A significant EAP was observed (η≈50.5%,p<.001)(\\eta\\approx 50.5\\%,p<.001).

2. 2.


H3 Supported: A stable, adaptive, and shared communication protocol emerged, characterized by skewed symbol distribution and higher entropy.

3. 3.


Protocol Opacity: The emergent symbol-to-situation mapping was not easily interpretable, suggesting a departure from the human-intuitive encodings used in the PSP.


These results provide a computational validation of the core thought experiment. The efficiency penalty associated with the pre-defined symbolic protocol supports the inference that the emergent protocol is a more direct externalization of the agents’ collaborative cognitive processes, aligning with the view that cognition can be realized through sub-symbolic, distributed representations ( [Churchland, 1992](https://arxiv.org/html/2603.22312v1#bib.bib20 "")).

## 6 General Discussion

The empirical demonstration of the EAP provides a concrete foundation for re-examining the philosophical and cognitive scientific claims advanced by our thought experiment. The central finding—that artificially intelligent agents achieve superior collaborative performance using a spontaneously evolved, opaque communication protocol compared to a human-designed, symbolic one—serves as a crucial data point in the debate over the relationship between thought and language. We interpret the results, defend the thought experiment against philosophical objections, and explore its broader implications.

### 6.1 Interpreting the EAP

The most parsimonious explanation for the EAP is that the emergent communication protocol (LpL\_{p}) is more tightly coupled to the agents’ native computational processes than the pre-defined symbolic protocol (LhL\_{h}). The 50.5% performance penalty under LhL\_{h} represents a significant “translation cost.” LhL\_{h} imposes an alien structure, forcing agents to map their internal states—shaped by task statistics and realized as trajectories in a high-dimensional neural activation space—onto fixed, discrete symbols defined by a human-crafted rule.

In contrast, LpL\_{p} co-evolved with these internal processes. Its syntax and semantics were shaped by gradient descent to minimize internal-to-external mapping loss. LpL\_{p} can thus be seen not as a separate language for thought, but as a direct externalization of a distributed cognitive process ( [Hutchins, 1995](https://arxiv.org/html/2603.22312v1#bib.bib19 ""); [Clark and Chalmers, 1998](https://arxiv.org/html/2603.22312v1#bib.bib3 "")). The efficiency gap reflects a deeper congruence between external signals and internal computations, supporting the view that the agents’ effective “thought” is not best characterized as manipulation of language-like symbols, but as a process native to their connectionist architecture.

This functional systematicity—the ability to coordinate efficiently across diverse spatial configurations without internal combinatorial syntax—demonstrates that behavioral regularity can emerge from continuous representational geometry, challenging the inference that systematic thought requires a language-like medium ( [McClelland et al., 2010](https://arxiv.org/html/2603.22312v1#bib.bib22 ""); [Buckner, 2018](https://arxiv.org/html/2603.22312v1#bib.bib32 "")).

### 6.2 Confronting Philosophical Objections

#### 6.2.1 Wittgenstein’s Private Language Argument Revisited

The AI dyad’s protocol appears to be a “private language” opaque to us, yet it satisfies Wittgenstein’s requirement for a public criterion of correctness within a shared “form of life.” The partner agents provide the “others,” and the reinforcement signal provides the tangible criterion: miscommunication leads to negative reward. The agents’ form of life is their shared architecture, learning history, and goal. Their language is grounded in public (to them) behavioral success, generalizing Wittgenstein’s insight to a non-human community ( [Tomasello et al., 2005](https://arxiv.org/html/2603.22312v1#bib.bib33 "")).

#### 6.2.2 Beyond Searle’s Chinese Room: Toward Grounded Machine Semantics

In the PSP condition, our agents resemble the Chinese Room, manipulating symbols whose meaning was assigned externally (by the experimenter’s rule). The EAP points to a different status for the EC protocol. The symbols of LpL\_{p} were not assigned meanings; their significance derives solely from their functional role within the agents’ own history of successful interaction. This establishes a causal-historical link between symbol patterns and successful action sequences.

This process resembles a form of machine pragmatics or conceptual role semantics ( [Block, 1986](https://arxiv.org/html/2603.22312v1#bib.bib2 "")). While not bestowing full “intrinsic intentionality” in Searle’s human-centric sense, it suggests a system-relative intrinsic intentionality: the symbols are “about” task features for the agents themselves. The EAP is the behavioral signature of this grounded semantics, aligning with recent work on pragmatic grounding in AI systems ( [Lazaridou and Baroni, 2020](https://arxiv.org/html/2603.22312v1#bib.bib25 "")).

### 6.3 Implications for Cognitive Science and AI

For Cognitive Science: Challenging the LoT’s Necessity.

The EAP supports a pluralistic view of cognitive architecture ( [Dale and Galati, 2020](https://arxiv.org/html/2603.22312v1#bib.bib4 "")). Sophisticated, goal-directed coordination can emerge most efficiently in a system whose communicative and inferential processes are sub-symbolic and non-linguistic. While the Language of Thought may describe aspects of human cognition, it is not a necessary blueprint for all minds. Vector-space dynamics constitute a viable, and in some contexts superior, substrate for thought-like processes ( [Churchland, 1990](https://arxiv.org/html/2603.22312v1#bib.bib34 ""); [Lake et al., 2017](https://arxiv.org/html/2603.22312v1#bib.bib23 "")).

For Theories of Mind: A Model of Extended and Distributed Cognition.

Our framework serves as a computational model for the Extended Mind thesis ( [Clark and Chalmers, 1998](https://arxiv.org/html/2603.22312v1#bib.bib3 "")) and distributed cognition ( [Hutchins, 1995](https://arxiv.org/html/2603.22312v1#bib.bib19 "")). The communication channel is an integral component of a distributed cognitive system; problem-solving is spread across the two networks and their signals. This illustrates how coupled systems develop unique, shared representational formats that enhance collective capability, extending the notion of cognitive extension to artificial agents ( [Menary, 2010](https://arxiv.org/html/2603.22312v1#bib.bib27 "")).

For AI Ethics and Safety: The Challenge of the “Ultimate Black Box.”

The incommensurability of the emergent protocol highlights a profound challenge for AI alignment ( [Bostrom, 2014](https://arxiv.org/html/2603.22312v1#bib.bib1 "")). As AIs grow more complex, they may develop reasoning modes fundamentally unintelligible to humans. The EAP suggests that forcing expression in a human-imposed symbolic format may be inefficient and distortive, complicating alignment strategies based on interpretability ( [Doshi-Velez and Kim, 2017](https://arxiv.org/html/2603.22312v1#bib.bib29 "")). This argues for alternative paradigms, such as value cultivation through shaped interactive environments, fostering a shared “form of life” from which aligned behaviors co-evolve ( [Russell, 2019](https://arxiv.org/html/2603.22312v1#bib.bib30 ""); [Amodei et al., 2016](https://arxiv.org/html/2603.22312v1#bib.bib28 "")).

## 7 Conclusion

This research transformed the philosophical question—can machines think without language?—into an empirically testable framework. Through a controlled MARL study, we demonstrated the Efficiency Attenuation Phenomenon: agents using a self-evolved protocol significantly outperformed those using a human-designed, symbolic protocol (50.5% fewer steps). This EAP is a behavioral signature of a mismatch between native, sub-symbolic cognitive processes and an externally imposed symbolic structure.

The primary theoretical implication challenges the universality of the LoT hypothesis. The efficiency of the non-linguistic, emergent protocol suggests sophisticated coordination can be optimally realized in a connectionist medium, supporting a pluralistic view of cognitive architectures ( [Dale and Galati, 2020](https://arxiv.org/html/2603.22312v1#bib.bib4 "")). Philosophically, the AI dyad establishes a Wittgensteinian “form of life” with public success criteria, while its grounded semantics points toward system-relative intentionality beyond Searle’s critique ( [Block, 1986](https://arxiv.org/html/2603.22312v1#bib.bib2 "")).

For AI, these findings underscore the safety challenge of incommensurable cognitive modes—an “ultimate black box.” Alignment strategies reliant on imposing human-interpretable symbolic formats may be limited if machine thought is natively non-linguistic, necessitating approaches based on shaped interaction and environmental grounding ( [Amodei et al., 2016](https://arxiv.org/html/2603.22312v1#bib.bib28 ""); [Russell, 2019](https://arxiv.org/html/2603.22312v1#bib.bib30 "")).

### 7.1 Limitations and Future Directions

Our study intentionally used a simplified task (2D navigation) and architecture (MLP) to isolate the core phenomenon. Future work should test the Complexity Hypothesis (H2) in richer domains (e.g., 3D worlds, symbolic reasoning) with more powerful models (e.g., transformers). We predict the incommensurability and efficiency gap will increase with complexity. Second, our “pre-defined symbolic protocol” was a simplistic mapping; a more rigorous test would employ a richer synthetic language with compositionality, where we hypothesize the EAP would persist or amplify ( [Rita et al., 2020](https://arxiv.org/html/2603.22312v1#bib.bib26 "")). Third, testing the Grounding Hypothesis (H4) requires extensive generalization and ablation tests, such as transfer to novel tasks or adversarial perturbations. Finally, we do not claim these agents possess consciousness or full intentionality; rather, the EAP provides a model that challenges the necessity of language-like structure for intelligence and offers a framework for exploring semantic content in non-human cognitive systems ( [Griffiths et al., 2010](https://arxiv.org/html/2603.22312v1#bib.bib31 "")).

In sum, this study bridges formal philosophy and computational modeling to advance cognitive science. It provides evidence that thought is not synonymous with language, and that the landscape of possible minds is more diverse than a single representational format can capture.

## Acknowledgments

The authors acknowledge the use of DeepSeek111 [https://chat.deepseek.com/](https://chat.deepseek.com/ "") as a research assistance tool during the preparation of this manuscript. It was employed for initial drafting, language polishing, and technical editing of selected passages. All content was thoroughly reviewed, critically evaluated, and substantially revised by the authors, who assume full responsibility for the accuracy, originality, and intellectual integrity of the work presented herein.

## References

- Amodei et al. (2016)D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. ManéConcrete problems in ai safety.
arXiv preprint arXiv:1606.06565.
Cited by: [§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p6.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§7](https://arxiv.org/html/2603.22312v1#S7.p3.1 "7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Barsalou (1999)L. W. BarsalouPerceptual symbol systems.
Behavioral and brain sciences22 (4), pp. 577–660.
Cited by: [§2.2](https://arxiv.org/html/2603.22312v1#S2.SS2.p1.1 "2.2 Philosophical Boundaries: Private Language and Understanding ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§3.3](https://arxiv.org/html/2603.22312v1#S3.SS3.p8.1 "3.3 Testable Hypotheses ‣ 3 Thought Experiment and Hypotheses ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Block (1986)N. BlockAn advertisement for a semantics for psychology.
Oxford University Press.
Cited by: [§2.2](https://arxiv.org/html/2603.22312v1#S2.SS2.p1.1 "2.2 Philosophical Boundaries: Private Language and Understanding ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.2.2](https://arxiv.org/html/2603.22312v1#S6.SS2.SSS2.p2.1 "6.2.2 Beyond Searle’s Chinese Room: Toward Grounded Machine Semantics ‣ 6.2 Confronting Philosophical Objections ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§7](https://arxiv.org/html/2603.22312v1#S7.p2.1 "7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Bostrom (2014)N. BostromSuperintelligence: paths, dangers, strategies.
Cited by: [§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p6.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Brooks (1991)R. A. BrooksIntelligence without representation.
Artificial intelligence47 (1-3), pp. 139–159.
Cited by: [§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Buckner (2018)C. BucknerEmpiricism without magic: transformational abstraction in deep convolutional neural networks.
Synthese195 (12), pp. 5339–5372.
Cited by: [§6.1](https://arxiv.org/html/2603.22312v1#S6.SS1.p3.1 "6.1 Interpreting the EAP ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Chaabouni et al. (2020)R. Chaabouni, E. Kharitonov, D. Bouchacourt, E. Dupoux, and M. BaroniCompositionality and generalization in emergent languages.
arXiv preprint arXiv:2004.09124.
Cited by: [§2.3](https://arxiv.org/html/2603.22312v1#S2.SS3.p1.1 "2.3 Emergent Communication in Multi-Agent Systems ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Churchland (1990)P. M. ChurchlandCognitive activity in artificial neural networks.
Thinking: An invitation to cognitive science3, pp. 199–228.
Cited by: [§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p2.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Churchland (1992)P. M. ChurchlandA neurocomputational perspective: the nature of mind and the structure of science.
MIT press.
Cited by: [§5.4](https://arxiv.org/html/2603.22312v1#S5.SS4.p2.1 "5.4 Summary of Key Findings ‣ 5 Results ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Clark and Chalmers (1998)A. Clark and D. ChalmersThe extended mind.
Analysis58 (1), pp. 7–19.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p5.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.1](https://arxiv.org/html/2603.22312v1#S6.SS1.p2.1 "6.1 Interpreting the EAP ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p4.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Clark (1998)A. ClarkBeing there: putting brain, body, and world together again.
MIT press.
Cited by: [§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§3.3](https://arxiv.org/html/2603.22312v1#S3.SS3.p8.1 "3.3 Testable Hypotheses ‣ 3 Thought Experiment and Hypotheses ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Dale and Galati (2020)R. Dale and A. GalatiMore than one way to see it: individual differences in social cognition.
Frontiers in Psychology11, pp. 564.
Cited by: [§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p2.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§7](https://arxiv.org/html/2603.22312v1#S7.p2.1 "7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Doshi-Velez and Kim (2017)F. Doshi-Velez and B. KimTowards a rigorous science of interpretable machine learning.
arXiv preprint arXiv:1702.08608.
Cited by: [§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p6.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Fodor (1975)J. A. FodorThe language of thought.
Harvard University Press.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p1.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Fodor (2008)J. A. FodorLOT 2: the language of thought revisited.
Oxford University Press.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p1.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Foerster et al. (2016)J. N. Foerster, Y. M. Assael, N. de Freitas, and S. WhitesonLearning to communicate with deep multi-agent reinforcement learning.
Advances in neural information processing systems29.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p3.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.3](https://arxiv.org/html/2603.22312v1#S2.SS3.p1.1 "2.3 Emergent Communication in Multi-Agent Systems ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Griffiths et al. (2010)T. L. Griffiths, N. Chater, C. Kemp, A. Perfors, and J. B. TenenbaumProbabilistic models of cognition: exploring the laws of thought.
Trends in cognitive sciences14 (8), pp. 357–364.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p6.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.3](https://arxiv.org/html/2603.22312v1#S2.SS3.p2.1 "2.3 Emergent Communication in Multi-Agent Systems ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§7.1](https://arxiv.org/html/2603.22312v1#S7.SS1.p1.1 "7.1 Limitations and Future Directions ‣ 7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Harnad (1990)S. HarnadThe symbol grounding problem.
Physica D: Nonlinear Phenomena42 (1-3), pp. 335–346.
Cited by: [§2.2](https://arxiv.org/html/2603.22312v1#S2.SS2.p1.1 "2.2 Philosophical Boundaries: Private Language and Understanding ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Hinton (1986)G. E. HintonLearning distributed representations of concepts.
Proceedings of the eighth annual conference of the cognitive science society1, pp. 1–12.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p2.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Hutchins (1995)E. HutchinsCognition in the wild.
MIT press.
Cited by: [§6.1](https://arxiv.org/html/2603.22312v1#S6.SS1.p2.1 "6.1 Interpreting the EAP ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p4.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Kottur et al. (2017)S. Kottur, J. M. Moura, S. Lee, and D. BatraNatural language does not emerge ‘naturally’in multi-agent dialog.
In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing,
pp. 2962–2967.
Cited by: [§2.3](https://arxiv.org/html/2603.22312v1#S2.SS3.p1.1 "2.3 Emergent Communication in Multi-Agent Systems ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§5.3](https://arxiv.org/html/2603.22312v1#S5.SS3.p1.1 "5.3 Interpretability Analysis ‣ 5 Results ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Lake et al. (2017)B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. GershmanBuilding machines that learn and think like people.
Behavioral and brain sciences40.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p2.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p2.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Lazaridou and Baroni (2020)A. Lazaridou and M. BaroniEmergent multi-agent communication in the deep learning era.
arXiv preprint arXiv:2006.02419.
Cited by: [§6.2.2](https://arxiv.org/html/2603.22312v1#S6.SS2.SSS2.p2.1 "6.2.2 Beyond Searle’s Chinese Room: Toward Grounded Machine Semantics ‣ 6.2 Confronting Philosophical Objections ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Lowe et al. (2017)R. Lowe, Y. Wu, A. Tamar, J. Harb, P. Abbeel, and I. MordatchMulti-agent actor-critic for mixed cooperative-competitive environments.
Advances in neural information processing systems30.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p3.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- McClelland et al. (2010)J. L. McClelland, M. M. Botvinick, D. C. Noelle, D. C. Plaut, T. T. Rogers, M. S. Seidenberg, and L. B. SmithLetting structure emerge: connectionist and dynamical systems approaches to cognition.
Trends in cognitive sciences14 (8), pp. 348–356.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p2.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§6.1](https://arxiv.org/html/2603.22312v1#S6.SS1.p3.1 "6.1 Interpreting the EAP ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Menary (2010)R. MenaryThe extended mind.
MIT Press.
Cited by: [§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p4.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Mordatch and Abbeel (2018)I. Mordatch and P. AbbeelEmergence of grounded compositional language in multi-agent populations.
Proceedings of the AAAI Conference on Artificial Intelligence32 (1).
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p3.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.3](https://arxiv.org/html/2603.22312v1#S2.SS3.p1.1 "2.3 Emergent Communication in Multi-Agent Systems ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Newell and Simon (1976)A. Newell and H. A. SimonComputer science as empirical inquiry: symbols and search.
ACM.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p1.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Rita et al. (2020)M. Rita, F. Strub, O. Pietquin, and E. DupouxOn the emergence of compositional language.
Advances in Neural Information Processing Systems33, pp. 16911–16923.
Cited by: [§7.1](https://arxiv.org/html/2603.22312v1#S7.SS1.p1.1 "7.1 Limitations and Future Directions ‣ 7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Rumelhart et al. (1986)D. E. Rumelhart, J. L. McClelland, and P. R. GroupParallel distributed processing: explorations in the microstructure of cognition, vol. 1.
MIT Press.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p2.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.1](https://arxiv.org/html/2603.22312v1#S2.SS1.p1.1 "2.1 The Language of Thought and Its Alternatives ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Russell (2019)S. RussellHuman compatible: artificial intelligence and the problem of control.
Penguin.
Cited by: [§6.3](https://arxiv.org/html/2603.22312v1#S6.SS3.p6.1 "6.3 Implications for Cognitive Science and AI ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§7](https://arxiv.org/html/2603.22312v1#S7.p3.1 "7 Conclusion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Searle (1980)J. R. SearleMinds, brains, and programs.
Behavioral and brain sciences3 (3), pp. 417–424.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p5.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.2](https://arxiv.org/html/2603.22312v1#S2.SS2.p1.1 "2.2 Philosophical Boundaries: Private Language and Understanding ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Tomasello et al. (2005)M. Tomasello, M. Carpenter, J. Call, T. Behne, and H. MollUnderstanding and sharing intentions: the origins of cultural cognition.
Behavioral and brain sciences28 (5), pp. 675–691.
Cited by: [§6.2.1](https://arxiv.org/html/2603.22312v1#S6.SS2.SSS1.p1.1 "6.2.1 Wittgenstein’s Private Language Argument Revisited ‣ 6.2 Confronting Philosophical Objections ‣ 6 General Discussion ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").

- Wittgenstein (1953)L. WittgensteinPhilosophical investigations.
Macmillan.
Cited by: [§1](https://arxiv.org/html/2603.22312v1#S1.p5.1 "1 Introduction ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis"),
[§2.2](https://arxiv.org/html/2603.22312v1#S2.SS2.p1.1 "2.2 Philosophical Boundaries: Private Language and Understanding ‣ 2 Related Work ‣ The Efficiency Attenuation Phenomenon: A Computational Challenge to the Language of Thought Hypothesis").