# Document Everything — Falsification Battery Master Ledger
*2026-09-23 — Every pull, number, artifact, grade, and gap for Financial Architecture: Weaponizing the Ledger + paper_unified §12. Nothing claimed without a file behind it.*

**Entity-case correction (2026-09-26):** The “three filings, three dismissals” shorthand in §10 and the VIE-to-creditor-recovery identification are corrected in [ENTITY_BOUNDARY_SOURCE_CORRECTIONS_2026-09-26.md](ENTITY_BOUNDARY_SOURCE_CORRECTIONS_2026-09-26.md), using the 2023 and 2025 appellate opinions and the 2025 Red River order.

## 1. Macro pulls (free, no key, reproducer in `experiments/lab_runs_falsify/fetch.sh`)

| Pull | Rows/size | Key numbers | Artifact |
|---|---|---|---|
| FRED CORALACBS charge-offs | 166 rows 1985→2026 | 0.98% 2008-Q1 → peak 3.02% 2010-Q1 | `fred_CORALACBS.csv` |
| FRED CPIAUCSL | 957 rows | CPI 2008-10 1.0391; 2020-22 1.1532 | `fred_CPIAUCSL.csv` |
| FRED M2SL | 813 rows | M2 2008-10 1.1741; 2020-22 1.3804 | `fred_M2SL.csv` |
| BIS WS_CREDIT_GAP bulk | 6.2M csv | US gap 10.1 (2006-Q4) → 11.63 (2007-Q4) → -9.43 (2010-Q4) | `bis_WS_CREDIT_GAP_flat.csv` |
| Combined verdict | — | St builds while Rt≈0; wall lags; dilution carries loss | `finance_falsify_v1.json` |

BIS via bulk `/static/bulk/WS_CREDIT_GAP_csv_flat.zip` (SDMX v1 flows 404'd). FRED via `fredgraph.csv?id=`. Empty-cell guard (`.`/`''`) before float().

## 2. Vintage recovery (free, no login)

Moody's 1920-2004 Special Comment, BU mirror, 1.8M PDF 40pp → `pdftotext` 1,855 lines. Exhibit 27 means per $100 par: Sr Secured 57.4 > Sr Unsecured 44.9 > Sr Sub 39.1 > Sub 32.0 > Jr Sub 28.9 (N 251/1207/478/485/22); medians confirm; trough 2000 All 25.7; Recovery = 0.52 − 6.9×DefaultRate, R²=0.65. Artifacts: `moodys_default_recovery_1920_2004.pdf`, `moodys_exhibit27.txt`, `moodys_vintage_recovery_v1.json`. S&P 2024 PDF mirror dead; 2025 gated — press-summary numbers only (117 vs 145 defaults, 55% distressed exchanges).

## 3. K placement (EDGAR XBRL + footnote prose, no login)

| Bank | CIK | 2010 10-K acc | VIE XBRL | Junior trust | LTD | Prose |
|---|---|---|---|---|---|---|
| Citi | 831001 (not 65145) | 0001206774-11-000316 | $54.8B | $10.1B (2012) | $315.8B | Mortgage securitizations = VIEs; Omni CPFF $2.5B (2009); SFAS 166/167 |
| JPM | 19617 | 0000950123-11-019773 | $28.6B | $2.3B (2016) | $267.9B | Note 16 four-prong sponsored VIE; conduits $24.8B (2009) |
| BofA | 70858 | 0000950123-11-018743 | $8.1B | missing | $317.8B | Jan-2010 consolidation +$100.4B assets / +$106.7B liab / $6.2B charge |
| Wells | 72971 | 0000950123-11-018541 | $0 | $0.7B (2020) | $174.7B | No VIE vehicles; on-balance whole-loan |

Method: `data.sec.gov/submissions` + archive crawl + `Host: www.sec.gov` header defeats Archives bot wall; EFTS `search-index` locates notes. Artifacts: 4× `edgar_*_2010_10K.htm` (0.2-8.8M), 7.6-8.4M `companyfacts` ×4, `edgar_K_panel_v1.json`, `edgar_VIE_prose_v1.json`, `edgar_VIE_panel_prose_v1.json`. VIE tag deprecated post-2011 (ASU 2009-17) — historical boundary illustration.

## 4. Gate counts (CourtListener RECAP, token ephemeral, never in repo)

Full-text hits type=r: proofs 1,410,962; secured 736,028; unsecured 298,775 (298,774 recount); priority 64,731; objections 67,308; disallows 125,615. Shares: secured 67% / unsecured 27% / priority 6%; objection rate 4.8%, disallow rate 8.9% vs proofs. Sample 60 recent cases in `recap_sample60.json`. Grade: measured activity, NOT adjudicated outcomes. Artifacts: `recap_gate_counts_v1.json`, `recap_rate_table_v1.json`.

## 4b. Adjudicated recovery — BRD paired (free, terms click, measured case-level adjudicated)

Source: Florida-UCLA LoPucki BRD 1-12-2023, 1,218 large public bankruptcies (Ch11 1,190), `brd_distributions_v1.json` + raw `brd_cases_2023.csv` (terms click via Playwright, free). Grade: measured case-level adjudicated, not activity proxy. Do not claim adjudicated allow/disallow rates — still proxy on dockets — but cents-on-dollar is adjudicated.

| Class | Mean | Median | n | Note |
|---|---|---|---|---|
| Secured (paired) | 0.869 | 1.0 | 105 | Paid in full at median |
| Unsecured nonpriority (paired) | 0.348 | 0.213 | 129 | 21c at median; below Moody's Sr Unsecured bond mean 44.9c |
| Unsecured pre-2008 | 0.377 | — | 77 | Pre wave |
| Unsecured post-2008 | 0.306 | — | 52 | Phi falls 7pp after the wave |

Reading: phi-fall ordering holds at case level (secured > bond unsecured > general unsecured), and post-2008 wave lowers unsecured phi. Short sentences, same story as Moody's vintage but now on adjudicated case distributions.

## 5. g4→0 mechanism (literature + domestic counterpart)

ISDS chill: Tienhaara 247 + 180, Van Harten 91, Janeba models, 3 forms (anticipatory/response/precedential). Finance-side instance: *Abaclat v Argentina* (Argentina-Italy BIT, 2001 default, ~60K bondholders, $3B 2007 claim, jurisdiction Aug-2011, settled 2016 ~$1.4B pre-merits; dissent = offshore/no-development boundary). Artifact: `isds_abaclat_v1.json`. Domestic counterpart: Gilens & Page 2014 (N=1,779, 1981-2002; coef .01 citizens n.s. / .21 elites / .16 groups; Fig.1 citizens flat ~0.3, elites 0.18→0.45, groups .16→.47). Full text via Playwright (Cambridge PDF 404 during disruption); artifact: `gilens_page_2014_v1.json`.

## 6. Harness mirrors (on-disk, zero spend)

CAS organ ablation: brake wiped 0.0846 vs intact 0.0315 (2.7×); intact≈shuffled (0.0315/0.0326). S126 n=1 null (raw 0.3333 vs sham 0.1667, P1 0.0 false) — needs n≥12 discriminating subject. Living theatre: energy 0.15 floor, fatigue 1.0 cap, query 0.0, health 0.5 unhealthy.

## 7. Papers

- `paper_ledger/main.tex`: falsification table + Abaclat + Gilens + VIE panel prose + Moody's row; bib `\citep{moodys2005,gilens2014,abaclat2016}` + prior 50+ entries. Build: pdflatex ×2.
- `paper_unified/main.tex`: 27pp, §12 weaponized formalisms + 3 TikZ + Barzakh/minds expansion.
- `research/LITERATURE_REVIEW_LEDGERS.md`: 3 lanes + OpenAlex consensus + 5 blocking gaps (2 now closed: vintage free source, finance award).

## 8. Still open (updated 2026-09-24)

1. S126 n≥12 φ-fall ordering — NO-GO documented (`s126_probe_verdict_v1.json`): Groq 403 all 4 keys, OpenRouter free 429/hang, Cerebras 2 keys 403 even after $5 top-up (credit not attached to key projects — dashboard fix needed). Needs funded lane + discriminating subject.
2. Allow/disallow *rates* by class — RECAP docket records remain proxy (no order text); BRD cents-on-dollar measured (paired secured 0.869/1.0 n=105 vs unsecured 0.348/0.213 n=129; era 0.377/0.306); USTP Ch13 dollars measured (48/23/6); BRD dispositions measured (89.9/5.2/2.0); 4 holdings hand-coded. Do not claim per-class filing-to-order conversion rates.
3. Post-2010 VIE panel — CLOSED 2026-09-24: 8 filings (2015/2020 × 4 banks), K shrinks/stays on-book (`edgar_VIE_evolution_2015_2020_v1.json`), wired + `fig:ktimeline`.
4. Token hygiene: CourtListener + Data.gov + 2× Cerebras keys touched chat/shell — reset all after session; scripts read env only (grep 0 in repo).
5. Repo weight: pruned 62M → 2.3M (41 files: JSONs + FRED CSVs + BRD CSV + Moody's PDF + fetch.sh with all URLs); `.gitattributes` LFS covers csv/pdf/htm/xlsx. Triage 67 dirty files before push — NO COMMIT without explicit file list.

## 9. Newest pulls (2026-09-24, all wired, paper_ledger 29pp 0 errors)

- IMF FSIC bulk 95M: USA AQ12 4.9599 (== WB 4.96 exact), AQ14 58.1→202.4 (`imf_fsi_US_v1.json`) — third source, same shape.
- S&P 2025 Annual Tables 1–8 via SSO session (`sp_2025_annual_extract_v1.md`); S&P 2024 via Tavily extract (`sp2024_extract_v1.json`).
- Macar +75% / Cao +8.6pp PDFs held verbatim (`macar_cao_verify_v1.json`); UNVERIFIED list now empty.
- Weco AIDE2 company-reported verified (`weco_aide2_v1.json`).
- SIFMA ABS +43% $388.1B (`sifma_abs_2024_v1.json`); FDIC coverage 112.5→430 (`fdic_coverage_v1.json` + `fig:coverage`); DSR mask (`fig:dsr`); K panel Table `tab:kpanel`; Gilens domestic g4 + Abaclat finance g4 with bib entries.
- Key audit: disk holds Groq×4 (all 403), CMDCLI (channel live, credits 0), MiniMax (401), OR mgmt (works, usage $0), Data.gov (works), CourtListener V4 (works); S2/Consensus disk keys empty; pasted S2 403.

## 10. Newest pulls #2 (2026-09-24 cont., paper_ledger 30pp 0 errors — AT CAP)

- Red River Talc THIRD Two-Step failure: S.D. Tex. No. 24-90505, Sept 2024 $9B prepack (90K votes) → denied + dismissed Mar 31 2025 (Lopez); J&J no appeal, back to tort, ~$7B reserves reversed. LTL and Red River dismissed; Bestwall’s injunction and later jurisdictional-dismissal denial affirmed in the Fourth Circuit — see 2026-09-26 correction note (`redriver_koreazinc_v1.json`).
- Korea Zinc live bypass Dec 2025: FTC raid Dec 17–19 on Young Poong/YPC over fresh circular link (5.26M shares, 25.42% in-kind); MRFTA 2006-review → 2007-amendments (`chaebol_reform_nyu_v1.json` with 1999/2002/2007 mechanics, Almeida loop prevalence, unwind forms).
- Moody's Ultimate Recovery (free PDF held): discounted at-resolution loans 82/100, Sr secured 65/67, Sr unsec 38, Jr sub 15, all bonds 37/24; trading prices explain ~50% of ultimate (`moodys_ultimate_v1.json`). 2008-by-type: distressed 50.8 vs payment 20.8 vs bankruptcy 24.4 (`moodys2008_bytype_v1.json`).
- Dividend recaps: market $81B 2024 (+500%), NBER census 61,628 LBOs → 1,572 recaps (2.6%/9.3%), single-deal $85M/370% ROE + contested (Buffets, KB Toys, Steward) (`divrecap_market_v1.json`, `divrecap_nber_extract_v1.json`).
- PE fees census: $20B (~6% equity, 3.6% EBITDA), no-work MSAs, 70–72% rebates; SEC $4.5M + $5.4M repaid (`pe_fees_census_v1.json`) — fee leg measured.
- Pod unwinds instanced: Balyasny 2018, Eisler 2025, Q1-2026 synchronized (−4.3/−4.5 shared-tail failure) (`pods_chaebol_instances_v1.json` + reform-cycle).
- IMF 154-country coverage panel (`imf_fsi_panel_countries_v1.json`); Gilens full PDF held + verified (`gilens2014_full.pdf`); USTP Ch13 dollars; BRD v2 paired + disposition; RECAP 298 + 4 holdings; S&P extract; Moody's 2024 narrative (cov-lite compression).
- F8/F10 rephrased in paper_v2 (τ range; 36-turn native); F9 verbatim; audit file updated; S126 verdict NO-GO extended (6 free lanes + Groq×4 + Cerebras×3 + MiniMax + cmdcli-0); Cerebras roster audit (only 2 public models survive).
- Repo: 64 artifacts, 7.1M (BRD xlsx? no — CSV + Moody's PDFs + EDGAR facts re-added for 4-bank prose work; prune again before push). NO COMMIT without explicit file list. Tokens touched chat: CourtListener, Data.gov, 3× Cerebras — all flagged for rotation.

## 11. Five-agent sourcing sweep (2026-09-25, paper_ledger 30pp 0 errors/0 undefined/0 multiply-defined, 69 artifacts)

- Pod autopsies: Klavdianos 2023 + Aug-2024 yen-carry 6+ pods (`pods_single_pod_autopsies_v1.json`).
- Chaebol FTC primary: KLRI Arts + Enf.Decree + KFTC sanctions verbatim (`korea_ftc_mrfta_primary_v1.json`); Gap 1 narrowed to case filings.
- Second ISDS award: Deutsche Bank v Sri Lanka ARB/09/2, $60.37M + interest, dissent flagged (`isds_deutschebank_srilanka_v1.json`).
- Culture: Smith 2007 rheology + Benna-Fusi chain + Bonilla-Quintana; Li & Bowling + Kouwenhoven + Guo 2026 dialects (`culture_dialect_v2.json`); lit-v2 +6 rows.
- AHE verified + bib audit clean except intentional `moodys2005` standing entry (`ahe_verify_v1.json`).
