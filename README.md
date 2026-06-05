# Shadow Cloud: A Non-Attribution Forensic Model for Mobile-Native LOTL-Like Apple Platform-State Anomalies

## A normal-first, falsifiable review package for Apple ecosystem platform-state seams

This repository documents a non-attribution forensic review model based on approximately eleven months of multi-device Apple ecosystem observations.

The working hypothesis is called **Shadow Cloud**.

This repository does **not** claim attribution to any actor, state, government, vendor, product, telecom provider, backup tool, mobile application, or known intrusion set.

It does **not** claim that traditional PC-style Living-off-the-Land techniques executed directly on iOS.

It does **not** claim confirmed malware, payload, C2, exploit chain, spyware-family deployment, confirmed MDM enrollment, baseband compromise, SIM compromise, OTP interception, or vendor causation.

The central question is narrower:

> Can LOTL-like forensic patterns be observed in a mobile ecosystem without relying on malware binaries, C2 indicators, IOC-based hashes, or actor attribution?

The proposed unit of analysis is the **platform-state seam**, not a conventional payload, toolset, or actor label.

Public SHA256 values in this repository are used for artifact integrity and reproducibility, not as malware-family indicators.

---

## Core review question

Can normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior explain a long-term structure in which trust state, restriction state, backup-ledger state, evidence-preservation behavior, telecom context, FileProvider state, account/document-provider state, and orchestration-trigger state appear to cluster at the same seams?

If yes, the normal explanation should be documented.

If no, the case may represent a forensic blind spot in how mobile platform state, backup-ledger behavior, restriction state, account-cloud-document state, telecom context, orchestration-trigger state, and evidence-preservation paths are currently reviewed.

---

## Mobile-native LOTL framing

Traditional Living-off-the-Land is historically centered on desktop or enterprise environments.

It usually means living off legitimate:

* tools
* accounts
* services
* administrative paths
* cloud identity
* document systems
* collaboration surfaces
* management surfaces
* scheduled tasks
* policy paths
* local automation paths

This repository asks whether a mobile equivalent can be modeled as:

> living off legitimate platform state.

Under the Shadow Cloud framing, the suspected review surface is not a conventional toolset.

The suspected review surface is Apple ecosystem state:

* Apple ID trust state
* iCloud trust state
* trusted-device behavior
* restriction policy state
* ScreenTime / ManagedSettings
* backup-ledger state
* Manifest-related artifacts
* RTCR / RTCReporting
* CommCenter / Baseband / SIM context
* FileProvider state
* account/document-provider state
* orchestration / trigger / automation state
* evidence-preservation behavior

In short:

Traditional LOTL:

> Living off tools.

Shadow Cloud:

> Living off Apple platform state.

Backup branch:

> Living off Apple backup state.

Trigger branch:

> Living off Apple orchestration / automation / trigger state.

---

## Scope and boundary

Dataset scope:

* approximately eleven months of multi-device Apple ecosystem observations
* six primary Apple devices
* comparison devices
* iOS diagnostic logs
* iMazing / iOS backup generations
* Manifest-related artifacts
* preserved backup-state material
* timeline and artifact summaries
* reproducibility scripts
* non-raw public artifact indexes

Review scope:

* forensic artifacts
* temporal consistency
* platform-state seams
* backup-ledger state
* orchestration-trigger state
* normal-explanation testing
* falsification

Not scope:

* attribution
* vendor blame
* spyware-family naming
* claims that PC-style LOTL executed directly on iOS
* claims that Microsoft / Outlook caused the anomaly
* claims that Manifest.db alone proves compromise
* claims that iMazing caused the anomaly
* claims that Apple caused the anomaly

---

## What this repository does not claim

This repository does **not** claim:

* actor attribution
* state attribution
* government attribution
* vendor attribution
* Apple attribution
* iMazing attribution
* Microsoft attribution
* Outlook causation
* telecom-provider attribution
* confirmed malware
* confirmed payload
* confirmed C2
* confirmed exploit chain
* confirmed spyware-family deployment
* confirmed MDM enrollment
* confirmed baseband compromise
* confirmed SIM compromise
* confirmed OTP interception
* attacker identity
* that subjective observations are standalone proof
* that Manifest.db alone proves the case
* that iMazing intentionally failed
* that Apple intentionally caused the observed behavior

Microsoft / Outlook / account-calendar-document surfaces, where mentioned, are treated only as possible future review surfaces or auxiliary correlative surfaces.

They are not asserted as causes.

---

## Normal-Hypothesis Reduction

To avoid overclaiming, ordinary explanations are treated first.

The following were treated as noise or normal-hypothesis candidates unless stronger cross-layer coupling remained:

* ordinary encrypted-backup opacity
* high-entropy artifacts alone
* broad keyword hits
* weak temporal joins
* non-core devices
* pre-March observations
* candidates without Manifest defects or backup/evidence overlap
* isolated device failures
* local PC / USB / storage explanations
* Microsoft app residue without cross-layer coupling
* ordinary account-calendar-document behavior
* ordinary Shortcuts / Reminders / Calendar / Home / Focus behavior
* ordinary background task behavior
* ordinary iMazing backup failure
* ordinary incomplete Snapshot upload/finalization state

The purpose is not to prove a malicious explanation.

The purpose is to test whether normal explanations can reproduce the full structure.

---

## Final retained core lines

After final filtering, two March-April 2026 core review lines remained.

These are review targets, not conclusions.

1. 2026-03-15 to 2026-03-21
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04
   Centered on 2026-03-31 to 2026-04-02

Both windows retained overlapping forensic artifacts across:

* account/cloud trust state
* restriction state
* backup-ledger state
* evidence-preservation behavior
* telecom context
* FileProvider state
* account/document-provider state
* orchestration-trigger state
* auxiliary Microsoft-adjacent surfaces

The Microsoft-adjacent surfaces are treated as correlative only.

---

## Public evidence packages

The repository contains public sanitized evidence packages.

These packages are intended to support reproducibility of the structure-level review without publishing raw logs, raw Manifest artifacts, raw Snapshot contents, private filesystem paths, device identifiers, device names, Apple ID material, BSSID/MAC values, OTP data, financial data, or other private source material.

### 2026-03-18 core anchor

Path:

* `evidence/2026-03-18-core-anchor/`

Purpose:

* public sanitized 2026-03-18 15G backup-ledger / Snapshot core anchor
* artifact index and backup-ledger summary
* Snapshot bucket summary
* plist status summary
* duplicate hash summary
* existing result-file map
* final public summary

Key files:

* `00_PACKAGE_MANIFEST.json`
* `01_public_artifact_index_0318.csv`
* `03_plist_status_info_0318.csv`
* `04_top_level_summary_0318.csv`
* `05_snapshot_bucket_summary_0318.csv`
* `06_duplicate_hash_summary_0318.csv`
* `07_existing_result_file_map.csv`
* `99_final_summary_0318.json`
* `SC_0318_final_summary.md`

Review relevance:

* This package documents the 2026-03-18 15G backup-ledger / Snapshot anchor.
* It is not treated as standalone proof of compromise.
* It is treated as a core backup-ledger / evidence-preservation seam for normal-explanation testing.

### 2026-04-01 core anchor

Path:

* `evidence/2026-04-01-core-anchor/`

Purpose:

* public sanitized 2026-04-01 15G two-generation Snapshot / backup-ledger core anchor
* generation summary
* plist status summary
* Snapshot bucket summary
* cross-generation summary
* top-level inventory
* bridge summary to the 2026-03-18 anchor
* machine-readable summary
* final public summary

Key files:

* `00_PACKAGE_MANIFEST_0401.json`
* `01_public_generation_summary_0401.csv`
* `02_public_plist_status_info_0401.csv`
* `03_public_snapshot_bucket_summary_0401.csv`
* `04_cross_generation_summary_0401.csv`
* `05_public_top_level_inventory_0401.csv`
* `06_0318_0401_bridge_summary.csv`
* `0401_machine_summary.json`
* `99_final_summary_0401.json`
* `SC_0401_final_summary.md`

Core observation:

* Two 2026-04-01 15G backup workspace generations reached large Snapshot-generation states.
* Both retained non-finalized backup-ledger indicators.
* The observed indicators include:

  * `BackupState=empty`
  * `SnapshotState=uploading`
  * `IsFullBackup=true`
  * `Info.plist.tmp` present
  * Snapshot hex bucket count `256`

Review relevance:

* The 2026-04-01 anchor is not a standalone claim of compromise.
* It is relevant because it repeats the same family of backup-ledger / Snapshot-generation structure already reviewed in the 2026-03-18 anchor.

### 2026-03-18 / 2026-04-01 cross anchor

Path:

* `evidence/2026-03-18-0401-cross-anchor/`

Purpose:

* public sanitized 2026-03-18 / 2026-04-01 15G log-manifest cross-anchor package
* source-existence summary
* Manifest core-state comparison
* layer-overlap matrix
* alignment score summary
* log-layer counts
* common log title summary
* compact manifest-log window hits
* Manifest top-level summary
* machine-readable cross summary
* final public summary

Key files:

* `00_PACKAGE_MANIFEST_cross.json`
* `00_source_existence_public.csv`
* `01_manifest_core_states_public.csv`
* `02_layer_overlap_matrix_public.csv`
* `03_alignment_score_public.csv`
* `04_log_layer_counts_by_day_public.csv`
* `05_common_log_titles_public.csv`
* `06_manifest_log_window_hits_compact_public.csv`
* `07_manifest_top_level_summary_public.csv`
* `98_public_package_summary.json`
* `99_cross_machine_summary.json`
* `SC_0318_0401_cross_public_summary.md`

Core observation:

* The 2026-03-18 core anchor and two 2026-04-01 generations show repeated non-finalized backup-ledger / Snapshot-generation states.
* The repeated pattern includes:

  * `BackupState=empty`
  * `SnapshotState=uploading`
  * `IsFullBackup=true`
  * `Info.plist.tmp` present
  * Snapshot hex bucket count `256`

Same-day layer overlap:

* account/cloud
* evidence backup/storage
* FileProvider
* orchestration/trigger
* restriction/management
* telecom
* usage state

Review relevance:

* This package strengthens the review because the 2026-03-18 anchor is not left as an isolated event.
* The 2026-04-01 evidence adds two additional generations showing the same backup-ledger / Snapshot-family structure.
* This still does not prove compromise, attribution, vendor causation, hidden MDM, baseband compromise, SIM compromise, OTP interception, or malware-family identity.

---

## Interpretation of the March-April 2026 anchors

The March-April anchor packages should be read together.

The 2026-03-18 package provides the initial core backup-ledger / Snapshot anchor.

The 2026-04-01 package provides a second date with two backup workspace generations showing the same family of non-finalized backup-ledger / Snapshot-generation behavior.

The 2026-03-18 / 2026-04-01 cross package connects those dates and tests same-day platform-state layer overlap.

The strongest structure-level statement supported by the public packages is:

> 2026-03-18 and 2026-04-01 show repeated non-finalized backup-ledger / Snapshot-generation states with same-day seven-layer platform-state overlap.

This is a review statement, not an attribution statement.

It does not establish:

* actor identity
* malicious intent
* vendor causation
* confirmed exploit chain
* confirmed malware
* confirmed C2
* confirmed hidden MDM
* confirmed baseband compromise
* confirmed SIM compromise
* confirmed OTP interception

It does support deeper review of whether ordinary iOS / iMazing / Windows / USB / storage behavior can reproduce the full structure.

---

## Machine-readable summaries

Machine-readable summaries are provided to support technical review and automated comparison.

Key machine-readable files include:

* `machine/machine_summary.yaml`
* `machine/integrated_machine_summary_2026-05-27.yml`
* `machine/2026-03-18_15G_core_anchor_machine_summary.yaml`
* `evidence/2026-04-01-core-anchor/0401_machine_summary.json`
* `evidence/2026-03-18-0401-cross-anchor/99_cross_machine_summary.json`

These files summarize the public review model, non-attribution boundary, retained core lines, backup-ledger anchors, cross-anchor relationship, and falsification-oriented review questions.

They are not raw evidence.

---

## Public evidence boundary

The public package intentionally excludes:

* raw iOS logs
* raw sysdiagnose archives
* raw Manifest artifacts
* raw Snapshot contents
* raw iMazing workspace contents
* private full paths
* Apple ID material
* device identifiers
* device names
* BSSID / MAC values
* telecom identifiers
* OTP data
* financial data
* personal messages
* screenshots containing private data
* videos containing private data

Public files are summaries, indexes, hashes, status tables, and machine-readable review material.

---

## How to review this package

A reviewer should not begin from the assumption that the Shadow Cloud hypothesis is correct.

The intended review method is normal-first:

1. Try to reproduce the 2026-03-18 and 2026-04-01 backup-ledger / Snapshot pattern through ordinary iOS backup behavior.
2. Try to reproduce the same pattern through ordinary iMazing behavior.
3. Try to reproduce it through Windows / USB / storage conditions.
4. Test whether incomplete Snapshot upload/finalization state explains the repeated structure.
5. Test whether the same-day seven-layer overlap can be reproduced through ordinary background activity.
6. If normal explanations reproduce the structure, the hypothesis should be weakened.
7. If normal explanations do not reproduce the structure, the case may represent a mobile forensic review blind spot.

---

## Falsification conditions

The Shadow Cloud framing should be weakened or rejected if reviewers can show that ordinary behavior reproduces the full structure.

Examples:

* documented iOS / iMazing behavior reproduces the same repeated non-finalized backup-ledger state
* ordinary incomplete Snapshot upload/finalization state explains the full pattern
* Windows / USB / storage conditions reproduce the same repeated pattern
* encrypted-backup behavior fully explains the Manifest-related observations
* same-day platform-state layer overlap is shown to be ordinary and unrelated
* clean controls reproduce the same backup-ledger / Snapshot state
* the apparent coupling disappears under better timestamp normalization
* the public summaries are shown to derive from artifact selection bias

---

## Practical takeaway

This repository does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether the observed Apple ecosystem platform-state seams can be reproduced through ordinary behavior.

If normal behavior explains the sequence, the hypothesis should be weakened.

If normal behavior does not explain the sequence, the case may represent a forensic blind spot in how iOS platform-state, backup-ledger behavior, restriction state, account-cloud-document state, telecom context, orchestration-trigger state, and evidence-preservation paths are currently reviewed.

---

## Current public position

This is a normal-first, non-attribution, falsifiable technical review package.

It is not an accusation package.

It is not an attribution report.

It is not a malware-family claim.

It is not a vendor-blame report.

It is a public structured review package for mobile-native LOTL-like Apple platform-state anomalies.
