# March-April 2026 Core Review Lines: Normal-First Phase-Shift Boundary

## Purpose

This report summarizes the March-April 2026 review window within the Shadow Cloud public package.

The purpose is technical review, not attribution.

This report does not claim that a beta phase was proven.

This report does not claim confirmed malware, confirmed MDM enrollment, confirmed telecom compromise, confirmed baseband compromise, confirmed SIM compromise, or actor attribution.

The current position is narrower:

> After Normal-Hypothesis Reduction, two March-April 2026 core review lines remained.

These retained lines are review targets, not conclusions.

---

## Current Framing

The broader Shadow Cloud model is currently framed as:

> A non-attribution forensic model for mobile-native LOTL-like Apple platform-state anomalies.

The proposed unit of analysis is the platform-state seam, not a conventional payload, toolset, or actor label.

For this report, the review question is:

> Can normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior explain the March-April 2026 clustering of account/cloud trust state, restriction state, backup-ledger state, evidence-preservation behavior, telecom context, FileProvider state, and account/document-provider state?

If normal behavior explains the structure, the model should be weakened.

If normal behavior does not explain the structure, the retained lines may justify deeper mobile forensic review.

---

## Normal-Hypothesis Reduction

To avoid overclaiming, ordinary explanations were treated first.

The following were treated as noise or normal-hypothesis candidates unless stronger cross-layer coupling remained:

- ordinary encrypted-backup opacity
- high-entropy artifacts alone
- broad keyword hits
- weak temporal joins
- non-core devices
- pre-March observations
- candidates without Manifest defects or backup/evidence overlap
- isolated device failures
- local PC / USB / storage explanations
- Microsoft app residue without cross-layer coupling
- ordinary account-calendar-document behavior
- ordinary iOS crash clustering
- ordinary storage pressure
- ordinary telecom/baseband events
- ordinary FileProvider behavior
- ordinary ScreenTime / Family Sharing / local restriction settings

The goal is not to prove a malicious explanation.

The goal is to test whether normal explanations can reproduce the full cross-layer structure.

---

## Final Retained Core Lines

After final filtering limited to two primary devices, two March-April 2026 core review lines remained.

These are review targets, not conclusions.

1. 2026-03-15 to 2026-03-21  
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04  
   Centered on 2026-03-31 to 2026-04-02

The value of these lines is not any single artifact.

The value is the retained overlap across multiple platform-state seams after normal-hypothesis reduction.

---

## Why the Older Beta-Phase Language Was Narrowed

Earlier wording described a broad March 2026 beta-phase candidate.

That wording remains useful as historical analysis context.

However, for public review and DFRWS-aligned framing, the safer position is narrower.

The public review position is now:

> March-April 2026 contains two retained core review lines after Normal-Hypothesis Reduction.

This is more precise than claiming a confirmed beta phase.

The phrase "beta / transitional control-layer candidate" should be read only as a hypothesis label, not as a conclusion.

---

## Retained Overlapping Seams

Both retained lines preserved overlap across the following review surfaces.

### 1. Account / Cloud Trust State

Review surface:

- Apple ID trust state
- iCloud trust state
- trusted-device behavior
- account/cloud bursts
- usage-state transitions

Review question:

> Can normal Apple account and iCloud behavior explain the timing and recurrence of the observed trust-state seams?

---

### 2. Restriction State

Review surface:

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- MDMStatus:false context
- visible-management absence versus restriction-like behavior

Review question:

> Can restriction-like behavior surface while ordinary visible management indicators remain absent or false?

---

### 3. Backup-Ledger State

Review surface:

- Manifest.db
- Manifest.plist
- Status.plist
- RTCR / RTCReporting
- sidecar mismatch
- encrypted versus unencrypted backup behavior
- iMazing / iOS backup generation state

Review question:

> Can normal Apple / iOS / iMazing backup behavior reproduce the backup-ledger defects and their timing against independent log-layer seams?

---

### 4. Evidence-Preservation Behavior

Review surface:

- storage pressure
- backup failure paths
- screenshot / recording difficulty reports
- log-preservation difficulty
- backup-generation inconsistency
- acquisition-surface mismatch

Review question:

> Can ordinary storage pressure, local PC behavior, or backup-tool behavior explain the preservation difficulty without invoking a broader platform-state seam?

---

### 5. Telecom Context

Review surface:

- CommCenter
- Baseband
- SIM context
- device-trust signals
- financial re-authentication context
- telecom-adjacent logs

Review question:

> Are telecom/baseband events independent ordinary events, or do they align with restriction, account/cloud, backup, and evidence-preservation seams?

---

### 6. FileProvider and Account/Document-Provider State

Review surface:

- FileProvider
- iCloud Drive provider state
- account-document-provider behavior
- document/cloud state
- SaveToFiles / fileproviderd activity

Review question:

> Can ordinary FileProvider and document-provider behavior explain the observed coupling with trust state, restriction state, and evidence preservation?

---

### 7. Auxiliary Microsoft-Adjacent Surfaces

Review surface:

- Outlook / Microsoft app residue
- account-calendar-document state
- Microsoft 365 / Exchange / OAuth / document-provider surfaces
- FileProvider-adjacent document state

Boundary:

> These surfaces are correlative only in this public package.

This report does not claim Microsoft causation.

This report does not claim Outlook causation.

This report does not treat Microsoft-adjacent surfaces as a proven entry point.

---

## March 15-21 Core Review Line

Range:

- 2026-03-15 to 2026-03-21

Center:

- 2026-03-17 to 2026-03-19

Review value:

This line is treated as a retained March-April 2026 core review target because it preserved cross-layer overlap after normal-hypothesis reduction.

Relevant review surfaces include:

- account/cloud trust state
- restriction state
- backup/evidence behavior
- telecom context
- FileProvider / account-document-provider state
- auxiliary Microsoft-adjacent surfaces

This line does not prove:

- actor attribution
- malware
- C2
- exploit chain
- MDM enrollment
- telecom compromise
- baseband compromise
- SIM compromise
- OTP interception
- Microsoft causation
- Outlook causation
- vendor causation

The review question is:

> Can normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior reproduce this clustering?

---

## March 29-April 4 Core Review Line

Range:

- 2026-03-29 to 2026-04-04

Center:

- 2026-03-31 to 2026-04-02

Review value:

This line is treated as a retained March-April 2026 core review target because it preserved cross-layer overlap after normal-hypothesis reduction.

Relevant review surfaces include:

- account/cloud trust state
- restriction state
- backup-ledger state
- evidence-preservation behavior
- telecom context
- FileProvider / account-document-provider state
- auxiliary Microsoft-adjacent surfaces

This line does not prove:

- actor attribution
- malware
- C2
- exploit chain
- MDM enrollment
- telecom compromise
- baseband compromise
- SIM compromise
- OTP interception
- Microsoft causation
- Outlook causation
- vendor causation

The review question is:

> Can normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior reproduce this clustering?

---

## Relationship to Manifest.db / Backup-Ledger Observations

Manifest.db unreadability or high entropy alone is not treated as evidence of compromise.

Ordinary encrypted-backup opacity may explain unreadability or high-entropy appearance.

The stronger observation is temporal coupling between backup-ledger defects and independent log-layer seams involving:

- backup/evidence behavior
- restriction state
- account/cloud trust
- telecom context
- FileProvider / account-document-provider state

This report treats Manifest-related artifacts as supporting evidence only.

They are not proof of causation by Apple, iMazing, Microsoft, Outlook, a telecom provider, a backup tool, a mobile app, or any actor.

---

## Relationship to MDMStatus:false and Restriction-State Review

MDMStatus:false is not treated as proof of hidden management.

The review question is narrower:

> Can MDMStatus:false, visible-management absence, restriction-related services, and management-adjacent daemon clustering coexist normally under the reviewed conditions?

Relevant components may include:

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- managedappdistributiond
- ScreenTimeAgent
- restriction-related stores
- visible profile / supervision absence

This report does not claim confirmed MDM enrollment.

This report does not claim confirmed supervision.

This report does not claim a confirmed configuration profile proving management.

---

## Relationship to Telecom Context

CommCenter, Baseband, SIM, device-trust, and financial re-authentication context are treated only as review surfaces.

This report does not claim:

- confirmed telecom compromise
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- telecom-provider attribution

The review question is whether telecom/baseband events are independent ordinary events, or whether they align with account/cloud, restriction, backup, and evidence-preservation seams.

---

## Relationship to Microsoft / Outlook

Microsoft / Outlook surfaces are not treated as proven causes.

They are treated only as possible future review surfaces or auxiliary correlative surfaces.

This report does not claim:

- Microsoft attribution
- Outlook causation
- Microsoft app causation
- Microsoft service causation
- Microsoft mobile apps directly modified Manifest.db
- Microsoft mobile apps directly modified Apple backup state
- Microsoft mobile apps directly modified iOS backup services
- Microsoft surfaces caused the anomaly

The safe interpretation is:

> Microsoft / Outlook surfaces, if later reviewed in preserved artifacts, should be evaluated as possible account-calendar-document-policy surfaces, not assumed causes.

---

## Strengthening Conditions

The March-April core-line interpretation is strengthened if qualified review shows that:

- the retained lines survive normal-hypothesis reduction
- clean controls do not reproduce the same cross-layer structure
- ordinary encrypted-backup opacity does not explain the backup-ledger observations
- broad keyword hits do not explain the retained clustering
- weak temporal joins were correctly removed
- non-core devices were correctly removed from final scoring
- backup-ledger defects align with independent log-layer seams
- restriction-state seams align with backup/evidence seams
- account/cloud trust-state seams align with restriction or backup/evidence seams
- telecom context aligns with backup/evidence or restriction seams
- FileProvider / account-document-provider seams align with the same windows
- Microsoft-adjacent surfaces, if present, are not sufficient as ordinary residue
- the two retained windows remain meaningful after normal controls

---

## Weakening or Falsification Conditions

The March-April core-line interpretation is weakened if qualified review shows that:

- documented Apple / iOS behavior reproduces the full structure
- documented iMazing behavior reproduces the full structure
- clean control devices reproduce the same cross-layer clustering
- encrypted backup behavior fully explains backup-ledger observations
- Manifest.db opens normally after proper handling
- local PC / USB / storage conditions reproduce the observed pattern
- ScreenTime / ManagedSettings behavior is fully explained by user settings or Family Sharing
- MDMStatus:false plus daemon clustering is ordinary and documented
- telecom context is independent and ordinary
- FileProvider behavior is ordinary and unrelated
- Microsoft-adjacent surfaces are ordinary residue
- cross-layer clustering disappears after normal controls
- the retained windows are explained by collection bias, observer-side changes, or artifact-processing error

If these conditions are met, the hypothesis should be weakened or rejected.

---

## Reviewer Questions

A qualified reviewer should ask:

1. Were ordinary explanations removed before retaining the March-April lines?
2. Were broad keyword hits and weak temporal joins sufficiently filtered?
3. Were non-core devices correctly excluded from final retained scoring?
4. Can ordinary Apple / iOS / iCloud behavior reproduce the retained cross-layer structure?
5. Can ordinary iMazing / iOS backup behavior reproduce the backup-ledger defects and sidecar mismatch behavior?
6. Can ordinary encrypted-backup opacity explain the Manifest-related observations without broader coupling?
7. Can ordinary ScreenTime / Family Sharing / ManagedSettings behavior explain the restriction-state pattern?
8. Can MDMStatus:false normally coexist with the reviewed management-adjacent daemon clustering?
9. Can CommCenter / Baseband / SIM / device-trust signals be explained as independent normal events?
10. Can FileProvider and account/document-provider behavior explain the observed account-cloud-document state?
11. Can Microsoft-adjacent surfaces be explained as ordinary residue?
12. Can local PC, USB, storage pressure, or acquisition-tool behavior reproduce the preservation anomalies?
13. Does cross-layer clustering remain after normal controls?
14. If normal explanations reproduce the structure, what documented test demonstrates it?
15. If normal explanations do not reproduce the structure, does the remaining pattern justify deeper mobile forensic review?

---

## Final Review Position

This report does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether the March-April 2026 retained core lines can be reproduced through ordinary behavior.

The final position is:

> The March-April lines are review targets, not conclusions.
> The older beta-phase language should be read as a hypothesis label only.
> The real review target is retained cross-layer coupling after Normal-Hypothesis Reduction.

If normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior explains the sequence, the hypothesis should be weakened.

If normal behavior does not explain the sequence, the retained lines may represent a platform-state seam requiring deeper mobile forensic review.
