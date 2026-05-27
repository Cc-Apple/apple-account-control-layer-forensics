# -*- coding: utf-8 -*-
r"""
ttp_2026_05_3devices.py

目的:
  2026-05 の 12G / 15G / iPhone11Pro ログに対して、
  TTP思想照合・構造照合・通常解釈ストレス解析を1回で実行する。

入力:
  C:\Users\Administrator\Desktop\05\12G
  C:\Users\Administrator\Desktop\05\15G
  C:\Users\Administrator\Desktop\05\iPhone11Pro

出力:
  C:\Users\Administrator\Desktop\05\Result\TTP_2026_05_3DEV_日時

重要:
  入力は読むだけ。
  削除なし。
  修正なし。
  リネームなし。
  移動なし。
  上書きなし。
"""

import os
import re
import csv
import json
import zipfile
import hashlib
from pathlib import Path
from datetime import datetime, date
from collections import defaultdict, Counter

RUN_DATE = datetime.now().strftime("%Y-%m-%d-%H%M%S")

ROOTS = [
    ("12G", Path(r"C:\Users\Administrator\Desktop\05\12G")),
    ("15G", Path(r"C:\Users\Administrator\Desktop\05\15G")),
    ("iPhone11Pro", Path(r"C:\Users\Administrator\Desktop\05\iPhone11Pro")),
]

OUT = Path(r"C:\Users\Administrator\Desktop\05\Result") / ("TTP_2026_05_3DEV_" + RUN_DATE)

START_DATE = date(2026, 5, 1)
END_DATE = date(2026, 5, 31)

MAX_READ_HEAD = 3_000_000
MAX_READ_TAIL = 2_000_000

APPLE_RAW_EXT = [
    ".ips", ".ca.synced", ".synced", ".plist", ".json",
    ".session", ".log", ".panic", ".crash"
]

TEXT_EXT = [".txt", ".md", ".csv"]

STRICT_EXCLUDE_TERMS = [
    "manifest.db", "manifest.plist", "status.plist", "info.plist", "ddnabackup.plist",
    "auto_final_report", "final_report", "summary", "machine_summary", "human_summary",
    "one_page", "readme", "evidence_index", "sha256_index", "hash_index",
    "github", "mega", "megashare", "ocr", "excerpt", "top12", "top_12",
    "note", "notes", "memo", "要約", "抽出", "比較結果",
    "result", "_combined", "ttp_result", "desktop.ini"
]

DEBUG_EXCLUDE_TERMS = [
    "sysdiagnose", ".tar.gz", ".gz", "stacks", "tailspin",
    "microstackshots", ".spin", "stackshot"
]

APPLE_FAMILIES = [
    "Analytics", "JetsamEvent", "SiriSearchFeedback",
    "RTCReporting_messageLog", "RTCReporting",
    "xp_amp_app_usage_dnu",
    "CommCenter", "Baseband",
    "ScreenTimeAgent",
    "ManagedSettingsAgent", "ManagedSettingsSubscriber", "ManagedSettings",
    "managedappdistributiond",
    "remotemanagementd", "RemoteManagementAgent",
    "SFA-networking", "SFA-CloudServices", "SFA-ckks",
    "SFA-local", "SFA-pcs", "SFA-sos",
    "LowBatteryLog", "WiFiConnectionQuality",
    "signpost_reporter", "proactive_event_tracker",
    "deleted", "searchd", "cloudd", "triald", "analyticsd",
    "duetexpertd", "parsecd", "suggestd", "backupd", "logd",
    "SaveToFiles", "maild", "amfid", "contactsd", "FaceTime",
    "Preferences", "assetsd", "biomed",
    "WeChat", "Facebook", "Binance"
]

TERMS = {
    "mdm_false": [
        "mdmstatus\":false", "mdmstatus = false", "mdmstatus:false",
        "ismdmenrolled\":false", "ismdmenrolled = false",
        "issupervised\":false", "issupervised = false",
        "isuserenrollment\":false", "isuserenrollment = false",
        "isdep\":false", "isdep = false"
    ],
    "mdm_true": [
        "mdmstatus\":true", "mdmstatus = true", "mdmstatus:true",
        "ismdmenrolled\":true", "issupervised\":true",
        "isuserenrollment\":true", "isdep\":true"
    ],
    "restriction_management": [
        "screentimeagent", "screentime",
        "managedsettingsagent", "managedsettingssubscriber", "managedsettings",
        "managedappdistributiond", "remotemanagementd", "remotemanagementagent",
        "remotemanagement", "familycontrols", "contentprivacy",
        "contentandprivacy", "restrictionsprofile", "gamecenter"
    ],
    "account_cloud": [
        "appleid", "apple id", "icloud", "cloudkit", "ckks",
        "cloudservices", "sfa", "authkit", "akfollowup", "lockdown",
        "trusted", "trust", "mobileidentity", "transparency",
        "keychain", "pcs", "sos"
    ],
    "telecom_proximity": [
        "commcenter", "commcentermobilehelper", "baseband",
        "basebandpowercycle", "simtransfer", "imsi", "plmn",
        "mcc", "mnc", "carrier", "cellularmcc", "cellularmnc",
        "l2report_cellularmcc", "l2report_cellularmnc",
        "privacyproxy", "pdp_ip0", "nearbyd", "nearby",
        "rapportd", "sharingd", "bluetooth", "bluetoothdiscovery",
        "awdl", "wificonnectionquality", "bssid", "rssi"
    ],
    "usage_state": [
        "usageclientid", "usage_client_id", "xp_amp_app_usage",
        "xp_amp_app_usage_dnu", "rtcreporting", "rtcreporting_messagelog",
        "clientid", "appusage"
    ],
    "daemon_repetition": [
        "deleted", "searchd", "cloudd", "triald", "analyticsd",
        "duetexpertd", "coreduetd", "suggestd", "parsecd", "pasted",
        "logd", "backupd", "runningboardd", "symptomsd", "assetsd",
        "biomed", "dasd", "spotlightknowledged", "photoanalysisd"
    ],
    "evidence_interference": [
        "savetofiles", "searchd", "maild", "amfid", "deleted",
        "backupd", "logd", "memory pressure", "memorypressure",
        "diskwrites", "cpu_resource", "out-of-budget", "watchdog",
        "reset", "thermal", "assertionfailure"
    ],
    "seam_failure": [
        "exc_crash", "exc_breakpoint", "exc_bad_access", "sigabrt",
        "sigtrap", "sigsegv", "abort trap", "trace/bpt trap",
        "assertionfailure", "nsassertionhandler", "out-of-budget",
        "memorypressure", "basebandpowercycle", "commcenterimsiswitchevent",
        "cellularmcc", "cellularmnc", "l2report_cellularmcc", "l2report_cellularmnc"
    ],
    "financial_strict": [
        "standard chartered", "binance", "com.binance", "otp",
        "re-auth", "reauth", "re authentication", "re-authentication",
        "device changed", "device change", "device trust", "trusted device"
    ],
}

TS_PATTERNS = [
    re.compile(r"(20\d{2})[-_.](\d{2})[-_.](\d{2})[T_ -]?(\d{2})?[:\-]?(\d{2})?[:\-]?(\d{2})?"),
    re.compile(r"(20\d{2})(\d{2})(\d{2})[_-]?(\d{2})?(\d{2})?(\d{2})?")
]

def low(s):
    return str(s).lower()

def safe_print(s):
    try:
        print(s)
    except Exception:
        print(str(s).encode("utf-8", "replace").decode("utf-8", "replace"))

def sha256_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def has_any(name, terms):
    n = low(name)
    return any(t in n for t in terms)

def is_debug_excluded(name):
    return has_any(name, DEBUG_EXCLUDE_TERMS)

def is_strict_excluded(name):
    return has_any(name, STRICT_EXCLUDE_TERMS)

def infer_family(name):
    n = low(name)
    for fam in APPLE_FAMILIES:
        if fam.lower() in n:
            return fam
    base = os.path.basename(str(name))
    return re.split(r"[-_.]", base)[0][:80]

def is_apple_family(name):
    n = low(name)
    return any(fam.lower() in n for fam in APPLE_FAMILIES)

def classify_source_type(name):
    n = low(name)

    if "sirisearchfeedback" in n:
        return "siri_feedback", 0.25

    if "rtcreporting_messagelog" in n or "rtcreporting" in n:
        return "rtc_reporting", 0.70

    if n.endswith(".txt") or n.endswith(".md") or n.endswith(".csv"):
        if is_apple_family(n):
            return "apple_text_family_low_weight", 0.35
        return "text_export_non_primary", 0.0

    if any(n.endswith(ext) for ext in APPLE_RAW_EXT):
        if is_apple_family(n):
            return "raw_apple_primary", 1.0
        return "raw_unknown_family", 0.60

    return "unknown_non_primary", 0.0

def is_candidate(name):
    n = low(name)

    if n.endswith(".zip"):
        return True

    if is_debug_excluded(n):
        return False

    if is_strict_excluded(n):
        return False

    if any(n.endswith(ext) for ext in APPLE_RAW_EXT + TEXT_EXT):
        return True

    return False

def read_text_file(path):
    try:
        size = os.path.getsize(path)
        with open(path, "rb") as f:
            if size <= MAX_READ_HEAD + MAX_READ_TAIL:
                raw = f.read()
            else:
                head = f.read(MAX_READ_HEAD)
                f.seek(max(0, size - MAX_READ_TAIL))
                tail = f.read(MAX_READ_TAIL)
                raw = head + b"\n\n---TAIL_SAMPLE---\n\n" + tail
        return raw.decode("utf-8", "replace")
    except Exception:
        return ""

def parse_date_from_string(s):
    for pat in TS_PATTERNS:
        for m in pat.finditer(s):
            try:
                y = int(m.group(1))
                mo = int(m.group(2))
                d = int(m.group(3))
                dt = date(y, mo, d)
                if START_DATE <= dt <= END_DATE:
                    return dt.isoformat()
            except Exception:
                pass
    return ""

def infer_date(path, name, text=""):
    d = parse_date_from_string(str(path) + " " + str(name))
    if d:
        return d
    return parse_date_from_string(text[:200000])

def count_terms(text, arr):
    t = low(text)
    total = 0
    detail = {}
    for term in arr:
        c = t.count(term)
        if c:
            detail[term] = c
            total += c
    return total, detail

def score_text(text, name, source_type, weight):
    details = {}
    raw = {}

    for k, arr in TERMS.items():
        s, d = count_terms(text, arr)
        raw[k] = s
        details[k] = d

    mdm_false = raw["mdm_false"]
    mdm_true = raw["mdm_true"]
    restriction = raw["restriction_management"]
    account = raw["account_cloud"]
    telecom = raw["telecom_proximity"]
    usage = raw["usage_state"]
    daemon = raw["daemon_repetition"]
    interference = raw["evidence_interference"]
    seam = raw["seam_failure"]
    financial = raw["financial_strict"]

    mdm_conflict = 30 if mdm_false > 0 and restriction > 0 else 0

    layer_count = sum(
        1 for x in [restriction, account, telecom, usage, daemon, interference]
        if x > 0
    )

    cross_layer = 0
    if layer_count >= 4:
        cross_layer += 20
    if layer_count >= 5:
        cross_layer += 30
    if layer_count >= 6:
        cross_layer += 40

    t = low(text)
    n = low(name)

    plmn_sfa = 0
    if (
        ("cellularmcc" in t or "cellularmnc" in t or "l2report_cellularmcc" in t)
        and ("sfa" in t or "sfa-networking" in n)
    ):
        plmn_sfa = 45

    crash_terms = ["exc_crash", "sigabrt", "abort trap", "exc_breakpoint", "sigtrap"]
    hit_crash = sum(1 for x in crash_terms if x in t)

    crash_cluster = 0
    if hit_crash >= 2:
        crash_cluster = 25
    elif hit_crash == 1:
        crash_cluster = 15

    apt42 = account * 2 + restriction + usage + mdm_false * 2 + telecom + mdm_conflict + cross_layer
    apt32 = daemon * 2 + interference * 2 + seam + crash_cluster + plmn_sfa + cross_layer
    control = restriction * 2 + account * 2 + telecom * 2 + usage + mdm_conflict + plmn_sfa + cross_layer
    seam_score = seam * 2 + mdm_conflict + plmn_sfa + crash_cluster + financial * 8 + interference

    normal_stress = 0
    normal_stress += layer_count * 12
    if mdm_conflict:
        normal_stress += 40
    if plmn_sfa:
        normal_stress += 40
    if financial:
        normal_stress += 30
    if seam > 0 and telecom > 0 and restriction > 0:
        normal_stress += 45
    if interference > 0 and account > 0:
        normal_stress += 20
    if layer_count >= 5:
        normal_stress += 35

    total_raw = apt42 + apt32 + control + seam_score + normal_stress

    return {
        "source_type": source_type,
        "primary_weight": weight,

        "mdm_false_hits": mdm_false,
        "mdm_true_hits": mdm_true,
        "restriction_management_score": restriction,
        "account_cloud_score": account,
        "telecom_proximity_score": telecom,
        "usage_state_score": usage,
        "daemon_repetition_score": daemon,
        "evidence_interference_score": interference,
        "seam_raw_score": seam,
        "financial_app_score": financial,
        "layer_count_file": layer_count,

        "mdm_false_conflict_bonus": mdm_conflict,
        "plmn_sfa_exposure_bonus": plmn_sfa,
        "cross_layer_bonus": cross_layer,
        "crash_cluster_bonus": crash_cluster,

        "apt42_style_score_raw": apt42,
        "apt32_legacy_score_raw": apt32,
        "control_layer_score_raw": control,
        "seam_failure_score_raw": seam_score,
        "normal_explanation_stress_raw": normal_stress,

        "raw_apple_score": round(total_raw, 2) if source_type == "raw_apple_primary" else 0,
        "rtc_reporting_score": round(total_raw * 0.70, 2) if source_type == "rtc_reporting" else 0,
        "siri_feedback_score": round(total_raw * 0.25, 2) if source_type == "siri_feedback" else 0,
        "text_export_score": round(total_raw, 2) if source_type in ["text_export_non_primary", "apple_text_family_low_weight"] else 0,

        "apt42_style_score_primary": round(apt42 * weight, 2),
        "apt32_legacy_score_primary": round(apt32 * weight, 2),
        "control_layer_score_primary": round(control * weight, 2),
        "seam_failure_score_primary": round(seam_score * weight, 2),
        "normal_explanation_stress_primary": round(normal_stress * weight, 2),

        "term_summary": json.dumps(
            {k: list(v.keys())[:15] for k, v in details.items() if v},
            ensure_ascii=False,
        ),
    }

def write_csv(path, rows, headers):
    path.parent.mkdir(parents=True, exist_ok=True)

    if not rows:
        with open(path, "w", encoding="utf-8-sig", newline="") as f:
            csv.DictWriter(f, fieldnames=headers).writeheader()
        return

    extra = []
    for r in rows:
        for k in r.keys():
            if k not in headers and k not in extra:
                extra.append(k)

    final_headers = headers + extra

    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=final_headers, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

def scan_root(device, root):
    records = []
    excluded = []
    errors = []

    all_files = []

    for base, dirs, files in os.walk(root):
        dirs[:] = [
            d for d in dirs
            if not is_strict_excluded(d)
            and not is_debug_excluded(d)
            and not d.lower().startswith("_ttp")
            and "ttp_result" not in d.lower()
        ]

        for fn in files:
            all_files.append(Path(base) / fn)

    for idx, p in enumerate(all_files, 1):
        name = p.name

        try:
            rel = str(p.relative_to(root))

            if is_debug_excluded(rel):
                excluded.append({"端末": device, "path": str(p), "理由": "debug/sysdiagnose/gz/stacks/tailspin除外"})
                continue

            if is_strict_excluded(rel):
                excluded.append({"端末": device, "path": str(p), "理由": "report/summary/OCR/Note/派生資料除外"})
                continue

            if not is_candidate(name):
                excluded.append({"端末": device, "path": str(p), "理由": "対象外拡張子"})
                continue

            if name.lower().endswith(".zip"):
                zip_hash = sha256_file(p)

                try:
                    with zipfile.ZipFile(p) as z:
                        for member in z.namelist():
                            if member.endswith("/"):
                                continue

                            display = f"{name}::{member}"

                            if is_debug_excluded(display):
                                excluded.append({"端末": device, "path": display, "理由": "zip内debug/sysdiagnose/gz除外"})
                                continue

                            if is_strict_excluded(display):
                                excluded.append({"端末": device, "path": display, "理由": "zip内派生資料除外"})
                                continue

                            if not is_candidate(member):
                                excluded.append({"端末": device, "path": display, "理由": "zip内対象外"})
                                continue

                            source_type, weight = classify_source_type(display)

                            if source_type == "text_export_non_primary":
                                excluded.append({"端末": device, "path": display, "理由": "zip内text export primary除外"})
                                continue

                            if weight <= 0:
                                excluded.append({"端末": device, "path": display, "理由": source_type})
                                continue

                            raw = z.read(member)

                            if len(raw) > MAX_READ_HEAD + MAX_READ_TAIL:
                                raw2 = raw[:MAX_READ_HEAD] + b"\n\n---TAIL_SAMPLE---\n\n" + raw[-MAX_READ_TAIL:]
                            else:
                                raw2 = raw

                            text = raw2.decode("utf-8", "replace")
                            day = infer_date(str(p), display, text)

                            if day and not (START_DATE.isoformat() <= day <= END_DATE.isoformat()):
                                continue

                            rec = {
                                "端末": device,
                                "日付": day,
                                "log_family": infer_family(display),
                                "source_type": source_type,
                                "相対パス": rel,
                                "表示名": display,
                                "サイズ": len(raw),
                                "sha256": sha256_bytes(raw),
                                "zip_sha256": zip_hash,
                            }
                            rec.update(score_text(text, display, source_type, weight))
                            records.append(rec)

                except Exception as e:
                    errors.append({"端末": device, "path": str(p), "member": "", "error": str(e)})

                continue

            source_type, weight = classify_source_type(name)

            if source_type == "text_export_non_primary":
                excluded.append({"端末": device, "path": str(p), "理由": "text export primary除外"})
                continue

            if weight <= 0:
                excluded.append({"端末": device, "path": str(p), "理由": source_type})
                continue

            text = read_text_file(p)

            if not text:
                errors.append({"端末": device, "path": str(p), "member": "", "error": "read_empty_or_failed"})
                continue

            day = infer_date(str(p), name, text)

            if day and not (START_DATE.isoformat() <= day <= END_DATE.isoformat()):
                continue

            rec = {
                "端末": device,
                "日付": day,
                "log_family": infer_family(name),
                "source_type": source_type,
                "相対パス": rel,
                "表示名": name,
                "サイズ": os.path.getsize(p),
                "sha256": sha256_file(p),
                "zip_sha256": "",
            }
            rec.update(score_text(text, name, source_type, weight))
            records.append(rec)

        except Exception as e:
            errors.append({"端末": device, "path": str(p), "member": "", "error": str(e)})

        if idx % 1000 == 0:
            safe_print(f"{device}: scanned {idx}/{len(all_files)}")

    return records, excluded, errors

def aggregate_daily(records):
    groups = defaultdict(list)

    for r in records:
        key = (r.get("端末", ""), r.get("日付", ""))
        groups[key].append(r)

    rows = []

    for (device, day), rs in sorted(groups.items()):
        if not day:
            continue

        fams = Counter(r["log_family"] for r in rs)
        stypes = Counter(r["source_type"] for r in rs)

        def sumf(field):
            return round(sum(float(r.get(field, 0) or 0) for r in rs), 2)

        layer_flags = {
            "mdm_false": sumf("mdm_false_hits") > 0,
            "restriction": sumf("restriction_management_score") > 0,
            "account_cloud": sumf("account_cloud_score") > 0,
            "telecom": sumf("telecom_proximity_score") > 0,
            "usage": sumf("usage_state_score") > 0,
            "daemon": sumf("daemon_repetition_score") > 0,
            "interference": sumf("evidence_interference_score") > 0,
            "seam": sumf("seam_failure_score_primary") > 0,
        }

        layer_count = sum(1 for v in layer_flags.values() if v)

        normal_stress = sumf("normal_explanation_stress_primary")

        if layer_count >= 6:
            normal_stress += 50

        if layer_flags["mdm_false"] and layer_flags["restriction"] and layer_flags["telecom"]:
            normal_stress += 60

        if layer_flags["account_cloud"] and layer_flags["telecom"] and layer_flags["restriction"]:
            normal_stress += 40

        anchor = ""
        if day in ["2026-05-05", "2026-05-10", "2026-05-20", "2026-05-21"]:
            anchor = "2026_05核心候補"

        rows.append({
            "端末": device,
            "日付": day,
            "ファイル数": len(rs),
            "source_type分類": ";".join(f"{k}:{v}" for k, v in stypes.most_common()),
            "上位family": ";".join(f"{k}:{v}" for k, v in fams.most_common(12)),

            "raw_apple_score": sumf("raw_apple_score"),
            "rtc_reporting_score": sumf("rtc_reporting_score"),
            "siri_feedback_score": sumf("siri_feedback_score"),
            "text_export_score": sumf("text_export_score"),

            "MDM_false合計": sumf("mdm_false_hits"),
            "MDM_true合計": sumf("mdm_true_hits"),
            "restriction_management合計": sumf("restriction_management_score"),
            "account_cloud合計": sumf("account_cloud_score"),
            "telecom_proximity合計": sumf("telecom_proximity_score"),
            "usage_state合計": sumf("usage_state_score"),
            "daemon_repetition合計": sumf("daemon_repetition_score"),
            "evidence_interference合計": sumf("evidence_interference_score"),

            "APT42思想_primary": sumf("apt42_style_score_primary"),
            "APT32旧TTP_primary": sumf("apt32_legacy_score_primary"),
            "control_layer_primary": sumf("control_layer_score_primary"),
            "seam_failure_primary": sumf("seam_failure_score_primary"),
            "normal_explanation_stress": round(normal_stress, 2),

            "層数": layer_count,
            "アンカー": anchor,
            "層フラグ": json.dumps(layer_flags, ensure_ascii=False),
        })

    return rows

def file_priority(row):
    score = 0.0
    score += float(row.get("raw_apple_score", 0) or 0) * 0.4
    score += float(row.get("normal_explanation_stress_primary", 0) or 0) * 2.0
    score += float(row.get("control_layer_score_primary", 0) or 0) * 0.8
    score += float(row.get("seam_failure_score_primary", 0) or 0) * 1.5
    score += float(row.get("apt42_style_score_primary", 0) or 0) * 0.3
    score += float(row.get("apt32_legacy_score_primary", 0) or 0) * 0.3

    if float(row.get("mdm_false_conflict_bonus", 0) or 0) > 0:
        score += 3000
    if float(row.get("plmn_sfa_exposure_bonus", 0) or 0) > 0:
        score += 3000
    if float(row.get("financial_app_score", 0) or 0) > 0:
        score += 2500
    if float(row.get("crash_cluster_bonus", 0) or 0) > 0:
        score += 2500

    st = row.get("source_type", "")
    if st == "raw_apple_primary":
        score += 2000
    elif st == "rtc_reporting":
        score += 1000
    elif st == "siri_feedback":
        score -= 1000

    return round(score, 2)

def select_daily(rows):
    out = []
    ref = []

    for r in rows:
        raw = float(r.get("raw_apple_score", 0) or 0)
        stress = float(r.get("normal_explanation_stress", 0) or 0)
        layers = float(r.get("層数", 0) or 0)
        mdm_false = float(r.get("MDM_false合計", 0) or 0)
        restriction = float(r.get("restriction_management合計", 0) or 0)
        account = float(r.get("account_cloud合計", 0) or 0)
        telecom = float(r.get("telecom_proximity合計", 0) or 0)
        seam = float(r.get("seam_failure_primary", 0) or 0)

        priority = (
            raw * 1.0
            + stress * 2.0
            + float(r.get("control_layer_primary", 0) or 0) * 0.5
            + seam * 1.2
            + float(r.get("APT42思想_primary", 0) or 0) * 0.25
            + float(r.get("APT32旧TTP_primary", 0) or 0) * 0.25
            + layers * 500
        )

        if mdm_false > 0 and restriction > 0:
            priority += 5000
        if account > 0 and telecom > 0:
            priority += 3000

        rr = dict(r)
        rr["V4優先度"] = round(priority, 2)

        reasons = []
        if raw >= 10000:
            reasons.append("raw_apple_score_強")
        elif raw >= 5000:
            reasons.append("raw_apple_score_中")
        if stress >= 3000:
            reasons.append("normal_explanation_stress_強")
        if layers >= 7:
            reasons.append("7層以上")
        elif layers >= 6:
            reasons.append("6層以上")
        if mdm_false > 0 and restriction > 0:
            reasons.append("MDM_false+制限管理")
        if account > 0 and telecom > 0:
            reasons.append("account_cloud+telecom")
        if seam > 0:
            reasons.append("seam_failure")
        rr["V4理由"] = ";".join(reasons)

        structural = layers >= 7 and mdm_false > 0 and restriction > 0 and account > 0 and telecom > 0
        strong = raw >= 10000 or stress >= 3000

        if structural and strong:
            out.append(rr)
        elif raw >= 5000 and layers >= 6:
            ref.append(rr)

    return (
        sorted(out, key=lambda x: float(x.get("V4優先度", 0)), reverse=True),
        sorted(ref, key=lambda x: float(x.get("V4優先度", 0)), reverse=True),
    )

def select_files(records, daily_selected):
    selected_day_keys = set((r.get("端末"), r.get("日付")) for r in daily_selected)
    out = []
    siri = []
    rtc = []
    text = []

    for r in records:
        key = (r.get("端末"), r.get("日付"))
        st = r.get("source_type", "")
        pr = file_priority(r)

        rr = dict(r)
        rr["V4優先度"] = pr

        reasons = []
        if st:
            reasons.append(st)
        if float(r.get("mdm_false_conflict_bonus", 0) or 0) > 0:
            reasons.append("MDM_false+制限管理")
        if float(r.get("plmn_sfa_exposure_bonus", 0) or 0) > 0:
            reasons.append("PLMN/SFA露出")
        if float(r.get("financial_app_score", 0) or 0) > 0:
            reasons.append("金融/device-trust文脈")
        if float(r.get("crash_cluster_bonus", 0) or 0) > 0:
            reasons.append("crash cluster")
        if float(r.get("evidence_interference_score", 0) or 0) > 0:
            reasons.append("保存検索認証副作用")
        rr["V4理由"] = ";".join(reasons)

        if st == "siri_feedback":
            siri.append(rr)
            continue

        if st == "rtc_reporting":
            rtc.append(rr)

        if "text" in st:
            text.append(rr)

        if key in selected_day_keys and st in ["raw_apple_primary", "rtc_reporting", "raw_unknown_family"] and pr >= 500:
            out.append(rr)

    def dedup(rows):
        seen = set()
        res = []
        for r in sorted(rows, key=lambda x: float(x.get("V4優先度", 0)), reverse=True):
            h = r.get("sha256", "")
            if h and h in seen:
                continue
            if h:
                seen.add(h)
            res.append(r)
        return res

    return dedup(out), dedup(siri), dedup(rtc), dedup(text)

FILE_HEADERS = [
    "V4優先度", "V4理由",
    "端末", "日付", "log_family", "source_type",
    "相対パス", "表示名", "サイズ", "sha256", "zip_sha256",
    "mdm_false_hits", "mdm_true_hits",
    "restriction_management_score", "account_cloud_score",
    "telecom_proximity_score", "usage_state_score",
    "daemon_repetition_score", "evidence_interference_score",
    "seam_raw_score", "financial_app_score", "layer_count_file",
    "mdm_false_conflict_bonus", "plmn_sfa_exposure_bonus",
    "cross_layer_bonus", "crash_cluster_bonus",
    "apt42_style_score_primary", "apt32_legacy_score_primary",
    "control_layer_score_primary", "seam_failure_score_primary",
    "normal_explanation_stress_primary",
    "term_summary"
]

DAILY_HEADERS = [
    "V4優先度", "V4理由",
    "端末", "日付", "ファイル数",
    "source_type分類", "上位family",
    "raw_apple_score", "rtc_reporting_score", "siri_feedback_score", "text_export_score",
    "MDM_false合計", "MDM_true合計",
    "restriction_management合計", "account_cloud合計", "telecom_proximity合計",
    "usage_state合計", "daemon_repetition合計", "evidence_interference合計",
    "APT42思想_primary", "APT32旧TTP_primary",
    "control_layer_primary", "seam_failure_primary",
    "normal_explanation_stress", "層数", "アンカー", "層フラグ"
]

def write_summary(path, records, excluded, errors, daily, daily_selected, files_selected, siri, rtc, text):
    dev_counts = Counter(r.get("端末") for r in daily_selected)
    top = sorted(daily_selected, key=lambda x: float(x.get("V4優先度", 0)), reverse=True)[:40]

    with open(path, "w", encoding="utf-8") as f:
        f.write("TTP 2026-05 3DEV SUMMARY\n")
        f.write(f"Run: {RUN_DATE}\n\n")
        f.write("重要:\n")
        f.write("  入力フォルダは読取のみ。\n")
        f.write("  2026-05の12G/15G/iPhone11Proのみ解析。\n")
        f.write("  帰属判定ではない。\n\n")
        f.write("件数:\n")
        f.write(f"  解析ファイル数: {len(records)}\n")
        f.write(f"  除外ファイル数: {len(excluded)}\n")
        f.write(f"  エラー数: {len(errors)}\n")
        f.write(f"  daily shortlist: {len(daily_selected)}\n")
        f.write(f"  file shortlist: {len(files_selected)}\n")
        f.write(f"  siri reference: {len(siri)}\n")
        f.write(f"  rtc reference: {len(rtc)}\n")
        f.write(f"  text reference: {len(text)}\n\n")

        f.write("端末別 daily shortlist 件数:\n")
        for k, c in dev_counts.most_common():
            f.write(f"  - {k}: {c}\n")

        f.write("\nTop daily:\n")
        for r in top:
            f.write(
                f"- {r.get('端末')} {r.get('日付')} "
                f"V4={r.get('V4優先度')} "
                f"raw={r.get('raw_apple_score')} "
                f"stress={r.get('normal_explanation_stress')} "
                f"APT42={r.get('APT42思想_primary')} "
                f"APT32={r.get('APT32旧TTP_primary')} "
                f"layers={r.get('層数')} "
                f"reason={r.get('V4理由')}\n"
            )

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    all_records = []
    all_excluded = []
    all_errors = []

    safe_print("=== TTP 2026-05 3DEV START ===")
    safe_print(f"OUT: {OUT}")

    for device, root in ROOTS:
        safe_print(f"--- START {device} ---")
        safe_print(f"ROOT: {root}")

        if not root.exists():
            all_errors.append({"端末": device, "path": str(root), "member": "", "error": "root_not_found"})
            safe_print(f"ERROR root not found: {root}")
            continue

        records, excluded, errors = scan_root(device, root)

        safe_print(f"{device}: records={len(records)} excluded={len(excluded)} errors={len(errors)}")

        all_records.extend(records)
        all_excluded.extend(excluded)
        all_errors.extend(errors)

    daily = aggregate_daily(all_records)
    daily_selected, daily_ref = select_daily(daily)
    files_selected, siri, rtc, text = select_files(all_records, daily_selected)

    write_csv(OUT / "01_file_level_scores.csv", all_records, FILE_HEADERS)
    write_csv(OUT / "02_daily_layer_matrix.csv", daily, DAILY_HEADERS)
    write_csv(OUT / "03_final_daily_shortlist.csv", daily_selected, DAILY_HEADERS)
    write_csv(OUT / "04_final_file_shortlist.csv", files_selected, FILE_HEADERS)
    write_csv(OUT / "05_daily_reference_medium.csv", daily_ref[:1000], DAILY_HEADERS)
    write_csv(OUT / "06_siri_feedback_reference.csv", siri[:2000], FILE_HEADERS)
    write_csv(OUT / "07_rtc_reporting_reference.csv", rtc[:2000], FILE_HEADERS)
    write_csv(OUT / "08_text_export_reference.csv", text[:2000], FILE_HEADERS)
    write_csv(OUT / "90_excluded_files.csv", all_excluded, ["端末", "path", "理由"])
    write_csv(OUT / "91_errors.csv", all_errors, ["端末", "path", "member", "error"])

    write_summary(OUT / "00_human_summary.txt", all_records, all_excluded, all_errors, daily, daily_selected, files_selected, siri, rtc, text)

    safe_print("=== ALL DONE ===")
    safe_print(f"OUT: {OUT}")

if __name__ == "__main__":
    main()
