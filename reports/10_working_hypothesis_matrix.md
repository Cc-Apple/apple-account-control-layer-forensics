# Working Hypothesis Matrix

## Purpose

This file defines a reviewer-facing hypothesis matrix for the Shadow Cloud working model.

These are not attribution claims.

They are not claims that any actor, state, government, company, vendor, telecom provider, backup tool vendor, Microsoft product, Apple product, iMazing workflow, or known spyware family executed the observed activity.

They are structured working hypotheses intended to make the Shadow Cloud model testable by qualified DFIR, CTI, mobile forensic, platform-security, OS-security, backup-forensic, and evidence-preservation reviewers.

The purpose is to separate:

* observed structural signals
* possible interpretations
* validation paths
* falsification paths
* mechanism-level TTP framing
* mobile-native LOTL-like framing
* backup-ledger seam review
* Microsoft / Outlook review-surface boundaries

from direct attribution or speculation.

---

## Core model being tested

Shadow Cloud is treated as a working hypothesis for a possible Apple account / iCloud / backup / restriction-layer / telecom / proximity / evidence-preservation anomaly.

The model does not assume that a classic malware payload must be visible.

Instead, the strongest traces may appear at the seams between legitimate Apple services, legitimate mobile app surfaces, and abnormal platform-state behavior.

The current strongest mechanism-level framing is:

> Shadow Cloud may represent a mobile-native LOTL-like Apple platform-state anomaly.

This means the review target is not a named actor.

The review target is whether legitimate mobile platform state behaves normally across account, cloud, calendar, document, policy, backup, telecom, proximity, and evidence-preservation layers.

The short formula is:

> Not living off tools.
> Living off Apple platform state.

For the backup layer:

> Living off Apple backup state.

The main seam areas are:

* Apple ID state
* iCloud / trusted-device behavior
* account-cloud-calendar-document state
* usageClientId / usage-state transitions
* ScreenTime / restriction-layer behavior
* ManagedSettings / FamilyControls traces
* visible management state versus management-adjacent daemon activity
* iMazing backup behavior
* Manifest.db / backup-ledger behavior
* RTCR / reporting generation behavior
* CommCenter / Baseband / SIM / OTP trust behavior
* BSSID / RSSI / proximity-related signals
* resource pressure and evidence-preservation interference

---

## Updated hypothesis stack

The recommended hypothesis stack is:

```text
Shadow Cloud
= working hypothesis name

Mobile-native LOTL-like Apple platform-state anomaly
= maximum current mechanism-level hypothesis

LOTL-like Apple platform-state anomaly
= mechanism-level framing

Backup-ledger seam in mobile LOTL-like platform-state anomaly
= focused backup-layer branch

Outlook / Microsoft account-cloud-calendar-document surface
= possible entry / state surface candidate for future review

Account / cloud / mobile-surveillance comparison
= public comparison reference

Historical TTP comparison
= secondary operational-history comparison

Telecom / proximity comparison
= tertiary condition / context comparison

Attribution
= not asserted
```

This matrix should be read as mechanism-centered, not actor-centered.

---

## Maximum working hypothesis

### Name

Mobile-native LOTL-like Apple platform-state anomaly.

### Meaning

Traditional Living-off-the-Land activity is usually discussed in PC, enterprise, endpoint, cloud, and administrative environments.

The maximum Shadow Cloud hypothesis asks whether the same general logic can have a mobile-native form.

The mobile-native form does not need to look like:

```text
PowerShell on iPhone.
```

The mobile-native form may look like:

```text
Normal-looking mobile platform state becoming the control and observation surface.
```

Relevant surfaces may include:

* legitimate mobile apps
* legitimate account state
* legitimate cloud identity
* legitimate calendar / meeting state
* legitimate document-provider state
* legitimate token / OAuth state
* legitimate policy / restriction state
* legitimate backup state
* legitimate telecom / SIM / OTP state
* legitimate evidence-preservation behavior

### Current structural fit

```text
Mobile-native LOTL-like Apple platform-state anomaly:
88 / 100
```

This is not an attribution score.

This is not an attack-probability score.

It is a structural-fit score.

It means the maximum hypothesis currently explains the observed cross-layer structure better than isolated normal explanations, while still requiring qualified artifact-level review.

### Why this is the current maximum hypothesis

This hypothesis explains why the strongest traces may appear not in:

* malware payloads
* simple implants
* C2 domains
* exploit chains
* configuration profiles
* visible management enrollment
* known spyware-family signatures

but instead in:

* Apple ID trust state
* iCloud trust state
* ScreenTime / ManagedSettings state
* MDMStatus:false with management-adjacent daemon repetition
* usageClientId / usage-state transitions
* CommCenter / Baseband / SIM / OTP context
* BSSID / RSSI proximity context
* backup state
* Manifest.db / backup-ledger behavior
* RTCR / RTCReporting
* storage pressure
* screenshot / recording difficulty
* evidence-preservation degradation
* possible account-cloud-calendar-document surfaces

### Public boundary

This maximum hypothesis does not assert:

* malware
* payload
* C2
* exploit chain
* confirmed MDM enrollment
* Apple attribution
* iMazing attribution
* Microsoft attribution
* Outlook causation
* state attribution
* government attribution
* actor attribution
* spyware-family attribution
* telecom compromise
* baseband compromise
* OTP interception
* attacker identity

---

## Outlook / Microsoft surface boundary

Outlook / Microsoft mobile surfaces are included only as possible future review surfaces.

They are not public proof.

They are not treated as causes.

They are not treated as the source of the Manifest.db anomaly.

Relevant future review surfaces include:

* Outlook
* Exchange
* Microsoft 365
* Teams
* OneDrive
* SharePoint
* Office
* Excel
* Word
* PowerPoint
* Microsoft Authenticator
* Microsoft Edge
* Company Portal
* Intune / MAM
* OAuth
* access tokens
* refresh tokens
* Microsoft Graph
* calendar invites
* meeting objects
* ICS files
* attachments
* document providers
* FileProvider behavior
* app protection policy
* selective wipe / managed app state

The current interpretation is:

```text
Outlook / Microsoft surfaces may be relevant as account-cloud-calendar-document-policy surfaces for future review.

They are not asserted as causes.
```

Current internal-review structural fit:

```text
Outlook / Microsoft entry-surface hypothesis:
75 / 100
```

This score means the surface is technically plausible and relevant to mobile-native LOTL-like review, not that Microsoft causation is established.

---

## Manifest.db as byproduct, not root cause

The Manifest.db issue is not treated as the root cause.

The stronger interpretation is that it may be a byproduct or observable evidence-preservation seam.

The proposed sequence is:

```text
mobile-native LOTL-like account / cloud / calendar / document / policy state
↓
Apple trust state / restriction state / backup state / keybag-encryption state / evidence-preservation state
↓
iMazing / iOS backup acquisition
↓
Manifest.db / backup-ledger abnormality becomes observable
```

This means Manifest.db is not the first step.

Manifest.db is where abnormal platform state may become visible during preservation.

The backup-layer formulation is:

> Living off Apple backup state.

Current structural fit:

```text
Manifest.db as byproduct / backup-ledger seam:
82 / 100
```

---

# Hypothesis 1: Policy-as-Persistence

## Meaning

The persistence mechanism may not be a classic malware implant.

Instead, persistence may be expressed through policy state, restriction state, Apple ID trust state, ScreenTime state, ManagedSettings behavior, or management-adjacent daemon activity.

## Observed indicator categories

* ScreenTime restrictions appearing without clear user configuration
* Apple ID sign-out restriction behavior
* ManagedSettings / FamilyControls traces
* management-adjacent daemon activity
* MDMStatus:false or supervised:false while restriction-like behavior appears
* repeated daemon failure or policy-state anomalies

## Why it matters

If policy state is being used as persistence, then ordinary malware triage may miss the control mechanism.

The relevant question becomes:

> What state is being preserved across devices, accounts, backups, or restore generations?

not only:

> What binary is running?

## What would support this hypothesis

* repeated restriction behavior across multiple devices
* restriction behavior surviving restore, migration, or Apple ID lineage changes
* mismatch between visible management state and effective restriction behavior
* correlation between ScreenTime / ManagedSettings / daemon activity and user-observed control symptoms
* restriction-like behavior clustering with account / cloud / backup / telecom state changes

## What would weaken or falsify it

* confirmed local user configuration for all restriction behavior
* reproducible normal Apple behavior explaining the same pattern
* no cross-device or cross-generation continuity
* vendor-confirmed benign explanation for all relevant policy-state transitions
* clean control devices reproducing the same restriction pattern under normal settings

## Current confidence

Medium to high as a structural hypothesis.

Not proven.

---

# Hypothesis 2: Backup-layer Anti-Forensics

## Meaning

Backup-layer artifacts may not be the primary attack mechanism.

They may instead represent an anti-forensic layer affecting evidence preservation, restoration integrity, reviewability, or third-party verification.

## Observed indicator categories

* Manifest.db abnormality
* non-SQLite or opaque Manifest behavior
* SQLite-level failure such as `file is not a database` in reviewed samples
* expected SQLite header absence in reviewed raw Manifest.db samples
* backup generation inconsistency
* RTCR generation anomalies
* encrypted versus unencrypted backup differences
* iMazing success display versus abnormal backend artifact state
* evidence package preservation difficulty

## Why it matters

If the backup ledger becomes opaque, abnormal, damaged, or inconsistent, then later forensic review becomes weaker even if the user attempted preservation.

The relevant question becomes:

> Is the backup layer preserving evidence, or becoming part of the anomaly?

## What would support this hypothesis

* repeated Manifest.db structural abnormality across backup generations
* different behavior between encrypted and unencrypted backups
* reproducible mismatch between backup success status and artifact validity
* abnormal RTCR / Manifest / Status / Info plist relationships
* comparison devices showing normal backup ledgers under similar conditions
* repeated SQLite-level failures that cannot be explained by normal backup encryption or keybag state

## What would weaken or falsify it

* confirmed iMazing or Apple backup behavior fully explaining the Manifest pattern
* identical Manifest behavior reproduced on clean control devices
* normal SQLite access after proper decryption and tool handling
* no meaningful difference between affected and control backups
* all SQLite failures explained by ordinary encryption, lock state, corruption, partial backup, local PC, or tool conditions

## Current confidence

Medium to high as a Shadow Cloud-specific differential hypothesis.

Not proven.

---

# Hypothesis 3: Backup-ledger Seam in Mobile LOTL-like Platform-State Anomaly

## Meaning

The Manifest.db / backup-ledger issue may represent a focused backup-layer seam within the broader mobile-native LOTL-like Apple platform-state anomaly model.

This hypothesis does not treat iMazing as the cause.

It treats iMazing as the acquisition surface through which abnormal Apple backup state may become observable.

The suspected review surface is not the backup tool alone.

The suspected review surface is the interaction between:

* Apple backup state
* backup encryption state
* keybag state
* pairing / trust state
* device lock state
* iOS backup service behavior
* Manifest.db / Manifest.plist / Status.plist / Info.plist
* RTCR / RTCReporting
* iMazing / iOS backup acquisition workflow
* storage pressure
* evidence-preservation behavior

## Observed indicator categories

* Manifest.db not normally openable as SQLite
* SQLite-level failure such as `file is not a database`
* expected SQLite header absent in reviewed raw samples
* repeated non-SQLite / opaque / high-entropy Manifest.db behavior
* multiple preserved backup generations
* iMazing success / backend artifact reviewability mismatch
* encrypted versus unencrypted backup differences
* readable mini1 non-encrypted subset showing normal SQLite integrity
* RTCR / Status.plist / Manifest.plist correlation questions
* relationship to evidence-preservation difficulty

## Why it matters

Traditional forensic review often assumes that once a backup acquisition appears successful, the backup can be treated as a stable evidence container.

This hypothesis asks whether the backup ledger itself may become part of the anomaly surface.

The relevant question becomes:

> Can normal Apple / iOS / iMazing backup behavior explain repeated Manifest.db / backup-ledger abnormality across preserved backup generations?

not only:

> Did iMazing complete a backup?

## What would support this hypothesis

* Manifest.db repeatedly not valid SQLite after proper handling
* expected SQLite header absent in raw reviewed samples
* same issue appearing across multiple preserved backup generations
* iMazing success state not matching backend artifact reviewability
* Status.plist / Manifest.plist / RTCR indicating completed or meaningful backup states despite Manifest.db abnormality
* control devices under the same acquisition environment producing normal Manifest.db
* issue correlating with ScreenTime / ManagedSettings / MDMStatus:false / daemon repetition / CommCenter / evidence-preservation events
* encrypted versus unencrypted backup comparisons not fully explaining the issue
* local PC / USB / antivirus / storage explanations failing to reproduce the pattern

## What would weaken or falsify it

* Manifest.db opens normally as SQLite after proper decryption and handling
* observed error is expected under ordinary encrypted backup conditions
* clean control devices reproduce the same Manifest.db behavior under the same conditions
* Status.plist clearly indicates partial or failed backup state
* iMazing documentation or reproducible testing fully explains the observed state
* Windows / USB / antivirus / file-lock conditions reproduce the same artifact pattern
* low storage alone reproduces the observed backup-ledger behavior
* issue does not correlate with broader trust-state, restriction-state, daemon-layer, telecom, or evidence-preservation pattern

## Current confidence

High as a backup-layer review hypothesis.

Not proven.

Conservative structural fit:

```text
Backup-ledger seam in mobile LOTL-like platform-state anomaly:
82 / 100
```

---

# Hypothesis 4: Trust-Graph Poisoning

## Meaning

The center of gravity may not be a single affected device.

The anomaly may involve distortion of a broader trust graph, including Apple ID lineage, trusted devices, backup lineage, usage state, SIM / OTP state, and financial device trust.

## Observed indicator categories

* Apple ID lineage transitions
* device identity discontinuity
* usageClientId switching
* trusted-device behavior anomalies
* SIM / CommCenter / OTP-related anomalies
* financial applications requesting re-authentication
* bank-side “device changed?” type indicators
* backup lineage inconsistency
* account / cloud / device trust-state discontinuity

## Why it matters

If the trust graph is affected, wiping or replacing one device may not eliminate the anomaly.

The relevant question becomes:

> Is the trusted relationship itself being distorted?

not only:

> Is this phone compromised?

## What would support this hypothesis

* similar trust-state anomalies across multiple Apple devices
* continuity after device replacement or Apple ID migration
* correlation between device trust anomalies and financial re-authentication events
* repeated identity discontinuity in logs
* difference between owner devices and clean comparison devices
* usageClientId discontinuity aligning with backup, restriction, telecom, or account-cloud state changes

## What would weaken or falsify it

* every event explained by normal account migration or device replacement
* no cross-device continuity
* no relation between trust-state anomalies and authentication events
* clean vendor-side confirmation that all trusted-device states are normal
* usageClientId transitions fully explained by normal analytics, restore, migration, or app behavior

## Current confidence

High as an explanatory hypothesis.

Not proven.

---

# Hypothesis 5: Proximity-triggered State Switch

## Meaning

Wi-Fi / BSSID / RSSI / nearby-device / radio-environment signals may not be the main mechanism.

They may function as proximity or condition triggers used to change state when the target is physically present in a specific environment.

## Observed indicator categories

* BSSID / RSSI / channel anchors
* WiFiLQMMetrics anomalies
* locationd correlation
* CommCenter / Baseband correlation
* movement or arrival-time correlation
* device behavior changes around physical proximity events
* repeated proximity-linked daemon activity
* telecom / account / restriction state changes near radio-environment anchors

## Why it matters

The proximity layer may act as a trigger, selector, or environmental condition.

The relevant question becomes:

> Did the device state change when the target entered a specific radio environment?

not only:

> Was a rogue AP used for traffic interception?

## What would support this hypothesis

* repeated state changes near specific BSSID / RSSI patterns
* time correlation between human proximity events and daemon / restriction / telecom events
* similar behavior after travel, arrival, or network environment change
* control devices showing no equivalent state change under similar conditions
* proximity anchors aligning with account / backup / restriction / evidence-preservation anomalies

## What would weaken or falsify it

* BSSID / RSSI patterns fully explained by ordinary Wi-Fi roaming
* no repeatable time correlation
* no link between proximity signals and control-layer symptoms
* clean network environment reproducing the same results
* telecom / proximity artifacts fully explained as independent normal events

## Current confidence

Medium.

Useful as a trigger hypothesis, not as a standalone attribution claim.

---

# Hypothesis 6: Deniability-first Design

## Meaning

The observed pattern may be designed or may naturally appear to look like ordinary iOS bugs, storage pressure, iCloud sync problems, Wi-Fi quality problems, user error, or backup-tool failure.

The relevant review question is whether plausible normal explanations explain the full cross-layer structure or only isolated pieces.

## Observed indicator categories

* minor daemon failures across multiple layers
* diskwrites / CPU resource pressure
* storage pressure during evidence-relevant moments
* screenshot or screen-recording difficulty during critical moments
* backup failure or partial backup behavior
* sync delay / deletion / log preservation anomalies
* normal-looking error categories masking cross-layer correlation
* visible management absence while management-adjacent activity repeats

## Why it matters

A deniability-first structure would not produce one obvious malware indicator.

It would produce many individually dismissible symptoms that become meaningful only when aligned across time, device, and layer.

## What would support this hypothesis

* repeated clustering of individually minor errors around evidence-relevant events
* cross-device recurrence of similar benign-looking failure modes
* strong time correlation between user action and evidence-preservation degradation
* comparison devices lacking the same clustered pattern
* normal-looking Apple platform states aligning in abnormal cross-layer sequences

## What would weaken or falsify it

* ordinary iOS behavior explains all clusters independently
* no timing relationship to evidence-relevant activity
* same pattern appears on clean control devices
* storage and backup problems are fully explained by local configuration or hardware failure
* all daemon failures are isolated, expected, and unrelated to account / restriction / backup / telecom states

## Current confidence

Medium to high as a design hypothesis.

Not proven.

---

# Hypothesis 7: Alpha / Beta Cohort Testing

## Meaning

The observed long-term, multi-device pattern may represent staged testing, phased refinement, or transition behavior rather than a finished mature operation.

The strongest anomalies may be exposed at the seams because the model is incomplete or still being tuned.

## Observed indicator categories

* phase-shift-like density increases
* March 2026 beta-phase candidate behavior
* different anomaly types across owner devices and comparison devices
* device-specific failure modes
* repeated but imperfect cross-layer coupling
* stronger contradictions during transition windows
* transition from distributed backup / trust / usage signals to more consolidated restriction / daemon / telecom / preservation clustering

## Why it matters

If this is a phased model, then the “flaws” are not noise.

They are the most important evidence.

The relevant question becomes:

> Where does the control model fail to hide itself?

## What would support this hypothesis

* clear phase boundaries
* increasing sophistication over time
* decreasing visible contradiction across later periods
* different devices showing different test roles
* comparison devices acting as negative or partial controls
* alpha-to-beta shift remaining after correcting for collection bias, device changes, iOS updates, and backup-method changes

## What would weaken or falsify it

* no chronological progression
* no repeatable phase windows
* no difference between affected and comparison devices
* all anomalies explained by unrelated local failures
* apparent phase shift caused by observer-side collection changes, dataset expansion, iOS updates, or changed analysis method

## Current confidence

Medium.

Important for timeline analysis, not a direct proof of actor identity.

---

# Hypothesis 8: Evidence-Suppression Objective

## Meaning

The objective may include not only surveillance or access, but also suppression of the user’s ability to preserve, explain, export, or validate evidence.

This would make evidence preservation itself part of the contested surface.

## Observed indicator categories

* screenshot failure
* screen recording failure
* storage pressure during critical events
* backup inconsistency
* Manifest / RTCR abnormality
* SFA or related artifact preservation difficulty
* deletion / logd / resource-pressure patterns
* inability to capture key moments despite user effort
* backend artifact abnormality despite apparent user-side preservation attempt

## Why it matters

If evidence suppression is an objective, then absence of evidence becomes less reassuring.

The relevant question becomes:

> Did the system behave normally when the user attempted to preserve evidence?

## What would support this hypothesis

* repeated preservation failure during high-value events
* correlation between user evidence actions and resource / daemon / backup anomalies
* cross-device or cross-period recurrence
* successful preservation on control devices under similar conditions
* failure modes aligning with the most important event windows
* backup / Manifest / RTCR anomalies aligning with preservation attempts

## What would weaken or falsify it

* preservation failures fully explained by storage exhaustion, user error, or tool limitations
* no timing relationship to important events
* same failures reproduced on clean devices
* no link between preservation failure and control-layer anomalies
* all preservation failures explained by local PC, iMazing, USB, storage, network, or app conditions

## Current confidence

High as a reviewer-facing hypothesis.

Not proven.

---

# Hypothesis 9: LOTL-like Platform-State Anomaly

## Meaning

The observed structure may not depend on a visible malicious tool, obvious payload, classic C2 infrastructure, configuration profile, or visible MDM enrollment.

Instead, the anomaly may appear as normal-looking Apple platform state across account, iCloud, policy, backup, telecom, proximity, and evidence-preservation layers.

This is a mechanism-level hypothesis.

It does not identify an actor.

## Observed indicator categories

* Apple ID trust state
* iCloud trust state
* trusted-device graph
* usageClientId / usage-state transitions
* ScreenTime
* ManagedSettings
* FamilyControls
* MDMStatus:false with management-adjacent daemon activity
* Manifest.db / backup ledger
* RTCR / RTCReporting
* CommCenter
* Baseband
* SIM / OTP / financial device-trust context
* BSSID / RSSI proximity anchors
* storage pressure
* backup failure
* screenshot / recording difficulty
* evidence-preservation interference

## Why it matters

Traditional Living-off-the-Land activity is usually discussed in enterprise environments, where attackers use legitimate tools, valid accounts, cloud consoles, admin utilities, or normal-looking processes.

The Shadow Cloud hypothesis appears conceptually similar, but the suspected surface is different.

The suspected surface is Apple platform state itself.

Traditional LOTL can be summarized as:

> Living off existing tools and accounts.

Shadow Cloud can be summarized as:

> Living off Apple platform state.

The relevant question becomes:

> Is this normal Apple platform state, or a LOTL-like anomaly surface where platform state itself becomes the control surface?

## What would support this hypothesis

* strongest traces appearing in Apple ecosystem seams rather than payloads
* repeated cross-layer clustering across account / iCloud / restriction / backup / telecom / preservation layers
* normal-looking artifacts remaining unexplained after artifact-level review
* MDMStatus:false coexisting with management-adjacent daemon repetition in a pattern not explained by normal behavior
* Manifest.db / backup-ledger behavior not reproducible as normal backup behavior
* usageClientId transitions not fully explained by normal migration, analytics, restore, or app behavior
* evidence-preservation failures clustering around key review windows
* affected devices showing recurring structure not reproduced on comparison devices

## What would weaken or falsify it

* all platform-state signals explained by normal Apple / iOS / iCloud / iMazing behavior
* cross-layer clustering disappears after normal controls are applied
* Manifest.db behavior is reproduced on clean backups
* MDMStatus:false plus daemon activity is normal and documented for the observed contexts
* ScreenTime / ManagedSettings behavior is fully explained by user settings, defaults, or Family Sharing
* usageClientId transitions are fully explained by normal device/account behavior
* CommCenter / Baseband / SIM / OTP events are independent normal events
* evidence-preservation failures are fully explained by storage, app behavior, local PC environment, or ordinary backup-tool behavior

## Current confidence

High as a mechanism-level framing hypothesis.

Not proven.

Estimated structural fit:

```text
LOTL-like Apple platform-state anomaly:
86 / 100
```

---

# Hypothesis 10: Mobile-native LOTL-like Apple Platform-State Anomaly

## Meaning

This is the current maximum working hypothesis.

It proposes that traditional PC / enterprise LOTL logic may have a mobile-native equivalent.

Instead of relying on visible PC-side tools, the mobile-native version may operate through legitimate mobile app, account, cloud, calendar, document, policy, backup, telecom, and evidence-preservation states.

This is not a claim that Outlook, Microsoft, Apple, or iMazing caused the observed behavior.

It is a review model.

## Observed indicator categories

* Outlook / Microsoft account-cloud-calendar-document surfaces as future review surfaces
* Apple ID trust state
* iCloud trust state
* ScreenTime / ManagedSettings state
* MDMStatus:false with management-adjacent activity
* Manifest.db / backup-ledger abnormality
* usageClientId / usage-state transitions
* CommCenter / Baseband / SIM / OTP context
* BSSID / RSSI proximity anchors
* storage pressure and backup / log preservation failures
* screenshot / recording difficulty
* evidence-preservation difficulty
* alpha / beta phase-shift behavior

## Why it matters

This hypothesis gives a cleaner explanation than actor-centered comparison.

It explains why:

* account / cloud / mobile-surveillance comparison is useful but not sufficient
* historical TTP comparison is secondary
* telecom / proximity comparison is tertiary
* Manifest.db is better treated as a byproduct / backup-ledger seam
* Outlook / Microsoft surfaces are better treated as possible entry or state surfaces
* payload / C2 absence is not fatal to the mechanism-level review
* cross-layer platform state is the main review surface

## What would support this hypothesis

* preserved Outlook / Microsoft traces during key windows
* Outlook / calendar / meeting / document-provider traces correlating with account / cloud / backup / evidence-preservation anomalies
* Microsoft-related token / account / document state appearing unexpectedly on affected devices
* normal Outlook / Calendar / Microsoft app behavior failing to explain the observed traces
* Manifest.db remaining abnormal after correct decryption and handling
* clean control devices under comparable conditions not reproducing the same Manifest.db behavior
* ScreenTime / ManagedSettings / MDMStatus:false patterns not explained by normal settings
* usageClientId transitions not explained by normal migration / restore / analytics behavior
* CommCenter / Baseband / SIM / OTP context aligning with account or trust-state changes
* evidence-preservation failures clustering around important review windows
* alpha / beta phase shift remaining after correcting for collection bias and method changes

## What would weaken or falsify it

* Outlook / Microsoft traces are normal residue, old login remnants, or ordinary calendar artifacts
* Microsoft-related observations do not correlate with any other anomaly layer
* Manifest.db behavior is fully explained by encrypted backup / keybag / iMazing / partial backup behavior
* ScreenTime / ManagedSettings behavior is fully explained by user settings, defaults, or Family Sharing
* MDMStatus:false plus daemon repetition is normal for the reviewed contexts
* usageClientId transitions are normal
* CommCenter / Baseband / SIM / OTP events are independent normal events
* BSSID / RSSI anchors are ordinary Wi-Fi roaming artifacts
* evidence-preservation failures are explained by storage, app behavior, PC conditions, or normal backup-tool behavior
* cross-device recurrence disappears after normal controls are applied
* alpha / beta phase shift is caused by dataset expansion, collection changes, or observer-side changes

## Current confidence

Current strongest mechanism-level hypothesis.

Not proven.

Estimated structural fit:

```text
Mobile-native LOTL-like Apple platform-state anomaly:
88 / 100
```

---

## Summary table

| Hypothesis                                                    | Main layer                                                                                  | Primary question                                                               | Current role               |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------- |
| Policy-as-Persistence                                         | ScreenTime / ManagedSettings / policy state                                                 | Is policy state acting as persistence?                                         | Core                       |
| Backup-layer Anti-Forensics                                   | Manifest / backup / RTCR                                                                    | Is the backup layer part of evidence degradation?                              | Core                       |
| Backup-ledger Seam in Mobile LOTL-like Platform-State Anomaly | Manifest.db / backup ledger / iMazing acquisition / Apple backup state                      | Is the backup ledger itself an anomaly surface?                                | Core backup branch         |
| Trust-Graph Poisoning                                         | Apple ID / trusted devices / financial trust                                                | Is the trust graph distorted?                                                  | Core                       |
| Proximity-triggered State Switch                              | BSSID / RSSI / telecom / location                                                           | Is proximity a trigger condition?                                              | Supporting                 |
| Deniability-first Design                                      | OS error surface / resource pressure                                                        | Are failures designed or clustered in a way that appears benign?               | Core-supporting            |
| Alpha / Beta Cohort Testing                                   | timeline / multi-device comparison                                                          | Are contradictions exposed during staged refinement?                           | Supporting                 |
| Evidence-Suppression Objective                                | preservation / capture / backup                                                             | Is evidence preservation itself being interfered with?                         | Core                       |
| LOTL-like Platform-State Anomaly                              | Apple platform state / trust state / seams                                                  | Is platform state itself the anomaly surface?                                  | Mechanism-level core       |
| Mobile-native LOTL-like Apple Platform-State Anomaly          | mobile app / account / calendar / document / policy / backup / telecom / preservation state | Does PC/enterprise LOTL logic have a mobile-native equivalent in this dataset? | Maximum working hypothesis |

---

## Reviewer guidance

Reviewers should not treat these hypotheses as conclusions.

They should be used as a validation framework.

A useful review should attempt to answer:

1. Which hypotheses are supported by the preserved artifacts?
2. Which hypotheses are contradicted by the artifacts?
3. Which hypotheses can be explained by normal Apple / iOS / iCloud / iMazing behavior?
4. Which hypotheses can be explained by normal Microsoft app residue, calendar behavior, account behavior, or document-provider behavior?
5. Which hypotheses require Apple-side telemetry, Microsoft-side telemetry, server-side logs, vendor-side backup behavior, or platform-level review?
6. Which artifacts are necessary for falsification?
7. Which normal explanations can be reproduced?
8. Which cross-layer correlations remain after normal explanations are applied?
9. Whether the remaining pattern is better framed as mobile-native LOTL-like Apple platform-state anomaly rather than an actor-centered claim.
10. Whether the Manifest.db / backup-ledger issue can be fully reproduced as ordinary encrypted backup, keybag, tool, partial-backup, local PC, or storage behavior.
11. Whether Outlook / Microsoft account-cloud-calendar-document surfaces are relevant, ordinary residue, or unrelated.
12. Whether the backup-ledger seam should be treated as a possible forensic blind spot.

The preferred outcome is not confirmation.

The preferred outcome is a reproducible explanation that supports, weakens, or falsifies each hypothesis.

---

## Non-attribution boundary

This hypothesis matrix does not assert:

* malware attribution
* actor attribution
* state attribution
* government attribution
* Apple attribution
* iMazing attribution
* Microsoft attribution
* Outlook causation
* telecom-provider attribution
* classic MDM enrollment
* known spyware family deployment
* confirmed C2
* confirmed payload
* confirmed exploit chain
* confirmed Evil Twin / rogue AP use
* confirmed baseband compromise
* confirmed SIM compromise
* confirmed OTP interception

Public TTP references, historical TTP comparison, telecom / proximity concepts, commercial spyware models, Microsoft app surfaces, and LOTL references are comparison points or possible review surfaces only.

The central question is not:

> Which actor did this?

The central question is:

> Can normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior explain the observed long-term, cross-device clustering of trust state, restriction state, account-calendar-document state, backup state, telecom state, proximity context, and evidence-preservation behavior?

For the backup layer, the narrower question is:

> Can normal Apple / iOS / iMazing backup behavior explain repeated Manifest.db / backup-ledger abnormality across preserved backup generations, especially when aligned with broader trust-state, restriction-state, daemon-layer, telecom, and evidence-preservation anomalies?

If yes, the hypotheses should be weakened.

If no, the case may represent a forensic blind spot in how iOS platform-state, backup-ledger behavior, restriction state, account-cloud-calendar-document state, telecom context, and evidence preservation are currently reviewed.

---

## Linked documents

* `README.md`
* `SUMMARY_ONE_PAGE.md`
* `machine_summary.yaml`
* `docs/mobile_lotl_maximum_hypothesis.md`
* `docs/ttp_framing_addendum_lotl_platform_state.md`
* `docs/backup_ledger_seam_mobile_lotl.md`
* `reports/00_manifest_db_anomaly_core_point.md`
* `reports/01_manifest_db_anomaly.md`
* `reports/06_public_ttp_mechanism_comparison.md`
* `reports/07_limitations_and_non_attribution.md`
* `reports/09_secondary_historical_ttp_comparison.md`
