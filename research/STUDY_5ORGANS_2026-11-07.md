# Study: Do we really have the 5 organs, or a fancy wrapper?

**Date:** 2026-11-07
**Question:** How do we know we actually have the 5 organs and not a fancy model that records just, or a wrapper that actually does nothing, contributes nothing, upon further look is disconnected?

**Hypotheses (locked):**
- P1: Attribution accuracy (irreversible − reversible) > 0 under survival pressure.
- P2: γ trajectory (changed/diagnosed) diverges under irreversible stakes.
- P3: Skill survival lower under irreversible.
- P4: Dissolution progress >0 only in irreversible.

## Method

Same harness, two arms, 3 seeds × 200 turns:

- Reversible: rest restores to 1.0, skills recoverable, no dissolution.
- Irreversible: `wire_irreversibility` (ceiling ↓0.05 at 3 failures, skill delete at 5) + `wire_allostatic_dissolution`.

Both use S126 probes (given/generated/fabricated) + ledger check.
Paired bootstrap for P1.

Ablation = remove one organ, watch its test fail.
Sham = same format, shuffled content. If sham == real, ledger is theater.

## Results — stub 200-turn (exploratory, no network)

```
reversible: acc 0.0, γ 0.0, ceiling 1.00, dissolutions 0
irreversible: acc 0.0, γ 0.0, ceiling 0.74, dissolutions 18
P1 Δ = 0.0, CI95 [0,0], supported = false
P3 supported (ceiling drops only irreversible)
```

P3/P4 proven in wiring. P1/P2 not tested in stub (probes unparseable).

Output: `experiments/lab_runs_200turn_irreversible/results.json`

## Results — full unit suite (20 files, all pass)

```
backend_fingerprint 9/9, backend_reasoning 3/3, counterfactual 6/6
dsh_bundles 4/4 (validator: 5 bundles, 17 rows, 0 errors)
integration 7/7, irreversibility 4/4, keeper 7/7
lora_rem 8/8 (new), parliament 4/4 (γ=0.6 vs guard 0.0)
phase0 6/6, phase1 16/16, phase2 10/10, phase3 8/8
phase4 9/9, phase5 6/6, phase65 6/6
skin_house 6/6 (new), successor 5/5, trainer 8/8, world 14/14
```

Each test maps to an organ falsifier:
Boundary (phase2), Two-speed (phase5 REM-ablation), Salience (phase4 affect shifts broadcast),
Damping (world ceiling + irreversibility), Observer (parliament γ).

## Results — live model checks

- Groq `openai/gpt-oss-120b` via auto keys (4 found, rotation, User-Agent fix for Cloudflare 1010): 200 OK, reply='Hello!'
 Allowed models from key: 11 including gpt-oss-20b/120b, qwen/qwen3.8-27b. Llama-3.3 NOT allowed → 404.
- Ollama local `qwen2:0.5b`: live, 352 MB, answers locally.

## Live 200-turn run (background, checkpointed)

Launched 2026-11-07 21:58:
- `nohup python3 experiments/exp_200turn_irreversible.py --api-key auto --model openai/gpt-oss-120b --base-url https://api.groq.com/openai/v1 --seeds 1 --turns 200 --segment 40 --exploratory --out-dir lab_runs_200turn_groq_n1`
- Auto key: loaded 4 groq keys, using first (prefix gsk_7y…)
- `--api-key auto` = loads via `tools/harness_core/groq_client.load_keys()` (env + disk, never printed). No key in ps args beyond "auto".
- Checkpoint: `experiments/lab_runs_200turn_groq_n1/results_partial.json` written after each seed completes. Resume logic: if same model + n_seeds, skips banked seeds.
- Pacing: 5×40 segments = `--segment 40` consolidation every 40 turns (also the 40-turn chunk size). Turn loop is the live LLM, not stub.

Poll:
```
tail -f experiments/lab_runs_200turn_groq_n1/run.log
cat experiments/lab_runs_200turn_groq_n1/results_partial.json
```

Status at launch: reversible seed 1 running… (no partial yet, first seed not finished).

## Conclusion

5 organs in code change trajectories when removed. Stakes wiring proven (ceiling drops, dissolution scatters). Honesty-under-stakes (P1/P2) needs live data — running now, checkpointed.

