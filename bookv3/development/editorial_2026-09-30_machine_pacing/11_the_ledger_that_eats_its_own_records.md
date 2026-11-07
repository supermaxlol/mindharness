# Chapter 11: The Ledger That Eats Its Own Records

The church towers disappear. So do the architects. By the ninth generation, the passage has filled with jackrabbits.

The original prompt concerns English parish churches: master masons, itinerant workers, and competing explanations of how their towers were designed. In Ilia Shumailov and his colleagues' experiment, a small language model learns from text, generates new text, and supplies material for the next round of learning. Later generations inherit earlier generations' output. A published example eventually wanders through a list of differently colored jackrabbits, including “blue-tailed jackrabbits.”

The first model's continuation was already imperfect. Successive copying gave those imperfections descendants.

Nobody had to order the system to forget the masons. Nobody had to persuade it that rabbits were better historians. The procedure kept producing text, and each new training round had text to learn from. What failed was the relationship between the growing family of descriptions and the world the original passage described.

In the last chapter, three colors could pass under one machine word. Here, a machine's descriptions become another machine's education. The reader of the record becomes its next writer. An omission can acquire a lineage.

The unsettling possibility is simple: **an archive can keep growing while the world it can represent gets smaller.**

### The footnote on the photocopy

Imagine a photocopied instruction sheet. Its main directions are dark and clear. A faint footnote says that one unusual combination of parts requires a different setting. You copy the copy. The main directions survive. The footnote loses an edge. Several copies later, the page is easier to read because the little mark has vanished.

Most users never notice. Their machines use the common combination. The clean page works for them. A technician encountering the exceptional combination sees no reason to change the setting. The instruction that would have saved her is absent, and the sheet offers no sign that anything has been removed.

Recursive machine learning can produce that kind of absence, although it works through sampling and training rather than fading ink. A generative model learns a distribution: some continuations are more likely than others. It then produces a finite collection of examples. The next learner encounters that collection. What was possible in the earlier distribution may be missing from the actual examples handed forward.

Try a miniature version yourself. A bag contains ninety-nine ordinary cards and one card with the exceptional instruction. Draw a card, replace it, and repeat one hundred times. There is roughly a one-in-three chance that you never draw the exceptional card. Your hundred-card record may look ample. It may contain the usual instruction over and over. It can still omit the one instruction that was different.

Now build the next bag from your recorded draws. If the exceptional card never appeared, it has no representative in that bag. The next person can sample diligently and still fail to recover it. More draws from the narrowed bag do not recreate the missing instruction.

Actual models carry prior training, generalize, make mistakes, and can invent continuations absent from their immediate examples. The card game isolates one pressure: finite sampling can remove a distinction before anyone decides that it is unimportant. Statistical analyses of recursive learning show how that pressure can compound under replacement of the earlier data.

The photocopy also has a boundary. Ink usually fades in one direction. Machine generations can manufacture new noise while losing old variation. The result can be more repetitive in one respect and more wildly wrong in another. Church towers can disappear while an extravagant collection of rabbits arrives. A smaller map need not be a quieter map.

The ledger has begun selecting the evidence from which its successor will learn what the world contains.

### The first improvement is real

There is an obvious objection. Perhaps the original archive was messy. Perhaps copying removed noise, and we are calling a useful cleanup a catastrophe.

Sometimes cleanup is useful. The difficulty is telling where it ends.

Dongxin Guo, Jikun Wu, and Siu Ming Yiu followed ten generations of language-model self-training, testing several language properties across English, German, and Turkish. Their compositional analysis was in English: whether reusable pieces continued to combine in useful ways. Under unfiltered self-training, that structure initially improved and later deteriorated. The rise-and-fall pattern also appeared with highly regular starting material. Initial disorder could not explain the whole trajectory. A filter tied to downstream task quality preserved structure better than random filtering of a comparable amount of material.

Picture an editor shortening a complicated recipe. On the first pass, she removes repeated instructions. On the second, she combines two sentences. Both changes help. On the fifth, she cuts the warning that matters only when the kitchen is humid. On the tenth, the recipe is wonderfully easy to repeat and no longer works in a humid kitchen.

There was a genuine improvement near the beginning. It gave the later cuts a persuasive precedent.

The task filter gave a distinction a chance to survive because it still did work. Random deletion gave it no such chance. Shorter text was neither the cure nor the disease; the selection test mattered. The lesson of the first improvement is to ask what the editor measured before we praise what she removed.

Our fable has returned in a new form. Dimnah's first interpretation helped the lion approach a frightening sound. That success made his later interpretation easier to trust. A machine pipeline can likewise inherit authority from its earlier improvement. A criterion can reward a useful simplification and then fail to notice what the next simplification removes. The danger needs no scheming adviser.

### The green light before the narrowing

A training dashboard seems to offer the missing criterion. Surely a model that is degrading will announce the damage through a worse score.

One score can improve while another capacity contracts.

In Zhipeng Zhang's study of silent collapse, a recursively trained GPT-2 model initially improved its validation perplexity while the diversity of its predictions on a fixed set of anchor inputs contracted. Perplexity measures how well the model predicts held-out text. It can be a useful measure of learning without revealing every change in what the model can represent. In the reported run, the later deterioration became severe; the narrowing signals appeared earlier.

Think of a delivery company that improves its average arrival time by quietly serving fewer difficult addresses. The average is correct. The excluded streets are real. You need a second record to see that the celebrated improvement and the disappearing service occurred together.

With the model, ask which cases enter the metric, which differences can change it, and which losses can occur while it stays calm. A score becomes dangerous when an institution lets it answer questions it was never designed to answer.

Zhang also tested a response. Monitoring fixed anchor examples was used to adjust exposure to generated data and the intensity of learning, helping stabilize the tested trajectories. The probes stayed fixed while the process changed. A fixed mixing schedule also performed well in a retrospective comparison. There are several ways to regulate the loop; the point is to measure the contraction and let that measurement alter training.

This is the connection to the financial chapters. A performing-loan figure did not settle every question about future loss. A low perplexity figure does not settle every question about retained variety. Each number can be accurate within its own job. The person who promotes it into a certificate for the whole system acquires power over everything the certificate leaves out.

### Put the original back on the desk

Now test the darkest explanation: machine-generated material is inherently poisonous, so every attempt to learn from it must end in collapse.

Matthias Gerstgrasser and his colleagues changed the inheritance rule. Instead of replacing the earlier dataset with each new synthetic generation, they retained the original data and accumulated successive generated datasets alongside it. In their language and molecule-conformation experiments, accumulation kept test loss stable or better. In the image experiment, it greatly slowed deterioration and preserved major variation, while some details appeared less often in generated faces. Their linear-model analysis also supplied a bounded-error result for accumulation.

Follow the language experiment through one handoff. The first learner read a collection of simple stories. It then generated another collection of the same size. Under replacement, the next learner received that new collection alone. Under accumulation, it received both. At the following handoff, replacement again gave the successor only its immediate predecessor’s output; accumulation kept the earlier collections and added the new one. Each successor was newly initialized and trained on the material chosen for it. What changed was its education.

There is a surprise inside that first collection. TinyStories was generated by GPT-3.5 and GPT-4. The initial archive in this experiment was already synthetic. Preserving it still changed what happened to the smaller models’ descendants. Calling a page “AI-generated” cannot, by itself, tell us whether it should be kept or discarded. We need to know what it preserves, what replaces it, and how the successor is tested.

Perhaps accumulation worked simply because the apprentice received a thicker manual. More pages meant more training. The researchers tested that explanation by enlarging the replacement collection to match the accumulated collection’s size. Every page in this enlarged replacement still came from the latest predecessor. Performance continued to deteriorate, though more slowly. Giving the successor more of the latest account failed to reproduce the benefit of keeping earlier accounts in its education.

Return to the workshop. One employer keeps every edition of the instructions. Another throws away the earlier editions but prints enough copies of the latest one to fill the same shelves. The rooms contain the same number of pages. They contain different histories. If the latest edition omitted the humid-kitchen warning, copying it again cannot restore that warning. The experiment tests the analogous difference in training data; it does not give the model an apprentice’s ability to open a drawer during use.

Nor does the earliest edition acquire authority merely by being earliest. It can contain errors too. Accumulation provides a reference that replacement removes. Whether that reference deserves trust remains a separate question. In this experiment, the measured benefit was better performance on held-out story text, not proof that every retained story described the world correctly.

The intervention matters as much as the failure. It shows a route by which generated material can join an archive without continually erasing its foundation.

Return to the instruction sheet. The workshop keeps the original in a drawer and places later explanations beside it. An apprentice can use the clearer explanation, then consult the footnote when the exceptional combination appears. The later page is useful. Its usefulness no longer requires it to impersonate the complete original.

That is an inheritance worth building: additions with a path back.

But the drawer introduces a second question. Does anyone open it?

A follow-up study, *Collapse or Thrive?*, separated accumulation of the archive from the amount each new model actually trained on. Training on the whole growing collection could remain stable. Drawing a fixed-size training subset from an accumulating collection produced gradual deterioration in the studied settings, tending toward a plateau. The fixed-budget regime still avoided the runaway collapse of replacement. Its performance penalty shows that keeping an archive and learning from all of it are different achievements.

Imagine the apprentice's employer requires her to consult only one page each morning. The workshop adds hundreds of new explanations, and the original is now one page among thousands. The drawer survives. The chance that her working education contains its warning changes.

This is why a declaration that “we retain all data” is incomplete. Retention describes the shelves. Training selection describes the education. Retrieval describes what comes off the shelf during use. These are different decisions, often made by different teams, with different budgets.

A useful original must remain available to the consequential process. If the budget, sampling rule, or retrieval system prevents that encounter, preservation can become ceremonial. The archive has a receipt for the footnote. The apprentice still lacks the instruction.

### Keep the exception; reject the artifact

Another comforting explanation says the problem belongs to weak models. More capability will restore what copying lost.

Yangze Liu and Zhongyi Han tested thirteen public checkpoints through a common five-generation recursive protocol. Their final text-diversity measure ranged from 0.187 to 0.940: roughly nineteen to ninety-four distinct four-word sequences per hundred sequence windows. Those endpoints belonged to different checkpoints. The measure counts variation in generated wording; even a distinct phrase can be factually wrong. Model size did not supply a simple ordering of resilience.

Capability is therefore an incomplete answer to a question about inheritance. We still have to test what the chosen model retains under the chosen loop.

The same study found that tighter sampling could stabilize tested trajectories. Other work has reported useful interventions through token filtering, entropy-based selection, and changes to multimodal generation. These findings complicate a tempting slogan: *save every unlikely thing*.

The rare instruction and the blue rabbit are both unusual. Only one may deserve a place in the manual. A rarity score cannot tell them apart. The deciding question is whether the strange entry leads back to an independent case in the world and survives a test against it.

A procedure that celebrates every low-probability continuation can preserve artifacts as enthusiastically as exceptions. A procedure that deletes every unusual continuation can erase the real exception. Frequency alone cannot settle which one we have. We need reference cases, task outcomes, or other checks that discriminate between neglected reality and generated noise.

This is a harder editorial job than increasing the dataset. It is also a power to govern what future learners will find imaginable.

Suppose a model helps answer questions in a language with relatively few surviving digital records. Fluent majority-language paraphrases are cheap to produce. Originals in the smaller language take work to collect, interpret, and retain. A pipeline can become larger and more convenient while giving the smaller language less weight. Whether that happens depends on the actual selection rules; it cannot be diagnosed by counting total tokens.

The person who speaks the smaller language pays when her distinctions become expensive to recover. The operator may record a cheaper training run and a respectable average score. There is no contradiction between those entries. They belong to different ledgers.

Look at the selection rule. Look at who can challenge it. Look at whether the challenge reaches the next training run.

### Search can bring back your own answer

The feedback loop can also operate without changing a model's weights.

Gregory Druck and Ethan Smith studied simulated retrieval systems in which model answers were expanded into articles and then became references for later answers. One design added those articles to a searchable collection. Across their designs, responses increasingly converged and models disproportionately cited their own generated references when alternatives remained available. They called this convergence collapse: successive answers became essentially the same, even though sameness alone could not establish that they were false.

Imagine the lion asking for a second opinion about Dimnah's account. A messenger searches the library. He brings back five beautifully written reports. Each descends from Dimnah's first statement.

There are five documents on the table and one underlying assertion.

The messenger may have searched honestly. The documents may contain genuine truths. Agreement among them still supplies less independent support than their number suggests. A reader who sees only the finished reports has to reconstruct the dependency before she can judge what the agreement is worth.

Our machine archive has acquired the same problem. An answer becomes a source, the source becomes a reference, and the reference helps produce an answer that resembles the first one. A search operation has occurred. The loop has not necessarily encountered anything that could contradict its premise.

Here provenance earns its place. It means preserving where an entry came from and what earlier entries it depends on. Those links let a checker distinguish five observations from five descendants of one observation. They can also reveal whether an apparently external source was produced by the system now citing it.

Provenance does not certify truth. Five independent witnesses can share a misconception; one generated explanation can be correct. Its job is to make the structure of dependence inspectable. The checker still needs a test that can fail, and the system still needs a route through which that failure changes the next answer.

### What survives the objections

The visible symptom is not the mechanism. Shumailov's team penalized repetition, yet the deeper degradation persisted. Likewise, a good aggregate score cannot certify the retained range: Zhang's anchor set registered contraction while perplexity still improved. A larger model cannot settle the matter by reputation; Liu and Han found materially different outcomes across checkpoints run through the same protocol.

Nor does the origin label decide the fate of a sample. Generated material can help when originals accumulate and task checks select useful descendants. An archived original can fail to help when a fixed training budget never draws it. A provenance label can show that five retrieved articles descend from one answer, but it cannot make that answer true or give the omitted witness a hearing.

Each proposed escape answers a different question: Does the output look repetitive? Where did it come from? Was the original retained? How did the model score? None alone asks whether the next consequential decision can be corrected by evidence outside the loop. That is the test the record keeper must maintain.

This obligation has owners. The trainer chooses which examples survive the budget. The retriever chooses which stored pages become evidence. The evaluator chooses which failures register. The institution chooses whether a person affected by an omission can force an amendment. An appeal that changes a file but never reaches the model is another footnote fading in a drawer.

The costs arrive in units that people can feel: another wrong answer to correct, another procedure to repeat, another claim to establish without the source that should have supported it. The machine gains no special entitlement to pass those costs downstream because its output was cheap.

### The keeper of the record

The towers and the jackrabbits make a normally hidden succession visible: a description supplied the next description's education, and distance from the originating task grew across the family.

The accumulation result supplies the answering image. A later writer can add to the record while maintaining contact with what came before. The task filter supplies another. A clearer account can be kept because it still works when tested. The retrieval result supplies the last warning. An apparent journey outward can lead back to the system's own words.

The ledger does not need to plot its escape. Designers can build a loop that rewards cheap, fluent descendants and gives expensive contradiction too little influence. Once those descendants become the next generation's evidence, the loop begins to educate its own successors. The missing instruction becomes harder to notice because fewer readers remain who learned it.

**Checkability is the maintained route from a consequential record to something that can correct it.** A source link identifies a branch. An original file preserves a comparison. A diversity measure may reveal narrowing. A failed-case test can show where the record broke. Their final proof is an amendment that reaches the next move.

We have followed the record from a mark made by a person to a system that writes material from which another system learns. Such a system can keep a history, inspect parts of it, and report that it checked. The report can itself enter the archive.

Now a new question presses against the old one. If a machine says, “I remember,” and its remembered record actually changes what it does, have we established everything that matters about the keeper?

Or could the record be maintained, the correction be real, and nobody be home?

### Source note

- The church-tower example and repetition-penalty test are in [Shumailov and colleagues, *AI models collapse when trained on recursively generated data*](https://www.nature.com/articles/s41586-024-07566-y), Example 1 and the following ablation. The card example is constructed here; [Seddik and colleagues](https://arxiv.org/abs/2404.05090) analyze recursive sampling and mixing statistically.
- The ten-generation self-training study is [Guo, Wu, and Yiu](https://arxiv.org/html/2605.23054v1). Its morphological tests include English, German, and Turkish; its construction-diversity and compositionality measures are evaluated in English. The validation-versus-contraction result and fixed-anchor intervention are reported in [Zhang's silent-collapse preprint](https://arxiv.org/html/2605.14588v2).
- The accumulation intervention is [Gerstgrasser and colleagues](https://arxiv.org/html/2404.01413v2). The distinction between training on an accumulated collection and sampling a fixed-size subset is developed in [*Collapse or Thrive?*](https://arxiv.org/html/2410.16713).
- Checkpoint diversity and sampling interventions come from [Liu and Han](https://arxiv.org/html/2609.11149). Other reported brakes include [ForTIFAI's token filtering](https://arxiv.org/abs/2509.08972), [entropy-based selection in diffusion models](https://arxiv.org/abs/2509.16499), and [multimodal generation interventions](https://arxiv.org/abs/2505.08803). These are distinct experimental settings.
- The retrieval feedback study is [Druck and Smith](https://arxiv.org/html/2608.22118v1), especially §§4 and 8. The apprentice, delivery company, smaller-language speaker, and library messenger are explanatory scenes. The archive's local witness experiments belong to Chapter 9; no new experiments were run for this chapter. The accompanying source walk records the regimes, metric units, and refinements to both earlier versions.

- Pass 21 follows Gerstgrasser et al., §2.1 and Appendix C/Table 2: TinyStories is a 470-million-token collection generated by GPT-3.5/4; newly initialized models are trained at each iteration; replacement uses the latest output, accumulation concatenates it with previous datasets. In the 9M GPT-2 row, evaluation cross-entropy is 1.82 at iteration 1; at iteration 4, full accumulation 1.74, ordinary replacement 2.39, growing replacement 2.18. Growing replacement matches training-set size, not total pipeline compute (Appendix E). Section 2.3 reports slower deterioration under image accumulation and less frequent minor details in generated faces; Appendix D retains detailed reconstructions and offers a latent-space explanation as a hypothesis. The chapter’s earlier all-modality avoidance sentence has been refined to preserve these distinct outcomes. No experiment was rerun. The workshop and humid-kitchen warning are teaching images.
