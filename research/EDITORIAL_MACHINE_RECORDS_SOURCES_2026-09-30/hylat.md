Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2605.25421v1 \[cs.CL\] 25 May 2026

# HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol

Xinyi Mou111



Equal contribution.Email: [xymou20@fudan.edu.cn](mailto:xymou20@fudan.edu.cn)Siyuan Wang111



Equal contribution.Affiliation: Fudan University,
The Chinese University of Hong Kong
Email: [zejunli20@fudan.edu.cn](mailto:zejunli20@fudan.edu.cn)Zejun Li
Email: [zywei@fudan.edu.cn](mailto:zywei@fudan.edu.cn)Yulan He222



Corresponding author.Email: [siyuanwang@cuhk.edu.hk](mailto:siyuanwang@cuhk.edu.hk)Zhongyu Wei222



Corresponding author.Affiliation: King’s College London,
The Alan Turing Institute,
Shanghai Innovation Institute
Email: [yulan.he@kcl.ac.uk](mailto:yulan.he@kcl.ac.uk)

###### Abstract

Communication protocol design is a central challenge in large language model-based multi-agent systems. Existing single-channel approaches face an inherent communication trilemma: text-based methods are interpretable but verbose, while latent-space methods are efficient but opaque and limited to unidirectional workflows. Inspired by multi-channel communication theory, we propose HyLaT, a hybrid latent-text communication protocol that transmits elaborate cognitive signals through a latent channel for efficiency, while expressing concise critical signals in natural language to preserve interpretability and precision. We introduce a two-stage training framework combining single-agent hybrid generation learning and multi-agent interactive co-training, enabling agents to generate and interpret hybrid messages across multiple rounds of interaction. Experiments demonstrate that HyLaT reduces communication overhead significantly while maintaining competitive task performance, with strong generalization and robustness across diverse settings 111



Equal contribution..

11footnotetext: Code is available at [https://github.com/xymou/hylat](https://github.com/xymou/hylat "").

## 1 Introduction

Large Language Models (LLM)-based multi-agent systems have shown strong performance in collaborative problem solving and social simulations [Guo et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib10 ""); [Mou et al. (2024a)](https://arxiv.org/html/2605.25421v1#bib.bib20 ""); [Qian et al. (2024a)](https://arxiv.org/html/2605.25421v1#bib.bib25 ""). In these systems, communication serves as the backbone of coordination, enabling agents to exchange information, align on shared goals, and collectively reason across extended interactions. As systems scale to more agents and longer horizons, the design of inter-agent communication protocols becomes a central challenge that directly shapes system capability and scalability [Marro et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib18 ""); [Zhang et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib37 ""); [Chen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib2 "").

![Refer to caption](https://arxiv.org/html/2605.25421v1/intro_v2.png)Figure 1: Comparison among different multi-agent communication paradigms. (A) Text-based communication: fully readable but with a heavy efficiency bottleneck. (B) Latent communication: highly efficient but opaque to users. (C) Hybrid latent-text communication (ours): balances efficiency and explainability through a dual-channel design.

Existing communication paradigms can be broadly characterized as single-channel, either text or latent space.
As illustrated in Figure [1](https://arxiv.org/html/2605.25421v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") A, text-based methods [Du et al. (2023)](https://arxiv.org/html/2605.25421v1#bib.bib5 ""); [Park et al. (2023)](https://arxiv.org/html/2605.25421v1#bib.bib23 ""); [Zhang et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib38 "") rely entirely on natural language, which, while interpretable, leads to verbose messages with high token overhead. Recent latent-space
communication methods [Zou et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib39 ""); [Du et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib6 ""); [Fu et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib7 ""); [Wu et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib34 "") instead exchange internal representations (Figure [1](https://arxiv.org/html/2605.25421v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") B), achieving dense and efficient
transfer but at the cost of interpretability. Latent signals are opaque to external observers, limiting applicability to scenarios where intermediate transparency
is essential, such as social simulation. Moreover, existing latent-space methods are primarily designed for single-shot or one-directional exchanges within a fixed workflow. This leaves multi-round interactive communication among multiple agents in more realistic settings largely unsupported.

The tension between interpretability and efficiency reflects a deeper structural limitation known as the _agent communication trilemma_ [Marro et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib18 ""):
no single-channel protocols can simultaneously optimize for
efficiency, portability, and versatility.
This suggests that the communication channel itself must be reconsidered.
Inspired by multi-channel communication
theory [Shannon (1948)](https://arxiv.org/html/2605.25421v1#bib.bib28 ""); [Monge and Contractor (2003)](https://arxiv.org/html/2605.25421v1#bib.bib19 "") that different types of information are best transmitted through varied channels suited to their functional roles, we argue that the heterogeneous nature of agent messages calls for an analogous hybrid communication design.
Specifically, agent messages often contain two functionally distinct types of information: (1) elaborate cognitive signals, such as explanations, intermediate reasoning, and contextual elaboration, that are well-suited to compact latent-space representations; and (2) concise but critical signals, such as answers, commitments, or final decisions, that must remain interpretable to both agents and human observers.

To this end, we propose HyLaT, a Hybrid Latent-Text communication protocol that routes each type of information through a dedicated channel (Figure [1](https://arxiv.org/html/2605.25421v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") C). Dense intermediate information flows through a latent channel for efficient machine-to-machine transfer, while concise critical signals are expressed in natural language to preserve interpretability. This dual-channel design addresses all axes of the trilemma: the latent channel provides efficiency, the text channel enables interoperation with agents using other protocols, and the combination provides versatility by supporting multi-round, multi-agent interaction, a setting that prior latent-space methods largely cannot handle.

Realizing this design poses key training challenges that agents need to learn generating hybrid outputs and also interpreting latent vectors from peers during multi-turn interactions. We address this with a two-stage training framework.
The first stage, single-agent hybrid generation learning, equips the model to generate hybrid responses from text-only inputs, using a cross-channel alignment loss to transfer the semantic content of textual elaborations into the latent space. The second stage, multi-agent interactive co-learning, enables agents to jointly learn to interpret and respond across both channels.
We evaluate HyLaT on various tasks, demonstrating that it significantly reduces communication overhead while maintaining strong task performance and preserving interpretability.
Our contributions are summarized as follows:

- •


We identify channel multiplicity as a structural resolution to the agent communication trilemma and introduce HyLaT, a hybrid latent-text communication protocol that enables agents to exchange information through complementary latent and textual channels.

- •


We propose a two-stage training approach combining single-agent hybrid learning and multi-agent interactive co-learning, enabling agents to generate and interpret both latent and textual messages in multi-round interactions.

- •


Experiments demonstrate that HyLaT effectively balances communication efficiency and information transparency, enabling scalable and interpretable multi-agent collaboration.


## 2 Methodology

![Refer to caption](https://arxiv.org/html/2605.25421v1/fm_0315.png)Figure 2: Overview of the proposed HyLaT framework. Agents exchange elaborate intermediate signals through a latent channel and concise commitments through a text channel. The model is trained to generate hybrid content in Stage 1 and to support multi-round hybrid communication in Stage 2.

### 2.1 Overview

This section details the proposed HyLaT framework, designed to facilitate efficient and transparent communication among agents. As illustrated in Figure [2](https://arxiv.org/html/2605.25421v1#S2.F2 "Figure 2 ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), we first define the dual-channel agent communication protocol in Section [2.2](https://arxiv.org/html/2605.25421v1#S2.SS2 "2.2 Hybrid Communication Protocol ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"). Furthermore, we design a two-stage training framework to empower existing models with dual-channel communication capabilities. Stage 1: Single-Agent Hybrid Generation Learning (Section [2.3](https://arxiv.org/html/2605.25421v1#S2.SS3 "2.3 Stage 1: Single-Agent Hybrid Generation Learning ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")) trains each agent to generate hybrid outputs consisting of both text and latent representations; and Stage 2: Multi-agent Interactive Co-Training (Section [2.4](https://arxiv.org/html/2605.25421v1#S2.SS4 "2.4 Stage 2: Multi-Agent Interactive Co-Training ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")) enables the shared backbone of multiple agents to jointly learn to interpret and respond to dual-channel information generated by others during multi-turn interactions.

### 2.2 Hybrid Communication Protocol

#### Interactive Setup

As illustrated in the top part of Figure [2](https://arxiv.org/html/2605.25421v1#S2.F2 "Figure 2 ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), we consider a multi-agent system of NN agents powered by a shared backbone model MM, communicating over TT
interaction rounds.
At round t=1t=1, every agent receives a text context. At each subsequent round t>1t>1, agent ii receives its accumulated context together with the responses from all other agents in the previous round:

| | | | |
| --- | --- | --- | --- |
| | xi(t)=\[𝐱i(t−1),⊕j≠ioj(t−1)\],t>1x\_{i}^{(t)}=\\Bigl\[\\mathbf{x}\_{i}^{(t-1)},\\;\\oplus\_{j\\neq i}o\_{j}^{(t-1)}\\Bigr\],\\quad t>1 | | (1) |

where 𝐱i(t−1)\\mathbf{x}\_{i}^{(t-1)} is agent ii’s accumulated context up to round t−1t-1, oj(t−1)o\_{j}^{(t-1)} denotes the response from agent jj at round t−1t-1, and ⊕\\oplus denotes concatenation. Agent ii then generates a response oi(t)=M⁡(xi(t))o\_{i}^{(t)}=M(x\_{i}^{(t)}).

#### Dual-Channel Response Format

In HyLaT, the output of agent ii at round tt consists of two parts from distinct channels: a latent
component 𝐙i(t)=(z1,…,zk)\\mathbf{Z}\_{i}^{(t)}=(z\_{1},\\ldots,z\_{k}) carrying elaborate cognitive signals, and a
text component 𝐘i(t)=(y1,…,ym)\\mathbf{Y}\_{i}^{(t)}=(y\_{1},\\ldots,y\_{m}) carrying concise, interpretable
conclusions:

| | | | |
| --- | --- | --- | --- |
| | oi(t)=\[⟨bot⟩​z1,…,zk​⟨eot⟩\]⏟latent component\|\[y1,…,ym\]⏟text component,o\_{i}^{(t)}=\\underbrace{\[\\langle\\texttt{bot}\\rangle\\;z\_{1},\\ldots,z\_{k}\\;\\langle\\texttt{eot}\\rangle\]}\_{\\text{latent component}}\\;\\\|\\;\\underbrace{\[y\_{1},\\ldots,y\_{m}\]}\_{\\text{text component}}, | | (2) |

where the latent component consists of kk continuous vectors produced by
autoregressively propagating the model’s last hidden state,
delimited by two learnable special tokens ⟨bot⟩\\langle\\texttt{bot}\\rangle and ⟨eot⟩\\langle\\texttt{eot}\\rangle.
The text component is a standard
natural-language sequence generated after ⟨eot⟩\\langle\\texttt{eot}\\rangle.

#### Channel Specialization

To balance communication efficiency with transparency, we retain the summary part of agent responses–such as final answers and commitments–in the textual channel. Conversely, verbose information, including explanations, elaboration, and reasoning processes, is compressed into the latent component. This channel specialization capability is induced through the structure of training data described in Section [2.3](https://arxiv.org/html/2605.25421v1#S2.SS3 "2.3 Stage 1: Single-Agent Hybrid Generation Learning ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol").

### 2.3 Stage 1: Single-Agent Hybrid Generation Learning

The goal of Stage 1 is to train the model to produce well-formed hybrid outputs from text-only input, preparing it for multi-agent interaction in Stage 2.
To achieve this, we construct single- and multi-turn user-assistant dialogues in single-agent scenarios as supervision. Each turn pairs a text input xx with a target response including both a textual elaboration ee and a critical output yy, corresponding to the two information types defined earlier.

As shown in Figure [2](https://arxiv.org/html/2605.25421v1#S2.F2 "Figure 2 ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") (bottom-left), each training step involves two forward passes over the input:

#### Forward with Hybrid Responses

Since no ground-truth latent supervision exists, teacher forcing is inapplicable to the latent component. The model instead autoregressively generates kk continuous latent vectors (𝐙={zi}i=1k\\mathbf{Z}=\\{z\_{i}\\}\_{i=1}^{k}) starting from ⟨bot⟩\\langle\\texttt{bot}\\rangle, after which ⟨eot⟩\\langle\\texttt{eot}\\rangle and target yy are appended. The language modeling loss is computed over yy:

| | | | |
| --- | --- | --- | --- |
| | ℒhybrid=−1\|y\|∑ilogP(yi∣y1:i−1,x,𝐙),\\mathcal{L}\_{\\text{hybrid}}=-\\frac{1}{\|y\|}\\sum\_{i}\\log P(y\_{i}\\mid y\_{1:i-1},\\,x,\\,\\mathbf{Z}), | | (3) |

ℒhybrid\\mathcal{L}\_{\\text{hybrid}} guides the model to derive yy based on its self-generated intermediate latent information 𝐙\\mathbf{Z}.

#### Forward with Textual Responses

To provide meaningful supervision for 𝐙\\mathbf{Z}, we
follow [Shen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib29 "") and introduce a pure-text branch.
In parallel with the hybrid forward pass, the model is trained to generate r=\[e,y\]r=\[e,\\,y\] conditioned on xx:

| | | | |
| --- | --- | --- | --- |
| | ℒtext=−1\|r\|∑ilogP(ri∣r1:i−1,x),\\mathcal{L}\_{\\text{text}}=-\\frac{1}{\|r\|}\\sum\_{i}\\log P(r\_{i}\\mid r\_{1:i-1},\\,x), | | (4) |

ℒtext\\mathcal{L}\_{\\text{text}} is optimized under teacher forcing to preserve the model’s ability to produce explicit elaborations.

#### Cross-Channel Alignment

Based on the parallel forward passes, we transfer the information encoded in ee into the latent space by aligning the hidden activations of both branches at a shared target position. This position is defined as the token immediately preceding the final answer (e.g., the token “is” in “My answer is A”), where all preceding context about the elaboration must be compressed before predicting the answer.
This alignment is applied across all LL transformer layers:

| | | | |
| --- | --- | --- | --- |
| | ℒalign=1L​∑l=1L‖sg⁡\[𝐡Tl\]−𝐡Sl‖2,\\mathcal{L}\_{\\text{align}}=\\frac{1}{L}\\sum\_{l=1}^{L}\\left\\\|\\operatorname{sg}\\left\[\\mathbf{h}\_{T}^{l}\\right\]-\\mathbf{h}\_{S}^{l}\\right\\\|\_{2}, | | (5) |

where 𝐡Tl\\mathbf{h}^{l}\_{T} and
𝐡Sl\\mathbf{h}^{l}\_{S} denote the hidden activations at the target position in the ll-th layer for the textual and the hybrid forward pass, respectively. sg⁡(⋅)\\operatorname{sg}(\\cdot) is the stop-gradient operation.

Overall, the training loss for Stage 1 is:

| | | | |
| --- | --- | --- | --- |
| | ℒstage1=α​ℒhybrid+β​ℒtext+γ​ℒalign,\\mathcal{L}\_{\\text{stage1}}=\\alpha\\mathcal{L}\_{\\text{hybrid}}+\\beta\\mathcal{L}\_{\\text{text}}+\\gamma\\mathcal{L}\_{\\text{align}}, | | (6) |

where α\\alpha, β\\beta and γ\\gamma are hyperparameters. This training process can be directly extended to multi-turn dialogues by generating latent-channel responses turn-by-turn during the hybrid forward pass.

### 2.4 Stage 2: Multi-Agent Interactive Co-Training

Stage 2 trains agents to communicate under the HyLaT protocol, exposing each agent to latent vectors produced by its peers. The training data consists of multi-turn, multi-agent dialogues, including the topic context for the initial round x(1)x^{(1)} and the textual responses {yi(t)}i=1N\\{y\_{i}^{(t)}\\}\_{i=1}^{N} from NN agents at each turn tt. Similar to Stage 1, each response yi(t)y\_{i}^{(t)} is augmented with its corresponding elaboration ei(t)e\_{i}^{(t)}.

Following the protocol formulated in Section [2.2](https://arxiv.org/html/2605.25421v1#S2.SS2 "2.2 Hybrid Communication Protocol ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), we construct the input xi(t)x\_{i}^{(t)} for each agent at turn tt by integrating prior context and responses from other agents (Equation [1](https://arxiv.org/html/2605.25421v1#S2.E1 "In Interactive Setup ‣ 2.2 Hybrid Communication Protocol ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")). Regarding the outputs, consistent with Stage 1, the textual forward pass utilizes the labeled \[ei(t),yi(t)\]\[e\_{i}^{(t)},y\_{i}^{(t)}\] under teacher-forcing training, while the hybrid forward pass generates latent representations Zi(t)Z\_{i}^{(t)} turn-by-turn.

Based on the constructed inputs and outputs, we calculate the loss Lstage1L\_{\\text{stage1}} for each agent, then aggregate losses across all NN agents:

| | | | |
| --- | --- | --- | --- |
| | ℒstage2=1N​∑i=1N(α​ℒhybrid(i)+β​ℒtext(i)+γ​ℒalign(i)),\\mathcal{L}\_{\\text{stage2}}=\\frac{1}{N}\\sum\_{i=1}^{N}\\Bigl(\\alpha\\,\\mathcal{L}\_{\\text{hybrid}}^{(i)}+\\beta\\,\\mathcal{L}\_{\\text{text}}^{(i)}+\\gamma\\,\\mathcal{L}\_{\\text{align}}^{(i)}\\Bigr), | | (7) |

where ℒhybrid(i)\\mathcal{L}\_{\\text{hybrid}}^{(i)}, ℒtext(i)\\mathcal{L}\_{\\text{text}}^{(i)}, and
ℒalign(i)\\mathcal{L}\_{\\text{align}}^{(i)} are respectively defined in Equations [3](https://arxiv.org/html/2605.25421v1#S2.E3 "In Forward with Hybrid Responses ‣ 2.3 Stage 1: Single-Agent Hybrid Generation Learning ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")– [5](https://arxiv.org/html/2605.25421v1#S2.E5 "In Cross-Channel Alignment ‣ 2.3 Stage 1: Single-Agent Hybrid Generation Learning ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol").
Through this joint training, agents are exposed to peers’ latent vectors as part of their input context and learn to interpret them while generating a proper hybrid response.

## 3 Experimental Setup

### 3.1 Training Data Construction

#### Stage 1

To construct data required in Section [2.3](https://arxiv.org/html/2605.25421v1#S2.SS3 "2.3 Stage 1: Single-Agent Hybrid Generation Learning ‣ 2 Methodology ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), we collect datasets with detailed explanations or reasoning chains as supervision for the latent component: CommonsenseQA [Talmor et al. (2019)](https://arxiv.org/html/2605.25421v1#bib.bib31 ""),
SocialIQA [Sap et al. (2019)](https://arxiv.org/html/2605.25421v1#bib.bib27 ""), WorldTree [Jansen et al. (2018)](https://arxiv.org/html/2605.25421v1#bib.bib14 ""), PubMedQA [Jin et al. (2019)](https://arxiv.org/html/2605.25421v1#bib.bib16 ""), and StrategyQA [Geva et al. (2021)](https://arxiv.org/html/2605.25421v1#bib.bib8 ""). All selected datasets contain detailed reasoning processes paired with concise final answers. This data-driven approach allows channel specialization to emerge naturally from the structure of the training examples, without requiring explicit routing annotations.

#### Stage 2

We construct two types of multi-agent interaction data. (1) _Refinement_: using Llama-3.2-1B-Instruct and GPT-5 [Singh et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib30 "") to conduct simulated multi-agent debate on Stage 1 datasets,
producing multi-round hybrid-output trajectories that converge to a final answer, where the answers of the first round may be incorrect. (2) _Decomposition_: Multi-hop questions sampled from HotpotQA [Yang et al. (2018)](https://arxiv.org/html/2605.25421v1#bib.bib36 ""), 2WikiMultiHopQA [Ho et al. (2020)](https://arxiv.org/html/2605.25421v1#bib.bib12 ""), and GSM8K-Aug-NL [Shen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib29 "") are decomposed into parallel sub-questions assigned across agents, who collaborate to reach a final answer. Dataset statistics and construction details are provided in Appendix [A.1](https://arxiv.org/html/2605.25421v1#A1.SS1 "A.1 Training Data Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol").

### 3.2 Implementation Details

We use Llama-3.2-1B-Instruct [Grattafiori et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib9 "") as the backbone for main experiments, while experiments on other backbones are provided in Appendix [B](https://arxiv.org/html/2605.25421v1#A2 "Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"). Parameter-efficient fine-tuning is applied via LoRA [Hu et al. (2022)](https://arxiv.org/html/2605.25421v1#bib.bib13 "") with rank r=128r=128 and α=32\\alpha=32, applied to all attention projection matrices. The number of latent vectors per turn is set to k=6k=6. Both stages are trained on 2-turn dialogues, with Stage 2 involving N=2N{=}2 agents. All training experiments are conducted on 8 NVIDIA H200 GPUs. For evaluation, each task is run independently on a single H200 GPU. More details can be found in Appendix [A.3](https://arxiv.org/html/2605.25421v1#A1.SS3 "A.3 Implementation Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol").

| | | | | | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | In-Domain | Out-of-Domain | InferenceEfficiency |
| Commonsense | StrategyQA | SocialIQA | WorldTree | PubMedQA | MedQA | ARC-E | ARC-C |
| Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | \# token | time |
| Training-Free Single-Agent Baseline | | | | | | | | | |
| Single-Agent | 43.67 | 43.67 | 52.00 | 52.00 | 56.00 | 56.00 | 59.33 | 59.33 | 55.67 | 55.67 | 38.33 | 38.33 | 30.67 | 30.67 | 34.00 | 34.00 | 113.59 | 1.25 |
| Training-Free Text-Based Communication Methods | | | | | | | | | |
| NL | 49.56 | 53.33 | 54.44 | 54.67 | 58.22 | 61.00 | 69.33 | 73.00 | 54.56 | 59.00 | 42.67 | 42.67 | 35.33 | 37.67 | 31.78 | 32.00 | 1247.50 | 13.15 |
| AutoForm | 47.78 | 50.33 | 54.56 | 55.00 | 59.89 | 63.00 | 67.11 | 68.67 | 56.11 | 57.00 | 44.11 | 46.00 | 35.89 | 35.33 | 33.56 | 34.00 | 1717.60 | 18.18 |
| EcoLang | 48.00 | 50.67 | 49.44 | 50.33 | 55.78 | 61.33 | 68.11 | 71.33 | 54.67 | 57.33 | 41.89 | 42.67 | 37.33 | 36.67 | 34.89 | 36.00 | 960.26 | 10.04 |
| SDE | 47.22 | 49.00 | 52.67 | 52.67 | 58.11 | 60.67 | 64.56 | 68.00 | 49.67 | 53.00 | 40.78 | 41.67 | 34.78 | 36.67 | 32.89 | 32.33 | 1316.20 | 14.48 |
| Training-Free Latent-Space Communication Methods | | | | | | | | | |
| Cipher | 50.22 | 52.00 | 52.78 | 54.67 | 57.89 | 60.33 | 69.22 | 71.33 | 55.44 | 57.67 | 42.56 | 43.33 | 35.67 | 36.00 | 34.56 | 35.33 | 1137.89 | 11.58 |
| LatentMAS-V | 26.11 | 26.00 | 49.67 | 50.00 | 42.78 | 43.00 | 45.00 | 46.33 | 54.22 | 55.00 | 32.67 | 33.00 | 27.67 | 27.89 | 27.00 | 28.33 | 324.43 | 3.61 |
| Training-Based Communication Methods | | | | | | | | | |
| TextFullT | 64.44 | 66.33 | 64.11 | 65.00 | 76.66 | 77.63 | 70.56 | 73.33 | 69.67 | 71.00 | 44.55 | 44.67 | 42.33 | 42.67 | 34.89 | 34.67 | 505.03 | 5.47 |
| LatentFullT | 56.00 | 56.33 | 63.11 | 63.33 | 80.78 | 80.67 | 68.56 | 68.33 | 66.11 | 66.67 | 42.11 | 42.33 | 38.89 | 38.67 | 33.78 | 34.00 | 57.00 | 0.70 |
| HyLaT | 63.78 | 64.33 | 64.67 | 65.33 | 82.56 | 83.00 | 69.22 | 69.00 | 67.44 | 67.33 | 42.11 | 42.33 | 39.00 | 39.33 | 33.89 | 34.00 | 72.01 | 1.47 |

Table 1: Experimental results of different methods. We report average accuracy (Avg.) and majority-vote
accuracy (Maj.) across agents, along with communication
efficiency measured by average token count (# token)
and wall-clock time (time, in seconds).
Bold denotes the best result and underline
denotes the second best.

### 3.3 Evaluation

#### Tasks

Following [Du et al. (2023)](https://arxiv.org/html/2605.25421v1#bib.bib5 ""), we adopt multi-agent debate (MAD) as the primary task for evaluation. We report results on both in-domain datasets encountered during training, i.e., CommonsenseQA, StrategyQA,
SocialIQA, WorldTree, and PubMedQA, as well as several out-of-domain datasets, specifically MedQA [Jin et al. (2021)](https://arxiv.org/html/2605.25421v1#bib.bib15 ""), ARC-Easy and ARC-Challenge [Clark et al. (2018)](https://arxiv.org/html/2605.25421v1#bib.bib3 ""). We follow  [Tang et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib32 "")
to use the first 300 questions of each dataset to build MAD tasks. We conduct evaluations on these tasks with 3 agents communicating over 2 turns.

#### Metrics

We assess both task performance and communication efficiency.
For performance, we report the average per-agent accuracy (Avg.) across all agents and the majority-vote accuracy (Maj.) aggregated over all agents. For efficiency, we report the average number of tokens generated per question across all
communication rounds (# token), and the average running time per question.

### 3.4 Compared Methods

We compare HyLaT against various methods designed to optimize communication between agents. The “Single-Agent” baseline serves as a lower bound with no inter-agent communication.
Multi-agent baselines are further categorized into: (1) text-based methods, including:

- •


NL uses unoptimised Natural-Language messages as the communication channel;

- •


AutoForm[Chen et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib1 "") directly prompts agents to communicate in structured language, such as JSON and code;

- •


EcoLang[Mou et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib21 "") evolves efficient communication rules via a selection procedure and prepends them to agent instructions;

- •


SDE[Tang et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib32 ""), where agents transmit textual tokens alongside the model’s internal
state-difference trajectory recorded in generation;


and (2) latent-space methods, including:

- •


Cipher[Pham et al. (2023)](https://arxiv.org/html/2605.25421v1#bib.bib24 "") replaces textual messages with semantic embedding vectors, computed as the belief-weighted average over the output vocabulary distribution.

- •


LatentMAS-V222Since the original LatentMAS does not distinguish between dialogue roles and does not support multi-round multi-agent communication, we adapt its implementation to the multi-round
setting. This modification may not reflect its intended use and could underestimate its performance.[Zou et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib39 "")
has each agent autoregressively generate hidden-state vectors
from the final layer and pass its full key–value cache as a latent memory to the next agent.


Since the aforementioned methods do not involve additional training, we introduce additional baselines, TextFullT and LatentFullT, to ensure a fair comparison. TextFullT is trained on the same data as HyLaT but restricts all communication, including elaborations and conclusions to a single textual channel. LatentFullT is trained on the same data as HyLaT, but intermediate rounds communicate purely through latent vectors, while only the final round retains a latent vector and a text output for supervision and evaluation.

## 4 Experimental Results

| Method | Avg. | Maj. | \# token | time | format err.(%) |
| TextFullT | 58.40 | 59.41 | 505.03 | 5.47 | 0.00 |
| LatentFullT | 56.17 | 56.29 | 57.00 | 0.70 | 0.00 |
| Ours | 57.83 | 58.08 | 72.01 | 1.47 | 0.00 |
| Variants based on Single-Channel Communication |
| w/ pure text | 56.93 | 57.00 | 639.18 | 13.18 | 3.28 |
| w/ pure latent | 50.28 | 50.33 | 56.09 | 1.16 | 6.12 |
| Variants with Single-Stage Training |
| w/o Stage 1 | 38.43 | 38.58 | 102.59 | 1.38 | 9.13 |
| w/o Stage 2 | 43.64 | 43.96 | 136.10 | 2.87 | 22.27 |

Table 2: Ablation study of the HyLaT framework. Reported results are averaged over all datasets.

### 4.1 Main Results

Table [1](https://arxiv.org/html/2605.25421v1#S3.T1 "Table 1 ‣ 3.2 Implementation Details ‣ 3 Experimental Setup ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") reports the overall performance of various methods, with several key findings highlighted:

#### I. Training-free methods fail to balance efficiency and performance.

Among training-free approaches: (1) The single-agent baseline achieves the highest efficiency but suffers from poor performance. (2) Text-based multi-agent methods yield strong results, yet offer limited room for efficiency optimization–even the most efficient one, EcoLang, requires 9×9\\times the duration of the single-agent baseline. (3) Latent-space methods are generally more efficient, particularly LatentMAS-V, but at the cost of a severe performance drop. These observations suggest that in a zero-shot setting, the fixed backbone model significantly constrains agent behavior, highlighting the necessity of additional training to co-optimize efficiency and performance.

#### II. HyLaT strikes a balance between efficiency and performance.

(1) Unparalleled efficiency. HyLaT operates at execution times close to the single-agent baseline while using only half the tokens. Specifically, HyLaT improves token and time efficiency by 10.6×\\times/6.8×\\times and 3.6×\\times/2.5×\\times over the most efficient text-based and latent-space baselines, respectively. (2) Task performance. Unlike LatentMAS-V, HyLaT preserves strong task performance, achieving top-2 or comparative performance on both in-domain and out-of-domain datasets. Notably, on SocialIQA, HyLaT clearly outperforms all baselines by utilizing the latent channel to supplement information that text alone cannot fully convey. (3) Advantage over TextFullT and LatentFullT. Although HyLaT slightly trails TextFullT on tasks requiring exhaustive structured reasoning, such as WorldTree and ARC-E, its overall performance is highly comparable, while incurring substantially lower time and token costs. Meanwhile, LatentFullT only slightly improves computational efficiency, but its performance is inferior to that of HyLaT, suggesting that the intermediate text channel serves as a semantic anchor that maintains contextual coherence across rounds.
In summary, HyLaT effectively enhances multi-agent communication efficiency, maintaining task capabilities of other multi-agent frameworks while operating at or below single-agent costs.

### 4.2 Ablation Study

Furthermore, we compare several variants of HyLaT in Table [2](https://arxiv.org/html/2605.25421v1#S4.T2 "Table 2 ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") to validate the effectiveness of the proposed dual-channel communication framework.

#### Effect of the Hybrid Channel Design

We first ablate the channel composition by comparing two degenerate variants: (1) w/ pure text uses our trained model, rather than TextFullT, to generate natural language throughout all rounds, resulting in significantly higher token usage and inference time, while yielding only marginal accuracy gains. This confirms that the latent channel is the primary driver of HyLaT’s efficiency advantage. (2) w/ pure latent restricts intermediate rounds to latent-only outputs, reserving hybrid generation for the final round only. Despite achieving the lowest token count, this variant suffers a notable drop in accuracy and a higher format error rate, suggesting that
textual signals are crucial for agents to maintain coherent comprehension across multiple turns.
In summary, the advantages of the two channels are clearly complementary. Thus, the dual-channel design of HyLaT represents the optimal choice for balancing efficiency and performance.

#### Effect of Two-stage Training

The variant w/o Stage 1 skips the single-agent warm-up and directly trains multi-agent interaction from scratch. Without first learning to generate stable hybrid outputs at the individual level, the latent representations produced early in training are noisy and unstable, and these errors propagate across rounds and agents, making optimization substantially more difficult and leading to negative results.
The variant w/o Stage 2 applies the Stage 1 checkpoint directly to multi-agent communication without co-learning. Since the model has never been exposed to peers’ hybrid outputs during training, it frequently fails to process latent vectors from other agents at test time, resulting in a high format error rate (22.27%) and a substantial drop in task performance. This confirms that Stage 2 co-learning is essential for enabling robust multi-round hybrid communication.

### 4.3 Compatibility and Robustness of the Hybrid Protocol

#### Communication Protocol Compatibility

A practical advantage of HyLaT’s hybrid design is that the preserved text channel allows it to interoperate with agents using other communication protocols. To verify this, we construct heterogeneous multi-agent groups mixing HyLaT- and NL-based agents in varying proportions and evaluate task performance and token usage. As shown in Figure [3](https://arxiv.org/html/2605.25421v1#S4.F3 "Figure 3 ‣ Robustness to Latent Perturbation ‣ 4.3 Compatibility and Robustness of the Hybrid Protocol ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(a), increasing the proportion of HyLaT agents consistently reduces token consumption while improving task performance, indicating that HyLaT agents can effectively communicate with NL agents through the shared text channel and guide the group toward more efficient and accurate outcomes. This compatibility is unavailable to pure latent communication methods, whose opaque signals cannot be interpreted by agents operating in natural language.

#### Robustness to Latent Perturbation

Figure 3: (a) Task performance and communication cost under heterogeneous agent settings; (b) Majority voting accuracy of HyLaT under increasing Gaussian noise applied to latent vectors at inference time.

To assess the stability, we inject Gaussian noise of varying magnitude into each latent vector at inference time. As shown in Figure [3](https://arxiv.org/html/2605.25421v1#S4.F3 "Figure 3 ‣ Robustness to Latent Perturbation ‣ 4.3 Compatibility and Robustness of the Hybrid Protocol ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(b), HyLaT maintains stable performance for σ≤0.5\\sigma\\leq 0.5. This robustness stems from the hybrid channel design: while the latent channel carries intermediate reasoning, critical information such as the final answer is expressed through the text channel, where discrete tokens are more resilient to noise than continuous vectors, safeguarding the output from total degradation.

#### Heterogeneous Agent Communication

HyLaT can be naturally extended to heterogeneous multi-agent settings with minimal architectural modification. During Stage 2 training, a lightweight MLP adapter is introduced for each agent to project received latent representations into its own semantic space prior to fusion, thereby bridging the representational gap between agents from different model families. To validate this, we construct a heterogeneous variant of HyLaT pairing Llama-3.2-1B-Instruct and Qwen2-1.5B-Instruct as communicating agents. We evaluate this variant on the MAD task under a 2-agent, 2-round setting. As shown in Figure [8](https://arxiv.org/html/2605.25421v1#A2.F8 "Figure 8 ‣ B.1 Heterogeneous Agent Communication ‣ Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(a), the results demonstrate that HyLaT successfully enables effective communication between agents from different model families, confirming the generality of our hybrid latent-text communication framework.

### 4.4 Scalability and Generalization Analysis

This section demonstrates that HyLaT can scale to more complex agent interactions and generalizes to other task scenarios, such as social simulation.

#### Scalability of Agent Count and Interaction Rounds

Figure 4: We vary the number of agents (N) while fixing the number of communication rounds to T=2 (left), and vary the number of rounds (T) while fixing N=2 (right).

As shown in Figure [4](https://arxiv.org/html/2605.25421v1#S4.F4 "Figure 4 ‣ Scalability of Agent Count and Interaction Rounds ‣ 4.4 Scalability and Generalization Analysis ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), HyLaT’s token usage remains relatively stable as both NN and TT increase, while NL incurs rapidly growing overhead and TextFullT shows moderate growth.
On accuracy, increasing NN or TT does not consistently lead to performance gains across all three methods, suggesting that effective coordination in more complex interactions generally remains challenging for 1B-scale models. For HyLaT, the degradation is also partially attributed to the gap between training and evaluation configuration: as the model is optimized for a small-scale setup where N=2N=2, T=2T=2, yet evaluated under larger-scale conditions. To verify this hypothesis, we constructed 3,400 training samples with 4-agent interactions and retrained Stage 2 of HyLaT. Figure [8](https://arxiv.org/html/2605.25421v1#A2.F8 "Figure 8 ‣ B.1 Heterogeneous Agent Communication ‣ Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(b) shows that the retrained model (HyLaT-scaled) notably alleviates the performance degradation. All these results demonstrate that the efficiency advantage of HyLaT becomes increasingly pronounced as interactions scale, and that HyLaT can generalize to larger multi-agent settings, which can be further enhanced with correspondingly scaled training data.

#### Generalization to Social Simulation

| Method | Trust |
| --- | --- |
| Avg. Sent | Avg. Returned | \# token | time |
| --- | --- | --- | --- |
| NL | 3.82 | 5.10 | 2134.13 | 22.36 |
| Autoform | 4.56 | 7.75 | 4963.44 | 55.34 |
| Ecolang | 4.05 | 7.13 | 776.81 | 8.43 |
| SDE | 3.66 | 6.60 | 1717.69 | 18.82 |
| TextFullT | 3.22 | 9.04 | 797.94 | 8.45 |
| HyLaT | 3.53 | 10.84 | 182.00 | 3.49 |
| Human\* | 7.48 | 12.24 | - | - |

Table 3: Results on repeated trust game for human trust behavior simulation. Avg. Sent and Avg. Returned represents the average amount sent by the trustors and that returned by the trustees. Human\*: estimated from figures in  [Cochard et al. (2004)](https://arxiv.org/html/2605.25421v1#bib.bib4 ""); [Xie et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib35 "")

To further explore the applicability of HyLaT to multi-agent social simulation, we conduct the repeated trust game
from [Xie et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib35 ""), in which a trustor and a trustee interact over 7 rounds: the trustor decides how much to send each round, and the trustee decides how much to return. As shown in Table [3](https://arxiv.org/html/2605.25421v1#S4.T3 "Table 3 ‣ Generalization to Social Simulation ‣ 4.4 Scalability and Generalization Analysis ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), both HyLaT and TextFullT achieve substantially higher returned amounts than other methods. We attribute this to training on social reasoning data, which likely improves agents’ ability to understand and respond to others’ intentions. HyLaT additionally achieves this with far lower communication cost, suggesting that hybrid communication can preserve the social reasoning capability acquired while substantially reducing overhead.

Figure 5: Top attended words at various generation steps during multi-agent communication. Tokens are color-coded by source: black (instructions and questions), gray (templates), green/blue (agent’s own latent/text), and orange/red (other agents’ latent/text).

### 4.5 Interpretability Analysis

#### Cross-Agent Attention Analysis

To understand how agents utilize information from both channels during communication, we analyze the learned attention in Figure [5](https://arxiv.org/html/2605.25421v1#S4.F5 "Figure 5 ‣ Generalization to Social Simulation ‣ 4.4 Scalability and Generalization Analysis ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"). In Round 1, latent generation primarily attends to keywords from the question and task instructions, while text generation shifts attention toward the agent’s own latent tokens. In Round 2, a more striking pattern emerges: latent generation is dominated by the other agent’s latent tokens from the previous round, providing direct evidence that cross-agent information change occurs through these continuous representations. When generating the critical textual output, the agent attends to a mixture of the other agent’s textual response and its own latent tokens, indicating that the final decision integrates both explicitly communicated content and implicitly encoded details.
Nevertheless, attention patterns alone do not represent causal explanations, and we will explore more rigorous interpretability analysis in future work.

#### Probing the Latent Tokens

To examine whether latent tokens encode meaningful information, we visualize the final-step latent embeddings across five datasets using PCA. As shown in Figure [9](https://arxiv.org/html/2605.25421v1#A2.F9 "Figure 9 ‣ B.3 Probing the Latent Tokens ‣ Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), the latent representations exhibit clear domain-level clustering despite the model never receiving explicit domain labels, demonstrating that the latent channel organizes information by semantic content rather than surface form. The first two principal components account for 70.5% of the total variance, indicating that the latent space organizes around a small number of dominant semantic directions rather than distributing information uniformly. These observations suggest that latent tokens are not merely auxiliary padding: they actively encode task-specific semantics in a geometrically organized space, providing the downstream text decoder with structured, domain-relevant context.

## 5 Related Work

### 5.1 LLM-based Multi-agent Systems

LLM-based multi-agent systems (MAS) have demonstrated strong performance across various scenarios [Guo et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib10 ""); [Mou et al. (2024a)](https://arxiv.org/html/2605.25421v1#bib.bib20 ""). Representative applications include debate [Du et al. (2023)](https://arxiv.org/html/2605.25421v1#bib.bib5 ""); [Tang et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib32 ""), software development [Qian et al. (2024a)](https://arxiv.org/html/2605.25421v1#bib.bib25 ""), and social simulation [Mou et al. (2024b)](https://arxiv.org/html/2605.25421v1#bib.bib22 ""). In these settings, agents communicate via natural language, structured messages, or shared memory to exchange information and coordinate actions. However, as the number of agents and interaction rounds increases, the rapidly growing communication overhead poses efficiency challenges [Qian et al. (2024b)](https://arxiv.org/html/2605.25421v1#bib.bib26 ""); [Chen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib2 "").

### 5.2 Multi-agent Communication

To optimize the communication efficiency, early work on emergent communication [Lazaridou and Baroni (2020)](https://arxiv.org/html/2605.25421v1#bib.bib17 "") showed that agents can develop their own compact protocols to solve cooperative tasks. With the rise of LLMs, recent studies have investigated how to optimize communication for both efficiency and performance. Some works [Chen et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib1 ""); [Mou et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib21 ""); [Chen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib2 "") explore ways to compress or simplify message content while maintaining task effectiveness. Other works prune message-passing graph [Zhang et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib37 "") or reorganize protocols [Marro et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib18 "") to reduce redundancy. Despite these advances, most approaches are limited to either structured text or learned symbolic languages, which constrains the density of information that can be exchanged.

### 5.3 Latent Reasoning and Communication

Recent work has explored latent representations as an alternative medium for reasoning in LLMs [Hao et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib11 ""); [Shen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib29 ""); [Wei et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib33 ""), improving efficiency compared to explicit chain-of-thought approaches. While this line of research mainly focuses on single-turn reasoning, it has recently been extended to multi-agent collaboration. These methods typically enable semantic transfer across models by sharing hidden states or projecting KV-cache representations [Pham et al. (2023)](https://arxiv.org/html/2605.25421v1#bib.bib24 ""); [Fu et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib7 ""); [Zou et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib39 ""); [Du et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib6 ""). Despite these advances, existing approaches generally rely solely on latent communication, which reduces interpretability and controllability. Moreover, their thought-transfer mechanisms are often designed for sequential workflows and do not support multi-turn interactions, which are more common in general communication scenarios.

## 6 Conclusion

In this paper, we present HyLaT, a hybrid latent-text communication protocol that transfers elaborate cognitive signals through a latent channel and concise critical signals through a text channel. A two-stage training framework is proposed to enable agents to participate
in effective multi-round hybrid communication. Experiments show that HyLaT dramatically improves communication efficiency while maintaining competitive task performance.

## Limitations

While HyLaT demonstrates promising results, several
limitations remain. We discuss them below and
outline directions for future work.

- •


Model scale. Due to computational
constraints, all experiments are conducted on relatively small models (1B and 3B parameters). Whether HyLaT’s benefits extend to larger-scale models remains to be verified.

- •


Deployment scale. HyLaT’s modified generation procedure is currently incompatible with inference frameworks such as vLLM, precluding evaluation in large-scale or long-horizon multi-agent scenarios, where communication efficiency becomes more important.

- •


Text channel diversity. The expressive diversity of the text channel is constrained by the scarcity of high-quality multi-agent communication data and human communication data. Currently, our training set mainly includes QA-style debating data, and following [Shen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib29 ""), we append a fixed answer prompt to align generation, both of which limit the range of communicative behaviors the text channel can express. Exploring richer and more diverse communication scenarios is an important direction for future work.

- •


Latent interpretability. While HyLaT improves upon pure latent communication by preserving observable intermediate text outputs, the latent channel itself remains opaque. Decoding the semantic content of latent vectors is still highly challenging, and how to balance latent decodability with communication performance is a non-trivial open problem that we leave for future work.


## References

- Chen et al. (2024)
Weize Chen, Chenfei Yuan, Jiarui Yuan, Yusheng Su, Chen Qian, Cheng Yang, Ruobing Xie, Zhiyuan Liu, and Maosong Sun. 2024.

Beyond natural language: Llms leveraging alternative formats for enhanced reasoning and communication.

In _Findings of the Association for Computational Linguistics: EMNLP 2024_, pages 10626–10641.

- Chen et al. (2025)
Weize Chen, Jiarui Yuan, Chen Qian, Cheng Yang, Zhiyuan Liu, and Maosong Sun. 2025.

Optima: Optimizing effectiveness and efficiency for llm-based multi-agent system.

In _Findings of the Association for Computational Linguistics: ACL 2025_, pages 11534–11557.

- Clark et al. (2018)
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. 2018.

Think you have solved question answering? try arc, the ai2 reasoning challenge.

_arXiv preprint arXiv:1803.05457_.

- Cochard et al. (2004)
Francois Cochard, Phu Nguyen Van, and Marc Willinger. 2004.

Trusting behavior in a repeated investment game.

_Journal of Economic Behavior & Organization_, 55(1):31–44.

- Du et al. (2023)
Yilun Du, Shuang Li, Antonio Torralba, Joshua B Tenenbaum, and Igor Mordatch. 2023.

Improving factuality and reasoning in language models through multiagent debate.

_arXiv preprint arXiv:2305.14325_.

- Du et al. (2025)
Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Yu Cheng, Bo Zheng, Wei Chen, and Haochao Ying. 2025.

Enabling agents to communicate entirely in latent space.

_arXiv preprint arXiv:2511.09149_.

- Fu et al. (2025)
Tianyu Fu, Zihan Min, Hanling Zhang, Jichao Yan, Guohao Dai, Wanli Ouyang, and Yu Wang. 2025.

Cache-to-cache: Direct semantic communication between large language models.

_arXiv preprint arXiv:2510.03215_.

- Geva et al. (2021)
Mor Geva, Daniel Khashabi, Elad Segal, Tushar Khot, Dan Roth, and Jonathan Berant. 2021.

Did aristotle use a laptop? a question answering benchmark with implicit reasoning strategies.

_Transactions of the Association for Computational Linguistics_, 9:346–361.

- Grattafiori et al. (2024)
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, and 1 others. 2024.

The llama 3 herd of models.

_arXiv preprint arXiv:2407.21783_.

- Guo et al. (2024)
Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V Chawla, Olaf Wiest, and Xiangliang Zhang. 2024.

Large language model based multi-agents: A survey of progress and challenges.

_arXiv preprint arXiv:2402.01680_.

- Hao et al. (2024)
Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, and Yuandong Tian. 2024.

Training large language models to reason in a continuous latent space.

_arXiv preprint arXiv:2412.06769_.

- Ho et al. (2020)
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. 2020.

Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps.

In _Proceedings of the 28th International Conference on Computational Linguistics_, pages 6609–6625.

- Hu et al. (2022)
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Liang Wang, Weizhu Chen, and 1 others. 2022.

Lora: Low-rank adaptation of large language models.

_Iclr_, 1(2):3.

- Jansen et al. (2018)
Peter Jansen, Elizabeth Wainwright, Steven Marmorstein, and Clayton Morrison. 2018.

Worldtree: A corpus of explanation graphs for elementary science questions supporting multi-hop inference.

In _Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)_.

- Jin et al. (2021)
Di Jin, Eileen Pan, Nassim Oufattole, Wei-Hung Weng, Hanyi Fang, and Peter Szolovits. 2021.

What disease does this patient have? a large-scale open domain question answering dataset from medical exams.

_Applied Sciences_, 11(14):6421.

- Jin et al. (2019)
Qiao Jin, Bhuwan Dhingra, Zhengping Liu, William Cohen, and Xinghua Lu. 2019.

Pubmedqa: A dataset for biomedical research question answering.

In _Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP)_, pages 2567–2577.

- Lazaridou and Baroni (2020)
Angeliki Lazaridou and Marco Baroni. 2020.

Emergent multi-agent communication in the deep learning era.

_arXiv preprint arXiv:2006.02419_.

- Marro et al. (2024)
Samuele Marro, Emanuele La Malfa, Jesse Wright, Guohao Li, Nigel Shadbolt, Michael Wooldridge, and Philip Torr. 2024.

A scalable communication protocol for networks of large language models.

_arXiv preprint arXiv:2410.11905_.

- Monge and Contractor (2003)
Peter R Monge and Noshir S Contractor. 2003.

_Theories of communication networks_.

Oxford University Press, USA.

- Mou et al. (2024a)
Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jingcong Liang, Xinnong Zhang, Libo Sun, Jiayu Lin, Jie Zhou, Xuanjing Huang, and 1 others. 2024a.

From individual to society: A survey on social simulation driven by large language model-based agents.

_arXiv preprint arXiv:2412.03563_.

- Mou et al. (2025)
Xinyi Mou, Chen Qian, Wei Liu, Xuanjing Huang, and Zhongyu Wei. 2025.

Ecolang: Efficient and effective agent communication language induction for social simulation.

_arXiv preprint arXiv:2505.06904_.

- Mou et al. (2024b)
Xinyi Mou, Zhongyu Wei, and Xuan-Jing Huang. 2024b.

Unveiling the truth and facilitating change: Towards agent-based large-scale social movement simulation.

In _Findings of the Association for Computational Linguistics: ACL 2024_, pages 4789–4809.

- Park et al. (2023)
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein. 2023.

Generative agents: Interactive simulacra of human behavior.

In _Proceedings of the 36th annual acm symposium on user interface software and technology_, pages 1–22.

- Pham et al. (2023)
Chau Pham, Boyi Liu, Yingxiang Yang, Zhengyu Chen, Tianyi Liu, Jianbo Yuan, Bryan A Plummer, Zhaoran Wang, and Hongxia Yang. 2023.

Let models speak ciphers: Multiagent debate through embeddings.

_arXiv preprint arXiv:2310.06272_.

- Qian et al. (2024a)
Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, and 1 others. 2024a.

Chatdev: Communicative agents for software development.

In _Proceedings of the 62nd annual meeting of the association for computational linguistics (volume 1: Long papers)_, pages 15174–15186.

- Qian et al. (2024b)
Chen Qian, Zihao Xie, Yifei Wang, Wei Liu, Kunlun Zhu, Hanchen Xia, Yufan Dang, Zhuoyun Du, Weize Chen, Cheng Yang, and 1 others. 2024b.

Scaling large language model-based multi-agent collaboration.

_arXiv preprint arXiv:2406.07155_.

- Sap et al. (2019)
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan Le Bras, and Yejin Choi. 2019.

Social iqa: Commonsense reasoning about social interactions.

In _Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP)_, pages 4463–4473.

- Shannon (1948)
Claude Elwood Shannon. 1948.

A mathematical theory of communication.

_The Bell system technical journal_, 27(3):379–423.

- Shen et al. (2025)
Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. 2025.

Codi: Compressing chain-of-thought into continuous space via self-distillation.

In _Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing_, pages 677–693.

- Singh et al. (2025)
Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, and 1 others. 2025.

Openai gpt-5 system card.

_arXiv preprint arXiv:2601.03267_.

- Talmor et al. (2019)
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. 2019.

Commonsenseqa: A question answering challenge targeting commonsense knowledge.

In _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)_, pages 4149–4158.

- Tang et al. (2025)
Yichen Tang, Weihang Su, Yujia Zhou, Yiqun Liu, Min Zhang, Shaoping Ma, and Qingyao Ai. 2025.

Augmenting multi-agent communication with state delta trajectory.

In _Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing_, pages 10230–10251.

- Wei et al. (2025)
Xilin Wei, Xiaoran Liu, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Jiaqi Wang, Xipeng Qiu, and Dahua Lin. 2025.

Sim-cot: Supervised implicit chain-of-thought.

_arXiv preprint arXiv:2509.20317_.

- Wu et al. (2025)
Shiguang Wu, Yaqing Wang, and Quanming Yao. 2025.

Dense communication between language models.

_arXiv preprint arXiv:2505.12741_.

- Xie et al. (2024)
Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye, Shiyang Lai, Kai Shu, Jindong Gu, Adel Bibi, Ziniu Hu, David Jurgens, and 1 others. 2024.

Can large language model agents simulate human trust behavior?

_arXiv preprint arXiv:2402.04559_.

- Yang et al. (2018)
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D Manning. 2018.

Hotpotqa: A dataset for diverse, explainable multi-hop question answering.

In _Proceedings of the 2018 conference on empirical methods in natural language processing_, pages 2369–2380.

- Zhang et al. (2024)
Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, Guancheng Wan, Kun Wang, Dawei Cheng, Jeffrey Xu Yu, and Tianlong Chen. 2024.

Cut the crap: An economical communication pipeline for llm-based multi-agent systems.

_arXiv preprint arXiv:2410.02506_.

- Zhang et al. (2025)
Xinnong Zhang, Jiayu Lin, Xinyi Mou, Shiyue Yang, Xiawei Liu, Libo Sun, Hanjia Lyu, Yihang Yang, Weihong Qi, Yue Chen, and 1 others. 2025.

Socioverse: A world model for social simulation powered by llm agents and a pool of 10 million real-world users.

_arXiv preprint arXiv:2504.10157_.

- Zou et al. (2025)
Jiaru Zou, Xiyuan Yang, Ruizhong Qiu, Gaotang Li, Katherine Tieu, Pan Lu, Ke Shen, Hanghang Tong, Yejin Choi, Jingrui He, and 1 others. 2025.

Latent collaboration in multi-agent systems.

_arXiv preprint arXiv:2511.20639_.


## Appendix A Supplemented Implementation Details

### A.1 Training Data Details

#### Datasets of Stage 1

To support hybrid communication, Stage 1 training requires data that naturally exhibits the two-part structure of HyLaT’s output: an elaborate cognitive signal encoding dense intermediate reasoning and a concise signal expressing the final response. Rather than constructing such data from scratch, we sample from training sets of existing datasets that already contain detailed reasoning processes alongside short final answers, treating the reasoning or explanation as the target for the latent channel and the concise answer as the supervision target for the text channel. Based on this, multiple QA pairs can be concatenated to form multi-turn dialogues. Dataset statistics are summarized in Table [4](https://arxiv.org/html/2605.25421v1#A1.T4 "Table 4 ‣ Datasets of Stage 2 ‣ A.1 Training Data Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol").

#### Datasets of Stage 2

To support multi-round multi-agent communication, we construct training data through multi-agent debate simulation along two complementary axes. (1) _Refinement_: In this setting, agents
independently answer the same question in parallel and iteratively refine their responses through discussion. To ensure that inter-agent communication provides meaningful information gain, we deliberately avoid using a strong model for all rounds, as it tends to produce correct answers in the first round, leaving little room for correction through
communication. Instead, we adopt a _weak-strong pairing strategy_: the first round is generated by Llama-3.2-1B and the second round by GPT-5, and dialogues in which the second round answer remains incorrect are discarded. We randomly sample questions from the Stage 1 datasets and retain 3,960 valid
dialogues; (2) _Decomposition_: In this setting, agents collaboratively solve a complex question by first addressing complementary sub-problems in parallel, then synthesizing their findings to produce a final answer in the second round. We sample 2,000 structurally parallel questions from HotpotQA [Yang et al. (2018)](https://arxiv.org/html/2605.25421v1#bib.bib36 ""), 2WikiMultihopQA [Ho et al. (2020)](https://arxiv.org/html/2605.25421v1#bib.bib12 ""), and GSM8K-AUG-NL [Shen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib29 ""), respectively. The prompts for data generation are provided in Figure [6](https://arxiv.org/html/2605.25421v1#A1.F6 "Figure 6 ‣ Datasets of Stage 2 ‣ A.1 Training Data Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol").

| Dataset | Type | \# samples |
| --- | --- | --- |
| CommonsenseQA [Talmor et al. (2019)](https://arxiv.org/html/2605.25421v1#bib.bib31 "") | commonsense reasoning | 3,600 |
| StrategyQA [Geva et al. (2021)](https://arxiv.org/html/2605.25421v1#bib.bib8 "") | commonsense reasoning | 1,800 |
| SocialIQA [Sap et al. (2019)](https://arxiv.org/html/2605.25421v1#bib.bib27 "") | social reasoning | 1,800 |
| WorldTree [Jansen et al. (2018)](https://arxiv.org/html/2605.25421v1#bib.bib14 "") | scientific question answering | 2,204 |
| PubMedQA [Jin et al. (2019)](https://arxiv.org/html/2605.25421v1#bib.bib16 "") | medical question answering | 500 |

Table 4: Statistics of training datasets in Stage 1.

Round 1: Initial PromptPlease answer the following question: {question}

First explain your reasoning, and provide your final answer in the form \\boxed{answer},
at the end of your response.

Round t>1t>1: Multi-Agent Interaction PromptThese are the solutions from other agents:

One agent’s response: \`\`\`{agent\_response}\`\`\`\[repeated for each other agent\]

Using the responses from other agents as additional information, can you provide your answer to the question?
The original question is {question}.

Your final answer should be in the form
\\boxed{answer}, at the end
of your response.

Figure 6: Prompts used for multi-agent interaction data construction.
Round 1 elicits an initial response with explicit reasoning.
In subsequent rounds, each agent receives the responses of all other agents and is asked to produce a revised answer.

| | | | | | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | In-Domain | Out-of-Domain | InferenceEfficiency |
| Commonsense | StrategyQA | SocialIQA | WorldTree | PubMedQA | MedQA | ARC-E | ARC-C |
| Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | \# token | time |
| Training-Free Single-Agent Baseline |
| Single-Agent | 73.67 | 73.67 | 66.00 | 66.00 | 74.00 | 74.00 | 89.00 | 89.00 | 71.00 | 71.00 | 62.00 | 62.00 | 42.67 | 42.67 | 45.67 | 45.67 | 130.65 | 2.46 |
| Training-Free Text-Based Communication Methods |
| NL | 72.33 | 76.00 | 66.56 | 67.67 | 74.89 | 76.33 | 89.78 | 90.33 | 69.00 | 69.00 | 60.44 | 62.00 | 44.00 | 44.67 | 44.89 | 46.00 | 1094.83 | 19.13 |
| AutoForm | 68.11 | 69.00 | 70.33 | 72.67 | 75.56 | 76.00 | 88.78 | 90.00 | 69.56 | 69.33 | 65.00 | 68.00 | 42.56 | 43.00 | 44.22 | 44.33 | 1668.19 | 29.09 |
| EcoLang | 72.33 | 74.33 | 68.44 | 68.00 | 74.44 | 73.33 | 87.89 | 88.33 | 69.22 | 69.33 | 61.11 | 61.33 | 43.00 | 43.67 | 42.78 | 42.00 | 603.64 | 10.43 |
| SDE | 72.56 | 74.00 | 64.89 | 65.33 | 72.89 | 74.67 | 86.56 | 88.67 | 69.00 | 69.00 | 58.67 | 62.67 | 42.56 | 43.67 | 43.67 | 44.67 | 913.33 | 16.35 |
| Training-Free Latent-Space Communication Methods |
| Cipher | 71.67 | 73.67 | 66.89 | 69.33 | 74.89 | 75.00 | 86.56 | 87.00 | 67.89 | 69.33 | 59.56 | 60.33 | 44.11 | 44.33 | 46.11 | 48.00 | 1080.19 | 18.40 |
| LatentMAS-V | 70.78 | 72.17 | 59.67 | 61.67 | 73.00 | 74.33 | 84.56 | 84.67 | 62.44 | 64.00 | 60.11 | 61.67 | 41.78 | 41.33 | 42.89 | 44.33 | 570.63 | 10.58 |
| Training-Based Communication Methods |
| TextFullT | 72.22 | 72.67 | 77.22 | 78.67 | 84.78 | 84.33 | 87.67 | 89.33 | 74.00 | 75.33 | 60.44 | 62.00 | 43.22 | 43.33 | 44.89 | 46.00 | 748.74 | 12.79 |
| LatentFullT | 78.67 | 78.33 | 81.22 | 81.00 | 89.22 | 89.67 | 84.67 | 84.67 | 73.56 | 73.33 | 59.44 | 59.00 | 43.67 | 43.67 | 43.33 | 43.33 | 57.00 | 1.21 |
| HyLaT | 78.67 | 78.33 | 85.00 | 85.00 | 90.11 | 90.00 | 86.89 | 86.33 | 73.89 | 74.00 | 59.44 | 59.33 | 44.00 | 44.00 | 43.44 | 43.67 | 72.00 | 2.46 |

Table 5: Experimental results of different methods on Llama-3.2-3B-Instruct. We report average accuracy (Avg.) and majority-vote accuracy (Maj.) across agents, along with communication efficiency measured by average token count (# token) and wall-clock time (time, in seconds). Bold denotes the best result and underline denotes the second best.

| | | | | | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | In-Domain | Out-of-Domain | InferenceEfficiency |
| Commonsense | StrategyQA | SocialIQA | WorldTree | PubMedQA | MedQA | ARC-E | ARC-C |
| Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | Avg. | Maj. | \# token | time |
| Training-Free Single-Agent Baseline |
| Single-Agent | 58.00 | 58.00 | 50.67 | 50.67 | 68.67 | 68.67 | 72.00 | 72.00 | 61.33 | 61.33 | 39.00 | 39.00 | 38.00 | 38.00 | 35.00 | 35.00 | 87.11 | 1.65 |
| Training-Free Text-Based Communication Methods |
| NL | 59.33 | 60.67 | 50.33 | 50.00 | 67.22 | 69.00 | 74.33 | 77.00 | 58.11 | 58.00 | 37.78 | 38.33 | 37.67 | 38.33 | 38.00 | 39.67 | 552.40 | 10.38 |
| AutoForm | 50.78 | 55.33 | 50.22 | 50.67 | 66.56 | 68.00 | 77.89 | 79.67 | 56.78 | 57.33 | 35.33 | 36.33 | 37.67 | 38.33 | 35.33 | 36.67 | 344.69 | 6.51 |
| EcoLang | 61.11 | 62.00 | 51.00 | 51.00 | 69.22 | 69.33 | 78.56 | 78.67 | 59.00 | 58.67 | 36.22 | 36.67 | 36.67 | 37.33 | 39.67 | 39.67 | 235.55 | 4.49 |
| SDE | 58.67 | 61.33 | 49.67 | 49.33 | 67.56 | 70.33 | 75.44 | 78.33 | 59.44 | 59.67 | 38.78 | 40.67 | 38.00 | 39.33 | 37.22 | 38.33 | 1514.63 | 10.29 |
| Training-Free Latent-Space Communication Methods |
| Cipher | 60.11 | 60.00 | 51.67 | 51.67 | 69.78 | 70.00 | 78.33 | 78.67 | 61.11 | 61.00 | 36.00 | 36.33 | 39.33 | 39.33 | 36.11 | 36.33 | 691.38 | 7.84 |
| LatentMAS-V | 4.56 | 4.00 | 0.33 | 0.00 | 13.78 | 13.00 | 10.33 | 10.00 | 21.00 | 20.33 | 13.89 | 12.33 | 4.33 | 3.67 | 4.33 | 3.00 | 587.99 | 11.86 |
| Training-Based Communication Methods |
| TextFullT | 62.56 | 62.00 | 55.11 | 55.00 | 76.11 | 76.00 | 78.33 | 78.67 | 59.11 | 60.33 | 38.67 | 39.00 | 38.56 | 40.00 | 37.67 | 39.33 | 545.30 | 10.06 |
| LatentFullT | 59.83 | 60.00 | 55.17 | 56.67 | 76.17 | 76.33 | 76.00 | 75.33 | 53.67 | 53.33 | 36.50 | 38.33 | 41.00 | 41.00 | 37.67 | 38.67 | 46.00 | 0.81 |
| HyLaT | 62.78 | 63.00 | 55.89 | 56.67 | 76.44 | 76.33 | 78.56 | 78.67 | 59.67 | 61.00 | 38.67 | 38.67 | 41.89 | 41.67 | 39.44 | 39.67 | 66.00 | 2.43 |

Table 6: Experimental results of different methods on Qwen2-1.5B-Instruct. We report average accuracy (Avg.) and majority-vote accuracy (Maj.) across agents, along with communication efficiency measured by average token count (# token) and wall-clock time (time, in seconds). Bold denotes the best result and underline denotes the second best.

### A.2 Evaluation Details

We implement all the multi-agent communication experiments using the framework provided by [Tang et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib32 ""). Following them, for datasets with more than 300 test examples, we evaluate on the first 300 samples. Evaluation tasks are constructed from the test splits of Stage 1 datasets as in-domain tasks, together with three additional out-of-domain datasets: MedQA [Jin et al. (2021)](https://arxiv.org/html/2605.25421v1#bib.bib15 ""), ARC-Easy and ARC-Challenge [Clark et al. (2018)](https://arxiv.org/html/2605.25421v1#bib.bib3 ""). Unless otherwise specified, all main experiments are conducted with N=3N=3 agents over T=2T=2 interaction rounds. During inference, we use the following generation configuration: temperature =0.2=0.2, top-kk=20=20, top-pp=0.9=0.9, with sampling enabled. The prompt templates for multi-agent debate are adapted from [Tang et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib32 "") (Figure [7](https://arxiv.org/html/2605.25421v1#A1.F7 "Figure 7 ‣ A.2 Evaluation Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")).

Initial PromptCan you answer the following question as accurately as possible?

{question}

Explain your reasoning, and write your final answer
on a new line.

{format\_instruction}

Debate PromptThese are the solutions to the problem from other
agents:{all\_other\_response}

Using the reasoning from other agents as additional
advice, can you give an updated answer? Examine your solution and that of other agents step by step.

The original question is {question}.

{format\_instruction}

Figure 7: Prompt templates used for multi-agent debate evaluation.

### A.3 Implementation Details

| Configuration | Stage 1 | Stage 2 |
| Model initialization | Llama-3.2-1B-Instruct | Stage 1 |
| LoRA | rank=128, alpha=32 | rank=128, alpha=32 |
| Global batch size | 128 | 128 |
| Peaking learning rate | 8.00e-04 | 3.00e-04 |
| Optimizer | AdamW | AdamW |
| LR scheduler | Cosine | Cosine |
| Training epochs | 3 | 3 |
| Warmup ratio | 0.03 | 0.03 |
| Precision | bfloat16 | bfloat16 |
| α\\alpha | 1 | 1 |
| β\\beta | 1 | 1 |
| γ\\gamma | 20 | 20 |

Table 7: The detailed training hyper-parameters of HyLaT.

We follow previous work [Hao et al. (2024)](https://arxiv.org/html/2605.25421v1#bib.bib11 ""); [Shen et al. (2025)](https://arxiv.org/html/2605.25421v1#bib.bib29 "") to set the number of latent vectors kk = 6, and we list the hyper-parameter settings used in Table [7](https://arxiv.org/html/2605.25421v1#A1.T7 "Table 7 ‣ A.3 Implementation Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"). For Stage 2 training, we only supervise on the last turn, considering that the intermediate conclusions can be incorrect in the refinement data.

## Appendix B Supplementary Experimental Results and Analysis

### B.1 Heterogeneous Agent Communication

Figure 8: (a) Performance of different communication methods under homogeneous and heterogeneous agent configurations; (b) Performance of HyLaT trained on original vs. scaled data as the number of agents increases.

We implemented a heterogeneous variant of HyLaT pairing Llama-3.2-1B and Qwen2-1.5B as communicating agents, with a lightweight MLP adapter bridging their respective latent spaces. We evaluated this variant on the MAD task under a 2-agent and 2-round setting. Figure [8](https://arxiv.org/html/2605.25421v1#A2.F8 "Figure 8 ‣ B.1 Heterogeneous Agent Communication ‣ Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(a) shows that although the heterogeneous setting sometimes does not surpass the best homogeneous configuration (2 × stronger model), HyLaT consistently performs well across all agent configurations.

### B.2 Further Improve the Scalability

In Figure [4](https://arxiv.org/html/2605.25421v1#S4.F4 "Figure 4 ‣ Scalability of Agent Count and Interaction Rounds ‣ 4.4 Scalability and Generalization Analysis ‣ 4 Experimental Results ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(a), we can observe that performance begins to degrade when number of agents exceeds 3. This degradation with more agents is attributed to two factors: (1) this phenomenon is a general characteristic of multi-agent systems at this model scale or for these tasks, rather than a limitation introduced by our method alone, as TextFullT exhibits the same degradation pattern when the number of agents exceeds 3. (2) the degradation in HyLaT is partly due to a gap between training and evaluation: Our current training setup uses 2-agent interaction, which does not fully cover the distribution of larger-scale agent configurations at evaluation time. To verify this hypothesis and mitigate the issue, we constructed 3,400 training samples with 4-agent interactions using the refinement method in Sec [3.1](https://arxiv.org/html/2605.25421v1#S3.SS1 "3.1 Training Data Construction ‣ 3 Experimental Setup ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"), and retrained stage 2 of HyLaT. Results in Figure [8](https://arxiv.org/html/2605.25421v1#A2.F8 "Figure 8 ‣ B.1 Heterogeneous Agent Communication ‣ Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol")(b) show that such training data notably alleviates the performance degradation, confirming that the scalability limitation stems from insufficient training coverage rather than a fundamental constraint of our method.

### B.3 Probing the Latent Tokens

Figure 9: (a) PCA analysis of final-step latent embeddings across five datasets. (b) Explained variance ratio of the top-10 principal components of the latent embeddings.

To probe the semantic content encoded in HyLaT’s latent channel, we collect 180 latent embeddings produced by agents at the final interaction round for each for the five datasets and apply PCA to project them into two dimensions. The results are visualized in Figure [9](https://arxiv.org/html/2605.25421v1#A2.F9 "Figure 9 ‣ B.3 Probing the Latent Tokens ‣ Appendix B Supplementary Experimental Results and Analysis ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol"). As shown in the figure, embeddings from the same dataset form relatively compact clusters that are well-separated from those of other datasets, suggesting that the latent vectors capture dataset-specific semantic structure rather than collapsing into an undifferentiated representation. This provides indirect evidence that the latent channel encodes meaningful content that reflects the nature of the task and communicative context, even though the vectors are never decoded into discrete tokens during inference.

### B.4 Different Model Scales

We extend the experiments on larger Llama backbones, i.e., Llama-3.2-3B-Instruct. Results in Table [5](https://arxiv.org/html/2605.25421v1#A1.T5 "Table 5 ‣ Datasets of Stage 2 ‣ A.1 Training Data Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") show that HyLaT scales effectively to this setting: task performance remains competitive across most benchmarks, and the efficiency advantage is fully preserved. The exception is WorldTree, where the 3B model already achieves strong performance under text-based communication, leaving limited room for further improvement.

### B.5 Different Model Families

We also conducted additional experiments using Qwen2-1.5B-Instruct as the backbone. Results in Table [6](https://arxiv.org/html/2605.25421v1#A1.T6 "Table 6 ‣ Datasets of Stage 2 ‣ A.1 Training Data Details ‣ Appendix A Supplemented Implementation Details ‣ HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol") show that HyLaT also demonstrates effectiveness on Qwen, matching or outperforming TextFullT across most tasks, while achieving dramatically higher communication efficiency. We also note that LatentMAS-V fails to produce meaningful results on most MAD tasks on Qwen, suggesting that adapting the original approach to multi-round multi-agent communication for different models requires non-trivial effort. Overall, the aforementioned results demonstrate that HyLaT possesses superior cross-family generalization.