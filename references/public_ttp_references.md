# Public TTP References

## Purpose

This file lists public references used only for TTP / operational-doctrine comparison.

No attribution is asserted.

APT32, APT42, and LIMINAL PANDA are used only as public comparison points.

---

## APT32 / OceanLotus

### MITRE ATT&CK - APT32

URL:

```text
https://attack.mitre.org/groups/G0050/

Relevant public points:
suspected Vietnam-based threat group
active since at least 2014
Southeast Asia focus
targets private sector, foreign governments, dissidents, and journalists
strategic web compromise
credential harvesting
web service abuse
event log deletion / trace suppression related techniques

Use in this repository:

APT32 is used as a comparison point for legacy operational doctrine:
long-term operation
legitimate service abuse
staged operations
trace suppression
forensic meaning disruption
Google Cloud / Mandiant - APT32 / OceanLotus
https://cloud.google.com/blog/topics/threat-intelligence/cyber-espionage-apt32/

Relevant public points:
APT32 / OceanLotus cyber espionage activity
targeting private sector companies
targeting foreign governments, dissidents, and journalists
operations assessed as aligned with Vietnamese state interests
use of custom malware and commercially available tools

Use in this repository:

Mandiant's APT32 reporting is used as a public reference for:
long-term targeted operations
public-sector/private-sector targeting
cyber espionage tradecraft
OceanLotus / APT32 operational doctrine
Meta - Taking Action Against Hackers in Bangladesh and Vietnam
https://about.fb.com/news/2020/12/taking-action-against-hackers-in-bangladesh-and-vietnam/

Relevant public points:
Meta publicly discussed APT32 in Vietnam
platform abuse
malware distribution
account hacking
infrastructure abuse

Use in this repository:

Meta's reporting is used only as a public TTP comparison point for:
platform abuse
account compromise
malware distribution infrastructure
cross-platform operational behavior

APT42
MITRE ATT&CK - APT42
https://attack.mitre.org/groups/G1044/

Relevant public points:
Iranian-sponsored cyber espionage and surveillance group
spearphishing
PINEFLOWER Android malware
monitoring compromised systems and devices
exfiltration using native features and open-source tools
account/cloud/identity-oriented tradecraft

Use in this repository:

APT42 is used as the closest surface comparison for:
credential / account / identity behavior
account/cloud operations
native feature abuse
long-term surveillance
non-payload-centric collection

LIMINAL PANDA / LightBasin
CrowdStrike - LIMINAL PANDA
https://www.crowdstrike.com/en-us/blog/an-analysis-of-lightbasin-telecommunications-attacks/

Relevant public points:

telecommunications-focused adversary
GPRS eDNS servers
roaming between mobile operators
compromised telecommunications companies
subscriber and call metadata focus
telecom-specific infrastructure knowledge

Use in this repository:

LIMINAL PANDA is used only as a comparison point for telecom/proximity-like elements:
BSSID / RSSI
Baseband
CommCenter
SIM / eSIM
carrier context
proximity / communication artifacts

How These References Are Used
These references are not used to claim attribution.
They are used to compare public operational patterns with observed forensic structures:
| Public TTP area                                         | Observed dataset area                                                        |
| ------------------------------------------------------- | ---------------------------------------------------------------------------- |
| APT32-like trace suppression / legitimate service abuse | Manifest.db opaque behavior, file-name/body mismatch, backup-layer anomalies |
| APT42-like account/cloud/identity operations            | Apple ID, CloudKit, backup/sync, usageClientId, MobileIdentity / Lockdown    |
| LIMINAL-like telecom/proximity operations               | BSSID/RSSI, Wi-Fi, Baseband, CommCenter, SIMTransfer                         |

Working Comparison
The observed dataset appears closest on the surface to APT42-style account/cloud/control-layer behavior.
However, the number and type of operational inconsistencies are difficult to explain as a clean APT42-native model.
A stronger working comparison is:
APT32-like legacy doctrine
→ adapted toward APT42-style account/cloud/control-layer operation
→ with LIMINAL-like telecom/proximity assistance

Non-Attribution Notice
This file is a reference list.
It does not accuse or attribute activity to APT32, APT42, LIMINAL PANDA, Meta, Google, Mandiant, CrowdStrike, Apple, or any specific person or organization.
