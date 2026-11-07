#!/bin/bash
# Real finance pulls, no mocks. Re-run to refresh. Needs: curl, unzip.
# CourtListener (RECAP) needs COURTLISTENER_TOKEN env (free account); never commit the token.
set -e
UA="MindHarness contact@arcusquantfund.com"
curl -sL "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CORALACBS" -o fred_CORALACBS.csv
curl -sL "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL" -o fred_CPIAUCSL.csv
curl -sL "https://fred.stlouisfed.org/graph/fredgraph.csv?id=M2SL" -o fred_M2SL.csv
curl -sL "https://data.bis.org/static/bulk/WS_CREDIT_GAP_csv_flat.zip" -o bis_gap.zip && unzip -o -q bis_gap.zip -d . && rm bis_gap.zip
curl -sL "https://www.bu.edu/econ/files/2015/01/Moodys_Default_1920-2004.pdf" -o moodys_default_recovery_1920_2004.pdf
curl -sL -H "User-Agent: $UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK0000831001.json" -o edgar_Citi_facts.json; sleep 1
curl -sL -H "User-Agent: $UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json" -o edgar_JPM_companyfacts.json; sleep 1
curl -sL -H "User-Agent: $UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK0000070858.json" -o edgar_BofA_facts.json; sleep 1
curl -sL -H "User-Agent: $UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK0000072971.json" -o edgar_Wells_facts.json
for spec in "831001/000120677411000316/citigroup_10k.htm edgar_Citi_2010_10K.htm" "19617/000095012311019773/y86143e10vk.htm edgar_JPM_2010_10K.htm" "70858/000095012311018743/g25571e10vk.htm edgar_BofA_2010_10K.htm" "72971/000095012311018541/f56816e10vk.htm edgar_Wells_2010_10K.htm"; do
  set -- $spec
  curl -sL -H "User-Agent: $UA" -H "Host: www.sec.gov" "https://www.sec.gov/Archives/edgar/data/$1" -o "$2"
done
echo OK
# --- arXiv PDFs (open, no key) ---
curl -sL "https://arxiv.org/pdf/2603.21396" -o macar2026_introspection.pdf
curl -sL "https://arxiv.org/pdf/2605.14186" -o cao2026_harness.pdf
curl -sL "https://proceedings.neurips.cc/paper_files/paper/2024/file/7f1f0218e45f5414c79c0679633e47bc-Paper-Conference.pdf" -o panickssery2024_neurips.pdf
# --- EDGAR companyfacts (needs User-Agent header) ---
# UA="MindHarness contact@arcusquantfund.com"
# for cik in 0000831001 0000019617 0000070858 0000072971; do curl -sL -H "User-Agent: $UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK$cik.json" -o edgar_${cik}_facts.json; sleep 1; done
# --- FFIEC CDR bulk (needs python3.13 + ffiec-data-collector 2.0.0rc2) ---
# python3.13 -c "from ffiec_data_collector import FFIECDownloader; d=FFIECDownloader(); d.download_cdr_single_period('20091231'); d.download_cdr_single_period('20260630')"
# --- RECAP (needs COURTLISTENER_TOKEN env, V4 API; paginate with sleep, ltl_entries via docket-entries/?docket=67134504) ---
# --- BRD CSV: browser-only (lopucki terms click) - KEEP the csv, cannot script ---
# --- LoPucki: https://lopucki.law.ufl.edu/download_cases_table_terms.php -> download_cases_table.php ---
