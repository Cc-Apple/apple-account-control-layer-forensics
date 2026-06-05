# scan_0318_workspace.py
# -*- coding: utf-8 -*-
r"""
2026-03-18 Workspace / Snapshot / backup-ledger audit.

Public-safe version.

Purpose:
  Audit one explicitly selected iMazing / iOS backup workspace in read-only mode.

Checks:
  - Snapshot directory existence
  - Snapshot hex buckets
  - file count
  - total size
  - zero-byte files
  - small / large file density
  - Status.plist / Status.plist.backup
  - Info.plist / Info.plist.tmp
  - BackupState / SnapshotState / IsFullBackup

Privacy:
  No private path is hard-coded.
  Input path is supplied at runtime.
  Public output uses relative paths only.
  Raw file contents are not exported.

Safety:
  Read input folder only.
  No deletion.
  No movement.
  No modification.
  No addition to input folder.
  No renaming.
"""

from pathlib import Path
from collections import Counter
import argparse
import os
import csv
import json
import plistlib
import hashlib
import datetime as dt
import traceback


SNAPSHOT_NAMES = {"Snapshot", "snapshot"}
SAMPLE_HASH_BYTES = 1024 * 1024
HEX_BUCKETS = {f"{i:02x}" for i in range(256)}


def parse_args():
    ap = argparse.ArgumentParser(
        description="Audit a 2026-03-18 iMazing Snapshot workspace in read-only mode."
    )
    ap.add_argument("--root", required=True, help="Workspace / backup root to audit.")
    ap.add_argument("--out-dir", required=True, help="Output directory.")
    ap.add_argument("--device-label", default="15G", help="Public device label.")
    ap.add_argument("--core-date", default="2026-03-18", help="Core date label.")
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


def sha256_sample(path: Path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            h.update(f.read(SAMPLE_HASH_BYTES))
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


def safe_stat(path: Path):
    try:
        st = path.stat()
        return {
            "size": st.st_size,
            "mtime": dt.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
            "ctime": dt.datetime.fromtimestamp(st.st_ctime).isoformat(timespec="seconds"),
        }
    except Exception:
        return {"size": 0, "mtime": "", "ctime": ""}


def classify_artifact(path: Path):
    s = str(path).lower()
    name = path.name.lower()

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
    if "snapshot" in s:
        return "snapshot_file"
    return "other"


def parse_plist(path: Path):
    try:
        with open(path, "rb") as f:
            obj = plistlib.load(f)
        return obj, ""
    except Exception as e:
        return None, repr(e)


def rel_path(root: Path, path: Path):
    try:
        return str(path.relative_to(root))
    except Exception:
        return path.name


def plist_rows(root: Path):
    rows = []

    targets = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        name = p.name.lower()
        if name in {"status.plist", "status.plist.backup", "info.plist", "info.plist.tmp", "manifest.plist"}:
            targets.append(p)

    for p in sorted(targets, key=lambda x: str(x).lower()):
        st = safe_stat(p)
        obj, err = parse_plist(p)

        base = {
            "relative_path": rel_path(root, p),
            "filename": p.name,
            "size_bytes": st["size"],
            "mtime": st["mtime"],
            "magic": file_magic(p),
            "parse_error": err,
        }

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
                if isinstance(v, (list, tuple, dict)):
                    v = len(v)
                if k == "Target Identifier" and v:
                    v = "[DEVICE_IDENTIFIER_REDACTED]"
                base[k] = str(v)

        rows.append(base)

    return rows


def find_snapshot_root(root: Path):
    if not root.exists():
        return None

    for child in root.iterdir():
        if child.is_dir() and child.name in SNAPSHOT_NAMES:
            return child

    for p in root.rglob("*"):
        if p.is_dir() and p.name in SNAPSHOT_NAMES:
            return p

    return None


def top_level_inventory(root: Path):
    rows = []
    if not root.exists():
        return rows

    for p in sorted(root.iterdir(), key=lambda x: x.name.lower()):
        total_size = 0
        file_count = 0
        dir_count = 0
        zero_count = 0

        if p.is_file():
            st = safe_stat(p)
            total_size = st["size"]
            file_count = 1
            zero_count = 1 if total_size == 0 else 0

        elif p.is_dir():
            for dp, dns, fns in os.walk(p):
                dir_count += len(dns)
                for fn in fns:
                    fp = Path(dp) / fn
                    try:
                        sz = fp.stat().st_size
                    except Exception:
                        sz = 0
                    total_size += sz
                    file_count += 1
                    if sz == 0:
                        zero_count += 1

        rows.append({
            "name": p.name,
            "type": "dir" if p.is_dir() else "file",
            "file_count": file_count,
            "dir_count": dir_count,
            "total_size_bytes": total_size,
            "total_size_gib": round(total_size / (1024 ** 3), 4),
            "zero_byte_files": zero_count,
        })

    return rows


def scan_files(root: Path):
    rows = []
    errors = []

    if not root.exists():
        return rows, errors

    idx = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {"$RECYCLE.BIN", "System Volume Information"}]

        for fn in filenames:
            idx += 1
            p = Path(dirpath) / fn

            try:
                st = safe_stat(p)
                rel = rel_path(root, p)
                parts = Path(rel).parts
                top = parts[0] if parts else ""

                snapshot_bucket = ""
                if parts and parts[0].lower() == "snapshot":
                    snapshot_bucket = parts[1] if len(parts) >= 2 else ""

                rows.append({
                    "idx": idx,
                    "relative_path": rel,
                    "top_level": top,
                    "snapshot_bucket": snapshot_bucket,
                    "filename": p.name,
                    "extension": p.suffix.lower(),
                    "category": classify_artifact(p),
                    "size_bytes": st["size"],
                    "mtime": st["mtime"],
                    "ctime": st["ctime"],
                    "is_zero_byte": st["size"] == 0,
                    "is_small_1kb_or_less": st["size"] <= 1024,
                    "is_large_1mb_or_more": st["size"] >= 1024 * 1024,
                    "is_large_100mb_or_more": st["size"] >= 100 * 1024 * 1024,
                    "magic": file_magic(p),
                    "sha256_sample_1mb": sha256_sample(p),
                })

            except Exception as e:
                errors.append({
                    "path": rel_path(root, p),
                    "error": repr(e),
                    "traceback": traceback.format_exc(limit=2),
                })

    return rows, errors


def bucket_summary(file_rows):
    buckets = {}

    for r in file_rows:
        b = r.get("snapshot_bucket", "")
        if not b:
            continue

        if b not in buckets:
            buckets[b] = {
                "bucket": b,
                "file_count": 0,
                "total_size_bytes": 0,
                "zero_byte_files": 0,
                "small_1kb_or_less": 0,
                "large_1mb_or_more": 0,
                "large_100mb_or_more": 0,
                "category_counts": Counter(),
                "magic_counts": Counter(),
            }

        x = buckets[b]
        x["file_count"] += 1
        x["total_size_bytes"] += int(r["size_bytes"])
        x["zero_byte_files"] += 1 if r["is_zero_byte"] in (True, "True") else 0
        x["small_1kb_or_less"] += 1 if r["is_small_1kb_or_less"] in (True, "True") else 0
        x["large_1mb_or_more"] += 1 if r["is_large_1mb_or_more"] in (True, "True") else 0
        x["large_100mb_or_more"] += 1 if r["is_large_100mb_or_more"] in (True, "True") else 0
        x["category_counts"][r["category"]] += 1
        x["magic_counts"][r["magic"]] += 1

    rows = []
    for b, x in buckets.items():
        rows.append({
            "bucket": x["bucket"],
            "is_hex_bucket": b.lower() in HEX_BUCKETS,
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

    rows.sort(key=lambda r: (not r["is_hex_bucket"], r["bucket"]))
    return rows


def make_summary(root: Path, device_label: str, core_date: str, file_rows, top_rows, buckets, plists, errors, snapshot_root):
    total_size = sum(int(r["size_bytes"]) for r in file_rows)
    zero = sum(1 for r in file_rows if r["is_zero_byte"] in (True, "True"))
    small = sum(1 for r in file_rows if r["is_small_1kb_or_less"] in (True, "True"))
    large_1mb = sum(1 for r in file_rows if r["is_large_1mb_or_more"] in (True, "True"))
    large_100mb = sum(1 for r in file_rows if r["is_large_100mb_or_more"] in (True, "True"))

    by_top = Counter(r["top_level"] for r in file_rows)
    by_cat = Counter(r["category"] for r in file_rows)
    by_magic = Counter(r["magic"] for r in file_rows)

    snapshot_files = [r for r in file_rows if r["top_level"].lower() == "snapshot"]
    snapshot_size = sum(int(r["size_bytes"]) for r in snapshot_files)

    status_rows = [r for r in plists if r["filename"].lower() in {"status.plist", "status.plist.backup"}]
    info_rows = [r for r in plists if r["filename"].lower() in {"info.plist", "info.plist.tmp"}]

    return {
        "script": "scan_0318_workspace.py",
        "generated_at": now(),
        "input_policy": "read_only_no_delete_no_move_no_modify_no_add_no_rename",
        "device_label": device_label,
        "core_date": core_date,
        "root_public": "[WORKSPACE_ROOT]",
        "output_dir": "[OUTPUT_DIR]",
        "root_exists": root.exists(),
        "snapshot_root_public": "[WORKSPACE_ROOT]/Snapshot" if snapshot_root else "",
        "total_files": len(file_rows),
        "total_size_bytes": total_size,
        "total_size_gib": round(total_size / (1024 ** 3), 4),
        "zero_byte_files": zero,
        "small_1kb_or_less": small,
        "large_1mb_or_more": large_1mb,
        "large_100mb_or_more": large_100mb,
        "snapshot_files": len(snapshot_files),
        "snapshot_size_bytes": snapshot_size,
        "snapshot_size_gib": round(snapshot_size / (1024 ** 3), 4),
        "top_level_counts": dict(by_top),
        "category_counts": dict(by_cat),
        "magic_counts": dict(by_magic),
        "hex_bucket_count_present": sum(1 for b in buckets if b["is_hex_bucket"]),
        "plist_rows": len(plists),
        "status_plist_rows": status_rows,
        "info_plist_rows": info_rows,
        "errors": len(errors),
    }


def make_markdown(summary):
    lines = []
    lines.append("# 2026-03-18 Workspace / Snapshot Audit")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- device: `{summary['device_label']}`")
    lines.append(f"- core date: `{summary['core_date']}`")
    lines.append(f"- root exists: `{summary['root_exists']}`")
    lines.append(f"- root: `{summary['root_public']}`")
    lines.append(f"- snapshot root: `{summary['snapshot_root_public']}`")
    lines.append(f"- total files: `{summary['total_files']}`")
    lines.append(f"- total size GiB: `{summary['total_size_gib']}`")
    lines.append(f"- Snapshot files: `{summary['snapshot_files']}`")
    lines.append(f"- Snapshot size GiB: `{summary['snapshot_size_gib']}`")
    lines.append(f"- zero-byte files: `{summary['zero_byte_files']}`")
    lines.append(f"- small files <=1KB: `{summary['small_1kb_or_less']}`")
    lines.append(f"- large files >=1MB: `{summary['large_1mb_or_more']}`")
    lines.append(f"- large files >=100MB: `{summary['large_100mb_or_more']}`")
    lines.append(f"- hex buckets present: `{summary['hex_bucket_count_present']}`")
    lines.append(f"- errors: `{summary['errors']}`")
    lines.append("")
    lines.append("## Status / Info plist observations")
    lines.append("")

    for r in summary.get("status_plist_rows", []):
        lines.append(f"### {r.get('filename')}")
        lines.append(f"- relative path: `{r.get('relative_path')}`")
        lines.append(f"- size: `{r.get('size_bytes')}`")
        lines.append(f"- BackupState: `{r.get('BackupState', '')}`")
        lines.append(f"- SnapshotState: `{r.get('SnapshotState', '')}`")
        lines.append(f"- IsFullBackup: `{r.get('IsFullBackup', '')}`")
        lines.append(f"- Date: `{r.get('Date', '')}`")
        lines.append("")

    for r in summary.get("info_plist_rows", []):
        lines.append(f"### {r.get('filename')}")
        lines.append(f"- relative path: `{r.get('relative_path')}`")
        lines.append(f"- size: `{r.get('size_bytes')}`")
        lines.append(f"- Last Backup Date: `{r.get('Last Backup Date', '')}`")
        lines.append(f"- Product Version: `{r.get('Product Version', '')}`")
        lines.append(f"- Build Version: `{r.get('Build Version', '')}`")
        lines.append(f"- Product Type: `{r.get('Product Type', '')}`")
        lines.append(f"- Target Identifier: `{r.get('Target Identifier', '')}`")
        lines.append(f"- Installed Applications: `{r.get('Installed Applications', '')}`")
        lines.append("")

    lines.append("## Interpretation boundary")
    lines.append("")
    lines.append("This audit does not prove compromise or attribution.")
    lines.append("")
    lines.append("It checks whether the selected workspace contains a completed backup-ledger state or a large Snapshot/uploading/tmp state.")
    lines.append("")

    return "\n".join(lines)


def main():
    args = parse_args()

    root = Path(args.root)
    out_dir = Path(args.out_dir)
    device_label = args.device_label
    core_date = args.core_date

    out_dir.mkdir(parents=True, exist_ok=True)

    started = now()
    print("=== Workspace scan start ===")
    print("root:", root)
    print("output:", out_dir)
    print("policy: read-only input")

    snapshot_root = find_snapshot_root(root)
    top_rows = top_level_inventory(root)
    plist_data = plist_rows(root)
    file_rows, errors = scan_files(root)
    bucket_rows = bucket_summary(file_rows)

    zero_rows = [r for r in file_rows if r["is_zero_byte"] in (True, "True")]
    large_rows = [r for r in file_rows if r["is_large_100mb_or_more"] in (True, "True")]
    small_rows = [r for r in file_rows if r["is_small_1kb_or_less"] in (True, "True")]

    file_fields = [
        "idx", "relative_path", "top_level", "snapshot_bucket", "filename",
        "extension", "category", "size_bytes", "mtime", "ctime",
        "is_zero_byte", "is_small_1kb_or_less", "is_large_1mb_or_more",
        "is_large_100mb_or_more", "magic", "sha256_sample_1mb"
    ]

    top_fields = [
        "name", "type", "file_count", "dir_count", "total_size_bytes",
        "total_size_gib", "zero_byte_files"
    ]

    plist_fields = [
        "relative_path", "filename", "size_bytes", "mtime", "magic", "parse_error",
        "BackupState", "SnapshotState", "IsFullBackup", "Date", "Last Backup Date",
        "Product Version", "Build Version", "Product Type", "Target Identifier",
        "Device Name", "Display Name", "Installed Applications", "iTunes Version"
    ]

    bucket_fields = [
        "bucket", "is_hex_bucket", "file_count", "total_size_bytes", "total_size_gib",
        "zero_byte_files", "small_1kb_or_less", "large_1mb_or_more",
        "large_100mb_or_more", "category_counts", "magic_counts"
    ]

    write_csv(out_dir / "00_top_level_inventory.csv", top_rows, top_fields)
    write_csv(out_dir / "01_workspace_file_inventory.csv", file_rows, file_fields)
    write_csv(out_dir / "02_snapshot_bucket_summary.csv", bucket_rows, bucket_fields)
    write_csv(out_dir / "03_plist_status_info.csv", plist_data, plist_fields)
    write_csv(out_dir / "04_zero_byte_files.csv", zero_rows, file_fields)
    write_csv(out_dir / "05_large_100mb_files.csv", large_rows, file_fields)
    write_csv(out_dir / "06_small_1kb_or_less_files.csv", small_rows, file_fields)
    write_csv(out_dir / "98_errors.csv", errors, ["path", "error", "traceback"])

    summary = make_summary(root, device_label, core_date, file_rows, top_rows, bucket_rows, plist_data, errors, snapshot_root)
    summary["started"] = started
    summary["finished"] = now()

    write_json(out_dir / "99_workspace_summary.json", summary)
    write_text(out_dir / "workspace_audit_summary.md", make_markdown(summary))

    print("=== complete ===")
    print("finished:", summary["finished"])
    print("total_files:", summary["total_files"])
    print("total_size_gib:", summary["total_size_gib"])
    print("snapshot_files:", summary["snapshot_files"])
    print("snapshot_size_gib:", summary["snapshot_size_gib"])
    print("zero_byte_files:", summary["zero_byte_files"])
    print("small_1kb_or_less:", summary["small_1kb_or_less"])
    print("large_100mb_or_more:", summary["large_100mb_or_more"])
    print("hex_bucket_count_present:", summary["hex_bucket_count_present"])
    print("errors:", summary["errors"])
    print("output:", out_dir)


if __name__ == "__main__":
    main()
