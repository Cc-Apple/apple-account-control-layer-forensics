# 2026-03-18 15G Backup-Ledger / Snapshot Core Anchor

## Status

Public technical anchor.

This document summarizes the 2026-03-18 15G backup-ledger / Snapshot observation.

It does not publish raw logs, raw Manifest artifacts, raw Snapshot contents, private full paths, Apple ID material, telecom identifiers, financial data, or personal content.

It does not claim compromise, attribution, vendor causation, iMazing causation, Apple causation, hidden MDM confirmation, baseband compromise, SIM compromise, or OTP interception.

## Scope

Device label:

- `15G`

Core date:

- `2026-03-18`

Explicitly indexed source groups:

- `log_0318`
- `manifest_0318_error`
- `manifest_0318_snapshot`

Public evidence index:

- `evidence/2026-03-18-core-anchor/01_public_artifact_index_0318.csv`

Private-path material is intentionally excluded.

## Indexed material

The 2026-03-18 package indexed 21,948 files.

Breakdown:

- `log_0318`: 133 files
- `manifest_0318_error`: 107 files
- `manifest_0318_snapshot`: 21,708 files

Errors:

- `0`

The indexed material includes public titles, file sizes, SHA256 hashes, sample SHA256 hashes, file magic, categories, source group labels, and redacted paths.

## Snapshot observation

The 2026-03-18 Snapshot-generation workspace retained the following structure:

- Snapshot file count: `19,625`
- Snapshot size: `56,713,615,632 bytes`
- Snapshot size: approximately `52.8187 GiB`
- Snapshot hex bucket count: `256`

This indicates that the backup pipeline did not fail before starting.

The workspace reached a deep Snapshot-generation state.

## Backup-ledger state

The retained plist state is the key observation.

`Status.plist`:

- `BackupState`: `empty`
- `SnapshotState`: `uploading`
- `IsFullBackup`: `true`
- `Date`: `2026-03-18 15:57:27`

`Status.plist.backup`:

- `BackupState`: `empty`
- `SnapshotState`: `uploading`
- `IsFullBackup`: `true`
- `Date`: `2026-03-18 15:57:27`

`Info.plist.tmp`:

- generated
- device identifier matched the 15G backup context
- Product Version: `18.5`
- Build Version: `22F76`
- Product Type: `iPhone13,1`
- Installed Applications: `39`

## Interpretation

This is not presented as a completed normal backup.

The stronger observation is:

> The 2026-03-18 15G backup workspace reached a large Snapshot-generation state, created Status.plist and Info.plist.tmp material, and retained 19,625 Snapshot files totaling approximately 52.8 GiB, while the backup-ledger state still reported BackupState=empty and SnapshotState=uploading.

This supports a backup-ledger / evidence-preservation seam.

It does not prove causation by iMazing, Apple, Windows, USB, storage, or any actor.

## Relationship to the seven-layer seam

This 2026-03-18 backup-ledger anchor supports the previously retained seven-layer platform-state seam.

The relevant layers are:

- account state
- iCloud state
- restriction state
- backup-ledger state
- FileProvider state
- telecom context
- evidence-preservation behavior

The 2026-03-18 daily core remained a seven-layer A-core anchor in the prior strict result.

## Relationship to the eighth trigger layer

The eighth layer is treated separately.

The eighth layer is not derived from the Snapshot folder itself.

It is a candidate orchestration / trigger layer involving:

- background tasks
- calendar
- Duet / CoreDuet
- HomeKit / Home
- location / network / time trigger context
- push notifications
- reminders
- Shortcuts automation
- trial / experiment state

The significance is that the backup-ledger / evidence-preservation anchor and the orchestration-trigger support both align with the same 2026-03-18 15G core date.

## Normal-hypothesis boundary

Normal explanations remain possible and should be tested.

Relevant normal explanations include:

- ordinary iMazing backup failure
- USB instability
- external storage behavior
- Windows file-system behavior
- local PC I/O failure
- ordinary iOS backup pipeline failure
- incomplete Snapshot upload/finalization state

However, the observation is not a simple no-device or no-start failure.

The device context, Status.plist, Info.plist.tmp, and large Snapshot material were present.

## Public reproducibility

Public files for this anchor:

- `00_PACKAGE_MANIFEST.json`
- `01_public_artifact_index_0318.csv`
- `03_plist_status_info_0318.csv`
- `04_top_level_summary_0318.csv`
- `05_snapshot_bucket_summary_0318.csv`
- `06_duplicate_hash_summary_0318.csv`
- `07_existing_result_file_map.csv`
- `99_final_summary_0318.json`
- `SC_0318_final_summary.md`

Raw artifacts are preserved privately and can be verified later by matching:

- original title
- size
- SHA256
- date
- device label
- source group
- file magic
- redacted path

## 2026-04-01 note

A similar core pattern was observed for 2026-04-01.

The public Snapshot / Workspace hash-index package for 2026-04-01 is not included in this update and may be added later after separate indexing.
