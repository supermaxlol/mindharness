Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:1706.08502v3 \[cs.CL\] 20 Aug 2017

# Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog

Satwik Kottur
Affiliation: Carnegie Mellon University
José M.F. Moura
Affiliation: Carnegie Mellon University
Stefan Lee
Affiliation: Virginia Tech
Affiliation: Georgia Tech
Dhruv Batra
Affiliation: Georgia Tech
Affiliation: Facebook AI Research

###### Abstract

A number of recent works have proposed techniques for end-to-end learning of communication protocols among cooperative multi-agent populations, and have simultaneously found the _emergence of grounded human-interpretable language_ in the protocols developed by the agents, learned without any human supervision!

In this paper, using a _Task & Talk_
reference game between two agents as a testbed,
we present a sequence of ‘negative’ results
culminating in a ‘positive’ one – showing
that while most agent-invented languages are effective
( _i.e_. achieve near-perfect task rewards), they
are decidedly _not_ interpretable or compositional.
In essence, we find that natural language does not emerge ‘naturally’,
despite the semblance of ease of natural-language-emergence that one may gather from recent literature.
We discuss how it is possible to coax the invented languages to become more and more human-like and compositional by increasing restrictions on how two agents may communicate.

## 1 Introduction

One fundamental goal of artificial intelligence (AI) is the development of goal-driven dialog agents –
specifically, agents that can perceive their environment (through vision, audition, or other sensors),
and communicate with humans or other agents in natural language towards some goal.

While historically such agents have been based on _slot filling_ [Lemon et al. (2006)](https://arxiv.org/html/1706.08502v3#bib.bib13 ""),
the dominant paradigm today is neural dialog models [Bordes and Weston (2016)](https://arxiv.org/html/1706.08502v3#bib.bib1 ""); [Weston (2016)](https://arxiv.org/html/1706.08502v3#bib.bib23 ""); [Serban et al. (2016a)](https://arxiv.org/html/1706.08502v3#bib.bib19 ""); [Serban et al. (2016b)](https://arxiv.org/html/1706.08502v3#bib.bib20 "")
trained on large quantities of data.
Perhaps somewhat counterintuitively, this current paradigm
treats dialog as a static supervised learning problem, rather than as the interactive agent learning problem that it naturally is. Specifically,
a typical pipeline is to collect a large dataset of human-human dialog [Lowe et al. (2015)](https://arxiv.org/html/1706.08502v3#bib.bib15 ""); [Das et al. (2017a)](https://arxiv.org/html/1706.08502v3#bib.bib3 ""); [de Vries et al. (2017)](https://arxiv.org/html/1706.08502v3#bib.bib5 ""); [Mostafazadeh et al. (2017)](https://arxiv.org/html/1706.08502v3#bib.bib17 ""),
inject a machine in the middle of a dialog from the dataset, and supervise it to mimic the human response.
While this teaches the agent correlations between symbols,
it does not convey the functional meaning of language,
grounding (mapping words to physical concepts), compositionality (combining knowledge of simpler concepts to describe richer concepts),
or aspects of planning (understanding the goal of the conversation).

An alternative paradigm that has a long history [Winograd (1971)](https://arxiv.org/html/1706.08502v3#bib.bib25 ""); [Kirby et al. (2014)](https://arxiv.org/html/1706.08502v3#bib.bib11 "") and is witnessing a
recent resurgence [Wang et al. (2016)](https://arxiv.org/html/1706.08502v3#bib.bib22 ""); [Foerster et al. (2016)](https://arxiv.org/html/1706.08502v3#bib.bib6 ""); [Sukhbaatar et al. (2016)](https://arxiv.org/html/1706.08502v3#bib.bib21 ""); [Jorge et al. (2016)](https://arxiv.org/html/1706.08502v3#bib.bib9 ""); [Lazaridou et al. (2017)](https://arxiv.org/html/1706.08502v3#bib.bib12 ""); [Havrylov and Titov (2017)](https://arxiv.org/html/1706.08502v3#bib.bib8 ""); [Mordatch and Abbeel (2017)](https://arxiv.org/html/1706.08502v3#bib.bib16 ""); [Das et al. (2017b)](https://arxiv.org/html/1706.08502v3#bib.bib4 "") –
is situated language learning.
A number of recent works have proposed reinforcement learning techniques to learn communication protocols of agents situated in virtual environments
in a completely end-to-end manner – from perceptual input ( _e.g_. pixels) to communication (discrete symbols without any pre-specified meanings) to action
( _e.g_. signaling in reference games or navigating in an environment) –
and have simultaneously found the _emergence of grounded_
_human-interpretable (often compositional) language_
in the communication protocols developed by the agents,
without any human supervision or pretraining, simply to succeed at the task.

In this paper, we study the following question –
what are the conditions that lead to the emergence
of human-interpretable or compositional grounded language?
Our key finding is that
natural language _does not emerge ‘naturally’_
in multi-agent dialog,
despite the semblance of ease of natural-language-emergence in multi-agent games that one may gather from recent literature.

Specifically, in a sequence of ‘negative’ results culminating in a ‘positive’ one,
we find that while agents always successfully invent communication protocols and languages to achieve their goals with
near-perfect accuracies, the invented languages are decidedly _not_ compositional, interpretable, or ‘natural’; and that it is possible to coax
the invented languages to become more and more human-like and compositional
by increasing restrictions on how two agents may communicate.

Related work and novelty.
The starting point for our investigation is the recent work of [Das et al. (2017b)](https://arxiv.org/html/1706.08502v3#bib.bib4 ""),
who proposed a cooperative reference game between two agents, where communication
is necessary to accomplish the goal due to an information asymmetry.
Our key contribution over [Das et al. (2017b)](https://arxiv.org/html/1706.08502v3#bib.bib4 "") is an exhaustive study of the
conditions that must be present before compositional grounded language emerges,
and subtle but important differences in execution – tabular Q-Learning (which does not scale)
_vs_. REINFORCE (which does), and generalization to novel environments (not studied in prior work).
We hope our findings shed more light into the interpretability of
languages invented in cooperative multi-agent settings,
place recent work in appropriate context, and
inform fruitful directions for future work.

## 2 The _Task & Talk_ Game

Our testbed is a cooperative reference game ( _Task & Talk_) between two agents, Q-bot and A-bot. The game is grounded in a synthetic world of
objects comprised of three attributes
– _color_, _style_, and _shape_ – each with four possible values for a total of 4×4×4=644\\times 4\\times 4=64 objects.
Fig. [1](https://arxiv.org/html/1706.08502v3#S2.F1 "Figure 1 ‣ 2 The Task & Talk Game ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") a shows all the possible attribute values.

![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/toy_world.png)Figure 1: (a) _Task & Talk_: The testbed for our study is cooperative 2-player game, _Task & Talk_, grounded in
a synthetic world of objects with 4 _shapes_ ×\\times 4 _colors_ ×\\times 4 _styles_.
(b) Q-bot is assigned a _task_ – to inquire about the state of an ordered pair of attributes.
(c) An example gameplay between the two agents - Q-bot asks questions depending on the task which are answered by A-bot conditioned on the hidden instance visible to only itself. At the end, Q-bot makes a prediction of pair of attributes _(purple, square)_.

_Task & Talk_ plays out over multiple rounds of dialog.
At the start, A-bot is given an object unseen by Q-bot, _e.g_. _(green, dotted, square)_.
On the other side, Q-bot is assigned a task GG (unknown to A-bot) consisting of two attributes, _e.g_. _(color, style)_
and the goal is for Q-bot to discover these two attributes of the hidden object, through dialog with A-bot.

Specifically, Q-bot and A-bot exchange utterances from finite vocabularies
VQV\_{Q} and VAV\_{A} over two rounds, with Q-bot speaking first.
The game culminates in Q-bot guessing a pair of attribute values,
_e.g_. _(green, dotted)_, and both agents are rewarded identically
based on the accuracy of Q-bot ‘s prediction.

Note that the Task & Talk game setting involves an informational asymmetry between the agents – A-bot sees the object while Q-bot does not; similarly Q-bot knows the task while A-bot does not.
Thus, a two-way communication is necessary for success. Without this asymmetry, A-bot could simply convey the target attributes from the task without Q-bot having to speak. Such a setting has been widely studies in economics and game theory as the classic Lewis Signaling (LS) game [Lewis (2008)](https://arxiv.org/html/1706.08502v3#bib.bib14 ""). By necessitating _dialog_ between agents, we are able ground both VAV\_{A} and VQV\_{Q} in our final setting (Sec. [4.3](https://arxiv.org/html/1706.08502v3#S4.SS3 "4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")).

## 3 Modeling Q-bot and A-bot

![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/model_double_figure.png)Figure 2: Policy networks for Q-bot and A-bot. At each round tt of dialog,
(1) Q-bot generates a question qtq\_{t} from its speaker network conditioned on its state encoding St−1QS^{Q}\_{t-1},
(2) A-bot encodes qtq\_{t} conditioned on instance yy encoded via instance encoder, updates its state encoding StAS^{A}\_{t}, and generates an answer ata\_{t},
(3) Q-bot encodes (qt,at)(q\_{t},a\_{t}) pair, while A-bot encodes the answer it sampled,
(4) Q-bot updates its state to StQS^{Q}\_{t}, predicts an attribute pair via prediction LSTM at round TT, and receives a reward.

We formalize Q-bot and A-bot as agents operating in a partially observable world and optimize their policies using deep reinforcement learning.

States and Actions.
Each agent observes its own input (task GG for Q-bot and object instance II for A-bot) and the output of the other agent as a stochastic environment.
At the beginning of round tt, Q-bot observes state sQt=\[G,q1,a1,…,qt−1,at−1\]s\_{Q}^{t}{=}\[G,q\_{1},a\_{1},\\dots,q\_{t-1},a\_{t-1}\] and acts by uttering some token qtq\_{t} from its vocabulary VQV\_{Q}.
Similarly, A-bot observes the history and this new utterance as state sAt=\[I,q1,a1,…,qt−1,at−1,qt\]s\_{A}^{t}{=}\[I,q\_{1},a\_{1},\\dots,q\_{t-1},a\_{t-1},q\_{t}\] and emits a response ata\_{t} from VAV\_{A}.
At the last round, Q-bot takes a final action by predicting a pair of attribute values w^G=(w^1G,w^2G)\\hat{w}^{G}=(\\hat{w}^{G}\_{1},\\hat{w}^{G}\_{2}) to solve the task.

Cooperative Reward.
Both Q-bot and A-bot are rewarded identically based on the accuracy of Q-bot’s prediction w^G\\hat{w}^{G},
receiving a positive reward of R=1R{=}1 if the prediction matches ground truth wGw^{G} and a negative reward of R=−10R{=}{-}10 otherwise.
We arrive at these values empirically based on the speed of convergence in our experiments.

Policy Networks.
We model Q-bot and A-bot as operating under stochastic policies πQ​(qt∣stQ;θQ)\\pi\_{Q}(q\_{t}{\\mid}s^{Q}\_{t};\\theta\_{Q})
and πA​(at∣stA;θA)\\pi\_{A}(a\_{t}{\\mid}s^{A}\_{t};\\theta\_{A}) respectively, which we instantiate as
LSTM-based models.
We use lower case characters ( _e.g_.stQs\_{t}^{Q}) to denote the strings ( _e.g_.Q-bot’s token at round tt), and upper case StQS\_{t}^{Q} to denote the corresponding vector as encoded by the model.

As show in Fig. [2](https://arxiv.org/html/1706.08502v3#S3.F2 "Figure 2 ‣ 3 Modeling Q-bot and A-bot ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog"), Q-bot is modeled with three modules –
speaking, listening, and prediction.
The task GG is received as a 6-dimensional one-hot encoding over the space
of possible tasks and embedded via the listener LSTM.
At each round tt,
the _speaker network_ models the probability of output utterances qt∈VQq\_{t}\\in V\_{Q} based on the state St−1QS^{Q}\_{t-1}.
This is modeled as a fully-connected layer followed by a softmax that transforms St−1QS^{Q}\_{t-1} to a distribution over VQV\_{Q}.
After receiving the reply ata\_{t} from A-bot, the
_listener LSTM_ updates the state by processing both tokens of the dialog exchange.
In the final round, the _prediction LSTM_ is unrolled twice to produce Q-bot’s prediction based on the final state STQS\_{T}^{Q} and the task GG.
As before, task GG is fed in as a one-hot encoding to the prediction LSTM for two time steps, resulting in a pair of outputs used as the predictionw^G\\hat{w}\_{G}.

Analogously, A-bot is modeled as a combination of
a _speaker network_, a _listener LSTM_, and an _instance encoder_.
Like in Q-bot, the speaker network models the probability of utterances at∈VAa\_{t}\\in V\_{A} given the state StAS\_{t}^{A} and the listener LSTM updates the state StAS\_{t}^{A} based on dialog exchanges.
The instance encoder embeds each one-hot attribute vector via a linear layer and concatenates all three encodings to obtain a unified instance representation.

Learning Policies with REINFORCE.
To train these agents, we update policy parameters θQ\\theta\_{Q} and θA\\theta\_{A} using the popular REINFORCE [Williams (1992)](https://arxiv.org/html/1706.08502v3#bib.bib24 "") policy gradient algorithm.
Note that while the game is fully-cooperative, we do not assume full observability of one agent by another, opting instead to treat each agent as part of the stochastic environment when updating the other.
We will now derive the parameter gradients for our setup.

Recall that our agents take actions – utterances (qtq\_{t} and ata\_{t}) and attribute prediction (w^G\\hat{w}\_{G}) – and our
objective is to maximize the expected reward under the agents’ policies:

| | | | |
| --- | --- | --- | --- |
| |
| | maxθA,θQ⁡J⁡(θA,θQ)where,\\displaystyle\\max\_{\\theta\_{A},\\theta\_{Q}}J(\\theta\_{A},\\theta\_{Q})\\quad\\text{where,} | | (1a) |
| | J⁡(θA,θQ)=𝔼πQ,πA\[R⁡(w^G,wG)\]\\displaystyle J(\\theta\_{A},\\theta\_{Q})=\\mathop{\\mathbb{E}}\_{\\pi\_{Q},\\pi\_{A}}\\left\[R\\big(\\hat{w}^{G},w^{G}\\big)\\right\] | | (1b) |

Though the agents receive the reward at the end of gameplay, all intermediate actions are assigned the same reward RR.
Following the REINFORCE algorithm, we write the gradient of this expectation as an expectation of policy gradients.
For θQ\\theta\_{Q}, we derive this explicitly at a time step tt:

| | | | | | |
| --- | --- | --- | --- | --- | --- |
| | ∇θQJ\\displaystyle\\nabla\_{\\theta\_{Q}}J | =\\displaystyle{=} | ∇θQ\[𝔼πQ,πA\[R⁡(w^G,wG)\]\]\\displaystyle\\nabla\_{\\theta\_{Q}}\\left\[\\mathop{\\mathbb{E}}\_{\\pi\_{Q},\\pi\_{A}}\\left\[R\\big(\\hat{w}^{G},w^{G}\\big)\\right\]\\right\] | | (2) |
| | | =\\displaystyle{=} | ∇θQ\[∑qt,atπQ(qt\|st−1Q)πA(at\|stA)R(.)\]\\displaystyle\\nabla\_{\\theta\_{Q}}\\left\[\\sum\_{q\_{t},a\_{t}}\\pi\_{Q}\\left(q\_{t}\|s^{Q}\_{t-1}\\right)\\pi\_{A}\\left(a\_{t}\|s^{A}\_{t}\\right)R(.)\\right\] | |
| | | =\\displaystyle{=} | ∑qt,atπQ(qt\|st−1Q)∇θQlogπQ(qt\|st−1Q)πA(at\|stA)R(.)\\displaystyle\\sum\_{q\_{t},a\_{t}}\\pi\_{Q}\\left(q\_{t}\|s^{Q}\_{t-1}\\right)\\nabla\_{\\theta\_{Q}}\\log\\pi\_{Q}\\left(q\_{t}\|s^{Q}\_{t-1}\\right)\\pi\_{A}\\left(a\_{t}\|s^{A}\_{t}\\right)R(.) | |
| | | =\\displaystyle{=} | 𝔼πQ,πA\[R(.)∇θQlogπQ(qt\|st−1Q)\]\\displaystyle\\mathop{\\mathbb{E}}\_{\\pi\_{Q},\\pi\_{A}}\\left\[R(.)\\,\\nabla\_{\\theta\_{Q}}\\log\\pi\_{Q}\\left(q\_{t}\|s^{Q}\_{t-1}\\right)\\right\]\\hskip-42.0pt | |

Similarly, gradient w.r.t.θA\\theta\_{A}, _i.e_., ∇θAJ\\nabla\_{\\theta\_{A}}J will be:

| | | | |
| --- | --- | --- | --- |
| | ∇θAJ=𝔼πQ,πA\[R(.)∇θAlogπA(at\|stA)\]\\displaystyle\\vskip-15.0pt\\nabla\_{\\theta\_{A}}J=\\mathop{\\mathbb{E}}\_{\\pi\_{Q},\\pi\_{A}}\\left\[R(.)\\,\\nabla\_{\\theta\_{A}}\\log\\pi\_{A}\\left(a\_{t}\|s^{A}\_{t}\\right)\\right\]\\vskip-18.0pt | | (3) |

As is standard practice, we estimate these expectations with sample averages – sampling an environment (object instance and task), sampling a dialog between Q-bot and A-bot, culminating in a prediction from Q-bot and the received reward.
The REINFORCE update rule above has an
intuitive interpretation – an _informative_ dialog (qt,at)(q\_{t},a\_{t}) that leads to positive reward will be made more probable (positive gradient), while a poor exchange leading to negative reward will be pushed down (negative gradient).

Implementation Details.
All our models are implemented using the Pytorch111 [github.com/pytorch/pytorch](http://github.com/pytorch/pytorch "") deep learning framework.
To represent instances, we learn a 2020 dimensional embedding for every possible attribute values and concatenate the three instance attributes to obtain a final instance representation of size 6060.
Tokens from VQV\_{Q} and VAV\_{A} are encoded as one-hot vectors and then embedded into 2020 dimension vectors.
Both A-bot and Q-bot learn their own token embeddings without sharing.
The listener networks in both agents are implemented as LSTMs with a hidden layer size of 5050 dimensions.
All modules within an agent are initialized using the Xavier method [Glorot and Bengio (2010)](https://arxiv.org/html/1706.08502v3#bib.bib7 "").

We use 10001000 episodes of two-round dialogs to compute policy gradients, and perform updates according to Adam optimizer [Kingma and Ba (2015)](https://arxiv.org/html/1706.08502v3#bib.bib10 ""), with a learning rate of 0.010.01.
Furthermore, gradients are clipped at \[−5.0,5.0\]\[-5.0,5.0\].
For faster convergence, 80%80\\% of train episodes for the next iteration are from instances misclassified by the current network, while randomly sampling the remaining from all instances.
Our code is publicly available222 [github.com/batra-mlp-lab/lang-emerge](http://github.com/batra-mlp-lab/lang-emerge "").

## 4 The Road to Compositionality

This section details our key observation –
that while the agents always successfully invent
a language to solve the game with
near-perfect accuracies, the invented languages are decidedly _not_ compositional, interpretable, or ‘natural’
( _e.g_.A-bot ignoring Q-bot’s utterances and simply
encoding every object with a unique symbol
if the vocabulary is sufficiently large).
In our setting, the language being compositional simply amounts to the ability of the agents to communicate the compositional atoms of a task ( _e.g_.shape or color) and an instance ( _e.g_.square or blue) independently.

Through this section, we present a series of settings that get progressively more restrictive to coax the agents towards adopting a compositional language, providing analysis of the learned languages and ‘cheating’ strategies developed along the way.
Tab. [2](https://arxiv.org/html/1706.08502v3#S4.T2 "Table 2 ‣ 4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") summarizes results for all settings.
In all experiments, optimal policies (achieving near-perfect training rewards) were found.
For each setting, we provide qualitative analysis of the learned languages and report their ability to generalize to unseen instances.
We use 80% of the object-instances for training and the remaining 20% for evaluation.

### 4.1 Overcomplete Vocabularies

We begin with the simplest setting where both A-bot and Q-bot are given arbitrarily large
vocabularies.
We find that when \|VA\|\|V\_{A}\| is greater than the number of instances (64), the learned
policy mostly ignores what Q-bot asks and instead has A-bot convey the instance using pairs of symbols across rounds unique to an instance,
_e.g_., both token pairs (a1,a2)=(14,31),(40,1)(a\_{1},a\_{2}){=}(14,31),(40,1) convey _(red, triangle, filled)_, as shown in Fig. [3](https://arxiv.org/html/1706.08502v3#S4.F3 "Figure 3 ‣ 4.1 Overcomplete Vocabularies ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").
Notice, this means no ‘dialog’ is necessary and amounts to each agent having a codebook that maps symbols to object instances.
In essence, this setting has collapsed to an analog of Lewis Signaling (LS) game with A-bot signaling its complete world state and Q-bot simply reporting the target attributes.
More examples to illustrate this behavior for this setting are shown in Fig. [3](https://arxiv.org/html/1706.08502v3#S4.F3 "Figure 3 ‣ 4.1 Overcomplete Vocabularies ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").

![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/examples_sec41_supp.png)

Figure 3: Overcomplete vocabularies setting (\|VQ\|=\|VA\|=64\|V\_{Q}\|=\|V\_{A}\|=64, Sec. [4.1](https://arxiv.org/html/1706.08502v3#S4.SS1 "4.1 Overcomplete Vocabularies ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")).
Owing to a large vocabulary, we denote the tokens using numbers, as opposed to English alphabet characters shown in other figures.
A-bot mostly ignores what Q-bot asks and instead conveys the instance using pairs of symbols across rounds unique to an instance, leading to a highly non-human intuitive and non-compositional language.

Perhaps as expected, the generalization of this language to unseen instances is quite poor (success rate: 25.6%).
The adopted strategy of mapping instances to token pairs fails for test instances containing novel combinations of attributes for which the agents lack an agreed-upon code from training.

It seems clear that like in human communication [Nowak et al. (2000)](https://arxiv.org/html/1706.08502v3#bib.bib18 ""), a limited vocabulary that cannot possibly encode the richness of the world seems to be necessary for non-trivial dialog to emerge. We explore such a setting next.

### 4.2 Attribute-Value Vocabulary

![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/examples_sec42_supp.png)

Figure 4: Attribute and Value vocabulary setting (\|VQ\|=3,\|VA\|=12\|V\_{Q}\|=3,\|V\_{A}\|=12, Sec. [4.2](https://arxiv.org/html/1706.08502v3#S4.SS2 "4.2 Attribute-Value Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")).
We show symmetric tasks for each instance on either side to illustrate the similarities in the language between the agents.
As seen here, Q-bot maps symmetric tasks in an order-agnostic fashion, and uses only the first token to convey task information to A-bot.

Since our world has 3 attributes ( _shape_/ _color_/ _style_) and 4+4+4=124+4+4=12 possible settings of their states,
one may believe that the intuitive
choice of \|VQ\|=3\|V\_{Q}\|=3 and \|VA\|=12\|V\_{A}\|=12 will be enough to circumvent
the ‘cheating’ enumeration strategy from
the previous experiment.
Surprisingly, we find that the new
language learned in this setting is not only
decidedly non-compositional but also very difficult to interpret!
Some observations follow from Fig. [4](https://arxiv.org/html/1706.08502v3#S4.F4 "Figure 4 ‣ 4.2 Attribute-Value Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") that shows sample dialogs for this setting.

We observe that Q-bot uses only the first round to convey the task to A-bot by encoding tasks in an order-agnostic fashion, as:
_(style, shape),(shape, style)_ →{\\rightarrow} X,
_(color, shape),(shape, color)_ →{\\rightarrow} Y, and
_(color, style),(style, color)_ →{\\rightarrow} Z.Thus, multiple rounds of utterance from Q-bot are rendered unnecessary and we find the second round is inconsistent across instances even for the same task.
For example, symmetric tasks _(color, shape)_ and _(shape, color)_ from first row of Fig. [4](https://arxiv.org/html/1706.08502v3#S4.F4 "Figure 4 ‣ 4.2 Attribute-Value Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") induce q1=Yq\_{1}{=}Y as the first token from Q-bot.

Given the task from Q-bot in the first round, A-bot only needs to identify one of the 4×4=164{\\times}4{=}16 attribute pairs for a given task.
Rather than ground its symbols into individual states, A-bot follows a ‘set partitioning’ strategy, _i.e_.A-bot identifies a pair of attributes with a unique combinations of round 1 and 2 utterances ( _i.e_. the round 2 utterance has no meaning independent from round 1).
Thus, symbols are reused across tasks to describe different attributes ( _i.e_. symbols do not have individual consistent groundings). This ‘set partitioning’ strategy is consistent
with known results from game theory on Nash equilibria in
‘cheap talk’ games [Crawford and Sobel (1982)](https://arxiv.org/html/1706.08502v3#bib.bib2 "").

This strategy has improved generalization to unseen instances because it is able to communicate the task; however, it fails on unseen attribute value combinations because
it is not compositional.

### 4.3 Memoryless A-bot, Minimal Vocabulary

![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/examples_sec43_supp.png)Figure 5: Example dialogs for memoryless A-bot, minimal vocabulary setting (\|VQ\|=3,\|VA\|=4\|V\_{Q}\|=3,\|V\_{A}\|=4, Sec. [4.3](https://arxiv.org/html/1706.08502v3#S4.SS3 "4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")).
Learnt language is consistent and grounded, denoted below each token.
Incorrect predictions on unseen instances (right, bottom) are also shown.
Notice that the incorrectly predicted attribute is still from the right category (a color attribute for _color_).

The key problem with the previous setting is that A-bot’s utterances _mean different things_ based on the round of dialog (a1=1a\_{1}=1 is different from a2=1a\_{2}=1).
Essentially, the communication protocol is over-parameterized and we must limit it further.
First, we limit A-bot’s vocabulary to \|VA\|=4\|V\_{A}\|{=}4 to reduce the number of ‘synonyms’ the agents learn.
Second, we eliminate A-bot’s capability to identify different rounds of interaction by _removing A-bot’s memory_.
In other words, we reset the state vector SAS^{A} at each time step so that A-bot can no longer distinguish rounds from one another.

By doing so, we hypothesize that Q-bot must now ground its own and A-bot’s tokens consistently across rounds to be able to communicate with a memoryless A-bot.

These restrictions result in a learned language
that grounds _individual symbols_ into
attributes and their states.
For example, Q-bot learns that Y→shapeY\\rightarrow\\mbox{shape}, X→colorX\\rightarrow\\mbox{color}, and Z→styleZ\\rightarrow\\mbox{style}.
Q-bot does not however learn to always utter these symbols in the same order as the task, _e.g_. asking for _shape_ first for both (c​o​l​o​r,s​h​a​p​e)(color,shape) and (s​h​a​p​e,c​o​l​o​r)(shape,color).
Notice that this is perfectly valid as Q-bot can later re-arrange the attributes in the task desired order.
Similarly, A-bot learns mappings to attribute values for each attribute query that remain consistent regardless of round ( _i.e_. when asked for c​o​l​o​rcolor, 11 always means b​l​u​eblue).

This is similar to learned languages reported in recent works and is most closely related to [Das et al. (2017b)](https://arxiv.org/html/1706.08502v3#bib.bib4 ""), who solve this problem by taking away Q-bot’s state rather than A-bot’s memory.
Their approach of taking away task GG from Q-bot’s state can be interpreted as Q-bot ‘forgetting’ the task after interacting with A-bot.
However, this behavior of Q-bot to remember the task only during dialog but not while predicting is somewhat unnatural compared to our setting.

Tab. [1](https://arxiv.org/html/1706.08502v3#S4.T1 "Table 1 ‣ 4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") enumerates the learnt groundings for both the agents.
Given this mapping, we can predict a plausible dialog between the agents for any unseen instance and task combination.
Notice that this is possible only due to the compositionality in the emergent language between the two agents.
For example, consider solving the task _(shape, color)_ for an instance _(red, square, filled)_ from Fig. [7](https://arxiv.org/html/1706.08502v3#S5.F7 "Figure 7 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")(b).
Q-bot queries _Y (shape)_ and _X (color)_ across two rounds, and receives _2 (square)_ and _4 (red)_ as answers.
More examples along with grounded meaning of each tokens are shown in Fig. [5](https://arxiv.org/html/1706.08502v3#S4.F5 "Figure 5 ‣ 4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").

| | Attributes |
| --- | --- |
| | _color_ | _shape_ | _style_ |
| VAV\_{A} | _X_ | _Y_ | _Z_ |
| _1_ | _blue_ | _triangle_ | _dotted_ |
| _2_ | _purple_ | _square_ | _filled_ |
| _3_ | _green_ | _circle_ | _dashed_ |
| _4_ | _red_ | _start_ | _solid_ |

(a) A-bot

| Task | q1,q2q\_{1},q\_{2} |
| --- | --- |
| _(color, shape)_ | _Y, X_ |
| _(shape, color)_ |
| _(shape, style)_ | _Y, Z_ |
| _(style, shape)_ |
| _(color, style)_ | _Z, X_ |
| _(style, color)_ | _X, Z_ |

(b) Q-bot

Table 1: Emergence of compositional grounding for language learnt by the agents.
A-bot (Tab. [1(a)](https://arxiv.org/html/1706.08502v3#S4.T1.st1 "In Table 1 ‣ 4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")) learns consistent mapping across rounds, depending on the query attribute.
Token grounding for Q-bot (Tab. [1(b)](https://arxiv.org/html/1706.08502v3#S4.T1.st2 "In Table 1 ‣ 4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")) depends on the task at hand.
Though compositional, Q-bot does not necessarily query attribute in the order of task, but instead re-arranges accordingly at prediction time as it contains memory.

Intuitively, this consistently grounded and compositional language has the greatest ability to generalize among the settings we have explored, correctly answering 74.4% of the held out instances.
We note that errors in this setting seem to largely be due to A-bot giving an incorrect answers despite Q-bot asking the correct questions to accomplish the task.
A plausible reason could be the model approximation error stemming from the instance encoder as test instances are unseen and have novel attribute combinations.

| Setting | Vocab. | Memory | Seen (%) | Unseen (%) | Characteristics |
| --- | --- | --- | --- | --- | --- |
| | VQV\_{Q} | VAV\_{A} | A | Q | Both | One | Both | One |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Overcomplete (§ [4.1](https://arxiv.org/html/1706.08502v3#S4.SS1 "4.1 Overcomplete Vocabularies ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")) | 64 | 64 | ✓ | ✓ | 100 | 100 | 25.6 | 79.5 | •Non-compositional language•Q-bot insignificant•Inconsistent A-bot grounding across rounds•Poor generalization to unseen instances |
| Attr-Value (§ [4.2](https://arxiv.org/html/1706.08502v3#S4.SS2 "4.2 Attribute-Value Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")) | 3 | 12 | ✓ | ✓ | 100 | 100 | 38.5 | 88.4 | •Non-compositional language•Q-bot uses one round to convey task•Inconsistent A-bot grounding across rounds•Poor generalization to unseen instances |
| NoMem-Min (§ [4.3](https://arxiv.org/html/1706.08502v3#S4.SS3 "4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog")) | 3 | 4 | ✗ | ✓ | 100 | 100 | 74.4 | 94.9 | •Compositional language•Q-bot uses both rounds to convey task•Consistent A-bot grounding across rounds•Good generalization to unseen instances |

Table 2: Overview of settings we explore to analyze the language learnt by two agents in a cooperative game, Task & Talk. Last two columns measure generalization in terms of prediction accuracy of both or at least one of the attribute pair, on a held-out test set containing unseen instances.

## 5 Evolution of Language

As demonstrated by the previous sections, even though compositional language is one of the optimal policies, the agents tend to learn other equally useful forms of communication.
Thus, compositional language does not naturally emerge without an explicit need for it.
Even in situations where compositionality does emerge, perhaps it is more interesting to analyze the process of emergence than the learnt language itself.
Therefore, we present such a study that explicitly identifies _when_ each symbol has been grounded by the agents in the training timeline, along with implications thereof on the performance on Task & Talk game.

### 5.1 Dialog Trees

When two agents–Q-bot and A-bot–converse with each other, they can be seen as traversing through a dialog tree, a subtree of which is depicted in Fig. [6](https://arxiv.org/html/1706.08502v3#S5.F6 "Figure 6 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").
Simply put, a dialog tree is an enumeration of all possible dialogs represented in the form of tree, with levels of the tree corresponding to the round of interaction.
To elaborate, consider a partial dialog tree for _(shape, color)_ task shown in Fig. [6](https://arxiv.org/html/1706.08502v3#S5.F6 "Figure 6 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") for the setting in Sec. [4.3](https://arxiv.org/html/1706.08502v3#S4.SS3 "4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").
For Q-bot’s first token q1=Yq\_{1}=Y, A-bot has \|VA\|=4\|V\_{A}\|=4 plausible replies shown as a 4-way branch off.
In general, the dialog tree for Task & Talk contains a total of \|VQ\|2​\|VA\|2\|V\_{Q}\|^{2}\|V\_{A}\|^{2} leaves and is 4 levels deep.
We use the dialog between the agents to descend and land in one of these leaves.

Dialog trees offer an interesting alternate view of our learning problem.
The goal of learning communication between the two agents can be equivalently seen as mapping _(instance, task)_ pairs to one of the dialog tree leaves.
Each leaf is labeled with an attribute pair used to accomplish the prediction task.
For example, if solving _(shape, color)_ for _(blue, triangle, solid)_ results in the dialog Y→1→X→1Y{\\rightarrow}1{\\rightarrow}X{\\rightarrow}1,
we descend the dialog tree along the corresponding path and assign the tuple _(blue, triangle, solid, shape, color)_ to the resulting leaf.
In case of a compositional, grounded dialog, all tuples of the form _(blue, triangle, ∗\\ast, shape, color)_ would get mapped to the same leaf, which can then be labeled as _(triangle, blue)_ to successfully solve the task.
Note the wildcard _style_ attribute in the tuple above, as it is irrelevant for this particular task.

In the following section, we use dialog trees to explore the evolution of language as learnt by the two agents in the memoryless A-bot, minimal vocabulary setting in Sec. [4.3](https://arxiv.org/html/1706.08502v3#S4.SS3 "4.3 Memoryless A-bot, Minimal Vocabulary ‣ 4 The Road to Compositionality ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").

![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/dialog_tree_v2.png)Figure 6: Dialog tree for memoryless A-bot and minimal vocabulary setting (Sec.4.3), shown only for one task _(shape, color)_.
Every dialog between the agents results in a tree traversal beginning from the root, _e.g_., Y→1→X→1Y{\\rightarrow}1{\\rightarrow}X{\\rightarrow}1 lands us in the top-right leaf. See text for more details.![Refer to caption](https://arxiv.org/html/1706.08502v3/figures/language_chart_supp.png)Figure 7: Evolution of Language: timeline shows groundings learned by the agents during training, overlaid on the accuracy. Note that Q-bot learns encodings for all tasks early (around epoch 2020) except _(style, color)_. Improvement in accuracy is strongly correlated with groundings learnt.

### 5.2 Evolution Timeline

To gain further insight into the languages learned,
we create a _language evolution_ plot shown in Fig. [7](https://arxiv.org/html/1706.08502v3#S5.F7 "Figure 7 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").
Specifically, at
regular intervals during policy learning, we construct dialog trees.
At some point in the learning, the nodes in the tree become and stay ‘pure’
(all _(instance, task)_ at the node are identical),
at which point we can say that the agents have learned this dialog subsequence.
Fig. [7](https://arxiv.org/html/1706.08502v3#S5.F7 "Figure 7 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") depicts a timeline of concepts learned at various nodes of the trees during training.
We next describe the procedure to identify when a particular ‘concept’ has been grounded by the agents in their language.

Construction.
After constructing dialog trees at regular intervals, we identify ‘concepts’ at each node/leaf using the dialog tree of the completely trained model, which achieves a perfect accuracy on train set.
A concept is simply the common trend among all the _(instance, task)_ tuples either assigned to a leaf or contained within the subtree with a node as root.
To illustrate, the concept of the top right leaf in Fig. [6](https://arxiv.org/html/1706.08502v3#S5.F6 "Figure 6 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") is _(blue, triangle, ∗\\ast, shape, color)_, _i.e_., all instances assigned to that leaf for _(shape, color)_ task are blue triangles.
Next, given a resultant concept for each of the node/leaf, we backtrack in time and check for the first occurrence when only tuples which satisfy the corresponding concept are assigned to that particular node/leaf.
In other words, we compute the earliest time when a node/leaf is ‘pure’ with respect to its final learned concept.
Finally, we plot these leaves/nodes and the associated concept with their backtracked time to get Fig. [7](https://arxiv.org/html/1706.08502v3#S5.F7 "Figure 7 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").

Observations. We highlight the key observations from Fig. [7](https://arxiv.org/html/1706.08502v3#S5.F7 "Figure 7 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog") below:

1. (a)


The agents ground most of the tasks initially at around epoch 20.
Specifically, Q-bot assigns _Y_ to both _(shape, style), (style, shape), (shape,color)_ and _(color, shape)_, while _(color, style)_ is mapped to _Z_.
Hence, Q-bot learns its first token very early into the training procedure at around 20 epochs.

2. (b)


The only other task _(style, color)_ is grounded towards the end (around epoch 170) using _X_, leading to an immediate convergence.

3. (c)


We see a strong correlation between improvement in performance and when agents learn a language grounding.
In particular, there is an improvement from 40%40\\% to 80%80\\% within a span of 25 epochs where most of the grounding is achieved, as seen from Fig. [7](https://arxiv.org/html/1706.08502v3#S5.F7 "Figure 7 ‣ 5.1 Dialog Trees ‣ 5 Evolution of Language ‣ Natural Language Does Not Emerge ‘Naturally’ in Multi-Agent Dialog").


## 6 Conclusion

In conclusion,
we presented a sequence of ‘negative’ results
culminating in a ‘positive’ one – showing
that while most invented languages are effective
( _i.e_. achieve near-perfect rewards), they
are decidedly _not_ interpretable or compositional.
Our goal is simply to improve understanding and interpretability
of invented languages in multi-agent dialog, place recent work in context, and inform fruitful directions for future work.

## References

- Bordes and Weston (2016)
Antoine Bordes and Jason Weston. 2016.

Learning End-to-End Goal-Oriented Dialog.

arXiv preprint arXiv:1605.07683 .

- Crawford and Sobel (1982)
Vincent Crawford and Joel Sobel. 1982.

Strategic information transmission.

Econometrica 50(6):1431–51.

- Das et al. (2017a)
Abhishek Das, Satwik Kottur, Khushi Gupta, Avi Singh, Deshraj Yadav,
José M.F. Moura, Devi Parikh, and Dhruv Batra. 2017a.

Visual Dialog.

In CVPR.

- Das et al. (2017b)
Abhishek Das, Satwik Kottur, José M.F. Moura, Stefan Lee, and Dhruv Batra.
2017b.

Learning Cooperative Visual Dialog Agents with Deep
Reinforcement Learning.

arXiv preprint arXiv:1703.06585 .

- de Vries et al. (2017)
Harm de Vries, Florian Strub, Sarath Chandar, Olivier Pietquin, Hugo
Larochelle, and Aaron C. Courville. 2017.

Guesswhat?! visual object discovery through multi-modal dialogue.

In CVPR.

- Foerster et al. (2016)
Jakob Foerster, Yannis M Assael, Nando de Freitas, and Shimon Whiteson. 2016.

Learning to communicate with deep multi-agent reinforcement learning.

In NIPS.

- Glorot and Bengio (2010)
Xavier Glorot and Yoshua Bengio. 2010.

Understanding the difficulty of training deep feedforward neural
networks.

In AISTATS.

- Havrylov and Titov (2017)
Serhii Havrylov and Ivan Titov. 2017.

Emergence of language with multi-agent games: Learning to communicate
with sequences of symbols.

In ICLR Workshop.

- Jorge et al. (2016)
Emilio Jorge, Mikael Kågebäck, and Emil Gustavsson. 2016.

Learning to play guess who? and inventing a grounded language as a
consequence.

In NIPS workshop on deep reinforcement learning.

- Kingma and Ba (2015)
Diederik Kingma and Jimmy Ba. 2015.

Adam: A Method for Stochastic Optimization.

In ICLR.

- Kirby et al. (2014)
Simon Kirby, Tom Griffiths, and Kenny Smith. 2014.

Iterated learning and the evolution of language.

Current opinion in neurobiology 28:108–114.

- Lazaridou et al. (2017)
Angeliki Lazaridou, Alexander Peysakhovich, and Marco Baroni. 2017.

Multi-agent cooperation and the emergence of (natural) language.

In ICLR.

- Lemon et al. (2006)
Oliver Lemon, Kallirroi Georgila, James Henderson, and Matthew Stuttle. 2006.

An ISU dialogue system exhibiting reinforcement learning of dialogue
policies: generic slot-filling in the TALK in-car system.

In EACL.

- Lewis (2008)
David Lewis. 2008.

Convention: A philosophical study.

John Wiley & Sons.

- Lowe et al. (2015)
Ryan Lowe, Nissan Pow, Iulian Serban, and Joelle Pineau. 2015.

The Ubuntu Dialogue Corpus: A Large Dataset for Research in
Unstructured Multi-Turn Dialogue Systems.

In SIGDIAL.

- Mordatch and Abbeel (2017)
Igor Mordatch and Pieter Abbeel. 2017.

Emergence of grounded compositional language in multi-agent
populations.

arXiv preprint arXiv:1703.04908 .

- Mostafazadeh et al. (2017)
Nasrin Mostafazadeh, Chris Brockett, Bill Dolan, Michel Galley, Jianfeng Gao,
Georgios P. Spithourakis, and Lucy Vanderwende. 2017.

Image-Grounded Conversations: Multimodal Context for Natural
Question and Response Generation.

arXiv preprint arXiv:1701.08251 .

- Nowak et al. (2000)
Martin A. Nowak, Joshua B. Plotkin, and Vincent A. A. Jansen. 2000.

The evolution of syntactic communication.

Nature 404(6777):495–498.

- Serban et al. (2016a)
Iulian V. Serban, Alessandro Sordoni, Yoshua Bengio, Aaron Courville, and
Joelle Pineau. 2016a.

Building End-To-End Dialogue Systems Using Generative Hierarchical
Neural Network Models.

In AAAI.

- Serban et al. (2016b)
Iulian Vlad Serban, Alessandro Sordoni, Ryan Lowe, Laurent Charlin, Joelle
Pineau, Aaron Courville, and Yoshua Bengio. 2016b.

A Hierarchical Latent Variable Encoder-Decoder Model for Generating
Dialogues.

arXiv preprint arXiv:1605.06069 .

- Sukhbaatar et al. (2016)
Sainbayar Sukhbaatar, Rob Fergus, et al. 2016.

Learning multiagent communication with backpropagation.

In NIPS. pages 2244–2252.

- Wang et al. (2016)
Sida I Wang, Percy Liang, and Christopher D Manning. 2016.

Learning language games through interaction.

Association for Computational Linguistics (ACL) .

- Weston (2016)
Jason Weston. 2016.

Dialog-based language learning.

arXiv preprint arXiv:1604.06045 .

- Williams (1992)
Ronald J Williams. 1992.

Simple statistical gradient-following algorithms for connectionist
reinforcement learning.

Machine learning 8(3-4):229–256.

- Winograd (1971)
Terry Winograd. 1971.

Procedures as a representation for data in a computer program for
understanding natural language.

Technical report, DTIC Document.