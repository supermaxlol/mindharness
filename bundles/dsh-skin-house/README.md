# dsh-skin-house

Town wallet. Work → Earn → Pay rent → Keep alive or dissolve.

- Master key is never given to the agent. Agent holds session key only.
- Session key: daily limit, per-action limit, whitelisted to Town contract only.
- Every spend writes a provenance span.
- Balance < rent → Shrink signal (cull skill). Balance < floor for N turns → DissolutionError.
