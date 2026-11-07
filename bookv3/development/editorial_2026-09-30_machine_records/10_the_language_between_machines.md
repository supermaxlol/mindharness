# Chapter 10: The Language Between Machines

Three objects sit on a laboratory table. Each has the same shape. Each appears alone. One is orange, one green, one blue.

A speaker gives all three the same name: `wipisu`.

The speaker is a language model, and the table is a list of simulated objects, but the mistake is recognizable. Imagine a shipping clerk who has learned to label every box by size and weight while dropping the label that says what is inside. Most packages still reach the right shelf. The clerk becomes very fast. Then a dangerous package arrives whose color was the warning.

In the experiment, nobody shipped a dangerous package. The objects were combinations of shape, color, and amount. There were twenty-seven possible combinations, and the researchers examined the artificial words that language models made for them. The same word appearing against those three colors is visible in their published table. It is one small failure inside a larger success: the models had discovered a way to reuse parts of words. In the same vocabulary, one ending tended to mark *one*, another *two*, and another *three*. A model could use the pattern to name objects it had never seen.

This example came from a code shaped by interaction within one generation. It had learned to reuse parts, and it had already begun to forget color. When the researchers then passed related vocabularies through generations of model learners, the codes became easier to inherit while growing more ambiguous.

That is the peril hidden in the word *efficient*. A good shorthand removes what a partner can already infer. A bad shorthand removes what neither partner has yet been made to care about. Both can look like progress on a scoreboard that counts only the distinctions tested today.

The last chapter's checker could not read the record it was meant to inspect. Here the machines can read their shared record well enough to pass it on. The unsettling question is what happens to a fact when the code they inherit stops carrying it.

### The game before the language

Go back to a simpler laboratory. One agent sees a target. Another sees several candidates. The first may send a short message; the second must choose the right candidate. A correct choice earns a reward. The two agents begin without an agreed word for *blue*, *triangle*, or *three*. They may settle on any signals that help them win.

If two coworkers invent `B2` to mean “the second blue box,” they are doing something similar. The symbol has no natural connection to the object. It works because one coworker uses it consistently and the other acts on it. If the convention is written down, a third coworker can learn it. The marks become a little external memory for the pair.

There is a temptation to look at successful coordination and announce that the agents have invented language in the full human sense. In 2017, Satwik Kottur and colleagues tested that leap. Their agents often achieved nearly perfect task rewards using invented messages that were difficult for humans to interpret and did not consistently break into reusable parts. A private code could solve the game without becoming a neat miniature of English. When the researchers imposed restrictions on what the agents could say and remember, more human-readable, compositional patterns could be coaxed out.

This was the first failed walk: *if agents need to communicate, surely a clear language will emerge*. They needed to coordinate. They did not need to make their messages clear to the person standing outside the game.

Consider an office where two experienced workers have handled the same machine for years. One taps the housing twice; the other changes a setting. Their signal is perfectly useful to the pair. A newly hired safety inspector may understand neither the tap nor the setting. It would be foolish to call the tap meaningless merely because the inspector is lost. It would be equally foolish to say the inspector has oversight because the tap was logged.

The comparison stops at a point that matters. Human workers can often stop and explain what a tap meant. A trained agent's convention may be distributed across weights, task history, and its partner's responses. A researcher can sometimes reconstruct a mapping by intervening and testing alternatives, but there may be no complete dictionary already sitting inside the system, waiting to be printed. The game measures coordination and aspects of structure; it does not measure a machine's intention to conceal anything.

The record, here, is not a secret diary. It is the durable mapping between a signal, a situation, and the next move. Two agents can maintain that mapping through use even when no human has named its rules. Once new agents inherit the mapping, the code begins to have a history beyond either original partner.

### Send in the new hire

Fushan Li and Michael Bowling changed one condition of the game: they replaced the listener.

Their speaker could send two symbols selected from a small vocabulary. The listener chose one target from five candidates. The objects varied in color and shape. Under one training schedule, the speaker and the same listener practiced together for 300,000 iterations. Under another, a new listener replaced the old one every 6,000 iterations. Fifty listeners passed through the speaker's working life.

Both schedules eventually produced communication that was about 97 percent successful when evaluated with their trained partners. If the researchers had stopped at the familiar accuracy score, the two histories would have looked nearly alike. But the reset speaker had learned a different kind of message. When a fresh listener arrived, it learned that speaker's code more quickly. The code had also become more structured: similar objects tended to receive more similar messages. The no-reset pair could win together without paying the cost of teaching a stranger.

The new hire changed what survived.

Think of the difference between a note that says “do the Tuesday thing” and one that says “when the pressure rises, open the left valve.” The first is shorter for a veteran who remembers Tuesday. The second travels to a worker hired on Wednesday. Repeated turnover makes the veteran pay for ambiguity at every handoff. Ease of teaching becomes part of the selection pressure on the code.

There is no mystical impulse toward clarity inside the speaker. The rules of the workplace changed. The easiest code to maintain with one partner was no longer the easiest code to maintain across a succession of partners. The experiment shows that replacement can select for teachable structure without a human writing the words. It does not show that the newcomers were less capable models, or that the resulting signals became transparent to any outsider who had not learned the game.

Now test the comforting story. Suppose you say, “The agents have a private language because they have not yet had to teach anyone.” Li and Bowling send in strangers and watch structure grow. Suppose you then say, “Once a language can be taught, everyone can read it.” Their new listeners learn by training inside the task. The human observer has neither their learning history nor their reward. A code can cross generations and still demand a separate effort to audit it.

Our own fable from two chapters ago worked by a related route. The lion, the adviser, and the bull are easy to teach because their relations can be reconstructed in many settings. A machine code can also become portable. Yet portability alone does not tell us which part of the world the code preserves. The fable can travel while one reader forgets the bull's innocence. A machine vocabulary can travel while its word for the object's color disappears.

### The word that lost a color

Tom Kouwenhoven, Max Peeperkorn, and Tessa Verhoef put large language models into a version of the inheritance game. Their objects combined three shapes, three colors, and one, two, or three copies: twenty-seven possibilities. The models saw examples for fifteen. They used artificial words made from syllables such as `su`, `pepi`, and `wipi`; later the researchers tested whether they could extend the vocabulary to the twelve combinations held back.

During communication, pairs of Llama 3 70B models took turns describing and identifying targets among distractors. Then the researchers arranged six transmission chains, each eight generations long. A later model received part of a predecessor's signal-to-object vocabulary and learned from it. The researchers selected the vocabulary with the highest measured structural similarity to pass to the next generation. The inheritance was experimental and curated, not a spontaneous migration of deployed agents from one system to another.

Something remarkable happened before the generations even began. In the first communication round, the models identified targets in roughly seven out of ten interactions, where random choice among the candidates would succeed one in four times. Interaction helped shape parts of the initially arbitrary vocabulary into reusable elements. In one example, a word ending marked quantity while a beginning marked shape. A model could extend that pattern to an object it had not seen during teaching.

Now follow the code as it is handed down. Later models reproduced inherited signals more faithfully. The words became easier for them to learn. If the only question were “Will the next model speak this code?” the answer improved across generations.

But the second question was “What can this code still say?” In the published analysis, the proportion of uniquely named objects fell from about seven in ten in the first generation to about five in ten in the last. Signals grew longer and more ambiguous. The authors found no corresponding increase in successful communication across generations. Some lineages produced the same signal for different objects.

That is where `wipisu` returns. The table's three differently colored, otherwise matching objects share the word. If the listener's current candidates make color irrelevant, it can still pick correctly. If two of those objects appear together and color is the only difference, the word has lost the discriminating bit. This particular word came from a within-generation test, before the eight-generation chains. The chains separately show how later learners favored an easier-to-repeat but increasingly ambiguous vocabulary. Together, the observations expose two points at which a distinction can disappear. The experiment does not say that all generated codes ignored color or that every trial failed.

The warehouse image helps us feel the error; it must not smuggle in a false event. These were textual stimuli and model responses in a controlled referential game. No package, patient, or financial claim was misrouted. The larger inference concerns systems whose consequential categories are also learned from use. If a category is seldom tested, the next version of a code may preserve the common decision while erasing the rare distinction on which a later person depends.

The researchers themselves supply the important counterweight. With enough pressure to distinguish meanings during actual communication, degenerate vocabularies may be checked. In this setup, the pull toward being easy for a model to learn was stronger than the pressure to keep every object distinct. The record kept being copied. What it could distinguish did not automatically keep up.

### The four comforting explanations

The first says that machine codes are gibberish. Gibberish would not help a listener pick targets beyond chance, allow a new listener to learn faster after resets, or let an unseen object inherit a structured name. These systems carried usable relations. The fact that a human needs experiments to recover them does not make the relations imaginary.

The second says that every effective code can be translated back into ordinary language, so no oversight problem remains. Some can be mapped after systematic probing. Indeed, the `wipisu` table is already a partial translation. But a successful translation requires access to the inputs, the signals, the partners, and the decisions that made a signal useful. Even then, a dictionary made for yesterday's code can lag behind a new generation's changes. What matters is whether the human can check a consequential distinction *before* the decision uses it, not whether a researcher can explain a pattern after collecting the full experiment.

The third says that if newcomers can learn the code, humans can learn it just as cheaply. Li and Bowling's newcomers were trained listeners in a narrow game. Kouwenhoven's successors were language models given a structured list of examples and selected vocabularies. A human supervisor can be taught a stable convention, but training a human on one code is a different operation from understanding a changing, task-specific code at every handoff. The newcomer result establishes inheritance. It does not grant outsiders immediate fluency.

The fourth says that the simplest cure is to require every message to be plain English. There is a cost worth naming. In one cooperative navigation simulation, agents using a learned signaling protocol reached their goal in an average of 28.7 steps near the end of training; agents constrained to a fixed, human-designed symbolic protocol took 43.2. The latter protocol was a simple rule for signals, not full English. It is evidence that *this particular imposed code* carried a performance penalty in *this particular task*, not a theorem that readable communication always fails.

The decisive reply to that fourth explanation is already being engineered. A hybrid protocol called HyLaT lets agents send dense information through a latent channel while expressing selected answers and commitments in text. Its experiments report lower communication overhead with competitive task performance. This is a live alternative to the claim that efficiency must always exclude a readable surface. It also leaves a harder question: **who decides which facts count as “critical” enough to emerge from the dense channel?** If the selection rule lets color vanish, a perfectly grammatical final sentence can still describe the wrong box.

Mycal Tucker and colleagues attacked the code's incentives from another direction. They trained agents while balancing task utility, how much the signal revealed, and how complicated the vocabulary became. Paying attention to those pressures helped produce compact lexicons closer in size to human ones without surrendering the task. Lexicon size is not an audit of the message's truth. It is evidence that the shape of machine communication responds to what designers make costly and what they reward.

**A code can win, travel, and be summarized in fluent language while leaving a consequential distinction unaccounted for.** Success at the task does not certify human readability. Teachability does not certify expressiveness. Readable final answers do not certify that the information omitted from them was immaterial. Each comforting explanation treats one of those achievements as if it settled the others. The experiments pull them apart.

### Read the consequence, not just the message

We can make oversight more concrete than “understand everything the agents say.” Imagine a pair of machine workers exchanging a signal before one authorizes a payment. A human auditor may not be able to translate the entire signal stream. She can still require the record of what claim was presented, which source was consulted, what rule authorized the payment, the amount sent, and the account that received it. She can ask whether changing a disputed input changes the decision. She can compare a true source with a shuffled one to test whether the purported check had causal force.

That is not a promise that receipts solve every governance problem. A receipt can record a bad decision accurately. A hash can prove that a message was not altered without revealing whether the message was fair. A model can produce a polished textual explanation after acting for reasons the explanation does not capture. The witness has to connect source, code, action, and correction. Chapter 9 showed what happens when even the first connection is miswired.

Nor can we move every burden onto the person downstream. A patient should not need to learn an agent's dialect before challenging a denial of care. A worker should not need to reconstruct a classifier's training lineage before contesting a lost wage. If institutions choose the faster code, they inherit the duty to preserve the decision-relevant distinctions and make a challenge possible while it can still matter. The cost of translation belongs with the operator who gains from compression.

We have reached the same old question in new materials. A mark survived its maker. A law made one claim payable and another remote. A fable crossed centuries because readers could reconstruct its relations. A machine word now crosses model generations because successor models can learn it. In every case, survival of the mark is only the first victory. The second is whether the next reader finds the distinction that reality will demand.

`Wipisu` is memorable because it names a success and a failure at once. The code learned to carry shape and amount. Its reader could sometimes act well. Three colors went by under one name. The later transmission chains add the unsettling possibility: a vocabulary can become easier to hand forward while preserving fewer distinctions.

What if the next generation learns not only that word, but a whole world described in such words? What happens when its training record is made increasingly of the previous generation's descriptions, and the missing colors are no longer present in the examples against which the code is tested? An absent distinction can begin to look as though it never existed.

### Source note

- The opening `wipisu` example and the twenty-seven-object design, fifteen taught combinations, first-round communication result, six eight-generation chains, selection of the highest structural-similarity vocabulary, and unique-signal decline come from [Kouwenhoven, Peeperkorn, and Verhoef](https://arxiv.org/abs/2412.07646), especially their Table 1 and §§3, 5–6. Table 1 records a within-generation testing vocabulary; it is not a snapshot from the eight-generation chain. The paper separately reports better learnability across generations alongside longer, more ambiguous signals and no increase in communicative success across generations. The shipping example is an analogy; no shipping or safety incident occurred in the study.
- [Kottur and colleagues](https://arxiv.org/html/1706.08502v3) measured successful yet often uninterpretable or noncompositional invented protocols, then used communication constraints to encourage structure. [Li and Bowling](https://arxiv.org/html/1906.02403v2) compared a single-listener 300,000-iteration training history with fifty sequential listeners replaced every 6,000 iterations; both achieved about 97% trained-partner success, while reset-selected languages were easier for new listeners to learn.
- [Zhang's efficiency-attenuation simulation](https://arxiv.org/html/2603.22312v1) reports 28.7 mean steps for emergent communication and 43.2 for a fixed symbolic protocol in its cooperative navigation task. The constrained protocol is a deterministic symbolic mapping, not ordinary English. [Mou and colleagues' HyLaT study](https://arxiv.org/html/2605.25421v1) tests a hybrid latent-text design; its reported gains do not prove that every consequential distinction reaches the text channel. [Tucker and colleagues' information-bottleneck study](https://arxiv.org/abs/2207.00088) treats utility, informativeness, and complexity as pressures that shape a code, including routes toward more human-like lexicons. The research archive's `LITERATURE_REVIEW_LEDGERS_V2.md` and `experiments/lab_runs_falsify/culture_dialect_v2.json` index the earlier source walk.
