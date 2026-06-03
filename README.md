# Shadow Cloud: A New-Era Spyware Model Hidden in Apple Account, iCloud, and Control-Layer Seams

## A forensic anomaly dataset for DFIR, mobile forensic, OS security, and cyber-espionage researchers

This repository documents a suspected **Apple account / iCloud / control-layer anomaly model** observed across approximately **11 months** and **9+ Apple devices**, including owner devices and comparison devices.

This is not a conventional malware report.

This is not a claim that a known spyware family was found.

This is not an attribution claim.

The core concern is deeper:

> What if the next generation of spyware does not appear as a visible payload, but as abnormal behavior across Apple ID, iCloud, trusted devices, backups, ScreenTime, Manifest.db, daemon activity, and telecom/proximity layers?

This working model is labeled:

## Shadow Cloud

The label **Shadow Cloud** is used as a working hypothesis for a possible new-era mobile/account/cloud-control spyware model.

It describes a pattern in which the attacker may not need to expose a classic malware implant. Instead, the observable traces appear at the seams between legitimate Apple services and abnormal control behavior.

The strongest traces are not expected to appear as a simple malware hash.

They appear as structural contradictions.

---

## Maximum working hypothesis: mobile-native LOTL-like Apple platform-state anomaly

The current strongest mechanism-level hypothesis is:

> Shadow Cloud may represent a mobile-native LOTL-like Apple platform-state anomaly.

This is not an attribution claim.

This is not a claim that a named actor, vendor, product, or service caused the observed behavior.

The model asks whether a PC / enterprise-style Living-off-the-Land concept may have a mobile-native equivalent, where legitimate mobile apps, accounts, cloud identity, calendar, document, policy, backup, telecom, and evidence-preservation states become the observable control surface.

The current hierarchy is:

```text
Shadow Cloud
= non-attribution working hypothesis

Mobile-native LOTL-like Apple platform-state anomaly
= maximum current mechanism-level hypothesis

Outlook / Microsoft account-cloud-calendar-document surface
= possible entry / state surface candidate

Manifest.db / backup-ledger seam
= byproduct / observable evidence-preservation seam

Account / cloud / mobile-surveillance comparison
= public comparison reference

Historical TTP comparison
= secondary operational-history comparison reference

Attribution
= not asserted
```

The key clarification is:

> Manifest.db is not treated as the root cause.
> Manifest.db / backup-ledger abnormality is treated as a possible byproduct or observable seam.

Similarly:

> Outlook / Microsoft mobile surfaces are not treated as proven causes.
> They are treated as possible account-cloud-calendar-document entry or state surfaces for future review.

See:

* `docs/mobile_lotl_maximum_hypothesis.md`

---

## Updated TTP framing: LOTL-like Apple platform-state anomaly

The current recommended framing is:

> Shadow Cloud is a non-attribution, LOTL-like Apple platform-state / trust-state anomaly hypothesis.

This means the strongest traces are not expected to appear primarily in malware payloads, C2 infrastructure, exploit chains, configuration profiles, or visible MDM enrollment.

Instead, the suspected anomaly surface is Apple platform state itself:

* Apple ID trust state
* iCloud trust state
* trusted-device behavior
* usageClientId / usage-state transitions
* ScreenTime / ManagedSettings
* backup-ledger behavior
* Manifest.db / Manifest.plist / Status.plist
* RTCR / RTCReporting
* CommCenter / Baseband / SIM / OTP context
* BSSID / RSSI proximity context
* evidence-preservation behavior

In short:

> Not living off tools.
> Living off Apple platform state.

For the backup layer:

> Living off Apple backup state.

Account / cloud / mobile-surveillance doctrine remains useful as a public comparison reference.

Historical long-term, low-noise, legitimate-service-oriented TTP reporting remains useful as secondary operational-history comparison.

Neither is used as attribution.

See:

* `docs/ttp_framing_addendum_lotl_platform_state.md`
* `docs/backup_ledger_seam_mobile_lotl.md`
* `docs/mobile_lotl_maximum_hypothesis.md`

---

## Core challenge

The central question is simple:

> Do these artifacts represent normal Apple/iOS behavior, iMazing backup behavior, user configuration, Microsoft app residue, ordinary account-calendar-document behavior, or device bugs?

Or:

> Do they justify deeper forensic triage as a possible Apple account / iCloud / backup / restriction-layer / telecom-control operation?

This repository exists to force that question into a form that can be reviewed, criticized, reproduced, and challenged.

If the observations are normal, the correct response is not dismissal.

The correct response is a reproducible explanation.

---

## What this repository is not

This repository does **not** assert:

* that any named threat group executed this activity
* that any specific government executed this activity
* that any specific company executed this activity
* that Apple executed this activity
* that iMazing caused this activity
* that Microsoft, Outlook, Office, Teams, OneDrive, Intune, or any Microsoft service caused this activity
* that a known spyware family was positively identified
* that a single malware payload explains the dataset

Named public threat reports, commercial spyware models, Microsoft app surfaces, and living-off-the-land tradecraft are referenced only as **public TTP comparison points or possible review surfaces**.

The purpose is not attribution.

The purpose is structural comparison.

### TTP-framing clarification

This repository should not be read as an actor-centered APT claim.

The preferred technical framing is now mechanism-centered:

* **Shadow Cloud** = working hypothesis name
* **Mobile-native LOTL-like Apple platform-state anomaly** = maximum current mechanism-level hypothesis
* **Backup-ledger seam in mobile LOTL-like platform-state anomaly** = focused backup-layer branch
* **Account / cloud / mobile-surveillance comparison** = public comparison reference
* **Historical TTP comparison** = secondary operational-history comparison
* **Attribution** = not asserted

This clarification reduces the risk that named public reporting is mistaken for attribution.

The central question is not which actor performed the activity.

The central question is whether normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior can explain a long-term, cross-device pattern in which trust state, restriction state, backup state, account-cloud-calendar-document state, telecom state, and evidence-preservation behavior appear to cluster at the same seams.

---

## Why this matters

A normal phishing case leaves URLs.

A normal malware case may leave samples, hashes, C2 domains, or known toolmarks.

This case does not look like that.

The observed pattern appears across:

* Apple account state
* iCloud / trusted-device behavior
* iMazing backup structures
* Manifest.db behavior
* ScreenTime / restriction-layer signals
* ManagedSettings / FamilyControls traces
* daemon-layer repetition
* usageClientId transitions
* CommCenter / Baseband / SIMTransfer signals
* BSSID / RSSI proximity anchors
* resource-pressure and evidence-preservation interference patterns
* possible account-cloud-calendar-document surfaces for future review

If this model is real, then the risk is larger than one infected phone.

It would mean that personal Apple devices, iCloud trust, backup ledgers, restriction layers, account-cloud-calendar-document surfaces, and telecom/proximity signals can become part of a hidden control surface.

That is why this dataset is public.

---

## Core observations

### 1. Manifest.db anomaly

Multiple backup generations showed `Manifest.db` behaving as:

* non-SQLite
* opaque
* high-entropy
* structurally abnormal
* inconsistent with ordinary readable Manifest.db expectations

The core issue is not merely encrypted backup handling.

The issue is repeated abnormal Manifest.db behavior at the backup path / backup service layer.

This matters because Manifest.db is a core backup ledger.

If the ledger itself becomes opaque, damaged, or structurally abnormal across generations, then standard backup trust assumptions become questionable.

This repository now also frames the Manifest.db issue as a possible **backup-ledger seam** within a mobile LOTL-like Apple platform-state anomaly.

This does not mean that iMazing is treated as the cause.

The safer interpretation is that iMazing may be the acquisition surface through which abnormal Apple backup state becomes observable.

See:

* `docs/backup_ledger_seam_mobile_lotl.md`

---

### 2. usageClientId transitions

Repeated `usageClientId` switching and discontinuity were observed across logs and devices.

This may indicate abnormal state transitions involving:

* app usage identity
* device/session state
* account-linked usage state
* possible continuity breaks between logical device identities

This is not treated as proof of compromise.

It is treated as a recurring structural signal requiring comparison against normal baselines.

---

### 3. Restriction-layer signals without visible MDM

ScreenTime / Game Center / Content & Privacy / ManagedSettings / FamilyControls signals were observed while visible MDM / supervised / userIsManaged indicators were not present.

The concern is the mismatch:

* restriction-layer behavior appears
* management-adjacent traces appear
* but ordinary visible device-management indicators are absent

If this is normal Apple behavior, it should be explainable.

If it is not normal, it may represent a control-layer anomaly.

---

### 4. March 2026 beta-phase candidate

Normalized analysis showed a density increase in several categories:

* restriction-layer signals
* ID / cloud signals
* resource-pressure signals
* operational-trace categories
* telecom / proximity-related signals

This period is treated as a possible phase shift or beta-phase candidate.

The claim is not that this proves an attacker.

The claim is that the density shift is worth forensic review.

---

### 5. March 12, 2026 mini1 core event

A mini1 Analytics log showed a strong proximity / communication pattern involving:

* SIMTransfer
* BluetoothDiscovery
* CommCenter
* BasebandPowerCycle
* PrivacyProxy
* RSSI
* Nearby
* resource reactions

This event is important because it connects telecom, proximity, privacy, and resource-pressure signals in a tight time window.

---

### 6. March 7, 2026 15G Wi-Fi / BSSID location anchor

WiFiConnectionQuality and sysdiagnose artifacts showed a physical Wi-Fi anchor involving:

* BSSID
* RSSI
* channel
* lastJoined timestamps
* location-specific wireless context

This is treated as a physical-world anchor for timeline correlation.

---

## The seam model

The central idea behind this repository is the **seam model**.

A sophisticated operation may not reveal itself through a single payload.

Instead, it may reveal itself where different systems must connect:

* Apple ID ↔ iCloud
* iCloud ↔ trusted devices
* trusted devices ↔ backup state
* backup state ↔ Manifest.db
* ScreenTime ↔ ManagedSettings
* restrictions ↔ visible MDM indicators
* daemon activity ↔ evidence preservation
* CommCenter ↔ Baseband
* BSSID/RSSI ↔ physical proximity
* resource pressure ↔ user attempt to preserve evidence
* account / calendar / document state ↔ backup and evidence-preservation state

The hypothesis is that Shadow Cloud-like activity would leave its clearest traces at these integration seams.

---

## Mobile-native LOTL maximum hypothesis

The strongest current hypothesis is not that one specific artifact explains the case.

The stronger hypothesis is that the observed artifacts may fit a mobile-native LOTL-like platform-state model.

In this model:

* Outlook / Microsoft mobile app surfaces are possible account-cloud-calendar-document state surfaces for future review.
* Manifest.db is not the root cause.
* Manifest.db / backup-ledger abnormality is a byproduct or observable evidence-preservation seam.
* iMazing is not treated as the cause.
* iMazing is treated as the acquisition surface.
* Apple backup state is treated as the review surface.
* The main question is whether normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior can reproduce the full cross-layer structure.

Current structural-fit estimates:

```text
Mobile-native LOTL-like Apple platform-state anomaly:
88 / 100

Existing seam observations with mobile LOTL-like model:
84-88 / 100

Outlook / Microsoft entry-surface hypothesis:
75 / 100

Manifest.db as byproduct / backup-ledger seam:
82 / 100
```

These are not attribution scores.

They are not attack-probability scores.

They are structural-fit scores used to guide review and falsification.

See:

* `docs/mobile_lotl_maximum_hypothesis.md`

---

## Backup-ledger seam addendum

The `docs/` directory includes a backup-layer addendum:

* `docs/backup_ledger_seam_mobile_lotl.md`
  Frames the Manifest.db / backup-ledger issue as a possible backup-ledger seam within a mobile LOTL-like Apple platform-state anomaly.

This addendum does not claim that iMazing caused the anomaly.

It treats iMazing as an acquisition surface through which abnormal Apple backup state may become observable.

The central review question is whether normal Apple / iOS / iMazing backup behavior can explain repeated Manifest.db / backup-ledger abnormality across preserved backup generations, especially when aligned with trust-state, restriction-state, daemon-layer, telecom, and evidence-preservation anomalies.

In short:

> Not living off tools.
> Living off Apple backup state.

This is a supporting technical interpretation.

It does not replace the broader Shadow Cloud model.

---

## Secondary historical TTP comparison

This repository includes a secondary historical TTP comparison report.

The comparison does not claim attribution.

It asks whether public reporting about long-term, low-noise, legitimate-service-oriented operations provides useful operational context for reviewing the observed seam structure.

The comparison is intentionally secondary.

The primary mechanism-level hypothesis remains:

> Mobile-native LOTL-like Apple platform-state anomaly.

See:

* `reports/09_secondary_historical_ttp_comparison.md`

---

## Supporting technical anchor repositories

This main repository should be read together with two supporting technical anchor packages.

These supporting repositories provide narrower, reviewable anchors for specific artifact structures.

* `support-invisible-restriction-anchor-2026-03-03-public`
  2026-03-03 support-invisible Apple ID sign-out restriction anchor involving ManagedSettings, MCState, Apple Support visibility, and MDMStatus:false context.

* `mdm-false-management-daemon-failure-chain-public`
  Cross-device MDMStatus:false and management-adjacent daemon failure chain across 15G and mini1.

Relationship:

* This repository provides the overall Shadow Cloud / Apple account-control-layer hypothesis.
* The two supporting repositories provide focused technical anchor packages.
* Raw logs and sensitive private evidence remain withheld unless provided later through a qualified secure review process.

---

## Reports

The `reports/` directory contains the structured analysis set:

* `00_manifest_db_anomaly_core_point.md`
  Core technical point explaining that the Manifest.db issue is not simple encrypted-backup unreadability, but repeated non-SQLite / opaque blob / high-entropy structural behavior across multiple backup generations.

* `01_manifest_db_anomaly.md`
  Manifest.db non-SQLite / opaque / high-entropy anomaly report.

* `02_usageclientid_shift.md`
  usageClientId transition and discontinuity report.

* `03_screentime_gamecenter_restrictions.md`
  ScreenTime / Game Center / Content & Privacy / ManagedSettings / FamilyControls restriction-layer report.

* `04_march2026_beta_phase.md`
  March 2026 density-shift and beta-phase candidate report.

* `05_bssid_proximity_anchor.md`
  BSSID / RSSI / Wi-Fi location-anchor report.

* `06_ttp_comparison_apt32_apt42_liminal.md`
  Public TTP comparison report. This file keeps named public reporting as comparison references only and places the primary mechanism-level framing on mobile-native LOTL-like platform-state behavior.

* `07_limitations_and_non_attribution.md`
  Limitations, non-attribution statement, and evidence-boundary clarification.

* `08_automotive_sector_risk_scenario.md`
  Automotive-sector risk scenario based on Apple account / iCloud / control-layer exposure.

* `09_secondary_historical_ttp_comparison.md`
  Secondary historical TTP comparison. This report keeps historical public TTP reporting as background comparison only, while the primary mechanism-level hypothesis remains mobile-native LOTL-like Apple platform-state anomaly.

* `10_working_hypothesis_matrix.md`
  Reviewer-facing hypothesis matrix including policy-as-persistence, backup-layer anti-forensics, backup-ledger seam, trust-graph poisoning, proximity-triggered state switch, deniability-first design, alpha/beta cohort testing, evidence-suppression objective, LOTL-like platform-state anomaly, and mobile-native LOTL-like Apple platform-state anomaly.

---

## Technical addenda

The `docs/` directory includes technical addenda:

* `docs/mobile_lotl_maximum_hypothesis.md`
  Defines the current maximum working hypothesis: mobile-native LOTL-like Apple platform-state anomaly. It treats Outlook / Microsoft surfaces as possible account-cloud-calendar-document entry or state surfaces, and Manifest.db / backup-ledger abnormality as a byproduct / observable evidence-preservation seam.

* `docs/ttp_framing_addendum_lotl_platform_state.md`
  Reframes Shadow Cloud as a non-attribution, LOTL-like Apple platform-state / trust-state anomaly hypothesis.

* `docs/backup_ledger_seam_mobile_lotl.md`
  Reviews the Manifest.db / backup-ledger issue as a possible evidence-preservation seam within a mobile LOTL-like Apple platform-state anomaly.

These addenda do not replace the existing comparison reports.

They clarify their role:

* Account / cloud / mobile-surveillance comparison remains a public comparison reference.
* Historical TTP comparison remains a secondary operational-history comparison.
* LOTL-like Apple platform-state anomaly is the preferred mechanism-level framing.
* Mobile-native LOTL-like Apple platform-state anomaly is the current maximum working hypothesis.
* No attribution is asserted.

---

## Evidence materials

The `evidence/` directory contains:

* `evidence_index.csv`
* `sha256_index.csv`

Raw private logs are not publicly uploaded.

Sensitive identifiers are redacted or represented by SHA256 hashes where possible.

The public repository is a minimal triage package, not the complete private evidence archive.

Representative original artifacts can be shared only under appropriate conditions, such as:

* NDA
* paid forensic scoping
* institutional review
* legal counsel involvement
* qualified DFIR / mobile forensic review

---

## References

The `references/` directory contains public TTP references used only for comparison.

These references do not prove attribution.

They provide context for comparing operational doctrine, not actor identity.

---

## Research question

The question for experts is not:

> Do you believe the hypothesis?

The question is:

> Can the observations be explained reproducibly as normal Apple/iOS behavior, iMazing backup behavior, user configuration, Microsoft app residue, ordinary account-calendar-document behavior, or ordinary device failure?

If yes, the normal explanation should be documented.

If no, the dataset may represent a serious mobile/account/cloud/platform-state risk model.

---

## Why public discussion is invited

This repository is intentionally public.

Criticism is welcome.

Disagreement is welcome.

Attempts to disprove the model are welcome.

The objective is not to protect a theory.

The objective is to force a technical question into public view:

> Can a modern spyware or control-layer operation hide inside normal Apple account, iCloud, backup, restriction, daemon, telecom, Microsoft app, and evidence-preservation behavior strongly enough that conventional malware-centric triage misses it?

If the answer is no, this repository should be easy to refute.

If the answer is yes, the implications are serious.

---

## Status

This repository is being prepared as a minimal reproducible evidence package.

Current status:

* public triage package prepared
* evidence index included
* SHA256 index included
* one-page summary included
* machine-readable summary included
* public TTP references included
* technical addenda included
* raw private logs withheld
* representative evidence available for qualified review

---

## Intended audience

This repository is intended for:

* DFIR professionals
* mobile forensic analysts
* iOS security researchers
* OS security researchers
* cloud-account security researchers
* cyber-espionage researchers
* incident response teams
* legal / technical reviewers
* research institutions
* automotive-sector security teams
* digital-rights and civil-society security teams

---

## Core position

This is not a claim of certainty.

This is a demand for serious technical review.

The dataset shows repeated structural anomalies across account, cloud, backup, restriction, daemon, telecom/proximity, account-calendar-document, and evidence-preservation layers.

If normal, explain it.

If abnormal, investigate it.

If this model is real, then the next generation of spyware may not look like spyware at all.

It may look like the cloud.

It may also look like normal mobile platform state.

---

## Latest integrated result: 2025-07 to 2026-05-26

As of 2026-05-27, an additional structured analysis was completed using already organized device-specific log folders.

The analysis covers:

* Owner Apple devices from 2025-07-01 to 2026-05-26
* Selected friend / comparison device logs
* A separate 2026-05 focused run for 12G, 15G, and iPhone11Pro
* Raw Apple log families, RTCReporting, SiriSearchFeedback, and text-derived artifacts separated by source type
* Derived summaries only; no raw logs or private identifiers are published here

This repository does not claim attribution to any named actor, state actor, Apple, iMazing, Microsoft, or any named organization.

The current observation is that the collected Apple device artifacts show a long-running account / cloud / telecom / restriction-layer / daemon-layer / backup-layer structure that appears more consistent with a mobile-native LOTL-like platform-state anomaly model than with isolated normal iOS behavior.

Working term used in this repository:

**Shadow Cloud**

This is a working label for the observed structure, not a malware name, not an actor name, and not an attribution claim.

---

## Working Hypothesis Matrix

This repository includes a reviewer-facing working hypothesis matrix for the Shadow Cloud model.

The matrix is not an attribution claim.

It is intended to help qualified DFIR, CTI, mobile forensic, platform-security, and OS-security reviewers test whether the observed artifacts are better explained as:

* normal Apple / iOS / iCloud behavior
* user-side backup artifacts
* tool-related artifacts
* Microsoft app residue or ordinary account-calendar-document behavior
* isolated device failures
* or a cross-layer account / cloud / policy / backup / telecom trust-state anomaly

The main validation hypotheses are:

1. **Policy-as-Persistence**
   Policy state, restriction state, ScreenTime state, ManagedSettings behavior, or Apple ID trust state may be acting as the persistence surface rather than a classic malware implant.

2. **Backup-layer Anti-Forensics**
   Manifest.db, Manifest.plist, RTCR, backup encryption state, or backup-generation behavior may be part of an evidence-preservation or reviewability problem.

3. **Backup-ledger Seam in Mobile LOTL-like Platform-State Anomaly**
   Manifest.db / backup-ledger abnormality may be a focused backup-layer seam where abnormal Apple backup state becomes observable through an acquisition workflow.

4. **Trust-Graph Poisoning**
   The anomaly may involve Apple ID lineage, trusted devices, backup lineage, SIM / OTP state, usageClientId continuity, and financial device trust rather than only one compromised device.

5. **Proximity-triggered State Switch**
   BSSID / RSSI / Wi-Fi / telecom / location signals may act as environmental or proximity-based state triggers.

6. **Deniability-first Design**
   Individually benign-looking symptoms such as iOS bugs, storage pressure, backup failure, iCloud sync delay, or user-error-like behavior may mask cross-layer correlation.

7. **Alpha / Beta Cohort Testing**
   The observed multi-device timeline may represent staged refinement or transition-phase behavior rather than a mature stable operation.

8. **Evidence-Suppression Objective**
   The objective may include suppression of the user’s ability to preserve, export, explain, or validate evidence.

9. **LOTL-like Platform-State Anomaly**
   The anomaly may not appear through a visible malicious tool, payload, C2, configuration profile, or confirmed MDM enrollment. Instead, normal-looking Apple platform states, including trust state, restriction state, backup state, telecom state, and evidence-preservation state, may become the anomaly surface.

10. **Mobile-native LOTL-like Apple Platform-State Anomaly**
    The current maximum hypothesis that PC / enterprise LOTL logic may have a mobile-native equivalent through legitimate mobile apps, account state, cloud identity, calendar / document state, policy state, backup state, telecom state, and evidence-preservation behavior.

These hypotheses are validation targets only.

They do not assert:

* malware attribution
* actor attribution
* state attribution
* Apple-side causation
* iMazing causation
* Microsoft causation
* classic MDM enrollment
* known spyware family deployment
* confirmed C2
* confirmed payload
* confirmed exploit chain
* Evil Twin / rogue AP use as a proven fact

See also:

* `SUMMARY_ONE_PAGE.md`
* `reports/10_working_hypothesis_matrix.md`
* `machine_summary.yaml`
* `docs/mobile_lotl_maximum_hypothesis.md`
* `docs/ttp_framing_addendum_lotl_platform_state.md`
* `docs/backup_ledger_seam_mobile_lotl.md`
