# 05. BSSID / Proximity Location Anchor

## Summary

This section documents the March 7, 2026 15G Wi-Fi/BSSID proximity anchor.

The purpose of this section is not to attribute activity to a person or device. The purpose is to record that 15G produced WiFiConnectionQuality / sysdiagnose artifacts consistent with a known physical Wi-Fi environment in the timeline.

This is treated as a location anchor only.

## Key Artifact

Date:

- 2026-03-07

Device:

- 15G

Artifact types:

- sysdiagnose
- WiFiConnectionQuality
- com.apple.wifi-private-mac-networks.plist
- Wi-Fi / BSSID / RSSI / channel / lastJoined metadata

## Public Redaction Notice

The original SSID and BSSID are not fully published in this repository.

Public form:

- SSID: redacted
- BSSID / uniqueID: partially redacted or represented by hash
- RSSI: -49
- Channel: 112
- lastJoined: 2026-03-07 17:35:02 +0700
- lastUpdated: 2026-03-07 17:51:31 +0700

The unredacted values are retained privately for technical review.

## Observed Wi-Fi Anchor

The sysdiagnose / WiFiConnectionQuality artifacts showed:

- a known SSID
- a BSSID / uniqueID
- RSSI value
- channel value
- lastJoined timestamp
- lastUpdated timestamp
- nearbyBSS context

The Wi-Fi environment matched a known physical location in the user's timeline.

## Interpretation

This artifact is important because it provides a location/time anchor for March 7, 2026.

It does not prove:

- that a specific person owned the access point
- that the access point belonged to an attacker
- that the access point was itself malicious
- that the BSSID identifies a nearby person
- attribution to any threat actor

It supports only:

- the device was in or evaluating that Wi-Fi environment
- the timestamp can be correlated with the user's timeline
- the proximity/communication layer was active in the March 2026 beta-phase window

## Relationship to March 2026 Beta-Phase

March 7, 2026 is treated as an early beta-phase anchor because it combines:

- 15G resource-pressure reaction
- ID/cloud-related signals
- proximity/communication signals
- Wi-Fi/BSSID evidence
- known physical location context

This makes March 7 important as a pre-March-12 event.

## Relationship to March 12, 2026

March 12, 2026 is treated as the stronger mini1 proximity/communication peak.

March 7 is treated as:

- an earlier location/proximity anchor
- a 15G-side resource/communication event
- a possible pre-peak stage before the March 12 mini1 event

## BSSID Evidence Handling

BSSID evidence is sensitive because it may identify a physical place or network.

Public repository policy:

- do not publish full raw sysdiagnose
- do not publish full Wi-Fi scan lists
- do not publish full unredacted BSSID values unless necessary
- use partial redaction or SHA256 hashes
- treat BSSID as location evidence, not person attribution

## Technical Triage Questions

1. Are the WiFiConnectionQuality / sysdiagnose artifacts normal for this type of iOS device state?
2. Does lastJoined / lastUpdated indicate actual connection, quality evaluation, or remembered network metadata?
3. Can nearbyBSS / RSSI / channel data be used as a reliable location/time anchor?
4. Is the March 7 Wi-Fi anchor technically meaningful when paired with resource-pressure and ID/cloud signals?
5. Could this be normal user movement and network connection behavior?

## Non-Attribution Notice

This section does not attribute activity to a person, device owner, access point owner, organization, or threat actor.

It records a technical location/time anchor for correlation with other forensic observations.
