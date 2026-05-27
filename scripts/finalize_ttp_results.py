# -*- coding: utf-8 -*-
"""
finalize_ttp_results.py

Purpose:
  Read existing TTP_STRUCTURED_ONCE result CSV files only.
  Reaggregate Friend_Device by the first path component.
  Generate a final person/device-level review package for DFIR scoping.

Safety:
  - Does not read raw logs
  - Does not touch original input log folders
  - Does not delete files
  - Does not modify files
  - Does not rename files
  - Does not move files
  - Does not overwrite source material

Input:
  E:\Result\2026-05-27\My_Device\TTP_STRUCTURED_ONCE_*
  E:\Result\2026-05-27\Friend_Device\TTP_STRUCTURED_ONCE_*

Output:
  E:\Result\2026-05-27\_FINAL_REVIEW_PACKAGE\FINAL_TTP_REVIEW_*

Note:
  This script supports both older Japanese-column CSV outputs and the later English-column outputs.
"""

import csv
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter


BASE = Path(r"E:\Result\2026-05-27")
MY_BASE = BASE / "My_Device"
FR_BASE = BASE / "Friend_Device"
OUT_BASE = BASE / "_FINAL_REVIEW_PACKAGE"

RUN = datetime.now().strftime("%Y-%m-%d-%H%M%S")
OUT = OUT_BASE / ("FINAL_TTP_REVIEW_" + RUN)


# Field aliases for compatibility with earlier Japanese CSV outputs and newer English CSV outputs.
ALIASES = {
    "group": ["group", "グループ"],
    "device": ["device", "端末"],
    "date": ["date", "日付"],
    "relative_path": ["relative_path", "相対パス"],
    "display_name": ["display_name", "表示名"],
    "file_size": ["file_size", "サイズ"],
    "reason": ["reason", "理由"],
    "priority": ["V4_priority", "V4優先度"],
    "v4_reason": ["V4_reason", "V4理由"],
    "family": ["log_family"],
    "source_type": ["source_type"],
    "sha256": ["sha256"],
    "zip_sha256": ["zip_sha256"],
    "source_type_breakdown": ["source_type_breakdown", "source_type分類"],
    "top_families": ["top_families", "上位family"],
    "file_count": ["file_count", "ファイル数"],
    "layers": ["layers", "層数"],
    "layer_flags": ["layer_flags", "層フラグ"],
    "anchor": ["anchor", "アンカー"],
    "raw_apple_score": ["raw_apple_score"],
    "rtc_reporting_score": ["rtc_reporting_score"],
    "siri_feedback_score": ["siri_feedback_score"],
    "text_export_score": ["text_export_score"],
    "mdm_false_total": ["MDM_false_total", "MDM_false合計"],
    "mdm_true_total": ["MDM_true_total", "MDM_true合計"],
    "restriction_total": ["restriction_management_total", "restriction_management合計"],
    "account_cloud_total": ["account_cloud_total", "account_cloud合計"],
    "telecom_total": ["telecom_proximity_total", "telecom_proximity合計"],
    "usage_total": ["usage_state_total", "usage_state合計"],
    "daemon_total": ["daemon_repetition_total", "daemon_repetition合計"],
    "interference_total": ["evidence_interference_total", "evidence_interference合計"],
    "apt42_primary": ["APT42_style_primary", "APT42思想_primary"],
    "apt32_primary": ["APT32_legacy_TTP_primary", "APT32旧TTP_primary"],
    "control_primary": ["control_layer_primary"],
    "seam_primary": ["seam_failure_primary"],
    "normal_stress": ["normal_explanation_stress"],
    "mdm_false_hits": ["mdm_false_hits"],
    "mdm_true_hits": ["mdm_true_hits"],
    "restriction_score": ["restriction_management_score"],
    "account_cloud_score": ["account_cloud_score"],
    "telecom_score": ["telecom_proximity_score"],
    "usage_score": ["usage_state_score"],
    "daemon_score": ["daemon_repetition_score"],
    "interference_score": ["evidence_interference_score"],
    "seam_raw_score": ["seam_raw_score"],
    "financial_score": ["financial_app_score"],
    "layer_count_file": ["layer_count_file"],
    "mdm_false_conflict_bonus": ["mdm_false_conflict_bonus"],
    "plmn_sfa_exposure_bonus": ["plmn_sfa_exposure_bonus"],
    "cross_layer_bonus": ["cross_layer_bonus"],
    "crash_cluster_bonus": ["crash_cluster_bonus"],
    "normal_stress_primary": ["normal_explanation_stress_primary"],
    "term_summary": ["term_summary"],
}


def val(row, key, default=""):
    for name in ALIASES.get(key, [key]):
        if name in row:
            return row.get(name, default)
    return default


def fnum(v):
    try:
        if v is None or v == "":
            return 0.0
        return float(str(v).replace(",", ""))
    except Exception:
        return 0.0


def read_csv(path):
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, headers=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    if headers is None:
        headers = []
        for row in rows:
            for key in row.keys():
                if key not in headers:
                    headers.append(key)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def latest_result_dir(base):
    if not base.exists():
        return None
    dirs = [p for p in base.iterdir() if p.is_dir() and p.name.startswith("TTP_STRUCTURED_ONCE_")]
    if not dirs:
        return None
    return sorted(dirs, key=lambda p: p.name)[-1]


def first_path_part(relative_path):
    text = str(relative_path or "").replace("/", "\\").strip("\\")
    if not text:
        return "UNKNOWN"
    part = text.split("\\")[0].strip()
    if not part:
        return "UNKNOWN"
    return re.sub(r"[^0-9A-Za-z _.-]", "_", part)


def normalized_device(row):
    group = val(row, "group")
    device = val(row, "device")
    relative_path = val(row, "relative_path")

    if group == "Friend_Device":
        person = first_path_part(relative_path)
        return f"Friend_Device:{person}"

    return f"My_Device:{device}"


def file_priority(row):
    score = 0.0
    score += fnum(val(row, "raw_apple_score")) * 0.4
    score += fnum(val(row, "normal_stress_primary")) * 2.0
    score += fnum(val(row, "control_primary")) * 0.8
    score += fnum(val(row, "seam_primary")) * 1.5
    score += fnum(val(row, "apt42_primary")) * 0.3
    score += fnum(val(row, "apt32_primary")) * 0.3

    if fnum(val(row, "mdm_false_conflict_bonus")) > 0:
        score += 3000
    if fnum(val(row, "plmn_sfa_exposure_bonus")) > 0:
        score += 3000
    if fnum(val(row, "financial_score")) > 0:
        score += 2500
    if fnum(val(row, "crash_cluster_bonus")) > 0:
        score += 2500

    source_type = val(row, "source_type")
    if source_type == "raw_apple_primary":
        score += 2000
    elif source_type == "rtc_reporting":
        score += 1000
    elif source_type == "siri_feedback":
        score -= 1000

    return round(score, 2)


def file_reason(row):
    reasons = []
    source_type = val(row, "source_type")
    if source_type:
        reasons.append(source_type)
    if fnum(val(row, "mdm_false_conflict_bonus")) > 0:
        reasons.append("MDM_false_plus_restriction_management")
    if fnum(val(row, "plmn_sfa_exposure_bonus")) > 0:
        reasons.append("PLMN_SFA_exposure")
    if fnum(val(row, "financial_score")) > 0:
        reasons.append("financial_or_device_trust_context")
    if fnum(val(row, "crash_cluster_bonus")) > 0:
        reasons.append("crash_cluster")
    if fnum(val(row, "interference_score")) > 0:
        reasons.append("save_search_auth_side_effect")
    return ";".join(reasons)


def aggregate_from_files(file_rows):
    groups = defaultdict(list)

    for row in file_rows:
        day = val(row, "date")
        if not day:
            continue
        dev2 = normalized_device(row)
        groups[(val(row, "group"), dev2, day)].append(row)

    out = []

    for (group, dev2, day), rows in sorted(groups.items()):
        families = Counter(val(row, "family") for row in rows)
        source_types = Counter(val(row, "source_type") for row in rows)

        def sumf(key):
            return round(sum(fnum(val(row, key)) for row in rows), 2)

        mdm_false = sumf("mdm_false_hits")
        restriction = sumf("restriction_score")
        account = sumf("account_cloud_score")
        telecom = sumf("telecom_score")
        usage = sumf("usage_score")
        daemon = sumf("daemon_score")
        interference = sumf("interference_score")
        seam = sumf("seam_primary")

        layer_flags = {
            "mdm_false": mdm_false > 0,
            "restriction": restriction > 0,
            "account_cloud": account > 0,
            "telecom": telecom > 0,
            "usage": usage > 0,
            "daemon": daemon > 0,
            "interference": interference > 0,
            "seam": seam > 0,
        }
        layers = sum(1 for flag in layer_flags.values() if flag)

        normal = sumf("normal_stress_primary")
        if layers >= 6:
            normal += 50
        if mdm_false > 0 and restriction > 0 and telecom > 0:
            normal += 60
        if account > 0 and telecom > 0 and restriction > 0:
            normal += 40

        raw = sumf("raw_apple_score")
        apt42 = sumf("apt42_primary")
        apt32 = sumf("apt32_primary")
        control = sumf("control_primary")

        priority = (
            raw * 1.0
            + normal * 2.0
            + control * 0.5
            + seam * 1.2
            + apt42 * 0.25
            + apt32 * 0.25
            + layers * 500
        )
        if mdm_false > 0 and restriction > 0:
            priority += 5000
        if account > 0 and telecom > 0:
            priority += 3000

        reasons = []
        if raw >= 10000:
            reasons.append("raw_apple_score_strong")
        elif raw >= 5000:
            reasons.append("raw_apple_score_medium")
        if normal >= 3000:
            reasons.append("normal_explanation_stress_strong")
        if layers >= 7:
            reasons.append("7_or_more_layers")
        elif layers >= 6:
            reasons.append("6_or_more_layers")
        if mdm_false > 0 and restriction > 0:
            reasons.append("MDM_false_plus_restriction_management")
        if account > 0 and telecom > 0:
            reasons.append("account_cloud_plus_telecom")
        if seam > 0:
            reasons.append("seam_failure")
        if apt42 > 0 and apt32 > 0:
            reasons.append("APT42_style_plus_APT32_legacy_TTP")

        out.append({
            "V4_priority": round(priority, 2),
            "V4_reason": ";".join(reasons),
            "group": group,
            "reaggregated_device": dev2,
            "date": day,
            "file_count": len(rows),
            "source_type_breakdown": ";".join(f"{k}:{v}" for k, v in source_types.most_common()),
            "top_families": ";".join(f"{k}:{v}" for k, v in families.most_common(12)),
            "raw_apple_score": raw,
            "rtc_reporting_score": sumf("rtc_reporting_score"),
            "siri_feedback_score": sumf("siri_feedback_score"),
            "text_export_score": sumf("text_export_score"),
            "MDM_false_total": mdm_false,
            "MDM_true_total": sumf("mdm_true_hits"),
            "restriction_management_total": restriction,
            "account_cloud_total": account,
            "telecom_proximity_total": telecom,
            "usage_state_total": usage,
            "daemon_repetition_total": daemon,
            "evidence_interference_total": interference,
            "APT42_style_primary": apt42,
            "APT32_legacy_TTP_primary": apt32,
            "control_layer_primary": control,
            "seam_failure_primary": seam,
            "normal_explanation_stress": round(normal, 2),
            "layers": layers,
            "layer_flags": str(layer_flags),
        })

    return sorted(out, key=lambda row: fnum(row.get("V4_priority")), reverse=True)


def select_final_days(daily_rows):
    final_days = []
    reference_days = []

    for row in daily_rows:
        raw = fnum(row.get("raw_apple_score"))
        stress = fnum(row.get("normal_explanation_stress"))
        layers = fnum(row.get("layers"))
        mdm = fnum(row.get("MDM_false_total"))
        restriction = fnum(row.get("restriction_management_total"))
        account = fnum(row.get("account_cloud_total"))
        telecom = fnum(row.get("telecom_proximity_total"))
        seam = fnum(row.get("seam_failure_primary"))

        structural = layers >= 7 and mdm > 0 and restriction > 0 and account > 0 and telecom > 0
        strong = raw >= 10000 or stress >= 3000
        medium = raw >= 5000 and layers >= 6

        if structural and strong:
            final_days.append(row)
        elif medium or (structural and seam > 0):
            reference_days.append(row)

    return final_days, reference_days


def select_top_files(file_rows, final_days):
    final_day_keys = set((row.get("reaggregated_device"), row.get("date")) for row in final_days)

    final_files = []
    siri_reference = []
    rtc_reference = []

    for row in file_rows:
        output = dict(row)
        output["reaggregated_device"] = normalized_device(row)
        output["V4_priority"] = file_priority(row)
        output["V4_reason"] = file_reason(row)

        source_type = val(row, "source_type")

        if source_type == "siri_feedback":
            siri_reference.append(output)
            continue

        if source_type == "rtc_reporting":
            rtc_reference.append(output)

        if (output.get("reaggregated_device"), val(row, "date")) in final_day_keys:
            if source_type in ["raw_apple_primary", "rtc_reporting", "raw_unknown_family"] and fnum(output.get("V4_priority")) >= 500:
                final_files.append(output)

    def dedup(rows):
        seen = set()
        result = []
        for row in sorted(rows, key=lambda item: fnum(item.get("V4_priority")), reverse=True):
            h = val(row, "sha256")
            if h and h in seen:
                continue
            if h:
                seen.add(h)
            result.append(row)
        return result

    return dedup(final_files), dedup(siri_reference), dedup(rtc_reference)


def per_device_top(daily_rows, n=10):
    groups = defaultdict(list)
    for row in daily_rows:
        groups[row.get("reaggregated_device", "")].append(row)

    out = []
    for dev, rows in groups.items():
        rows = sorted(rows, key=lambda row: fnum(row.get("V4_priority")), reverse=True)
        for i, row in enumerate(rows[:n], 1):
            output = dict(row)
            output["device_rank"] = i
            out.append(output)
    return out


DAILY_HEADERS = [
    "V4_priority", "V4_reason", "group", "reaggregated_device", "date", "file_count",
    "source_type_breakdown", "top_families",
    "raw_apple_score", "rtc_reporting_score", "siri_feedback_score", "text_export_score",
    "MDM_false_total", "MDM_true_total",
    "restriction_management_total", "account_cloud_total", "telecom_proximity_total",
    "usage_state_total", "daemon_repetition_total", "evidence_interference_total",
    "APT42_style_primary", "APT32_legacy_TTP_primary", "control_layer_primary",
    "seam_failure_primary", "normal_explanation_stress", "layers", "layer_flags",
]

FILE_HEADERS = [
    "V4_priority", "V4_reason", "group", "device", "reaggregated_device", "date",
    "log_family", "source_type", "relative_path", "display_name", "file_size",
    "sha256", "zip_sha256",
    "mdm_false_hits", "mdm_true_hits",
    "restriction_management_score", "account_cloud_score", "telecom_proximity_score",
    "usage_state_score", "daemon_repetition_score", "evidence_interference_score",
    "seam_raw_score", "financial_app_score", "layer_count_file",
    "mdm_false_conflict_bonus", "plmn_sfa_exposure_bonus",
    "cross_layer_bonus", "crash_cluster_bonus",
    "apt42_style_score_primary", "apt32_legacy_score_primary",
    "control_layer_score_primary", "seam_failure_score_primary",
    "normal_explanation_stress_primary",
    "term_summary",
]


def normalize_file_row(row):
    return {
        "V4_priority": row.get("V4_priority", ""),
        "V4_reason": row.get("V4_reason", ""),
        "group": val(row, "group"),
        "device": val(row, "device"),
        "reaggregated_device": row.get("reaggregated_device", ""),
        "date": val(row, "date"),
        "log_family": val(row, "family"),
        "source_type": val(row, "source_type"),
        "relative_path": val(row, "relative_path"),
        "display_name": val(row, "display_name"),
        "file_size": val(row, "file_size"),
        "sha256": val(row, "sha256"),
        "zip_sha256": val(row, "zip_sha256"),
        "mdm_false_hits": val(row, "mdm_false_hits"),
        "mdm_true_hits": val(row, "mdm_true_hits"),
        "restriction_management_score": val(row, "restriction_score"),
        "account_cloud_score": val(row, "account_cloud_score"),
        "telecom_proximity_score": val(row, "telecom_score"),
        "usage_state_score": val(row, "usage_score"),
        "daemon_repetition_score": val(row, "daemon_score"),
        "evidence_interference_score": val(row, "interference_score"),
        "seam_raw_score": val(row, "seam_raw_score"),
        "financial_app_score": val(row, "financial_score"),
        "layer_count_file": val(row, "layer_count_file"),
        "mdm_false_conflict_bonus": val(row, "mdm_false_conflict_bonus"),
        "plmn_sfa_exposure_bonus": val(row, "plmn_sfa_exposure_bonus"),
        "cross_layer_bonus": val(row, "cross_layer_bonus"),
        "crash_cluster_bonus": val(row, "crash_cluster_bonus"),
        "apt42_style_score_primary": val(row, "apt42_primary"),
        "apt32_legacy_score_primary": val(row, "apt32_primary"),
        "control_layer_score_primary": val(row, "control_primary"),
        "seam_failure_score_primary": val(row, "seam_primary"),
        "normal_explanation_stress_primary": val(row, "normal_stress_primary"),
        "term_summary": val(row, "term_summary"),
    }


def write_summary(path, my_dir, fr_dir, daily, final_days, ref_days, final_files, siri, rtc):
    dev_counts = Counter(row.get("reaggregated_device", "") for row in final_days)

    with open(path, "w", encoding="utf-8") as f:
        f.write("FINAL RESULT CSV REVIEW PACKAGE\n")
        f.write(f"Run: {RUN}\n\n")
        f.write("Input:\n")
        f.write(f"  My_Device result: {my_dir}\n")
        f.write(f"  Friend_Device result: {fr_dir}\n\n")
        f.write("Important:\n")
        f.write("  This script read existing result CSV files only.\n")
        f.write("  It did not read raw logs.\n")
        f.write("  Friend_Device was reaggregated by the first relative-path component.\n")
        f.write("  This is not an attribution finding.\n\n")
        f.write("Counts:\n")
        f.write(f"  daily reaggregated: {len(daily)}\n")
        f.write(f"  final daily: {len(final_days)}\n")
        f.write(f"  reference daily: {len(ref_days)}\n")
        f.write(f"  final files: {len(final_files)}\n")
        f.write(f"  siri reference: {len(siri)}\n")
        f.write(f"  rtc reference: {len(rtc)}\n\n")

        f.write("Final daily count by reaggregated device:\n")
        for dev, count in dev_counts.most_common():
            f.write(f"  - {dev}: {count}\n")

        f.write("\nTop daily 40:\n")
        for row in final_days[:40]:
            f.write(
                f"- {row.get('reaggregated_device')} {row.get('date')} "
                f"V4={row.get('V4_priority')} "
                f"raw={row.get('raw_apple_score')} "
                f"stress={row.get('normal_explanation_stress')} "
                f"APT42={row.get('APT42_style_primary')} "
                f"APT32={row.get('APT32_legacy_TTP_primary')} "
                f"layers={row.get('layers')} "
                f"reason={row.get('V4_reason')}\n"
            )


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    my_dir = latest_result_dir(MY_BASE)
    fr_dir = latest_result_dir(FR_BASE)

    if not my_dir:
        print("ERROR: My_Device result folder not found")
        return
    if not fr_dir:
        print("ERROR: Friend_Device result folder not found")
        return

    print("MY:", my_dir)
    print("FR:", fr_dir)
    print("OUT:", OUT)

    my_files = read_csv(my_dir / "01_file_level_scores.csv")
    fr_files = read_csv(fr_dir / "01_file_level_scores.csv")
    all_files = my_files + fr_files

    daily = aggregate_from_files(all_files)
    final_days, reference_days = select_final_days(daily)
    final_files, siri_reference, rtc_reference = select_top_files(all_files, final_days)
    device_top = per_device_top(final_days, 10)

    final_files_normalized = [normalize_file_row(row) for row in final_files]
    siri_normalized = [normalize_file_row(row) for row in siri_reference]
    rtc_normalized = [normalize_file_row(row) for row in rtc_reference]

    write_csv(OUT / "00_final_daily_by_person.csv", final_days, DAILY_HEADERS)
    write_csv(OUT / "01_final_files_by_person.csv", final_files_normalized, FILE_HEADERS)
    write_csv(OUT / "02_per_device_top10_days.csv", device_top, ["device_rank"] + DAILY_HEADERS)
    write_csv(OUT / "03_reference_daily_medium.csv", reference_days[:1000], DAILY_HEADERS)
    write_csv(OUT / "04_siri_reference.csv", siri_normalized[:2000], FILE_HEADERS)
    write_csv(OUT / "05_rtc_reference.csv", rtc_normalized[:2000], FILE_HEADERS)
    write_csv(OUT / "06_all_daily_reaggregated.csv", daily, DAILY_HEADERS)

    write_summary(
        OUT / "00_human_summary.txt",
        my_dir,
        fr_dir,
        daily,
        final_days,
        reference_days,
        final_files,
        siri_reference,
        rtc_reference,
    )

    print("DONE")
    print("OUT:", OUT)


if __name__ == "__main__":
    main()
