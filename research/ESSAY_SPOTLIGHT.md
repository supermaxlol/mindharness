# Spotlight / Salience Gate: The Gain Knob That Decides What Matters Next

*Why scarce work must not be spent equally, and how a bounded multiplier decides the winner before content is read.*

---

Spotlight is not a ranking. It is a **gain knob** — one multiplier, **gain ∈ [0.5, 2.0]**, scaling every bid before content is read. 0.5× is half-volume, not silence. 2.0× is double-volume, not infinity. The 4× range (2.0/0.5) is enough to flip a winner without erasing the loser.

Every ~200 ms specialists — perception, memory, planner, habit, narrator — bid `salience × utility` for the single broadcast. Spotlight scales it:

```
effective_bid = raw_bid × gain
```

Skin decided what is inside. Spotlight decides what inside gets heard next. Without it the 0.85 saved from the gradient (1 photon at 5,800 K → ~20 at 255 K, entropy ×20, 0.15 you must dump to cycle) is spent equally — dissipated on noise. At the synapse the same knob is Ca²⁺ shape: big-brief spike → CaMKII → LTP; small trickle → calcineurin → LTD. At the market it is volume and IV. Same operation, different substrate.

### 1. Affect Is the Hand: Valence/Arousal, NE = Volume, DA = Stake

Affect is two EMAs, not an emotion word:

```
valence(t)=0.25·event+0.75·valence(t-1) arousal(t)=0.25·event+0.75·arousal(t-1)
```

Valence = good/bad. Arousal = calm/activated. Half-life ~2–3 turns; single shocks smooth, persistent signal moves the dial.

**NE = volume.** `gain_NE = 0.5 + 1.5·σ(arousal)`. High phasic NE → ~1.8×, every bid louder, thresholds lower. Tonic high → hypervigilant, nothing distinct. Low NE → ~0.6×, drowsy, content decides.

**DA = stake.** `effective_bid = salience × (utility^stake) × gain_NE`, stake ∈ [0.5,2.0]. High DA → utility dominates, quiet valuable bid wins. Low DA → salience dominates, loudest wins. NE says "how loud?" DA says "how much does winning matter?" Positive valence → exploit; negative → explore.

### 2. It Shifts Every Bid Before Content Arrives

```
World → Skin → Affect sets gain [0.5,2.0] → Specialists bid → gain×bid → Winner → Content read
```

One affect shift scales **all** bids. NE 1.0→1.6 raises every bid 60%. Habit 0.6×1.8=1.08 beats planner 0.9×1.0=0.9 though planner was stronger raw. Which memory is retrieved, which plan is simulated — all inherit the scaling before any sentence is scored.

Bounded means recoverable: 0.55×2.0=1.10 cannot beat 0.70×1.8=1.26 by infinite amplification; 1.0×0.5=0.50 stays competitive. No one is permanently crowned or silenced. Because the knob turns on arousal/valence, not truth, a loud false alarm at 2.0 beats a quiet true report at 0.6 — hypervigilance (everything at 2.0 → noise drowns signal) and fog (everything at 0.5 → nothing crosses) from one circuit.

### 3. Bounded Tuple Vision

Spotlight sees a **bounded tuple** `(salience [0,1], utility [0,1], gain [0.5,2.0])`. Each element capped, so product capped: best 1.0×1.0×2.0=2.0, not 200; whisper 0.3×0.3×0.5=0.045, not zero. Never infinity, never oblivion — only a small box. Gain amplifies differences that exist; it cannot invent utility.

### 4. Examples: IV Sharp vs Flow Whisper

**IV sharp: -0.034 vs +0.027.** Regressing allocation quality on IV change: sharp IV *rise* (+1 SD fear) → **-0.034**, gain ~2.0 on wrong signal, 3.4 points worse per SD. Sharp IV *fall* (-1 SD calm) → **+0.027**, gain ~0.8, winners win on utility. Same size move, opposite sign; spread 0.061 = ~6% swing from fear alone. Content unchanged, multiplier flipped.

**Flow whisper: +0.016.** Order-flow imbalance predicts **+0.016** per SD, small and stable. At gain 0.5 it is 0.008 and invisible; at 1.8 it is 0.029 and crosses threshold. Only helps when DA stake weights utility over salience. Turn NE volume up and the whisper drowns — why stress makes the loud useless bid beat the quiet useful one. A worry rehearsed at high gain myelinates ~100× faster over weeks: repetition × gain, not better content.

### 5. Failures: SKEW 0/16 and Saturation 79,993

**SKEW backwards 0/16 — Goodhart.** SKEW prices tail-risk salience. Tested as next-month direction predictor across 16 non-overlapping worlds: **0/16 hit, max |t|=1.79, ML p=0.675 once price added.** Not weak — backwards. 2.0× gain on salience with zero utility. When a salience measure becomes the target it ceases to measure value. Salience ≠ utility.

**Saturation 79,993 — knob stuck.** Build 11: **79,993 promotions** saturated the consolidation gate — tagged but never compressed because gain never differentiated (uniform ~1.0). Nightly SHY ×0.85 undone by daytime potentiation; mean weight → ~1.95× baseline. At ~2× everywhere, firing everywhere is firing nowhere. 79,993 is the counted cost of spending equally. Fix is restoring [0.5,2.0] spread so SHY can create room, not more potentiation.

Together: spend equally → no return.

### 6. How to Study It

**Sweep gain, hold content.** Fix bids, sweep 0.5→2.0 in 0.25 steps. At 0.5 high-utility quiet bid should win ~75%; at 2.0 high-salience loud bid ~75%. Plot P(win|gain) monotonic, slope ~0.4 per 0.5 gain. No flip = disconnected.

**Move affect, measure before content.** Induce arousal/valence shift (sleep loss, reward, threat). Correlate EMA with pre-content effective bids: expect r≈0.5–0.7 NE-volume, r≈0.4–0.6 DA-stake, content held constant.

**Price the dissociation.** Regress next return on `IV × flow`. Expect IV -0.034 to +0.027, flow +0.016, ΔR²≥0.02 for interaction after main effects. IV alone is 0/16 — cross-term is test.

**Count saturation.** Healthy: ~15–20% sequences replay, total weight → ~0.85× pre-sleep, saturation <1%. Failing: >30% saturated, mean weight >1.5×, 79,993-like counts in one build.

### 7. Connection to Gradient + 5

One photon in at 5,800 K → ~20 out at 255 K, entropy ×20. Keep ~0.85; 0.15 is dump to cycle again. Five organs answer five ways the gradient kills you:

| Demand | Organ | Solves | Without it |
|---|---|---|---|
| Whose loan? | **Skin** | Inside vs outside | Leakage |
| Spend now or keep? | **Two memories** | Fast labile vs slow stable; sleep saves | Drift 30%/12h or rigidity |
| **Spend on what?** | **Spotlight [0.5,2.0]** | **Allocates 0.85 to highest (salience, utility, gain) before content — NE volume, DA stake** | **Equal spend → -0.034/+0.027 flip, +0.016 lost, SKEW 0/16, 79,993 saturated** |
| When to stop? | **Brake** | Caps runaway (0.15 floor, SHY ×<1) | Seizure, spiral, crash |
| Did it earn? | **Watcher (γ)** | Did spend change next act? | Perfect ledger, zero steer |

Spotlight is allocation. Skin says what counts, two memories say when to keep it, spotlight says what deserves the scarce work *right now*, bounded so choice stays reversible — never 0.0, never infinite. Remove it and the other four still run but spend blindly: intact memories, correct ledger, brake at 0.15, every coin on noise.

```
World → Skin → Two memories → Spotlight [0.5,2.0] (what, before content) → Brake → Watcher → World
 SHY ×<1 NE vol / DA stake · tuple [0,1]×[0,1]×[0.5,2.0] · IV -0.034/+0.027 flow +0.016
```

---

*Affect does not tell you what is true. It tells you what to turn up before you check — half to double, never zero, never infinite — so the 0.85 saved from 1→20 is spent where it can earn the next 0.85.*


<!-- TRANSFER PACKET §53 — Is Experience What It Is Like... — Appended 2026-09-06 — See GRADIENT_FIVE_EXPANDED_ESSAY.md §14 for full 11-family table -->
# Is Experience What It Is Like to Be an Integrated Self-Monitoring Loop — Or Could the Loop Run Dark?
*Essay — One transfer packet for another LLM, researcher, or philosopher to continue without the original conversation. Built from consciousness_self_free_will_context.md §§1-145, consciousness_framework_synthesis_plain.md 54 §§, and LITERATURE_REVIEW.md 13 sections — re-derived, not remembered.*

We have functional model consciousness as integrated self-monitoring control process World→Perception→Model→Valuation→Attention→Thought→Self-model→Deliberation→Intention→Action→Outcome→Learning→Updated System; self as emergent model not permanent entity; free will as endorsed > impulse (parachute example, repeated choice trains automatic). Remaining: Is experience simply what it is like for such system to operate, or could system perform all functions without experiencing anything? Compare against GWT/HOT/RPT/Predictive/IIT/Beautiful Loop/Biological Computationalism/functionalism/illusionism/Buddhist no-self/Ghazali.

See GRADIENT_FIVE_EXPANDED_ESSAY.md §14 for full comparison table (11 families, 3 gates, 4 verdicts A-D) — this packet is now appended to every research/*.md so each file is self-contained transfer packet §53.


# Is Experience What It Is Like to Be an Integrated Self-Monitoring Loop — Or Could the Loop Run Dark?
*Essay — One transfer packet for another LLM, researcher, or philosopher to continue without the original conversation. Built from consciousness_self_free_will_context.md §§1-145, consciousness_framework_synthesis_plain.md 54 §§, and LITERATURE_REVIEW.md 13 sections — re-derived, not remembered.*

## 1. The Functional Model We Have Built
We propose a human as an embodied, continuously learning, predictive, self-monitoring system that must stay itself while changing while entropy rises: WORLD/ENV → PERCEPTION → INTERNAL MODEL (Memory + Prediction + Context) → VALUATION (reward/threat/goals) → ATTENTION → THOUGHT → SELF-MODEL → [Automatic → impulse] vs [Reflective → awareness of impulse] → DELIBERATION ("What do I endorse?") → INTENTION/CHOICE → ACTION → OUTCOME → LEARNING → Updated Memory/Habits/Values/Predictions/Self-model → LOOP

System is recursive: not merely models world, but models itself modeling world. Self = constructed control model integrating memories, bodily states, goals, relationships, predictions, future selves → narrative I am this kind of person. No-self ≠ nothing — processes exist, entity doesn't. Map still guides. Thoughts arise nonconsciously (NONCONSCIOUS → thought/urge → AWARENESS → feed/don't feed → elaboration or fade); impulse is event not instruction (I want to keep scrolling → I notice I want → Do I endorse? → No → act differently — basis of agency). Awareness makes information available; attention decides what receives processing; both distinct from consciousness and from memory.

Consciousness as control process: selected information becomes available for flexible control — attention, planning, comparison, future simulation, self-monitoring. Simple automatic stimulus → response vs flexible situation → represent alternatives → remember past → simulate future → compare → choose — huge advantage for novel situations.

Free will as compatibilist, functional: increasing ability to act according to endorsed values even when another system pulls elsewhere. Not escaping causality, but organism becoming cause: impulse → awareness → alternatives → values/consequences → deliberation → endorsed intention → action → feedback. Parachute example: automatic jumping = danger + conscious context parachute/training/controlled → different expected outcome → recontextualized prediction. Repeated choice → plasticity → stronger pattern → more automatic — conscious choice trains automatic system, second-order loop.

Remaining question H1: Is subjective experience simply what it is like for such integrated self-monitoring system to operate, or could system perform all functions — perceive, integrate, remember, plan, self-monitor, select, report, learn, modify — without experiencing anything (functional zombie)? User intuition: no; genuine awareness of own processing is experience; no inner observer required (homunculus rejected: no little observer, system models itself).

## 2. What "Subjective Experience" Means Before We Compare
Phenomenal vs access (Block): Phenomenal = what it is like (reddishness of red); Access = information available for reasoning/reporting/action.
Awareness vs attention vs metacognition vs self-consciousness: Awareness (information available), attention (what receives further processing), metacognition (representing own states with confidence), self-consciousness (I am experiencing this).
Self-model vs narrative identity vs organism: Organism (body+brain+environment), self-model (representation), narrative (story), self-consciousness (representation of experiencing), consciousness (something-it-is-like). Conflating them makes theories talk past each other. H1 targets phenomenal as integrated self-monitoring for flexible control — so access without phenomenal would be zombie.

## 3. Eleven Families — Agreements, Differences, Distinguishing Evidence
*See GRADIENT_FIVE_EXPANDED_ESSAY.md §14 for full table (GWT/HOT/RPT/Predictive/IIT/Beautiful Loop/Biological/Functionalism/Illusionism/Buddhist/Ghazali, 3 gates, 4 verdicts).*

GWT (Baars/Dehaene): broadcast itself suffices vs H1 requires L2+ minimal monitoring → Cogitate 2025 25/647 sustained, 0/645 double ignition → both challenged.
HOT (Rosenthal/Lau): thought about thought with aPFC locus — most aligned, but H1 requires control loop not just meta-representation → aPFC TMS dissociates meta-d′ vs d′.
RPT (Lamme): recurrence necessary but H1 says not sufficient — A1 no-input recurrence tests.
Predictive (Friston): prediction + self as model agrees, but PP can run feedforward without L4/L5 — needs ΔR² increment.
IIT (Tononi): Φ intrinsic vs H1 functional integration for control — Aaronson grid high Φ not conscious, PCI tracks L2+ not Φ.
Beautiful Loop (Laukkonen-Friston 2025): Closest ally/killer — denies self-model, B3 self-dissolution decisive collision, B2 depth-gradient.
Biological Computationalism (Milinkovic & Aru): Substrate matters — C4 metabolic-invariant FAIL (Ketamine ↑ vs Propofol ↓ both unconscious).
Functionalism (Putnam/Huh platonic + Jha vec2vec): M1=φ(M2) up to recoding — zombie §125 8-component test if passes all → H1 fails sufficiency.
Illusionism (Frankish/Dennett): Confabulation constitutes vs presupposes experience — same zombie + blindsight dissociations.
Buddhist no-self: No permanent self ≠ nothing, thick narrative N constrained toward fail, L2 survives — NDA.
Ghazali: muraqaba → meta-d′/d′ rises + DMN deactivation → L5 0.770→0.909.

## 4. What Evidence Would Actually Distinguish — Your §136 5-Variable Battery
Not p>0.05. 3 gates must pass before any rule fires: G1 Probe (live probe + positive control + equivalence TOST/BF₀₁>3 + replication ≥2×≥2) + G2 Construct (depth ≠ attention/WM) + G3 Theory.
Rules 1-4 (§136, pre-registered): A: experience at floor depth (L2 absent) → Loop necessity fails — only clean home = non-lucid vs lucid dreaming eye-signal; B: depth at floor experience (blindsight L4 without d′) → H1 sufficiency fails; C: experience tracks depth → Loop strengthened; D: depth no unique variance → cancel depth.
Master scoring sheet §137 + roadmap §138 conditional: A→A-series, B→B1 falsification machine, C→B1 justified + A5, D→cancel depth.

## 5. Bottom Line
Beautiful Loop is closest ally and closest killer — denies self-model you think is needed, but predicts same depth battery differently. B3 already constrained thick self; C4 already killed metabolic-invariant. Next filament to hold is not another LLM — it is B2/B4 Tier1 non-lucid vs lucid dreaming — the only place Loop necessity can be decisively tested with L5 eye signal where H1-minimal L≥2 vs Loop L3-5 vs HOT L3-4 make opposite predictions on same 7 measures.

*Appended as transfer packet §53 — read with main body as one loop.*
