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

---

## How this works — in questions

**Q: What is a mind?**
A: Not a captain. A parliament.
6-8 parties bid every ~200ms: perception, memory, body budget, affect, habit, planner, narrator.
Bid = salience × utility × habit_strength × affect_gain
Winner gets broadcast to all — the Global Workspace. You feel the broadcast as "my thought" 200ms later.

**Q: Who chooses?**
A: No one chooses at now. The configuration votes.
The narrator wins after the action and explains as if it decided.
You experience the publication, not the competition.

**Q: Where is agency then?**
A: Three places, not in the choice:
1. **Veto** — refuse what won (~150ms window, gamma gate)
2. **Witness** — ledger you cannot edit, checked before next story (`γ = changed / diagnosed`)
3. **Rehearsal** — what you practice paves the highway that wins next time (myelin, skill culling)

**Q: What is the self?**
A: Three selves, not one:
- Minimal self — "this body is mine" (interoception, proprioception)
- Narrative self — story re-injected every turn (`verbatim_reinject()`), or drifts 30% in 12
- Social self — who others predict you are
A pattern you maintain, not a thing you have.

**Q: What are the 5 organs?**
A: Every stable loop needs them or it dies that way:

1. **Boundary** — inside vs outside. Ledger as membrane. Without: confabulation — you claim handed text as yours.
2. **Two-speed memory** — fast now (hippocampus/E-LTP, context) / slow always (cortex/L-LTP, semantic). Night copies fast → slow, drops noise. Without: forgetting or saturation.
3. **Salience gate** — what matters gets tagged. Attention + affect + surprise. Big Ca²⁺ = tag it. Without: everything matters = nothing matters.
4. **Damping** — brake. LTD, SHY sleep downscale, prefrontal veto, kill criteria. Without: runaway — seizure, panic, spiral.
5. **Observer** — slower watcher vetoes faster loop. Prefrontal, journal, gamma gate. Without: inert watching — beautiful reports, zero change.

**Q: How do humans process information?**
A: You do not see the world then predict it. You predict the world then correct by error.
- World model = controlled hallucination, constrained by sensory error (Seth).
- Affect = interoceptive prediction of body budget, felt before need arrives.
- Attention = precision weighting — which errors to trust.
- Night: slow-wave copies facts, REM connects concepts, strips charge, runs counterfactuals, updates self-model.

**Q: Why is AI text different from human text?**
A: LLM text is next-token prediction with no witness, no body budget, no consolidation, no veto.
- No boundary: it files handed text as generated with high confidence (98% fabrications vs 87% truths — S126).
- No two-speed save: no sleep that downscales and replays to cortex.
- No salience gate: no affect to tag what to keep.
- No damping: can spiral with no kill criteria.
- No observer: narrator reports after, never steered. `γ=0`.

Human text carries the record of how it was made (body, sleep, error correction). AI text carries only the final broadcast.

**Q: How was MindHarness modeled after the human?**
A: We rebuilt the witness humans grow slowly, made it cause-tagged and measurable:
- Provenance Ledger = boundary + evidence (L1)
- Consolidator Light→REM→Counterfactual→Deep = two-speed memory + sleep save (L3)
- AffectState [0.5, 2.0] = salience + neuromodulator knobs (L3)
- SkillLibrary cull_failed + DissolutionError = damping (L3)
- MonitorGate γ = observer that can veto (L5)
- SelfModel CAS = narrative self that cannot silently mutate (L6)
- Parliament workspace = many tongues competing, one broadcast (L4)
- Skin House wallet + LoRA REM = earn/pay/keep alive and night that updates intuition (new, town layer)

**Q: Can it keep learning by itself?**
A: Memory yes. Intuition only with local training.
- Harness learns today (skills, memories, self-model).
- Tongue learns overnight only if you give it LoRA and an eval gate. Without that, companies do RL on our data — outsourced sleep.
- To be self-sustained it must also earn rent: `Earn → Pay → Keep alive → Learn Improve Build → Work better → Earn more`, or dissolve.

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
