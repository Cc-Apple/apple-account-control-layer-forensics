# BSSID / RSSI / Proximity-Context Review Report

## Purpose

This report summarizes the BSSID / RSSI / proximity-context review branch of the Shadow Cloud public package.

The purpose is technical review, not attribution.

This report does not claim physical-person attribution.

This report does not claim confirmed proximity attack.

This report does not claim confirmed Wi-Fi compromise.

This report does not claim confirmed telecom compromise.

This report does not claim confirmed baseband compromise, SIM compromise, OTP interception, malware, C2, exploit chain, vendor causation, or actor attribution.

The current review question is narrower:

> Can BSSID / RSSI / Wi-Fi / telecom-context observations be explained as ordinary network behavior, or do they align with account/cloud, restriction, backup/evidence, FileProvider, or evidence-preservation seams?

---

## Current Framing

The broader Shadow Cloud model is currently framed as:

> A non-attribution forensic model for mobile-native LOTL-like Apple platform-state anomalies.

The proposed unit of analysis is the platform-state seam, not a conventional payload, toolset, or actor label.

For this report, the relevant seam is:

> proximity / network context plus telecom / device-trust context plus platform-state timing.

This is a review target.

It is not a conclusion.

---

## Core Review Question

Can ordinary Wi-Fi roaming, local network behavior, router behavior, signal variation, iOS networking behavior, or telecom/baseband behavior explain the observed BSSID / RSSI / proximity-context artifacts when they appear near other retained platform-state seams?

Relevant review surfaces include:

- BSSID
- RSSI
- Wi-Fi channel
- Wi-Fi quality
- lastJoined timestamps
- local network anchor
- CommCenter
- Baseband
- TelephonyBaseband
- SIM context
- device-trust signals
- financial re-authentication context
- account/cloud trust state
- restriction state
- backup/evidence behavior
- FileProvider / account-document-provider state
- evidence-preservation behavior

The key question is not whether a BSSID or RSSI value exists.

The key question is whether network/proximity-context timing can be explained normally when it aligns with other retained platform-state seams.

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
- Wi-Fi provider attribution
- physical-person attribution
- confirmed malware
- confirmed payload
- confirmed C2
- confirmed exploit chain
- confirmed spyware-family deployment
- confirmed MDM enrollment
- confirmed supervision
- confirmed Wi-Fi compromise
- confirmed router compromise
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- confirmed physical tracking
- attacker identity
- that BSSID / RSSI alone proves compromise
- that proximity context alone proves compromise
- that subjective observations are standalone proof

---

## Normal-Hypothesis Reduction

Ordinary explanations must be tested first.

The following are treated as normal-hypothesis candidates unless stronger cross-layer coupling remains:

- ordinary Wi-Fi roaming
- ordinary RSSI fluctuation
- ordinary router or access-point behavior
- ordinary channel change
- ordinary lastJoined behavior
- ordinary iOS Wi-Fi quality logging
- ordinary CommCenter behavior
- ordinary baseband logging
- ordinary SIM or carrier behavior
- ordinary financial app device-trust behavior
- ordinary local network congestion
- ordinary VPN or proxy behavior
- ordinary device movement
- ordinary nearby access-point visibility
- isolated BSSID / RSSI observations
- broad keyword hits
- weak temporal joins
- non-core devices
- pre-March observations
- subjective proximity observations without artifact coupling

The purpose is not to prove a malicious explanation.

The purpose is to test whether normal network, Wi-Fi, telecom, and platform behavior can reproduce the full coupled structure.

---

## Proximity-Context Seam Definition

A proximity-context seam is a review point where Wi-Fi, radio, local-network, telecom, or device-trust context intersects with other platform-state layers.

Relevant proximity-context artifacts include:

- BSSID
- RSSI
- Wi-Fi channel
- Wi-Fi quality metrics
- lastJoined timestamps
- local access-point identifiers
- nearby network context
- network transition timing
- VPN / proxy context where relevant

Relevant adjacent layers include:

- CommCenter
- Baseband
- SIM context
- device-trust signals
- account/cloud trust state
- restriction state
- backup-ledger state
- evidence-preservation behavior
- FileProvider / account-document-provider state

The review target is not:

> Was a BSSID observed?

The review target is:

> Can network/proximity timing be reproduced normally when it aligns with account/cloud, restriction, backup/evidence, telecom, FileProvider, or preservation seams?

---

## Weak Alone

The following are weak or insufficient by themselves:

- one BSSID observation
- one RSSI value
- one Wi-Fi channel value
- one lastJoined timestamp
- one Wi-Fi quality event
- one local access-point observation
- one CommCenter event
- one Baseband event
- one SIM event
- one financial re-authentication event
- one subjective proximity report

These may be normal.

They should not be presented as standalone proof.

---

## Stronger When Coupled

BSSID / RSSI / proximity-context observations become more important if they align with independent platform-state seams.

Stronger conditions include:

- repeated proximity-context artifacts near retained core windows
- BSSID / RSSI timing near account/cloud trust-state observations
- Wi-Fi or telecom timing near restriction-state observations
- CommCenter / Baseband context near backup/evidence behavior
- device-trust signals near financial re-authentication context
- proximity-context timing near FileProvider or account-document-provider behavior
- evidence-preservation difficulty near network or telecom context
- clean controls not reproducing the same structure
- ordinary Wi-Fi / telecom behavior not reproducing the full timing pattern

The stronger review question is:

> Can normal Wi-Fi / telecom / iOS behavior reproduce proximity-context timing when it aligns with independent platform-state seams?

---

## Final Retained Core Lines

After final filtering limited to two primary devices, two March-April 2026 core review lines remained in the broader Shadow Cloud model.

These are review targets, not conclusions.

1. 2026-03-15 to 2026-03-21  
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04  
   Centered on 2026-03-31 to 2026-04-02

This proximity-context report should be read as one branch of those retained review lines where applicable.

The value is not a single BSSID or RSSI artifact.

The value is whether proximity, Wi-Fi, telecom, or device-trust timing aligns with other platform-state seams after Normal-Hypothesis Reduction.

---

## Relationship to Account / Cloud Trust State

Proximity-context observations may be more relevant when they align with account/cloud trust-state behavior.

Relevant account/cloud review surfaces include:

- Apple ID trust state
- iCloud trust state
- trusted-device behavior
- account/cloud bursts
- usage-state transitions
- authentication-adjacent behavior
- financial device-trust context

The review question is:

> Can ordinary Apple account, iCloud, and network behavior explain proximity-context timing when it aligns with other platform-state seams?

This report does not claim account compromise.

This report does not claim Apple ID takeover.

This report does not claim OTP interception.

---

## Relationship to Restriction State

Proximity-context observations may be more relevant when they align with restriction-state artifacts.

Relevant restriction surfaces include:

- ScreenTime
- ManagedSettings
- FamilyControls
- DMD / Digital Health
- MDMStatus:false context
- Apple ID sign-out restriction behavior
- visible-management absence

The review question is:

> Do proximity-context observations align with restriction-like behavior or management-adjacent daemon context?

This report does not claim confirmed MDM enrollment.

This report does not claim hidden management.

This report does not claim supervision.

---

## Relationship to Backup-Ledger Observations

Manifest.db unreadability or high entropy alone is not treated as evidence of compromise.

Backup-ledger observations become more relevant only when they align with independent platform-state seams.

For this report, the relevant question is:

> Do BSSID / RSSI / telecom-context observations align with backup/evidence behavior or backup-ledger defects?

This report does not claim that proximity context caused Manifest.db behavior.

This report does not claim that Manifest.db proves proximity-based compromise.

The review question is temporal coupling.

---

## Relationship to Evidence Preservation

Proximity-context observations may be relevant if they align with evidence-preservation difficulty.

Relevant preservation surfaces include:

- storage pressure
- backup failure paths
- screenshot / recording difficulty reports
- log-preservation difficulty
- backup-generation inconsistency
- acquisition-surface mismatch

The review question is:

> Do proximity-context observations align with evidence-preservation difficulty, or are they ordinary and independent?

Subjective observations are not standalone proof.

They may be used only as timestamp context for why the observer was interacting with or preserving the device at a given time.

---

## Relationship to Telecom Context

Telecom context is treated only as a review surface.

Relevant telecom surfaces include:

- CommCenter
- Baseband
- TelephonyBaseband
- SIM context
- carrier context
- device-trust signals
- financial re-authentication context
- telecom-adjacent logs

This report does not claim:

- confirmed telecom compromise
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- telecom-provider attribution

The review question is whether telecom/baseband events are independent ordinary events, or whether they align with proximity, account/cloud, restriction, backup, and evidence-preservation seams.

---

## Relationship to FileProvider / Account-Document State

FileProvider and account-document-provider behavior may be relevant when they align with proximity or telecom context.

Relevant surfaces include:

- FileProvider
- iCloud Drive provider state
- account-document-provider behavior
- SaveToFiles / fileproviderd activity
- document/cloud state
- attachment or provider state

The review question is:

> Can ordinary FileProvider and document-provider behavior explain the observed coupling with proximity context, trust state, restriction state, and evidence preservation?

---

## Relationship to Microsoft / Outlook

Microsoft / Outlook surfaces are not treated as proven causes.

They are treated only as possible future review surfaces or auxiliary correlative surfaces.

This report does not claim:

- Microsoft attribution
- Outlook causation
- Microsoft app causation
- Microsoft service causation
- Microsoft mobile apps directly modified Wi-Fi state
- Microsoft mobile apps directly modified telecom state
- Microsoft mobile apps directly modified Manifest.db
- Microsoft mobile apps directly modified Apple backup state
- Microsoft surfaces caused proximity-context behavior

The safe interpretation is:

> Microsoft / Outlook surfaces, if later reviewed in preserved artifacts, should be evaluated as possible account-calendar-document-policy surfaces, not assumed causes.

---

## Strengthening Conditions

The proximity-context review branch is strengthened if qualified review shows that:

- proximity-context observations align with retained core windows
- ordinary Wi-Fi roaming does not reproduce the pattern
- ordinary RSSI fluctuation does not explain the timing
- ordinary iOS Wi-Fi logging does not explain the timing
- ordinary telecom/baseband behavior does not explain the timing
- account/cloud trust-state seams align with proximity context
- restriction-state seams align with proximity context
- backup/evidence seams align with proximity context
- FileProvider / account-document-provider seams align with proximity context
- storage pressure or preservation difficulty aligns with proximity context
- clean controls do not reproduce the same structure

---

## Weakening or Falsification Conditions

The proximity-context review branch is weakened if qualified review shows that:

- ordinary Wi-Fi roaming explains the observations
- ordinary RSSI variation explains the observations
- ordinary router or access-point behavior explains the observations
- ordinary lastJoined behavior explains the observations
- ordinary iOS Wi-Fi quality logging explains the observations
- ordinary telecom/baseband behavior explains the observations
- BSSID / RSSI timing does not align with other retained seams
- financial re-authentication context is ordinary and independent
- FileProvider or account-document timing is unrelated
- Microsoft-adjacent surfaces are ordinary residue
- clean controls reproduce the same proximity-context structure
- subjective observations are the only remaining support

If these conditions are met, the proximity-context hypothesis should be weakened or rejected.

---

## Reviewer Questions

A qualified reviewer should ask:

1. Can ordinary Wi-Fi roaming explain the reviewed BSSID / RSSI observations?
2. Can ordinary RSSI fluctuation explain the reviewed signal pattern?
3. Can ordinary router or access-point behavior explain the reviewed pattern?
4. Can ordinary iOS Wi-Fi quality logging explain the pattern?
5. Can ordinary CommCenter / Baseband / SIM behavior explain the timing?
6. Does proximity-context timing align with account/cloud trust-state seams?
7. Does proximity-context timing align with restriction-state seams?
8. Does proximity-context timing align with backup/evidence seams?
9. Does proximity-context timing align with FileProvider or account-document-provider state?
10. Does proximity-context timing align with evidence-preservation difficulty?
11. Can clean controls reproduce the same proximity-context structure?
12. If normal explanations reproduce the structure, what documented test demonstrates it?
13. If normal explanations do not reproduce the structure, does the proximity-context seam justify deeper mobile forensic review?

---

## Final Position

This report does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether the observed BSSID / RSSI / proximity-context seams can be reproduced through ordinary behavior.

The final position is:

> BSSID / RSSI observations are review targets, not conclusions.
> Proximity context alone does not prove compromise.
> Telecom context alone does not prove compromise.
> The strongest issue is cross-layer coupling after Normal-Hypothesis Reduction.

If normal Wi-Fi / telecom / iOS behavior explains the sequence, the proximity-context branch should be weakened.

If normal behavior does not explain the sequence, the proximity-context seam may remain a supporting branch within the broader Shadow Cloud platform-state review model.
