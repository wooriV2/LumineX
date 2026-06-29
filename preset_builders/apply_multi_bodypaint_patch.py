"""
apply_multi_bodypaint_patch.py
dashboard.py에 멀티 바디페인팅 카테고리 + 티어 패치 실제 적용
실행: python apply_multi_bodypaint_patch.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

# ══════════════════════════════════════════════
# PATCH 1: PRESET_CATEGORIES에 카테고리 추가
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

# ══════════════════════════════════════════════
# PATCH 2: SSS_TIER에 추가
# ══════════════════════════════════════════════

SSS_OLD = '''    # 듀오 글래머 SS (SSS 23종 + SS전용 5종)'''

SSS_ADDITION = '''    # 2026-06-29 멀티 바디페인팅 24종 전원 SSS
    # G1 대비형 듀오
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
    "duo_klimt_tree_bodypaint",
    "duo_galaxy_split_bodypaint",
    "duo_wave_hokusai_bodypaint",
    # G4 연결형 트리오
    "trio_triptych_klimt_bodypaint",
    "trio_phoenix_rising_bodypaint",
    "trio_world_tree_bodypaint",
    "trio_ocean_depth_bodypaint",
    "trio_aurora_spectrum_bodypaint",
    "trio_cosmic_creation_bodypaint",
    # 듀오 글래머 SS (SSS 23종 + SS전용 5종)'''

# ══════════════════════════════════════════════
# PATCH 3: SS_TIER에 추가
# ══════════════════════════════════════════════

SS_OLD = '''    # 2026-06-26 한국 역사 & 궁중 글래머 SS (78종 전체)'''

SS_ADDITION = '''    # 2026-06-29 멀티 바디페인팅 SS (SSS 24종 포함)
    "duo_fire_and_ice_bodypaint",
    "duo_day_and_night_bodypaint",
    "duo_bloom_and_void_bodypaint",
    "duo_gold_and_shadow_bodypaint",
    "duo_ocean_and_desert_bodypaint",
    "duo_circuit_and_nature_bodypaint",
    "trio_rgb_trinity_bodypaint",
    "trio_earth_water_sky_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_predator_prey_apex_bodypaint",
    "trio_ink_gold_chrome_bodypaint",
    "trio_season_trinity_bodypaint",
    "duo_butterfly_split_bodypaint",
    "duo_yin_yang_merge_bodypaint",
    "duo_world_map_bodypaint",
    "duo_klimt_tree_bodypaint",
    "duo_galaxy_split_bodypaint",
    "duo_wave_hokusai_bodypaint",
    "trio_triptych_klimt_bodypaint",
    "trio_phoenix_rising_bodypaint",
    "trio_world_tree_bodypaint",
    "trio_ocean_depth_bodypaint",
    "trio_aurora_spectrum_bodypaint",
    "trio_cosmic_creation_bodypaint",
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
        print("❌ PATCH 1 앵커 없음")
        return False
    content = content.replace(CAT_OLD, CAT_NEW, 1)
    print("✅ PATCH 1: 카테고리 추가 완료")

    # PATCH 2
    if SSS_OLD not in content:
        print("❌ PATCH 2 앵커 없음")
        return False
    content = content.replace(SSS_OLD, SSS_ADDITION, 1)
    print("✅ PATCH 2: SSS_TIER 추가 완료")

    # PATCH 3
    if SS_OLD not in content:
        print("❌ PATCH 3 앵커 없음")
        return False
    content = content.replace(SS_OLD, SS_ADDITION, 1)
    print("✅ PATCH 3: SS_TIER 추가 완료")

    if content == original:
        print("⚠️ 변경사항 없음 (이미 패치 적용됨?)")
        return False

    # 백업
    backup = DASHBOARD.with_suffix(".py.bak")
    backup.write_text(original, encoding="utf-8")
    print(f"💾 백업: {backup}")

    # 저장
    DASHBOARD.write_text(content, encoding="utf-8")
    print(f"✅ 저장: {DASHBOARD}")
    return True


if __name__ == "__main__":
    print("🎨 멀티 바디페인팅 패치 적용\n")
    success = apply_patch()
    if success:
        print("\n✅ 모든 패치 완료!")
        print("\n다음 단계:")
        print("  1. python generate_multi_bodypaint_presets.py  # JSON 24종 생성")
        print("  2. PowerShell로 검증:")
        print('     Select-String "멀티 바디페인팅" dashboard.py')
        print("  3. git add -A && git commit -m '🎨 멀티 바디페인팅 신설 (24종, G1~G4)'")
    else:
        print("\n❌ 패치 실패 — 수동 확인 필요")
