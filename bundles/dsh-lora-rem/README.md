# dsh-lora-rem

Night trainer. Updates intuition (transformer LoRA), not just memory.

- Triggered by Consolidator Deep phase.
- Builds chosen/rejected pairs from witnessed spans + counterfactual regret.
- Trains a small adapter. Runs eval gate (sham + attribution + utility). Fail = discard.
- Pass = promote, pin adapter id in SelfModel CAS, archive old.
- Cull if utility < 0 for N evals.

No gate = no promotion. Untagged adapter = BLOCKED.
