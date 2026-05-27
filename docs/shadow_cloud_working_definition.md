# Shadow Cloud: Working Definition

## Definition

Shadow Cloud is a working term used to describe the observed account / cloud / control-layer anomaly structure found across Apple device logs and related artifacts.

It refers to a recurring multi-layer pattern involving:

- Apple ID
- iCloud
- CloudKit
- SFA
- CKKS
- CloudServices
- ScreenTime
- ManagedSettings
- CommCenter
- Baseband
- PLMN / carrier state
- RTCReporting
- usageClientId
- daemon repetition
- backup / logging / search / deletion-adjacent behavior

## What Shadow Cloud is not

- Not a confirmed malware name
- Not an actor name
- Not an APT attribution
- Not a claim against Apple
- Not a claim against any specific state
- Not a claim of confirmed C2 or payload

## Current phase estimate

Based on the observed structure:

- 2025-07 to 2026-02 / early 2026-03:
  - Alpha / field-prototype phase
  - Estimated maturity: 55-65%

- 2026-03 to 2026-04:
  - Beta / migration acceleration phase
  - Estimated maturity: 70-78%

- 2026-05:
  - Late beta / pre-release-candidate-like phase
  - Estimated maturity: 75-82%
  - Center estimate: approximately 78%

## Why it does not appear fully mature

The structure still leaves visible seams:

- MDM_false appears alongside restriction / management-adjacent behavior
- ScreenTime / ManagedSettings-adjacent artifacts remain visible
- CommCenter / Baseband / PLMN joins remain visible
- SFA / CloudServices joins remain visible
- Seam-failure and crash-adjacent artifacts remain visible
- Financial device-trust side effects appear in the timeline
- Search / save / log / auth side effects remain visible

A more mature operation would be expected to suppress or hide these seams more effectively.

## Working interpretation

Shadow Cloud appears to describe a long-running account / cloud / telecom / restriction-layer / daemon-layer anomaly structure.

The current interpretation is that the structure is more consistent with a possible test-phase, beta-phase, or transitional control-layer model than with a fully mature and silent operation.

This remains a working technical observation, not an attribution claim.
