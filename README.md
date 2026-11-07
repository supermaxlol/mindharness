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

**Q: So what is left when the wrong answers fall away?**

A: One loop, five organs, at every scale — **State(t) → harness(t+1)**.
State updates harness. Harness rewrites the conditions for next State.
With a witness you cannot edit and a slower watcher that can veto the faster one, the loop can check its own directions.
That is not a better narrator. It is a reliable witness.

---

## Research docs

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
