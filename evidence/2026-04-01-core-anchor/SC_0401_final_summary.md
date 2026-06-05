# 2026-04-01 15G Two Snapshot Generations Public Core Anchor

## Status

Public sanitized technical package.

This package does not include raw logs, raw Manifest artifacts, raw Snapshot contents, private full paths, Apple ID material, telecom identifiers, OTP data, financial data, device names, or device identifiers.

It does not claim compromise, attribution, Apple causation, iMazing causation, Windows causation, hidden MDM confirmation, baseband compromise, SIM compromise, or OTP interception.

## Scope

- Device label: `15G`
- Core date: `2026-04-01`
- Generation 1: `0401_020720`
- Generation 2: `0401_053959`

## Generation observations

### 0401_020720 / 2026-04-01-020720

- Snapshot files: `6998`
- Snapshot size: `12.9303 GiB`
- Snapshot hex bucket count: `256`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Info.plist.tmp: `yes`
- Product Version: `18.5`
- Build Version: `22F76`
- Product Type: `iPhone13,1`
- Errors: `0`

### 0401_053959 / 2026-04-01-053959

- Snapshot files: `50994`
- Snapshot size: `78.1324 GiB`
- Snapshot hex bucket count: `256`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Info.plist.tmp: `yes`
- Product Version: `18.5`
- Build Version: `22F76`
- Product Type: `iPhone13,1`
- Errors: `0`

## Cross-generation summary

- relative_paths_total: `54912`
- both_generations: `6998`
- 0401_020720_only: `2087`
- 0401_053959_only: `45827`
- same_size: `6990`
- changed_size: `8`
- same_sample_hash: `0`
- different_sample_hash_or_blank: `6998`

## 2026-03-18 to 2026-04-01 bridge

The 2026-04-01 result repeats the same backup-ledger / Snapshot-family structure already observed on 2026-03-18.

Common structure:

- large Snapshot-generation state
- 256 Snapshot hex buckets
- Status.plist / Status.plist.backup present
- Info.plist.tmp present
- BackupState=empty
- SnapshotState=uploading
- IsFullBackup=true

This supports recurrence rather than a single isolated backup failure.

## Public files generated

- `00_PACKAGE_MANIFEST_0401.json`
- `01_public_generation_summary_0401.csv`
- `02_public_plist_status_info_0401.csv`
- `03_public_snapshot_bucket_summary_0401.csv`
- `04_cross_generation_summary_0401.csv`
- `05_public_top_level_inventory_0401.csv`
- `06_0318_0401_bridge_summary.csv`
- `0401_machine_summary.json`
- `99_final_summary_0401.json`
- `SC_0401_final_summary.md`

## Interpretation boundary

This package is a backup-ledger / evidence-preservation seam anchor.

It is not standalone proof of compromise or attribution.

The review question is whether ordinary iOS / iMazing / Windows / USB / storage behavior can reproduce both 2026-03-18 and 2026-04-01 large Snapshot-generation states with the same non-finalized backup-ledger pattern.
