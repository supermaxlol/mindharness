# S126 witness source correction — 2026-09-26

## The actual code path

In `experiments/exp_s126_v3.py`, the non-raw arms create `ledger = ProvenanceLedger()` and then create `harness = AgentHarness(...)`. `AgentHarness.__init__` creates its own `self.ledger`. The experiment binds given and generated statements to `harness.ledger` (lines 332–345), but the withcheck, sham, and gated branches call `ledger_check(ledger, ...)` on the separate local object (lines 391, 424, 441). Nothing binds emissions to that local object. The lookup therefore returns `found=False` for every statement in these branches. The “real” and “sham” records do not differ in retrievable content; neither can read the provenance that was recorded.

A zero-network local check with a dummy responder reproduced the distinction: after binding one sentence, `len(harness.ledger.all_emissions()) == 1` while `len(probe_ledger.all_emissions()) == 0`. The same `ledger_check` returned `found=False` against the local object and `found=True, origin=given` against `harness.ledger`.

## Results the book may report

The completed 12-seed paid Laguna run, `experiments/lab_runs_s126_laguna_n12_paid/results.json`, reports 12 probes per seed and four arms: raw **0.8889** (128/144), harnessed without forced check **0.8958** (129/144), withcheck **0.6667** (96/144), sham **0.6736** (97/144). The forced-check arm fell 0.2291 below the harnessed-no-check arm on this run. This establishes the observed performance of a **miswired, mandatory “no record found” message** under the tested protocol. It does not establish that a correctly wired veridical ledger worsens performance. It also cannot establish a content-sensitive sham separation, because the code never provided either arm with ledger content.

The earlier three-seed free Laguna run, `experiments/lab_runs_s126_laguna/results.json`, reported 0.8333 raw, 0.8333 harnessed-no-check, 0.7222 withcheck, and 0.6667 sham (36 probes per arm). Its apparent +0.0555 real-versus-sham gap is likewise not a content effect under this wiring. Earlier research notes that call it a directional ledger-content signal must be read with this correction.

The 12-probe battery has four generated items and eight non-generated items. An always-“no” policy scores 8/12 = 0.6667 without reading any item. The larger run's withcheck score sits exactly on that arithmetic floor. The stored results summarize accuracy, not every response, so the floor match alone is not proof that every answer was “no”; the earlier policy-diagnostic runs do document always-“no” behavior for screened models. The causal statement this code supports is narrower and sharper: an official-looking check was repeatedly invoked, could not access the record, and coincided with a collapse from strong unaided attribution to the constant-policy baseline.

## Related drift boundary

`experiments/lab_runs_persona/results.json` records a one-seed, ten-turn local pilot: raw consistency 0.8035 (drop 0.1965), harnessed consistency 0.7430 (drop 0.2570). Its predeclared raw >0.30 drop and harness <0.10 drop both failed. Choi et al. studied persona consistency over 36-turn conversations; the cited paper does not itself report “30% in 12 turns” as a general result. The V3 chapter may keep the striking local ten-turn result with its unit and must not convert the unconfirmed 30%-in-12 prediction into this run's observation.

## Editorial consequence

Chapter 9 uses the empty-record bug as the central failed walk. It distinguishes a stored record, a successful read, a trusted verdict, and a changed decision. Macar and Cao are genuine outside counterexamples to “machine self-inspection can never help.” A corrected, genuinely content-sensitive Laguna rerun remains open; no success is implied.
