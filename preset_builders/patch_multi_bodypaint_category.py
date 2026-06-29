"""
patch_multi_bodypaint_category.py
dashboard.py에 🎨 멀티 바디페인팅 카테고리 추가
적용: str.replace 앵커 방식
"""

# ── 삽입 위치: "👯 듀오 글래머" 카테고리 바로 앞 ──
OLD = '''    "👯 듀오 글래머": ['''

NEW = '''    "🎨 멀티 바디페인팅": [
        # G1 대비형 듀오 (2인, 반대 테마 충돌/조화)
        "duo_fire_and_ice_bodypaint",
        "duo_day_and_night_bodypaint",
        "duo_bloom_and_void_bodypaint",
        "duo_gold_and_shadow_bodypaint",
        "duo_ocean_and_desert_bodypaint",
        "duo_circuit_and_nature_bodypaint",
        # G2 대비형 트리오 (3인, 삼원 대비)
        "trio_rgb_trinity_bodypaint",
        "trio_earth_water_sky_bodypaint",
        "trio_past_present_future_bodypaint",
        "trio_predator_prey_apex_bodypaint",
        "trio_ink_gold_chrome_bodypaint",
        "trio_season_trinity_bodypaint",
        # G3 연결형 듀오 (2인, 합치면 하나의 작품)
        "duo_butterfly_split_bodypaint",
        "duo_yin_yang_merge_bodypaint",
        "duo_world_map_bodypaint",
        "duo_klimt_tree_bodypaint",
        "duo_galaxy_split_bodypaint",
        "duo_wave_hokusai_bodypaint",
        # G4 연결형 트리오 (3인, 합치면 거대한 작품)
        "trio_triptych_klimt_bodypaint",
        "trio_phoenix_rising_bodypaint",
        "trio_world_tree_bodypaint",
        "trio_ocean_depth_bodypaint",
        "trio_aurora_spectrum_bodypaint",
        "trio_cosmic_creation_bodypaint",
    ],
    "👯 듀오 글래머": ['''

print("=== 멀티 바디페인팅 카테고리 패치 ===")
print(f"삽입 앵커: '👯 듀오 글래머' 바로 앞")
print(f"신규 프리셋: 24종 (G1×6 + G2×6 + G3×6 + G4×6)")
print()
print("--- str.replace 패치 코드 ---")
print()
print(f"OLD (앵커):")
print(repr(OLD[:60]))
print()
print(f"NEW (삽입 후):")
print(repr(NEW[:120]))
