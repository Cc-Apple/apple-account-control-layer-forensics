# 2026-03-18 / 2026-04-01 15G Log-Manifest Cross Public Summary

## Status

Public sanitized technical package.

This package does not include raw logs, raw Manifest artifacts, raw Snapshot contents, private full paths, Apple ID material, telecom identifiers, BSSID values, OTP data, financial data, device names, or device identifiers.

It does not claim compromise, attribution, Apple causation, iMazing causation, Windows causation, hidden MDM confirmation, baseband compromise, SIM compromise, or OTP interception.

## Core observation

The 2026-03-18 and 2026-04-01 15G results show repeated non-finalized backup-ledger / Snapshot-generation states, with same-day platform-state layer overlap across both dates.

## Repeated Manifest / Snapshot states

### 0318_155727 / 2026-03-18
- Snapshot files: `19625`
- Snapshot size GiB: `52.8187`
- Snapshot hex bucket count: `256`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Info.plist.tmp: `yes`
- Errors: `0`

### 0401_020720 / 2026-04-01
- Snapshot files: `6998`
- Snapshot size GiB: `12.9303`
- Snapshot hex bucket count: `256`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Info.plist.tmp: `yes`
- Errors: `0`

### 0401_053959 / 2026-04-01
- Snapshot files: `50994`
- Snapshot size GiB: `78.1324`
- Snapshot hex bucket count: `256`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Info.plist.tmp: `yes`
- Errors: `0`

## Layer overlap on both dates

- `account_cloud`
- `evidence_backup_storage`
- `fileprovider`
- `orchestration_trigger`
- `restriction_management`
- `telecom`
- `usage_state`

## Alignment scores

- `0318_155727`: score `113`, ledger `6/6`, layers `7`
- `0401_020720`: score `113`, ledger `6/6`, layers `7`
- `0401_053959`: score `113`, ledger `6/6`, layers `7`

## Interpretation boundary

This is a cross-validation package for repeated backup-ledger / Snapshot / platform-state layer overlap.

It is not standalone proof of compromise or attribution.

The review question is whether ordinary iOS / iMazing / Windows / USB / storage behavior can reproduce both 2026-03-18 and 2026-04-01 large Snapshot-generation states with the same non-finalized backup-ledger pattern and same-day layer overlap.
