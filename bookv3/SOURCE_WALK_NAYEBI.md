# Source walk 1 — from Nayebi's theorem to the five-job synthesis

**Purpose:** Turn an expert's compressed line into a reader's causal understanding. This is a writer's research trace for V3, not manuscript prose. Primary source: Aran Nayebi, [*What Capable Agents Must Know: Selection Theorems for Robust Decision-Making under Uncertainty*](https://arxiv.org/html/2603.02491), arXiv:2603.02491v3 (28 June 2026), especially Theorem 5 and Corollaries 3–5.

## The compressed sentence in the archive

The archive's compressed claim is that successful reflexive systems repeatedly build five jobs: boundary, two-speed memory, salience, damping, and a corrective witness. [Nayebi's published paper](https://proceedings.mlr.press/v337/nayebi26a.html) supplies the mathematical leg of that case. Low average regret on diagnostic task families forces predictive state, belief-like memory, regime tracking under mixtures, and informational modularity under block structure. This is stronger than saying a clever designer *can* add memory. It means a memoryless or aliasing agent pays for the missing distinction on the relevant tests. The five-job synthesis then combines that pressure with biological evidence and the project's ablations. It is the book's cross-domain inference, not a sentence attributed verbatim to one theorem.

## The failed walk that makes the result necessary

The old, reasonable claim was: *We can build a successful controller using a world model or belief state.* But a successful design does not show that every successful controller must use such information. Perhaps a clever reactive policy could do just as well. Nayebi's question is what kinds of tasks would make that escape route fail.

Imagine two sealed boxes that look identical now. You saw one filled mostly with red balls and the other mostly with blue balls, but the labels have been removed. You must bet on the next draw. An agent that remembers which box history it is in can make different bets. An agent whose memory maps both histories to one identical internal state must use the same betting rule for both. When the correct bets are confidently opposite, that rule must incur loss in at least one history. This box scene is an invented teaching example; it is not an experiment in the paper.

Now the technical claim has a foothold. In the paper, *aliasing* means mapping histories that matter for a prediction to the same memory state. The margin parameter **γ** marks how far the relevant success probabilities sit from a 50–50 bet. It is a confidence gap in the diagnostic task, not a meter for consciousness or an “observer” inside the agent. Theorem 5 lower-bounds paired regret by the amount of such witnessed aliasing times a margin-dependent factor. In plain language: if the tests repeatedly demand different confident bets, a low-regret agent cannot keep forgetting the difference between the histories. See the [Theorem 5 setup and bound](https://arxiv.org/html/2603.02491).

## What the next results add

- **Corollary 3:** With specified block-structured test families, low regret rules out aliasing of relevant histories *within each block*. The result supplies a formal reason to expect differentiated, locally useful state rather than one indiscriminate memory pool.
- **Corollary 4:** Under shifting task mixtures where different regimes demand opposite confident bets, the agent's memory has to preserve regime-relevant information. The author compares such functional variables to affective or homeostatic modulation in embodied systems, then explicitly distinguishes that claim from a theory of felt emotion.
- **Corollary 5:** Two agents with low pair-regret can agree on the **decision-relevant partitions** of histories, up to invertible recoding, when the same evaluation family, γ-minimality, and complete witnesses are assumed. This is narrower than claiming that all capable agents, brains, or contemplative traditions converge to identical structures.

These conditions and conclusions are stated in the paper's [structured-task corollaries and discussion](https://arxiv.org/html/2603.02491). The paper also says it makes **no claim about subjective experience**.

## The paragraph we can earn in the book

> Two boxes look identical after their labels fall off. You watched one fill with red balls and the other with blue. If you now have to bet on the next draw, the last glimpse of each box is insufficient; the history matters. An agent that erases the distinction must give the same answer in both cases and will be wrong when the boxes demand opposite bets. Nayebi formalizes that pressure: on task families that repeatedly reward the right prediction, low-regret memory cannot collapse histories that require different confident decisions. The boxes are only a way into the proof. The theorem applies under specified tests and assumptions; it does not prescribe five modules, prove consciousness, or show that a particular AI system has passed those tests.

This belongs in the AI act when the reader has seen the project's failed watcher and transfer experiment. The betting proof explains why a consequential record must retain a distinction the next decision requires; the experiments show what happens when the record is miswired or its key does not transfer. The scene gives the theorem a failure history, then returns to the five jobs of the broader thesis.

## Claims to keep in the research ledger

| Sentence | Grade | Editorial action |
|---|---|---|
| Low regret on the paper's diagnostic task families constrains predictive memory and no-aliasing. | Theoretical, conditional on task and setup | Use with assumptions. |
| Block-structured and shifting-regime tests induce additional information-preservation constraints. | Theoretical, conditional | Use only when that task structure matters to the scene. |
| The five jobs recur because systems that must persist, predict, select, stabilize, and correct face distinct failure pressures. | Cross-domain inference from theorem, biology, and ablations | Put at the center of the book; earn each job through a failed rival. |
| Corollary 5 shows convergence of decision-relevant partitions under shared tests and its minimality and witness conditions. | Theoretical | Use to explain why independent systems can discover comparable distinctions; do not turn a partition result into a claim of identical anatomy. |
| The selection theorems prove subjective experience. | Contradicted by the author's stated scope | Do not use. |

**Next source walk in this sequence:** the S126 sham result and miswired checker. It gives an empirical counterpart: a record can exist yet fail to influence the decision if the actor cannot consult the right one. That application needs its own result files and code path, not a borrowed proof from Nayebi.
