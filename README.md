# Apple Account / Cloud / Control-Layer Forensic Anomaly Dataset

This repository is a technical triage package, not an attribution claim.

It summarizes approximately 11 months of forensic observations across 9+ Apple devices, including owner devices and comparison devices. The dataset focuses on recurring Apple account, cloud, backup, restriction-layer, and proximity-communication anomalies that do not resemble a simple spyware payload infection.

## Core request

Do these artifacts look like normal Apple/iOS behavior, or do they merit deeper forensic triage as a possible account/cloud/control-layer operation?

No attribution is asserted.  
No malware family name is asserted.  
APT32, APT42, and LIMINAL PANDA are referenced only as public TTP comparison points.

## Key observations

1. Manifest.db anomaly  
   Multiple backup generations showed Manifest.db behaving as non-SQLite / opaque / high-entropy structures. The core issue is not merely encrypted backup handling, but repeated abnormal Manifest.db behavior at the backup path / backup service layer.

2. usageClientId transitions  
   Repeated usageClientId switching and discontinuity were observed across logs and devices.

3. Restriction-layer signals without visible MDM  
   ScreenTime / Game Center / Content & Privacy / ManagedSettings / FamilyControls signals were observed while visible MDM / supervised / userIsManaged indicators were not present.

4. March 2026 beta-phase candidate  
   Normalized analysis showed a density increase in restriction-layer, ID/cloud, resource-pressure, and operational-trace categories.

5. March 12, 2026 mini1 core event  
   A mini1 Analytics log showed a strong proximity/communication pattern involving SIMTransfer, BluetoothDiscovery, CommCenter, BasebandPowerCycle, PrivacyProxy, RSSI, Nearby, and resource reactions.

6. March 7, 2026 15G Wi-Fi/BSSID location anchor  
   WiFiConnectionQuality/sysdiagnose artifacts showed a physical Wi-Fi anchor with RSSI, channel, and lastJoined timestamps.

## Repository status

This repository is being prepared as a minimal reproducible evidence package. Raw private logs are not publicly uploaded. Sensitive identifiers are redacted or represented by SHA256 hashes where possible.

## Included materials

- Evidence index
- SHA256 index
- Reproducible Python scripts
- Sanitized summaries
- TTP comparison notes
- Limitation and non-attribution notes
