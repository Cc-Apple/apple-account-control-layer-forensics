# 07. Limitations and Non-Attribution Statement

## Summary

This repository is a technical triage package.

It does not assert attribution to any state, company, threat group, or individual.

APT32, APT42, and LIMINAL PANDA are used only as public TTP comparison points.

## What This Repository Claims

This repository claims only that the dataset contains recurring forensic observations that may merit technical review.

The core observations include:

- Manifest.db non-SQLite / opaque / high-entropy repetition
- usageClientId switching / discontinuity
- ScreenTime / Game Center / Content & Privacy restriction-layer signals
- absence of visible MDM / supervised / userIsManaged indicators
- March 2026 normalized density increase
- March 12, 2026 mini1 proximity/communication event
- March 7, 2026 15G Wi-Fi/BSSID location anchor
- multi-device recurrence across approximately 11 months

## What This Repository Does Not Claim

This repository does not claim:

- that APT32 executed the activity
- that APT42 executed the activity
- that LIMINAL PANDA executed the activity
- that NSO, Intellexa, Candiru, QuaDream, or any spyware vendor executed the activity
- that Apple is the attacker
- that any specific person owns or controls a BSSID
- that any specific government is responsible
- that the physical incident timeline is proven by device logs
- that these artifacts alone prove malicious control

## Why Attribution Is Not Asserted

Attribution requires evidence beyond this repository, such as:

- infrastructure ownership
- server-side logs
- Apple account access logs
- law enforcement records
- legal discovery
- cloud-provider records
- telecom-provider records
- malware samples
- direct operator mistakes
- third-party forensic validation

This repository does not contain enough evidence for attribution.

## Physical Incident Timeline

The user has a physical incident timeline.

However, physical incident claims are not used as primary technical evidence in this repository.

They may be used only as timeline context.

The primary technical evidence is based on:

- logs
- backup artifacts
- SHA256 hashes
- reproducible scripts
- derived CSV summaries
- visible device/account/control-layer artifacts

## BSSID Limitation

BSSID evidence is treated only as a location/time anchor.

It is not used to identify a person, attacker, access point owner, or device owner.

BSSID values may be redacted or hashed in public materials.

## Manifest.db Limitation

Manifest.db anomalies are important, but they do not alone prove malicious activity.

Possible explanations include:

- encrypted backup behavior
- partial or incomplete backup state
- iMazing-specific behavior
- copy or extraction artifact
- Apple backup workflow behavior
- OS/account/control-layer anomaly

The purpose of this repository is to request expert triage of these possibilities.

## ScreenTime / Restriction-Layer Limitation

ScreenTime, Game Center, Content & Privacy, ManagedSettings, and FamilyControls signals may have normal explanations.

Possible explanations include:

- user configuration
- iCloud sync
- Family Sharing
- Apple ID migration
- backup / restore artifacts
- OS bugs
- app-specific settings

The concern is the repeated combination of these signals with other anomalies, not any single string alone.

## TTP Comparison Limitation

APT32, APT42, and LIMINAL PANDA are used only for comparison.

The comparison is based on public operational patterns:

- APT32-like long-term operation, legitimate service abuse, and trace suppression
- APT42-like credential/account/cloud/identity operations
- LIMINAL-like telecom/proximity signals

This is not actor attribution.

## Data Privacy

Raw private logs are not publicly uploaded.

Sensitive identifiers should be redacted or hashed, including:

- Apple ID
- email addresses
- phone numbers
- IMEI
- ICCID
- serial numbers
- BSSID values
- exact physical addresses
- personal notes
- authentication tokens
- third-party names

## Request to Reviewers

Please review the dataset as a technical triage package.

The main question is:

Do these artifacts look like normal Apple/iOS behavior, user-side backup artifacts, or do they merit deeper forensic triage as a possible account/cloud/control-layer anomaly?

## Final Statement

This repository is not an accusation.

It is a structured technical request for independent review.
