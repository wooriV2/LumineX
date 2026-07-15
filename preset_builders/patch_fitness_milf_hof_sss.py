# -*- coding: utf-8 -*-
"""
Fitness 10종 + MILF 1~40종 HOF/SSS 패치 스크립트
- core/hof_tier.py  : HOF_TIER
- core/presets_meta.py : SSS_TIER, SS_TIER

실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_fitness_milf_hof_sss.py
"""

HOF_KEYS = [
    # Fitness 5종
    "fitness_korean_tattoo_rio_carnival",
    "fitness_korean_tattoo_thigh_monaco",
    "fitness_korean_glutes_ibiza_sunset",
    "fitness_korean_tattoo_sleeve_aurora",
    "fitness_korean_tattoo_full_maldives_void",
    # MILF 15종
    "milf_korean_penthouse_micro_bikini",
    "milf_korean_boudoir_corset",
    "milf_korean_club_latex_mini",
    "milf_korean_onsen_silk",
    "milf_korean_rain_wet_street",
    "milf_korean_amazon_warrior",
    "milf_korean_neon_latex_micro",
    "milf_korean_hanok_traditional_edge",
    "milf_korean_dark_fantasy_latex",
    "milf_korean_micro_bandeau_pool_edge",
    "milf_korean_latex_catsuit_stage",
    "milf_korean_micro_bikini_waterfall",
    "milf_korean_strappy_harness_club",
    "milf_korean_bbw_wet_pool",
    "milf_korean_chrome_bodysuit_cyber",
]

SSS_KEYS = [
    # Fitness SSS 5종
    "fitness_korean_silver_hair_cliff",
    "fitness_korean_abs_neon_void",
    "fitness_korean_mature_40_seoul_penthouse",
    "fitness_korean_abs_seychelles_granite",
    "fitness_korean_cyber_muscle_ddp",
    # MILF SSS
    "milf_korean_pool_bandeau",
    "milf_korean_beach_micro_thong",
    "milf_korean_office_power",
    "milf_korean_resort_deep_plunge",
    "milf_korean_bbw_lingerie_boudoir",
    "milf_korean_bust_queen_pool",
    "milf_korean_fitness_micro_sports",
    "milf_korean_yacht_bikini_gold",
    "milf_korean_rooftop_vinyl_mini",
    "milf_korean_sheer_lace_boudoir",
    "milf_korean_micro_skirt_rooftop_wind",
    "milf_korean_gold_chain_body",
    "milf_korean_deep_plunge_gown_casino",
    "milf_korean_vinyl_shorts_neon",
    "milf_korean_micro_crop_jeju_cliff",
    "milf_korean_ribbon_only_editorial",
    "milf_korean_micro_tennis_skirt_pool",
    "milf_korean_micro_hanbok_palace",
    "milf_korean_open_shirt_beach",
]

SS_KEYS = [
    "milf_korean_tennis_club",
    "milf_korean_spa_white_micro",
]

def patch_set(filepath, anchor, keys, label):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        src = f.read()
    if anchor not in src:
        print(f"[ERROR] 앵커 없음: {anchor}")
        return
    added, skipped = [], []
    for key in keys:
        if f'"{key}"' in src:
            skipped.append(key)
        else:
            src = src.replace(anchor, anchor + f'\n    "{key}",')
            added.append(key)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(src)
    print(f"\n[{label}] 추가: {len(added)}종 / 스킵: {len(skipped)}종")
    for k in added:
        print(f"  ✅ {k}")
    for k in skipped:
        print(f"  ⏭️  {k}")

print("=" * 60)
print("패치 시작: Fitness 10종 + MILF 40종 HOF/SSS")
print("=" * 60)

patch_set("core/hof_tier.py",    "HOF_TIER = {",  HOF_KEYS, "HOF_TIER")
patch_set("core/presets_meta.py","SSS_TIER = {",  SSS_KEYS, "SSS_TIER")
patch_set("core/presets_meta.py","SS_TIER = {",   SS_KEYS,  "SS_TIER")

print("\n" + "=" * 60)
print(f"✅ 완료! HOF {len(HOF_KEYS)}종 / SSS {len(SSS_KEYS)}종 / SS {len(SS_KEYS)}종")
print("=" * 60)
