# Claims-gate source corrections for Book V3 Chapter 5

**Date:** 2026-09-26. **Decision:** preserve the book's strong claim—that recognition, rank, and reachable assets determine who bears an unpaid obligation—using realised distributions and correctly paired comparisons. Replace older activity proxies where they were treated as claimant outcomes.

## A creditor's actual three columns

The [District of Connecticut Chapter 7 trustee's final account for Central CT Coop](https://www.ctb.uscourts.gov/sites/ctb/files/040015392773%20%281%29.pdf), case 16-21255, doc. 498, filed December 9, 2024, is the primary scene. Exhibit 7, p. 8, records Green Mountain Feeds claim 2: **$1,078.35 asserted, $1,078.35 allowed, $333.39 paid**. Exhibit 9, p. 125, independently records check 30009 on June 7, 2024 at a 30.92% dividend; unlike another check in the same register, it is not shown as voided or reissued. The trustee certified full administration of the estate. **$744.96** of the allowed claim was unpaid through this distribution. The debtor filed August 1, 2016; the report does **not** state when this creditor filed its own proof, so the case's eight-year duration is not a measured claim-specific wait.

In the same report, p. 2, secured claims show $1,051,802.81 allowed and paid; priority unsecured $59,780.44 allowed and paid; general unsecured $162,184.18 allowed and $50,142.69 paid; Chapter 7 administration $496,887.88 paid. These plus secured and priority payments reconcile to $1,658,613.82 of net receipts and disbursements. Secured payments can be tied to collateral; the class totals should not be pictured as one fungible jar. The gap between $1,490,398.95 asserted and $162,184.18 allowed general unsecured claims cannot be assigned to specific objection mechanisms from the summary totals alone; amended or duplicate claims may contribute. The source supports three distinct columns, not an inferred motive for each reduction.

The prior claim-level pilot is at `outputs/claim_level_realised_pilot.csv` in the September 25 Codex work folder; the full filed account is held in `work/claim_pilot/central_ct_coop_tdr.pdf`. The public court URL is controlling.

## LoPucki denominator correction

The [Florida–UCLA–LoPucki Bankruptcy Research Database](https://lopucki.law.ufl.edu/index.php) has 1,218 large public-company cases in the January 12, 2023 release. The reproducible calculation in `work/ledger_revision/code/a1_brd_paired.py` and `data/derived/brd_paired.json` reports:

| Comparison | Cases | Median secured | Median general unsecured | Direction |
|---|---:|---:|---:|---|
| Same cases with both class outcomes | 105 | 1.00 | **0.20** | Secured higher in 95/105 |
| All cases with unsecured outcome, regardless of secured data | 129 | — | **0.21278956** | Not a paired comparison |

V1/V2 and some research notes incorrectly say “paired cases secured median 1.0 versus unsecured 0.213.” The **0.213** belongs to the 129-case unsecured subset; the true matched comparison is **1.00 versus 0.20 across 105 cases**. The core ordering survives and is stronger when the same-case pair is stated correctly. This is descriptive incidence, not a causal estimate of the effect of acquiring collateral. Selection into secured status and collateral value both matter.

## Search activity is not passage or duration

The older RECAP numbers—1.41 million full-text hits for “proof of claim” and about 193,000 hits for “claim objection” plus “disallow claim”—are **overlapping search-query counts**. They do not link the same creditor's filing, objection, order, and payment. Therefore `193,000 / 1,410,000` is **not** a gate-conversion rate, and “priority has fewer hits” does not prove priority claimants have less voice or worse recovery. The counts can show corpus coverage, not the toll charged to an individual claim.

The 298-docket sample's 2,655–4,219 days are docket filing-to-termination spans in search-query-selected cases. They do **not** measure each creditor's claim-filing-to-payment delay. The Chapter 5 scene uses the court's filing and distribution dates as two known case events, while explicitly leaving the supplier's individual proof date unknown. Litigation delay remains an important mechanism, but this dataset cannot quantify it as “seven to twelve years per claim.”

## Moody's period and unit

Moody's [*Default and Recovery Rates of Corporate Bond Issuers, 1920–2004*](https://www.bu.edu/econ/files/2015/01/Moodys_Default_1920-2004.pdf), Exhibit 27, reports issuer-weighted **trading-price recoveries** by seniority for **1982–2004**, despite the report's broader historical title. Mean senior secured is 57.4 per $100 par; junior subordinated is 28.9. Those are prices around default, not ultimate distributions. Do not call Exhibit 27 a 1920–2004 recovery sample or mix its units with trustee cash. The hierarchy supports the chapter as an independent market observation, while the Connecticut report and LoPucki data supply realised distributions.

## Manuscript application

Book V3 Chapter 5, `05_the_tollbooths.md`, uses the Green Mountain payment as the scene and the matched LoPucki analysis as a second population. Four 70% gates yielding 24.01% appear only as an arithmetic illustration. The court's actual 30.92% distribution is not derived from that illustration. The chapter's governing line is: **asserted, allowed, and paid are different records, and the gap assigns the unpaid amount to someone.**
