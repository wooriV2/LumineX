# -*- coding: utf-8 -*-
"""
통합 패치 스크립트 — Fitness 10종 + Runway Slim 20종 + Young Adult 20종
- core/presets_meta.py : SSS_TIER, SS_TIER (set {} 구조)
- core/hof_tier.py     : HOF_TIER (set {} 구조)

실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_korean_50_all.py
"""

# ── 티어 분류 ──────────────────────────────────────────────────

HOF_KEYS = [
    # Fitness — HOF 없음 (이번 10종은 SSS/SS만)
]

SSS_PRESETS_META = [
    # Fitness 10종
    "fitness_korean_tattoo_sleeve_aurora",
    "fitness_korean_tattoo_full_maldives_void",
    # Runway Slim 20종
    "runway_korean_slim_milan_catwalk",
    "runway_korean_slim_tokyo_shibuya_rain",
    "runway_korean_slim_icelandic_glacier",
    "runway_korean_slim_aurora_finland",
    "runway_korean_slim_tattoo_collarbone_void",
    "runway_korean_slim_crystal_gala",
    # Young Adult 20종
    "young_korean_paris_first_europe",
    "young_korean_midnight_rooftop_seoul",
    "young_korean_nyc_first_american",
    "young_korean_debut_red_carpet",
    "young_korean_21_birthday_gold",
]

SS_PRESETS_META = [
    # Fitness 10종
    "fitness_korean_tattoo_rio_carnival",
    "fitness_korean_silver_hair_cliff",
    "fitness_korean_abs_neon_void",
    "fitness_korean_tattoo_thigh_monaco",
    "fitness_korean_mature_40_seoul_penthouse",
    "fitness_korean_glutes_ibiza_sunset",
    "fitness_korean_abs_seychelles_granite",
    "fitness_korean_cyber_muscle_ddp",
    # Runway Slim 20종
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
    # Young Adult 20종
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
]

S_PRESETS_META = [
    # Young Adult
    "young_korean_pool_pastel",
    "young_korean_tokyo_first_solo",
    "young_korean_gym_first_gains",
    "young_korean_campus_spring",
]

# ── 패치 함수 ──────────────────────────────────────────────────

def patch_set(filepath, set_anchor, keys, label):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        src = f.read()

    if set_anchor not in src:
        print(f"[ERROR] 앵커 없음: {set_anchor} in {filepath}")
        return

    added = []
    skipped = []
    for key in keys:
        entry = f'    "{key}",'
        if f'"{key}"' in src:
            skipped.append(key)
        else:
            src = src.replace(set_anchor, set_anchor + f'\n    "{key}",')
            added.append(key)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(src)

    print(f"\n[{label}] 추가: {len(added)}종 / 스킵: {len(skipped)}종")
    for k in added:
        print(f"  ✅ {k}")
    for k in skipped:
        print(f"  ⏭️  {k} (이미 존재)")


# ── 실행 ───────────────────────────────────────────────────────

print("=" * 60)
print("패치 시작: Fitness 10 + Runway Slim 20 + Young Adult 20")
print("=" * 60)

# 1. HOF_TIER (hof_tier.py)
if HOF_KEYS:
    patch_set("core/hof_tier.py", "HOF_TIER = {", HOF_KEYS, "HOF_TIER")
else:
    print("\n[HOF_TIER] 이번 50종에 HOF 없음 — 스킵")

# 2. SSS_TIER (presets_meta.py)
patch_set("core/presets_meta.py", "SSS_TIER = {", SSS_PRESETS_META, "SSS_TIER")

# 3. SS_TIER (presets_meta.py)
patch_set("core/presets_meta.py", "SS_TIER = {", SS_PRESETS_META, "SS_TIER")

# 4. S_TIER (presets_meta.py) — 앵커 확인 후 처리
with open("core/presets_meta.py", "r", encoding="utf-8-sig") as f:
    check = f.read()

S_ANCHOR = "S_TIER = {"
if S_ANCHOR in check:
    patch_set("core/presets_meta.py", S_ANCHOR, S_PRESETS_META, "S_TIER")
else:
    print(f"\n[WARN] S_TIER 앵커 없음. 아래 항목 수동 추가 필요:")
    for k in S_PRESETS_META:
        print(f"  - {k}")

print("\n" + "=" * 60)
print("✅ 패치 완료!")
print(f"   HOF : {len(HOF_KEYS)}종")
print(f"   SSS : {len(SSS_PRESETS_META)}종")
print(f"   SS  : {len(SS_PRESETS_META)}종")
print(f"   S   : {len(S_PRESETS_META)}종")
print("=" * 60)
