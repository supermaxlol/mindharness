# Chapter 10 machine-language source walk — 2026-09-26

This note records where the V3 chapter improves on the V1/V2 machine section after checking the primary papers. The studies use different agents, tasks, and mechanisms. Their results converge on selection pressures without forming one uninterrupted real-world history of a deployed swarm.

## The exact opening image

Kouwenhoven, Peeperkorn, and Verhoef, [*Searching for Structure*](https://arxiv.org/abs/2412.07646), Table 1: `wipisu` appears for shape 3 / amount 1 in orange, green, and blue. The table is a **within-generation testing-phase vocabulary after communication**, not a vocabulary from the eight-generation transmission chains. The paper also identifies `su` as marking amount one and describes partial shape structure, while colors are less clearly encoded. This supports a vivid, specific example of a distinction lost despite emergent structure. It does not prove that every machine code drops colors.

## Inheritance and the failure of a simple progress story

The same Kouwenhoven paper uses Llama 3 70B models, 27 possible shape/color/amount combinations, 15 teaching examples, and 12 held-out combinations. Its generational experiment includes six chains of eight generations. The vocabulary with highest topographic similarity is selected for transmission to the next generation. Learnability improves; communicative success does **not** increase across generations. Signals become longer and more ambiguous; mean proportion of unique signals falls from 0.707 (generation 0) to 0.519 (generation 7), with the paper's comparison `t(5)=2.64, p=.046`. V1/V2 accurately noted inheritance and increased learnability but compressed this into “holistic-to-structured transition” without making the simultaneous loss of expressive distinctions the plot. The research review should be read with that result in mind.

Li and Bowling, [*Ease-of-Teaching and Language Structure*](https://arxiv.org/html/1906.02403v2), test a different question with pre-LLM neural-agent referential games. The speaker sends two symbols from eight possible symbols to identify one of five candidates. One arm keeps the same listener for 300,000 iterations; the reset arm replaces a listener every 6,000 iterations, for 50 listeners. Both reach around 97% trained-partner success. Reset languages are easier to teach to fresh listeners and more structured. The result establishes a selection pressure from learner turnover. It does not establish that newcomers were weaker model architectures or that an uninvolved human immediately understood the code.

Kottur and colleagues, [*Natural Language Does Not Emerge Naturally*](https://arxiv.org/html/1706.08502v3), found effective invented codes that need not be interpretable or compositional, and elicited more structure by changing communication restrictions. It is evidence against automatic human legibility under unrestricted task reward, while also showing that design constraints can alter the outcome.

## Legibility and efficiency

Zhang's [*Efficiency Attenuation Phenomenon*](https://arxiv.org/html/2603.22312v1) compares a learned code with a **fixed deterministic symbolic mapping**, not fluent natural language. It reports 28.7 versus 43.2 mean steps near the end of a cooperative-navigation simulation. The text calls this “50.5% higher efficiency” and elsewhere “50.5% fewer steps”; those phrases use inconsistent denominators, since `(43.2−28.7)/28.7≈50.5%` while `(43.2−28.7)/43.2≈33.6%`. V3 uses the raw step counts and the correct task description.

Mou and colleagues' [HyLaT](https://arxiv.org/html/2605.25421v1) sends dense content in latent form and selected critical commitments in text, reporting reduced communication overhead with competitive performance. It is a constructive answer to a **single-channel** trade-off. It does not prove every decision-relevant feature of the latent exchange reaches the text. Tucker and colleagues' [VQ-VIB study](https://arxiv.org/abs/2207.00088) likewise demonstrates that changing utility, informativeness, and complexity pressures shapes the emergent lexicon; human-like lexicon size is not the same as full interpretability.

The V1/V2 assertion that “no training trick makes both cheap and readable at once” overstates these papers, particularly HyLaT, which explicitly proposes a hybrid route. The V3 argument is stronger at the operational level: the human-readable or audited channel has to carry every distinction required for a consequential decision, and that coverage must be tested. Unreadability is a risk under some objectives, not an unavoidable law of every possible protocol.

## Allocation to Chapter 11

Guo, Wu, and Yiu's [*Model Collapse as Cultural Evolution*](https://arxiv.org/html/2605.23054v1) studies ten generations of **self-training on model output** in English, German, and Turkish. This is recursive training, not the same as live agents transmitting invented words in a referential game. It finds compositionality first rising then falling under unfiltered self-training, with task-grounded filtering preserving structure better than random filtering. It belongs chiefly in Chapter 11, where generated records become the next training corpus. Chapter 10's last question sets that handoff up without conflating the designs.
