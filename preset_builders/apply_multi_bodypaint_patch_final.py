"""
apply_multi_bodypaint_patch_final.py
멀티 바디페인팅 카테고리 신설 + 57종 전체 + SSS/SS 한 번에 적용
실행: python preset_builders/apply_multi_bodypaint_patch_final.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

# ══════════════════════════════════════════════
# PATCH 1: 카테고리 신설 (👯 듀오 글래머 바로 앞)
# ══════════════════════════════════════════════

CAT_OLD = '''    "👯 듀오 글래머": ['''

CAT_NEW = '''    "🎨 멀티 바디페인팅": [
        # G1 대비형 듀오 (2인, 반대 테마 충돌/조화)
        "duo_fire_and_ice_bodypaint",
        "duo_day_and_night_bodypaint",
        "duo_bloom_and_void_bodypaint",
        "duo_gold_and_shadow_bodypaint",
        "duo_ocean_and_desert_bodypaint",
        "duo_circuit_and_nature_bodypaint",
        # G1 대비형 듀오 추가 (6종)
        "duo_east_and_west_bodypaint",
        "duo_macro_and_micro_bodypaint",
        "duo_ancient_and_future_bodypaint",
        "duo_poison_and_medicine_bodypaint",
        "duo_storm_and_calm_bodypaint",
        "duo_deep_sea_bodypaint",
        # G2 대비형 트리오 (3인, 삼원 대비)
        "trio_rgb_trinity_bodypaint",
        "trio_earth_water_sky_bodypaint",
        "trio_past_present_future_bodypaint",
        "trio_predator_prey_apex_bodypaint",
        "trio_ink_gold_chrome_bodypaint",
        "trio_season_trinity_bodypaint",
        # G2 대비형 트리오 추가 (6종)
        "trio_sun_moon_star_bodypaint",
        "trio_three_oceans_bodypaint",
        "trio_three_civilizations_bodypaint",
        "trio_fire_water_earth_bodypaint",
        "trio_angel_human_demon_bodypaint",
        "trio_three_big_cats_bodypaint",
        # G3 연결형 듀오 (2인, 합치면 하나의 작품)
        "duo_butterfly_split_bodypaint",
        "duo_yin_yang_merge_bodypaint",
        "duo_world_map_bodypaint",
        "duo_klimt_tree_bodypaint",
        "duo_galaxy_split_bodypaint",
        "duo_wave_hokusai_bodypaint",
        # G3 연결형 듀오 추가 (6종)
        "duo_dna_helix_bodypaint",
        "duo_solar_eclipse_bodypaint",
        "duo_human_shadow_bodypaint",
        "duo_tiger_split_bodypaint",
        "duo_starry_night_split_bodypaint",
        "duo_peacock_split_bodypaint",
        # G4 연결형 트리오 (3인, 합치면 거대한 작품)
        "trio_triptych_klimt_bodypaint",
        "trio_phoenix_rising_bodypaint",
        "trio_world_tree_bodypaint",
        "trio_ocean_depth_bodypaint",
        "trio_aurora_spectrum_bodypaint",
        "trio_cosmic_creation_bodypaint",
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
    ],
    "👯 듀오 글래머": ['''

# ══════════════════════════════════════════════
# PATCH 2: SSS_TIER에 추가
# ══════════════════════════════════════════════

# 기존 SSS_TIER의 듀오 글래머 블록 앞에 삽입
SSS_OLD = '''    # 듀오 글래머 SS (SSS 23종 + SS전용 5종)'''

SSS_NEW = '''    # 2026-06-29 멀티 바디페인팅 57종 SSS (검증 완료 24종 확정 + 33종 검증 예정)
    # G1 대비형 듀오 (24종 검증 완료 SSS)
    "duo_fire_and_ice_bodypaint",
    "duo_day_and_night_bodypaint",
    "duo_bloom_and_void_bodypaint",
    "duo_gold_and_shadow_bodypaint",
    "duo_ocean_and_desert_bodypaint",
    "duo_circuit_and_nature_bodypaint",
    # G2 대비형 트리오
    "trio_rgb_trinity_bodypaint",
    "trio_earth_water_sky_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_predator_prey_apex_bodypaint",
    "trio_ink_gold_chrome_bodypaint",
    "trio_season_trinity_bodypaint",
    # G3 연결형 듀오
    "duo_butterfly_split_bodypaint",
    "duo_yin_yang_merge_bodypaint",
    "duo_world_map_bodypaint",
    "duo_galaxy_split_bodypaint",
    "duo_wave_hokusai_bodypaint",
    # G3 SS (연결 컨셉 미달)
    # "duo_klimt_tree_bodypaint",  # SS 전용
    # G4 연결형 트리오
    "trio_triptych_klimt_bodypaint",
    "trio_phoenix_rising_bodypaint",
    "trio_world_tree_bodypaint",
    "trio_ocean_depth_bodypaint",
    "trio_aurora_spectrum_bodypaint",
    "trio_cosmic_creation_bodypaint",
    # G1 추가 (검증 예정)
    "duo_east_and_west_bodypaint",
    "duo_macro_and_micro_bodypaint",
    "duo_ancient_and_future_bodypaint",
    "duo_poison_and_medicine_bodypaint",
    "duo_storm_and_calm_bodypaint",
    "duo_deep_sea_bodypaint",
    # G2 추가 (검증 예정)
    "trio_sun_moon_star_bodypaint",
    "trio_three_oceans_bodypaint",
    "trio_three_civilizations_bodypaint",
    "trio_fire_water_earth_bodypaint",
    "trio_angel_human_demon_bodypaint",
    "trio_three_big_cats_bodypaint",
    # G3 추가 (검증 예정)
    "duo_dna_helix_bodypaint",
    "duo_solar_eclipse_bodypaint",
    "duo_human_shadow_bodypaint",
    "duo_tiger_split_bodypaint",
    "duo_starry_night_split_bodypaint",
    "duo_peacock_split_bodypaint",
    # G4 추가 (검증 예정)
    "trio_last_supper_bodypaint",
    "trio_rainbow_arc_bodypaint",
    "trio_milky_way_panorama_bodypaint",
    "trio_coral_reef_zones_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_poles_and_equator_bodypaint",
    # QUAD 4인 (검증 예정)
    "quad_four_seasons_bodypaint",
    "quad_four_elements_bodypaint",
    "quad_four_directions_bodypaint",
    "quad_four_seasons_klimt_bodypaint",
    "quad_rgba_spectrum_bodypaint",
    # QUINT 5인 (검증 예정)
    "quint_five_continents_bodypaint",
    "quint_five_elements_asia_bodypaint",
    "quint_rainbow_five_bodypaint",
    "quint_five_oceans_bodypaint",
    # 듀오 글래머 SS (SSS 23종 + SS전용 5종)'''

# ══════════════════════════════════════════════
# PATCH 3: SS_TIER에 추가
# ══════════════════════════════════════════════

SS_OLD = '''    # 2026-06-26 한국 역사 & 궁중 글래머 SS (78종 전체)'''

SS_NEW = '''    # 2026-06-29 멀티 바디페인팅 SS (57종 전체)
    "duo_fire_and_ice_bodypaint",
    "duo_day_and_night_bodypaint",
    "duo_bloom_and_void_bodypaint",
    "duo_gold_and_shadow_bodypaint",
    "duo_ocean_and_desert_bodypaint",
    "duo_circuit_and_nature_bodypaint",
    "duo_east_and_west_bodypaint",
    "duo_macro_and_micro_bodypaint",
    "duo_ancient_and_future_bodypaint",
    "duo_poison_and_medicine_bodypaint",
    "duo_storm_and_calm_bodypaint",
    "duo_deep_sea_bodypaint",
    "trio_rgb_trinity_bodypaint",
    "trio_earth_water_sky_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_predator_prey_apex_bodypaint",
    "trio_ink_gold_chrome_bodypaint",
    "trio_season_trinity_bodypaint",
    "trio_sun_moon_star_bodypaint",
    "trio_three_oceans_bodypaint",
    "trio_three_civilizations_bodypaint",
    "trio_fire_water_earth_bodypaint",
    "trio_angel_human_demon_bodypaint",
    "trio_three_big_cats_bodypaint",
    "duo_butterfly_split_bodypaint",
    "duo_yin_yang_merge_bodypaint",
    "duo_world_map_bodypaint",
    "duo_klimt_tree_bodypaint",
    "duo_galaxy_split_bodypaint",
    "duo_wave_hokusai_bodypaint",
    "duo_dna_helix_bodypaint",
    "duo_solar_eclipse_bodypaint",
    "duo_human_shadow_bodypaint",
    "duo_tiger_split_bodypaint",
    "duo_starry_night_split_bodypaint",
    "duo_peacock_split_bodypaint",
    "trio_triptych_klimt_bodypaint",
    "trio_phoenix_rising_bodypaint",
    "trio_world_tree_bodypaint",
    "trio_ocean_depth_bodypaint",
    "trio_aurora_spectrum_bodypaint",
    "trio_cosmic_creation_bodypaint",
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
    # 2026-06-26 한국 역사 & 궁중 글래머 SS (78종 전체)'''

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
        print("❌ PATCH 1 앵커 없음 — '👯 듀오 글래머' 카테고리를 찾을 수 없음")
        return False
    content = content.replace(CAT_OLD, CAT_NEW, 1)
    print("✅ PATCH 1: 🎨 멀티 바디페인팅 카테고리 신설 (57종)")

    # PATCH 2
    if SSS_OLD not in content:
        print("❌ PATCH 2 앵커 없음")
        return False
    content = content.replace(SSS_OLD, SSS_NEW, 1)
    print("✅ PATCH 2: SSS_TIER 추가 완료")

    # PATCH 3
    if SS_OLD not in content:
        print("❌ PATCH 3 앵커 없음")
        return False
    content = content.replace(SS_OLD, SS_NEW, 1)
    print("✅ PATCH 3: SS_TIER 추가 완료")

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
    print("🎨 멀티 바디페인팅 통합 패치 (카테고리 신설 + 57종)\n")
    success = apply_patch()
    if success:
        print("\n✅ 완료!")
        print("\n검증:")
        print('  Select-String "멀티 바디페인팅" dashboard.py')
        print('  Select-String "quad_four_seasons_bodypaint" dashboard.py')
        print("\n커밋:")
        print("  git add -A; git commit -m '🎨 멀티 바디페인팅 카테고리 신설 + 57종 (G1~G4 + QUAD + QUINT)'; git push")
    else:
        print("\n❌ 패치 실패")
