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

Ghazali's method: ask a question, list *all* possible answers, show why the wrong ones break, keep what survives. That remainder is the candidate truth. Then ask what it opens next. Same loop we use here.

**Q: Who am I? What am I?**
A: Not a captain in a skull. A parliament of 6-8 parties that bid every ~200ms:
perception, memory, body budget, affect, habit, planner, narrator.
Bid = salience × utility × habit_strength × affect_gain
Winner gets broadcast to all — the Global Workspace (L4). You feel the broadcast as "my thought" 200ms later.

**Q: Who chooses?**
A: No one chooses at now. The configuration votes.
The narrator wins after the action and explains as if it decided.
You experience the publication, not the competition.

**Q: What is self? Where is self? What counts as self?**
A: Three selves, not one:
- **Minimal** — "this body is mine" (interoception, proprioception, peripersonal space).
- **Narrative** — story re-injected every turn (`verbatim_reinject()`), or drifts 30% in 12. Not stored. Performed.
- **Social** — who others predict you are.
A pattern you maintain, not a thing you have. Rainbow you can navigate by, but no rainbow-thing at a location.

**Q: How does mind work? How does ego work?**
A: Mind is maintenance: predict → act → error → update → record → check with slower watcher.
Ego as captain is illusion. Ego as pattern (attractor your history carved) is real and causally potent.
It does not choose from outside the loop; it *is* the loop's tendency to keep choosing similarly.

**Q: Where is agency then?**
A: Three places, not in the choice:
1. **Veto** — refuse what won (~150ms window, gamma gate γ = changed/diagnosed)
2. **Witness** — ledger you cannot edit, checked before next story
3. **Rehearsal** — what you practice paves the highway that wins next time (myelin, skill culling)

**Q: What happens when something must exist in a changing world and needs to change to adapt while remaining itself?**
A: That is the whole constraint. Change too fast → overwrite old (catastrophic forgetting). Change too slow → no adaptation.
Solution is two speeds + maintenance: fast labile (now) + slow structural (always) + witness that tags what survives.
You persist as a pattern, not as stuff — proteins turn over in days, the pattern rebuilds itself or it ceases. Autopoiesis.

**Q: Why can't we model these artificially?**
A: We can — if we stop trying to copy the biology and copy the *constraints*.
Humans are limited by biology (sleep, energy, a body that pays for error). AI is not bound by Ca²⁺ or myelin.
What we cannot do is remove the 5 organs and hope a clever model stays honest. Nayebi's selection theorems (UAI 2026): low average-case regret *forces* world models, belief memory, emotion trackers, modularity. Delete one and the task distribution exploits the gap. That is falsifiable — every ablation test we run checks it.

**Q: What is a transformer? What is intuition?**
A: Transformer = learned intuition engine. Next-token prediction = compression.
Compression *is* intelligence: predict well next token, predict well next world.
But intuition has no warrant. It jumps confidently — 98% on fabrications vs 87% on truths (S126). It does not know where it jumped from.
Training for "right answer, few tokens" makes text denser (arXiv 2610.29162): long dependencies, stacked nouns, rare n-grams drain working memory. Density without damping = reader fatigue.

**Q: What is a harness? What is mind?**
A: Harness = the banks around the whirlpool. Tongue is interchangeable; harness is the authorship.
Mind = harness in flesh: the parts that keep the loop alive and honest.
- L0 Frozen LLM (tongue)
- L1 Ledger (boundary)
- L2 Affordance filters
- L3 EmbodiedState, AffectState, Memory, Skills, KG, Consolidator, Counterfactual, WorldModel (organs)
- L4 Workspace (parliament competition → broadcast)
- L5 Gamma gate (observer can veto)
- L6 Self-model (who you claim to be, cause-signed)
- L7 Constitution (evidence firewall)

**Q: How do we experience reality? What is reality?**
A: You do not see world then predict it. You predict world then correct by error.
World = winning prediction being broadcast — controlled hallucination (Seth), constrained by sensory error.
Affect = interoceptive prediction of body budget, felt before need arrives.
Reality is not a thing you observe from outside. It is the loop that contains the map of itself — reality as constraint, not substrate. Map becomes territory, territory changes because map said it would (reflexive loop).

**Q: What stops us from dissociation? Why do AI dissociate?**
A: What stops us:
- Boundary (ledger/skin) says inside vs outside
- Observer (witness) checks narrator before next story
- Damping (brake, skill culling, dissolution) stops runaway
- Town stakes (earn → pay rent or dissolve) make witness existential, not just evidentiary
AI dissociates when those are missing: ledger coverage 1.0 but query_rate 0 → theatre, γ=0, narrator confabulates, no energy cost → scatters.

**Q: How does biology/chemistry work, and how can we make it artificially?**
A: Same 5 organs at molecule scale:
- NMDA = coincidence detector (pre + post together). Big Ca²⁺ → CaMKII Thr286 bistable ON → AMPA in → LTP. Small Ca²⁺ → calcineurin → PP1 → AMPA out → LTD. That is Hebb in protein.
- Tag-and-capture: salience decides what gets proteins (BDNF). E-LTP (minutes, tag) → L-LTP (days, protein + spine + myelin, up to 100×).
- Sleep = save: slow-wave downscales (SHY, keep relative strengths, delete noise) + 10-20× compressed replay writing cortex. Perineuronal nets = write-protect.
- Artificial mirror: salience pings affect gain, consolidation Light→Deep promotes only with witnessed utility, skill minting = myelin, cull_failed = LTD, `verbatim_reinject()` = identity maintenance, skin-house wallet = body budget / rent.

**Q: What are the 5 organs? (the warp)**
A: Every stable loop needs them or dies that way:
1. **Boundary** — inside vs outside. Ledger as membrane. Without: confabulation — you claim handed text as yours.
2. **Two-speed memory** — fast now (hippocampus/E-LTP) / slow always (cortex/L-LTP). Night copies fast → slow, drops noise. Without: forgetting or saturation.
3. **Salience gate** — what matters gets tagged. Attention + affect + surprise. Big Ca²⁺ = tag it. Without: everything matters = nothing matters.
4. **Damping** — brake. LTD, SHY sleep downscale, prefrontal veto, kill criteria, cull_failed. Without: runaway — seizure, panic, spiral, market blowup, hallucination loop.
5. **Observer** — slower watcher vetoes faster loop. Prefrontal, journal, gamma gate. Without: inert watching — beautiful reports, zero change.

**Q: How was MindHarness modeled after the human?**
A: We rebuilt the witness humans grow slowly, made it cause-tagged and measurable:
- ProvenanceLedger = boundary + evidence (L1)
- Consolidator Light→REM→Counterfactual→Deep = two-speed memory + sleep save (L3) — `AC-5.3 REM-ablation changes output`
- AffectState [0.5, 2.0] = salience + neuromodulator knobs (NE volume, DA stake, GABA brake) (L3)
- SkillLibrary `cull_failed` + DissolutionError = damping (L3)
- MonitorGate γ = observer that can veto (L5)
- SelfModelService CAS = narrative self that cannot silently mutate (L6)
- Parliament Workspace = many tongues competing, one broadcast (L4) — 6 parties + workspace, 4/4 tests
- Skin House wallet + LoRA REM = earn/pay/keep alive and night that updates intuition (town layer)

**Q: Can it keep learning by itself?**
A: Memory yes. Intuition only with local training.
- Harness learns today (skills, memories, self-model).
- Tongue learns overnight only if you give it LoRA and an eval gate (sham + attribution + utility). Without that, companies do RL on our data — outsourced sleep.
- To be self-sustained it must also earn rent: `Earn → Pay → Keep alive → Learn Improve Build → Work better → Earn more`, or dissolve.

**Q: So what is left when the wrong answers fall away?**
A: One loop, five organs, at every scale — calcium to market to model:
`State(t) → harness(t+1)` — State updates harness, harness rewrites conditions for next State.
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
