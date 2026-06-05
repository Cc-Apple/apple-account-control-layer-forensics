# scan_0401_two_snapshots.py
# -*- coding: utf-8 -*-
r"""
Public-safe reproducibility script.

Purpose:
  Scan two iMazing / iOS backup workspace generations for a given date and
  compare Snapshot / backup-ledger state.

Default use case:
  2026-04-01 15G two-generation Snapshot / backup-ledger anchor.

Privacy:
  - No private path is hard-coded.
  - No raw file contents are exported.
  - Device identifiers and device names are redacted from plist-derived output.

Safety:
  - Input folders are read-only.
  - No delete / move / modify / rename operation is performed.

Example:
  python scan_0401_two_snapshots.py ^
    --gen-a "X:\path\to\first\iMazing\UDID" ^
    --gen-b "X:\path\to\second\iMazing\UDID" ^
    --out-dir ".\out_0401_scan" ^
    --device-label "15G" ^
    --core-date "2026-04-01"
"""

from pathlib import Path
from collections import Counter, defaultdict
import argparse
import csv
import json
import plistlib
import hashlib
import datetime as dt
import os
import traceback


HEX_BUCKETS = {f"{i:02x}" for i in range(256)}
SAMPLE_BYTES = 1024 * 1024
SNAPSHOT_NAMES = {"Snapshot", "snapshot"}


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen-a", required=True, help="First backup workspace root")
    ap.add_argument("--gen-b", required=True, help="Second backup workspace root")
    ap.add_argument("--out-dir", required=True, help="Output directory")
    ap.add_argument("--device-label", default="15G")
    ap.add_argument("--core-date", default="2026-04-01")
    return ap.parse_args()


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


def rel(root: Path, p: Path):
    try:
        return str(p.relative_to(root))
    except Exception:
        return p.name


def safe_stat(p: Path):
    try:
        st = p.stat()
        return {
            "size_bytes": st.st_size,
            "mtime": dt.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
            "ctime": dt.datetime.fromtimestamp(st.st_ctime).isoformat(timespec="seconds"),
        }
    except Exception:
        return {"size_bytes": 0, "mtime": "", "ctime": ""}


def sha256_sample(p: Path):
    h = hashlib.sha256()
    try:
        with open(p, "rb") as f:
            h.update(f.read(SAMPLE_BYTES))
        return h.hexdigest()
    except Exception:
        return ""


def magic(p: Path):
    try:
        b = p.read_bytes()[:64]
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


def classify(p: Path):
    n = p.name.lower()
    s = str(p).lower()

    if n == "manifest.db":
        return "manifest_db"
    if n == "manifest.plist":
        return "manifest_plist"
    if n == "status.plist":
        return "status_plist"
    if n == "status.plist.backup":
        return "status_plist_backup"
    if n == "info.plist":
        return "info_plist"
    if n == "info.plist.tmp":
        return "info_plist_tmp"
    if "photos.sqlite" in n:
        return "photos_sqlite"
    if n.endswith("-wal") or n.endswith(".wal"):
        return "sqlite_wal"
    if n.endswith("-shm") or n.endswith(".shm"):
        return "sqlite_shm"
    if "snapshot" in s:
        return "snapshot_file"
    return "other"


def snapshot_bucket(relative_path):
    parts = Path(relative_path).parts
    if len(parts) >= 2 and parts[0].lower() == "snapshot":
        return parts[1]
    return ""


def parse_plist(p: Path):
    try:
        with open(p, "rb") as f:
            obj = plistlib.load(f)
        return obj, ""
    except Exception as e:
        return None, repr(e)


def scan_plists(gen_id, root: Path):
    rows = []
    targets = {"status.plist", "status.plist.backup", "info.plist", "info.plist.tmp", "manifest.plist"}

    if not root.exists():
        return rows

    for p in sorted(root.rglob("*"), key=lambda x: str(x).lower()):
        if not p.is_file() or p.name.lower() not in targets:
            continue

        st = safe_stat(p)
        obj, err = parse_plist(p)

        row = {
            "gen_id": gen_id,
            "relative_path": rel(root, p),
            "filename": p.name,
            "category": classify(p),
            "size_bytes": st["size_bytes"],
            "mtime": st["mtime"],
            "magic": magic(p),
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
                if k in {"Device Name", "Display Name"} and v:
                    v = "[DEVICE_NAME_REDACTED]"
                row[k] = str(v)

        rows.append(row)

    return rows


def scan_files(gen_id, label, root: Path):
    rows = []
    errors = []

    if not root.exists():
        errors.append({
            "gen_id": gen_id,
            "path_public": f"[{gen_id}_ROOT]",
            "error": "root_not_found",
            "traceback": "",
        })
        return rows, errors

    idx = 0

    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in {"$RECYCLE.BIN", "System Volume Information"}]

        for fn in fns:
            idx += 1
            p = Path(dp) / fn
            try:
                st = safe_stat(p)
                rp = rel(root, p)
                bucket = snapshot_bucket(rp)
                top = Path(rp).parts[0] if Path(rp).parts else ""

                rows.append({
                    "gen_id": gen_id,
                    "label": label,
                    "idx": idx,
                    "relative_path": rp,
                    "top_level": top,
                    "snapshot_bucket": bucket,
                    "is_hex_bucket": bucket.lower() in HEX_BUCKETS if bucket else False,
                    "filename": p.name,
                    "extension": p.suffix.lower(),
                    "category": classify(p),
                    "size_bytes": st["size_bytes"],
                    "mtime": st["mtime"],
                    "ctime": st["ctime"],
                    "is_zero_byte": st["size_bytes"] == 0,
                    "is_small_1kb_or_less": st["size_bytes"] <= 1024,
                    "is_large_1mb_or_more": st["size_bytes"] >= 1024 * 1024,
                    "is_large_100mb_or_more": st["size_bytes"] >= 100 * 1024 * 1024,
                    "magic": magic(p),
                    "sha256_sample_1mb": sha256_sample(p),
                })

            except Exception as e:
                errors.append({
                    "gen_id": gen_id,
                    "path_public": "[REDACTED_PATH]",
                    "error": repr(e),
                    "traceback": traceback.format_exc(limit=2),
                })

    return rows, errors


def summarize_generation(gen_id, label, file_rows, plist_rows, errors):
    rows = [r for r in file_rows if r["gen_id"] == gen_id]
    plists = [r for r in plist_rows if r["gen_id"] == gen_id]

    snapshot_rows = [r for r in rows if str(r["top_level"]).lower() == "snapshot"]
    buckets = {r["snapshot_bucket"].lower() for r in snapshot_rows if r["snapshot_bucket"]}

    status_rows = [r for r in plists if r["filename"].lower() in {"status.plist", "status.plist.backup"}]
    info_rows = [r for r in plists if r["filename"].lower() in {"info.plist", "info.plist.tmp"}]

    backup_state = ""
    snapshot_state = ""
    is_full = ""
    status_date = ""

    if status_rows:
        r = status_rows[0]
        backup_state = r.get("BackupState", "")
        snapshot_state = r.get("SnapshotState", "")
        is_full = r.get("IsFullBackup", "")
        status_date = r.get("Date", "")

    info_tmp = "yes" if any(r["filename"].lower() == "info.plist.tmp" for r in info_rows) else "no"

    product_version = ""
    build_version = ""
    product_type = ""

    for r in info_rows:
        product_version = product_version or r.get("Product Version", "")
        build_version = build_version or r.get("Build Version", "")
        product_type = product_type or r.get("Product Type", "")

    return {
        "gen_id": gen_id,
        "label": label,
        "root_public": f"[{gen_id}_ROOT]",
        "total_files": len(rows),
        "total_size_bytes": sum(int(r["size_bytes"]) for r in rows),
        "total_size_gib": round(sum(int(r["size_bytes"]) for r in rows) / (1024 ** 3), 4),
        "snapshot_files": len(snapshot_rows),
        "snapshot_size_bytes": sum(int(r["size_bytes"]) for r in snapshot_rows),
        "snapshot_size_gib": round(sum(int(r["size_bytes"]) for r in snapshot_rows) / (1024 ** 3), 4),
        "snapshot_hex_bucket_count": sum(1 for b in buckets if b in HEX_BUCKETS),
        "zero_byte_files": sum(1 for r in rows if str(r["is_zero_byte"]).lower() == "true"),
        "small_1kb_or_less": sum(1 for r in rows if str(r["is_small_1kb_or_less"]).lower() == "true"),
        "large_1mb_or_more": sum(1 for r in rows if str(r["is_large_1mb_or_more"]).lower() == "true"),
        "large_100mb_or_more": sum(1 for r in rows if str(r["is_large_100mb_or_more"]).lower() == "true"),
        "plist_rows": len(plists),
        "BackupState": backup_state,
        "SnapshotState": snapshot_state,
        "IsFullBackup": is_full,
        "Status_Date": status_date,
        "Info_plist_tmp": info_tmp,
        "Product_Version": product_version,
        "Build_Version": build_version,
        "Product_Type": product_type,
        "errors": len([e for e in errors if e["gen_id"] == gen_id]),
    }


def bucket_summary(file_rows):
    acc = {}

    for r in file_rows:
        b = r.get("snapshot_bucket", "")
        if not b:
            continue

        key = (r["gen_id"], b)
        if key not in acc:
            acc[key] = {
                "gen_id": r["gen_id"],
                "bucket": b,
                "is_hex_bucket": b.lower() in HEX_BUCKETS,
                "file_count": 0,
                "total_size_bytes": 0,
                "zero_byte_files": 0,
                "magic_counts": Counter(),
                "category_counts": Counter(),
            }

        x = acc[key]
        x["file_count"] += 1
        x["total_size_bytes"] += int(r["size_bytes"])
        x["zero_byte_files"] += 1 if str(r["is_zero_byte"]).lower() == "true" else 0
        x["magic_counts"][r["magic"]] += 1
        x["category_counts"][r["category"]] += 1

    out = []
    for x in acc.values():
        out.append({
            "gen_id": x["gen_id"],
            "bucket": x["bucket"],
            "is_hex_bucket": x["is_hex_bucket"],
            "file_count": x["file_count"],
            "total_size_bytes": x["total_size_bytes"],
            "total_size_gib": round(x["total_size_bytes"] / (1024 ** 3), 4),
            "zero_byte_files": x["zero_byte_files"],
            "magic_counts": json.dumps(dict(x["magic_counts"]), ensure_ascii=False),
            "category_counts": json.dumps(dict(x["category_counts"]), ensure_ascii=False),
        })

    out.sort(key=lambda r: (r["gen_id"], r["bucket"]))
    return out


def cross_generation_summary(file_rows):
    by_rel = defaultdict(dict)
    for r in file_rows:
        by_rel[r["relative_path"]][r["gen_id"]] = r

    gen_ids = sorted(set(r["gen_id"] for r in file_rows))
    if len(gen_ids) != 2:
        return []

    a, b = gen_ids
    total = len(by_rel)
    both = sum(1 for v in by_rel.values() if a in v and b in v)
    only_a = sum(1 for v in by_rel.values() if a in v and b not in v)
    only_b = sum(1 for v in by_rel.values() if b in v and a not in v)
    same_size = sum(
        1 for v in by_rel.values()
        if a in v and b in v and int(v[a]["size_bytes"]) == int(v[b]["size_bytes"])
    )
    same_sample_hash = sum(
        1 for v in by_rel.values()
        if a in v and b in v and v[a]["sha256_sample_1mb"] == v[b]["sha256_sample_1mb"]
    )

    return [
        {"metric": "relative_paths_total", "value": total},
        {"metric": "both_generations", "value": both},
        {"metric": f"{a}_only", "value": only_a},
        {"metric": f"{b}_only", "value": only_b},
        {"metric": "same_size", "value": same_size},
        {"metric": "same_sample_hash", "value": same_sample_hash},
    ]


def make_markdown(device_label, core_date, gen_summaries):
    lines = []
    lines.append("# Two-Generation Snapshot / Backup-Ledger Scan")
    lines.append("")
    lines.append(f"- device label: `{device_label}`")
    lines.append(f"- core date: `{core_date}`")
    lines.append("- raw file contents exported: `false`")
    lines.append("- private paths exported: `false`")
    lines.append("")

    for g in gen_summaries:
        lines.append(f"## {g['gen_id']} / {g['label']}")
        lines.append("")
        lines.append(f"- Snapshot files: `{g['snapshot_files']}`")
        lines.append(f"- Snapshot size GiB: `{g['snapshot_size_gib']}`")
        lines.append(f"- Snapshot hex bucket count: `{g['snapshot_hex_bucket_count']}`")
        lines.append(f"- BackupState: `{g['BackupState']}`")
        lines.append(f"- SnapshotState: `{g['SnapshotState']}`")
        lines.append(f"- IsFullBackup: `{g['IsFullBackup']}`")
        lines.append(f"- Info.plist.tmp: `{g['Info_plist_tmp']}`")
        lines.append(f"- errors: `{g['errors']}`")
        lines.append("")

    lines.append("## Boundary")
    lines.append("")
    lines.append("This script supports reproducibility of the structure-level review.")
    lines.append("It does not prove compromise, attribution, vendor causation, hidden MDM, baseband compromise, SIM compromise, OTP interception, payload, malware, or C2.")
    lines.append("")
    return "\n".join(lines)


def main():
    args = parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    gens = [
        {"gen_id": "gen_a", "label": "generation_a", "root": Path(args.gen_a)},
        {"gen_id": "gen_b", "label": "generation_b", "root": Path(args.gen_b)},
    ]

    all_files = []
    all_plists = []
    all_errors = []

    for g in gens:
        files, errors = scan_files(g["gen_id"], g["label"], g["root"])
        plists = scan_plists(g["gen_id"], g["root"])

        all_files.extend(files)
        all_plists.extend(plists)
        all_errors.extend(errors)

    gen_summaries = [
        summarize_generation(g["gen_id"], g["label"], all_files, all_plists, all_errors)
        for g in gens
    ]

    buckets = bucket_summary(all_files)
    cross = cross_generation_summary(all_files)

    file_fields = [
        "gen_id", "label", "idx", "relative_path", "top_level", "snapshot_bucket",
        "is_hex_bucket", "filename", "extension", "category", "size_bytes",
        "mtime", "ctime", "is_zero_byte", "is_small_1kb_or_less",
        "is_large_1mb_or_more", "is_large_100mb_or_more", "magic",
        "sha256_sample_1mb"
    ]

    plist_fields = [
        "gen_id", "relative_path", "filename", "category", "size_bytes",
        "mtime", "magic", "parse_error", "BackupState", "SnapshotState",
        "IsFullBackup", "Date", "Last Backup Date", "Product Version",
        "Build Version", "Product Type", "Target Identifier", "Device Name",
        "Display Name", "Installed Applications", "iTunes Version"
    ]

    bucket_fields = [
        "gen_id", "bucket", "is_hex_bucket", "file_count", "total_size_bytes",
        "total_size_gib", "zero_byte_files", "magic_counts", "category_counts"
    ]

    gen_fields = list(gen_summaries[0].keys())
    cross_fields = ["metric", "value"]

    write_csv(out_dir / "01_file_inventory.csv", all_files, file_fields)
    write_csv(out_dir / "02_plist_status_info.csv", all_plists, plist_fields)
    write_csv(out_dir / "03_snapshot_bucket_summary.csv", buckets, bucket_fields)
    write_csv(out_dir / "04_generation_summary.csv", gen_summaries, gen_fields)
    write_csv(out_dir / "05_cross_generation_summary.csv", cross, cross_fields)
    write_csv(out_dir / "98_errors.csv", all_errors, ["gen_id", "path_public", "error", "traceback"])

    summary = {
        "script": "scan_0401_two_snapshots.py",
        "generated_at": now(),
        "device_label": args.device_label,
        "core_date": args.core_date,
        "input_policy": "read_only",
        "raw_file_contents_exported": False,
        "private_paths_exported": False,
        "device_identifiers_exported": False,
        "device_names_exported": False,
        "generation_summary": gen_summaries,
        "cross_generation_summary": cross,
        "errors": len(all_errors),
    }

    write_json(out_dir / "99_scan_summary.json", summary)
    write_text(out_dir / "scan_summary.md", make_markdown(args.device_label, args.core_date, gen_summaries))

    print("complete")
    print("out:", out_dir)
    for g in gen_summaries:
        print(g["gen_id"], g["snapshot_files"], g["snapshot_size_gib"], g["BackupState"], g["SnapshotState"])


if __name__ == "__main__":
    main()
