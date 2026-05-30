# Working Hypothesis Matrix

## Purpose

This file defines a reviewer-facing hypothesis matrix for the Shadow Cloud working model.

These are not attribution claims.

They are not claims that APT32, APT42, LIMINAL PANDA, any government, any company, or any known spyware family executed this activity.

They are structured working hypotheses intended to make the Shadow Cloud model testable by qualified DFIR, CTI, mobile forensic, platform-security, and OS-security reviewers.

The purpose is to separate:

- observed structural signals
- possible interpretations
- validation paths
- falsification paths

from direct attribution or speculation.

---

## Core model being tested

Shadow Cloud is treated as a working hypothesis for a possible Apple account / iCloud / backup / restriction-layer / telecom / proximity control-surface anomaly.

The model does not assume that a classic malware payload must be visible.

Instead, the strongest traces may appear at the seams between legitimate Apple services and abnormal control behavior.

The main seam areas are:

- Apple ID state
- iCloud / trusted-device behavior
- ScreenTime / restriction-layer behavior
- ManagedSettings / FamilyControls traces
- visible MDM state versus management-adjacent daemon activity
- iMazing backup behavior
- Manifest.db / backup ledger behavior
- RTCR / reporting generation behavior
- CommCenter / Baseband / SIM / OTP trust behavior
- BSSID / RSSI / proximity-related signals
- resource pressure and evidence-preservation interference

---

## Hypothesis 1: Policy-as-Persistence

### Meaning

The persistence mechanism may not be a classic malware implant.

Instead, persistence may be expressed through policy state, restriction state, Apple ID trust state, ScreenTime state, ManagedSettings behavior, or management-adjacent daemon activity.

### Observed indicator categories

- ScreenTime restrictions appearing without clear user configuration
- Apple ID sign-out restriction behavior
- ManagedSettings / FamilyControls traces
- management-adjacent daemon activity
- MDMStatus:false or supervised:false while restriction-like behavior appears
- repeated daemon failure or policy-state anomalies

### Why it matters

If policy state is being used as persistence, then ordinary malware triage may miss the control mechanism.

The relevant question becomes:

> What state is being preserved across devices, accounts, backups, or restore generations?

not only:

> What binary is running?

### What would support this hypothesis

- repeated restriction behavior across multiple devices
- restriction behavior surviving restore, migration, or Apple ID lineage changes
- mismatch between visible management state and effective restriction behavior
- correlation between ScreenTime / ManagedSettings / daemon activity and user-observed control symptoms

### What would weaken or falsify it

- confirmed local user configuration for all restriction behavior
- reproducible normal Apple behavior explaining the same pattern
- no cross-device or cross-generation continuity
- vendor-confirmed benign explanation for all relevant policy-state transitions

### Current confidence

Medium to high as a structural hypothesis.

Not proven.

---

## Hypothesis 2: Backup-layer Anti-Forensics

### Meaning

Backup-layer artifacts may not be the primary attack mechanism.

They may instead represent an anti-forensic layer affecting evidence preservation, restoration integrity, reviewability, or third-party verification.

### Observed indicator categories

- Manifest.db abnormality
- non-SQLite or opaque Manifest behavior
- backup generation inconsistency
- RTCR generation anomalies
- encrypted versus unencrypted backup differences
- iMazing success display versus abnormal backend artifact state
- evidence package preservation difficulty

### Why it matters

If the backup ledger becomes opaque, abnormal, damaged, or inconsistent, then later forensic review becomes weaker even if the user attempted preservation.

The relevant question becomes:

> Is the backup layer preserving evidence, or becoming part of the anomaly?

### What would support this hypothesis

- repeated Manifest.db structural abnormality across backup generations
- different behavior between encrypted and unencrypted backups
- reproducible mismatch between backup success status and artifact validity
- abnormal RTCR / Manifest / Status / Info plist relationships
- comparison devices showing normal backup ledgers under similar conditions

### What would weaken or falsify it

- confirmed iMazing or Apple backup behavior fully explaining the Manifest pattern
- identical Manifest behavior reproduced on clean control devices
- normal SQLite access after proper decryption and tool handling
- no meaningful difference between affected and control backups

### Current confidence

Medium to high as a Shadow Cloud-specific differential hypothesis.

Not part of known public APT42 TTP based on current public reporting.

Not proven.

---

## Hypothesis 3: Trust-Graph Poisoning

### Meaning

The center of gravity may not be a single infected device.

The anomaly may involve distortion of a broader trust graph, including Apple ID lineage, trusted devices, backup lineage, SIM / OTP state, and financial device trust.

### Observed indicator categories

- Apple ID lineage transitions
- device identity discontinuity
- usageClientId switching
- trusted-device behavior anomalies
- SIM / CommCenter / OTP-related anomalies
- financial applications requesting re-authentication
- bank-side “device changed?” type indicators
- backup lineage inconsistency

### Why it matters

If the trust graph is affected, wiping or replacing one device may not eliminate the anomaly.

The relevant question becomes:

> Is the trusted relationship itself being distorted?

not only:

> Is this phone compromised?

### What would support this hypothesis

- similar trust-state anomalies across multiple Apple devices
- continuity after device replacement or Apple ID migration
- correlation between device trust anomalies and financial re-authentication events
- repeated identity discontinuity in logs
- difference between owner devices and clean comparison devices

### What would weaken or falsify it

- every event explained by normal account migration or device replacement
- no cross-device continuity
- no relation between trust-state anomalies and authentication events
- clean vendor-side confirmation that all trusted-device states are normal

### Current confidence

High as an explanatory hypothesis.

Not proven.

---

## Hypothesis 4: Proximity-triggered State Switch

### Meaning

Wi-Fi / BSSID / RSSI / Evil Twin / rogue AP / nearby-device signals may not be the main attack mechanism.

They may function as proximity or condition triggers used to change state when the target is physically present in a specific environment.

### Observed indicator categories

- BSSID / RSSI / channel anchors
- WiFiLQMMetrics anomalies
- locationd correlation
- CommCenter / Baseband correlation
- movement or arrival-time correlation
- device behavior changes around physical proximity events
- repeated proximity-linked daemon activity

### Why it matters

The proximity layer may act as a trigger, selector, or environmental condition.

The relevant question becomes:

> Did the device state change when the target entered a specific radio environment?

not only:

> Was a rogue AP used for traffic interception?

### What would support this hypothesis

- repeated state changes near specific BSSID / RSSI patterns
- time correlation between human proximity events and daemon / restriction / telecom events
- similar behavior after travel, arrival, or network environment change
- control devices showing no equivalent state change under similar conditions

### What would weaken or falsify it

- BSSID / RSSI patterns fully explained by ordinary Wi-Fi roaming
- no repeatable time correlation
- no link between proximity signals and control-layer symptoms
- clean network environment reproducing the same results

### Current confidence

Medium.

Useful as a trigger hypothesis, not as a standalone attribution claim.

---

## Hypothesis 5: Deniability-first Design

### Meaning

The observed pattern may be designed to appear as ordinary iOS bugs, storage pressure, iCloud sync problems, Wi-Fi quality problems, user error, or backup-tool failure.

The goal may include plausible deniability.

### Observed indicator categories

- minor daemon failures across multiple layers
- diskwrites / CPU resource pressure
- storage pressure during evidence-relevant moments
- screenshot or screen-recording difficulty during critical moments
- backup failure or partial backup behavior
- sync delay / deletion / log preservation anomalies
- normal-looking error categories masking cross-layer correlation

### Why it matters

A deniability-first design would not produce one obvious malware indicator.

It would produce many individually dismissible symptoms that become meaningful only when aligned across time, device, and layer.

### What would support this hypothesis

- repeated clustering of individually minor errors around evidence-relevant events
- cross-device recurrence of similar “benign-looking” failure modes
- strong time correlation between user action and evidence-preservation degradation
- comparison devices lacking the same clustered pattern

### What would weaken or falsify it

- ordinary iOS behavior explains all clusters independently
- no timing relationship to evidence-relevant activity
- same pattern appears on clean control devices
- storage and backup problems are fully explained by local configuration or hardware failure

### Current confidence

Medium to high as a design hypothesis.

Not proven.

---

## Hypothesis 6: Alpha / Beta Cohort Testing

### Meaning

The observed long-term, multi-device pattern may represent staged testing or phased refinement rather than a finished mature operation.

The strongest anomalies may be exposed at the seams because the model is incomplete or still being tuned.

### Observed indicator categories

- phase-shift-like density increases
- March 2026 beta-phase candidate behavior
- different anomaly types across owner devices and comparison devices
- device-specific failure modes
- repeated but imperfect cross-layer coupling
- stronger contradictions during transition windows

### Why it matters

If this is a phased test, then the “flaws” are not noise.

They are the most important evidence.

The relevant question becomes:

> Where does the control model fail to hide itself?

### What would support this hypothesis

- clear phase boundaries
- increasing sophistication over time
- decreasing visible contradiction across later periods
- different devices showing different test roles
- comparison devices acting as negative or partial controls

### What would weaken or falsify it

- no chronological progression
- no repeatable phase windows
- no difference between affected and comparison devices
- all anomalies explained by unrelated local failures

### Current confidence

Medium.

Important for timeline analysis, not a direct proof of actor identity.

---

## Hypothesis 7: Evidence-Suppression Objective

### Meaning

The objective may include not only surveillance or access, but also suppression of the user’s ability to preserve, explain, export, or validate evidence.

This would make evidence preservation itself part of the contested surface.

### Observed indicator categories

- screenshot failure
- screen recording failure
- storage pressure during critical events
- backup inconsistency
- Manifest / RTCR abnormality
- SFA or related artifact preservation difficulty
- deletion / logd / resource-pressure patterns
- inability to capture key moments despite user effort

### Why it matters

If evidence suppression is an objective, then absence of evidence becomes less reassuring.

The relevant question becomes:

> Did the system behave normally when the user attempted to preserve evidence?

### What would support this hypothesis

- repeated preservation failure during high-value events
- correlation between user evidence actions and resource / daemon / backup anomalies
- cross-device or cross-period recurrence
- successful preservation on control devices under similar conditions
- failure modes aligning with the most important event windows

### What would weaken or falsify it

- preservation failures fully explained by storage exhaustion, user error, or tool limitations
- no timing relationship to important events
- same failures reproduced on clean devices
- no link between preservation failure and control-layer anomalies

### Current confidence

High as a reviewer-facing hypothesis.

Not proven.

---

## Summary table

| Hypothesis | Main layer | Primary question | Current role |
|---|---|---|---|
| Policy-as-Persistence | ScreenTime / ManagedSettings / policy state | Is policy state acting as persistence? | Core |
| Backup-layer Anti-Forensics | Manifest / backup / RTCR | Is the backup layer part of evidence degradation? | Core |
| Trust-Graph Poisoning | Apple ID / trusted devices / financial trust | Is the trust graph distorted? | Core |
| Proximity-triggered State Switch | BSSID / RSSI / telecom / location | Is proximity a trigger condition? | Supporting |
| Deniability-first Design | OS error surface / resource pressure | Are failures designed to look benign? | Core-supporting |
| Alpha / Beta Cohort Testing | timeline / multi-device comparison | Are contradictions exposed during staged refinement? | Supporting |
| Evidence-Suppression Objective | preservation / capture / backup | Is evidence preservation itself being interfered with? | Core |

---

## Reviewer guidance

Reviewers should not treat these hypotheses as conclusions.

They should be used as a validation framework.

A useful review should attempt to answer:

1. Which hypotheses are supported by the preserved artifacts?
2. Which hypotheses are contradicted by the artifacts?
3. Which hypotheses can be explained by normal Apple / iOS / iCloud / iMazing behavior?
4. Which hypotheses require Apple-side telemetry, server-side logs, or platform-level review?
5. Which artifacts are necessary for falsification?

The preferred outcome is not confirmation.

The preferred outcome is a reproducible explanation.
