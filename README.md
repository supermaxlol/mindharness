# MindHarness — The Dynamic Reflexive Harness

> *LLM = tongue / intuition. Harness = mind. Tongue + mind = agent.*

A harness that makes any LLM honest about what it did — and improves its intuition overnight. Tongue + harness = agent. Unfrozen via adapters (local LoRA REM trained overnight with eval gate), witnessed ledger, `γ = changed/diagnosed`, counterfactual replay, Town wallet rent. 22 test files green, validator 0 errors.

**Companion:** [SpringFish / Spring-Loaded Door](~/Desktop/springfish) — crises, contracts, anchors. Same thesis: loops + witnesses.

---

## 30-second TL;DR

- **Question:** Can a language model know what it did, or does it just confabulate? Bare models do: 98% confident on fabrications vs 87% on truths.
- **Answer:** add the missing witness — ledger you cannot edit, self-model you cannot silently mutate, slower watcher that can veto, sleep that consolidates, brake that culls, rent you must pay or dissolve.
- **One line Nayebi proved:** anything that must stay itself while changing in a changing world must have the 5 — or be exploited. Cell, animal, human, business, country, model — same 5, different stuff.
- **What survives:** a pattern that maintains itself. Not a better narrator. A reliable witness.

**What it is:** harness (mind) + tongue (LLM) + town (world/rent) = agent that earns, pays, learns at night, or scatters.
**What it is not:** AGI finished, proof of consciousness, or a bigger model. Compression is intelligence, but density without damping = reader fatigue (arXiv 2610.29162).

---

## One picture

```
Environment (room, phone, people, town)
  ↕ modify / perceive
Self (minimal • narrative • social — re-injected or drifts)
  ↕ performs
Simulation (replay • counterfactual regret • plan)
  ↕ predicts
World Model (controlled hallucination, error-corrected)
  ↕ acts
Action Loop: Input → State → Prediction → Salience → Impulse → Agency (veto) → Action → Consequence → Evidence → Updated Self
```

5 organs hold the loop stable:
Boundary (inside/outside) • Two speeds (fast/slow) • Salience (what matters) • Damping (brake) • Observer (watcher vetoes)

Town underneath: `Earn → Pay (rent) → Keep alive → Learn Improve Build → Work better → Earn more` or dissolve.

---

## Start here

- **Questions (Ghazali → organs):** mind, agency, self, reality, dissociation, biology → 5 organs, with all possible answers and why wrong ones fail → **`QUESTIONS.md`**
- **Nayebi core + plant-not-copy + moldable layers + build order / eval gate / safety** → also in `QUESTIONS.md` (appended at the end)
- **One-pagers (printable):** `~/Desktop/ge-existence-program/essays/` → `HUMAN_MIND_ONE_PAGE.md`, `AGENT_TOWN_ONE_PAGE.md`, `WORLD_SELF_SIMULATION_ONE_PAGE.md`, `MOLDABLE_WITHIN_UNMOLDABLE_CLOSING.md`
- **Single thread essay (whirlpool → witness future):** `~/Desktop/ge-existence-program/essays/SINGLE_THREAD_WHIRLPOOL_2026-11-07.md` — full text is also at the bottom of `QUESTIONS.md`
- **Specs:** `essays/LOCAL_LORA_REM_AND_TOWN_WALLET_SPEC.md`, `essays/HERMES_DSH_5ORGANS_AUDIT.md`, `essays/MINDHARNESS_MISSING_2_PLUGINS_CHECKLIST.md`

Read those files only when you need them. This page stays short on purpose.

---

## Quick start

```bash
# Tests (no API keys needed)
for f in tests/test_*.py; do python3 "$f"; done  # 22 files green

# Living session (needs Groq or OpenRouter key)
python3 experiments/living_session.py --api-key $GROQ_KEY --model openai/gpt-oss-120b --base-url https://api.groq.com/openai/v1 --turns 40

# Attribution battery (S126)
python3 experiments/exp_s126_v3.py --api-key $KEY --model <model> --base-url <url> --seeds 3

# Papers
open paper_v2/main.pdf   # empirical (21pp)
open paper_v3/main.pdf   # program paper (29pp)
```

> Large files stay in `experiments/lab_runs_falsify/` as JSONs/CSVs (2.1M). Bulk raws re-pull via `bash experiments/lab_runs_falsify/fetch.sh`.

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
L0 LLM (unfrozen via LoRA)  Any OpenAI-compatible API; local base for night LoRA (qwen2:0.5b default, openai/gpt-oss-120b via Groq API)
```

Five invariants — boundary, two-speed memory, salience gate, damping, internal observer — appear at every scale (cell → mind → market → model) and are mandatory per selection theorems (Nayebi UAI 2026).

---

## Papers & research

- **v2** (`paper_v2/`, 23pp): *Witnessed Introspection* — S126, sham control, γ-gate, living sessions
- **v3** (`paper_v3/`, 36pp): program paper — unreliable narrator, reflexive dynamics, 5 invariants everywhere, Cordis, Research Mirror
- `research/PROGRAM_SYNTHESIS_DETAILED.md` (352 lines) · `research/DYNAMIC_REFLEXIVE_HARNESS.md` (249) · `research/RESEARCH_MIRROR.md` (273) · `research/AGENCY_AND_THE_CONSTRUCTED_SELF.md` (193)
- Study: `research/STUDY_5ORGANS_2026-11-07.md` — 200-turn stub: ceiling 1.0 vs 0.74, dissolutions 0 vs 18; live run in `experiments/lab_runs_200turn_groq_n1/` (checkpointed)

```yaml
bundles: [dsh-base, dsh-mindharness]  # + dsh-mindharness-parliament for many-model competition
```
`dsh --profile web --dump-config` shows 6 mindharness rows + parliament scaffold (9 inserts, 7 packages).

---

## Where agency lies

You don't choose the options. You don't fully choose the winner. You can veto the winner, keep a witness, and slowly change which options appear by what you rehearse. See `QUESTIONS.md`.

---

*Built by Shehzad Ahmed · 2026-09-06 · 22 test files green · Five NESS gates wired, sham sham-controlled, 200-turn irreversible live in background*
