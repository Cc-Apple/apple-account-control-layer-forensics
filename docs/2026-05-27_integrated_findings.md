# Integrated Findings: 2025-07-01 to 2026-05-26

## Scope

This document summarizes the integrated result of the structured TTP / behavioral-alignment analysis performed on organized Apple device log folders.

This is not an attribution finding.

No raw logs, Manifest.db files, iMazing backup folders, Apple ID values, BSSID values, banking records, or personal identifiers are published in this repository.

## Input scope

### Wide-range organized result

Period:

2025-07-01 to 2026-04-30

Sources:

- My_Device
- Friend_Device

Final daily shortlist:

318 days

### 2026-05 focused result

Period:

2026-05-01 to 2026-05-26

Devices:

- 12G
- 15G
- iPhone11Pro

Final daily shortlist:

17 days

### Integrated total

Final daily shortlist total:

335 days

Integrated period:

2025-07-01 to 2026-05-26

## Device-level result

- My_Device:mini1: 142
- My_Device:15G: 89
- Friend_Device:Ha Thao: 34
- Friend_Device:Ngoc: 20
- May3Dev:15G: 15
- Friend_Device:Vy: 13
- My_Device:12G: 11
- My_Device:mini2: 4
- Friend_Device:HaThao_Mother: 3
- May3Dev:12G: 2
- Friend_Device:kanaoya: 1
- My_Device:iPhone11Pro: 1

## Monthly distribution

- 2025-07: 57
- 2025-08: 56
- 2025-09: 36
- 2025-10: 17
- 2025-11: 34
- 2025-12: 44
- 2026-01: 23
- 2026-02: 7
- 2026-03: 25
- 2026-04: 19
- 2026-05: 17

## Main observation

The integrated result did not collapse after:

- removing derived text artifacts
- separating SiriSearchFeedback
- separating RTCReporting
- reaggregating Friend_Device by person / folder
- analyzing organized device-specific folders
- adding the 2026-05 focused 3-device result

The structure remained visible across multiple devices and months.

## Core structure observed

The following layers repeatedly appeared together:

- MDM_false
- restriction / management-adjacent artifacts
- account / cloud artifacts
- telecom / proximity artifacts
- usage / RTCReporting artifacts
- daemon repetition
- evidence-interference-adjacent artifacts
- seam-failure artifacts

## Key interpretation

The result is more consistent with a long-running account / cloud / telecom / restriction-layer / daemon-layer anomaly pattern than with isolated single-log anomalies.

However, this repository does not claim:

- actor attribution
- APT42 attribution
- APT32 attribution
- state attribution
- Apple attribution
- confirmed malware
- confirmed payload
- confirmed C2
- confirmed exploit chain

## Current technical position

The integrated result supports a structure-level observation:

The observed Apple device artifacts show a long-running, multi-device, multi-layer account / cloud / telecom / restriction-layer / daemon-layer anomaly structure that appears difficult to explain as isolated benign iOS behavior alone.

This remains a technical observation and a request for expert review.
