# The Ledger Principle — V3 working folder

The full sequential draft is written: prologue, fifteen chapters, and future outlook. Editorial work has begun. This folder is the delivery copy; the canonical copy is `/Users/shehzad/Desktop/mindharness/bookv3/`.

## Read the book

- [MANUSCRIPT_V3.md](MANUSCRIPT_V3.md): the complete reading sequence, with sources gathered at the back.
- [CONTENTS_AND_STATUS.md](CONTENTS_AND_STATUS.md): chapter links, exact word counts, completed work, and the next pass.
- `chapters/`: the editable manuscript. The reading copy is rebuilt from these files; [MANUSCRIPT_BUILD.json](MANUSCRIPT_BUILD.json) records its inputs.

## Architecture and comparison

- [BOOK3_CANONICAL_SPINE.md](BOOK3_CANONICAL_SPINE.md): the controlling chapter order and each chapter’s contract.
- [PLAN.md](PLAN.md): thesis, rival explanations, translation method, and proof obligations.
- [EDITORIAL_AUDIT.md](EDITORIAL_AUDIT.md) and [CHAPTER_COMPARISON.md](CHAPTER_COMPARISON.md): V1/V2 comparison and what V3 repairs.
- [ESSAY_TO_BOOK3_CROSSWALK.md](ESSAY_TO_BOOK3_CROSSWALK.md): where the supplied synthesis enters the book.
- [TRANSLATION_MAP.md](TRANSLATION_MAP.md) and [ALLEGORY_ANCHOR_MAP.md](ALLEGORY_ANCHOR_MAP.md): reader anchors and their limits.
- [CONSCIOUSNESS_CHAPTER_DECISION.md](CONSCIOUSNESS_CHAPTER_DECISION.md) and [AGENCY_CHAPTER_DECISION.md](AGENCY_CHAPTER_DECISION.md): the consciousness hinge and personal coda.

## Editorial record

[EDITORIAL_PASS_01_HANDOFFS_2026-09-28.md](EDITORIAL_PASS_01_HANDOFFS_2026-09-28.md) documents the first pass. Earlier drafts are in `development/`; snapshots immediately before this edit are in `development/editorial_2026-09-28_handoffs/`. [EDITORIAL_HANDOFF_CHANGES_2026-09-28.json](EDITORIAL_HANDOFF_CHANGES_2026-09-28.json) records each changed chapter and its prior digest.

## Research and evidence

`evidence.sqlite` inventories source files, chapters, claims, observed quantities, primary web sources, and dated forecasts. The research archive is `/Users/shehzad/Desktop/mindharness/research/`.

- [RE_AUDIT_2026-09-25.md](RE_AUDIT_2026-09-25.md): source checks behind the restored maintenance, narration, speed, and dilution passages.
- [SOURCE_WALK_NAYEBI.md](SOURCE_WALK_NAYEBI.md): the worked primary-paper translation.
- [S126_WITNESS_SOURCE_CORRECTION_2026-09-26.md](S126_WITNESS_SOURCE_CORRECTION_2026-09-26.md): the wrong-ledger finding.
- `CH10_` through `CH16_` source-walk files: the dialect, collapse, consciousness, synthesis, agency, practice, and outlook checks.
- The research archive’s `ENTITY_BOUNDARY_SOURCE_CORRECTIONS_2026-09-26.md`, `CLAIMS_GATE_SOURCE_CORRECTIONS_2026-09-26.md`, `STORED_LOSS_SOURCE_CORRECTIONS_2026-09-26.md`, and `SOVEREIGN_BOUNDARY_SOURCE_CORRECTIONS_2026-09-26.md`: the financial correction trail.

Useful queries:

```sql
SELECT id, domain, grade, v3_decision FROM claims ORDER BY domain, id;
SELECT path, sha256 FROM sources WHERE kind = 'research_md' ORDER BY path;
SELECT c.id, w.title, w.url FROM claim_web_sources cw
JOIN claims c ON c.id = cw.claim_id JOIN web_sources w ON w.id = cw.web_source_id;
SELECT claim_id, horizon, observable_test, status FROM forecasts;
```

Next: edit the prologue and first two chapters together, then continue through the book’s interiors in sequence.
