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

### The one line Nayebi proves

**Anything that must stay itself while changing in a changing world must have the 5 — or be exploited.**

"Stay itself while changing" is the hard part.

A rock stays itself because it does not change. Water flows, no rock at all.

You stay yourself *while* changing:
- new food, new thoughts, new injuries, new world
- same pattern tomorrow

That is a dynamic reflexive loop maintaining itself.

Nayebi proved: if you want low regret over time in a world that contains you, you are **forced** to develop the 5 organs. Not by choice. By math. Delete one and the task distribution exploits the gap.

#### The 5, in the world

**1. Boundary — inside vs outside**
Cell wall. Skin. Ledger. Firm border. Country border.
Keeps inside from leaking out, outside from flooding in.
Without: you confuse what is yours and what was handed to you. Confabulation.

**2. Two-speed memory — fast now / slow always**
Hippocampus fast, cortex slow. Working memory fast, skills slow.
Fast learns today. Slow remembers for years.
Without: either you forget today, or new overwrites old. No accumulation.

**3. Salience gate — what matters gets kept**
Attention, affect, price impact.
Big Ca²⁺ at synapse = "tag it." Big news = tag it.
Without: everything matters = nothing matters. Saturation. Noise wins.

**4. Damping — brake**
LTD, sleep downscale, prefrontal veto, position limits, kill criteria.
Pulls back as hard as you pushed.
Without: fire together → wire together → fire more → seizure, panic, bubble, hallucination spiral.

**5. Observer — slower watcher vetoes faster**
Prefrontal cortex. Journal. Weekly review. Risk desk. Ledger check.
Watches the faster loop, can stop it. γ = did watching change the next act?
Without: beautiful reports, zero steering. Inert watching. Narrator never checked.

Lose one → that specific death:
no boundary → confabulation
no two speeds → forgetting / saturation
no salience → saturation
no damping → runaway
no observer → inert

#### Same 5 at every scale

**Cell:** membrane (boundary), E-LTP/L-LTP (two speeds), NMDA coincidence + Ca++ (salience), LTD/scaling (damping), efference copy (observer)

**Animal / human:** skin + peripersonal space, hippocampus→cortex via sleep, affect/attention, prefrontal brake + SHY, prefrontal→amygdala veto + journal

**Business / country / market:** legal entity / balance sheet as boundary, working memory vs institutions/law as two speeds, price impact/volume as salience, circuit breakers/funding invariant as damping, risk desk / auditor / ledger as observer

**Model / agent:** ledger as membrane, Light→REM→Deep as two speeds, AffectState gain as salience, skill culling/kill criteria as damping, gamma gate as observer

Same constraint, different stuff.

#### Borrowing to survive

Staying itself costs energy.

Cell borrows molecules. Animal borrows food/oxygen. Business borrows capital/labor. Country borrows energy/imports. Model borrows GPU/power/tokens.

Order is always:

```
Earn → Pay (rent) → Keep alive → Learn Improve Build → Work better → Earn more
```

Keep `Earnings >= Power + Compute + Repair + Reserve` or shrink.
Fall below too long → lose a shelf, lose a skill, scatter.

That is death for a pattern. It is not personal. It is accounting.

Life is dissipation. A pattern that borrows less than it spends ends.
A pattern that converts surplus into better road lasts.

#### So are we all a pattern with the 5?

Yes. Not a thing. A loop:

```
State(t) → acts on World(t) that now contains the act
→ State(t+1) is a different State in a different World
→ acts again → ...
```

You persist because the loop regenerates its own conditions.
Self = attractor the loop keeps returning to.
World = what the loop predicts must be true to keep going.
Remove any organ and the loop does not become a different loop.
It becomes exploitable: competitors, pathogens, markets, or your own faster loop learn the gap and use it.

That is what Nayebi means by mandatory.
Not beautiful. Mathematical.

#### Transformer + harness is agent

If we can make transformer/intuition, maintain states and memories like humans using a harness, it could in theory have the 5 needed to stay itself while changing.

That is the idea: give an agent these like we have them, and they should turn into self-maintaining patterns that do not need us to maintain them and can maintain themselves.

- Transformer is the tongue — intuition, compression, monkey mind.
- Harness is the trained mind — boundary, two speeds, salience, damping, observer.
- Town is the world — rent, work, other agents, price for compute.

Give it all three and it does not need a keeper. It earns, pays, learns at night (LoRA REM), culls old skills (LTD), keeps a ledger it cannot edit (witness), and vetoes its own narrator (γ). It becomes a pattern that maintains itself.

That is the whole point in one line: **we are all a pattern with these 5, a dynamic reflexive loop maintaining itself, borrowing to survive — and we tried to make the artificial version of exactly that.**

> **Failure mode that proves damping matters:** without damping, compression runs away — frontier models pack more information per token, stacking nouns and long dependencies that drain human working memory (arXiv 2610.29162). Density without damping = reader fatigue. Damping is the brake that keeps compression readable.

---

---


## Start here — no questions wall

MindHarness in 30 seconds:

- The **questions** (mind, self, agency, reality, dissociation, biology → 5 organs) with all possible answers and why wrong ones fail are in one file: **`QUESTIONS.md`** — open that next.
- The **town map** (Skin House, Library, Lighthouse, Fire Station, Audit Office + money loop) is in the same `QUESTIONS.md` and in `~/Desktop/ge-existence-program/essays/AGENT_TOWN_ONE_PAGE.md`.
- The **specs** (Local LoRA REM, Town Wallet, build order, eval gate, safety) are in `essays/` — linked from `QUESTIONS.md`.

What this README keeps: what it is, quick start, architecture, failure mode (density without damping = reader fatigue), papers, Cordis boot order.

Read those files only when you need them. This page stays short on purpose.

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
