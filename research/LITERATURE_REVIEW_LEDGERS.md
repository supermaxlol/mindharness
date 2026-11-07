# Literature Review — Ledgers: Financial, Cognitive, Machine
*2026-09-23 — Graded review for Financial Architecture: Weaponizing the Ledger + paper_ledger. Thesis: complex systems accumulate power/meaning/survival via externalized history-dependent ledgers.*

Evidence grades: **measured** (data/controls) / **theoretical** (proved/derived) / **convergent** (independent same structure) / **analogical** (same type, different substrate) / **open** (unresolved). No invented citations; program-internal sources flagged as such.

## Lane 1 — Financial engineering: whoever designs the ledger distributes wealth and risk

### Reflexivity + Goodhart (the loop that breaks measurement)
- **Soros, Alchemy of Finance (1987, book)** — cognitive + participatory functions operate simultaneously; predictions reshape outcomes. *Theoretical, founding.* Maps to belief→price→belief in paper_ledger §1.
- **Goodhart's law formalizations (measured/theoretical):** `arXiv:2410.09638` (tail-distribution proof of when proxy optimization backfires); `arXiv:2505.23445` (strong/weak/benign taxonomy, independence-free); `arXiv:1803.04585` (failure-mode variants); `arXiv:1803.00345` Proxyeconomics (proxy corruption in competitive systems); `PMID:37357710` (proxy failure as inherent risk); `PMID:29180439` (waiting-times target case). *Verdict: convergent — measurement corrupts once targeted. Direct warrant for ψ-gate analysis.*
- **Academic metric over-optimization:** `arXiv:1809.07841` / `PMC6541803` (120M papers, metrics become targets). *Measured — Goodhart outside finance, same mechanism.*

### Stored loss: par debt, evergreening, zombies
- **Zombie lending prevalence + spillovers:** `arXiv:2201.10524` (US listed firms; zombies narrow but spillovers hit healthy SMEs, productivity/capital/employment); `PMC7454878` (healthy-firm deterioration as zombie share rises); `PMID:38461638` (consistent losses, risky without external support). *Measured — warrants S_t evergreening + SME as first loss bearer.*
- **Policy as zombie factory:** `PMID:35725881` (green credit → 3 zombie types); `PMC12714253` (subsidies → TFP loss via zombies); `PMC7799295`, `PMC9985437`, `PMC8920973` (COVID guarantees saved jobs but decoupled credit from value). *Measured — warrants R_t=0 regime, credit decoupled from value.*
- **Zombie detection:** `arXiv:2306.08165` (304,906 Italian firms 2008-2017, disclosed accounts + missing values predict distress). *Measured — method precedent for S_t proxy.*
- **Production-network rigidity:** `arXiv:2604.23566` (informational rigidity breaks Modigliani-Miller, default in equilibrium). *Theoretical — warrants rigidity ⇒ leverage matters, feedback severance formalism.*
- *Gap: par-debt S_t law of motion itself is our formalism (analogical until sourced to accounting standards + call-report data). Next: map S_t to ASC 310 / IFRS 9 staging + FFIEC charge-off series.*

### Entity isolation: Chaebol pyramid + cross-shareholding networks
- **Chaebol investment/behavior:** `PMC8801770` (chaebol vs non-chaebol investment under COVID); `PMC10462866`, `PMID:36282376` (cross-shareholding game models); `PMC11283091` (Korean leverage); `PMC4588441`, `PMC8623544` (governance/R&D, carbon disclosure in chaebols). *Measured — warrants vertical-group behavior distinct from standalone firms.*
- **Chaebol bibliometrics:** `arXiv:2306.08743` (systematic review of business-group literature). *Convergent — entry point for post-1997 FTC reform sourcing (still needs primary FTC text).*
- **Ownership networks:** `arXiv:1107.5728` (bow-tie transnational control, core of financial institutions); `arXiv:1807.09346` (copula-entropy cross-shareholding concentration); `PMC13020756` (23-year Japanese cross-shareholding hierarchy stability). *Measured/theoretical — warrants zero-cross-shareholding invariant as contagion breaker; our invariant is design prescription (analogical).*
- *Gap: primary Fair Trade Commission post-1997 reform text (LG/SK) + Texas Business Organizations Code division statute still unsourced — flagged in paper_ledger.*

### Sovereign arbitrage: BIT/ISDS as standing gate
- **ISDS regulatory chill (measured, health-trade literature as mechanism precedent):** `PMC8611909` (ISDS chill on NCD prevention); `PMC5040601` (corporate veto on health policy); `PMC5417151` (ISDS no longer justified); `PMC8422681` (3 forms: anticipatory/response/precedential, South Africa); `PMID:32130317` (tobacco FCTC chill via arbitration); `PMC4121868` (treaty-drafting neutralizers); `PMID:23447902` (Philip Morris vs Australia plain packaging); `PMID:30136556` (NuCoal vs NSW mining/fracking). *Measured — warrants g4→0 mechanism: bypass local courts → supranational damages → chill. Finance-defendant cases still to source (mining/energy awards as closest analog).*
- *Gap: one finance-side treaty text + award pair for paper_ledger §7 upgrade from analogical to measured (case).*

## Lane 2 — Cognitive science: external memory ledger + culture as vectors

### Cumulative cultural evolution + external storage
- **CCE core:** `PMC8864182` (Henrich 2015 / Laland 2018 distinguishing role); `PMC2865079` (ratchet; human vs chimp mechanisms); `PMC8579038` (external cognitive representations as non-social dimension of CCE); `PMC8126465` (self-assembly: culture evolved culturally); `PMC3525879` (tipping points: storage outside brain, Upper Paleolithic); `PMC11370978` (group coordination catalyzes intelligence); `PMID:22555004` / Henrich 2004 Tasmania (demography → maladaptive loss); `PMID:24434740` (teaching/imitation as CCE prerequisites); `PMID:27040522` (explicit memory → cumulative modification); `PMC3385685` (cultural origins of cultural learning). *Convergent/measured — warrants human foundation §I: child inherits external OS; genius as navigation of precomputed trajectories.*
- **Program-internal anchors (flagged, not re-sourced here):** Tomasello / Henrich books, Clark Surfing Uncertainty (2016), Seth Being You (2021), Baars (1988), Dehaene GWT indicators, Kandel Principles (2000), Maturana-Varela Autopoiesis (1980). *Grade as in paper_unified; do not upgrade without re-fetch.*

### Sleep/homeostasis + plasticity (maintenance, not storage)
- **SHY core:** `PMID:14638388` (hypothesis: wake net-potentiation, sleep restores); `PMID:16376591` (slow-wave function review); `PMC6612535` (sleep as price for plasticity, down-selection); `PMC3921176` (price of plasticity → consolidation); `PMC5873548` (downscaling in vivo); `PMC5592216` (network activity → plasticity); `PMID:22998858` (upscale/downscale balance, REM mediation); `PMID:18624658` (sleep as weight normalization stabilizing Hebbian learning). *Measured/convergent — warrants SHY ×<1 + replay 10-20× + tagging without capture.*
- *Mapping to paper: viscoelasticity/hysteresis (memory kernels, path-dependence) is analogical extension of SHY + LTP/LTD — keep flagged until rheology-to-spine model sourced.*

### Manifest vs evoked, relational compression
- *Status: framework synthesis (analogical). Fable-as-compression (Kalila wa Dimna) + Kant-vs-Aesop phase-space steering lack primary cites in this pass. Next: Boyd/Gottschall narrative cognition + Sperber relevance + at least one fabulist transmission study.*

## Lane 3 — AI: autonomous machine ledgers + universal geometry

### Emergent dialects under efficiency pressure (governance paradox)
- **Efficiency vs interpretability trilemma:** `arXiv:2605.25421` HyLaT (hybrid latent-text; text interpretable-but-verbose vs latent efficient-but-opaque); `arXiv:2207.00088` VQ-VIB (utility/informativeness/complexity tradeoff shapes emergent codes); `PMC11984795` (complexity limit → human-language alignment). *Measured — warrants governance paradox: optimization strips redundancy oversight reads.*
- **Negative results that matter:** `arXiv:1706.08502` (agent-invented languages effective yet decidedly non-human-interpretable); `arXiv:2302.14276` (emergent messages often uncompressed/uninformative); `arXiv:2401.12624` (EC high train cost on multimodal vs LLM-LSC high inference cost). *Measured — warrants private-ledger opacity + forensic-guessing oversight.*
- **Grounding fixes:** `arXiv:2506.05236` (language-augmented MARL improves coordination); `arXiv:2102.12550` (discrete broadcast-and-listen improves interpretability); `arXiv:2603.22312` (Efficiency Attenuation: forcing human-comprehensible language degrades performance — LoT challenge). *Measured — warrants transaction-layer witness (receipts/hashes) over speak-English mandates.*
- **Cumulative machine evolution:** `arXiv:2302.14276` social learning via explicit communication (newcomer inherits pioneer shorthand). *Convergent — warrants pioneer/newcomer claim; needs longitudinal dialect-inheritance study for measured upgrade.*

### Collapse + universal geometry + witness (program bridge)
- **Model collapse (measured):** `arXiv:2404.05090` (statistical tails vanish under recursion); `arXiv:2505.08803` (multimodal VLMs/diffusion); `arXiv:2404.01413` (accumulate vs replace — accumulation mitigates); `arXiv:2509.16499` (generalization→memorization); `arXiv:2601.03385` SIGMA (spectral Gram-matrix onset metric); `arXiv:2509.08972` ForTIFAI (mitigations scarce); `arXiv:2605.14588` silent collapse (entropy/diversity contract while loss looks stable); `arXiv:2609.11149` (fragility spectrum 0.187-0.940 unique 4-grams across 13 checkpoints). *Measured — warrants loop-eating-itself without provenance witness; maps to paper_unified niche-construction vs autophagy.*
- **Program-internal (flagged):** Shumailov Nature 2024 (founding), Jha vec2vec `2505.12540` (M1=φ(M2) universal geometry), Panickssery r=0.94 evaluator corruption, Weco AIDE² 63%→34%, Dream-RSI 42% fewer calls. *Grades as in paper_unified; vec2vec already read in-session.*

## Cross-lane synthesis → paper_ledger mapping
| Engine layer | Finance warrant | Cognition warrant | AI warrant | Grade |
|---|---|---|---|---|
| Timeline (Day-1 ABS/recaps) | Zombie/COVID guarantee decoupling | Tag without capture (repetition without sleep) | Silent collapse (metrics stable while internals contract) | Convergent |
| Entity (OpCo/PropCo, zero cross-share) | Chaebol/network topology | Boundary fence (selective/costly/accountable) | HyLaT/VQ-VIB modularity | Analogical |
| Claims (ψ×K) | Goodhart/proxy corruption | Salience gate saturation (79,993) | EAP + uninterpretable codes | Convergent |
| Stored loss (S_t→ΔM→P1/P0) | Zombie spillovers + rigidity breaking MM | SHY debt + cortisol asymmetry | Collapse tails vanish | Convergent |
| Sovereign (A=0⇒K=0, g4→0) | ISDS chill (3 forms) | — (no analog claimed) | — (no analog claimed) | Analogical, finance-measured mechanism |

## OpenAlex + Scholar consensus (2026-09-23 fetch, cited-by as consensus proxy)

- **Multi-agent consensus:** Gronauer MADRL survey 934 cites (W3156295478); Wang LLM-agents survey 1622 cites (W4393065402); Zhu communication survey 147 cites; Guo LLM multi-agents 259 cites; Di Marzo self-organization 245 cites. *Consensus: efficiency-interpretability tradeoff + emergent opacity are field-central, not fringe.*
- **CCE consensus:** Muthukrishna Cultural Brain Hypothesis 170 cites (W2890095733, Henrich co-author); Kaaronen tipping points 113 cites; Richerson/Henrich tribal instincts 90 cites. *Consensus: culture-drives-brain + external storage as human distinction.*
- **ISDS chill consensus:** Tienhaara 2011 threat-of-arbitration view 247 cites (W1483847214); Tienhaara 2017 climate threat 180 cites (W2777227462); Van Harten Canada vetting 91 cites; Janeba formal chill models 23/17 cites. *Consensus: anticipatory/response/precedential chill measured across health, climate, mining — warrants g4→0 for finance by mechanism transfer (flagged analogical until finance award).*
- **Zombie/evergreening consensus:** Adler Gone with Headwinds 179 cites (W2607369674, IMF); White price-stability 155 cites; Molnar China corporate debt 35 cites; Steinkamp Euro-area evergreening 5 cites. *Consensus: forbearance + guarantees decouple credit from value; SME spillovers are the bearer.*

## What remains unsourced (blocking for journal)
1. FTC post-1997 reform primary text + LG/SK application; Texas division statute.
2. One finance-side BIT text + ISDS award pair (energy/mining closest).
3. ASC 310 / IFRS 9 staging + FFIEC charge-off mapping for S_t.
4. Fable-as-compression primary (narrative cognition) + viscoelasticity spine model.
5. Longitudinal dialect-inheritance study for cumulative machine evolution upgrade.
