# scan_0318_workspace.py
# -*- coding: utf-8 -*-
r"""
2026-03-18 15G Workspace / Snapshot / backup-ledger audit

対象:
  D:\Manifest\My_Device\15G\00008101-000524EC3A30001E\2026-03-18\2026-03-18-155727  (Snashpt肥大化世代)\iMazing\00008101-000524EC3A30001E

出力:
  C:\Users\Administrator\Desktop\2026-03-18-Workspace

目的:
  - Snapshot肥大化の実体確認
  - 00〜ff folder / bucket の有無とサイズ確認
  - 0KB file確認
  - Status.plist / Info.plist / Info.plist.tmp確認
  - BackupState / SnapshotState / IsFullBackup確認
  - top-level構造確認
  - file count / total size / small file / large file / hash sample 出力

禁止:
  - 入力側の削除なし
  - 移動なし
  - 修正なし
  - 追加なし
  - リネームなし
  - raw本文出力なし
"""

from pathlib import Path
from collections import Counter, defaultdict
import os
import csv
import json
import plistlib
import hashlib
import datetime as dt
import traceback


ROOT = Path(r"D:\Manifest\My_Device\15G\00008101-000524EC3A30001E\2026-03-18\2026-03-18-155727  (Snashpt肥大化世代)\iMazing\00008101-000524EC3A30001E")
OUT_DIR = Path(r"C:\Users\Administrator\Desktop\2026-03-18-Workspace")

SNAPSHOT_NAMES = {"Snapshot", "snapshot"}
SAMPLE_HASH_BYTES = 1024 * 1024
HASH_SAMPLE_ONLY = True

HEX_BUCKETS = {f"{i:02x}" for i in range(256)}


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


def plist_rows():
    rows = []

    targets = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        name = p.name.lower()
        if name in {"status.plist", "status.plist.backup", "info.plist", "info.plist.tmp", "manifest.plist"}:
            targets.append(p)

    for p in sorted(targets, key=lambda x: str(x).lower()):
        st = safe_stat(p)
        obj, err = parse_plist(p)

        base = {
            "path": str(p),
            "relative_path": str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p),
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
                base[k] = str(v)
        rows.append(base)

    return rows


def find_snapshot_root():
    for child in ROOT.iterdir() if ROOT.exists() else []:
        if child.is_dir() and child.name in SNAPSHOT_NAMES:
            return child
    # fallback
    for p in ROOT.rglob("*"):
        if p.is_dir() and p.name in SNAPSHOT_NAMES:
            return p
    return None


def top_level_inventory():
    rows = []
    if not ROOT.exists():
        return rows

    for p in sorted(ROOT.iterdir(), key=lambda x: x.name.lower()):
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
            "path": str(p),
        })

    return rows


def scan_files():
    rows = []
    errors = []

    if not ROOT.exists():
        return rows, errors

    idx = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {"$RECYCLE.BIN", "System Volume Information"}]

        for fn in filenames:
            idx += 1
            p = Path(dirpath) / fn

            try:
                st = safe_stat(p)
                rel = str(p.relative_to(ROOT))

                parts = p.relative_to(ROOT).parts
                top = parts[0] if parts else ""

                # Snapshot下の1階層目bucket判定
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
                    "full_path": str(p),
                })

            except Exception as e:
                errors.append({
                    "path": str(p),
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


def make_summary(file_rows, top_rows, buckets, plists, errors, snapshot_root):
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
        "root": str(ROOT),
        "output_dir": str(OUT_DIR),
        "input_policy": "read_only_no_delete_no_move_no_modify_no_add_no_rename",
        "root_exists": ROOT.exists(),
        "snapshot_root": str(snapshot_root) if snapshot_root else "",
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
    lines.append("# 2026-03-18 15G Workspace / Snapshot Audit")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- root exists: `{summary['root_exists']}`")
    lines.append(f"- root: `{summary['root']}`")
    lines.append(f"- snapshot root: `{summary['snapshot_root']}`")
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
    lines.append("It checks whether the 2026-03-18 15G workspace contains a completed backup-ledger state or a large Snapshot/uploading/tmp state.")
    lines.append("")

    return "\n".join(lines)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    started = now()
    print("=== 2026-03-18 Workspace scan start ===")
    print("root:", ROOT)
    print("output:", OUT_DIR)
    print("policy: read-only input")

    snapshot_root = find_snapshot_root()
    top_rows = top_level_inventory()
    plist_data = plist_rows()
    file_rows, errors = scan_files()
    bucket_rows = bucket_summary(file_rows)

    zero_rows = [r for r in file_rows if r["is_zero_byte"] in (True, "True")]
    large_rows = [r for r in file_rows if r["is_large_100mb_or_more"] in (True, "True")]
    small_rows = [r for r in file_rows if r["is_small_1kb_or_less"] in (True, "True")]

    file_fields = [
        "idx", "relative_path", "top_level", "snapshot_bucket", "filename",
        "extension", "category", "size_bytes", "mtime", "ctime",
        "is_zero_byte", "is_small_1kb_or_less", "is_large_1mb_or_more",
        "is_large_100mb_or_more", "magic", "sha256_sample_1mb", "full_path"
    ]

    top_fields = [
        "name", "type", "file_count", "dir_count", "total_size_bytes",
        "total_size_gib", "zero_byte_files", "path"
    ]

    plist_fields = [
        "path", "relative_path", "filename", "size_bytes", "mtime", "magic", "parse_error",
        "BackupState", "SnapshotState", "IsFullBackup", "Date", "Last Backup Date",
        "Product Version", "Build Version", "Product Type", "Target Identifier",
        "Device Name", "Display Name", "Installed Applications", "iTunes Version"
    ]

    bucket_fields = [
        "bucket", "is_hex_bucket", "file_count", "total_size_bytes", "total_size_gib",
        "zero_byte_files", "small_1kb_or_less", "large_1mb_or_more",
        "large_100mb_or_more", "category_counts", "magic_counts"
    ]

    write_csv(OUT_DIR / "00_top_level_inventory.csv", top_rows, top_fields)
    write_csv(OUT_DIR / "01_workspace_file_inventory.csv", file_rows, file_fields)
    write_csv(OUT_DIR / "02_snapshot_bucket_summary.csv", bucket_rows, bucket_fields)
    write_csv(OUT_DIR / "03_plist_status_info.csv", plist_data, plist_fields)
    write_csv(OUT_DIR / "04_zero_byte_files.csv", zero_rows, file_fields)
    write_csv(OUT_DIR / "05_large_100mb_files.csv", large_rows, file_fields)
    write_csv(OUT_DIR / "06_small_1kb_or_less_files.csv", small_rows, file_fields)
    write_csv(OUT_DIR / "98_errors.csv", errors, ["path", "error", "traceback"])

    summary = make_summary(file_rows, top_rows, bucket_rows, plist_data, errors, snapshot_root)
    summary["started"] = started
    summary["finished"] = now()

    write_json(OUT_DIR / "99_workspace_summary.json", summary)
    write_text(OUT_DIR / "workspace_audit_summary.md", make_markdown(summary))

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
    print("output:", OUT_DIR)


if __name__ == "__main__":
    main()