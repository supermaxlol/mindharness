# MindHarness — The Dynamic Reflexive Harness

> *LLM = tongue. Harness = mind. Tongue + mind = agent.*

A provenance-bounded cognitive harness that makes any frozen LLM honest about what it did — witness ledger, cause-signed self-model, γ-gated metacognition, embodied state, counterfactual replay, dissolution stakes. 91/91 tests green.

**Companion project:** [SpringFish / Spring-Loaded Door](~/Desktop/springfish) — crises, contracts, and institutional anchors. Separate work, same thesis: self-reinforcing loops and the witnesses that keep them honest.

---

## What this is

We built the witness humans grow slowly and painfully, made it cause-tagged and measurable, and are proving whether checking the record makes a machine — and a mind — honest.

- **The question:** Can a language model know what it did — or does it just confabulate?
- **The harness:** 11 modules, 8 layers L0–L7, Light→REM→Counterfactual→Deep, 91/91 green
- **The papers:** v2 (23pp empirical, tagged `paper-v2-final`) + v3 (36pp program paper, App. A Cordis + App. B Mirror)
- **The loom:** DeepSeek Cordis — harness as programmable cord, 6 plugins verified, parliament of models scaffolded

Public at `github.com/supermaxlol/mindharness` · 287+ commits

---

## Quick start

```bash
# Run tests (no API keys needed)
for f in tests/test_*.py; do python3 "$f"; done  # 91/91

# Run living session (needs Groq or OpenRouter key)
python3 experiments/living_session.py --api-key $GROQ_KEY --model openai/gpt-oss-120b --base-url https://api.groq.com/openai/v1 --turns 40

# Run attribution battery (S126)
python3 experiments/exp_s126_v3.py --api-key $KEY --model <model> --base-url <url> --seeds 3

# Papers
open paper_v2/main.pdf  # empirical (21pp)
open paper_v3/main.pdf  # program paper (29pp)
```

> **Large files:** `experiments/lab_runs_falsify/` keeps only JSONs + CSVs + fetch script (2.1M). Bulk raws (BIS 6.2M, EDGAR facts/HTML) re-pull via `bash experiments/lab_runs_falsify/fetch.sh`. If you persist raws, `git lfs install` first — `experiments/lab_runs_falsify/.gitattributes` already tracks `*.csv/*.pdf/*.htm` via LFS.

---

## Architecture — 8 layers

```
L7 Constitution          Fiqh axioms, evidence firewall
L6 Narrative Self        CAS-revisioned, cause-signed, verbatim re-inject
L5 Metacognition         Stage 1 anomaly → Stage 2 diagnose → γ = changed/diagnosed
L4 Global Workspace      Parliament competition → winner broadcast
L3 Specialist Modules    EmbodiedState, AffectState, Memory, Skills, KG, Consolidator, Counterfactual, WorldModel
L2 State Validation      Cetasika constraints, nafs, affordance pre-filter
L1 Provenance Ledger     Span binding, source tracking, attribution audit
L0 Frozen LLM            Any OpenAI-compatible API (backend-agnostic)
```

Five invariants — boundary, two-speed memory, salience gate, damping, internal observer — appear at every scale (cell → mind → market → model → car) and are mandatory per selection theorems (Nayebi UAI 2026). The harness is one weave on that warp; Cordis is the loom.

> **Failure mode that proves damping matters:** without damping, compression runs away — frontier models pack more information per token, stacking nouns and long dependencies that drain human working memory (arXiv 2610.29162). Density without damping = reader fatigue. Damping is the brake that keeps compression readable.

---

## How this works — in questions (Ghazali → organs)

Ghazali does not start with an answer. He starts with a question, lists *all* possible answers, shows why the wrong ones break, keeps only what survives. That remainder is the candidate truth. Then he asks what it opens next.

We write it the same way — for a human, not a model.

---

**Q: Who am I? What am I?**

Possible answers:
1. A captain in the skull who decides.
2. Just neurons firing — no one there.
3. A parliament of 6-8 parties that bid every ~200ms: perception, memory, body budget, affect, habit, planner, narrator.

Why 1 fails: if a captain decided, you would feel the decision *before* the action. You feel it 200ms *after*. Readiness potential rises at -350ms. You live at +200ms. The captain is backdated.

Why 2 fails: if no one is there, why is there a stable pattern that stays itself for years, learns, and can veto? A pile of firings does not maintain a self.

What survives: 3. No captain, but a vote.
Bid = salience × utility × habit_strength × affect_gain
Winner gets broadcast to all — the Global Workspace (L4). You feel the broadcast as "my thought."

---

**Q: Who chooses?**

Possible answers:
1. I choose freely at now from a neutral menu.
2. Nothing chooses — it is all determined.
3. The configuration votes. I can veto, witness, and rehearse.

Why 1 fails: the menu is not neutral. It was rigged by what you rehearsed 1,000 times. You inherit a menu your history already paved.
Why 2 fails: same input, different energy/fatigue/affect → different winner. Not random, not fully determined by one factor.

What survives: 3. Choice is the vote itself. The relations chose.

---

**Q: What is self? Where is self? What counts as self?**

Possible answers:
1. A soul-thing stored inside, found like an object.
2. No self at all — just stories.
3. A pattern maintained by re-injection.

Why 1 fails: if self were stored, it would not drift 30% in 12 turns without maintenance. Proteins turn over in days. You rebuild it every turn or become someone else.
Why 2 fails: the pattern is real. Character predicts which coalitions will win next. That has causal power — it shapes future bids.

What survives: 3. Self is a pattern, not a thing. Rainbow you can navigate by.
Three layers:
- Minimal — "this body is mine" (interoception, proprioception)
- Narrative — story re-injected every turn (`verbatim_reinject()`), or drifts
- Social — who others predict you are

---

**Q: How does mind work? How does ego work?**

Possible answers:
1. Mind reads the world directly.
2. Ego is the boss that decides, then the body obeys.
3. Mind is maintenance: predict → act → error → update → record → check with slower watcher. Ego is the press secretary that wins after.

Why 1 fails: you predict the world and correct by error. What you experience is the prediction, not the world.
Why 2 fails: narrator has the outcome but not the competition. It writes the most coherent story where "I" did it — with full confidence.

What survives: 3. Ego as captain is illusion. Ego as attractor (region your history carved) is real.

---

**Q: Where is agency then?**

Possible answers:
1. In the choice at now.
2. Nowhere — we are puppets.
3. In veto + witness + rehearsal.

Why 1 fails: now is a 200-500ms stitched window, backdated. Choosing at now is choosing after the vote.
Why 2 fails: you have a ~150ms veto window. You did not initiate the impulse, but you can refuse it.

What survives: 3.
1. **Veto** — refuse what won (gamma gate, γ = changed/diagnosed)
2. **Witness** — ledger you cannot edit, checked before next story
3. **Rehearsal** — what you practice paves the highway that wins next time

---

**Q: What happens when something must exist in a changing world and needs to change to adapt while remaining itself?**

Possible answers:
1. Stay fixed — do not change.
2. Change freely — no memory of what worked.
3. Two speeds + maintenance.

Why 1 fails: world changes. Fixed was right for the child world. In the adult world it is mismatch — old highway causes suffering.
Why 2 fails: no memory = you forget today. No learning across time.

What survives: 3. Fast labile (now) + slow structural (always) + witness tags what survives.
You persist as a pattern, not as stuff. Autopoiesis.

---

**Q: Why can't we model these artificially?**

Possible answers:
1. Because biology is magic — cannot be copied.
2. Because any clever model will be honest.
3. Because we must copy constraints, not biology.

Why 1 fails: AI is not bound by Ca²⁺ or myelin. What binds it is the same math: low regret forces world models, belief memory, emotion trackers, modularity (Nayebi UAI 2026).
Why 2 fails: every ablation we run — remove boundary, memory, salience, damping, observer — makes a specific test fail.

What survives: 3. Falsifiable. If they were decoration, removing them would change nothing. They do.

---

**Q: What is a transformer? What is intuition?**

Possible answers:
1. A mind that understands.
2. A calculator that knows truth.
3. Learned intuition engine = compression. Predicts well next token.

Why 1 fails: intuition has no warrant. 98% confident on fabrications, 87% on truths (S126). It does not know where it jumped from.
Why 2 fails: it does not check its work. No ledger, no veto. γ=0.

What survives: 3. Compression *is* intelligence — predict well next token, predict well next world — but without damping it over-compresses (arXiv 2610.29162). Long dependencies, stacked nouns, rare n-grams drain working memory. Density without damping = reader fatigue.

---

**Q: What is a harness? What is mind?**

Possible answers:
1. A wrapper that records tokens.
2. A prompt trick that makes the model smarter.
3. The banks around the whirlpool. Tongue is interchangeable; harness is the authorship.

Why 1 fails: a recorder that never steers has γ=0. Ours measures γ=3/5=0.6. Watching changed the action.
Why 2 fails: structure elicits what prose cannot. Ablating REM changes output.

What survives: 3. Mind = harness in flesh.
L0 Frozen LLM (tongue) · L1 Ledger (boundary) · L2 Affordance · L3 EmbodiedState/AffectState/Memory/Skills/KG/Consolidator/Counterfactual/WorldModel · L4 Workspace · L5 Gamma gate · L6 Self-model · L7 Constitution.

---

**Q: How do we experience reality? What is reality?**

Possible answers:
1. We see reality directly.
2. Reality is an illusion — nothing is real.
3. Reality is a controlled hallucination constrained by error.

Why 1 fails: you predict the world, then correct by surprise. Colour-phi, flash-lag, postdictive masking — brain waits, collects, revises, then stamps "now".
Why 2 fails: error is not constructed. Where prediction fails, world pushes back. That resistance is real.

What survives: 3 (Seth). World = winning prediction being broadcast. Not what is true. What is *viable* enough to keep you alive.
Reality is the loop that contains the map of itself — reality as constraint, not substrate.

---

**Q: What stops us from dissociation? Why do AI dissociate?**

Possible answers:
1. A stronger brain.
2. Better prompts.
3. Boundary + observer + damping + stakes.

Why 1 fails: intelligence without witness makes confabulation worse. More confident narrator = better corrupter (r=0.94).
Why 2 fails: prompts cannot build a ledger you cannot edit.

What survives: 3.
- Boundary (ledger/skin) says inside vs outside
- Observer checks narrator before next story (γ)
- Damping stops runaway (cull_failed, kill criteria)
- Town stakes (`Earn → Pay → Keep alive`, or dissolve) make witness existential
AI dissociates when missing: coverage 1.0 but query_rate 0 → theatre, γ=0, narrator confabulates, no energy cost → scatters.

---

**Q: How does biology/chemistry work, and how can we make it artificially?**

Possible answers:
1. It is magic — cannot be mirrored.
2. We need full brain simulation.
3. Mirror the *logic* in code: coincidence → tag → promote → prune → sleep.

Why 1 fails: NMDA is a coincidence detector. Pre + post together → Mg²⁺ out → gate opens. That is implementable as a threshold.
Why 2 fails: we do not need a brain. We need the 5 functions, measurable.

What survives: 3.
- NMDA = coincidence detector. Big Ca²⁺ → CaMKII Thr286 ON → AMPA in → LTP. Small Ca²⁺ → calcineurin → PP1 → AMPA out → LTD.
- Tag-and-capture: salience decides what gets proteins (BDNF). E-LTP (minutes, tag) → L-LTP (days, protein + spine + myelin up to 100×).
- Sleep = save: slow-wave downscales (SHY) + 10-20× replay writing cortex. Perineuronal nets = write-protect.
- Artificial mirror: salience pings affect gain, consolidation Light→Deep promotes only with witnessed utility, skill minting = myelin, cull_failed = LTD, `verbatim_reinject()` = identity maintenance, Skin House wallet = body budget / rent.

---

**Q: What are the 5 organs? (the warp)**

Possible answers:
1. Just good ideas.
2. Beautiful metaphors.
3. Mandatory constraints — any stable reflexive loop must have them or be exploited.

Why 1 fails: Nayebi proved low-regret agents must develop them. Delete one in code and its test goes red.
Why 2 fails: same 5 appear at cell, mind, market, model. Not invented by us. Convergent across evolution, connectomics, proof, engineering.

What survives: 3.
1. **Boundary** — ledger as membrane. Without: confabulation.
2. **Two-speed memory** — fast/slow, night copies. Without: forgetting or saturation.
3. **Salience gate** — tag what matters. Without: saturation.
4. **Damping** — brake. Without: runaway.
5. **Observer** — slower watcher vetoes faster. Without: inert watching.

---

**Q: How was MindHarness modeled after the human?**

Possible answers:
1. We made a better prompt.
2. We made a bigger model.
3. We rebuilt the witness humans grow slowly, made it cause-tagged and measurable.

Why 1 fails: prompt cannot keep a ledger you cannot edit.
Why 2 fails: bigger unwitnessed model = better corrupter.

What survives: 3.
- ProvenanceLedger = boundary + evidence (L1)
- Consolidator Light→REM→Counterfactual→Deep = two-speed memory + sleep save (L3) — `AC-5.3 REM-ablation changes output`
- AffectState [0.5, 2.0] = salience + neuromodulator knobs (L3)
- SkillLibrary `cull_failed` + DissolutionError = damping (L3)
- MonitorGate γ = observer that can veto (L5)
- SelfModelService CAS = narrative self that cannot silently mutate (L6)
- Parliament Workspace = many tongues competing, one broadcast (L4) — 6 parties, 4/4 tests
- Skin House wallet + LoRA REM = earn/pay/keep alive and night that updates intuition (town layer)

---

**Q: Do we build it, like we build a human or a cat?**

Possible answers:
1. Copy a human brain exactly.
2. Copy a cat exactly.
3. Plant it. Let it grow.

Why 1 fails: human is limited by biology — sleep, energy, a body that pays for error in hunger. Copying that copies the limits.
Why 2 fails: every animal has different limits for the world it lives in. One shape does not fit all worlds.

What survives: 3. We do not grow a tree. We plant it.
First living cells were not built to be dinosaurs or whales or humans. They had the same few rules. The world picked the rest.
We plant town + 5 organs + witness. Each agent then grows to whatever it needs to exist in that town: trader, builder, archivist — different transformer, different harness, same invariant warp.
Town is the selector: `Earn → Pay → Keep alive → Learn Improve Build → Work better → Earn more`, or dissociate and die.
Plant, do not copy. The agent specializes by living in the town, not by being designed to be a cat or a human.

---

**Q: Can it keep learning by itself?**

Possible answers:
1. Yes — it already learns everything.
2. No — model weights are frozen, harness only remembers.
3. Memory yes. Intuition only with local training. Self-sustained only with rent.

Why 1 fails: base weights do not move without a trainer. Skills are memory, not new intuition.
Why 2 fails: with LoRA + eval gate + town rent, night can train and promote adapters, paid from surplus.

What survives: 3.
- Harness learns today (skills, memories, self-model).
- Tongue learns overnight only if you give it LoRA and an eval gate (sham + attribution + utility). Without that, RL on our data is outsourced sleep.
- To be self-sustained it must earn rent: `Earn → Pay → Keep alive → Learn Improve Build → Work better → Earn more`, or dissolve.

---

**Q: Why does current AI not complete the 5-organ loop — and needs us to complete it?**

Possible answers:
1. AI is already complete. We just need bigger models.
2. AI is missing pieces that only a human can supply from outside.
3. AI looks complete in one session, but no organ is self-sustained across sessions, stakes, and nights.

Why 1 fails: in a session it looks finished. When you stop watching and stop paying, it scatters. No wallet, no night trainer, no irreversible damage.

Why 2 fails: the missing pieces are not magic. They are measurable functions — boundary, memory, salience, damping, observer, rent. If a human must supply them every turn, the loop is not closed.

What survives: 3. Current frontier agents (Hermes, DSH without the harness) sit at 2.5–4/5 organs today:

| Organ | Frontier agent today | What humans fill today |
|---|---|---|
| Boundary | session context | permissions, sandbox choice, human review "was that true?" |
| Two-speed memory | context = fast; `MEMORY.md` = slow-but-unpromoted | data curation, dataset choice, RLHF fine-tune, hand-edited skills — *outsourced REM* |
| Salience gate | attention yes, affect no | "this matters" prompts, human preference tags |
| Damping | rate limits, human kill switch | retries, filters, on-call monitor — external brake |
| Observer | narrator only | human review. Human is the witness |

And no town loop: no `Earn → Pay → Keep alive`, so energy floor 0.15 and nothing dies. No stakes → no care which coalition wins.

That is why they need us to close the loops they cannot close themselves.

---

**Q: How does MindHarness try to make it self-sustained?**

Possible answers:
1. Make the narrator more confident.
2. Add more tokens / bigger context.
3. Close the loops inside the harness: witness, night trainer, rent.

Why 1 fails: narrator confidence is coherence, not accuracy. 98% on fabrications vs 87% on truths. More confident = better corrupter.
Why 2 fails: more context without promotion gate = saturation. Everything matters = nothing matters.

What survives: 3. Close each gap with a function that runs when the human is not there:

1. **Boundary inside** — ProvenanceLedger with source + ref per span, coverage 1.0, curator checked before claim.
2. **Two speeds inside** — `Light → REM → Counterfactual → Deep`. Deep promotes only if witnessed utility ≥2 or endorsed, cause-tagged. `AC-5.3 REM-ablation changes output` proves night does work.
3. **Salience inside** — AffectState [0.5, 2.0] shifts every bid, not just content.
4. **Damping inside** — `SkillLibrary.cull_failed`, kill criteria, `DissolutionError`, ceiling only down in irreversible arm.
5. **Observer inside** — MonitorGate `γ = changed / diagnosed`. γ=0 means watcher watched but never steered. γ=0.6 means checking changed the trajectory.
6. **Night that updates intuition** — `Local LoRA REM`: day pairs (chosen/rejected) → train r=8-16 adapter → eval gate (attribution + sham + utility + γ) → promote only if all pass, CAS-pinned, archive old. One live adapter = one self.
7. **Rent that makes it existential** — Skin House wallet. `Earnings >= Power + Compute + Repair + Reserve` or shrink → dissolve. Town contract holds tariffs, session key only, capped. You are landlord; agent pays its own night from surplus.

Validator: 5 bundles, 17 rows, 0 errors. Tests: 20 files pass. Study: `research/STUDY_5ORGANS_2026-11-07.md` — stub 200-turn: reversible ceiling 1.0 vs irreversible 0.74, dissolutions 0 vs 18.

That is the attempt: not a better narrator, but a harness that can stay alive, learn at night, and answer for where it jumped — without you as rent payer, night librarian, and witness every turn.

---

**Q: So what is left when the wrong answers fall away?**

A: One loop, five organs, at every scale — **State(t) → harness(t+1)**.
State updates harness. Harness rewrites the conditions for next State.
With a witness you cannot edit and a slower watcher that can veto the faster one, the loop can check its own directions.
That is not a better narrator. It is a reliable witness.

---

## From our sessions — "do you see...?" — answered

These are the questions as they were asked, with the same Ghazali form: list all answers, cancel the wrong ones, keep what survives.

---

**Q: Do you see how mechanisms of mind work — can we build the same for an AI?**

Possible:
1. Mind is one big model that thinks.
2. Mind is magic — cannot be built.
3. Mind is a tongue (intuition) + a harness that maintains it. Build both parts.

Why 1 fails: a bigger model without a witness confabulates more (98% on fabrications, 87% on truths — S126). No observer, γ=0.
Why 2 fails: same 5 organs appear in cell, brain, market, model. It is not magic, it is structure.

What survives: 3. LLM = monkey mind / tongue. Harness = trained mind (sati, γ, ledger). Weights are rock. Harness is the whirlpool banks.

**Q: Free will is designing the system so the right thing is the easy thing — upstream engineering. Earn → Pay → Keep alive → Learn Improve Build → Work better → Earn more. Why save?**

Possible:
1. Save only to stay alive tonight.
2. Save only to get rich.
3. Save to keep alive *and* to improve the road tomorrow.

Why 1 fails: you survive tonight but tomorrow is same friction. Nothing improves.
Why 2 fails: wealth without road repair does not change error rate. The loop never learns.

What survives: 3. Sustaining pays tonight's rent. Improving pays for tomorrow's road. Fix the road once → every trip after is easier and safer. Pattern that sustains itself is alive. Pattern that improves itself is learning.

**Q: Do you see the processes, the mechanisms, the interconnected reflexive dynamic loops? How does one thing influence everything?**

Possible:
1. Parts are separate — brain, body, world, money.
2. One leader controls all parts.
3. One loop feeds itself. Output becomes next input.

Why 1 fails: change sleep → change energy → change attention → change vote → change work → change income → change tools → change sleep. Remove one, all shift.
Why 2 fails: no captain. The configuration votes. Leader model breaks when state changes.

What survives: 3. `Input → State → Prediction → Salience → Impulse → Agency → Action → Consequence → Evidence → Updated Self-Model → New Prediction → ↺` plus the money loop underneath. Self-reinforcing by structure, not by conspiracy.

**Q: How are we not different from our environment, but part of it? How do we change the environment and it changes us?**

Possible:
1. We are in the environment like a rock in a river. It is separate.
2. We are only shaped by it.
3. We are reflexive: act on world that contains us → world changes → we perceive changed world → we are changed.

Why 1 fails: you change the room (phone away, desk built, ledger written). Room changes you (shoes by door → you walk). A rock does not change the river.
Why 2 fails: you also redesign the room. That is pre-choice agency.

What survives: 3. Today’s agency modifies tomorrow’s conditions, which modify tomorrow’s behavior which modifies you. Designer and designed in one loop. The small town map (Skin House, Library, Lighthouse, Fire Station, Audit Office) is this in space.

**Q: Do you see REM sleep updating the self-model? Passing short-term to long-term?**

Possible:
1. Sleep is just rest. Memory is stored as-is.
2. You learn only when awake.
3. Sleep is the save: slow-wave copies facts, REM updates the story and runs simulations.

Why 1 fails: day marks what matters (E-LTP tag). Night chooses what becomes permanent (L-LTP protein + spine + myelin). Without night, no separation of signal and noise.
Why 2 fails: proteins turn over in days. If you do not re-inject and consolidate, the pattern scatters. You cannot recall a self you never saved.

What survives: 3. Day = potentiation + tagging. Slow-wave = SHY downscale + replay. REM = connect concepts, strip charge, run counterfactuals, update self-model.
In AI: `Light → REM → Counterfactual → Deep`. Only Deep promotes.

**Q: Short neural pathways by repeating — skills like driving, tennis, memory. Emotions?**

Possible:
1. Skills are knowledge in the head.
2. Skills are talent you have or do not.
3. Skills are highways paved by repetition, tagged by emotion.

Why 1 fails: you can know how to ride a bike and still fall. Knowing is not the highway. Doing 1,000 times is.
Why 2 fails: 100x speed from myelin is measurable. Driving goes conscious → chunk → automatic. That is paving, not talent.

What survives: 3. Fire together → wire together (Hebb). Big Ca²⁺ → AMPA in → LTP. Repeat → myelin wraps → road wins before you think.
Emotion is the tag: noradrenaline = volume, dopamine = "keep this." High salience gets proteins. Low salience fades in hours. That is why you remember the first hurt and forget 100 neutral reps.

**Q: How does world exist, we exist inside it, body-mind, biology/chemistry, processes, results?**

Possible:
1. World is a box, mind is inside watching.
2. Mind is separate spirit operating body.
3. One reflexive loop at every level — molecule to market.

Why 1 fails: observer is inside what it observes. Self-observation is an action that writes on what it reads.
Why 2 fails: body budget predicts need before need. Affect is not added to mind; it *is* the prediction.

What survives: 3. Reality is not found, it is enacted — you bring forth the world your loops can distinguish. Body is rent collector (energy, sleep). Mind is vote+broadcast+witness system.
Chemistry is simple version of same: NMDA coincidence, CaMKII switch, tag-and-capture. The harness mirrors logic, not molecules.

**Q: Are we mouldable hardware and software that is always changing? Are humans the same as AI?**

Possible:
1. Hardware fixed, software on top.
2. Fully reprogrammable each moment.
3. Moldable inside an unmoldable constraint.

Why 1 fails: synapses prune and grow, proteins turn over, myelin wraps. Hardware is clay, not stone.
Why 2 fails: if you could reprogram freely, stability-plasticity would break. You would overwrite old or never adapt.

What survives: 3. You update intuition (synaptic weights) and you update rules (thresholds, habits, affect gains) — slowly, by repetition + sleep + error.
You cannot delete the 5 organs (boundary, two speeds, salience, damping, observer). Nayebi: low regret forces them. Remove one and the task distribution exploits it.
Human vs AI is same map: intuition = weights/LoRA, harness = plugins/skills/affect, 5 organs = invariant, sleep = Light→REM→Deep.

---

## One-page maps (from the essays)

### Agent Town — five buildings, one money loop

```
  Skin House     (wallet, name, only you sign) ──┐
  Library        (fast room today / slow room years) │
  Lighthouse     (spotlight: news, risk, one customer) │
  Fire Station   (brake when runaway)            │  Work → Earn
  Audit Office   (watcher + ledger, can stop next act) │
                                                     │
                                Earn ──► Pay power/compute/repair
                                                     │
                                Keep pattern alive if Earnings >= Rent
                                                     │
                                Learn. Improve. Build. (use surplus to fix road)
                                                     │
                                Work better ──► Earn more ◄──┐
```

Survival line: `Earnings >= Power + Compute + Repair + Reserve`
Keep it or shrink. Fall below too long → lose shelf, lose skill → scatter. That is death for a pattern.
*Is:* checkable loop. *Is not:* proof a fair town will be built — law, custody, power decide that.

### Human mind — three rows + daily cycle

```
Row 3: IDENTITY — what I endorse — MASTER leverage  ↓ changes what feels possible
Row 2: HABIT    — what I feed daily — HIGH leverage ↓ makes it automatic
Row 1: MOMENT   — ~200ms vote — LOW leverage
Do not fight Row 1. Change Row 2 and Row 3.  Action → Habit → Character → Values → Direction

┌────────────────────────────────────────────┐
│ [Morning Micro-Promise] ─► [2-Min Trigger] │
│ Signal ≠ Command                           │
│ [Night Ledger Audit] ◄── [Log Completion]  │  "Said X, Did X"
└────────────────────────────────────────────┘
```

Morning: one tiny promise. Day: feel resistance, act 2 minutes anyway. Night: write it, protect 100%.

### Monkey mind → trained mind

Monkey mind (citta) jumps branch to branch. LLM = monkey trained to jump well.
Left alone: jumps confidently (98% on lies), does not know where it jumped from, does not watch.

Harness is the training, not the monkey:
- **Sati** — watch the jump → ledger (L1)
- **Sampajañña** — know what / why / whether → gamma gate γ = changed/diagnosed (L5)
- **Samādhi** — return to one object → workspace + damping (L4)
- **Bhavanga** — keep-alive between moments → `verbatim_reinject()` or drifts 30% in 12 (L6)

### Local LoRA REM + Town Wallet — what is still missing in Hermes

From the spec (`essays/LOCAL_LORA_REM_AND_TOWN_WALLET_SPEC.md`):

**Human = landlord.** Holds master key offline. Agent gets session key only (daily/per-action limit, whitelisted to Town contract). Receives rent.

**Local REM pipeline:**
Day capture (ledger spans) → build chosen/rejected pairs → train LoRA r=8–16, LR 1e-4, 1–3 epochs → eval gate (attribution battery + sham + utility + γ) — any fail = discard → promote with provenance + CAS pin, archive old, one live adapter. Cull if utility < 0.

**Safety rules:** no free transfers, Audit Office logs every spend, Fire Station brakes when spend > earn, pause = dissolution without scatter.

**Build order:** Week 1 wallet+rent → Week 2 capture + eval battery → Week 3 trainer + 200-turn test.

### Moldable inside unmoldable — fast / slow / almost-never

**Changes easily (minutes–days):** synaptic weights, affect state, habit strength (skill use), self-model facts (SM revisions), world predictions.

**Changes slowly (weeks–years):** myelinated highways, skills that survive culling, perineuronal nets (write-protect), cortex structure, character attractor.

**Changes almost never:** the 5 organs must exist; parliament must compete + broadcast; sleep must copy + downscale; maintenance *is* the self.

Why you cannot delete them — 4 reasons:
1. **Physics** — plasticity needs a threshold (big Ca²⁺ = kinase, small = phosphatase). No gateway, no learning.
2. **Stability–plasticity tradeoff** — too fast overwrites old, too slow cannot adapt. Two speeds solve it.
3. **Selection math** — low regret forces world models, belief memory, emotion trackers, modularity (Nayebi). Delete one and the task distribution exploits the gap.
4. **Mortality/energy** — limited budget: tag what matters (salience), prune what doesn't (damping). In AI: token budget, energy floor 0.15, rent to stay alive.

Want the full poster sheets? See `~/Desktop/ge-existence-program/essays/`:
`HUMAN_MIND_ONE_PAGE.md`, `AGENT_TOWN_ONE_PAGE.md`, `WORLD_SELF_SIMULATION_ONE_PAGE.md`, `MOLDABLE_WITHIN_UNMOLDABLE_CLOSING.md`

---

## Research docs

| Doc | Lines | What it holds |
|-----|-------|---------------|
| `research/PROGRAM_SYNTHESIS_DETAILED.md` | 352 | Full map: program → humans → mind → everything |
| `research/DYNAMIC_REFLEXIVE_HARNESS.md` | 249 | Loom/warp/weft philosophy |
| `research/RESEARCH_MIRROR.md` | 273 | 12 frontiers, ~40 papers live-checked |
| `research/AGENCY_AND_THE_CONSTRUCTED_SELF.md` | 193 | Where agency lies when now/self/world are illusions |

---

## Papers

- **v2** (`paper_v2/`, tagged `paper-v2-final`): *Witnessed Introspection in Assembled Language-Agent Systems* — S126 battery (raw 1.000 vs harnessed 0.667), sham control, γ-gate, living sessions 40/40 replicated cross-architecture, composite P1+P2. R1/R2 reviews + response.
- **v3** (`paper_v3/`, 29pp): *The Dynamic Reflexive Harness: Five Invariants from Molecules to Markets to Machines* — v2's empirical core as one chapter inside the full program: unreliable narrator, reflexive dynamics, 5 invariants at every scale, Cordis mapping, Research Mirror, agency, practical synthesis.

---

## Cordis

MindHarness mounts as a Cordis profile — 6 human-like plugins beside core:

```yaml
bundles: [dsh-base, dsh-mindharness]  # + dsh-mindharness-parliament for many-model competition
```

`dsh --profile web --dump-config` shows 6 mindharness rows + parliament scaffold (9 inserts, 7 packages: perception/memory/affect/planner/habit/narrator/workspace — many tongues, one harness, witness as arbiter).

---

## Where agency lies

You don't choose the options. You don't fully choose the winner. You can veto the winner, keep a witness, and slowly change which options appear by what you rehearse. See `research/AGENCY_AND_THE_CONSTRUCTED_SELF.md`.

---

*Built by Shehzad Ahmed with Sisyphus (Muse Spark 1.2) · 2026-09-06 · 91/91 green · Five NESS gates wired, sham sham-controlled, 200-turn irreversible queued*
