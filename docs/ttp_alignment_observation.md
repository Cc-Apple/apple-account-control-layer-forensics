# TTP Alignment Observation

## Important limitation

This repository does not claim attribution to APT42, APT32, or any other named group.

References to APT42 or APT32 are used only as public TTP comparison anchors.

The analysis compares observed structure and operational style against public TTP concepts.

## APT42-style alignment

Current assessment:

- Structural alignment: high
- Estimated score range: 85-88 / 100
- Center estimate: 86 / 100

Observed alignment:

- Account / identity layer involvement
- Cloud / iCloud / CloudKit / SFA / CKKS / CloudServices involvement
- Native-feature / built-in service orientation
- Surveillance / device-state / usage-state style observation
- No requirement for visible MDM=true or supervised=true

Strong matching structure:

- MDM_false + restriction_management
- account_cloud + telecom_proximity
- usageClientId / RTCReporting
- ScreenTime / ManagedSettings-adjacent artifacts
- CommCenter / Baseband / PLMN artifacts

Boundary:

- APT42 attribution: not established
- APT42 infrastructure: not identified
- APT42 malware family: not identified
- C2: not identified
- payload: not identified
- credential-theft chain: not established

## APT32-style legacy TTP / seam-failure alignment

Current assessment:

- Structural alignment: medium to high
- Estimated score range: 72-78 / 100
- Center estimate: 75 / 100

Observed alignment:

- Long-running behavior
- Low-exposure behavior
- Use of legitimate-looking system components
- Daemon-layer repetition
- Search / save / log / delete / backup-adjacent side effects
- Visible seams at integration points

Observed seam points:

- MDM_false + restriction_management
- account_cloud + telecom_proximity
- PLMN / SFA exposure
- CommCenter / Baseband joins
- seam_failure
- crash / resource / out-of-budget artifacts
- SaveToFiles / searchd / maild / amfid side effects

Boundary:

- APT32 attribution: not established
- APT32 C2: not identified
- APT32 malware family: not identified
- phishing lure: not identified
- known IOC: not identified

## Overall interpretation

The observed Apple device artifacts are more consistent with a long-running account / cloud / telecom / restriction-layer / daemon-layer anomaly model than with isolated benign iOS events.

This remains a technical observation, not an attribution claim.
