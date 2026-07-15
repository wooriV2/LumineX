# -*- coding: utf-8 -*-
"""
수정 스크립트 — 잘못 삽입된 항목 정리
1. SSS_TIER에서 SS/S 항목 제거
2. SS_TIER에 누락된 SS 항목 추가 (S 항목도 SS_TIER에 포함)

실행: $env:PYTHONUTF8 = "1"; python preset_builders/fix_tier_misplaced.py
"""

TARGET = "core/presets_meta.py"

# SSS_TIER에서 제거할 항목 (SS/S인데 잘못 들어간 것들)
REMOVE_FROM_SSS = [
    "young_korean_campus_spring",
    "young_korean_gym_first_gains",
    "young_korean_tokyo_first_solo",
    "young_korean_pool_pastel",
    "young_korean_first_snowfall_seoul",
    "young_korean_tattoo_shoulder_okinawa",
    "young_korean_tattoo_ankle_jeju",
    "young_korean_summer_busan",
    "young_korean_bali_first_solo",
    "young_korean_tattoo_first_wrist",
    "young_korean_maldives_first_trip",
    "young_korean_neon_first_night",
    "young_korean_cherry_blossom",
    "young_korean_studio_black_minimal",
    "young_korean_jeju_sunrise",
    "runway_korean_slim_newyork_snowstorm",
    "runway_korean_slim_seychelles_granite",
    "runway_korean_slim_sahara_wind",
    "runway_korean_slim_palawan_karst",
    "runway_korean_slim_kyoto_autumn",
    "runway_korean_slim_bali_temple_gold",
    "runway_korean_slim_berlin_underground",
    "runway_korean_slim_amalfi_cliff",
    "runway_korean_slim_moroccan_riad",
    "runway_korean_slim_seoulforest_spring",
    "runway_korean_slim_nyc_rooftop",
    "runway_korean_slim_dubai_penthouse",
    "runway_korean_slim_paris_window",
    "runway_korean_slim_void_studio",
    "fitness_korean_cyber_muscle_ddp",
    "fitness_korean_abs_seychelles_granite",
    "fitness_korean_glutes_ibiza_sunset",
    "fitness_korean_mature_40_seoul_penthouse",
    "fitness_korean_tattoo_thigh_monaco",
    "fitness_korean_abs_neon_void",
    "fitness_korean_silver_hair_cliff",
    "fitness_korean_tattoo_rio_carnival",
]

# SS_TIER에 있어야 할 항목 (SS + S 통합)
SHOULD_BE_IN_SS = [
    # SS
    "young_korean_jeju_sunrise",
    "young_korean_studio_black_minimal",
    "young_korean_cherry_blossom",
    "young_korean_neon_first_night",
    "young_korean_maldives_first_trip",
    "young_korean_tattoo_first_wrist",
    "young_korean_bali_first_solo",
    "young_korean_summer_busan",
    "young_korean_tattoo_ankle_jeju",
    "young_korean_tattoo_shoulder_okinawa",
    "young_korean_first_snowfall_seoul",
    # S → SS_TIER에 포함
    "young_korean_pool_pastel",
    "young_korean_tokyo_first_solo",
    "young_korean_gym_first_gains",
    "young_korean_campus_spring",
    # Runway SS
    "runway_korean_slim_void_studio",
    "runway_korean_slim_paris_window",
    "runway_korean_slim_dubai_penthouse",
    "runway_korean_slim_nyc_rooftop",
    "runway_korean_slim_seoulforest_spring",
    "runway_korean_slim_moroccan_riad",
    "runway_korean_slim_amalfi_cliff",
    "runway_korean_slim_berlin_underground",
    "runway_korean_slim_bali_temple_gold",
    "runway_korean_slim_kyoto_autumn",
    "runway_korean_slim_palawan_karst",
    "runway_korean_slim_sahara_wind",
    "runway_korean_slim_seychelles_granite",
    "runway_korean_slim_newyork_snowstorm",
    # Fitness SS
    "fitness_korean_tattoo_rio_carnival",
    "fitness_korean_silver_hair_cliff",
    "fitness_korean_abs_neon_void",
    "fitness_korean_tattoo_thigh_monaco",
    "fitness_korean_mature_40_seoul_penthouse",
    "fitness_korean_glutes_ibiza_sunset",
    "fitness_korean_abs_seychelles_granite",
    "fitness_korean_cyber_muscle_ddp",
]

with open(TARGET, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

# ── SSS_TIER ~ SS_TIER 범위 탐색 ──────────────────────────────
sss_start = None
ss_start = None
for i, line in enumerate(lines):
    if "SSS_TIER = {" in line and sss_start is None:
        sss_start = i
    if "SS_TIER = {" in line and sss_start is not None and ss_start is None:
        ss_start = i
        break

print(f"SSS_TIER 블록: {sss_start+1}줄 ~ {ss_start}줄")

# ── SSS_TIER에서 잘못된 항목 제거 ─────────────────────────────
removed_sss = []
new_lines = []
for i, line in enumerate(lines):
    if sss_start <= i < ss_start:
        stripped = line.strip().strip('",')
        if stripped in REMOVE_FROM_SSS:
            removed_sss.append(stripped)
            continue
    new_lines.append(line)

lines = new_lines
print(f"\n[SSS_TIER] 제거: {len(removed_sss)}종")
for k in removed_sss:
    print(f"  🗑️  {k}")

# ── SS_TIER에 누락 항목 추가 ──────────────────────────────────
content = "".join(lines)
SS_ANCHOR = "SS_TIER = {"
missing_ss = [k for k in SHOULD_BE_IN_SS if f'"{k}"' not in content]

if missing_ss:
    insert_block = "\n" + "".join(f'    "{k}",\n' for k in missing_ss)
    content = content.replace(SS_ANCHOR, SS_ANCHOR + insert_block)
    print(f"\n[SS_TIER] 추가: {len(missing_ss)}종")
    for k in missing_ss:
        print(f"  ✅ {k}")
else:
    print(f"\n[SS_TIER] 누락 항목 없음 — 이미 모두 존재")

# ── 저장 ──────────────────────────────────────────────────────
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

print("\n" + "=" * 60)
print("✅ fix_tier_misplaced.py 완료!")
print("=" * 60)
