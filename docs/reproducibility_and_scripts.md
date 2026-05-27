# Reproducibility and Scripts

## Purpose

The scripts used in this analysis were designed to support reproducible triage of Apple device log artifacts.

They were written to:

- read input folders only
- avoid modifying input evidence
- avoid deleting files
- avoid renaming files
- avoid moving files
- avoid overwriting source material
- write results to separate output folders

## Main script groups

### Wide organized-device run

Scripts:

- ttp_structured_once.py
- run_ttp_structured_once.bat

Purpose:

Run strict-plus TTP alignment and final shortlist extraction against organized device folders.

Input categories:

- My_Device
- Friend_Device

Output categories:

- file-level scores
- daily layer matrix
- final daily shortlist
- final file shortlist
- SiriSearchFeedback reference
- RTCReporting reference
- excluded files
- error log

### Existing result finalization

Scripts:

- finalize_ttp_results.py
- run_finalize_ttp_results.bat

Purpose:

Read existing result CSV files only.

This script does not reread raw logs.

It reaggregates Friend_Device by first path component and generates a final person / device-level review package.

Output categories:

- final_daily_by_person
- final_files_by_person
- per_device_top10_days
- all_daily_reaggregated
- human summary

### 2026-05 focused 3-device run

Scripts:

- ttp_2026_05_3devices.py
- run_ttp_2026_05_3devices.bat

Purpose:

Analyze 2026-05 logs for:

- 12G
- 15G
- iPhone11Pro

Output categories:

- file-level scores
- daily layer matrix
- final daily shortlist
- final file shortlist
- SiriSearchFeedback reference
- RTCReporting reference
- excluded files
- error log

## Python version

Python 3.14.5

## Key output files

- 00_human_summary.txt
- 03_final_daily_shortlist.csv
- 04_final_file_shortlist.csv
- 00_final_daily_by_person.csv
- 01_final_files_by_person.csv
- 02_per_device_top10_days.csv
- 06_all_daily_reaggregated.csv

## Source-type separation

The analysis separates source types into different roles:

- raw Apple logs: primary scoring source
- RTCReporting: strong reference source
- SiriSearchFeedback: separate reference source
- text export: non-primary or reference-only source
- derived summaries / OCR / notes: excluded from primary scoring

## Evidence handling

Published repository content should include:

- derived summaries
- machine-readable summaries
- SHA256 indexes
- methodology
- non-sensitive result tables
- reproducibility notes

Published repository content should not include:

- raw logs
- Manifest.db
- full iMazing backups
- Apple ID values
- email addresses
- phone numbers
- banking records
- BSSID values
- precise residence information
- friend identifiers
- private screenshots

## Reproducibility boundary

The scripts support repeatable triage and scoring.

They do not establish attribution, malware identity, C2 infrastructure, payload, or exploit chain.

The output is intended to help a qualified forensic reviewer identify which dates, devices, and artifacts should be examined first.
