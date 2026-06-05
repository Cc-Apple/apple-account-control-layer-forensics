# build_0318_final_from_real_paths.py
# -*- coding: utf-8 -*-
r"""
2026-03-18 15G final evidence package builder.

Public-safe version.

Purpose:
  Audit explicitly selected 2026-03-18 folders in read-only mode:
    - 2026-03-18 log folder
    - 2026-03-18 Manifest error-generation folder
    - 2026-03-18 Manifest Snapshot-generation folder
    - optional prior result folder

  Generate a small public artifact index and summary for GitHub / external review.

Privacy:
  This script does not hard-code private paths or device identifiers.
  Input paths are supplied at runtime.
  Public outputs use redacted paths.
  Raw file contents are not exported.

Safety:
  Read input folders only.
  No deletion.
  No movement.
  No modification.
  No addition to input folders.
  No renaming.
"""

from pathlib import Path
from collections import Counter, defaultdict
import argparse
import csv
import json
import os
import re
import hashlib
import plistlib
import shutil
import zipfile
import datetime as dt
import traceback


HASH_CHUNK = 1024 * 1024 * 4
SAMPLE_BYTES = 1024 * 1024
HEX_BUCKETS = {f"{i:02x}" for i in range(256)}

SKIP_EXTS = {
    ".zip", ".7z", ".rar", ".tar", ".gz", ".tgz", ".xz", ".bz2",
    ".mp4", ".mov", ".jpg", ".jpeg", ".png", ".heic", ".webp",
}

NOISE_NAMES = {
    "keyword_hits.csv",
    "text_hits.tsv",
    "text_strong_hits.tsv",
}


def parse_args():
    ap = argparse.ArgumentParser(
        description="Build a public-safe 2026-03-18 core anchor evidence package."
    )

    ap.add_argument("--log-0318", required=True, help="Path to 2026-03-18 log folder.")
    ap.add_argument("--manifest-error", required=True, help="Path to Manifest error-generation folder.")
    ap.add_argument("--manifest-snapshot", required=True, help="Path to Manifest Snapshot-generation folder.")
    ap.add_argument("--result-root", default="", help="Optional prior result folder.")
    ap.add_argument("--out-dir", required=True, help="Output directory.")
    ap.add_argument("--zip-out", default="", help="Optional output ZIP path.")
    ap.add_argument("--device-label", default="15G", help="Public device label.")
    ap.add_argument("--core-date", default="2026-03-18", help="Core date label.")
    ap.add_argument("--device-id-label", default="[15G_DEVICE_ID]", help="Public redaction label for device identifier.")

    return ap.parse_args()


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def mkdir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def write_csv(path, rows, fields):
    mkdir(path.parent)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_json(path, obj):
    mkdir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def write_text(path, text):
    mkdir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_json(path):
    if not path or not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def sha256_file(path: Path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                b = f.read(HASH_CHUNK)
                if not b:
                    break
                h.update(b)
        return h.hexdigest()
    except Exception:
        return ""


def sha256_sample(path: Path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            h.update(f.read(SAMPLE_BYTES))
        return h.hexdigest()
    except Exception:
        return ""


def file_magic(path: Path):
    try:
        with open(path, "rb") as f:
            b = f.read(64)
    except Exception:
        return "unreadable"

    if not b:
        return "empty"
    if b.startswith(b"SQLite format 3\x00"):
        return "sqlite"
    if b.startswith(b"bplist"):
        return "binary_plist"
    if b.startswith(b"<?xml") or b.lstrip().startswith(b"<plist"):
        return "xml_plist_or_xml"
    if b.startswith(b"{") or b.startswith(b"["):
        return "json_like"
    if b.startswith(b"\x1f\x8b"):
        return "gzip"
    if b.startswith(b"PK\x03\x04"):
        return "zip"
    if all((32 <= x <= 126) or x in (9, 10, 13) for x in b[:32]):
        return "text_like"
    return "binary_or_unknown"


def stat_row(path: Path):
    try:
        st = path.stat()
        return {
            "size_bytes": st.st_size,
            "mtime": dt.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
            "ctime": dt.datetime.fromtimestamp(st.st_ctime).isoformat(timespec="seconds"),
            "mtime_date": dt.datetime.fromtimestamp(st.st_mtime).date().isoformat(),
        }
    except Exception:
        return {
            "size_bytes": 0,
            "mtime": "",
            "ctime": "",
            "mtime_date": "",
        }


def classify_category(path: Path):
    s = str(path).lower()
    name = path.name.lower()

    if name.startswith("stacks-"):
        return "stacks"
    if name.startswith("jetsamevent"):
        return "jetsam"
    if name.startswith("forcereset") or "forcereset" in name:
        return "force_reset"
    if "sysdiagnose" in name:
        return "sysdiagnose"
    if name.startswith("analytics-"):
        return "analytics"
    if "commcenter" in name:
        return "commcenter"
    if "baseband" in name:
        return "baseband"
    if "screentime" in name:
        return "screentime"
    if "managedsettings" in name:
        return "managedsettings"
    if "managedappdistributiond" in name:
        return "managedappdistributiond"
    if "dmd" in name or "digitalhealth" in name:
        return "dmd_digitalhealth"
    if "fileprovider" in name:
        return "fileprovider"
    if "triald" in name or "trial" in name:
        return "trial"
    if "duet" in name or "coreduet" in name:
        return "duet_coreduet"
    if "cloud" in name or "ckks" in name or "sos" in name or "pcs" in name:
        return "icloud_cloud"
    if name == "manifest.db":
        return "manifest_db"
    if name == "manifest.plist":
        return "manifest_plist"
    if name == "status.plist":
        return "status_plist"
    if name == "status.plist.backup":
        return "status_plist_backup"
    if name == "info.plist":
        return "info_plist"
    if name == "info.plist.tmp":
        return "info_plist_tmp"
    if "photos.sqlite" in name:
        return "photos_sqlite"
    if "cloudphotodb" in s:
        return "cloudphotodb"
    if name.endswith("-wal") or name.endswith(".wal"):
        return "sqlite_wal"
    if name.endswith("-shm") or name.endswith(".shm"):
        return "sqlite_shm"
    if "setupapi" in name:
        return "setupapi"
    if "snapshot" in s:
        return "snapshot_file"
    if name in NOISE_NAMES or name.endswith(".py") or "result" in s:
        return "generated_or_result"
    return "other"


def redacted_path(path: Path, cfg):
    s = str(path)

    replacements = [
        (str(cfg["log_0318"]), "[LOG_0318]"),
        (str(cfg["manifest_error"]), "[MANIFEST_0318_ERROR]"),
        (str(cfg["manifest_snapshot"]), "[MANIFEST_0318_SNAPSHOT]"),
        (str(cfg["result_root"]), "[RESULT_ROOT]") if cfg["result_root"] else ("", ""),
    ]

    for old, new in replacements:
        if old:
            s = s.replace(old, new)

    # Hide common long identifiers.
    s = re.sub(r"0000[0-9A-Fa-f]{4}-[0-9A-Fa-f]{16}", cfg["device_id_label"], s)
    s = re.sub(r"[0-9A-Fa-f]{40}", "[SHA1LIKE]", s)

    return s


def under_snapshot(path: Path):
    parts = [p.lower() for p in path.parts]
    return "snapshot" in parts


def snapshot_bucket(path: Path, manifest_snapshot: Path):
    try:
        rel = path.relative_to(manifest_snapshot)
    except Exception:
        return ""

    parts = rel.parts
    for i, p in enumerate(parts):
        if p.lower() == "snapshot" and len(parts) > i + 1:
            return parts[i + 1]
    return ""


def is_noise(path: Path):
    name = path.name.lower()
    s = str(path).lower()
    if name in NOISE_NAMES:
        return True
    if name.endswith(".py") or name.endswith(".bat") or name.endswith(".cmd"):
        return True
    if "core_evidence_extract" in s or "8_final" in s or "8_strict" in s:
        return True
    return False


def collect_files(root: Path):
    files = []
    if not root.exists():
        return files

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {"$RECYCLE.BIN", "System Volume Information"}]

        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in SKIP_EXTS:
                continue
            files.append(p)

    return files


def scan_source_files(cfg):
    roots = [
        ("log_0318", cfg["log_0318"]),
        ("manifest_0318_error", cfg["manifest_error"]),
        ("manifest_0318_snapshot", cfg["manifest_snapshot"]),
    ]

    rows = []
    errors = []
    idx = 0

    for root_label, root in roots:
        files = collect_files(root)

        for p in files:
            idx += 1
            try:
                st = stat_row(p)
                bucket = snapshot_bucket(p, cfg["manifest_snapshot"])

                row = {
                    "artifact_id": f"SC-0318-{idx:06d}",
                    "core_date": cfg["core_date"],
                    "device_label": cfg["device_label"],
                    "source_group": root_label,
                    "category": classify_category(p),
                    "original_title": p.name,
                    "extension": p.suffix.lower(),
                    "size_bytes": st["size_bytes"],
                    "mtime": st["mtime"],
                    "ctime": st["ctime"],
                    "mtime_date": st["mtime_date"],
                    "sha256": sha256_file(p),
                    "sample_sha256_1mb": sha256_sample(p),
                    "file_magic": file_magic(p),
                    "under_snapshot": under_snapshot(p),
                    "snapshot_bucket": bucket,
                    "is_hex_bucket": bucket.lower() in HEX_BUCKETS if bucket else False,
                    "is_zero_byte": st["size_bytes"] == 0,
                    "is_small_1kb_or_less": st["size_bytes"] <= 1024,
                    "is_large_1mb_or_more": st["size_bytes"] >= 1024 * 1024,
                    "is_large_100mb_or_more": st["size_bytes"] >= 100 * 1024 * 1024,
                    "public_raw": "no",
                    "preserved_private": "yes",
                    "noise_or_generated": is_noise(p),
                    "relative_path_redacted": redacted_path(p, cfg),
                    "private_full_path": str(p),
                }
                rows.append(row)

            except Exception as e:
                errors.append({
                    "path": str(p),
                    "error": repr(e),
                    "traceback": traceback.format_exc(limit=2),
                })

    return rows, errors


def parse_plists(rows):
    plist_rows = []

    for r in rows:
        title = r["original_title"].lower()
        if title not in {"status.plist", "status.plist.backup", "info.plist", "info.plist.tmp", "manifest.plist"}:
            continue

        p = Path(r["private_full_path"])
        obj = None
        err = ""

        try:
            with open(p, "rb") as f:
                obj = plistlib.load(f)
        except Exception as e:
            err = repr(e)

        out = dict(r)
        out["parse_error"] = err

        if isinstance(obj, dict):
            keys = [
                "BackupState",
                "SnapshotState",
                "IsFullBackup",
                "Date",
                "Last Backup Date",
                "Product Version",
                "Build Version",
                "Product Type",
                "Target Identifier",
                "Device Name",
                "Display Name",
                "Installed Applications",
                "iTunes Version",
            ]
            for k in keys:
                v = obj.get(k, "")
                if isinstance(v, dict):
                    v = len(v)
                elif isinstance(v, list):
                    v = len(v)
                out[k] = str(v)

        plist_rows.append(out)

    return plist_rows


def top_level_summary(rows):
    c = {}

    for r in rows:
        key = (r["source_group"], r["category"])
        if key not in c:
            c[key] = {
                "source_group": r["source_group"],
                "category": r["category"],
                "file_count": 0,
                "total_size_bytes": 0,
                "zero_byte_files": 0,
                "small_1kb_or_less": 0,
                "large_1mb_or_more": 0,
                "large_100mb_or_more": 0,
            }

        x = c[key]
        x["file_count"] += 1
        x["total_size_bytes"] += int(r["size_bytes"])
        x["zero_byte_files"] += 1 if r["is_zero_byte"] in (True, "True") else 0
        x["small_1kb_or_less"] += 1 if r["is_small_1kb_or_less"] in (True, "True") else 0
        x["large_1mb_or_more"] += 1 if r["is_large_1mb_or_more"] in (True, "True") else 0
        x["large_100mb_or_more"] += 1 if r["is_large_100mb_or_more"] in (True, "True") else 0

    out = []
    for x in c.values():
        x["total_size_gib"] = round(x["total_size_bytes"] / (1024 ** 3), 4)
        out.append(x)

    out.sort(key=lambda r: (r["source_group"], r["category"]))
    return out


def snapshot_bucket_summary(rows):
    b = {}

    for r in rows:
        if r["source_group"] != "manifest_0318_snapshot":
            continue

        bucket = r.get("snapshot_bucket", "")
        if not bucket:
            continue

        if bucket not in b:
            b[bucket] = {
                "bucket": bucket,
                "is_hex_bucket": bucket.lower() in HEX_BUCKETS,
                "file_count": 0,
                "total_size_bytes": 0,
                "zero_byte_files": 0,
                "small_1kb_or_less": 0,
                "large_1mb_or_more": 0,
                "large_100mb_or_more": 0,
                "category_counts": Counter(),
                "magic_counts": Counter(),
            }

        x = b[bucket]
        x["file_count"] += 1
        x["total_size_bytes"] += int(r["size_bytes"])
        x["zero_byte_files"] += 1 if r["is_zero_byte"] in (True, "True") else 0
        x["small_1kb_or_less"] += 1 if r["is_small_1kb_or_less"] in (True, "True") else 0
        x["large_1mb_or_more"] += 1 if r["is_large_1mb_or_more"] in (True, "True") else 0
        x["large_100mb_or_more"] += 1 if r["is_large_100mb_or_more"] in (True, "True") else 0
        x["category_counts"][r["category"]] += 1
        x["magic_counts"][r["file_magic"]] += 1

    out = []
    for x in b.values():
        out.append({
            "bucket": x["bucket"],
            "is_hex_bucket": x["is_hex_bucket"],
            "file_count": x["file_count"],
            "total_size_bytes": x["total_size_bytes"],
            "total_size_gib": round(x["total_size_bytes"] / (1024 ** 3), 4),
            "zero_byte_files": x["zero_byte_files"],
            "small_1kb_or_less": x["small_1kb_or_less"],
            "large_1mb_or_more": x["large_1mb_or_more"],
            "large_100mb_or_more": x["large_100mb_or_more"],
            "category_counts": json.dumps(dict(x["category_counts"]), ensure_ascii=False),
            "magic_counts": json.dumps(dict(x["magic_counts"]), ensure_ascii=False),
        })

    out.sort(key=lambda r: (not r["is_hex_bucket"], r["bucket"]))
    return out


def duplicate_hash_summary(rows):
    by_hash = defaultdict(list)

    for r in rows:
        h = r.get("sha256", "")
        if h:
            by_hash[h].append(r)

    out = []

    for h, items in by_hash.items():
        if len(items) <= 1:
            continue

        out.append({
            "sha256": h,
            "count": len(items),
            "source_groups": "|".join(sorted(set(x["source_group"] for x in items))),
            "categories": "|".join(sorted(set(x["category"] for x in items))),
            "titles": "|".join(sorted(set(x["original_title"] for x in items))[:30]),
            "paths_redacted": " || ".join(x["relative_path_redacted"] for x in items[:20]),
        })

    out.sort(key=lambda r: (-r["count"], r["sha256"]))
    return out


def collect_existing_result_files(cfg):
    wanted = [
        "99_core_evidence_extract_summary.json",
        "04_core_evidence_summary.md",
        "05_core_machine_summary.yaml",
        "00_core_daily_A_only.csv",
        "01_core_windows_A_only.csv",
        "99_trigger_core_final_summary.json",
        "02_trigger_core_summary.md",
        "00_trigger_core_daily_compact.csv",
        "01_trigger_core_windows_compact.csv",
        "99_refined_summary.json",
        "github_artifact_index_refined.md",
        "github_reproducibility_note_refined.md",
        "03_log_only_core_artifacts.csv",
        "05_duplicate_hash_classified.csv",
        "06_issue_summary.csv",
        "02_artifact_index_public_compact_github.csv",
        "99_workspace_summary.json",
        "workspace_audit_summary.md",
    ]

    rows = []
    found_paths = {}

    root = cfg["result_root"]
    if not root or not root.exists():
        for name in wanted:
            found_paths[name] = ""
            rows.append({
                "file": name,
                "found": False,
                "size_bytes": 0,
                "path_redacted": "",
            })
        return rows, found_paths

    for name in wanted:
        hits = list(root.rglob(name))
        if hits:
            hits.sort(key=lambda p: len(str(p)))
            p = hits[0]
            found_paths[name] = str(p)
            st = stat_row(p)
            rows.append({
                "file": name,
                "found": True,
                "size_bytes": st["size_bytes"],
                "path_redacted": redacted_path(p, cfg),
            })
        else:
            found_paths[name] = ""
            rows.append({
                "file": name,
                "found": False,
                "size_bytes": 0,
                "path_redacted": "",
            })

    return rows, found_paths


def load_existing_jsons(found):
    data = {}

    for k, p in found.items():
        if not p or not p.lower().endswith(".json"):
            continue
        data[k] = read_json(Path(p))

    return data


def make_summary(cfg, rows, plist_rows, bucket_rows, dup_rows, result_map, errors):
    by_source = Counter(r["source_group"] for r in rows)
    by_cat = Counter(r["category"] for r in rows)
    by_magic = Counter(r["file_magic"] for r in rows)

    snapshot_rows = [
        r for r in rows
        if r["source_group"] == "manifest_0318_snapshot" and r["under_snapshot"] in (True, "True")
    ]
    snapshot_size = sum(int(r["size_bytes"]) for r in snapshot_rows)

    return {
        "script": "build_0318_final_from_real_paths.py",
        "generated_at": now(),
        "input_policy": "read_only_no_delete_no_move_no_modify_no_add_no_rename",
        "output_dir": str(cfg["out_dir"]),
        "core_date": cfg["core_date"],
        "device_label": cfg["device_label"],
        "device_identifier_redacted": cfg["device_id_label"],
        "source_paths_public": {
            "log_0318": "[LOG_0318]",
            "manifest_0318_error": "[MANIFEST_0318_ERROR]",
            "manifest_0318_snapshot": "[MANIFEST_0318_SNAPSHOT]",
            "result_root": "[RESULT_ROOT]" if cfg["result_root"] else "",
        },
        "source_exists": {
            "log_0318": cfg["log_0318"].exists(),
            "manifest_0318_error": cfg["manifest_error"].exists(),
            "manifest_0318_snapshot": cfg["manifest_snapshot"].exists(),
            "result_root": cfg["result_root"].exists() if cfg["result_root"] else False,
        },
        "total_indexed_files": len(rows),
        "by_source_group": dict(by_source),
        "category_counts": dict(by_cat),
        "magic_counts": dict(by_magic),
        "snapshot_file_count": len(snapshot_rows),
        "snapshot_size_bytes": snapshot_size,
        "snapshot_size_gib": round(snapshot_size / (1024 ** 3), 4),
        "snapshot_hex_bucket_count": sum(1 for b in bucket_rows if b["is_hex_bucket"]),
        "zero_byte_files": sum(1 for r in rows if r["is_zero_byte"] in (True, "True")),
        "small_1kb_or_less": sum(1 for r in rows if r["is_small_1kb_or_less"] in (True, "True")),
        "large_1mb_or_more": sum(1 for r in rows if r["is_large_1mb_or_more"] in (True, "True")),
        "large_100mb_or_more": sum(1 for r in rows if r["is_large_100mb_or_more"] in (True, "True")),
        "plist_rows": len(plist_rows),
        "duplicate_hash_groups": len(dup_rows),
        "existing_result_files_found": sum(1 for r in result_map if r["found"]),
        "existing_result_files_missing": sum(1 for r in result_map if not r["found"]),
        "errors": len(errors),
    }


def make_markdown(summary, plist_rows, result_map):
    lines = []

    lines.append("# SC 2026-03-18 Final Result Summary")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(f"- Device: `{summary['device_label']}`")
    lines.append(f"- Date: `{summary['core_date']}`")
    lines.append("- Raw logs / raw Manifest are not included in this output.")
    lines.append("- This package indexes titles, sizes, SHA256, file magic, category, source group, and redacted paths.")
    lines.append("")
    lines.append("## Explicit source folders")
    lines.append("")
    for k, v in summary["source_paths_public"].items():
        if v:
            lines.append(f"- `{k}`: `{v}` / exists=`{summary['source_exists'][k]}`")
    lines.append("")
    lines.append("## Indexed counts")
    lines.append("")
    lines.append(f"- total indexed files: `{summary['total_indexed_files']}`")
    lines.append(f"- by source group: `{summary['by_source_group']}`")
    lines.append(f"- snapshot files: `{summary['snapshot_file_count']}`")
    lines.append(f"- snapshot size GiB: `{summary['snapshot_size_gib']}`")
    lines.append(f"- snapshot hex buckets: `{summary['snapshot_hex_bucket_count']}`")
    lines.append(f"- zero-byte files: `{summary['zero_byte_files']}`")
    lines.append(f"- small files <=1KB: `{summary['small_1kb_or_less']}`")
    lines.append(f"- large files >=1MB: `{summary['large_1mb_or_more']}`")
    lines.append(f"- large files >=100MB: `{summary['large_100mb_or_more']}`")
    lines.append(f"- duplicate hash groups: `{summary['duplicate_hash_groups']}`")
    lines.append(f"- errors: `{summary['errors']}`")
    lines.append("")
    lines.append("## Plist observations")
    lines.append("")

    for r in plist_rows:
        title = r.get("original_title", "")
        if title.lower() not in {"status.plist", "status.plist.backup", "info.plist", "info.plist.tmp", "manifest.plist"}:
            continue

        lines.append(f"### {title}")
        lines.append(f"- source: `{r.get('source_group')}`")
        lines.append(f"- size: `{r.get('size_bytes')}`")
        lines.append(f"- magic: `{r.get('file_magic')}`")
        for k in [
            "BackupState", "SnapshotState", "IsFullBackup", "Date",
            "Last Backup Date", "Product Version", "Build Version",
            "Product Type", "Target Identifier", "Installed Applications"
        ]:
            if r.get(k, ""):
                val = r.get(k)
                if k == "Target Identifier":
                    val = "[DEVICE_IDENTIFIER_REDACTED]"
                lines.append(f"- {k}: `{val}`")
        lines.append("")

    lines.append("## Existing result files")
    lines.append("")
    for r in result_map:
        lines.append(f"- `{r['file']}`: found=`{r['found']}` size=`{r['size_bytes']}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("This result package is not an attribution or compromise proof.")
    lines.append("")
    lines.append("It supports provenance and backup-ledger review for the 2026-03-18 core date.")
    lines.append("The key question is whether the backup workspace represents a completed normal backup or a deep Snapshot-generation state that failed to finalize into a completed backup ledger.")
    lines.append("")

    return "\n".join(lines)


def copy_key_existing_files(cfg, result_map):
    dst = cfg["out_dir"] / "copied_key_results"
    dst.mkdir(parents=True, exist_ok=True)

    copied = []
    root = cfg["result_root"]

    if not root or not root.exists():
        return copied

    for r in result_map:
        if not r["found"]:
            continue

        hits = list(root.rglob(r["file"]))
        if not hits:
            continue

        hits.sort(key=lambda p: len(str(p)))
        p = hits[0]

        if p.name in {
            "99_local_private_path_refined.csv",
            "01_artifact_index_public_refined_full.csv",
            "04_manifest_only_core_artifacts.csv",
        }:
            continue

        target = dst / p.name
        shutil.copy2(p, target)
        copied.append({
            "file": p.name,
            "size_bytes": target.stat().st_size,
            "copied_to": str(target),
        })

    return copied


def zip_output(cfg):
    zip_out = cfg["zip_out"]
    if not zip_out:
        return ""

    if zip_out.exists():
        zip_out.unlink()

    with zipfile.ZipFile(zip_out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in cfg["out_dir"].rglob("*"):
            if p.is_file():
                z.write(p, arcname=str(p.relative_to(cfg["out_dir"])))

    return str(zip_out)


def main():
    args = parse_args()

    cfg = {
        "log_0318": Path(args.log_0318),
        "manifest_error": Path(args.manifest_error),
        "manifest_snapshot": Path(args.manifest_snapshot),
        "result_root": Path(args.result_root) if args.result_root else Path(),
        "out_dir": Path(args.out_dir),
        "zip_out": Path(args.zip_out) if args.zip_out else Path(),
        "device_label": args.device_label,
        "core_date": args.core_date,
        "device_id_label": args.device_id_label,
    }

    started = now()
    cfg["out_dir"].mkdir(parents=True, exist_ok=True)

    print("=== SC 0318 final from explicit paths ===")
    print("log_0318:", cfg["log_0318"])
    print("manifest_error:", cfg["manifest_error"])
    print("manifest_snapshot:", cfg["manifest_snapshot"])
    print("result_root:", cfg["result_root"] if args.result_root else "")
    print("output:", cfg["out_dir"])
    print("policy: read-only input")

    rows, errors = scan_source_files(cfg)
    plist_rows = parse_plists(rows)
    top_rows = top_level_summary(rows)
    bucket_rows = snapshot_bucket_summary(rows)
    dup_rows = duplicate_hash_summary(rows)
    result_map, found_paths = collect_existing_result_files(cfg)
    existing_jsons = load_existing_jsons(found_paths)

    summary = make_summary(cfg, rows, plist_rows, bucket_rows, dup_rows, result_map, errors)
    summary["started"] = started
    summary["finished"] = now()
    summary["existing_json_summaries_loaded"] = list(existing_jsons.keys())

    file_fields = [
        "artifact_id", "core_date", "device_label", "source_group", "category",
        "original_title", "extension", "size_bytes", "mtime", "ctime", "mtime_date",
        "sha256", "sample_sha256_1mb", "file_magic", "under_snapshot",
        "snapshot_bucket", "is_hex_bucket", "is_zero_byte", "is_small_1kb_or_less",
        "is_large_1mb_or_more", "is_large_100mb_or_more", "public_raw",
        "preserved_private", "noise_or_generated", "relative_path_redacted"
    ]

    private_fields = file_fields + ["private_full_path"]

    plist_fields = private_fields + [
        "BackupState", "SnapshotState", "IsFullBackup", "Date",
        "Last Backup Date", "Product Version", "Build Version",
        "Product Type", "Target Identifier", "Device Name", "Display Name",
        "Installed Applications", "iTunes Version", "parse_error"
    ]

    top_fields = [
        "source_group", "category", "file_count", "total_size_bytes",
        "zero_byte_files", "small_1kb_or_less", "large_1mb_or_more",
        "large_100mb_or_more", "total_size_gib"
    ]

    bucket_fields = [
        "bucket", "is_hex_bucket", "file_count", "total_size_bytes",
        "total_size_gib", "zero_byte_files", "small_1kb_or_less",
        "large_1mb_or_more", "large_100mb_or_more", "category_counts",
        "magic_counts"
    ]

    dup_fields = [
        "sha256", "count", "source_groups", "categories", "titles", "paths_redacted"
    ]

    result_fields = ["file", "found", "size_bytes", "path_redacted"]

    public_rows = []
    for r in rows:
        rr = dict(r)
        rr.pop("private_full_path", None)
        public_rows.append(rr)

    write_csv(cfg["out_dir"] / "01_public_artifact_index_0318.csv", public_rows, file_fields)
    write_csv(cfg["out_dir"] / "02_private_artifact_index_0318_local_only.csv", rows, private_fields)
    write_csv(cfg["out_dir"] / "03_plist_status_info_0318.csv", plist_rows, plist_fields)
    write_csv(cfg["out_dir"] / "04_top_level_summary_0318.csv", top_rows, top_fields)
    write_csv(cfg["out_dir"] / "05_snapshot_bucket_summary_0318.csv", bucket_rows, bucket_fields)
    write_csv(cfg["out_dir"] / "06_duplicate_hash_summary_0318.csv", dup_rows, dup_fields)
    write_csv(cfg["out_dir"] / "07_existing_result_file_map.csv", result_map, result_fields)
    write_csv(cfg["out_dir"] / "98_errors.csv", errors, ["path", "error", "traceback"])

    write_json(cfg["out_dir"] / "99_final_summary_0318.json", summary)
    write_json(cfg["out_dir"] / "99_loaded_existing_json_summaries.json", existing_jsons)

    md = make_markdown(summary, plist_rows, result_map)
    write_text(cfg["out_dir"] / "SC_0318_final_summary.md", md)

    copied = copy_key_existing_files(cfg, result_map)
    write_json(cfg["out_dir"] / "00_copied_key_results_manifest.json", copied)

    package_manifest = {
        "created_at": now(),
        "input_policy": "read_only",
        "raw_artifacts_included": False,
        "private_full_paths_in_public_index": False,
        "output_dir": str(cfg["out_dir"]),
        "zip": str(cfg["zip_out"]) if cfg["zip_out"] else "",
        "core_date": cfg["core_date"],
        "device": cfg["device_label"],
        "summary_file": "99_final_summary_0318.json",
        "markdown_summary": "SC_0318_final_summary.md",
        "public_index": "01_public_artifact_index_0318.csv",
        "private_local_only_index": "02_private_artifact_index_0318_local_only.csv",
        "do_not_publish": [
            "02_private_artifact_index_0318_local_only.csv"
        ],
    }
    write_json(cfg["out_dir"] / "00_PACKAGE_MANIFEST.json", package_manifest)

    zip_path = zip_output(cfg)

    print("=== complete ===")
    print("finished:", summary["finished"])
    print("total_indexed_files:", summary["total_indexed_files"])
    print("by_source_group:", summary["by_source_group"])
    print("snapshot_file_count:", summary["snapshot_file_count"])
    print("snapshot_size_gib:", summary["snapshot_size_gib"])
    print("snapshot_hex_bucket_count:", summary["snapshot_hex_bucket_count"])
    print("zero_byte_files:", summary["zero_byte_files"])
    print("duplicate_hash_groups:", summary["duplicate_hash_groups"])
    print("existing_result_files_found:", summary["existing_result_files_found"])
    print("errors:", summary["errors"])
    print("output:", cfg["out_dir"])
    if zip_path:
        print("zip:", zip_path)


if __name__ == "__main__":
    main()
