# Working Hypothesis Matrix: Shadow Cloud Platform-State Seam Review

## Purpose

This document defines the working hypothesis matrix for the Shadow Cloud review package.

The purpose is technical review, not attribution.

The matrix does not claim that any hypothesis is proven.

The matrix does not claim malware, actor attribution, vendor causation, confirmed MDM enrollment, telecom compromise, baseband compromise, SIM compromise, or OTP interception.

The current framing is:

Shadow Cloud is a non-attribution forensic model for mobile-native LOTL-like Apple platform-state anomalies.

The proposed unit of analysis is the platform-state seam, not a conventional payload, toolset, or actor label.

---

## Current Top-Level Model

The current top-level review model is:

> Mobile-native LOTL-like Apple platform-state anomaly.

Short formulation:

Traditional LOTL:
Living off tools.

Shadow Cloud:
Living off Apple platform state.

Backup branch:
Living off Apple backup state.

This model asks whether legitimate Apple ecosystem states can become the observable surface of recurring forensic anomalies.

It does not claim that PC-style LOTL techniques executed directly on iOS.

It does not identify an actor.

It does not prove compromise.

It provides a falsifiable structure for review.

---

## Normal-Hypothesis Reduction

All hypotheses below must be tested normal-first.

The following explanations are treated as noise or normal-hypothesis candidates unless stronger cross-layer coupling remains:

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

The purpose is not to prove a malicious explanation.

The purpose is to test whether normal explanations can reproduce the full cross-layer structure.

---

## Final Retained Core Lines

After final filtering limited to two primary devices, two March-April 2026 core review lines remained.

These are review targets, not conclusions.

1. 2026-03-15 to 2026-03-21  
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04  
   Centered on 2026-03-31 to 2026-04-02

The value of these lines is not any single artifact.

The value is retained overlap across multiple platform-state seams after Normal-Hypothesis Reduction.

---

## Matrix Summary

The matrix is organized into eight review hypotheses.

Each hypothesis is a review question, not a conclusion.

1. Platform-State Seam Hypothesis
2. Policy-State / Restriction-State Hypothesis
3. Backup-Ledger Seam Hypothesis
4. Evidence-Preservation Hypothesis
5. Account / Cloud Trust-State Hypothesis
6. Telecom / Device-Trust Context Hypothesis
7. FileProvider / Account-Document State Hypothesis
8. Auxiliary Microsoft-Adjacent Surface Hypothesis

The strongest current model is not any one hypothesis in isolation.

The strongest current model is the coupling of multiple hypotheses across the retained March-April core lines.

---

## Hypothesis 1: Platform-State Seam Hypothesis

### Review Question

Can legitimate Apple ecosystem platform states form a recurring anomaly surface without relying on visible malware, C2, exploit-chain proof, or actor attribution?

### Relevant Surfaces

- Apple ID trust state
- iCloud trust state
- trusted-device behavior
- usage-state transitions
- restriction state
- backup-ledger state
- telecom context
- FileProvider state
- evidence-preservation behavior

### Supporting Pattern

This hypothesis is supported only if multiple platform-state surfaces cluster in the same review windows after normal explanations are removed.

### Weak Alone

Weak by itself:

- one unusual log
- one crash
- one backup issue
- one storage event
- one account event
- one telecom event
- one subjective observation

### Strengthening Conditions

This hypothesis is strengthened if:

- cross-layer clustering remains after normal controls
- clean controls do not reproduce the same pattern
- retained windows cannot be explained by isolated device failure
- platform-state seams appear across account, restriction, backup, telecom, and preservation layers

### Weakening Conditions

This hypothesis is weakened if:

- documented Apple / iOS behavior reproduces the full structure
- clean control devices reproduce the same clustering
- retained windows are explained by processing error or collection bias
- each layer is independently normal and timing overlap disappears after correction

---

## Hypothesis 2: Policy-State / Restriction-State Hypothesis

### Review Question

Can restriction-like behavior surface while ordinary visible management indicators remain absent or false?

### Relevant Surfaces

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- MDMStatus:false context
- visible profile absence
- supervision absence
- Apple ID sign-out restriction behavior
- management-adjacent daemon clustering

### Supporting Pattern

This hypothesis is supported only if restriction-state artifacts align with account/cloud, backup/evidence, telecom, or FileProvider seams.

### Weak Alone

Weak by itself:

- ScreenTime artifact alone
- ManagedSettings artifact alone
- MDMStatus:false alone
- dmd or ScreenTimeAgent crash alone
- user-interface restriction report without artifact context

### Strengthening Conditions

This hypothesis is strengthened if:

- restriction-state artifacts align with retained core windows
- MDMStatus:false coexists with management-adjacent daemon clustering
- visible-management absence conflicts with effective restriction-like behavior
- normal ScreenTime / Family Sharing behavior does not reproduce the pattern
- restriction-state timing aligns with backup/evidence or account/cloud seams

### Weakening Conditions

This hypothesis is weakened if:

- ordinary ScreenTime settings explain the pattern
- Family Sharing explains the restriction behavior
- documented iOS behavior explains MDMStatus:false plus daemon clustering
- user configuration explains the observed state
- restriction-state timing does not align with other retained seams

---

## Hypothesis 3: Backup-Ledger Seam Hypothesis

### Review Question

Can normal Apple / iOS / iMazing backup behavior reproduce backup-ledger defects when those defects align with independent platform-state seams?

### Relevant Surfaces

- Manifest.db
- Manifest.plist
- Status.plist
- Info.plist
- RTCR / RTCReporting
- sidecar mismatch
- success-like mismatch
- encrypted versus unencrypted backup behavior
- iMazing / iOS backup generation state

### Supporting Pattern

This hypothesis is supported only when backup-ledger defects align with other independent seams.

### Weak Alone

Weak by itself:

- Manifest.db unreadability
- high entropy
- SQLite open failure
- file is not a database error
- expected SQLite header absence
- encrypted-backup opacity
- one-off backup failure
- tool-specific parse failure

### Strengthening Conditions

This hypothesis is strengthened if:

- backup-ledger defects persist after correct handling
- ordinary encrypted-backup opacity does not fully explain the state
- sidecar mismatch or success-like mismatch remains
- Status.plist / Manifest.plist / RTCR indicate meaningful backup state
- clean controls do not reproduce the same structure
- backup-ledger defects align with restriction, account/cloud, telecom, FileProvider, or evidence-preservation seams

### Weakening Conditions

This hypothesis is weakened if:

- Manifest.db opens normally after proper handling
- encrypted backup behavior fully explains the state
- iMazing documentation or reproducible testing explains the behavior
- local PC / USB / file-lock / storage conditions reproduce the pattern
- backup-ledger defects do not align with independent platform-state seams

---

## Hypothesis 4: Evidence-Preservation Hypothesis

### Review Question

Can ordinary storage pressure, local PC behavior, or backup-tool behavior explain evidence-preservation difficulty without invoking a broader platform-state seam?

### Relevant Surfaces

- storage pressure
- backup failure paths
- screenshot / recording difficulty reports
- log-preservation difficulty
- backup-generation inconsistency
- acquisition-surface mismatch
- preservation-time artifact instability

### Supporting Pattern

This hypothesis is supported only when preservation difficulty aligns with independent technical artifacts.

### Weak Alone

Weak by itself:

- storage pressure alone
- screenshot difficulty alone
- backup failure alone
- local PC issue alone
- user observation alone

### Strengthening Conditions

This hypothesis is strengthened if:

- preservation difficulty aligns with retained core windows
- backup failures align with backup-ledger defects
- storage pressure aligns with restriction, account/cloud, or telecom seams
- clean controls do not reproduce the same preservation failure pattern
- local PC / USB / storage explanations do not reproduce the full structure

### Weakening Conditions

This hypothesis is weakened if:

- low storage alone explains the sequence
- local PC or USB behavior reproduces the issue
- backup-tool behavior fully explains the failure
- preservation difficulty does not align with independent log-layer seams
- subjective observations are the only remaining support

---

## Hypothesis 5: Account / Cloud Trust-State Hypothesis

### Review Question

Can ordinary Apple account and iCloud behavior explain the timing and recurrence of the observed trust-state seams?

### Relevant Surfaces

- Apple ID trust state
- iCloud trust state
- trusted-device behavior
- account/cloud bursts
- usage-state transitions
- authentication-adjacent behavior
- financial device-trust context

### Supporting Pattern

This hypothesis is supported only when account/cloud trust-state behavior aligns with other retained seams.

### Weak Alone

Weak by itself:

- ordinary iCloud sync issue
- isolated account prompt
- isolated trust-device event
- isolated authentication event
- isolated financial app re-authentication

### Strengthening Conditions

This hypothesis is strengthened if:

- account/cloud events align with retained core windows
- trusted-device behavior aligns with restriction or backup/evidence seams
- usage-state transitions align with other platform-state seams
- financial device-trust signals align with telecom or account/cloud context
- normal account behavior does not reproduce the full timing structure

### Weakening Conditions

This hypothesis is weakened if:

- ordinary iCloud behavior explains the events
- ordinary Apple ID authentication explains the timing
- financial app behavior is independent and ordinary
- account/cloud timing does not align with other retained seams
- clean controls reproduce the same behavior

---

## Hypothesis 6: Telecom / Device-Trust Context Hypothesis

### Review Question

Are telecom/baseband events independent ordinary events, or do they align with account/cloud, restriction, backup, and evidence-preservation seams?

### Relevant Surfaces

- CommCenter
- Baseband
- TelephonyBaseband
- SIM context
- device-trust signals
- financial re-authentication context
- telecom-adjacent logs
- BSSID / RSSI context where relevant

### Supporting Pattern

This hypothesis is supported only when telecom context aligns with retained platform-state seams.

### Weak Alone

Weak by itself:

- CommCenter crash alone
- Baseband log alone
- SIM event alone
- BSSID/RSSI event alone
- financial re-authentication alone
- telecom timing without other seams

### Strengthening Conditions

This hypothesis is strengthened if:

- telecom context aligns with retained core windows
- CommCenter / Baseband timing aligns with restriction or account/cloud seams
- device-trust signals align with account/cloud or financial re-authentication context
- telecom context aligns with backup/evidence or preservation difficulty
- normal telecom behavior does not reproduce the full timing structure

### Weakening Conditions

This hypothesis is weakened if:

- telecom/baseband events are ordinary and independent
- BSSID/RSSI observations are ordinary Wi-Fi behavior
- financial re-authentication is explained by normal app policy
- telecom timing does not align with retained seams
- clean controls reproduce the same telecom context

---

## Hypothesis 7: FileProvider / Account-Document State Hypothesis

### Review Question

Can ordinary FileProvider and document-provider behavior explain the observed coupling with trust state, restriction state, and evidence preservation?

### Relevant Surfaces

- FileProvider
- iCloud Drive provider state
- account-document-provider behavior
- document/cloud state
- SaveToFiles / fileproviderd activity
- provider authentication mismatch
- attachment or document-provider state

### Supporting Pattern

This hypothesis is supported only when FileProvider or account/document-provider state aligns with retained platform-state seams.

### Weak Alone

Weak by itself:

- FileProvider activity alone
- iCloud Drive provider state alone
- SaveToFiles event alone
- document-provider artifact alone
- account-document state without timing alignment

### Strengthening Conditions

This hypothesis is strengthened if:

- FileProvider state aligns with retained core windows
- provider authentication state aligns with account/cloud or restriction seams
- fileproviderd activity aligns with evidence-preservation difficulty
- document-provider state aligns with backup/evidence seams
- normal FileProvider behavior does not reproduce the timing structure

### Weakening Conditions

This hypothesis is weakened if:

- FileProvider behavior is ordinary and unrelated
- iCloud Drive provider state is normally explained
- document-provider activity is normal app behavior
- FileProvider timing does not align with retained seams
- clean controls reproduce the same behavior

---

## Hypothesis 8: Auxiliary Microsoft-Adjacent Surface Hypothesis

### Review Question

Can Microsoft-adjacent surfaces be explained as ordinary residue, or do they remain useful as future account-calendar-document-policy review surfaces?

### Relevant Surfaces

- Outlook / Microsoft app residue
- account-calendar-document state
- Microsoft 365 / Exchange / OAuth / document-provider surfaces
- FileProvider-adjacent document state
- calendar or meeting objects
- attachments
- document-provider behavior

### Boundary

These surfaces are correlative only in this public package.

This hypothesis does not claim:

- Microsoft attribution
- Outlook causation
- Microsoft app causation
- Microsoft service causation
- Microsoft mobile apps directly modified Manifest.db
- Microsoft mobile apps directly modified Apple backup state
- Microsoft mobile apps directly modified iOS backup services

### Supporting Pattern

This hypothesis is supported only if Microsoft-adjacent surfaces align with retained platform-state seams and cannot be reduced to ordinary residue.

### Weak Alone

Weak by itself:

- Microsoft app residue
- Outlook traces
- calendar traces
- document-provider traces
- historical login residue
- app install / uninstall residue

### Strengthening Conditions

This hypothesis is strengthened if:

- Microsoft-adjacent traces align with retained core windows
- account-calendar-document state aligns with FileProvider or backup/evidence seams
- traces cannot be explained as ordinary residue
- document-provider or OAuth-related surfaces align with account/cloud or restriction seams
- preserved artifacts support the timing relationship

### Weakening Conditions

This hypothesis is weakened if:

- Microsoft-adjacent surfaces are ordinary residue
- Outlook traces are old login remnants
- calendar/document traces are ordinary app behavior
- traces do not align with retained core windows
- preserved artifacts do not support the timing relationship

---

## Cross-Hypothesis Coupling

The strongest current review target is not any single hypothesis.

The strongest review target is coupling across multiple hypotheses.

Relevant coupling patterns include:

- account/cloud trust state plus restriction state
- restriction state plus backup/evidence behavior
- backup-ledger defects plus evidence-preservation difficulty
- telecom context plus account/cloud or restriction state
- FileProvider state plus account/document-provider state
- Microsoft-adjacent surfaces plus account-document state
- retained windows surviving Normal-Hypothesis Reduction

The model becomes weaker if each layer is independently normal and the timing overlap disappears.

The model becomes stronger if the cross-layer structure remains after normal controls.

---

## Reviewer Questions

A qualified reviewer should ask:

1. Are all hypotheses being treated as review questions, not conclusions?
2. Were ordinary explanations removed before retaining the March-April lines?
3. Were broad keyword hits and weak temporal joins sufficiently filtered?
4. Were non-core devices correctly excluded from final retained scoring?
5. Can ordinary Apple / iOS / iCloud behavior reproduce the retained cross-layer structure?
6. Can ordinary iMazing / iOS backup behavior reproduce the backup-ledger defects and sidecar mismatch behavior?
7. Can ordinary encrypted-backup opacity explain the Manifest-related observations without broader coupling?
8. Can ordinary ScreenTime / Family Sharing / ManagedSettings behavior explain the restriction-state pattern?
9. Can MDMStatus:false normally coexist with the reviewed management-adjacent daemon clustering?
10. Can CommCenter / Baseband / SIM / device-trust signals be explained as independent normal events?
11. Can FileProvider and account/document-provider behavior explain the observed account-cloud-document state?
12. Can Microsoft-adjacent surfaces be explained as ordinary residue?
13. Can local PC, USB, storage pressure, or acquisition-tool behavior reproduce the preservation anomalies?
14. Does cross-layer clustering remain after normal controls?
15. If normal explanations reproduce the structure, what documented test demonstrates it?
16. If normal explanations do not reproduce the structure, does the remaining pattern justify deeper mobile forensic review?

---

## Final Position

This matrix does not prove the Shadow Cloud hypothesis.

It organizes review questions.

The strongest current model is:

> mobile-native LOTL-like Apple platform-state anomaly.

The strongest current evidence unit is:

> retained cross-layer platform-state seam coupling after Normal-Hypothesis Reduction.

The final position is:

- each hypothesis is falsifiable
- each hypothesis must be tested normal-first
- no hypothesis asserts attribution
- no hypothesis asserts vendor causation
- no hypothesis asserts confirmed malware
- no hypothesis asserts confirmed MDM enrollment
- no hypothesis asserts telecom, baseband, SIM, or OTP compromise
- the retained March-April lines are review targets, not conclusions

If normal behavior explains the retained structure, the hypotheses should be weakened.

If normal behavior does not explain the retained structure, the matrix may help guide deeper mobile forensic review.
