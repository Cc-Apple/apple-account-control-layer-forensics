# SC 2026-03-18 Final Result Summary

## Scope

- Device: `15G`
- Date: `2026-03-18`
- Raw logs / raw Manifest are not included in this output.
- This package indexes titles, sizes, SHA256, file magic, category, source group, and redacted paths.

## Explicit source folders

- `log_0318`: `D:\Device-Logs_整理済み\My_Device\15G\2026\03\18` / exists=`True`
- `manifest_0318_error`: `D:\Manifest\My_Device\15G\00008101-000524EC3A30001E\2026-03-18\2026-03-18-093500  Error` / exists=`True`
- `manifest_0318_snapshot`: `D:\Manifest\My_Device\15G\00008101-000524EC3A30001E\2026-03-18\2026-03-18-155727  (Snashpt肥大化世代)` / exists=`True`
- `result_root`: `D:\Result\2026-06-05` / exists=`True`

## Indexed counts

- total indexed files: `21948`
- by source group: `{'log_0318': 133, 'manifest_0318_error': 107, 'manifest_0318_snapshot': 21708}`
- snapshot files: `19625`
- snapshot size GiB: `52.8187`
- snapshot hex buckets: `256`
- zero-byte files: `30`
- small files <=1KB: `8284`
- large files >=1MB: `977`
- large files >=100MB: `177`
- duplicate hash groups: `28`
- errors: `0`

## Plist observations

### Info.plist.tmp
- source: `manifest_0318_error`
- size: `858679`
- magic: `binary_plist`
- Last Backup Date: `2026-03-18 10:54:47`
- Product Version: `18.5`
- Build Version: `22F76`
- Product Type: `iPhone13,1`
- Target Identifier: `00008101-000524EC3A30001E`
- Installed Applications: `39`

### Info.plist.tmp
- source: `manifest_0318_snapshot`
- size: `858679`
- magic: `binary_plist`
- Last Backup Date: `2026-03-18 15:57:30`
- Product Version: `18.5`
- Build Version: `22F76`
- Product Type: `iPhone13,1`
- Target Identifier: `00008101-000524EC3A30001E`
- Installed Applications: `39`

### Status.plist
- source: `manifest_0318_snapshot`
- size: `192`
- magic: `binary_plist`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Date: `2026-03-18 15:57:27.007015`

### Status.plist.backup
- source: `manifest_0318_snapshot`
- size: `192`
- magic: `binary_plist`
- BackupState: `empty`
- SnapshotState: `uploading`
- IsFullBackup: `True`
- Date: `2026-03-18 15:57:27.007015`

## Existing result files

- `99_core_evidence_extract_summary.json`: found=`True` size=`10035`
- `04_core_evidence_summary.md`: found=`True` size=`6661`
- `05_core_machine_summary.yaml`: found=`True` size=`2693`
- `00_core_daily_A_only.csv`: found=`True` size=`2875`
- `01_core_windows_A_only.csv`: found=`True` size=`1715`
- `99_trigger_core_final_summary.json`: found=`True` size=`7661`
- `02_trigger_core_summary.md`: found=`True` size=`8399`
- `00_trigger_core_daily_compact.csv`: found=`True` size=`861`
- `01_trigger_core_windows_compact.csv`: found=`True` size=`2711`
- `99_refined_summary.json`: found=`True` size=`2375`
- `github_artifact_index_refined.md`: found=`True` size=`44359`
- `github_reproducibility_note_refined.md`: found=`True` size=`1367`
- `03_log_only_core_artifacts.csv`: found=`True` size=`162560`
- `05_duplicate_hash_classified.csv`: found=`True` size=`152510`
- `06_issue_summary.csv`: found=`True` size=`303`
- `02_artifact_index_public_compact_github.csv`: found=`True` size=`4774227`
- `99_workspace_summary.json`: found=`True` size=`4000`
- `workspace_audit_summary.md`: found=`True` size=`1596`

## Interpretation

This result package is not an attribution or compromise proof.

It supports provenance and backup-ledger review for the 2026-03-18 15G core date.
The key question is whether the backup workspace represents a completed normal backup or a deep Snapshot-generation state that failed to finalize into a completed backup ledger.
