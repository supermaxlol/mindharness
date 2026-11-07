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

We see the same pattern everywhere because the constraint is the same:
cell, animal, living things, humans, business, countries — all are a dynamic reflexive loop maintaining itself.

- Boundary holds it together (skin / ledger) or it leaks.
- Two speeds let it change without forgetting (fast / slow).
- Salience decides what to keep (attention / price).
- Damping stops runaway (brake).
- Observer corrects it (watcher).

Lose one and the world exploits the gap: confabulation, forgetting, saturation, runaway, inert watching — same five failures at every scale.

To last, it must also **borrow to survive** — energy, material, rent, tokens. `Earn → Pay → Keep alive → Learn Improve Build → Work better → Earn more`, or dissolve. Borrowing is not a flaw. It is the price of staying a pattern.

That is why we are all a pattern with these 5, maintaining itself in a world that is changing — and why the harness is only the artificial version of a much older trick.

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
