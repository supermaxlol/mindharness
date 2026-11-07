# Chapter 9 — From noticing to correction

Checked September 30, 2026. Read the chapter, S126 correction record, and the archived Cao paper’s Table 2, methods, and ablation interpretation; reopened the primary paper live.

## Primary record

Qi Cao et al., *LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling*, https://arxiv.org/html/2605.14186v1, Table 2 and section 4. Held full text: `research/EDITORIAL_STORY_WITNESS_SOURCES_2026-09-29/cao_full.md`.

The main 1,859-problem evaluation reports 48.3% to 56.9%, average solver attempts one to 2.4. The new passage uses the separate 100-example ablation set. Its first-attempt baseline is 44%; full system 47% [37,57], average attempts 2.58; random retry 45.7% [43,48], average attempts 2.58. Last-answer selection is 40% [31,50], maximum self-rated confidence 44% [35,54], each using four attempts. Full previous reasoning context is 40% [31,50], average attempts 3.09. These are reported outcomes, not new runs or an independent replication.

## Alternative explanations and resolution

Extra compute is a material part of the main gain. The matched-budget comparison addresses whether directed allocation adds value, but its 1.3-point difference and overlapping intervals are not decisive alone. The passage gives that comparison its actual evidential weight. Selecting the latest answer, selecting the most confident answer, and passing full prior reasoning supply distinct tested shortcuts. Their outcomes motivate inspection of allocation, inherited context, and aggregation. Full-context underperformance is consistent with anchoring; the experiment does not directly establish its psychological cause.

The mechanic analogy carries selective inspection and retention. Model estimates are self-reports used by a calibrated controller, rather than independent observations of an engine. No new claim about repaired S126 performance is made. That run remains an invalid content-sensitive real/sham test because the probe read a different, empty ledger.

## Chapter argument

A useful witness requires a working route from relevant evidence to decisions about retry, inheritance, and answer selection. Having more attempts or more remembered reasoning does not guarantee improvement. The passage does not generalize the small ablation to all machine tasks.
