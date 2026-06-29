"""
apply_multi_bodypaint_patch_v3.py
dashboard.py 멀티 바디페인팅 카테고리에 33종 추가 + SSS/SS 패치
실행: python preset_builders/apply_multi_bodypaint_patch_v3.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

# ══════════════════════════════════════════════
# PATCH 1: 카테고리에 33종 추가
# ══════════════════════════════════════════════

CAT_OLD = '''        # G4 연결형 트리오 (3인, 합치면 거대한 작품)
        "trio_triptych_klimt_bodypaint",
        "trio_phoenix_rising_bodypaint",
        "trio_world_tree_bodypaint",
        "trio_ocean_depth_bodypaint",
        "trio_aurora_spectrum_bodypaint",
        "trio_cosmic_creation_bodypaint",
    ],'''

CAT_NEW = '''        # G4 연결형 트리오 (3인, 합치면 거대한 작품)
        "trio_triptych_klimt_bodypaint",
        "trio_phoenix_rising_bodypaint",
        "trio_world_tree_bodypaint",
        "trio_ocean_depth_bodypaint",
        "trio_aurora_spectrum_bodypaint",
        "trio_cosmic_creation_bodypaint",
        # G1 대비형 듀오 추가 (6종)
        "duo_east_and_west_bodypaint",
        "duo_macro_and_micro_bodypaint",
        "duo_ancient_and_future_bodypaint",
        "duo_poison_and_medicine_bodypaint",
        "duo_storm_and_calm_bodypaint",
        "duo_deep_sea_bodypaint",
        # G2 대비형 트리오 추가 (6종)
        "trio_sun_moon_star_bodypaint",
        "trio_three_oceans_bodypaint",
        "trio_three_civilizations_bodypaint",
        "trio_fire_water_earth_bodypaint",
        "trio_angel_human_demon_bodypaint",
        "trio_three_big_cats_bodypaint",
        # G3 연결형 듀오 추가 (6종)
        "duo_dna_helix_bodypaint",
        "duo_solar_eclipse_bodypaint",
        "duo_human_shadow_bodypaint",
        "duo_tiger_split_bodypaint",
        "duo_starry_night_split_bodypaint",
        "duo_peacock_split_bodypaint",
        # G4 연결형 트리오 추가 (6종)
        "trio_last_supper_bodypaint",
        "trio_rainbow_arc_bodypaint",
        "trio_milky_way_panorama_bodypaint",
        "trio_coral_reef_zones_bodypaint",
        "trio_creation_of_adam_bodypaint",
        "trio_poles_and_equator_bodypaint",
        # 4인 QUAD (5종)
        "quad_four_seasons_bodypaint",
        "quad_four_elements_bodypaint",
        "quad_four_directions_bodypaint",
        "quad_four_seasons_klimt_bodypaint",
        "quad_rgba_spectrum_bodypaint",
        # 5인 QUINT (4종)
        "quint_five_continents_bodypaint",
        "quint_five_elements_asia_bodypaint",
        "quint_rainbow_five_bodypaint",
        "quint_five_oceans_bodypaint",
    ],'''

# ══════════════════════════════════════════════
# PATCH 2: SSS_TIER에 추가
# ══════════════════════════════════════════════

SSS_OLD = '''    # 2026-06-29 멀티 바디페인팅 24종 전원 SSS'''

SSS_NEW = '''    # 2026-06-29 멀티 바디페인팅 v3 확장 33종 (검증 후 추가)
    # G1 대비형 듀오 추가
    "duo_east_and_west_bodypaint",
    "duo_macro_and_micro_bodypaint",
    "duo_ancient_and_future_bodypaint",
    "duo_poison_and_medicine_bodypaint",
    "duo_storm_and_calm_bodypaint",
    "duo_deep_sea_bodypaint",
    # G2 대비형 트리오 추가
    "trio_sun_moon_star_bodypaint",
    "trio_three_oceans_bodypaint",
    "trio_three_civilizations_bodypaint",
    "trio_fire_water_earth_bodypaint",
    "trio_angel_human_demon_bodypaint",
    "trio_three_big_cats_bodypaint",
    # G3 연결형 듀오 추가
    "duo_dna_helix_bodypaint",
    "duo_solar_eclipse_bodypaint",
    "duo_human_shadow_bodypaint",
    "duo_tiger_split_bodypaint",
    "duo_starry_night_split_bodypaint",
    "duo_peacock_split_bodypaint",
    # G4 연결형 트리오 추가
    "trio_last_supper_bodypaint",
    "trio_rainbow_arc_bodypaint",
    "trio_milky_way_panorama_bodypaint",
    "trio_coral_reef_zones_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_poles_and_equator_bodypaint",
    # 4인 QUAD
    "quad_four_seasons_bodypaint",
    "quad_four_elements_bodypaint",
    "quad_four_directions_bodypaint",
    "quad_four_seasons_klimt_bodypaint",
    "quad_rgba_spectrum_bodypaint",
    # 5인 QUINT
    "quint_five_continents_bodypaint",
    "quint_five_elements_asia_bodypaint",
    "quint_rainbow_five_bodypaint",
    "quint_five_oceans_bodypaint",
    # 2026-06-29 멀티 바디페인팅 24종 전원 SSS'''

# ══════════════════════════════════════════════
# PATCH 3: SS_TIER에 추가
# ══════════════════════════════════════════════

SS_OLD = '''    # 2026-06-29 멀티 바디페인팅 SS (SSS 24종 포함)'''

SS_NEW = '''    # 2026-06-29 멀티 바디페인팅 v3 확장 33종 SS (SSS 포함)
    "duo_east_and_west_bodypaint",
    "duo_macro_and_micro_bodypaint",
    "duo_ancient_and_future_bodypaint",
    "duo_poison_and_medicine_bodypaint",
    "duo_storm_and_calm_bodypaint",
    "duo_deep_sea_bodypaint",
    "trio_sun_moon_star_bodypaint",
    "trio_three_oceans_bodypaint",
    "trio_three_civilizations_bodypaint",
    "trio_fire_water_earth_bodypaint",
    "trio_angel_human_demon_bodypaint",
    "trio_three_big_cats_bodypaint",
    "duo_dna_helix_bodypaint",
    "duo_solar_eclipse_bodypaint",
    "duo_human_shadow_bodypaint",
    "duo_tiger_split_bodypaint",
    "duo_starry_night_split_bodypaint",
    "duo_peacock_split_bodypaint",
    "trio_last_supper_bodypaint",
    "trio_rainbow_arc_bodypaint",
    "trio_milky_way_panorama_bodypaint",
    "trio_coral_reef_zones_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_poles_and_equator_bodypaint",
    "quad_four_seasons_bodypaint",
    "quad_four_elements_bodypaint",
    "quad_four_directions_bodypaint",
    "quad_four_seasons_klimt_bodypaint",
    "quad_rgba_spectrum_bodypaint",
    "quint_five_continents_bodypaint",
    "quint_five_elements_asia_bodypaint",
    "quint_rainbow_five_bodypaint",
    "quint_five_oceans_bodypaint",
    # 2026-06-29 멀티 바디페인팅 SS (SSS 24종 포함)'''

# ══════════════════════════════════════════════
# 적용
# ══════════════════════════════════════════════

def apply_patch():
    if not DASHBOARD.exists():
        print(f"❌ 파일 없음: {DASHBOARD}")
        return False

    content = DASHBOARD.read_text(encoding="utf-8")
    original = content

    # PATCH 1
    if CAT_OLD not in content:
        print("❌ PATCH 1 앵커 없음")
        return False
    content = content.replace(CAT_OLD, CAT_NEW, 1)
    print("✅ PATCH 1: 카테고리 33종 추가 완료")

    # PATCH 2
    if SSS_OLD not in content:
        print("❌ PATCH 2 앵커 없음")
        return False
    content = content.replace(SSS_OLD, SSS_NEW, 1)
    print("✅ PATCH 2: SSS_TIER 33종 추가 완료")

    # PATCH 3
    if SS_OLD not in content:
        print("❌ PATCH 3 앵커 없음")
        return False
    content = content.replace(SS_OLD, SS_NEW, 1)
    print("✅ PATCH 3: SS_TIER 33종 추가 완료")

    if content == original:
        print("⚠️ 변경사항 없음")
        return False

    backup = DASHBOARD.with_suffix(".py.bak")
    backup.write_text(original, encoding="utf-8")
    print(f"💾 백업: {backup}")

    DASHBOARD.write_text(content, encoding="utf-8")
    print(f"✅ 저장: {DASHBOARD}")
    return True


if __name__ == "__main__":
    print("🎨 멀티 바디페인팅 v3 패치 적용\n")
    print("추가: 33종 (G1+6 G2+6 G3+6 G4+6 QUAD5 QUINT4)\n")
    success = apply_patch()
    if success:
        print("\n✅ 모든 패치 완료!")
        print("\n다음 단계:")
        print("  1. PowerShell 검증:")
        print('     Select-String "quad_four_seasons_bodypaint" dashboard.py')
        print("  2. git add -A; git commit -m '🎨 멀티 바디페인팅 v3 카테고리+티어 패치 (33종 추가, 총 57종)'; git push")
    else:
        print("\n❌ 패치 실패")
