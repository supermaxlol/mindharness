Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2412.07646v1 \[cs.CL\] 10 Dec 2024

# Searching for Structure: Investigating Emergent Communication with Large Language Models

Tom Kouwenhoven
Affiliation: Leiden Institute of Advanced Computer Science, Leiden University, Netherlands
Email: [t.kouwenhoven@liacs.leidenuniv.nl](mailto:t.kouwenhoven@liacs.leidenuniv.nl)Max Peeperkorn
Affiliation: School of Computing, University of Kent, United Kingdom
Email: [t.verhoef@liacs.leidenuniv.nl](mailto:t.verhoef@liacs.leidenuniv.nl)Tessa Verhoef
Affiliation: Leiden Institute of Advanced Computer Science, Leiden University, Netherlands

###### Abstract

Human languages have evolved to be structured through repeated language learning and use. These processes introduce biases that operate during language acquisition and shape linguistic systems toward communicative efficiency. In this paper, we investigate whether the same happens if artificial languages are optimised for implicit biases of Large Language Models (LLMs). To this end, we simulate a classical referential game in which LLMs learn and use artificial languages. Our results show that initially unstructured holistic languages are indeed shaped to have some structural properties that allow two LLM agents to communicate successfully. Similar to observations in human experiments, generational transmission increases the learnability of languages, but can at the same time result in non-humanlike degenerate vocabularies. Taken together, this work extends experimental findings, shows that LLMs can be used as tools in simulations of language evolution, and opens possibilities for future human-machine experiments in this field.

## 1 Introduction

Vocabularies of signals enable us to communicate about meanings, but to express an arbitrary number of meanings, vocabularies would require an equally large set of words as there are meanings, and learning such holistic vocabularies is cognitively challenging. Human languages therefore typically show some form of compositional structure, where meaningful signal-meaning mappings can be composed such that the combination of individual meaningful signals can express more than the meaning of the individual components alone [Hockett (1960)](https://arxiv.org/html/2412.07646v1#bib.bib22 ""). An important finding in the field of language evolution is that such structural properties can emerge as a result of individual learning biases and pressures that continuously shape the languages on a longer timescale, often eventually resulting in languages that are easier to learn and exhibit some degree of structure [Smith (2022)](https://arxiv.org/html/2412.07646v1#bib.bib52 "").

The processes involved in the evolution of language have been investigated abundantly with experiments and simulations. The latter typically use hard-coded agents with inductive biases [de Boer (2006)](https://arxiv.org/html/2412.07646v1#bib.bib14 ""), Bayesian learners ( [Griffiths and Kalish, 2007](https://arxiv.org/html/2412.07646v1#bib.bib21 ""); [Culbertson and Smolensky, 2012](https://arxiv.org/html/2412.07646v1#bib.bib12 ""); [Kirby et al., 2015](https://arxiv.org/html/2412.07646v1#bib.bib29 ""), e.g.), or reinforcement learning agents [Lazaridou and Baroni (2020)](https://arxiv.org/html/2412.07646v1#bib.bib33 "") to investigate the evolution of structured languages. In contrast, we investigate whether more flexible LLMs as relatively unbiased language learners [Wilcox et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib63 "") are appropriate tools to study how languages evolve. While their internal mechanisms are fundamentally different from humans, they still are the first close flexible comparators of human language users that can be used as tools to answer cognitive and typological investigations [Warstadt and Bowman (2022)](https://arxiv.org/html/2412.07646v1#bib.bib61 ""); [van Dijk et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib58 ""). Given that languages are shaped by the biases and pressures of individual language learners, which are different for LLMs (e.g., fewer memory constraints), we are interested in finding similarities and differences between humans and LLMs on specific language evolution-oriented tasks.

Our work largely follows the experimental design by [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 "") in which Bayesian learners and humans learn an artificial language to communicate in a referential game. They find that linguistic structure arises from a trade-off between pressures for compressibility and expressivity. Our work extends their work by using LLMs as objects of investigation. Specifically, we investigate how artificial languages evolve when two LLMs communicate in a referential game and what the effects of generational transmission on these languages are. We compare properties of these languages to those that are found in experiments involving humans. Results show that 1) LLMs can learn artificial languages and use them to communicate successfully, 2) the languages exhibit higher degrees of structure after multiple communication rounds, 3) LLMs generalise in more systematic ways when the evolved language is more structured, and 4) languages adapt, although not necessarily in a human-like way, and become easier to learn by the LLMs as a result of generational transmission.

## 2 Background & Related work

### 2.1 The evolution of structure

Learning novel signal-meaning mappings, and the emergence of rules that can combine these signals into structured languages have been abundantly investigated in the field of language evolution using human experiments [Kirby et al. (2008)](https://arxiv.org/html/2412.07646v1#bib.bib28 ""); [Galantucci (2005)](https://arxiv.org/html/2412.07646v1#bib.bib17 ""); [Scott-Phillips et al. (2009)](https://arxiv.org/html/2412.07646v1#bib.bib49 ""); [Verhoef (2012)](https://arxiv.org/html/2412.07646v1#bib.bib59 ""); [Raviv et al. (2019a)](https://arxiv.org/html/2412.07646v1#bib.bib47 ""); [Raviv et al. (2019b)](https://arxiv.org/html/2412.07646v1#bib.bib48 ""); [Kouwenhoven et al. (2022a)](https://arxiv.org/html/2412.07646v1#bib.bib30 "") and computational simulations [de Boer (2006)](https://arxiv.org/html/2412.07646v1#bib.bib14 ""); [Steels et al. (2012)](https://arxiv.org/html/2412.07646v1#bib.bib55 ""); [Lazaridou and Baroni (2020)](https://arxiv.org/html/2412.07646v1#bib.bib33 ""); [Kouwenhoven et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib31 ""). These typically follow a setup where success depends on cooperation between two or more participants/agents in a Lewis game. Here, players are prevented from communicating using conventional communicative means and instead must establish novel communication systems through repeated cooperation. Outcomes often show that players, human or machine, quickly establish novel signal-meaning mappings that enable them to communicate successfully. However, recent computational simulations using reinforcement learning agents often develop communicative systems different from those of humans [Galke et al. (2022)](https://arxiv.org/html/2412.07646v1#bib.bib18 "")111



But see [Lian et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib34 ""); [Lian et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib35 ""); [Zhang et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib65 "") for recent work showing that the need to be understood (i.e. communicative success), noise, context sensitivity, and incremental sentence processing help induce human-like patterns of dependency length minimisation in reinforcement learning agents. unless specific key pressures are introduced to recover initially absent human patterns [Galke and Raviv (2024)](https://arxiv.org/html/2412.07646v1#bib.bib20 "").

It has been suggested that seemingly arbitrary aspects of linguistic structure may result from general learning and processing biases deriving from the structure of thought processes, perceptuo-motor factors, cognitive limitations, and pragmatics [Christiansen and Chater (2008)](https://arxiv.org/html/2412.07646v1#bib.bib11 ""). A well-investigated cause for this phenomenon is the process of cumulative cultural evolution [Boyd et al. (1996)](https://arxiv.org/html/2412.07646v1#bib.bib5 ""); [Tomasello (1999)](https://arxiv.org/html/2412.07646v1#bib.bib57 ""), which is typically investigated using iterated learning experiments [Kirby et al. (2008)](https://arxiv.org/html/2412.07646v1#bib.bib28 ""). Here, information (e.g., a language) is repeatedly passed down from one generation to the next, where the information is modified and improved upon within each generation. The influential work from [Kirby et al. (2008)](https://arxiv.org/html/2412.07646v1#bib.bib28 ""); [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 "") shows that when human individuals learn an artificial language that was previously learned by another individual, languages become easier to learn and display a higher degree of structure. Crucially, these results are mostly attributed to the fact that the language repeatedly goes through a learning bottleneck, in which individual cognitive biases such as memory constraints slowly shape the language. Iterated learning has been used to show that structure emerges in various setups with, for example, continuous signals [Verhoef (2012)](https://arxiv.org/html/2412.07646v1#bib.bib59 "") or continuous meaning spaces [Carr et al. (2017)](https://arxiv.org/html/2412.07646v1#bib.bib9 ""), and it is argued that it may have led to the statistical Zipfian structure of language [Arnon and Kirby (2024)](https://arxiv.org/html/2412.07646v1#bib.bib3 ""). Yet, [Raviv et al. (2019a)](https://arxiv.org/html/2412.07646v1#bib.bib47 "") showed that structure can also emerge without generational transmission. In this case, a pressure for compressibility originating from communication with multiple interaction partners and expanding meaning spaces causes languages to become compositional. This effect is even more prominent if the number of interaction partners is larger [Raviv et al. (2019b)](https://arxiv.org/html/2412.07646v1#bib.bib48 ""). The current work is inspired by the traditional methods described before and extends them with our current most sophisticated models of natural language.

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/overview.png)Figure 1: A graphical representation of the experimental blocks. The agents first go through a guessing block before labelling each of the 15 training stimuli in the labelling block. The communication block is done for 4 rounds each consisting of 30 tasks TT, where the agents alternate speaker-listener roles to be a speaker and listener for each stimulus once. Finally, the agents label 27 (15 original and 12 novel) stimuli in the testing block.

### 2.2 LLMs as models of language

LLMs are sophisticated models of natural languages and growing evidence shows their ability to exhibit ‘average’ human behaviours. It is, for example, suggested that LLMs can model human moral judgements [Dillion et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib15 "") and transmission chain experiments revealed human-like content biases in GPT-3.5 [Acerbi and Stubbersfield (2023)](https://arxiv.org/html/2412.07646v1#bib.bib1 "").
When LLMs are extended with records of experiences, [Park et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib43 "") showed that groups of generative agents display believable human-like individual and emergent social behaviours when they interact over extended periods. It is even suggested that human-LLM interactions in everyday life can potentially mediate human cultures through their influence on cultural evolutionary processes of variation, transmission and selection [Brinkmann et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib7 ""); [Yiu et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib64 "").

While previous work has investigated human-like behaviour at inference time, findings from cognitive science can also be used to improve model performance. Iterated learning can, for example, be incorporated into the training regime to extrapolate desirable behaviours. [Zheng et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib66 "") have likewise shown that representations are easier to learn when vision-language contrastive learning is reframed as the Lewis signaling game between a vision agent and a language agent, ultimately improving compositional reasoning in vision-language models. However, this does not guarantee model improvements, [Shumailov et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib50 "") have for example shown that LLMs, autoencoders and Gaussian mixture models drift when trained repeatedly on AI-generated data. In these cases, crucially, the generated content is slowly optimised to be understandable for models, not for humans, resulting in what they call model collapse. The authors therefore argue that genuine human interactions with systems will be increasingly important to prevent model collapse. While drift is often seen as an unwanted effect of unsupervised training, from a language evolution viewpoint this is not surprising, since languages adapt to how they are learned and used. As such, it has been suggested that languages should adapt to become more natural for humans and machines [Kouwenhoven et al. (2022b)](https://arxiv.org/html/2412.07646v1#bib.bib32 "") and that findings from cognitive science can prevent modal collapse [Smith et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib53 "") or inform modelling choices [Galke and Raviv (2024)](https://arxiv.org/html/2412.07646v1#bib.bib20 ""). Here, we view LLMs from this evolutionary perspective.

Although biases inherent to a language model’s (pre-)training objectives (i.e. the cloze task and instruction tuning) and memory constraints are very different from those in humans, recent work has shown that GPT-2 models struggle to learn languages that contain unnatural word orders, lack hierarchical structure, or lack information locality [Kallini et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib26 ""). This suggests that, even though the language processing mechanisms in transformers are non-humanlike, LLMs share some preference for structured languages similar to humans. Moreover, in an artificial language learning experiment similar to the work presented here, [Galke et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib19 "") showed that compositional structure is advantageous for GPT-3 when learning an artificial language and that a higher degree of compositional structure also resulted in human-like generalisation for new unseen items. Our work is different in that [Galke et al.](https://arxiv.org/html/2412.07646v1#bib.bib19 "") tested the ability of GPT-3 to learn languages that evolved during a human experiment ( [Raviv et al., 2019b](https://arxiv.org/html/2412.07646v1#bib.bib48 ""); [Raviv et al., 2021](https://arxiv.org/html/2412.07646v1#bib.bib46 "")), thus being optimised for human learners. We instead wish to investigate what kinds of languages evolve when they are optimised for LLMs.

[⬇](data:text/plain;base64,ICAgICAgICAgICAgIHsnc2hhcGUnOjMsJ2NvbG91cic6J2JsdWUnLCdhbW91bnQnOjEsJ3dvcmQnOiduaW5pa29udSd9CiAgICAgICAgICAgICB7J3NoYXBlJzoxLCdjb2xvdXInOidncmVlbicsJ2Ftb3VudCc6Mywnd29yZCc6J2hhbm9zYSd9KkBcdnNwYWNley40ZW19QCoKICAgICAgICAgICAgICAgICAkXHNtYXNoXHZkb3RzJAogICAgICAgICAgICAgeydzaGFwZSc6MiwnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzoyLCd3b3JkJzonc2FudSd9CiAgICAgICAgICAgICB7J3NoYXBlJzoxLCdjb2xvdXInOidncmVlbicsJ2Ftb3VudCc6Mywnd29yZCc6J1tDT01QTEVURV0=)

{’shape’:3,’colour’:’blue’,’amount’:1,’word’:’ninikonu’}

{’shape’:1,’colour’:’green’,’amount’:3,’word’:’hanosa’}

⋮\\smash{\\vdots}

{’shape’:2,’colour’:’orange’,’amount’:2,’word’:’sanu’}

{’shape’:1,’colour’:’green’,’amount’:3,’word’:’\[COMPLETE\]

List of Prompts 2.1 A vocabulary snippet used in a completion prompt. Full prompts are visible in Appendix [C](https://arxiv.org/html/2412.07646v1#A3 "Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")

## 3 Methodology

Our methodology is inspired by [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 "") and [Raviv et al. (2021)](https://arxiv.org/html/2412.07646v1#bib.bib46 ""). The complete simulation set-up consists of four blocks: guessing, labelling, communication and testing (§ [3.2](https://arxiv.org/html/2412.07646v1#S3.SS2 "3.2 Simulation blocks ‣ 3 Methodology ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") & Figure [1](https://arxiv.org/html/2412.07646v1#S2.F1 "Figure 1 ‣ 2.1 The evolution of structure ‣ 2 Background & Related work ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") 111



This is for illustration purposes only, we stress that our simulations are entirely run in the textual modality only to avoid the additional challenge of extracting relevant visual features and mapping these to artificial languages.). The agents perform the guessing, labelling, and testing block separately; communication is interactive. The communication block is a classic referential game in which two agents communicate to discriminate a target stimulus from four distractor stimuli. They do so in four rounds, each consisting of 30 interactions TT, alternating speaker-listener roles between interactions. In a single interaction round, the speaker observes a target stimulus and utters a signal that describes the current stimulus. Using this utterance, the listener must discriminate the correct target. Cooperation is successful when the listener’s guess is the target stimulus.

### 3.1 Stimuli and initial languages

The meaning space consists of stimuli with three attributes. They have one of three shapes, one of three colours, and can appear in groups of one, two, or three shapes, creating 27 distinct stimuli. Initial signals for these stimuli were generated before each experiment according to the method used by [Kirby et al. (2008)](https://arxiv.org/html/2412.07646v1#bib.bib28 ""). The signals are concatenations of 2, 3, or 4 randomly picked consonant-vowel (CV) syllables resulting in artificial non-existing signals (e.g., watopo, nafa, nomomeme). The CV syllables consist of one of eight consonants g, h, k, l, m, n, p, w and one of five vowels a, e, i, o, u. Out of 27 stimuli, only 15 stimuli are used during the guessing, labelling, and communication blocks. All 27 stimuli are used in the testing block. The training stimuli are selected randomly before each simulation, but we ensure that each attribute value is represented equally often across this set.

### 3.2 Simulation blocks

Each simulation consists of four blocks. In the first block, we assess whether agents can guess the right signal when presented with a stimulus. Second, in the labelling block, an agent repeatedly produces a signal for each stimulus given the initial training vocabulary. The signals generated in this block are taken as the learned vocabulary for that agent. In the third block, the agents communicate as described before, taking turns as speaker and listener until all rounds are completed and each stimulus appeared twice per round (i.e., both agents produced a signal for each stimulus and made a guess for each stimulus). In this block, the interaction between the agents slowly alters each agent’s individual vocabulary much like done by [de Boer (2000)](https://arxiv.org/html/2412.07646v1#bib.bib13 ""); [Steels et al. (2012)](https://arxiv.org/html/2412.07646v1#bib.bib55 "") by updating the current stimulus to be associated with the produced signal. After the communication block, the testing block tasks the agents to generate signals for the entire meaning space of 27 stimuli using the training vocabulary that was optimised in the labelling and communication block. Hence, they must generalise their strategies to unseen samples.

### 3.3 LLMs as agents

The LLMs in our experiment were instruction-tuned instantiations of Llama 3 70B [Llama Team (2024)](https://arxiv.org/html/2412.07646v1#bib.bib37 "") with greedy sampling222



Although we only report results on one model type, initial explorations with GPT-3.5 and Llama 2 7B showed similar behaviours to LLama 3 70B. While human participants typically learn signal-meaning mappings through a learning block, we use LLMs’ in-context learning [Brown et al. (2020)](https://arxiv.org/html/2412.07646v1#bib.bib8 "") ability to teach them the languages. Specifically, we prepend our prompts with the items to be learned in a structured JSON-like format (Prompt [2.1](https://arxiv.org/html/2412.07646v1#S2.prompt1 "List of Prompts 2.1 ‣ 2.2 LLMs as models of language ‣ 2 Background & Related work ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). Given the observed behavioural similarities between humans and LLMs [Galke et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib19 ""), we assume that a vocabulary of signal-meaning mappings in the context of a prompt provides enough (distributional) information for a LLM to learn an appropriate mapping between the attributes of the stimuli and signal syllables. Although the prompt structure ’invites’ the LLM to infer a signal from the stimulus attributes, we are agnostic about how exactly and what kind of mapping the LLM deduces, but we are interested in the resulting behaviours.

Throughout a simulation, agents essentially perform one of two tasks: generation or guessing. The labelling block and speaking in the communication block involve generating signals. The guessing block and discrimination in the communication block involve guessing. The prompts for these tasks are extensions of those used by [Galke et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib19 ""), with slight adaptations to enable LLMs to discriminate between stimuli. Given that LLMs show a primacy and recency bias [Liu et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib36 ""), the vocabulary is shuffled before each task such that ordering effects are minimal. System instructions depend on the task performed but are largely similar and chosen to be maximally close to instructions given to humans in experimental settings.

Generating signals. For signal generation in the labelling block, we use prompt completion (Prompt [C.1](https://arxiv.org/html/2412.07646v1#A3.prompt1 "List of Prompts C.1 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). During labelling, the agents see the entire training set and generate a signal for each stimulus, effectively amounting to a look-up task since the stimulus is present in the prompt. On the other hand, the vocabulary presented to agents during communication and testing does not include the current stimulus, thus requiring the agents to extract an appropriate mapping and generalise to new stimuli (Prompt [C.2](https://arxiv.org/html/2412.07646v1#A3.prompt2 "List of Prompts C.2 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). A human-like solution would be to map stimulus attributes (i.e. shape, colour, and amount) to syllables representing these attributes and create compositions that describe the stimulus. During communication, we add a communicativeSuccess attribute which is set to 11 if the previous interaction for this stimulus was successful and zero otherwise. Adding this attribute functions as a memory between interactions and provides a pressure for expressivity. It is hypothesised that the latter plays an important role in human language evolution since it prevents languages from becoming degenerate [Smith et al. (2013)](https://arxiv.org/html/2412.07646v1#bib.bib54 ""). Importantly, during testing, the vocabulary presented to the agents always includes the train set (without the current stimulus), and items from the test set are never present.

Guessing signals or meanings. For guessing and discrimination during communication, the agents need to respond with a choice corresponding to the speaker’s signal. Unfortunately, LLMs are inconsistent and unreliable in answering multiple choice questions [Khatun and Brown (2024)](https://arxiv.org/html/2412.07646v1#bib.bib27 ""). In our initial exploration, this indeed proved to be unusable. Instead, for each distractor (signal or meaning), we run the prompt prefilled with that distractor through the model and select the distractor with the highest probability (Prompt [C.3](https://arxiv.org/html/2412.07646v1#A3.prompt3 "List of Prompts C.3 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). Again, the agents observe the training vocabulary with the current stimulus in the guessing block. In the communication block, agents observe the training vocabulary without the current stimulus.

### 3.4 Metrics

We are firstly interested in investigating whether two agents settle on a language that enables them to communicate, measured by the percentage of successful interactions (PercCom) in a round. We use multiple metrics to measure structure in messages. The most common metric is topographic similarity ( [Brighton and Kirby, 2006](https://arxiv.org/html/2412.07646v1#bib.bib6 ""), TopSim,). Similar to [Kirby et al. (2008)](https://arxiv.org/html/2412.07646v1#bib.bib28 ""), we report Z-scores of the Mantel test [Mantel (1967)](https://arxiv.org/html/2412.07646v1#bib.bib38 "") between signal similarities (normalised Levenshteins distance) and semantic similarities (the number of equal attributes between two meanings). A communication system with a high TopSim uses similar signals for similar meanings. We compute the Ngram diversity [Meister et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib39 ""), being the average fraction of unique vs. total Ngrams for N∈{1,2,3,4,5}N\\in\\{1,2,3,4,5\\} in all produced signals. Low Ngram diversity implies the agents re-use parts of signals in different signals, hinting at compositional signals when it happens in combination with increased TopSim.
We assess the degree of signal systematicity between the signals produced for unseen stimuli in the test block and the previous stimuli in the communication block using the generalisation score ( [Raviv et al., 2021](https://arxiv.org/html/2412.07646v1#bib.bib46 ""), GenScore,). First, we compute the pairwise semantic difference between each stimulus in the train and test scenes, followed by the pairwise normalised edit distance between the signals produced for these scenes. We then take the Pearson correlation between these differences across all stimuli. Intuitively, this measures whether similar scenes across both sets are similarly labelled, thereby suggesting generalisation.

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/combined-TopSim.png)(a) TopSim scores over the agent’s vocabulary in each block and round. The dashed red line indicates the p<.05p<.05 level.

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/combined-NGram.png)(b) Ngram diversity scores over the agent’s vocabulary in each block and round.

Figure 2: Communication clearly increases the structure of the vocabularies, as seen by the increasing TopSim scores and decreasing Ngram diversity.

## 4 Evaluation

We ran 15 simulations, each initialised with a random seed and unique artificial unstructured language. Metrics were computed for each block, except for the generalisation score, which is only computed for the testing block. A human-like result would show increasingly successful interactions and increasing TopSim scores, while Ngram diversity should go down. If this is the case, we expect to observe higher generalisation scores since agents can compose new signals according to a learned structured strategy. We use linear mixed effects models to analyse the results of the communication block to take the random effects of each simulation’s vocabulary into account. The slope (β^\\hat{\\beta}) determines the direction of the effect and the rate of change. Additionally, we use conditional R2R^{2}[Nakagawa and Schielzeth (2013)](https://arxiv.org/html/2412.07646v1#bib.bib42 ""), denoted by Rc2R^{2}\_{c}, which considers fixed and random effects, to show how much variance can be explained by the model. Higher values of Rc2R^{2}\_{c} indicate that the model captures more variance and that correlations are stronger. Finally, we report the marginal Rm2R^{2}\_{m}, which is the variance explained by the fixed effects.

## 5 Results

### 5.1 Learning the artificial languages

We first assess whether LLMs were able to learn the initially unstructured languages. Given the nature of the guessing task, which is essentially a lookup task, unsurprisingly, LLMs were able to guess the correct signals for the stimuli almost perfectly (M=.973,S​D=.031M=.973,SD=.031). However, labelling the same stimuli via completion proved much more difficult (M=.453,S​D=.152M=.453,SD=.152) despite the presence of the correct signal in the prompt. This contrast is in line with work showing that LLM predictions are sensitive to task instructions and how predictions are extracted [Weber et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib62 ""); [Hu and Levy (2023)](https://arxiv.org/html/2412.07646v1#bib.bib25 ""); [Hu and Frank (2024)](https://arxiv.org/html/2412.07646v1#bib.bib24 ""). Additionally, it corroborates using prefilled options in our guessing prompts during communication. Nevertheless, this performance is still better than that of humans333



Preliminary analyses of an ongoing experiment involving humans show that the guessing block is much easier than the labelling block. and is not unimpressive given the vast number of possible signals that can be produced. Finally, the expected struggle to correctly reproduce (i.e., learn) unstructured signals introduces some welcome variation to the agents’ vocabulary which is used at the start of the communication block.

### 5.2 Agents communicate successfully

Once the agents have individually learned the vocabulary, they start communicating. Despite initially starting with different languages, 70%70\\% of the interactions in the first round are successful (chance performance would amount to 25%25\\%). This increases somewhat in the following rounds to ≈75%\\approx 75\\%, but not significantly (Appendix [A](https://arxiv.org/html/2412.07646v1#A1 "Appendix A Communication per round ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models"), Figure [5](https://arxiv.org/html/2412.07646v1#A1.F5 "Figure 5 ‣ Appendix A Communication per round ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). Interestingly, communicative success is not guaranteed, it fluctuates between rounds and in some simulations it even decreases drastically.

### 5.3 Communication results in structure

Although the initial languages are unstructured, some form of structure emerges due to repeated learning and using (Figure [2](https://arxiv.org/html/2412.07646v1#S3.F2 "Figure 2 ‣ 3.4 Metrics ‣ 3 Methodology ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). This mostly happens during the communication block where TopSim increases significantly across rounds (β^=.508±.073,Rc2=.579,Rm2=.355,p<.001\\hat{\\beta}=.508\\pm.073,R^{2}\_{c}=.579,R^{2}\_{m}=.355,p<.001) and Ngram decreases across rounds (β^=−.054±.004,Rc2=.812,Rm2=.558,p<.001\\hat{\\beta}=-.054\\pm.004,R^{2}\_{c}=.812,R^{2}\_{m}=.558,p<.001). However, we also observe behaviour that is not human-like; the signals used to communicate become longer over the rounds (β^=−.557±.044,Rc2=.919,Rm2=.505,p<.001\\hat{\\beta}=-.557\\pm.044,R^{2}\_{c}=.919,R^{2}\_{m}=.505,p<.001). This finding contradicts what is observed in human experiments, where we typically observe that messages become shorter and lie close to a theoretical frontier balancing expressivity and simplicity [Piantadosi et al. (2011)](https://arxiv.org/html/2412.07646v1#bib.bib45 ""); [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 ""). Finally, structured signals, i.e., signals with a higher degree of TopSim, benefit communicative success positively (β^=.035±.007,Rc2=.769,Rm2=.427,p<.001\\hat{\\beta}=.035\\pm.007,R^{2}\_{c}=.769,R^{2}\_{m}=.427,p<.001).

These results extend the findings of [Galke et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib19 "") that LLMs not only learn structured vocabularies better, but also naturally create languages that exhibit some form of structure when it is optimised for their inherent biases. In addition to LLMs’ struggle to learn impossible languages [Kallini et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib26 ""), the insight that reframing prompt instructions into a structured list improves the model response [Mishra et al. (2022)](https://arxiv.org/html/2412.07646v1#bib.bib41 ""), and given that we do not impose pressure to induce structure, this surprising outcome may be the result of an apparent “structure bias” in LLMs.

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/TopSim-GenScore.png)Figure 3: Languages that have evolved to be more structured allow for better generalisation to unseen test stimuli. Colours refer to individual simulations.

### 5.4 Structure enables better generalisation

After the communication block, the agents engage in the final block of the simulation. Here they generate signals for all 27 stimuli using the vocabulary that has evolved after learning and communication. We find that high TopSim languages clearly allow for better generalisation (r=0.735,p<.001r=0.735,p<.001, Figure [3](https://arxiv.org/html/2412.07646v1#S5.F3 "Figure 3 ‣ 5.3 Communication results in structure ‣ 5 Results ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")).

A qualitative inspection of the signals generated in the testing block of the simulation which resulted in the highest TopSim after communication reveals that this agent repeatedly re-uses parts of signals in different compositions (Table [1](https://arxiv.org/html/2412.07646v1#S5.T1 "Table 1 ‣ 5.4 Structure enables better generalisation ‣ 5 Results ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). For example: “su” refers to the amount one, “pepi” to two, “petite” to three. For shape 1, the signals “sunu” and “sutu” are used, “ginu” for shape 2, and shape 3 is referred to with “wipi” or “wipu”. However, colours are less clearly demarcated by unique signal parts. This is also reflected in the ratio of unique signals produced during the test block (M=62.1%,S​D=19.8%M=62.1\\%,SD=19.8\\%), showing that some simulations sometimes result in repetitive use of the same signals for different meanings, resulting in a somewhat degenerate vocabulary. Nevertheless, it is clear that unseen stimuli are often labelled similarly to previously seen stimuli.

| | Shape | Colour | Amount | Word |
| --- | --- | --- | --- | --- |
| train set | 3 | orange | 1 | wipisu |
| 1 | green | 2 | sutupepi |
| 2 | green | 1 | ginisu |
| 3 | green | 1 | wipisu |
| 1 | blue | 2 | sunupepi |
| 1 | green | 3 | sutupitite |
| 2 | orange | 1 | ginusu |
| 3 | blue | 3 | wipipitite |
| 3 | green | 3 | wipupitite |
| 3 | blue | 1 | wipisu |
| 1 | blue | 3 | sunupitite |
| 2 | orange | 3 | ginupitite |
| 2 | blue | 2 | ginupepi |
| 1 | orange | 2 | sunupepi |
| 2 | orange | 2 | ginupepi |
| test set | 1 | orange | 1 | sutisu |
| 1 | orange | 3 | sutupitite |
| 1 | green | 1 | sutusu |
| 1 | blue | 1 | sunusi |
| 2 | green | 2 | ginupepi |
| 2 | green | 3 | ginupitite |
| 2 | blue | 1 | ginisu |
| 2 | blue | 3 | ginupitite |
| 3 | orange | 2 | wipupepi |
| 3 | orange | 3 | wipipitite |
| 3 | green | 2 | wipupepi |
| 3 | blue | 2 | wipupepi |

Table 1: The signals produced in the testing phase of the simulation that resulted in the highest TopSim score (7.13) after communication. The signals for the test stimuli share parts of signals and are composed similarly to train stimuli (G​e​n​S​c​o​r​e=.792GenScore=.792)

## 6 Iterated learning

The previous results showed that two LLMs can successfully communicate and slowly shape the language to become more structured. Provided that cumulative cultural evolution can extrapolate weak biases to have strong effects in socially learned systems like language [Smith (2011)](https://arxiv.org/html/2412.07646v1#bib.bib51 ""), we extend our simulations by adding generations of learners. The first generation is initialised with a random unstructured language described in Section [3.1](https://arxiv.org/html/2412.07646v1#S3.SS1 "3.1 Stimuli and initial languages ‣ 3 Methodology ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models"), but in following generations, agents learn a portion of the signal-meaning mappings produced in the testing block by the agents of the previous generation. Only the vocabulary of the agent with the highest TopSim is transmitted to the next generation. We ran six transmission chains of 8 generations each. The seed generations for each chain were selected randomly from our initial 15 simulations.

### 6.1 Learnability increases

Figure [4](https://arxiv.org/html/2412.07646v1#S6.F4 "Figure 4 ‣ 6.1 Learnability increases ‣ 6 Iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") clearly reveals that the learnability increases. While LLMs in the first generation struggle to look up signals and reproduce them, a single generation learning and using a language tremendously decreases the edit distance between ground truth signals and the produced signals. These results are remarkably similar to findings with human participants [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 ""), and show that the languages are optimised for LLMs’ preferences.

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/LabellingError-Chain.png)Figure 4: The normalised Levenshtein distance between the ground truth and the produced signal in the learning block. Solid lines indicate chains, dashed blue line indicates the average Levenshtein distance across chains.

### 6.2 Communicative success and non-humanlike structures

Despite the increase in learnability, we do not observe an increase in communicative success due to iterated learning (Appendix [B](https://arxiv.org/html/2412.07646v1#A2 "Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") Figure [6](https://arxiv.org/html/2412.07646v1#A2.F6 "Figure 6 ‣ Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). Possibly, this is due to the already high scores of the first generation. Despite their increased learnability, the signals become significantly longer and more ambiguous. We take this non-humanlike solution to be an artefact of an absence of pressures for memorisation in LLMs’. While human language is optimised to be compressible and expressive [Fedzechkina et al. (2012)](https://arxiv.org/html/2412.07646v1#bib.bib16 ""); [Tamariz and Kirby (2015)](https://arxiv.org/html/2412.07646v1#bib.bib56 ""); [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 ""), context windows of LLMs, are considerably larger. In our case, Llama 3 70B has a context window of 8.2K tokens, which we do not exceed.

Finally, the metrics to measure structure display a mixed picture. TopSim, does increase but not significantly across generations (Figure [7](https://arxiv.org/html/2412.07646v1#A2.F7 "Figure 7 ‣ Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") and Table [2](https://arxiv.org/html/2412.07646v1#A2.T2 "Table 2 ‣ Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") in appendix [B](https://arxiv.org/html/2412.07646v1#A2 "Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")) but Ngram diversity decreases significantly across generations. Qualitative inspections of several vocabularies show that some languages evolve into degenerate languages with repeating signals for different stimuli (i.e., underspecification). Corroborated by a significantly lower number of uniquely produced signals in the last generation compared to the first simulation (t⁡(5)=2.64,p=.046,Mg​e​n​0=.707,S​Dg​e​n​0=.142,Mg​e​n​7=.519,S​Dg​e​n​7=.119t(5)=2.64,p=.046,M\_{gen0}=.707,SD\_{gen0}=.142,M\_{gen7}=.519,SD\_{gen7}=.119). Together this causes the Ngram diversity to be lower while clearly hurting communicative expressiveness. Even though degenerate languages are not uncommon in iterated learning experiments with humans ( [Kirby et al., 2008](https://arxiv.org/html/2412.07646v1#bib.bib28 ""), e.g., experiment 1 in), an additional pressure for expressivity typically prevents languages from becoming underspecified. Given the expressivity pressure that we expect to result from the communication block, we expected to see less underspecification. Iterated learning therefore results in vocabularies optimised for LLM agents but do so in a non-humanlike way.

## 7 Discussion

Our findings show a mixed picture, agents comprised of LLMs can learn and use artificial languages in a referential game. They do so by optimising the initially holistic vocabulary to fit better with the preferences of their language model, resulting in increased regularity and structure (Table [1](https://arxiv.org/html/2412.07646v1#S5.T1 "Table 1 ‣ 5.4 Structure enables better generalisation ‣ 5 Results ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models")). Yet, we also observe some degeneracy, i.e. many-to-one mappings of signals and attributes, and non-humanlike behaviours such as a tendency to produce long signals. Iterated learning further increases the learnability of the vocabulary but also extrapolates these behaviours further. Despite not being able to directly compare our results to human data, these findings are loosely comparable to earlier work involving human participants [Kirby et al. (2015)](https://arxiv.org/html/2412.07646v1#bib.bib29 ""); [Raviv et al. (2019b)](https://arxiv.org/html/2412.07646v1#bib.bib48 "") in which languages with similar properties emerge.

Table [1](https://arxiv.org/html/2412.07646v1#S5.T1 "Table 1 ‣ 5.4 Structure enables better generalisation ‣ 5 Results ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") suggests that certain attributes, such as the colour attribute, in the inputs may be ignored, possibly due to the primacy and recency bias in LLMs [Liu et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib36 ""). Optimising the instructive sentences by choosing sentences that maximise the fraction of valid model answers for each task, as suggested by [Aher et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib2 ""), may alleviate these ignorances and increase focus on relevant attributes. It is also possible that the LLMs do not ‘experience’ enough pressure to be understood by other agents, i.e., the communicativeSuccess attribute is not able to force a need to be expressive, which is deemed an essential pressure in computational simulations for human-like structures [Galke and Raviv (2024)](https://arxiv.org/html/2412.07646v1#bib.bib20 ""). Despite these discrepancies, it is nevertheless interesting that some form of structure emerges.

Our results further show variability between generations of learners. This is not uncommon in human experiments where processes of interaction and transmission sometimes generate fully systematic, compositional languages, but can also result in systems that lack structure entirely [Verhoef et al. (2022)](https://arxiv.org/html/2412.07646v1#bib.bib60 ""). Differences in personal biases may be a contributing factor to these differences [Kouwenhoven et al. (2022a)](https://arxiv.org/html/2412.07646v1#bib.bib30 ""). Since we do not initialise agents with different biases, these variations, originating in distributional information of the prepended vocabularies, are a natural human-like outcome of repeated exposure to and use of the language.

The evolution of degenerate vocabularies could be explained by the use of greedy decoding during signal generation, which does not necessarily produce the most human-like text [Holtzman et al. (2020)](https://arxiv.org/html/2412.07646v1#bib.bib23 ""); [Meister et al. (2022)](https://arxiv.org/html/2412.07646v1#bib.bib40 ""); [Meister et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib39 "") and may therefore also result in non-humanlike composition. Moreover, once an agent, perhaps mistakingly, duplicates a signal, its raw probabilities are increased when producing the next utterance, possibly resulting in a feedback loop that collapses onto a degenerate vocabulary. This effect may be further increased due to LLMs’ inability to innovate [Bender et al. (2021)](https://arxiv.org/html/2412.07646v1#bib.bib4 ""); [Yiu et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib64 "") and the choice of structured prompts that do not explicitly ask for innovation. Future work could attempt to increase the composition of novel signals by increasing the temperature parameter. Perhaps resulting in slightly more novel outputs as this forces exploration of the vocabulary embedding space [Peeperkorn et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib44 ""), possibly alleviating the evolution of degenerate vocabularies and shifting the optimisation of the language to different solutions.

The rapid increase in learnability resulting from iterated learning proves that weak learning biases in language models, such as, for example, an observed simplicity bias [Chen et al. (2024)](https://arxiv.org/html/2412.07646v1#bib.bib10 ""), can be amplified by the process of generational transmission. Additional simulations with increased communicative difficulty, e.g., by increasing the number of distractors or the number of interaction partners, could reveal whether and how some form of memory constraint affects the learnability of the languages. Doing so additionally captures the diversity and dynamic nature of language in the real world. In general, systematic manipulations across model features (e.g., size, training data, or decoding strategies) may expose why we observe tendencies such as producing longer signals. Similar to what was proposed by [Galke and Raviv (2024)](https://arxiv.org/html/2412.07646v1#bib.bib20 ""), we argue that careful manipulation of our setup can help reveal underlying mechanistic biases of language models and inform modelling choices when simulating language acquisition in LLMs. Taking into account the important role communication plays in shaping human language, LLM performance drastically increased when it was optimised for successful communication through reinforcement learning from human feedback.

Finally, we acknowledge that our results depend on many methodological considerations, such as the prompt format, task instructions, and the tokenisation process. However, our primary goal was to investigate whether LLMs can be used in simulations of artificial language emergence. We aimed to stay maximally close to well-known experimental methods in the field of language emergence and did not optimise for performance, human-like results, or compositional vocabularies. Instead, our goal was to reveal LLMs’ natural behaviours resulting from learning and using artificial languages. Future work could extend our findings by performing experiments in which humans collaborate with LLMs to investigate whether languages can evolve that are optimised for human and LLM preferences.

## 8 Conclusion

Given the remarkable linguistic abilities of recent LLMs, we show how they behave in a classical referential game in which artificial languages, typically used in the field of language evolution, are learned and used. Primarily, our results suggest that LLMs can be used as artificial language learners to investigate the evolution of language. We show that initially unstructured languages are optimised for improved learnability and allow for successful communication. While we found some evidence of human-like compositional structures that enhance generalization abilities, we also identified notable differences in behavioural characteristics of LLMs in comparison to humans. Notably, iterated learning processes increased vocabulary learnability but also amplified such different characteristics further. As such, we extend existing research by revealing that structured languages are not merely easier for LLMs to learn. Critically, the inherent biases of LLMs also shape unstructured languages towards increased regularity. These findings contribute to a deeper understanding of how LLMs process and evolve language, potentially bridging the gap between computational models and natural language evolution. Finally, we hope to have shown that our setup is useful in exposing the underlying mechanistic biases of LLMs and demystifying their uninterpretable nature.

## Acknowledgments

We wish to thank Bram van Dijk for his comments on an early draft of this paper and the helpful discussions.

## References

- Acerbi and Stubbersfield (2023)
Alberto Acerbi and Joseph M. Stubbersfield. 2023.

[Large language models show human-like content biases in transmission chain experiments](https://doi.org/10.1073/pnas.2313790120 "").

_Proceedings of the National Academy of Sciences_, 120(44):e2313790120.

- Aher et al. (2023)
Gati V Aher, Rosa I. Arriaga, and Adam Tauman Kalai. 2023.

[Using large language models to simulate multiple humans and replicate human subject studies](https://proceedings.mlr.press/v202/aher23a.html "").

In _Proceedings of the 40th International Conference on Machine Learning_, volume 202 of _Proceedings of Machine Learning Research_, pages 337–371. PMLR.

- Arnon and Kirby (2024)
Inbal Arnon and Simon Kirby. 2024.

[Cultural evolution creates the statistical structure of language](https://doi.org/10.1038/s41598-024-56152-9 "").

_Scientific Reports_, 14(1):5255.

- Bender et al. (2021)
Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021.

[On the dangers of stochastic parrots: Can language models be too big?](https://doi.org/10.1145/3442188.3445922 "")In _Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency_, FAccT ’21, page 610–623, New York, NY, USA. Association for Computing Machinery.

- Boyd et al. (1996)
Robert Boyd, Peter J Richerson, et al. 1996.

Why culture is common, but cultural evolution is rare.

In _Proceedings-british academy_, volume 88, pages 77–94. Oxford University Press Inc.

- Brighton and Kirby (2006)
Henry Brighton and Simon Kirby. 2006.

[Understanding linguistic evolution by visualizing the emergence of topographic mappings](https://doi.org/10.1162/artl.2006.12.2.229 "").

_Artificial Life_, 12(2):229–242.

- Brinkmann et al. (2023)
Levin Brinkmann, Fabian Baumann, Jean-François Bonnefon, Maxime Derex, Thomas F Müller, Anne-Marie Nussberger, Agnieszka Czaplicka, Alberto Acerbi, Thomas L Griffiths, Joseph Henrich, et al. 2023.

[Machine culture](https://doi.org/10.1038/s41562-023-01742-2 "").

_Nature Human Behaviour_, 7(11):1855–1868.

- Brown et al. (2020)
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020.

[Language models are few-shot learners](https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf "").

In _Advances in Neural Information Processing Systems_, volume 33, pages 1877–1901. Curran Associates, Inc.

- Carr et al. (2017)
Jon W. Carr, Kenny Smith, Hannah Cornish, and Simon Kirby. 2017.

[The cultural evolution of structured languages in an open-ended, continuous world](https://doi.org/10.1111/cogs.12371 "").

_Cognitive Science_, 41(4):892–923.

- Chen et al. (2024)
Angelica Chen, Ravid Shwartz-Ziv, Kyunghyun Cho, Matthew L Leavitt, and Naomi Saphra. 2024.

[Sudden drops in the loss: Syntax acquisition, phase transitions, and simplicity bias in MLMs](https://openreview.net/forum?id=MO5PiKHELW "").

In _The Twelfth International Conference on Learning Representations_.

- Christiansen and Chater (2008)
Morten H. Christiansen and Nick Chater. 2008.

[Language as shaped by the brain](https://doi.org/10.1017/S0140525X08004998 "").

_Behavioral and Brain Sciences_, 31(5):489–509.

- Culbertson and Smolensky (2012)
Jennifer Culbertson and Paul Smolensky. 2012.

[A bayesian model of biases in artificial language learning: The case of a word-order universal](https://doi.org/10.1111/j.1551-6709.2012.01264.x "").

_Cognitive Science_, 36(8):1468–1498.

- de Boer (2000)
Bart de Boer. 2000.

[Self-organization in vowel systems](https://doi.org/10.1006/jpho.2000.0125 "").

_Journal of Phonetics_, 28(4):441–465.

- de Boer (2006)
Bart de Boer. 2006.

[_Computer modelling as a tool for understanding language evolution_](https://doi.org/10.1007/1-4020-3395-8_17 ""), pages 381–406.

Springer Netherlands, Dordrecht.

- Dillion et al. (2023)
Danica Dillion, Niket Tandon, Yuling Gu, and Kurt Gray. 2023.

[Can ai language models replace human participants?](https://doi.org/10.1016/j.tics.2023.04.008 "")_Trends in Cognitive Sciences_, 27(7):597–600.

- Fedzechkina et al. (2012)
Maryia Fedzechkina, T. Florian Jaeger, and Elissa L. Newport. 2012.

[Language learners restructure their input to facilitate efficient communication](https://doi.org/10.1073/pnas.1215776109 "").

_Proceedings of the National Academy of Sciences_, 109(44):17897–17902.

- Galantucci (2005)
Bruno Galantucci. 2005.

[An experimental study of the emergence of human communication systems](https://doi.org/10.1207/s15516709cog0000_34 "").

_Cognitive Science_, 29(5):737–767.

- Galke et al. (2022)
Lukas Galke, Yoav Ram, and Limor Raviv. 2022.

[Emergent communication for understanding human language evolution: What’s missing?](https://openreview.net/forum?id=rqUGZQ-0XZ5 "")In _Emergent Communication Workshop at ICLR 2022_.

- Galke et al. (2023)
Lukas Galke, Yoav Ram, and Limor Raviv. 2023.

What makes a language easy to deep-learn?

_arXiv preprint arXiv:2302.12239_.

- Galke and Raviv (2024)
Lukas Galke and Limor Raviv. 2024.

[Learning and communication pressures in neural networks: Lessons from emergent communication](https://doi.org/10.34842/3vr5-5r49 "").

_Language Development Research_, 5(1):116–143.

- Griffiths and Kalish (2007)
Thomas L. Griffiths and Michael L. Kalish. 2007.

[Language evolution by iterated learning with bayesian agents](https://doi.org/10.1080/15326900701326576 "").

_Cognitive Science_, 31(3):441–480.

- Hockett (1960)
Charles F. Hockett. 1960.

[The origin of speech](https://www.jstor.org/stable/24940617 "").

_Scientific American_, 203(3):88–97.

- Holtzman et al. (2020)
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. 2020.

[The curious case of neural text degeneration](https://openreview.net/forum?id=rygGQyrFvH "").

In _International Conference on Learning Representations_.

- Hu and Frank (2024)
Jennifer Hu and Michael Frank. 2024.

[Auxiliary task demands mask the capabilities of smaller language models](https://openreview.net/forum?id=U5BUzSn4tD "").

In _First Conference on Language Modeling_.

- Hu and Levy (2023)
Jennifer Hu and Roger Levy. 2023.

[Prompting is not a substitute for probability measurements in large language models](https://doi.org/10.18653/v1/2023.emnlp-main.306 "").

In _Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing_, pages 5040–5060, Singapore. Association for Computational Linguistics.

- Kallini et al. (2024)
Julie Kallini, Isabel Papadimitriou, Richard Futrell, Kyle Mahowald, and Christopher Potts. 2024.

[Mission: Impossible language models](https://doi.org/10.18653/v1/2024.acl-long.787 "").

In _Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pages 14691–14714, Bangkok, Thailand. Association for Computational Linguistics.

- Khatun and Brown (2024)
Aisha Khatun and Daniel G Brown. 2024.

[A study on large language models’ limitations in multiple-choice question answering](https://arxiv.org/abs/2401.07955 "").

_Preprint_, arXiv:2401.07955.

- Kirby et al. (2008)
Simon Kirby, Hannah Cornish, and Kenny Smith. 2008.

[Cumulative cultural evolution in the laboratory: An experimental approach to the origins of structure in human language](https://doi.org/10.1073/pnas.0707835105 "").

_Proceedings of the National Academy of Sciences_, 105(31):10681–10686.

- Kirby et al. (2015)
Simon Kirby, Monica Tamariz, Hannah Cornish, and Kenny Smith. 2015.

[Compression and communication in the cultural evolution of linguistic structure](https://doi.org/10.1016/j.cognition.2015.03.016 "").

_Cognition_, 141:87–102.

- Kouwenhoven et al. (2022a)
Tom Kouwenhoven, Roy De Kleijn, Stephan Raaijmakers, and Tessa Verhoef. 2022a.

Need for structure and the emergence of communication.

In _Proceedings of the Annual Meeting of the Cognitive Science Society_, volume 44.

- Kouwenhoven et al. (2024)
Tom Kouwenhoven, Max Peeperkorn, Bram Van Dijk, and Tessa Verhoef. 2024.

[The curious case of representational alignment: Unravelling visio-linguistic tasks in emergent communication](https://doi.org/10.18653/v1/2024.cmcl-1.5 "").

In _Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics_, pages 57–71, Bangkok, Thailand. Association for Computational Linguistics.

- Kouwenhoven et al. (2022b)
Tom Kouwenhoven, Tessa Verhoef, Roy De Kleijn, and Stephan Raaijmakers. 2022b.

[Emerging grounded shared vocabularies between human and machine, inspired by human language evolution](https://doi.org/10.3389/frai.2022.886349 "").

_Frontiers in Artificial Intelligence_, 5:886349.

- Lazaridou and Baroni (2020)
Angeliki Lazaridou and Marco Baroni. 2020.

[Emergent multi-agent communication in the deep learning era](https://arxiv.org/abs/2006.02419 "").

_Preprint_, arXiv:2006.02419.

- Lian et al. (2023)
Yuchen Lian, Arianna Bisazza, and Tessa Verhoef. 2023.

[Communication Drives the Emergence of Language Universals in Neural Agents: Evidence from the Word-order/Case-marking Trade-off](https://doi.org/10.1162/tacl_a_00587 "").

_Transactions of the Association for Computational Linguistics_, 11:1033–1047.

- Lian et al. (2024)
Yuchen Lian, Tessa Verhoef, and Arianna Bisazza. 2024.

[Nellcom-x: A comprehensive neural-agent framework to simulate language learning and group communication](https://arxiv.org/abs/2407.13999 "").

_Preprint_, arXiv:2407.13999.

- Liu et al. (2024)
Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024.

[Lost in the middle: How language models use long contexts](https://doi.org/10.1162/tacl_a_00638 "").

_Transactions of the Association for Computational Linguistics_, 12:157–173.

- Llama Team (2024)
Meta Llama Team. 2024.

[The llama 3 herd of models](https://arxiv.org/abs/2407.21783 "").

_Preprint_, arXiv:2407.21783.

- Mantel (1967)
Nathan Mantel. 1967.

The detection of disease clustering and a generalized regression approach.

_Cancer research_, 27(2\_Part\_1):209–220.

- Meister et al. (2023)
Clara Meister, Tiago Pimentel, Gian Wiher, and Ryan Cotterell. 2023.

[Locally typical sampling](https://doi.org/10.1162/tacl_a_00536 "").

_Transactions of the Association for Computational Linguistics_, 11:102–121.

- Meister et al. (2022)
Clara Meister, Gian Wiher, Tiago Pimentel, and Ryan Cotterell. 2022.

[On the probability–quality paradox in language generation](https://doi.org/10.18653/v1/2022.acl-short.5 "").

In _Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)_, pages 36–45, Dublin, Ireland. Association for Computational Linguistics.

- Mishra et al. (2022)
Swaroop Mishra, Daniel Khashabi, Chitta Baral, Yejin Choi, and Hannaneh Hajishirzi. 2022.

[Reframing instructional prompts to GPTk’s language](https://doi.org/10.18653/v1/2022.findings-acl.50 "").

In _Findings of the Association for Computational Linguistics: ACL 2022_, pages 589–612, Dublin, Ireland. Association for Computational Linguistics.

- Nakagawa and Schielzeth (2013)
Shinichi Nakagawa and Holger Schielzeth. 2013.

[A general and simple method for obtaining r2 from generalized linear mixed-effects models](https://doi.org/10.1111/j.2041-210x.2012.00261.x "").

_Methods in Ecology and Evolution_, 4(2):133–142.

- Park et al. (2023)
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023.

[Generative agents: Interactive simulacra of human behavior](https://doi.org/10.1145/3586183.3606763 "").

In _Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology_, UIST ’23, New York, NY, USA. Association for Computing Machinery.

- Peeperkorn et al. (2024)
Max Peeperkorn, Tom Kouwenhoven, Dan Brown, and Anna Jordanous. 2024.

Is temperature the creativity parameter of large language models?

In _15th International Conference on Computational Creativity_. Association for Computational Creativity.

- Piantadosi et al. (2011)
Steven T. Piantadosi, Harry Tily, and Edward Gibson. 2011.

[Word lengths are optimized for efficient communication](https://doi.org/10.1073/pnas.1012551108 "").

_Proceedings of the National Academy of Sciences_, 108(9):3526–3529.

- Raviv et al. (2021)
Limor Raviv, Marianne de Heer Kloots, and Antje Meyer. 2021.

[What makes a language easy to learn? a preregistered study on how systematic structure and community size affect language learnability](https://doi.org/10.1016/j.cognition.2021.104620 "").

_Cognition_, 210:104620.

- Raviv et al. (2019a)
Limor Raviv, Antje Meyer, and Shiri Lev-Ari. 2019a.

[Compositional structure can emerge without generational transmission](https://doi.org/10.1016/j.cognition.2018.09.010 "").

_Cognition_, 182:151–164.

- Raviv et al. (2019b)
Limor Raviv, Antje Meyer, and Shiri Lev-Ari. 2019b.

[Larger communities create more systematic languages](https://doi.org/10.1098/rspb.2019.1262 "").

_Proceedings of the Royal Society B: Biological Sciences_, 286(1907):20191262.

- Scott-Phillips et al. (2009)
Thomas C. Scott-Phillips, Simon Kirby, and Graham R.S. Ritchie. 2009.

[Signalling signalhood and the emergence of communication](https://doi.org/10.1016/j.cognition.2009.08.009 "").

_Cognition_, 113(2):226–233.

- Shumailov et al. (2024)
Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.

[Ai models collapse when trained on recursively generated data](https://doi.org/10.1038/s41586-024-07566-y "").

_Nature_, 631(8022):755–759.

- Smith (2011)
Kenny Smith. 2011.

[Learning Bias, Cultural Evolution of Language, and theBiological Evolution of the Language Faculty](https://doi.org/10.3378/027.083.0207 "").

_Human Biology_, 83(2):261 – 278.

- Smith (2022)
Kenny Smith. 2022.

[How Language Learning and Language Use Create Linguistic Structure](https://doi.org/10.1177/09637214211068127 "").

_Current Directions in Psychological Science_, 31(2):177–186.

- Smith et al. (2024)
Kenny Smith, Simon Kirby, Shangmin Guo, and Thomas L Griffiths. 2024.

[Ai model collapse might be prevented by studying human language transmission](https://doi.org/10.1038/d41586-024-03023-y "").

_Nature_, 633(8030):525.

- Smith et al. (2013)
Kenny Smith, Monica Tamariz, and Simon Kirby. 2013.

Linguistic structure is an evolutionary trade-off between simplicity and expressivity.

In _Proceedings of the annual meeting of the cognitive science society_, volume 35.

- Steels et al. (2012)
Luc Steels, Martin Loetzsch, et al. 2012.

The grounded naming game.

_Experiments in cultural language evolution_, 3:41–59.

- Tamariz and Kirby (2015)
Mónica Tamariz and Simon Kirby. 2015.

[Culture: Copying, compression, and conventionality](https://doi.org/10.1111/cogs.12144 "").

_Cognitive Science_, 39(1):171–183.

- Tomasello (1999)
Michael Tomasello. 1999.

[_The Cultural Origins of Human Cognition_](http://www.jstor.org/stable/j.ctvjsf4jc "").

Harvard University Press.

- van Dijk et al. (2023)
Bram van Dijk, Tom Kouwenhoven, Marco Spruit, and Max Johannes van Duijn. 2023.

[Large language models: The need for nuance in current debates and a pragmatic perspective on understanding](https://doi.org/10.18653/v1/2023.emnlp-main.779 "").

In _Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing_, pages 12641–12654, Singapore. Association for Computational Linguistics.

- Verhoef (2012)
Tessa Verhoef. 2012.

[The origins of duality of patterning in artificial whistled languages](https://doi.org/10.1515/langcog-2012-0019 "").

_Language and Cognition_, 4(4):357–380.

- Verhoef et al. (2022)
Tessa Verhoef, Esther Walker, and Tyler Marghetis. 2022.

[Interaction dynamics affect the emergence of compositional structure in cultural transmission of space-time mappings](https://escholarship.org/uc/item/7vj8b55x "").

In _Proceedings of the Annual Meeting of the Cognitive Science Society_, volume 44, pages 2133–2139.

- Warstadt and Bowman (2022)
Alex Warstadt and Samuel R Bowman. 2022.

What artificial neural networks can tell us about human language acquisition.

_Algebraic Structures in Natural Language_, pages 17–60.

- Weber et al. (2023)
Lucas Weber, Elia Bruni, and Dieuwke Hupkes. 2023.

[Mind the instructions: a holistic evaluation of consistency and interactions in prompt-based learning](https://doi.org/10.18653/v1/2023.conll-1.20 "").

In _Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL)_, pages 294–313, Singapore. Association for Computational Linguistics.

- Wilcox et al. (2023)
Ethan Gotlieb Wilcox, Richard Futrell, and Roger Levy. 2023.

[Using Computational Models to Test Syntactic Learnability](https://doi.org/10.1162/ling_a_00491 "").

_Linguistic Inquiry_, pages 1–44.

- Yiu et al. (2024)
Eunice Yiu, Eliza Kosoy, and Alison Gopnik. 2024.

[Transmission versus truth, imitation versus innovation: What children can do that large language and language-and-vision models cannot (yet)](https://doi.org/10.1177/17456916231201401 "").

_Perspectives on Psychological Science_, 19(5):874–883.

PMID: 37883796.

- Zhang et al. (2024)
Yuqing Zhang, Tessa Verhoef, Gertjan van Noord, and Arianna Bisazza. 2024.

[Endowing neural language learners with human-like biases: A case study on dependency length minimization](https://aclanthology.org/2024.lrec-main.516 "").

In _Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)_, pages 5819–5832, Torino, Italia. ELRA and ICCL.

- Zheng et al. (2024)
Chenhao Zheng, Jieyu Zhang, Aniruddha Kembhavi, and Ranjay Krishna. 2024.

Iterated learning improves compositionality in large vision-language models.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, pages 13785–13795.


## Appendix A Communication per round

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/PercCom-roundId-lines.png)Figure 5: The communicative success over the communication rounds. Each line indicates a simulation, the dashed blue line is the average with bars indicating the 95% confidence interval. The dashed red line indicates chance performance.

## Appendix B Additional results iterated learning

![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/CommSucces-Chain.png)Figure 6: The average communicative success across rounds for each generation. Each line indicates a chain, and the dashed blue line is the average with bars indicating the 95% confidence interval. See Table [2](https://arxiv.org/html/2412.07646v1#A2.T2 "Table 2 ‣ Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models").![Refer to caption](https://arxiv.org/html/2412.07646v1/figures/TopSim-Chain.png)Figure 7: The evolution of our structure metrics on the words produced in the testing block. Each line indicates a chain, and the dashed blue line is the average with bars indicating the 95% confidence interval. See Table [2](https://arxiv.org/html/2412.07646v1#A2.T2 "Table 2 ‣ Appendix B Additional results iterated learning ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models").

| | t⁡(5)t(5) | pp | Mg​e​n​0M\_{gen0} | S​Dg​e​n​0SD\_{gen0} | Mg​e​n​7M\_{gen7} | S​Dg​e​n​7SD\_{gen7} |
| --- | --- | --- | --- | --- | --- | --- |
| TopSim | -1.42 | .215 | 9.62 | 1.21 | 10.5 | 1.77 |
| Ngram | 2.83 | .037 | .158 | .074 | .071 | .025 |

Table 2: Paired t-tests shows that Ngram does significantly change resulting from generational transmission, while TopSim does not.

## Appendix C Prompts

Our agents act based on prompts and system instructions. These are designed to be maximally close to the classical experimental setup formatted similar to [Galke et al. (2023)](https://arxiv.org/html/2412.07646v1#bib.bib19 ""). The completion prompt [C.1](https://arxiv.org/html/2412.07646v1#A3.prompt1 "List of Prompts C.1 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") is used for labelling and guessing. For the latter task, we prefill the word and pick the word with the highest probability. See Prompts [C.1](https://arxiv.org/html/2412.07646v1#A3.prompt1 "List of Prompts C.1 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models"), [C.2](https://arxiv.org/html/2412.07646v1#A3.prompt2 "List of Prompts C.2 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models"), and [C.3](https://arxiv.org/html/2412.07646v1#A3.prompt3 "List of Prompts C.3 ‣ Appendix C Prompts ‣ Searching for Structure: Investigating Emergent Communication with Large Language Models") below.

[⬇](data:text/plain;base64,PHxiZWdpbl9vZl90ZXh0fD48fHN0YXJ0X2hlYWRlcl9pZHw+c3lzdGVtPHxlbmRfaGVhZGVyX2lkfD4gWW91IGFyZSBhIGxhbmd1YWdlIGxlYXJuZXIgd2hvIGhhcyB0byBsZWFybiBhbiBhcnRpZmljaWFsIGxhbmd1YWdlIHdpdGggd29yZHMgYW5kIHRoZWlyIGNvcnJlc3BvbmRpbmcgZmVhdHVyZXMuIFlvdXIgdGFzayBpcyB0byBjb21wbGV0ZSB0aGUgdm9jYWJ1bGFyeSBieSBnZW5lcmF0aW5nIGEgd29yZCB0aGF0IGRlc2NyaWJlcyB0aGUgbGFzdCBpdGVtLiBPbmx5IHJlc3BvbmQgd2l0aCB0aGUgd29yZC48fGVvdF9pZHw+PHxzdGFydF9oZWFkZXJfaWR8PnVzZXI8fGVuZF9oZWFkZXJfaWR8PgoKeydzaGFwZSc6MiwnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzoxLCd3b3JkJzonZ2luaXdpdGUnfQp7J3NoYXBlJzozLCdjb2xvdXInOidncmVlbicsJ2Ftb3VudCc6MSwnd29yZCc6J2dpbmlzdSd9Cnsnc2hhcGUnOjEsJ2NvbG91cic6J29yYW5nZScsJ2Ftb3VudCc6Miwnd29yZCc6J3BpbmlzdWdpJ30KeydzaGFwZSc6MywnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjMsJ3dvcmQnOidzdXRlcGknfQp7J3NoYXBlJzoyLCdjb2xvdXInOidvcmFuZ2UnLCdhbW91bnQnOjIsJ3dvcmQnOid3aW5pc3UnfQp7J3NoYXBlJzozLCdjb2xvdXInOidvcmFuZ2UnLCdhbW91bnQnOjEsJ3dvcmQnOiduaXdpJ30KeydzaGFwZSc6MSwnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6Miwnd29yZCc6J3N1dHV3aXRlJ30KeydzaGFwZSc6MSwnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6Mywnd29yZCc6J3R1cGl0ZW5lJ30KeydzaGFwZSc6MywnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6MSwnd29yZCc6J3dpcGluZXBpJ30KeydzaGFwZSc6MiwnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzozLCd3b3JkJzonZ2lnaSd9Cnsnc2hhcGUnOjEsJ2NvbG91cic6J2dyZWVuJywnYW1vdW50JzoyLCd3b3JkJzonbml0ZSd9Cnsnc2hhcGUnOjMsJ2NvbG91cic6J2JsdWUnLCdhbW91bnQnOjMsJ3dvcmQnOid3aXRlJ30KeydzaGFwZSc6MSwnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjMsJ3dvcmQnOidzdW5lJ30KeydzaGFwZSc6MiwnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6Miwnd29yZCc6J25pbmVuZSd9Cnsnc2hhcGUnOjIsJ2NvbG91cic6J2dyZWVuJywnYW1vdW50JzoxLCd3b3JkJzondHVzZXRldHUnfQp7J3NoYXBlJzoxLCdjb2xvdXInOidncmVlbicsJ2Ftb3VudCc6Mywnd29yZCc6Jzx8ZW90X2lkfD48fHN0YXJ0X2hlYWRlcl9pZHw+YXNzaXN0YW50PHxlbmRfaGVhZGVyX2lkfD4KW0NPTVBMRVRJT04gT1IgUFJFRkZJTEVEXQ==)

<\|begin\_of\_text\|><\|start\_header\_id\|>system<\|end\_header\_id\|>Youarealanguagelearnerwhohastolearnanartificiallanguagewithwordsandtheircorrespondingfeatures.Yourtaskistocompletethevocabularybygeneratingawordthatdescribesthelastitem.Onlyrespondwiththeword.<\|eot\_id\|><\|start\_header\_id\|>user<\|end\_header\_id\|>

{’shape’:2,’colour’:’orange’,’amount’:1,’word’:’giniwite’}

{’shape’:3,’colour’:’green’,’amount’:1,’word’:’ginisu’}

{’shape’:1,’colour’:’orange’,’amount’:2,’word’:’pinisugi’}

{’shape’:3,’colour’:’green’,’amount’:3,’word’:’sutepi’}

{’shape’:2,’colour’:’orange’,’amount’:2,’word’:’winisu’}

{’shape’:3,’colour’:’orange’,’amount’:1,’word’:’niwi’}

{’shape’:1,’colour’:’blue’,’amount’:2,’word’:’sutuwite’}

{’shape’:1,’colour’:’blue’,’amount’:3,’word’:’tupitene’}

{’shape’:3,’colour’:’blue’,’amount’:1,’word’:’wipinepi’}

{’shape’:2,’colour’:’orange’,’amount’:3,’word’:’gigi’}

{’shape’:1,’colour’:’green’,’amount’:2,’word’:’nite’}

{’shape’:3,’colour’:’blue’,’amount’:3,’word’:’wite’}

{’shape’:1,’colour’:’green’,’amount’:3,’word’:’sune’}

{’shape’:2,’colour’:’blue’,’amount’:2,’word’:’ninene’}

{’shape’:2,’colour’:’green’,’amount’:1,’word’:’tusetetu’}

{’shape’:1,’colour’:’green’,’amount’:3,’word’:’<\|eot\_id\|><\|start\_header\_id\|>assistant<\|end\_header\_id\|>

\[COMPLETIONORPREFFILED\]

List of Prompts C.1 Completion Prompt used for labelling and guessing.

[⬇](data:text/plain;base64,PHxiZWdpbl9vZl90ZXh0fD48fHN0YXJ0X2hlYWRlcl9pZHw+c3lzdGVtPHxlbmRfaGVhZGVyX2lkfD4gWW91IGFyZSBhIGxhbmd1YWdlIGxlYXJuZXIgd2hvIGhhcyB0byBsZWFybiBhbiBhcnRpZmljaWFsIGxhbmd1YWdlIHdpdGggd29yZHMgYW5kIHRoZWlyIGNvcnJlc3BvbmRpbmcgZmVhdHVyZXMuIFlvdXIgdGFzayBpcyB0byBnZW5lcmF0ZSBhIHdvcmQgc3VjaCB0aGF0IHlvdXIgY29tbXVuaWNhdGlvbiBwYXJ0bmVyIGNhbiBndWVzcyB0aGUgY29ycmVjdCBtZWFuaW5nIG9mIHRoZSB3b3JkLiBDb21tdW5pY2F0aXZlIHN1Y2Nlc3MgaXMgaW1wb3J0YW50LiBPbmx5IHJlc3BvbmQgd2l0aCB0aGUgd29yZC48fGVvdF9pZHw+PHxzdGFydF9oZWFkZXJfaWR8PnVzZXI8fGVuZF9oZWFkZXJfaWR8PgoKeydzaGFwZSc6MSwnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjMsJ3dvcmQnOidzdXR1cGl0aXRlJywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnc2hhcGUnOjIsJ2NvbG91cic6J29yYW5nZScsJ2Ftb3VudCc6Miwnd29yZCc6J2dpbnVwZXBpJywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnc2hhcGUnOjEsJ2NvbG91cic6J29yYW5nZScsJ2Ftb3VudCc6Miwnd29yZCc6J3N1dHVwZXBpJywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnc2hhcGUnOjEsJ2NvbG91cic6J2dyZWVuJywnYW1vdW50JzoyLCd3b3JkJzonc3V0dXBlcGknLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MH0KeydzaGFwZSc6MiwnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzoxLCd3b3JkJzonZ2luaXN1JywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnc2hhcGUnOjIsJ2NvbG91cic6J29yYW5nZScsJ2Ftb3VudCc6Mywnd29yZCc6J2dpbnVwaXRpdGUnLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0KeydzaGFwZSc6MywnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjEsJ3dvcmQnOid3aXBpc3UnLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MH0KeydzaGFwZSc6MiwnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjEsJ3dvcmQnOidnaW5pc3UnLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0KeydzaGFwZSc6MSwnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6Miwnd29yZCc6J3N1bnVwZXBpJywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnc2hhcGUnOjMsJ2NvbG91cic6J2dyZWVuJywnYW1vdW50JzozLCd3b3JkJzond2lwaXBpdGl0ZScsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzoxfQp7J3NoYXBlJzozLCdjb2xvdXInOidvcmFuZ2UnLCdhbW91bnQnOjEsJ3dvcmQnOid3aXBpc3UnLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MH0KeydzaGFwZSc6MSwnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6Mywnd29yZCc6J3N1bnVwaXRpdGUnLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0KeydzaGFwZSc6MywnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6Mywnd29yZCc6J3dpcGlwaXRpdGUnLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0KeydzaGFwZSc6MywnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6MSwnd29yZCc6J3dpcGlzdScsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzoxfQp7J3NoYXBlJzoyLCdjb2xvdXInOidibHVlJywnYW1vdW50JzoyLCd3b3JkJzonPHxlb3RfaWR8Pjx8c3RhcnRfaGVhZGVyX2lkfD5hc3Npc3RhbnQ8fGVuZF9oZWFkZXJfaWR8PgpbQ09NUExFVElPTl0=)

<\|begin\_of\_text\|><\|start\_header\_id\|>system<\|end\_header\_id\|>Youarealanguagelearnerwhohastolearnanartificiallanguagewithwordsandtheircorrespondingfeatures.Yourtaskistogenerateawordsuchthatyourcommunicationpartnercanguessthecorrectmeaningoftheword.Communicativesuccessisimportant.Onlyrespondwiththeword.<\|eot\_id\|><\|start\_header\_id\|>user<\|end\_header\_id\|>

{’shape’:1,’colour’:’green’,’amount’:3,’word’:’sutupitite’,’communicativeSuccess’:1}

{’shape’:2,’colour’:’orange’,’amount’:2,’word’:’ginupepi’,’communicativeSuccess’:1}

{’shape’:1,’colour’:’orange’,’amount’:2,’word’:’sutupepi’,’communicativeSuccess’:1}

{’shape’:1,’colour’:’green’,’amount’:2,’word’:’sutupepi’,’communicativeSuccess’:0}

{’shape’:2,’colour’:’orange’,’amount’:1,’word’:’ginisu’,’communicativeSuccess’:1}

{’shape’:2,’colour’:’orange’,’amount’:3,’word’:’ginupitite’,’communicativeSuccess’:1}

{’shape’:3,’colour’:’green’,’amount’:1,’word’:’wipisu’,’communicativeSuccess’:0}

{’shape’:2,’colour’:’green’,’amount’:1,’word’:’ginisu’,’communicativeSuccess’:1}

{’shape’:1,’colour’:’blue’,’amount’:2,’word’:’sunupepi’,’communicativeSuccess’:1}

{’shape’:3,’colour’:’green’,’amount’:3,’word’:’wipipitite’,’communicativeSuccess’:1}

{’shape’:3,’colour’:’orange’,’amount’:1,’word’:’wipisu’,’communicativeSuccess’:0}

{’shape’:1,’colour’:’blue’,’amount’:3,’word’:’sunupitite’,’communicativeSuccess’:1}

{’shape’:3,’colour’:’blue’,’amount’:3,’word’:’wipipitite’,’communicativeSuccess’:1}

{’shape’:3,’colour’:’blue’,’amount’:1,’word’:’wipisu’,’communicativeSuccess’:1}

{’shape’:2,’colour’:’blue’,’amount’:2,’word’:’<\|eot\_id\|><\|start\_header\_id\|>assistant<\|end\_header\_id\|>

\[COMPLETION\]

List of Prompts C.2 Speaking Prompt during communication.

[⬇](data:text/plain;base64,PHxiZWdpbl9vZl90ZXh0fD48fHN0YXJ0X2hlYWRlcl9pZHw+c3lzdGVtPHxlbmRfaGVhZGVyX2lkfD4gWW91IGFyZSBhIGxhbmd1YWdlIGxlYXJuZXIgd2hvIGhhcyB0byBsZWFybiBhbiBhcnRpZmljaWFsIGxhbmd1YWdlIHdpdGggd29yZHMgYW5kIHRoZWlyIGNvcnJlc3BvbmRpbmcgZmVhdHVyZXMuIFlvdXIgdGFzayBpcyB0byBjb21wbGV0ZSB0aGUgdm9jYWJ1bGFyeSBieSBpbnRlcnByZXRpbmcgdGhlIGludGVuZGVkIG1lYW5pbmcgb2YgdGhlIHdvcmQgZ2VuZXJhdGVkIGJ5IHlvdXIgY29tbXVuaWNhdGlvbiBwYXJ0bmVyLiBDb21tdW5pY2F0aXZlIHN1Y2Nlc3MgaXMgaW1wb3J0YW50LiBPbmx5IHJlc3BvbmQgd2l0aCB0aGUgY29tcGxldGUgbGFzdCBpdGVtLjx8ZW90X2lkfD48fHN0YXJ0X2hlYWRlcl9pZHw+dXNlcjx8ZW5kX2hlYWRlcl9pZHw+Cgp7J3dvcmQnOid3aXBpcGl0aXRlJywnc2hhcGUnOjMsJ2NvbG91cic6J2JsdWUnLCdhbW91bnQnOjMsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzoxfQp7J3dvcmQnOid3aXBpc3UnLCdzaGFwZSc6MywnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzoxLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MH0Keyd3b3JkJzond2lwaXN1Jywnc2hhcGUnOjMsJ2NvbG91cic6J2dyZWVuJywnYW1vdW50JzoxLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MH0Keyd3b3JkJzonc3V0dXBlcGknLCdzaGFwZSc6MSwnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzoyLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0Keyd3b3JkJzonZ2ludXBlcGknLCdzaGFwZSc6MiwnY29sb3VyJzonb3JhbmdlJywnYW1vdW50JzoyLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0Keyd3b3JkJzonc3V0dXBpdGl0ZScsJ3NoYXBlJzoxLCdjb2xvdXInOidncmVlbicsJ2Ftb3VudCc6MywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnd29yZCc6J3dpcGlwaXRpdGUnLCdzaGFwZSc6MywnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjMsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzoxfQp7J3dvcmQnOid3aXBpc3UnLCdzaGFwZSc6MywnY29sb3VyJzonYmx1ZScsJ2Ftb3VudCc6MSwnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnd29yZCc6J2dpbmlzdScsJ3NoYXBlJzoyLCdjb2xvdXInOidncmVlbicsJ2Ftb3VudCc6MSwnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnd29yZCc6J2dpbmlzdScsJ3NoYXBlJzoyLCdjb2xvdXInOidvcmFuZ2UnLCdhbW91bnQnOjEsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzoxfQp7J3dvcmQnOidzdW51cGVwaScsJ3NoYXBlJzoxLCdjb2xvdXInOidibHVlJywnYW1vdW50JzoyLCdjb21tdW5pY2F0aXZlU3VjY2Vzcyc6MX0Keyd3b3JkJzonc3V0dXBlcGknLCdzaGFwZSc6MSwnY29sb3VyJzonZ3JlZW4nLCdhbW91bnQnOjIsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzowfQp7J3dvcmQnOidzdW51cGl0aXRlJywnc2hhcGUnOjEsJ2NvbG91cic6J2JsdWUnLCdhbW91bnQnOjMsJ2NvbW11bmljYXRpdmVTdWNjZXNzJzoxfQp7J3dvcmQnOidnaW51cGl0aXRlJywnc2hhcGUnOjIsJ2NvbG91cic6J29yYW5nZScsJ2Ftb3VudCc6MywnY29tbXVuaWNhdGl2ZVN1Y2Nlc3MnOjF9Cnsnd29yZCc6J2dpbnVwZXBpJywnc2hhcGUnOic8fGVvdF9pZHw+PHxzdGFydF9oZWFkZXJfaWR8PmFzc2lzdGFudDx8ZW5kX2hlYWRlcl9pZHw+CltQUkVGSUxMRUQgV0lUSCBESVNUUkFDVE9SIEFUVFJJQlVURVNd)

<\|begin\_of\_text\|><\|start\_header\_id\|>system<\|end\_header\_id\|>Youarealanguagelearnerwhohastolearnanartificiallanguagewithwordsandtheircorrespondingfeatures.Yourtaskistocompletethevocabularybyinterpretingtheintendedmeaningofthewordgeneratedbyyourcommunicationpartner.Communicativesuccessisimportant.Onlyrespondwiththecompletelastitem.<\|eot\_id\|><\|start\_header\_id\|>user<\|end\_header\_id\|>

{’word’:’wipipitite’,’shape’:3,’colour’:’blue’,’amount’:3,’communicativeSuccess’:1}

{’word’:’wipisu’,’shape’:3,’colour’:’orange’,’amount’:1,’communicativeSuccess’:0}

{’word’:’wipisu’,’shape’:3,’colour’:’green’,’amount’:1,’communicativeSuccess’:0}

{’word’:’sutupepi’,’shape’:1,’colour’:’orange’,’amount’:2,’communicativeSuccess’:1}

{’word’:’ginupepi’,’shape’:2,’colour’:’orange’,’amount’:2,’communicativeSuccess’:1}

{’word’:’sutupitite’,’shape’:1,’colour’:’green’,’amount’:3,’communicativeSuccess’:1}

{’word’:’wipipitite’,’shape’:3,’colour’:’green’,’amount’:3,’communicativeSuccess’:1}

{’word’:’wipisu’,’shape’:3,’colour’:’blue’,’amount’:1,’communicativeSuccess’:1}

{’word’:’ginisu’,’shape’:2,’colour’:’green’,’amount’:1,’communicativeSuccess’:1}

{’word’:’ginisu’,’shape’:2,’colour’:’orange’,’amount’:1,’communicativeSuccess’:1}

{’word’:’sunupepi’,’shape’:1,’colour’:’blue’,’amount’:2,’communicativeSuccess’:1}

{’word’:’sutupepi’,’shape’:1,’colour’:’green’,’amount’:2,’communicativeSuccess’:0}

{’word’:’sunupitite’,’shape’:1,’colour’:’blue’,’amount’:3,’communicativeSuccess’:1}

{’word’:’ginupitite’,’shape’:2,’colour’:’orange’,’amount’:3,’communicativeSuccess’:1}

{’word’:’ginupepi’,’shape’:’<\|eot\_id\|><\|start\_header\_id\|>assistant<\|end\_header\_id\|>

\[PREFILLEDWITHDISTRACTORATTRIBUTES\]

List of Prompts C.3 Guessing Prompt during communication.