# cross_0318_0401_logs_manifest.py
# -*- coding: utf-8 -*-
r"""
Public-safe reproducibility script.

Purpose:
  Cross-check two date-based iOS log folders against three iMazing / iOS backup
  workspace generations.

Default review use case:
  - 2026-03-18 log folder
  - 2026-04-01 log folder
  - 2026-03-18 backup workspace generation
  - 2026-04-01 backup workspace generation A
  - 2026-04-01 backup workspace generation B

The script tests:
  - repeated non-finalized backup-ledger / Snapshot state
  - Status.plist / Info.plist / Info.plist.tmp indicators
  - Snapshot bucket coverage
  - same-day conceptual platform-state layer overlap
  - compact log-manifest temporal proximity

Privacy:
  - No private path is hard-coded.
  - No raw log contents are exported.
  - Device identifiers and device names from plist output are redacted.
  - Absolute paths, UDID-like strings, MAC/BSSID-like values, and phone-like
    long digit strings are redacted in public text fields.

Safety:
  - Input folders are read-only.
  - No delete / move / modify / rename operation is performed.

Example:
  python cross_0318_0401_logs_manifest.py ^
    --log-0318 "X:\logs\2026\03\18" ^
    --log-0401 "X:\logs\2026\04\01" ^
    --manifest-0318 "X:\manifest\2026-03-18\iMazing\UDID" ^
    --manifest-0401-a "X:\manifest\2026-04-01-a\iMazing\UDID" ^
    --manifest-0401-b "X:\manifest\2026-04-01-b\iMazing\UDID" ^
    --out-dir ".\out_cross_0318_0401" ^
    --device-label "15G"
"""

from pathlib import Path
from collections import Counter, defaultdict
import argparse
import csv
import json
import plistlib
import hashlib
import gzip
import datetime as dt
import os
import re
import traceback


TEXT_SAMPLE_BYTES = 2 * 1024 * 1024
HASH_SAMPLE_BYTES = 1024 * 1024
HEX_BUCKETS = {f"{i:02x}" for i in range(256)}
SNAPSHOT_NAMES = {"Snapshot", "snapshot"}


CONCEPTUAL_LAYERS = {
    "account_state": [
        "appleid", "accountsd", "account", "akd", "authkit", "trusted",
        "trust", "securityd", "sfa", "sos", "pcs"
    ],
    "icloud_state": [
        "icloud", "cloudd", "cloudkit", "ckks", "ubiquity", "bird",
        "icloud drive", "cloudphotodb"
    ],
    "restriction_management_state": [
        "screentime", "managedsettings", "familycontrols", "contentprivacy",
        "dmd", "digitalhealth", "mdm", "remotemanagement",
        "managedappdistributiond", "profile", "configuration", "restriction",
        "managed"
    ],
    "backup_ledger_snapshot_state": [
        "backup", "snapshot", "manifest", "mobilebackup", "imazing",
        "status.plist", "info.plist", "rtc", "rtcreporting"
    ],
    "fileprovider_state": [
        "fileprovider", "fileproviderd", "document", "documents",
        "provider", "save"
    ],
    "telecom_context": [
        "commcenter", "baseband", "carrier", "sim", "esim", "plmn",
        "modem", "cellular", "lte", "nr", "rat", "telephony", "ims"
    ],
    "evidence_preservation_backup_storage_state": [
        "deleted", "logd", "analyticsd", "osanalytics", "storage", "disk",
        "space", "purge", "jetsam", "diskwrites", "cpu_resource"
    ],
    "orchestration_trigger_automation_state": [
        "shortcuts", "workflow", "automation", "reminder", "calendar",
        "homekit", "home", "duet", "coreduet", "trial", "triald",
        "backgroundtask", "notification", "push", "xpc", "launchd",
        "suggest", "suggestd", "parsecd", "searchd"
    ],
}

AUXILIARY_LAYERS = {
    "usage_state": [
        "usage", "usageclientid", "knowledgec", "biome", "appusage",
        "screen time", "xp_amp_app_usage"
    ]
}

ALL_LAYERS = {}
ALL_LAYERS.update(CONCEPTUAL_LAYERS)
ALL_LAYERS.update(AUXILIARY_LAYERS)


SENSITIVE_REGEXES = [
    (re.compile(r"\b[A-Z]:\\[^,\n\r\t ]*", re.IGNORECASE), "[REDACTED_PATH]"),
    (re.compile(r"0000[0-9A-Fa-f]{4}-[0-9A-Fa-f]{16}"), "[DEVICE_IDENTIFIER_REDACTED]"),
    (re.compile(r"\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b"), "[MAC_OR_BSSID_REDACTED]"),
    (re.compile(r"\b\+?\d{9,15}\b"), "[LONG_DIGIT_STRING_REDACTED]"),
]


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log-0318", required=True, help="2026-03-18 log folder")
    ap.add_argument("--log-0401", required=True, help="2026-04-01 log folder")
    ap.add_argument("--manifest-0318", required=True, help="2026-03-18 backup workspace root")
    ap.add_argument("--manifest-0401-a", required=True, help="2026-04-01 backup workspace root A")
    ap.add_argument("--manifest-0401-b", required=True, help="2026-04-01 backup workspace root B")
    ap.add_argument("--out-dir", required=True, help="Output folder")
    ap.add_argument("--device-label", default="15G")
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


def redact(value):
    s = "" if value is None else str(value)
    for rx, repl in SENSITIVE_REGEXES:
        s = rx.sub(repl, s)
    return s


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


def rel(root: Path, p: Path):
    try:
        return redact(str(p.relative_to(root)))
    except Exception:
        return redact(p.name)


def sha256_sample(p: Path):
    h = hashlib.sha256()
    try:
        with open(p, "rb") as f:
            h.update(f.read(HASH_SAMPLE_BYTES))
        return h.hexdigest()
    except Exception:
        return ""


def magic(p: Path):
    try:
        with open(p, "rb") as f:
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


def read_text_sample(p: Path):
    try:
        if p.suffix.lower() == ".gz":
            with gzip.open(p, "rb") as f:
                b = f.read(TEXT_SAMPLE_BYTES)
        else:
            with open(p, "rb") as f:
                b = f.read(TEXT_SAMPLE_BYTES)
    except Exception:
        return ""

    for enc in ("utf-8", "utf-16", "latin-1"):
        try:
            return b.decode(enc, errors="ignore")
        except Exception:
            pass

    return ""


def parse_dt_from_title(name):
    patterns = [
        r"(20\d{2})-(\d{2})-(\d{2})-(\d{2})(\d{2})(\d{2})",
        r"(20\d{2})_(\d{2})_(\d{2})_(\d{2})(\d{2})(\d{2})",
        r"(20\d{2})-(\d{2})-(\d{2})[ T_](\d{2})[:\-](\d{2})[:\-](\d{2})",
    ]

    for pat in patterns:
        m = re.search(pat, name)
        if not m:
            continue
        y, mo, d, hh, mi, ss = [int(x) for x in m.groups()]
        try:
            return dt.datetime(y, mo, d, hh, mi, ss)
        except Exception:
            return None

    return None


def parse_any_dt(v):
    if not v:
        return None

    s = str(v).strip()
    s = s.replace("T", " ").replace("Z", "")
    s = s.split("+")[0]

    for fmt in (
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
    ):
        try:
            return dt.datetime.strptime(s[:26], fmt)
        except Exception:
            pass

    return None


def minutes_delta(a, b):
    if not a or not b:
        return None
    return round((a - b).total_seconds() / 60.0, 2)


def normalize_log_title(name):
    s = name.lower()
    s = re.sub(r"20\d{2}[-_]\d{2}[-_]\d{2}[-_ ]?\d{6}", "[date-time]", s)
    s = re.sub(r"20\d{2}[-_]\d{2}[-_]\d{2}", "[date]", s)
    s = re.sub(r"iphone[0-9,]+", "[iphone-model]", s)
    return redact(s)


def layer_hits(text):
    low = text.lower()
    hits = {}

    for layer, patterns in ALL_LAYERS.items():
        matched = []
        count = 0
        for pat in patterns:
            p = pat.lower()
            if p in low:
                c = low.count(p)
                count += c
                matched.append(pat)
        hits[layer] = {
            "count": count,
            "matched": sorted(set(matched)),
        }

    return hits


def scan_logs(day_id, date_label, root: Path):
    rows = []
    errors = []

    if not root.exists():
        errors.append({
            "source": "log",
            "id": day_id,
            "path_public": f"[{day_id}_LOG_ROOT]",
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
                text = read_text_sample(p)
                combined = f"{p.name}\n{text}".lower()
                hits = layer_hits(combined)
                counts = {layer: obj["count"] for layer, obj in hits.items()}
                matched_layers = [layer for layer, c in counts.items() if c > 0]

                matched_keywords = []
                for layer, obj in hits.items():
                    for kw in obj["matched"]:
                        matched_keywords.append(f"{layer}:{kw}")

                title_dt = parse_dt_from_title(p.name)

                rows.append({
                    "day_id": day_id,
                    "date": date_label,
                    "idx": idx,
                    "relative_path": rel(root, p),
                    "original_title": redact(p.name),
                    "normalized_title": normalize_log_title(p.name),
                    "title_datetime": title_dt.isoformat(sep=" ") if title_dt else "",
                    "size_bytes": st["size_bytes"],
                    "mtime": st["mtime"],
                    "ctime": st["ctime"],
                    "extension": "".join(p.suffixes[-2:]).lower() if len(p.suffixes) >= 2 else p.suffix.lower(),
                    "magic": magic(p),
                    "sha256_sample_1mb": sha256_sample(p),
                    "matched_layer_count": len(matched_layers),
                    "matched_layers": "|".join(matched_layers),
                    "matched_keywords": redact("|".join(sorted(set(matched_keywords)))),
                    **{f"layer_{layer}": counts[layer] for layer in ALL_LAYERS.keys()},
                })

            except Exception as e:
                errors.append({
                    "source": "log",
                    "id": day_id,
                    "path_public": "[REDACTED_PATH]",
                    "error": repr(e),
                    "traceback": traceback.format_exc(limit=2),
                })

    return rows, errors


def snapshot_bucket(relative_path):
    parts = Path(relative_path).parts
    if len(parts) >= 2 and parts[0].lower() == "snapshot":
        return parts[1]
    return ""


def classify_manifest_file(p: Path, relative_path):
    n = p.name.lower()
    s = relative_path.lower()

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
    if "snapshot" in s:
        return "snapshot_file"
    if n.endswith("-wal") or n.endswith(".wal"):
        return "sqlite_wal"
    if n.endswith("-shm") or n.endswith(".shm"):
        return "sqlite_shm"
    return "other"


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
            "size_bytes": st["size_bytes"],
            "mtime": st["mtime"],
            "magic": magic(p),
            "parse_error": err,
        }

        if isinstance(obj, dict):
            for k in [
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
            ]:
                v = obj.get(k, "")
                if isinstance(v, (list, tuple, dict)):
                    v = len(v)
                if k == "Target Identifier" and v:
                    v = "[DEVICE_IDENTIFIER_REDACTED]"
                elif k in {"Device Name", "Display Name"} and v:
                    v = "[DEVICE_NAME_REDACTED]"
                else:
                    v = redact(v)
                row[k] = str(v)

        rows.append(row)

    return rows


def scan_manifest_generation(gen_id, date_label, label, root: Path):
    errors = []
    file_count = 0
    total_size = 0
    zero_files = 0
    snapshot_files = 0
    snapshot_size = 0
    snapshot_buckets = Counter()
    magic_counts = Counter()
    category_counts = Counter()

    if not root.exists():
        return {
            "gen_id": gen_id,
            "date": date_label,
            "label": label,
            "root_public": f"[{gen_id}_ROOT]",
            "root_exists": False,
            "total_files": 0,
            "total_size_bytes": 0,
            "total_size_gib": 0,
            "snapshot_files": 0,
            "snapshot_size_bytes": 0,
            "snapshot_size_gib": 0,
            "snapshot_hex_bucket_count": 0,
            "zero_byte_files": 0,
            "magic_counts": {},
            "category_counts": {},
            "errors": 1,
        }, [{
            "source": "manifest",
            "id": gen_id,
            "path_public": f"[{gen_id}_ROOT]",
            "error": "root_not_found",
            "traceback": "",
        }]

    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in {"$RECYCLE.BIN", "System Volume Information"}]

        for fn in fns:
            p = Path(dp) / fn
            try:
                st = safe_stat(p)
                rp = rel(root, p)
                bucket = snapshot_bucket(rp)
                mg = magic(p)
                cat = classify_manifest_file(p, rp)

                file_count += 1
                total_size += st["size_bytes"]
                zero_files += 1 if st["size_bytes"] == 0 else 0
                magic_counts[mg] += 1
                category_counts[cat] += 1

                if bucket:
                    snapshot_files += 1
                    snapshot_size += st["size_bytes"]
                    snapshot_buckets[bucket.lower()] += 1

            except Exception as e:
                errors.append({
                    "source": "manifest",
                    "id": gen_id,
                    "path_public": "[REDACTED_PATH]",
                    "error": repr(e),
                    "traceback": traceback.format_exc(limit=2),
                })

    return {
        "gen_id": gen_id,
        "date": date_label,
        "label": label,
        "root_public": f"[{gen_id}_ROOT]",
        "root_exists": True,
        "total_files": file_count,
        "total_size_bytes": total_size,
        "total_size_gib": round(total_size / (1024 ** 3), 4),
        "snapshot_files": snapshot_files,
        "snapshot_size_bytes": snapshot_size,
        "snapshot_size_gib": round(snapshot_size / (1024 ** 3), 4),
        "snapshot_hex_bucket_count": sum(1 for b in snapshot_buckets if b in HEX_BUCKETS),
        "zero_byte_files": zero_files,
        "magic_counts": dict(magic_counts),
        "category_counts": dict(category_counts),
        "errors": len(errors),
    }, errors


def manifest_core_states(plist_rows, manifest_summaries):
    by_gen_plists = defaultdict(list)
    for r in plist_rows:
        by_gen_plists[r["gen_id"]].append(r)

    by_gen_summary = {r["gen_id"]: r for r in manifest_summaries}
    rows = []

    for gen_id, plist_list in sorted(by_gen_plists.items()):
        status_rows = [r for r in plist_list if r["filename"].lower() in {"status.plist", "status.plist.backup"}]
        info_rows = [r for r in plist_list if r["filename"].lower() in {"info.plist", "info.plist.tmp"}]

        backup_state = ""
        snapshot_state = ""
        is_full = ""
        status_date = ""
        status_dt = None

        if status_rows:
            r = status_rows[0]
            backup_state = r.get("BackupState", "")
            snapshot_state = r.get("SnapshotState", "")
            is_full = r.get("IsFullBackup", "")
            status_date = r.get("Date", "")
            status_dt = parse_any_dt(status_date)

        info_tmp = "yes" if any(r["filename"].lower() == "info.plist.tmp" for r in info_rows) else "no"

        product_version = ""
        build_version = ""
        product_type = ""

        for r in info_rows:
            product_version = product_version or r.get("Product Version", "")
            build_version = build_version or r.get("Build Version", "")
            product_type = product_type or r.get("Product Type", "")

        s = by_gen_summary.get(gen_id, {})

        rows.append({
            "gen_id": gen_id,
            "date": s.get("date", ""),
            "label": s.get("label", ""),
            "snapshot_files": s.get("snapshot_files", 0),
            "snapshot_size_bytes": s.get("snapshot_size_bytes", 0),
            "snapshot_size_gib": s.get("snapshot_size_gib", 0),
            "snapshot_hex_bucket_count": s.get("snapshot_hex_bucket_count", 0),
            "total_files": s.get("total_files", 0),
            "total_size_gib": s.get("total_size_gib", 0),
            "BackupState": backup_state,
            "SnapshotState": snapshot_state,
            "IsFullBackup": is_full,
            "Status_Date": redact(status_date),
            "Status_Date_iso": status_dt.isoformat(sep=" ") if status_dt else "",
            "Info_plist_tmp": info_tmp,
            "Product_Version": product_version,
            "Build_Version": build_version,
            "Product_Type": product_type,
            "errors": s.get("errors", 0),
        })

    return rows


def summarize_log_layers(log_rows):
    acc = defaultdict(Counter)

    for r in log_rows:
        day = r["day_id"]
        for layer in ALL_LAYERS.keys():
            c = int(r.get(f"layer_{layer}", 0) or 0)
            if c > 0:
                acc[(day, layer)]["files_hit"] += 1
                acc[(day, layer)]["keyword_hits"] += c

    rows = []
    for (day, layer), c in sorted(acc.items()):
        rows.append({
            "day_id": day,
            "layer": layer,
            "conceptual_or_auxiliary": "conceptual" if layer in CONCEPTUAL_LAYERS else "auxiliary",
            "files_hit": c["files_hit"],
            "keyword_hits": c["keyword_hits"],
        })

    return rows


def common_log_titles(log_rows):
    by_title = defaultdict(set)
    examples = defaultdict(list)

    for r in log_rows:
        title = r["normalized_title"]
        by_title[title].add(r["day_id"])
        if len(examples[title]) < 5:
            examples[title].append(r["original_title"])

    rows = []
    for title, days in by_title.items():
        if "0318" in days and "0401" in days:
            rows.append({
                "normalized_title": title,
                "days": "|".join(sorted(days)),
                "example_titles": " || ".join(examples[title]),
            })

    rows.sort(key=lambda r: r["normalized_title"])
    return rows


def cross_window_hits(log_rows, manifest_core):
    rows = []

    for m in manifest_core:
        m_dt = parse_any_dt(m.get("Status_Date_iso") or m.get("Status_Date"))
        if not m_dt:
            continue

        for r in log_rows:
            if r.get("date") != m.get("date"):
                continue

            l_dt = parse_any_dt(r.get("title_datetime"))
            if not l_dt:
                continue

            delta = minutes_delta(l_dt, m_dt)
            if delta is None:
                continue

            abs_delta = abs(delta)

            if abs_delta <= 720 and int(r.get("matched_layer_count", 0) or 0) > 0:
                rows.append({
                    "gen_id": m["gen_id"],
                    "manifest_date": m["date"],
                    "manifest_status_date": m.get("Status_Date", ""),
                    "BackupState": m.get("BackupState", ""),
                    "SnapshotState": m.get("SnapshotState", ""),
                    "log_day_id": r["day_id"],
                    "log_title": r["original_title"],
                    "log_datetime": r["title_datetime"],
                    "delta_minutes_log_minus_manifest": delta,
                    "abs_delta_minutes": abs_delta,
                    "within_60m": abs_delta <= 60,
                    "within_180m": abs_delta <= 180,
                    "within_360m": abs_delta <= 360,
                    "matched_layer_count": r.get("matched_layer_count", 0),
                    "matched_layers": r.get("matched_layers", ""),
                    "size_bytes": r.get("size_bytes", ""),
                })

    rows.sort(key=lambda r: (r["gen_id"], r["abs_delta_minutes"], r["log_title"]))
    return rows


def layer_overlap_matrix(log_layer_rows):
    by_day = defaultdict(set)

    for r in log_layer_rows:
        if int(r.get("files_hit", 0) or 0) > 0:
            by_day[r["day_id"]].add(r["layer"])

    rows = []
    for layer in sorted(ALL_LAYERS.keys()):
        rows.append({
            "layer": layer,
            "conceptual_or_auxiliary": "conceptual" if layer in CONCEPTUAL_LAYERS else "auxiliary",
            "0318_present": layer in by_day.get("0318", set()),
            "0401_present": layer in by_day.get("0401", set()),
            "both_present": layer in by_day.get("0318", set()) and layer in by_day.get("0401", set()),
        })

    return rows


def alignment_score(manifest_core, log_layer_rows, window_rows):
    by_day_layers = defaultdict(set)

    for r in log_layer_rows:
        if int(r.get("files_hit", 0) or 0) > 0:
            by_day_layers[r["day_id"]].add(r["layer"])

    rows = []

    for m in manifest_core:
        day_id = "0318" if m["date"] == "2026-03-18" else "0401"
        layers = by_day_layers.get(day_id, set())
        conceptual_layers = {x for x in layers if x in CONCEPTUAL_LAYERS}
        auxiliary_layers = {x for x in layers if x in AUXILIARY_LAYERS}
        w = [r for r in window_rows if r["gen_id"] == m["gen_id"]]

        ledger_score = 0
        ledger_score += 1 if str(m.get("BackupState", "")).lower() == "empty" else 0
        ledger_score += 1 if str(m.get("SnapshotState", "")).lower() == "uploading" else 0
        ledger_score += 1 if str(m.get("IsFullBackup", "")).lower() == "true" else 0
        ledger_score += 1 if str(m.get("Info_plist_tmp", "")).lower() == "yes" else 0
        ledger_score += 1 if int(m.get("snapshot_hex_bucket_count", 0) or 0) == 256 else 0
        ledger_score += 1 if float(m.get("snapshot_size_gib", 0) or 0) > 1 else 0

        conceptual_layer_count = len(conceptual_layers)
        auxiliary_layer_count = len(auxiliary_layers)
        window_group_count = min(6, len(set(r["matched_layers"] for r in w if r["matched_layers"])))

        rough = ledger_score * 10 + conceptual_layer_count * 5 + window_group_count * 3

        rows.append({
            "gen_id": m["gen_id"],
            "date": m["date"],
            "ledger_score_0_6": ledger_score,
            "conceptual_layer_count_0_8": conceptual_layer_count,
            "auxiliary_layer_count": auxiliary_layer_count,
            "window_hit_groups_capped": window_group_count,
            "rough_alignment_score": rough,
            "BackupState": m.get("BackupState", ""),
            "SnapshotState": m.get("SnapshotState", ""),
            "snapshot_size_gib": m.get("snapshot_size_gib", ""),
            "snapshot_hex_bucket_count": m.get("snapshot_hex_bucket_count", ""),
            "conceptual_layers_present": "|".join(sorted(conceptual_layers)),
            "auxiliary_layers_present": "|".join(sorted(auxiliary_layers)),
            "interpretation": "higher means stronger log-manifest same-day coupling; not proof of compromise",
        })

    return rows


def make_markdown(device_label, manifest_core, overlap_rows, score_rows):
    lines = []

    lines.append("# 2026-03-18 / 2026-04-01 Log-Manifest Cross Validation")
    lines.append("")
    lines.append(f"- device label: `{device_label}`")
    lines.append("- raw log contents exported: `false`")
    lines.append("- private full paths exported: `false`")
    lines.append("- device identifiers exported: `false`")
    lines.append("- device names exported: `false`")
    lines.append("")

    lines.append("## Manifest core states")
    lines.append("")
    for r in manifest_core:
        lines.append(f"### {r['gen_id']} / {r['date']}")
        lines.append(f"- Snapshot files: `{r['snapshot_files']}`")
        lines.append(f"- Snapshot size GiB: `{r['snapshot_size_gib']}`")
        lines.append(f"- Snapshot hex bucket count: `{r['snapshot_hex_bucket_count']}`")
        lines.append(f"- BackupState: `{r['BackupState']}`")
        lines.append(f"- SnapshotState: `{r['SnapshotState']}`")
        lines.append(f"- IsFullBackup: `{r['IsFullBackup']}`")
        lines.append(f"- Info.plist.tmp: `{r['Info_plist_tmp']}`")
        lines.append(f"- errors: `{r['errors']}`")
        lines.append("")

    lines.append("## Conceptual layer overlap")
    lines.append("")
    for r in overlap_rows:
        if r["conceptual_or_auxiliary"] == "conceptual" and str(r["both_present"]).lower() == "true":
            lines.append(f"- `{r['layer']}`")
    lines.append("")

    lines.append("## Alignment scores")
    lines.append("")
    for r in score_rows:
        lines.append(
            f"- `{r['gen_id']}`: score `{r['rough_alignment_score']}`, "
            f"ledger `{r['ledger_score_0_6']}/6`, "
            f"conceptual layers `{r['conceptual_layer_count_0_8']}/8"
        )
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

    log_specs = [
        ("0318", "2026-03-18", Path(args.log_0318)),
        ("0401", "2026-04-01", Path(args.log_0401)),
    ]

    manifest_specs = [
        ("0318_main", "2026-03-18", "2026-03-18 main generation", Path(args.manifest_0318)),
        ("0401_a", "2026-04-01", "2026-04-01 generation A", Path(args.manifest_0401_a)),
        ("0401_b", "2026-04-01", "2026-04-01 generation B", Path(args.manifest_0401_b)),
    ]

    source_rows = []
    errors = []
    all_logs = []
    all_plists = []
    manifest_summaries = []

    for day_id, date_label, root in log_specs:
        source_rows.append({
            "type": "log",
            "id": day_id,
            "date": date_label,
            "path_public": f"[{day_id}_LOG_ROOT]",
            "exists": root.exists(),
        })

        rows, errs = scan_logs(day_id, date_label, root)
        all_logs.extend(rows)
        errors.extend(errs)

    for gen_id, date_label, label, root in manifest_specs:
        source_rows.append({
            "type": "manifest",
            "id": gen_id,
            "date": date_label,
            "path_public": f"[{gen_id}_ROOT]",
            "exists": root.exists(),
        })

        summary, errs = scan_manifest_generation(gen_id, date_label, label, root)
        manifest_summaries.append(summary)
        errors.extend(errs)
        all_plists.extend(scan_plists(gen_id, root))

    manifest_core = manifest_core_states(all_plists, manifest_summaries)
    log_layer_rows = summarize_log_layers(all_logs)
    common_titles = common_log_titles(all_logs)
    window_rows = cross_window_hits(all_logs, manifest_core)
    overlap_rows = layer_overlap_matrix(log_layer_rows)
    score_rows = alignment_score(manifest_core, log_layer_rows, window_rows)

    source_fields = ["type", "id", "date", "path_public", "exists"]

    log_fields = [
        "day_id", "date", "idx", "relative_path", "original_title",
        "normalized_title", "title_datetime", "size_bytes", "mtime", "ctime",
        "extension", "magic", "sha256_sample_1mb", "matched_layer_count",
        "matched_layers", "matched_keywords",
    ] + [f"layer_{layer}" for layer in ALL_LAYERS.keys()]

    manifest_summary_fields = [
        "gen_id", "date", "label", "root_public", "root_exists",
        "total_files", "total_size_bytes", "total_size_gib",
        "snapshot_files", "snapshot_size_bytes", "snapshot_size_gib",
        "snapshot_hex_bucket_count", "zero_byte_files",
        "magic_counts", "category_counts", "errors"
    ]

    plist_fields = [
        "gen_id", "relative_path", "filename", "size_bytes", "mtime", "magic",
        "parse_error", "BackupState", "SnapshotState", "IsFullBackup", "Date",
        "Last Backup Date", "Product Version", "Build Version", "Product Type",
        "Target Identifier", "Device Name", "Display Name",
        "Installed Applications", "iTunes Version"
    ]

    manifest_core_fields = [
        "gen_id", "date", "label", "snapshot_files", "snapshot_size_bytes",
        "snapshot_size_gib", "snapshot_hex_bucket_count", "total_files",
        "total_size_gib", "BackupState", "SnapshotState", "IsFullBackup",
        "Status_Date", "Status_Date_iso", "Info_plist_tmp", "Product_Version",
        "Build_Version", "Product_Type", "errors"
    ]

    log_layer_fields = [
        "day_id", "layer", "conceptual_or_auxiliary", "files_hit", "keyword_hits"
    ]

    common_fields = ["normalized_title", "days", "example_titles"]

    window_fields = [
        "gen_id", "manifest_date", "manifest_status_date", "BackupState",
        "SnapshotState", "log_day_id", "log_title", "log_datetime",
        "delta_minutes_log_minus_manifest", "abs_delta_minutes",
        "within_60m", "within_180m", "within_360m",
        "matched_layer_count", "matched_layers", "size_bytes"
    ]

    overlap_fields = [
        "layer", "conceptual_or_auxiliary", "0318_present", "0401_present", "both_present"
    ]

    score_fields = [
        "gen_id", "date", "ledger_score_0_6", "conceptual_layer_count_0_8",
        "auxiliary_layer_count", "window_hit_groups_capped",
        "rough_alignment_score", "BackupState", "SnapshotState",
        "snapshot_size_gib", "snapshot_hex_bucket_count",
        "conceptual_layers_present", "auxiliary_layers_present", "interpretation"
    ]

    error_fields = ["source", "id", "path_public", "error", "traceback"]

    write_csv(out_dir / "00_source_existence.csv", source_rows, source_fields)
    write_csv(out_dir / "01_log_file_index.csv", all_logs, log_fields)
    write_csv(out_dir / "02_manifest_generation_summary.csv", manifest_summaries, manifest_summary_fields)
    write_csv(out_dir / "03_plist_status_info.csv", all_plists, plist_fields)
    write_csv(out_dir / "04_manifest_core_states.csv", manifest_core, manifest_core_fields)
    write_csv(out_dir / "05_log_layer_counts_by_day.csv", log_layer_rows, log_layer_fields)
    write_csv(out_dir / "06_common_log_titles_0318_0401.csv", common_titles, common_fields)
    write_csv(out_dir / "07_manifest_log_window_hits.csv", window_rows, window_fields)
    write_csv(out_dir / "08_layer_overlap_matrix.csv", overlap_rows, overlap_fields)
    write_csv(out_dir / "09_alignment_score.csv", score_rows, score_fields)
    write_csv(out_dir / "98_errors.csv", errors, error_fields)

    final_summary = {
        "script": "cross_0318_0401_logs_manifest.py",
        "generated_at": now(),
        "device_label": args.device_label,
        "input_policy": "read_only",
        "raw_log_content_exported": False,
        "private_full_paths_exported": False,
        "device_identifier_exported": False,
        "device_name_exported": False,
        "source_summary": source_rows,
        "log_files_indexed": len(all_logs),
        "manifest_generations_indexed": len(manifest_summaries),
        "manifest_core": manifest_core,
        "conceptual_layers": list(CONCEPTUAL_LAYERS.keys()),
        "auxiliary_layers": list(AUXILIARY_LAYERS.keys()),
        "log_layer_rows": len(log_layer_rows),
        "common_log_title_count": len(common_titles),
        "cross_window_hit_count": len(window_rows),
        "layer_overlap": overlap_rows,
        "alignment_scores": score_rows,
        "errors": len(errors),
        "interpretation_boundary": {
            "not_proof_of_compromise": True,
            "not_attribution": True,
            "not_vendor_causation": True,
            "not_hidden_mdm_confirmation": True,
            "not_baseband_compromise": True,
            "not_sim_compromise": True,
            "not_otp_interception": True,
        },
    }

    write_json(out_dir / "99_cross_summary.json", final_summary)
    write_text(out_dir / "cross_summary.md", make_markdown(args.device_label, manifest_core, overlap_rows, score_rows))

    print("complete")
    print("out:", out_dir)
    print("log_files_indexed:", len(all_logs))
    print("manifest_generations:", len(manifest_summaries))
    print("cross_window_hits:", len(window_rows))
    print("errors:", len(errors))
    for r in score_rows:
        print(
            r["gen_id"],
            "ledger",
            r["ledger_score_0_6"],
            "conceptual_layers",
            r["conceptual_layer_count_0_8"],
            "score",
            r["rough_alignment_score"],
        )


if __name__ == "__main__":
    main()
