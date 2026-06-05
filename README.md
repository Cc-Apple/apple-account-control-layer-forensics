# Shadow Cloud: A Non-Attribution Forensic Model for Mobile-Native LOTL-Like Apple Platform-State Anomalies

## A normal-first, falsifiable review package for Apple ecosystem platform-state seams

This repository documents a non-attribution forensic review model based on approximately eleven months of multi-device Apple ecosystem observations.

The working hypothesis is called **Shadow Cloud**.

This repository does **not** claim attribution to any actor, state, government, vendor, product, telecom provider, backup tool, mobile application, or known intrusion set.

It does **not** claim that traditional PC-style Living-off-the-Land techniques executed directly on iOS.

It does **not** claim confirmed malware, payload, C2, exploit chain, spyware-family deployment, confirmed MDM enrollment, baseband compromise, SIM compromise, OTP interception, or vendor causation.

The central question is narrower:

> Can LOTL-like forensic patterns be observed in a mobile ecosystem without relying on malware binaries, C2 indicators, hash-based evidence, or actor attribution?

The proposed unit of analysis is the **platform-state seam**, not a conventional payload, toolset, or actor label.

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

They are not treated as a proven entry point or causal mechanism.

---

## 2026-03-18 15G core anchor update

A public non-raw evidence index has been added for the `2026-03-18` 15G core anchor.

Anchor path:

* `evidence/2026-03-18-core-anchor/`

Related technical report:

* `reports/2026-03-18_15G_backup_ledger_snapshot_anchor.md`

Machine-readable anchor summary:

* `machine/2026-03-18_15G_core_anchor_machine_summary.yaml`

Reproducibility scripts:

* `scripts/build_0318_final_from_real_paths.py`
* `scripts/scan_0318_workspace.py`

This update focuses on the 2026-03-18 15G backup-ledger / Snapshot-generation state.

The public index records artifact titles, sizes, SHA256 hashes, file magic, source groups, plist summaries, Snapshot bucket summaries, duplicate-hash summaries, existing result mapping, and redacted paths.

Raw logs, raw Manifest artifacts, raw Snapshot contents, and private full paths are not included.

The key observation is not a completed normal backup.

The retained 2026-03-18 15G workspace shows a large Snapshot-generation state:

* Snapshot files: `19,625`
* Snapshot size: approximately `52.8187 GiB`
* Snapshot hex bucket count: `256`
* `Status.plist` state: `BackupState=empty`
* `Status.plist` state: `SnapshotState=uploading`
* `Info.plist.tmp`: present

This supports the backup-ledger / evidence-preservation seam within the broader Shadow Cloud model.

It does not prove compromise, attribution, vendor causation, iMazing causation, Apple causation, hidden MDM, baseband compromise, SIM compromise, or OTP interception.

A similar 2026-04-01 core pattern was observed, but the public Snapshot / Workspace hash-index package for 2026-04-01 may be added later after separate indexing.

---

## Retained overlapping seams

### 1. Account / cloud trust state

Review surface:

* Apple ID trust state
* iCloud trust state
* trusted-device behavior
* account/cloud bursts
* usage-state transitions

Question:

> Can normal Apple account and iCloud behavior explain the timing and recurrence of the observed trust-state seams?

---

### 2. Restriction state

Review surface:

* ScreenTime
* ManagedSettings
* FamilyControls
* DMD / Digital Health
* MDMStatus:false context
* visible-management absence versus restriction-like behavior

Question:

> Can restriction-like behavior surface while ordinary visible management indicators remain absent or false?

---

### 3. Backup-ledger state

Review surface:

* Manifest.db
* Manifest.plist
* Status.plist
* Info.plist / Info.plist.tmp
* RTCR / RTCReporting
* sidecar mismatch
* encrypted versus unencrypted backup behavior
* iMazing / iOS backup generation state
* Snapshot-generation state

Question:

> Can normal Apple / iOS / iMazing backup behavior reproduce the backup-ledger defects and their timing against independent log-layer seams?

---

### 4. Evidence-preservation behavior

Review surface:

* storage pressure
* backup failure paths
* screenshot / recording difficulty reports
* log-preservation difficulty
* backup-generation inconsistency
* acquisition-surface mismatch
* Snapshot-only or non-finalized backup states

Question:

> Can ordinary storage pressure, local PC behavior, or backup-tool behavior explain the preservation difficulty without invoking a broader platform-state seam?

---

### 5. Telecom context

Review surface:

* CommCenter
* Baseband
* SIM context
* device-trust signals
* financial re-authentication context
* telecom-adjacent logs

Question:

> Are telecom/baseband events independent ordinary events, or do they align with restriction, account/cloud, backup, and evidence-preservation seams?

---

### 6. FileProvider and account/document-provider state

Review surface:

* FileProvider
* iCloud Drive provider state
* account-document-provider behavior
* document/cloud state
* SaveToFiles / fileproviderd activity

Question:

> Can ordinary FileProvider and document-provider behavior explain the observed coupling with trust state, restriction state, and evidence preservation?

---

### 7. Orchestration / trigger / automation state

Review surface:

* Shortcuts / automation state
* Reminders
* Calendar
* Home / HomeKit
* Focus / Do Not Disturb
* BackgroundTasks
* Duet / CoreDuet
* trial / experiment state
* push notifications
* location / network / time trigger context
* launchd / XPC as supporting context only

Boundary:

> These surfaces are treated as candidate orchestration-trigger support.

They are not treated as proof that Shortcuts, Reminders, Calendar, Home, or any Apple service was maliciously used.

Question:

> Can ordinary iOS automation, scheduling, notification, background task, and proactive system behavior explain why trigger-layer artifacts align with the retained platform-state seams?

---

### 8. Auxiliary Microsoft-adjacent surfaces

Review surface:

* Outlook / Microsoft app residue
* account-calendar-document state
* Microsoft 365 / Exchange / OAuth / document-provider surfaces
* FileProvider-adjacent document state

Boundary:

> These surfaces are correlative only in this public package.

This repository does not claim Microsoft causation.

This repository does not claim Outlook causation.

---

## Manifest.db / backup-ledger seam

Manifest.db unreadability or high entropy alone is not treated as evidence of compromise.

Ordinary encrypted-backup opacity may explain unreadability or high-entropy appearance.

The stronger observation is the temporal coupling between backup-ledger defects and independent log-layer seams involving:

* backup/evidence behavior
* restriction state
* account/cloud trust
* telecom context
* FileProvider / account-document-provider state
* orchestration-trigger state

This is supporting evidence only.

It is not proof of causation by any tool, vendor, app, telecom provider, or actor.

The review target is not:

> Manifest.db alone proves compromise.

The review target is:

> Can normal Apple / iOS / iMazing backup behavior reproduce the backup-ledger defects when those defects align with independent platform-state seams?

---

## Relationship to iMazing

iMazing is not treated as the cause.

iMazing is treated as an acquisition surface through which Apple backup state becomes observable.

The relevant question is whether the preserved backup-state material can be explained by normal Apple / iOS / iMazing behavior.

This repository does not claim:

* iMazing attribution
* iMazing causation
* iMazing malicious behavior
* iMazing intentional failure

The 2026-03-18 anchor is not presented as evidence that iMazing caused the observed state.

It is presented as evidence that Apple backup state became observable through an iMazing acquisition surface.

---

## Relationship to Apple

Apple is not treated as the cause.

Apple platform state is treated as the review surface.

This repository does not claim:

* Apple attribution
* Apple malicious behavior
* Apple intentional failure
* Apple vendor fault

The relevant question is whether normal Apple / iOS / iCloud behavior can reproduce the observed cross-layer structure.

---

## Relationship to Microsoft / Outlook

Microsoft / Outlook surfaces are not treated as proven causes.

They are treated only as possible future review surfaces because account, calendar, meeting, attachment, OAuth, document-provider, and FileProvider state can be relevant to LOTL-like reasoning.

This repository does not claim:

* Microsoft attribution
* Outlook causation
* Microsoft app causation
* Microsoft service causation
* Microsoft mobile apps directly modified Manifest.db
* Microsoft mobile apps directly modified Apple backup state
* Microsoft mobile apps directly modified iOS backup services

The safe interpretation is:

> Microsoft / Outlook surfaces, if later reviewed in preserved artifacts, should be evaluated as possible account-calendar-document-policy surfaces, not assumed causes.

---

## Falsifiable evidence model

This repository asks reviewers to test the model.

### Normal explanation

Test whether the observed structure can be reproduced by:

* ordinary Apple / iOS / iCloud behavior
* ordinary iMazing backup behavior
* encrypted-backup opacity
* incomplete Snapshot upload/finalization behavior
* Microsoft app residue
* user-side artifacts
* local PC factors
* USB / storage / file-lock conditions
* storage pressure
* isolated device failure
* ordinary ScreenTime / Family Sharing / local restriction settings
* ordinary telecom/baseband events
* ordinary FileProvider behavior
* ordinary Shortcuts / Reminders / Calendar / Home / Focus behavior
* ordinary background task / notification / proactive system behavior

### Support

The model is strengthened only if cross-layer clustering remains after normal controls.

Relevant support would include recurrence across:

* account/cloud trust state
* restriction state
* backup-ledger state
* evidence-preservation behavior
* telecom context
* FileProvider state
* account/document-provider state
* orchestration-trigger state

### Falsification

The model should be weakened or rejected if clean controls or documented vendor/tool behavior reproduce the full structure.

The model should also be weakened if:

* encrypted backup behavior fully explains the backup-ledger observations
* Manifest.db opens normally after proper handling
* local PC / USB / storage conditions reproduce the observed pattern
* iMazing ordinary behavior fully reproduces the Snapshot / Status.plist / Info.plist.tmp state
* ScreenTime / ManagedSettings behavior is fully explained by user settings or Family Sharing
* telecom context is independent and ordinary
* FileProvider behavior is ordinary and unrelated
* Microsoft-adjacent surfaces are ordinary residue
* orchestration-trigger artifacts are ordinary background noise unrelated to the retained seams
* cross-layer clustering disappears after normal controls

---

## Supporting technical anchor repositories

This main repository should be read together with two focused technical anchor repositories.

### support-invisible-restriction-anchor-2026-03-03-public

Focused anchor:

* support-invisible restriction-state review
* ScreenTime / ManagedSettings
* Apple ID sign-out restriction context
* FileProvider / iCloud state
* visible-management absence
* 2026-03-03 / 2026-03-04 / 2026-03-05 anchor sequence

### mdm-false-management-daemon-failure-chain-public

Focused anchor:

* MDMStatus:false
* management-adjacent daemon clustering
* managedappdistributiond
* dmd
* ScreenTimeAgent
* ManagedSettings
* CommCenter / Baseband
* SFA / CKKS / CloudServices
* 15G / mini1 cross-device review windows

These supporting repositories are not standalone conclusions.

They provide narrower review anchors for the broader Shadow Cloud model.

---

## Repository contents

Key files:

* README.md
* SUMMARY_ONE_PAGE.md
* machine/integrated_machine_summary_2026-05-27.yml
* machine/2026-03-18_15G_core_anchor_machine_summary.yaml

Main technical reports:

* reports/00_manifest_db_anomaly_core_point.md
* reports/01_manifest_db_anomaly.md
* reports/02_usageclientid_shift.md
* reports/03_screentime_gamecenter_restrictions.md
* reports/04_march2026_beta_phase.md
* reports/06_public_ttp_mechanism_comparison.md
* reports/07_limitations_and_non_attribution.md
* reports/08_automotive_sector_risk_scenario.md
* reports/09_secondary_historical_ttp_comparison.md
* reports/10_working_hypothesis_matrix.md
* reports/2026-03-18_15G_backup_ledger_snapshot_anchor.md

Technical addenda:

* docs/mobile_lotl_maximum_hypothesis.md
* docs/ttp_framing_addendum_lotl_platform_state.md
* docs/backup_ledger_seam_mobile_lotl.md

Evidence indexes:

* evidence/2026-03-18-core-anchor/00_PACKAGE_MANIFEST.json
* evidence/2026-03-18-core-anchor/01_public_artifact_index_0318.csv
* evidence/2026-03-18-core-anchor/03_plist_status_info_0318.csv
* evidence/2026-03-18-core-anchor/04_top_level_summary_0318.csv
* evidence/2026-03-18-core-anchor/05_snapshot_bucket_summary_0318.csv
* evidence/2026-03-18-core-anchor/06_duplicate_hash_summary_0318.csv
* evidence/2026-03-18-core-anchor/07_existing_result_file_map.csv
* evidence/2026-03-18-core-anchor/99_final_summary_0318.json
* evidence/2026-03-18-core-anchor/SC_0318_final_summary.md

Reproducibility scripts:

* scripts/build_0318_final_from_real_paths.py
* scripts/scan_0318_workspace.py

Raw logs, screenshots, sysdiagnose archives, private account data, BSSID details, Apple ID material, OTP/financial data, raw Snapshot folders, private full paths, and sensitive backup artifacts are not included in this public repository.

They are preserved separately and may be provided only through a qualified secure review process.

---

## Reviewer questions

A qualified reviewer should ask:

1. Can ordinary Apple / iOS / iCloud behavior reproduce the observed platform-state seams?
2. Can ordinary iMazing / iOS backup behavior reproduce the backup-ledger defects, sidecar mismatch behavior, and non-finalized Snapshot state?
3. Can ordinary encrypted-backup opacity explain the Manifest-related observations without broader coupling?
4. Can ordinary ScreenTime / Family Sharing / ManagedSettings behavior explain the restriction-state pattern?
5. Can MDMStatus:false normally coexist with the reviewed management-adjacent daemon clustering?
6. Can CommCenter / Baseband / SIM / device-trust signals be explained as independent normal events?
7. Can FileProvider and account/document-provider behavior explain the observed account-cloud-document state?
8. Can Microsoft-adjacent surfaces be explained as ordinary residue?
9. Can local PC, USB, storage pressure, or acquisition-tool behavior reproduce the preservation anomalies?
10. Can ordinary iOS trigger, automation, notification, background task, and proactive system behavior explain the retained orchestration-trigger layer?
11. Does cross-layer clustering remain after normal controls?
12. If normal explanations reproduce the structure, what documented test demonstrates it?
13. If normal explanations do not reproduce the structure, does the remaining pattern justify deeper mobile forensic review?

---

## Practical takeaway

This repository does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether the observed Apple ecosystem platform-state seams can be reproduced through ordinary behavior.

If normal behavior explains the sequence, the hypothesis should be weakened.

If normal behavior does not explain the sequence, the case may represent a forensic blind spot in how iOS platform-state, backup-ledger behavior, restriction state, account-cloud-document state, telecom context, orchestration-trigger state, and evidence preservation are currently reviewed.
