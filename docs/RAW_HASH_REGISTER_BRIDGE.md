# Raw Artifact Hash Register Bridge

This repository is the upper-level public review package for the Shadow Cloud / Apple ecosystem state-anomaly model.

The canonical public raw-artifact hash register is published in the companion repository:

```text
https://github.com/Cc-Apple/shadow-cloud-state-reconstruction
```

## Canonical hash register

```text
Repository:
  https://github.com/Cc-Apple/shadow-cloud-state-reconstruction

Path:
  evidence-index/RAW_ARTIFACT_HASH_REGISTER_PUBLIC.csv

Summary:
  manifests/RAW_ARTIFACT_HASH_REGISTER_SUMMARY.json

Output manifest:
  manifests/RAW_HASH_REGISTER_OUTPUT_SHA256_MANIFEST.csv
```

## Current register status

```text
public_rows:
  56508

errors:
  0

hashed_count:
  56508

duplicates:
  3650

public CSV size:
  18219829 bytes

public CSV sha256:
  8f1fcd108cf7ed39d45034d2ee0d4ff08768ace8fcedf9ed2845bcc11ddad372
```

## Why this repo uses a bridge

The hash register is maintained in one canonical location to avoid drift between repositories.

This upper-level repo points to the canonical register instead of duplicating the full CSV.

## Boundary

The hash register is an integrity and reproducibility anchor only.

It does not prove attacker attribution, state attribution, Apple attribution, C2 endpoint discovery, communication success, hidden MDM enrollment, explicit usageClientId old→new transition, or complete clean control.
