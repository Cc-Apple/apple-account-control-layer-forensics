# Limitations and Non-Attribution Statement

## Status

Public technical limitation and non-attribution statement.

This document defines the boundary of the Shadow Cloud working hypothesis.

It is intended to prevent this repository from being misread as an attribution claim, a confirmed malware report, a confirmed spyware report, or a claim against any vendor, country, group, company, product, service, or individual.

---

## Core position

This repository does not claim certainty.

This repository requests qualified technical review.

The observed dataset appears to show repeated structural anomalies across Apple account, iCloud, backup, restriction, daemon, telecom, proximity, account-calendar-document, and evidence-preservation layers.

However, the current public package does not establish:

* confirmed malware
* confirmed payload
* confirmed C2 infrastructure
* confirmed exploit chain
* confirmed spyware-family deployment
* confirmed MDM enrollment
* confirmed attacker identity
* confirmed state attribution
* confirmed vendor attribution
* confirmed Apple attribution
* confirmed iMazing attribution
* confirmed Microsoft attribution
* confirmed Outlook causation
* confirmed telecom compromise
* confirmed baseband compromise
* confirmed SIM compromise
* confirmed OTP interception

The central question remains:

> Can the observed long-term, cross-device Apple ecosystem artifact structure be explained as normal Apple / iOS / iCloud / iMazing behavior, Microsoft app residue, ordinary account-calendar-document behavior, user-side artifact, local environment issue, isolated device failure, or ordinary configuration state?

If yes, the hypothesis should be weakened or rejected.

If no, the case may merit deeper forensic review as a possible Apple platform-state / backup-ledger / evidence-preservation anomaly.

---

## Maximum working hypothesis boundary

The current maximum mechanism-level hypothesis is:

> Shadow Cloud may represent a mobile-native LOTL-like Apple platform-state anomaly.

This is not an attribution claim.

This is not a confirmed abuse claim.

This is not a claim that any named actor, vendor, product, app, or service caused the observed behavior.

The model asks whether a PC / enterprise-style Living-off-the-Land concept may have a mobile-native equivalent, where legitimate mobile apps, accounts, cloud identity, calendar, document, policy, backup, telecom, and evidence-preservation states become the observable control surface.

The current hierarchy is:

```text
Shadow Cloud
= non-attribution working hypothesis

Mobile-native LOTL-like Apple platform-state anomaly
= maximum current mechanism-level hypothesis

Outlook / Microsoft account-cloud-calendar-document surface
= possible entry / state surface candidate for future review

Manifest.db / backup-ledger seam
= byproduct / observable evidence-preservation seam

APT42-style ACMS
= account / cloud / mobile-surveillance comparison reference

APT32-style historical transfer
= secondary operational-history comparison reference

Attribution
= not asserted
```

The key boundary is:

* Manifest.db is not treated as the root cause.
* Manifest.db / backup-ledger abnormality is treated as a possible byproduct or observable evidence-preservation seam.
* Outlook / Microsoft mobile surfaces are not treated as proven causes.
* Outlook / Microsoft surfaces are treated as possible account-cloud-calendar-document entry or state surfaces for future review.
* iMazing is not treated as the cause.
* iMazing is treated as an acquisition surface.
* Apple backup state is treated as the review surface.

---

## Updated TTP framing boundary

The recommended current framing is:

> Shadow Cloud is a non-attribution, LOTL-like Apple platform-state / trust-state anomaly hypothesis.

This means the primary review target is not a named actor.

The primary review target is whether Apple ecosystem state itself appears to behave abnormally across:

* Apple ID trust state
* iCloud trust state
* trusted-device behavior
* usageClientId / usage-state transitions
* ScreenTime
* ManagedSettings
* FamilyControls
* MDMStatus:false with management-adjacent daemon activity
* backup-ledger behavior
* Manifest.db / Manifest.plist / Status.plist
* RTCR / RTCReporting
* CommCenter / Baseband / SIM / OTP context
* BSSID / RSSI proximity context
* account-cloud-calendar-document state
* evidence-preservation behavior

In short:

> Not living off tools.
> Living off Apple platform state.

For the backup layer, the narrower formulation is:

> Living off Apple backup state.

This is a mechanism-level framing.

It is not attribution.

It is not a confirmed abuse claim.

It is not a claim that any named actor, vendor, tool, app, or service performed the observed activity.

---

## Why the LOTL-like framing is not attribution

Living-off-the-Land-like framing describes a mechanism or detection problem.

It does not identify an actor.

Traditional Living-off-the-Land activity usually refers to the use of legitimate tools, valid accounts, normal processes, native administrative utilities, or ordinary cloud operations to avoid detection.

The Shadow Cloud hypothesis applies a similar logic to Apple ecosystem state.

The suspected surface is not primarily:

* PowerShell
* WMI
* RDP
* PsExec
* SSH
* VPN tools
* enterprise admin consoles

The suspected surface is Apple platform state.

Therefore, the LOTL-like framing should be read as:

> A mechanism-level comparison about how activity may blend into legitimate platform behavior.

It should not be read as:

> A claim that a specific known LOTL actor performed the activity.

It should also not be read as:

> A claim that the word “abuse” proves intent, actor identity, or confirmed malicious control.

Where public-facing language requires maximum caution, this repository prefers:

> LOTL-like Apple platform-state anomaly.

---

## Relationship to mobile-native LOTL-like model

The mobile-native LOTL-like model is an extension of the mechanism-level framing.

It does not claim that PC LOTL tools are running on iPhone.

It does not claim:

```text
PowerShell on iPhone.
```

The mobile-native question is different:

> Can normal-looking mobile platform state become the control and observation surface?

Relevant mobile-native surfaces may include:

* legitimate mobile apps
* legitimate account state
* legitimate cloud state
* legitimate calendar / meeting state
* legitimate document-provider state
* legitimate token / OAuth state
* legitimate policy / restriction state
* legitimate backup state
* legitimate telecom / SIM / OTP state
* legitimate evidence-preservation behavior

The model is treated as a review hypothesis only.

It must be tested against normal explanations first.

---

## Relationship to backup-ledger seam

The updated Shadow Cloud model includes a focused backup-layer branch:

> Backup-ledger seam in mobile LOTL-like platform-state anomaly.

This branch concerns Manifest.db / backup-ledger behavior.

It does not claim that Manifest.db alone proves the case.

It does not claim that backup-ledger abnormality proves an actor.

It does not claim that iMazing caused the anomaly.

The safer technical framing is:

```text
iMazing = acquisition surface

Apple backup state = review surface

Manifest.db = observable backup-ledger seam
```

The review question is:

> Can normal Apple / iOS / iMazing backup behavior explain repeated Manifest.db / backup-ledger abnormality across preserved backup generations, especially when aligned with broader trust-state, restriction-state, daemon-layer, telecom, and evidence-preservation anomalies?

If yes, the backup-ledger seam hypothesis should be weakened.

If no, the backup ledger may require deeper forensic review as a possible evidence-preservation seam.

---

## Relationship to APT42

APT42 is referenced only as a public TTP comparison point.

APT42-style public reporting is relevant because it emphasizes:

* account targeting
* credential / MFA / OTP targeting
* cloud access
* mobile surveillance
* long-term monitoring
* low-noise collection
* cross-layer observation of human, authentication, cloud, and mobile behavior

This is useful for comparing account / cloud / mobile-surveillance doctrine.

However, this repository does not claim:

* APT42 executed the observed activity
* APT42 targeted the devices
* APT42 infrastructure was found
* APT42 malware was found
* APT42 phishing infrastructure was found
* APT42 attribution is established

The similarity is doctrinal, not attributional.

APT42-style ACMS is used only as:

> An account / cloud / mobile-surveillance comparison reference.

---

## Relationship to APT32 / OceanLotus

APT32 / OceanLotus is referenced only as a historical and operational TTP comparison point.

APT32-style comparison may be useful for examining:

* older operational doctrine
* long-term low-noise operation
* legitimate-service abuse
* trace suppression
* staged operational refinement
* residual seam failures
* possible old-doctrine leakage
* historical TTP transfer or adaptation

However, this repository does not claim:

* APT32 executed the observed activity
* OceanLotus executed the observed activity
* APT32 infrastructure was found
* APT32 malware was found
* APT32 C2 was found
* APT32 attribution is established

APT32-style comparison is secondary.

It is not required for the Shadow Cloud hypothesis to be reviewed.

The primary mechanism-level framing is:

> Mobile-native LOTL-like Apple platform-state anomaly.

---

## Relationship to LIMINAL-style telecom / proximity concepts

LIMINAL-style or telecom/proximity concepts are referenced only as comparison models.

They may be useful for thinking about:

* telecom state
* proximity-linked behavior
* SIM / baseband context
* network-edge or mobile-network interaction
* condition-based state changes

However, this repository does not claim:

* LIMINAL PANDA attribution
* telecom operator attribution
* confirmed baseband compromise
* confirmed rogue base station
* confirmed Evil Twin operation
* confirmed proximity-based attack infrastructure
* confirmed SIM compromise
* confirmed OTP interception

BSSID / RSSI / Wi-Fi / telecom artifacts are treated as:

> Timeline and condition anchors for review.

They are not treated as standalone attribution evidence.

---

## Relationship to commercial spyware models

Mercenary spyware, zero-click spyware, Pegasus-style, Predator-style, Intellexa-style, NSO-style, or similar commercial surveillance models may be referenced as comparison points only.

They may be relevant because mobile surveillance cases can involve:

* limited user-visible traces
* difficult artifact preservation
* platform-specific forensic methodology
* cross-layer device and account review
* evidence that may not appear as a simple malware sample

However, this repository does not claim:

* Pegasus deployment
* Predator deployment
* Intellexa deployment
* NSO involvement
* commercial spyware-family attribution
* confirmed zero-click exploit
* confirmed exploit chain

These models are comparison references only.

---

## Relationship to Apple

This repository does not claim that Apple performed the observed activity.

This repository does not claim that Apple intentionally caused the observed anomalies.

This repository does not claim that Apple is the attacker.

This repository does not claim that Apple engineering, Apple Support, Apple iCloud, ScreenTime, MDM, or any Apple service is malicious.

Apple systems are discussed because the observed artifacts appear within Apple ecosystem layers, including:

* Apple ID
* iCloud
* trusted devices
* ScreenTime
* ManagedSettings
* FileProvider
* backup services
* Manifest.db
* CommCenter
* Baseband-related logs
* analytics / sysdiagnose artifacts

The review question is whether the observed behavior is normal Apple behavior, abnormal Apple ecosystem state, user-side artifact, third-party tool artifact, or something requiring deeper forensic review.

For the backup layer, Apple backup state is treated as a review surface, not as proof of Apple-side causation.

---

## Relationship to iMazing

This repository does not claim that iMazing is malicious.

This repository does not claim that iMazing intentionally caused the observed anomalies.

This repository does not claim that iMazing is responsible for the entire dataset.

This repository does not claim that iMazing caused the Manifest.db / backup-ledger anomaly.

iMazing is discussed because multiple preserved backup generations and backup artifacts were reviewed through iMazing / iOS backup workflows.

The safer framing is:

```text
iMazing may be the acquisition surface.

Apple backup state may be the review surface.

Manifest.db may be the observable backup-ledger seam.
```

The relevant review questions include:

* whether Manifest.db behavior is normal for the reviewed backup state
* whether encrypted backup behavior explains the observed structures
* whether backup location, file lock, storage condition, local PC environment, security software, or Apple components could explain the anomalies
* whether iMazing success / visibility states align with raw backup artifact structure
* whether the backup ledger is preserving evidence normally
* whether the same iMazing version / PC / cable / workflow produces normal Manifest.db on clean control devices

If iMazing or ordinary iOS backup behavior explains the observed Manifest.db / backup-ledger behavior, that explanation should be documented and the hypothesis weakened accordingly.

---

## Relationship to Microsoft / Outlook / Office surfaces

This repository does not claim Microsoft attribution.

This repository does not claim that Outlook, OneDrive, Teams, Office, Excel, Word, PowerPoint, Microsoft 365, Microsoft Authenticator, Microsoft Edge, Intune, Company Portal, or any Microsoft service caused the Manifest.db anomaly.

This repository does not claim that Microsoft mobile apps directly modified Manifest.db, backup keybags, iOS backup services, or Apple backup state.

Microsoft-related mobile apps and services may be relevant only as possible future review surfaces because they can involve:

* account state
* cloud state
* calendar state
* meeting / schedule state
* document-provider behavior
* FileProvider behavior
* authentication tokens
* keychain items
* app protection / policy state
* document cache behavior
* notification state

User-observed Outlook / meeting / schedule-like traces are not used here as public proof.

Without preserved public artifact support in this package, those observations remain internal review anchors only.

The safe interpretation is:

> Microsoft mobile apps may be relevant as legitimate account-cloud-calendar-document surfaces for future review. They are not asserted as causes of the Manifest.db anomaly.

No Microsoft causation is asserted.

No Microsoft attribution is asserted.

No Outlook causation is asserted.

---

## Relationship to MDM

This repository does not claim confirmed MDM enrollment.

This repository does not claim classic visible MDM supervision.

This repository does not claim that configuration profiles were found proving management.

The issue is the apparent mismatch:

* visible management indicators appear absent or false
* MDMStatus:false appears in reviewed contexts
* management-adjacent daemons or restriction-adjacent services appear repeatedly
* ScreenTime / ManagedSettings / restriction-layer signals appear in related windows

The review question is:

> Can visible MDM absence normally coexist with the observed management-adjacent and restriction-adjacent artifact pattern?

If yes, the normal explanation should be documented.

If no, this may justify deeper review of policy-state or platform-state behavior.

---

## Relationship to ScreenTime / ManagedSettings

This repository does not claim that every ScreenTime or ManagedSettings artifact is abnormal.

ScreenTime, ManagedSettings, FamilyControls, Game Center restrictions, Content & Privacy signals, and Apple ID sign-out restrictions may have legitimate explanations, including:

* user configuration
* Family Sharing
* parental controls
* default iOS behavior
* app restrictions
* account state
* regional behavior
* device migration
* local settings

The review question is whether the observed pattern, timing, and cross-layer correlation can be explained by these normal mechanisms.

A normal explanation should address:

* which settings are defaults
* which settings require user action
* which states can be account-driven
* which states can arise without visible MDM or supervision
* whether Apple ID sign-out restriction behavior is consistent with ordinary ScreenTime / ManagedSettings behavior

---

## Relationship to usageClientId

This repository does not claim that usageClientId transitions alone prove compromise.

The usageClientId / usage-state transition issue is treated as a recurring structural signal.

Possible normal explanations include:

* device migration
* app reinstall
* account transition
* analytics reset
* iOS update
* backup restore
* user-side configuration
* Apple analytics behavior

The review question is whether repeated usage-state discontinuity across the broader timeline aligns with normal behavior or contributes to a larger trust-state discontinuity pattern.

---

## Relationship to Manifest.db / backup ledger

This repository does not claim that Manifest.db alone proves the entire case.

Manifest.db is treated as a high-value supporting artifact layer because it is central to iOS backup review and evidence preservation.

Observed concerns include repeated behavior described as:

* non-SQLite
* opaque
* high-entropy
* structurally abnormal
* inconsistent with ordinary readable Manifest.db expectations
* SQLite-level failure such as `file is not a database` in reviewed samples
* expected SQLite header absence in reviewed raw Manifest.db samples
* iMazing success / backend artifact reviewability mismatch as a review question

Potential normal explanations must be considered, including:

* encrypted backup behavior
* keybag / lock state
* backup corruption
* partial backup state
* storage failure
* local PC environment
* iMazing behavior
* Apple component behavior
* file lock
* security software interference
* low storage / disk pressure
* ordinary iOS / iMazing backup bug

The updated interpretation is:

> Manifest.db / backup-ledger abnormality may be a backup-ledger seam within a mobile LOTL-like Apple platform-state anomaly.

This does not mean:

* Manifest.db proves compromise
* Manifest.db proves attribution
* iMazing caused the anomaly
* Apple caused the anomaly
* Microsoft caused the anomaly
* Outlook caused the anomaly

If normal explanations reproduce the observed behavior across preserved backup generations, the hypothesis should be weakened.

If they do not, the backup ledger may require deeper forensic review.

---

## Relationship to CommCenter / Baseband / SIM / OTP context

This repository does not claim confirmed baseband compromise.

This repository does not claim confirmed telecom compromise.

This repository does not claim confirmed SIM attack.

This repository does not claim confirmed OTP interception.

CommCenter, Baseband, SIM, OTP, financial device-trust, BSSID, RSSI, and proximity-related artifacts are treated as:

* context signals
* timing anchors
* possible condition indicators
* review targets

The review question is whether these events are independent normal events or whether they align with account, restriction, backup, and evidence-preservation state changes.

---

## Relationship to evidence-preservation interference

This repository does not claim that every backup failure, screenshot issue, storage-pressure event, or recording difficulty is malicious.

Normal explanations may include:

* low storage
* app behavior
* OS resource pressure
* iCloud sync
* local backup-tool behavior
* local PC issues
* USB instability
* user-side error
* third-party software
* security software
* network conditions

The review question is whether evidence-preservation failures cluster around key review moments and cross-layer state changes more than expected under normal behavior.

Relevant observations include:

* backup failure
* storage pressure
* diskwrites
* CPU pressure
* screenshot difficulty
* screen-recording difficulty
* log preservation difficulty
* Manifest.db / RTCR abnormality
* repeated resource pressure during evidence preservation attempts

---

## Alpha / beta phase boundary

The alpha / beta framing is not a conclusion.

It is a timeline review model.

### Alpha-phase candidate

Approximate period:

```text
2025-07 to 2026-03
```

Observed pattern:

* distributed backup / Manifest.db / RTCR anomalies
* usageClientId / usage-state transitions
* Apple ID / iCloud trust discontinuities
* resource pressure
* log-preservation difficulty
* cross-device signals with less consolidated structure

### Beta / transitional control-layer candidate

Approximate period:

```text
2026-03 to 2026-05
```

Observed pattern:

* ScreenTime / ManagedSettings restriction-layer signals
* MDMStatus:false with management-adjacent daemon activity
* managedappdistributiond / dmd / ScreenTimeAgent clustering
* CommCenter / Baseband / SFA / CKKS / CloudServices context
* BSSID / RSSI proximity signals
* backup failure
* storage pressure
* screenshot / recording difficulty
* evidence-preservation interference

### Transition note

No deliberate configuration, iOS update, or backup-method change by the observer is known at the transition point.

The shift was identified retrospectively during timeline and log-cluster review.

This transition itself should be treated as a review question, not as proof.

A qualified reviewer may weaken or falsify this phase model by showing that the apparent shift was caused by:

* collection bias
* changed logging behavior
* changed analysis method
* changed device usage
* iOS updates
* backup-method changes
* dataset expansion
* observer-side configuration changes
* ordinary March 2026 iOS behavior

---

## Evidence boundary

Raw private logs are not publicly uploaded.

The public repository contains:

* written technical summaries
* artifact names
* referenced log titles
* SHA256 references
* evidence indexes
* machine-readable summaries
* reviewer-facing hypotheses
* public TTP comparison references
* scripts or reproducibility aids where safe

The public repository does not include:

* raw iOS logs
* raw sysdiagnose archives
* private screenshots
* private videos
* Apple ID values
* BSSID values where sensitive
* banking records
* OTP records
* private account identifiers
* third-party personal data

Raw artifacts may be shared only through an appropriate evidence-handling process, such as:

* NDA
* qualified forensic review
* paid scoping
* institutional review
* legal counsel involvement
* secure upload
* mutually agreed evidence-handling procedure

---

## Personal observation boundary

Some observations may include subjective or user-observed context.

These are not treated as standalone proof.

Subjective observations may be used only as:

* timestamp context
* reason for device interaction
* reason for evidence-preservation attempt
* timeline annotation
* future review anchor

They are not used alone to establish:

* attacker identity
* physical attack
* malware
* telecom compromise
* spyware deployment
* attribution
* vendor causation
* Microsoft causation
* Outlook causation

Any subjective observation must be supported by artifact-level review before it can contribute to technical conclusions.

---

## Scoring boundary

Any similarity score in this repository is a structural comparison score.

It is not an attribution score.

It is not an attack-probability score.

It does not establish actor identity.

It does not establish campaign identity.

It does not establish malware-family identity.

It only estimates how strongly the observed structure resembles a public operational doctrine, TTP pattern, or mechanism-level review model.

Examples:

* APT42-style alignment means similarity to account / cloud / mobile-surveillance doctrine.
* APT32-style alignment means similarity to historical operational doctrine, seam failures, or old-doctrine leakage.
* LOTL-like alignment means similarity to a mechanism where normal-looking platform states or legitimate functions become the anomaly surface.
* Backup-ledger seam alignment means the Manifest.db / backup-ledger abnormality is structurally consistent with a mobile LOTL-like platform-state review model.
* Mobile-native LOTL-like alignment means the broader structure is consistent with a mobile adaptation of LOTL logic where account, calendar, document, policy, backup, telecom, and evidence-preservation states become the review surface.

Scores should be treated as triage aids, not conclusions.

---

## Falsification requirements

This hypothesis should be weakened or rejected if qualified review shows that:

1. Manifest.db behavior is normal for the reviewed backup state.
2. SQLite errors are expected under ordinary encryption, keybag, lock, corruption, or tool conditions.
3. iMazing behavior or ordinary iOS backup behavior fully explains the backup-ledger state.
4. Local PC, USB, antivirus, file-lock, storage, or backup-location conditions reproduce the observed Manifest.db pattern.
5. MDMStatus:false plus management-adjacent daemon activity is normal for the reviewed iOS versions and contexts.
6. ScreenTime / ManagedSettings states are default, user-configured, or Family Sharing-related.
7. usageClientId transitions are normal account/device behavior.
8. CommCenter / Baseband / SIM / OTP events are independent normal events.
9. BSSID / RSSI proximity anchors are ordinary Wi-Fi roaming artifacts.
10. Evidence-preservation failures are explained by storage, app behavior, local PC environment, or ordinary backup-tool behavior.
11. Alpha / beta timeline shift is caused by dataset bias, collection changes, iOS updates, backup-method changes, or user-side configuration changes.
12. Cross-device recurrence is explained by normal shared Apple ecosystem behavior, shared account state, shared backup practice, or shared analysis bias.
13. Microsoft / Outlook / Office traces, if reviewed later, are fully explained by ordinary account, calendar, app, meeting, document-provider, or policy behavior and do not correlate with the broader structure.
14. The apparent mobile-native LOTL-like pattern disappears after normal controls are applied.

If normal explanations reproduce the observed structure, the Shadow Cloud hypothesis should be reduced, revised, or rejected.

---

## What would strengthen the hypothesis

The hypothesis would be strengthened only by qualified review showing that:

* normal iOS / iCloud / iMazing explanations do not reproduce the observed structure
* Manifest.db / backup-ledger behavior is abnormal after artifact-level review
* encrypted versus unencrypted backup behavior does not fully explain the Manifest.db pattern
* iMazing success / backend artifact reviewability mismatch is confirmed under proper review
* clean control devices under comparable acquisition conditions do not reproduce the same Manifest.db behavior
* ScreenTime / ManagedSettings behavior cannot be explained by default settings, user configuration, or Family Sharing
* MDMStatus:false does not normally coexist with the observed management-adjacent daemon pattern
* usageClientId transitions are not normal under the reviewed conditions
* CommCenter / Baseband / SIM / OTP context aligns with trust-state or restriction-state changes
* Outlook / Microsoft traces exist in preserved artifacts during key windows and cannot be explained as ordinary residue
* account-cloud-calendar-document state correlates with backup, restriction, telecom, or evidence-preservation anomalies
* evidence-preservation failures cluster around critical review moments beyond expected normal behavior
* cross-device recurrence survives control comparison
* raw artifact review supports the public summary structure

Even then, this would not automatically prove attribution.

It would only support deeper technical investigation.

---

## What this document claims

This document claims only the following:

* The repository is non-attribution.
* Shadow Cloud is a working hypothesis.
* The updated preferred framing is LOTL-like Apple platform-state anomaly.
* The current maximum mechanism-level hypothesis is mobile-native LOTL-like Apple platform-state anomaly.
* The backup-layer branch is a backup-ledger seam in a mobile LOTL-like platform-state anomaly.
* iMazing is treated as an acquisition surface, not an asserted cause.
* Apple backup state is treated as a review surface, not proof of Apple causation.
* Microsoft / Outlook / Office surfaces are future review surfaces only, not public evidence of causation.
* APT42, APT32, LIMINAL-style, mercenary spyware, Microsoft app surfaces, and LOTL references are comparison points or review surfaces only.
* The review target is the cross-layer Apple ecosystem seam structure.
* The hypothesis is falsifiable.
* Normal explanations are welcome and should be documented.
* Raw private artifacts are not public.

---

## What this document does not claim

This document does not claim:

* confirmed malware
* confirmed payload
* confirmed C2
* confirmed exploit chain
* confirmed spyware
* confirmed MDM enrollment
* APT42 attribution
* APT32 attribution
* LIMINAL PANDA attribution
* state attribution
* Apple attribution
* iMazing attribution
* Microsoft attribution
* Outlook causation
* telecom-provider attribution
* attacker identity
* criminal attribution
* that Manifest.db alone proves the case
* that ScreenTime artifacts alone prove the case
* that subjective observations alone prove the case
* that BSSID / RSSI alone proves proximity-based attack
* that Outlook / Microsoft app traces caused the backup anomaly
* that LOTL-like framing identifies an actor
* that mobile-native LOTL-like framing identifies an actor

---

## Final limitation statement

The Shadow Cloud model is a review framework.

It is not a conclusion.

It is not an accusation.

It is not an attribution claim.

It is not a malware-family claim.

It is an attempt to organize long-term, cross-device Apple ecosystem artifacts into a falsifiable review structure.

The preferred reviewer question is:

> Can normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior explain the observed cross-layer structure?

For the backup layer, the narrower question is:

> Can normal Apple / iOS / iMazing backup behavior explain repeated Manifest.db / backup-ledger abnormality across preserved backup generations, especially when aligned with broader trust-state, restriction-state, daemon-layer, telecom, and evidence-preservation anomalies?

If yes, document the normal explanation.

If no, the case may represent a forensic blind spot in how iOS platform-state, backup-ledger behavior, restriction state, account-cloud-calendar-document state, telecom context, and evidence preservation are currently reviewed.
