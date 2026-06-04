# ScreenTime / ManagedSettings / Restriction-State Review Report

## Purpose

This report summarizes the restriction-state review branch of the Shadow Cloud public package.

The purpose is technical review, not attribution.

This report does not claim confirmed MDM enrollment.

This report does not claim confirmed supervision.

This report does not claim that a configuration profile proving management was found.

This report does not claim Apple attribution, Microsoft attribution, Outlook causation, telecom compromise, malware, C2, exploit chain, or actor attribution.

The current review question is narrower:

> Can restriction-like behavior surface through ScreenTime / ManagedSettings / DMD / Apple ID sign-out behavior while ordinary visible management indicators remain absent or false?

---

## Current Framing

The broader Shadow Cloud model is currently framed as:

> A non-attribution forensic model for mobile-native LOTL-like Apple platform-state anomalies.

The proposed unit of analysis is the platform-state seam, not a conventional payload, toolset, or actor label.

For this report, the relevant seam is:

> restriction state plus visible-management absence plus management-adjacent daemon context.

This is a review target.

It is not a conclusion.

---

## Core Review Question

Can normal Apple / iOS / iCloud / ScreenTime / Family Sharing / ManagedSettings behavior explain a pattern where restriction-like behavior appears while ordinary visible management indicators are absent, false, or not sufficient to explain the observed state?

Relevant review surfaces include:

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- Game Center restriction behavior
- Apple ID sign-out restriction behavior
- MDMStatus:false context
- visible profile absence
- supervision absence
- managedappdistributiond
- ScreenTimeAgent
- FileProvider / iCloud state
- account/cloud trust state
- evidence-preservation behavior

---

## What This Report Does Not Claim

This report does not claim:

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
- that restriction-state artifacts alone prove compromise
- that subjective observations are standalone proof

---

## Normal-Hypothesis Reduction

Ordinary explanations must be tested first.

The following are treated as normal-hypothesis candidates unless stronger cross-layer coupling remains:

- ordinary ScreenTime settings
- ordinary Family Sharing behavior
- ordinary Content & Privacy restrictions
- user-side configuration
- old or forgotten ScreenTime passcode state
- normal Game Center restriction behavior
- ordinary ManagedSettings behavior
- ordinary DMD / Digital Health recomputation
- ordinary iOS crash clustering
- ordinary account sign-in state
- ordinary iCloud state
- ordinary FileProvider behavior
- local device state
- isolated device failure
- storage pressure
- broad keyword hits
- weak temporal joins
- restriction artifacts without backup/evidence overlap
- restriction artifacts without account/cloud or telecom context

The purpose is not to prove a malicious explanation.

The purpose is to test whether normal Apple / iOS behavior can reproduce the full coupled structure.

---

## Restriction-State Seam Definition

A restriction-state seam is a review point where restriction-related artifacts intersect with other platform-state layers.

Relevant restriction-layer artifacts include:

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- Game Center restriction behavior
- Apple ID sign-out restriction behavior
- Content & Privacy restriction behavior
- local restriction stores
- visible profile absence
- supervision absence
- MDMStatus:false context

Relevant adjacent layers include:

- Apple ID trust state
- iCloud trust state
- FileProvider state
- backup-ledger state
- evidence-preservation behavior
- telecom context
- management-adjacent daemon activity

The review target is not:

> Was ScreenTime present?

The review target is:

> Can the observed restriction-like behavior and management-adjacent context be reproduced under ordinary visible-management absence?

---

## Visible Management Boundary

This report does not claim classic visible MDM enrollment.

This report does not claim confirmed supervision.

This report does not claim a configuration profile proving management.

The issue is the mismatch:

- restriction-like behavior appears
- management-adjacent daemons or services appear
- visible MDM / supervision / profile indicators are absent, false, or insufficient
- account/cloud, FileProvider, backup/evidence, or telecom context may align with the same window

The review question is:

> Can visible management absence normally coexist with the observed restriction-state and management-adjacent artifact pattern?

---

## Relevant Artifact Families

### ScreenTime

Review focus:

- ScreenTime state
- ScreenTime settings behavior
- Content & Privacy restrictions
- Apple ID sign-out restriction behavior
- ScreenTime passcode context
- local restriction behavior

Weak alone:

- ScreenTime artifact alone
- user interface restriction report alone
- old passcode possibility alone
- one isolated ScreenTime log

Stronger when coupled with:

- ManagedSettings artifacts
- DMD / Digital Health recomputation
- MDMStatus:false context
- Apple ID / iCloud trust-state anomalies
- FileProvider / account-document state
- backup/evidence-preservation seams
- telecom context

---

### ManagedSettings

Review focus:

- ManagedSettings state
- restriction-related store behavior
- policy-like recomputation
- interaction with ScreenTime / FamilyControls
- interaction with DMD / Digital Health

Weak alone:

- ManagedSettings artifact alone
- isolated recomputation
- normal app restriction behavior

Stronger when coupled with:

- visible-management absence
- MDMStatus:false context
- ScreenTime UI behavior
- Apple ID sign-out restriction behavior
- account/cloud bursts
- backup/evidence overlap
- FileProvider state

---

### DMD / Digital Health

Review focus:

- restriction recomputation
- Digital Health activity
- ScreenTime-related recomputation
- Game Center or social restriction context
- timing against user-visible restriction behavior

Weak alone:

- dmd activity alone
- Digital Health activity alone
- recomputation without user-visible effect

Stronger when coupled with:

- ScreenTime / ManagedSettings state
- MDMStatus:false context
- visible profile absence
- Apple Support or support-window observations
- account/cloud or FileProvider state
- evidence-preservation behavior

---

### Game Center Restriction Behavior

Review focus:

- Game Center visibility
- Game Center social / friends restriction behavior
- restriction baseline
- timing against ScreenTime / ManagedSettings / DMD recomputation

Weak alone:

- Game Center UI artifact alone
- normal Game Center setting
- isolated social restriction behavior

Stronger when coupled with:

- ScreenTime / ManagedSettings state
- Apple ID / iCloud state
- support-window timing
- visible-management absence
- DMD recomputation

---

### MDMStatus:false Context

Review focus:

- MDMStatus:false
- IsSupervised:false
- visible profile absence
- empty or absent payload structures
- absence of ordinary user-facing management indicators

Weak alone:

- MDMStatus:false alone
- IsSupervised:false alone
- empty profile list alone

Stronger when coupled with:

- management-adjacent daemon clustering
- ScreenTime / ManagedSettings behavior
- Apple ID sign-out restriction behavior
- DMD / Digital Health recomputation
- account/cloud trust-state seams
- backup/evidence seams
- telecom context

The review question is not:

> Does MDMStatus:false prove hidden management?

The review question is:

> Can MDMStatus:false normally coexist with the reviewed restriction-state and management-adjacent clustering?

---

## Final Retained Core Lines

After final filtering limited to two primary devices, two March-April 2026 core review lines remained in the broader Shadow Cloud model.

These are review targets, not conclusions.

1. 2026-03-15 to 2026-03-21  
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04  
   Centered on 2026-03-31 to 2026-04-02

This restriction-state report should be read as one branch of those retained review lines where applicable.

The value is not any single ScreenTime or ManagedSettings artifact.

The value is whether restriction-state artifacts align with other platform-state seams after normal-hypothesis reduction.

---

## Relationship to Backup-Ledger Observations

Manifest.db unreadability or high entropy alone is not treated as evidence of compromise.

Backup-ledger observations become more relevant only when they align with independent platform-state seams.

For this report, the relevant question is:

> Do restriction-state seams align with backup/evidence behavior or backup-ledger defects?

This report does not claim that restriction-state artifacts caused Manifest.db behavior.

This report does not claim that Manifest.db proves restriction-state compromise.

The review question is temporal coupling.

---

## Relationship to Account / Cloud Trust State

Restriction-state artifacts may be more relevant when they align with account/cloud trust-state observations.

Relevant account/cloud review surfaces include:

- Apple ID trust state
- iCloud trust state
- trusted-device behavior
- account/cloud bursts
- usage-state transitions
- FileProvider / iCloud Drive state

The review question is:

> Can ordinary Apple account and iCloud behavior explain the timing and recurrence of restriction-state seams?

---

## Relationship to FileProvider / Account-Document State

FileProvider and account-document-provider behavior may be relevant when they align with restriction-state artifacts.

Relevant surfaces include:

- FileProvider
- iCloud Drive provider state
- account-document-provider behavior
- SaveToFiles / fileproviderd activity
- document/cloud state

The review question is:

> Can ordinary FileProvider and document-provider behavior explain the observed coupling with restriction state and evidence preservation?

---

## Relationship to Telecom Context

Telecom context is treated only as a review surface.

This report does not claim:

- confirmed telecom compromise
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- telecom-provider attribution

The review question is whether telecom/baseband events are independent ordinary events, or whether they align with restriction, account/cloud, backup, and evidence-preservation seams.

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
- Microsoft surfaces caused restriction-state behavior

The safe interpretation is:

> Microsoft / Outlook surfaces, if later reviewed in preserved artifacts, should be evaluated as possible account-calendar-document-policy surfaces, not assumed causes.

---

## Strengthening Conditions

The restriction-state review branch is strengthened if qualified review shows that:

- restriction-state artifacts align with retained core windows
- normal ScreenTime / Family Sharing behavior does not reproduce the pattern
- MDMStatus:false coexists with management-adjacent daemon clustering in a way not explained by ordinary iOS behavior
- visible-management absence conflicts with effective restriction-like behavior
- DMD / Digital Health recomputation aligns with user-visible restriction behavior
- ManagedSettings aligns with ScreenTime or FamilyControls state
- Apple ID sign-out restriction behavior aligns with account/cloud trust-state seams
- restriction-state timing aligns with backup/evidence seams
- restriction-state timing aligns with FileProvider or account-document-provider state
- restriction-state timing aligns with telecom context
- clean controls do not reproduce the same structure

---

## Weakening or Falsification Conditions

The restriction-state review branch is weakened if qualified review shows that:

- ordinary ScreenTime settings explain the pattern
- Family Sharing explains the restriction behavior
- user configuration explains the observed state
- documented iOS behavior explains MDMStatus:false plus daemon clustering
- ManagedSettings behavior is ordinary and unrelated
- DMD / Digital Health recomputation is ordinary and unrelated
- Game Center behavior is ordinary and unrelated
- Apple ID sign-out restriction behavior is explained by normal settings
- restriction-state timing does not align with other retained seams
- clean controls reproduce the same behavior
- subjective observations are the only remaining support

If these conditions are met, the restriction-state hypothesis should be weakened or rejected.

---

## Reviewer Questions

A qualified reviewer should ask:

1. Can ordinary ScreenTime settings explain the reviewed restriction behavior?
2. Can Family Sharing explain the reviewed restriction behavior?
3. Can local user configuration explain the reviewed restriction behavior?
4. Can ManagedSettings / DMD / Digital Health recomputation explain the pattern under ordinary iOS behavior?
5. Can MDMStatus:false normally coexist with the reviewed management-adjacent daemon clustering?
6. Can visible-management absence coexist with the observed restriction-state artifacts under normal conditions?
7. Can Apple ID sign-out restriction behavior be explained by ordinary settings?
8. Can Game Center restriction behavior be explained by ordinary settings?
9. Does restriction-state timing align with account/cloud trust-state seams?
10. Does restriction-state timing align with backup/evidence seams?
11. Does restriction-state timing align with FileProvider or account-document-provider state?
12. Does restriction-state timing align with telecom context?
13. Can clean controls reproduce the same restriction-state structure?
14. If normal explanations reproduce the structure, what documented test demonstrates it?
15. If normal explanations do not reproduce the structure, does the restriction-state seam justify deeper mobile forensic review?

---

## Final Position

This report does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether the observed restriction-state seams can be reproduced through ordinary behavior.

The final position is:

> Restriction-state artifacts are review targets, not conclusions.
> MDMStatus:false does not prove hidden management.
> Visible-management absence plus restriction-like behavior is a review question.
> The strongest issue is cross-layer coupling after Normal-Hypothesis Reduction.

If normal Apple / iOS / iCloud / ScreenTime / Family Sharing / ManagedSettings behavior explains the sequence, the restriction-state branch should be weakened.

If normal behavior does not explain the sequence, the restriction-state seam may remain a supporting branch within the broader Shadow Cloud platform-state review model.
