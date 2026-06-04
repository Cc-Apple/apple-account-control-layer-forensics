# Limitations and Non-Attribution Boundary

## Purpose

This document defines the public limitation and non-attribution boundary for the Shadow Cloud review package.

The purpose is to prevent overclaiming.

The package requests technical review of platform-state seams.

It does not claim attribution, malware confirmation, vendor fault, or confirmed compromise.

The current framing is:

Shadow Cloud is a non-attribution forensic model for mobile-native LOTL-like Apple platform-state anomalies.

The proposed unit of analysis is the platform-state seam, not a conventional payload, toolset, or actor label.

---

## Core Boundary

This package does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether the observed Apple ecosystem platform-state seams can be reproduced through ordinary behavior.

If normal behavior explains the sequence, the hypothesis should be weakened.

If normal behavior does not explain the sequence, the case may represent a forensic blind spot in how iOS platform-state, backup-ledger behavior, restriction state, account-cloud-document state, telecom context, and evidence preservation are currently reviewed.

---

## What This Package Does Not Claim

This package does not claim:

- actor attribution
- state attribution
- government attribution
- vendor attribution
- Apple attribution
- iMazing attribution
- Microsoft attribution
- Outlook causation
- telecom-provider attribution
- confirmed malware
- confirmed payload
- confirmed C2
- confirmed exploit chain
- confirmed spyware-family deployment
- confirmed MDM enrollment
- confirmed supervision
- confirmed configuration profile proving management
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- attacker identity
- that PC-style LOTL techniques executed directly on iOS
- that Manifest.db alone proves compromise
- that Manifest.db unreadability alone proves compromise
- that high entropy alone proves compromise
- that subjective observations are standalone proof

---

## Non-Attribution Position

Public TTP reports, spyware models, telecom concepts, Microsoft app surfaces, and Living-off-the-Land concepts are used only as comparison material or future review surfaces.

They are not used as attribution evidence.

Correct reading:

Public mechanism comparison helps reviewers understand what types of legitimate-state mechanisms may be relevant.

Incorrect reading:

Public mechanism comparison identifies the actor.

Correct reading:

LOTL-like reasoning helps explain why traces may appear in platform state rather than payloads.

Incorrect reading:

PC-style LOTL tools ran directly on iOS.

Correct reading:

Account/cloud, restriction, backup, telecom, FileProvider, and evidence-preservation states are review surfaces.

Incorrect reading:

Any vendor, app, service, telecom provider, state, government, or actor is blamed.

---

## Normal-First Review Requirement

Ordinary explanations must be tested first.

The following are treated as normal-hypothesis candidates unless stronger cross-layer coupling remains:

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

The goal is to test whether normal explanations can reproduce the full structure.

---

## Final Retained Core Lines

After final filtering limited to two primary devices, two March-April 2026 core review lines remained.

These are review targets, not conclusions.

1. 2026-03-15 to 2026-03-21  
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04  
   Centered on 2026-03-31 to 2026-04-02

The retained lines do not prove attribution.

They do not prove malware.

They do not prove confirmed MDM enrollment.

They do not prove telecom or baseband compromise.

They do not prove Microsoft or Outlook causation.

They are retained review targets after Normal-Hypothesis Reduction.

---

## Evidence Boundary

The public repository contains:

- written technical summaries
- artifact names
- referenced log titles
- timeline summaries
- machine-readable summaries
- reviewer questions
- analysis framing
- selected hash references where available

The public repository does not contain:

- raw iOS logs
- raw sysdiagnose archives
- raw screenshots
- raw videos
- private account data
- BSSID details
- Apple ID material
- OTP / financial data
- sensitive backup artifacts
- full raw device backups

Raw and sensitive materials are preserved separately.

They may be provided only through a qualified secure review process.

---

## Manifest.db / Backup-Ledger Limitation

Manifest.db unreadability or high entropy alone is not treated as evidence of compromise.

Ordinary encrypted-backup opacity may explain unreadability or high-entropy appearance.

The stronger review target is temporal coupling between backup-ledger defects and independent log-layer seams involving:

- backup/evidence behavior
- restriction state
- account/cloud trust
- telecom context
- FileProvider / account-document-provider state
- evidence-preservation behavior

This package does not claim:

- Manifest.db alone proves compromise
- unreadability alone proves compromise
- high entropy alone proves compromise
- encrypted-backup behavior proves compromise
- iMazing caused the issue
- Apple caused the issue
- Microsoft caused the issue
- Outlook caused the issue
- any backup tool caused the issue

The backup-ledger seam is supporting evidence only.

It is not proof of causation or attribution.

---

## iMazing Boundary

iMazing is treated as an acquisition surface.

iMazing is not treated as the cause.

This package does not claim:

- iMazing attribution
- iMazing causation
- iMazing malicious behavior
- iMazing intentional failure
- iMazing as an attacker tool

The review question is whether normal iMazing / iOS backup behavior can reproduce the preserved backup-ledger state and its timing against independent platform-state seams.

---

## Apple Boundary

Apple is treated as the platform and review surface.

Apple is not treated as the cause.

This package does not claim:

- Apple attribution
- Apple malicious behavior
- Apple intentional failure
- Apple vendor fault

The review question is whether normal Apple / iOS / iCloud behavior can reproduce the observed cross-layer structure.

---

## Microsoft / Outlook Boundary

Microsoft / Outlook surfaces are not treated as proven causes.

They are treated only as possible future review surfaces or auxiliary correlative surfaces.

This package does not claim:

- Microsoft attribution
- Outlook causation
- Microsoft app causation
- Microsoft service causation
- Microsoft mobile apps directly modified Manifest.db
- Microsoft mobile apps directly modified Apple backup state
- Microsoft mobile apps directly modified iOS backup services
- Microsoft surfaces caused the anomaly

The safe interpretation is:

Microsoft / Outlook surfaces, if later reviewed in preserved artifacts, should be evaluated as possible account-calendar-document-policy surfaces, not assumed causes.

---

## MDM / Restriction-State Boundary

This package does not claim confirmed MDM enrollment.

This package does not claim confirmed supervision.

This package does not claim that a configuration profile proving management was found.

The review question is narrower:

Can restriction-like behavior, ScreenTime / ManagedSettings artifacts, DMD / Digital Health recomputation, and management-adjacent daemon activity coexist with visible-management absence or MDMStatus:false under normal iOS conditions?

Relevant surfaces include:

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- managedappdistributiond
- ScreenTimeAgent
- visible profile absence
- supervision absence
- MDMStatus:false context
- Apple ID sign-out restriction behavior

The issue is a review question.

It is not proof of hidden MDM.

---

## Telecom / Baseband Boundary

Telecom, CommCenter, Baseband, SIM, BSSID/RSSI, and device-trust observations are treated as context and review surfaces.

This package does not claim:

- confirmed telecom compromise
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- telecom-provider attribution
- physical-proximity attribution

The review question is whether telecom/baseband events are independent ordinary events, or whether they align with account/cloud, restriction, backup, FileProvider, and evidence-preservation seams.

---

## Subjective Observation Boundary

Subjective observations are not treated as standalone proof.

They may be used only as timestamp context for why the observer was interacting with, preserving, or reviewing a device at a given time.

This package does not ask reviewers to accept subjective observations as evidence of compromise.

The public review target remains artifact-based:

- logs
- backup state
- Manifest-related artifacts
- RTCR / RTCReporting
- restriction-state artifacts
- account/cloud state
- telecom context
- FileProvider state
- evidence-preservation behavior
- timeline consistency

---

## Dataset Limitation

The dataset is observational.

It is not a controlled laboratory capture.

It includes multiple devices and comparison devices, but the public package does not include full raw artifacts.

The public repository is therefore not sufficient by itself to prove compromise.

It is intended to support qualified triage and scoping.

Important limitations include:

- raw artifacts are withheld from the public repository
- artifact interpretation requires qualified review
- some observations may be explained by ordinary iOS behavior
- some backup artifacts may be explained by encryption, keybag, tool, or local PC behavior
- some log clusters may be explained by storage pressure or crash behavior
- some Microsoft-adjacent traces may be ordinary residue
- some telecom events may be ordinary network behavior
- some FileProvider behavior may be ordinary cloud-document behavior
- some apparent cross-layer timing may be collection bias or processing artifact

---

## What Would Weaken the Model

The Shadow Cloud model should be weakened if qualified review shows that:

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
- retained windows are explained by collection bias
- retained windows are explained by observer-side changes
- retained windows are explained by artifact-processing error
- subjective observations are the only remaining support

If these conditions are met, the hypothesis should be weakened or rejected.

---

## What Would Strengthen the Model

The model would be strengthened if qualified review shows that:

- normal explanations do not reproduce the retained March-April core lines
- clean controls do not reproduce the same cross-layer structure
- broad keyword hits and weak temporal joins were properly removed
- non-core devices were properly excluded from final scoring
- backup-ledger defects align with independent log-layer seams
- restriction-state seams align with backup/evidence seams
- account/cloud trust-state seams align with restriction or backup/evidence seams
- telecom context aligns with backup/evidence or restriction seams
- FileProvider / account-document-provider seams align with the same windows
- Microsoft-adjacent surfaces cannot be reduced to ordinary residue
- storage pressure alone does not reproduce the preservation pattern
- cross-layer clustering remains after normal controls
- the remaining pattern is better described as platform-state seam behavior than isolated app, device, or backup-tool behavior

---

## Reviewer Questions

A qualified reviewer should ask:

1. Are any attribution claims being made?
2. Are any vendor, app, telecom provider, or spyware-family claims being made?
3. Were ordinary explanations removed before retaining the March-April lines?
4. Were broad keyword hits and weak temporal joins sufficiently filtered?
5. Were non-core devices correctly excluded from final retained scoring?
6. Can ordinary Apple / iOS / iCloud behavior reproduce the retained cross-layer structure?
7. Can ordinary iMazing / iOS backup behavior reproduce the backup-ledger defects and sidecar mismatch behavior?
8. Can ordinary encrypted-backup opacity explain the Manifest-related observations without broader coupling?
9. Can ordinary ScreenTime / Family Sharing / ManagedSettings behavior explain the restriction-state pattern?
10. Can MDMStatus:false normally coexist with the reviewed management-adjacent daemon clustering?
11. Can CommCenter / Baseband / SIM / device-trust signals be explained as independent normal events?
12. Can FileProvider and account/document-provider behavior explain the observed account-cloud-document state?
13. Can Microsoft-adjacent surfaces be explained as ordinary residue?
14. Can local PC, USB, storage pressure, or acquisition-tool behavior reproduce the preservation anomalies?
15. Does cross-layer clustering remain after normal controls?
16. If normal explanations reproduce the structure, what documented test demonstrates it?
17. If normal explanations do not reproduce the structure, does the remaining pattern justify deeper mobile forensic review?

---

## Final Position

This package is a request for qualified technical review.

It is not a public accusation.

It is not an attribution claim.

It is not a confirmed compromise report.

It is not a malware report.

It is not a vendor-fault claim.

The final position is:

Public TTP comparison is mechanism context only.

Manifest.db / backup-ledger observations are supporting evidence only.

The retained March-April lines are review targets, not conclusions.

Microsoft / Outlook surfaces are correlative or future review surfaces only.

Telecom and baseband observations are context, not compromise proof.

Subjective observations are timestamp context only, not standalone proof.

The model should be weakened if normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior reproduces the full structure.

If normal behavior does not reproduce the structure, the retained pattern may represent a platform-state forensic blind spot requiring deeper mobile forensic review.
