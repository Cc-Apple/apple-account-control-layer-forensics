# DFIR Review Package Index

## Purpose

This repository is intended to support a paid preliminary DFIR / mobile forensic scoping review.

The current request is not for attribution.

The request is for an expert assessment of whether the preserved evidence is technically meaningful and whether it justifies a formal mobile forensic review or expert report.

## Current public package

The public repository contains only non-sensitive summary material.

It does not publish:

- raw iOS logs
- Manifest.db files
- iMazing backup folders
- Apple ID values
- email addresses
- phone numbers
- banking records
- BSSID values
- precise residence information
- friend device raw data
- private screenshots

## Proposed minimal package for review

### 1. Public overview

- README.md
- docs/non_attribution_statement.md
- docs/shadow_cloud_working_definition.md
- docs/2026-05-27_integrated_findings.md
- docs/2026-05_anchor_summary.md
- docs/ttp_alignment_observation.md

### 2. Methodology

- docs/reproducibility_and_scripts.md

### 3. Result summaries

- FINAL_TTP_REVIEW human summary
- final_daily_by_person.csv
- per_device_top10_days.csv
- TTP_2026_05_3DEV human summary
- 2026-05 15G anchor summary

### 4. Reproducibility scripts

- ttp_structured_once.py
- run_ttp_structured_once.bat
- finalize_ttp_results.py
- run_finalize_ttp_results.bat
- ttp_2026_05_3devices.py
- run_ttp_2026_05_3devices.bat

### 5. Evidence integrity

- SHA256 index of result ZIPs
- SHA256 index of scripts
- SHA256 index of selected raw logs if requested by the reviewer

## Review questions for a DFIR provider

1. Are the observed cross-artifact correlations technically meaningful?
2. Are the MDM_false + restriction_management patterns explainable by normal iOS behavior?
3. Are the account_cloud + telecom_proximity correlations explainable by normal usage?
4. Are the seam-failure patterns consistent with benign instability, or do they justify deeper review?
5. Is a formal mobile forensic review or expert report justified?
6. What minimal raw sample set is needed for verification?
7. What secure submission process should be used?
8. Should physical devices be examined after preliminary review?
9. What chain-of-custody procedure should be followed if physical devices are later provided?

## Physical-device handling position

At the preliminary stage, the preferred review method is based on preserved backup artifacts, iOS logs, structured summaries, and SHA256 indexes.

If a qualified forensic provider determines that physical-device examination is valuable after preliminary review, physical devices may be provided through a controlled chain-of-custody process.

The current position is to avoid casual shipping of evidence devices through uncertain routes.

## Boundary

This package is designed for technical triage.

It does not claim:

- APT attribution
- state attribution
- confirmed malware
- confirmed C2
- confirmed payload
- confirmed exploit chain
- confirmed criminal actor

The goal is to determine whether the evidence is technically meaningful and whether a formal forensic review is justified.
