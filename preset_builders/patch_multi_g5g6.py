"""
LumineX 멀티 바디페인팅 신규 65종 추가 패치
- G5 연결형 듀오 30종
- G6 대비형 트리오 35종
저장위치: C:\Dev\LumineX\preset_builders\
실행: python preset_builders/patch_multi_g5g6.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")
BACKUP    = Path("C:/Dev/LumineX/preset_builders/backup_pre_g5g6.py")

# ── PRESET_CATEGORIES 안 멀티 바디페인팅 카테고리 앵커 ──
# 기존 마지막 줄: "quint_five_oceans_bodypaint",
CAT_ANCHOR = '        "quint_five_oceans_bodypaint",'

CAT_INSERT = '''
        # G5 연결형 듀오 (30종) — 두 몸이 합쳐지면 하나의 완성체
        # 자연/우주
        "duo_earth_hemisphere_bodypaint",
        "duo_day_city_night_city_bodypaint",
        "duo_volcano_glacier_bodypaint",
        "duo_storm_eye_bodypaint",
        "duo_aurora_milkyway_bodypaint",
        "duo_coral_abyss_bodypaint",
        "duo_tree_root_bodypaint",
        "duo_lightning_rainbow_bodypaint",
        # 동물/생물
        "duo_eagle_serpent_bodypaint",
        "duo_wolf_moon_bodypaint",
        "duo_butterfly_cocoon_bodypaint",
        "duo_shark_whale_bodypaint",
        "duo_dragon_phoenix_bodypaint",
        "duo_lion_zebra_bodypaint",
        "duo_spider_web_bodypaint",
        # 명화/문화
        "duo_sistine_hands_bodypaint",
        "duo_mona_lisa_split_bodypaint",
        "duo_birth_venus_split_bodypaint",
        "duo_yin_yang_koi_bodypaint",
        "duo_chess_board_bodypaint",
        "duo_map_east_west_bodypaint",
        # SF/판타지
        "duo_android_human_bodypaint",
        "duo_black_hole_star_bodypaint",
        "duo_past_future_city_bodypaint",
        "duo_virus_antibody_bodypaint",
        "duo_matrix_reality_bodypaint",
        "duo_crystal_lava_bodypaint",
        # 인체/철학
        "duo_skeleton_bloom_bodypaint",
        "duo_shadow_light_figure_bodypaint",
        "duo_ink_wash_split_bodypaint",
        # G6 대비형 트리오 (35종) — 3 극단의 충돌/조화
        # 시간/역사
        "trio_stone_bronze_iron_bodypaint",
        "trio_ancient_medieval_modern_bodypaint",
        "trio_past_present_future_self_bodypaint",
        "trio_dawn_noon_dusk_bodypaint",
        "trio_birth_life_death_bodypaint",
        "trio_seed_tree_ash_bodypaint",
        # 원소/자연
        "trio_lightning_ocean_earthquake_bodypaint",
        "trio_sand_ice_magma_bodypaint",
        "trio_sky_earth_underground_bodypaint",
        "trio_micro_human_macro_bodypaint",
        "trio_fog_rain_snow_bodypaint",
        "trio_jungle_desert_tundra_bodypaint",
        # 색/빛
        "trio_primary_colors_bodypaint",
        "trio_black_white_gray_bodypaint",
        "trio_gold_silver_bronze_bodypaint",
        "trio_neon_pastel_dark_bodypaint",
        "trio_sunrise_sunset_moonrise_bodypaint",
        "trio_infrared_visible_uv_bodypaint",
        # 신화/종교
        "trio_heaven_earth_hell_bodypaint",
        "trio_creator_preserver_destroyer_bodypaint",
        "trio_fate_three_bodypaint",
        "trio_medusa_sphinx_hydra_bodypaint",
        "trio_valkyrie_siren_medea_bodypaint",
        # 문명/지역
        "trio_amazon_sahara_arctic_bodypaint",
        "trio_east_west_south_bodypaint",
        "trio_viking_samurai_spartan_bodypaint",
        "trio_geisha_odalisque_gisaeng_bodypaint",
        "trio_nile_amazon_yangtze_bodypaint",
        "trio_rome_babylon_aztec_bodypaint",
        # 감정/철학
        "trio_love_war_peace_bodypaint",
        "trio_fear_anger_joy_bodypaint",
        "trio_order_chaos_void_bodypaint",
        "trio_predator_prey_scavenger_bodypaint",
        "trio_id_ego_superego_bodypaint",
        "trio_thesis_antithesis_synthesis_bodypaint",'''

# ── SSS_TIER 앵커: QUINT 확정 주석 뒤 ──
SSS_ANCHOR = '    "quint_five_oceans_bodypaint",'

SSS_INSERT = '''
    # G5 연결형 듀오 30종 (검증 예정)
    "duo_earth_hemisphere_bodypaint",
    "duo_day_city_night_city_bodypaint",
    "duo_volcano_glacier_bodypaint",
    "duo_storm_eye_bodypaint",
    "duo_aurora_milkyway_bodypaint",
    "duo_coral_abyss_bodypaint",
    "duo_tree_root_bodypaint",
    "duo_lightning_rainbow_bodypaint",
    "duo_eagle_serpent_bodypaint",
    "duo_wolf_moon_bodypaint",
    "duo_butterfly_cocoon_bodypaint",
    "duo_shark_whale_bodypaint",
    "duo_dragon_phoenix_bodypaint",
    "duo_lion_zebra_bodypaint",
    "duo_spider_web_bodypaint",
    "duo_sistine_hands_bodypaint",
    "duo_mona_lisa_split_bodypaint",
    "duo_birth_venus_split_bodypaint",
    "duo_yin_yang_koi_bodypaint",
    "duo_chess_board_bodypaint",
    "duo_map_east_west_bodypaint",
    "duo_android_human_bodypaint",
    "duo_black_hole_star_bodypaint",
    "duo_past_future_city_bodypaint",
    "duo_virus_antibody_bodypaint",
    "duo_matrix_reality_bodypaint",
    "duo_crystal_lava_bodypaint",
    "duo_skeleton_bloom_bodypaint",
    "duo_shadow_light_figure_bodypaint",
    "duo_ink_wash_split_bodypaint",
    # G6 대비형 트리오 35종 (검증 예정)
    "trio_stone_bronze_iron_bodypaint",
    "trio_ancient_medieval_modern_bodypaint",
    "trio_past_present_future_self_bodypaint",
    "trio_dawn_noon_dusk_bodypaint",
    "trio_birth_life_death_bodypaint",
    "trio_seed_tree_ash_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_micro_human_macro_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    "trio_jungle_desert_tundra_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_neon_pastel_dark_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    "trio_heaven_earth_hell_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_valkyrie_siren_medea_bodypaint",
    "trio_amazon_sahara_arctic_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_geisha_odalisque_gisaeng_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_love_war_peace_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_predator_prey_scavenger_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint",'''

# ── SS_TIER 앵커: SSS와 동일 위치 (두 번째 출현) ──
SS_INSERT = SSS_INSERT  # 동일 내용


def apply_patch(content: str) -> str:

    # ── STEP 1: PRESET_CATEGORIES 카테고리 목록에 추가 ──
    idx = content.find(CAT_ANCHOR)
    if idx == -1:
        print("  [ERROR] PRESET_CATEGORIES 앵커 미발견!")
        return content
    line_end = content.find('\n', idx)
    content = content[:line_end + 1] + CAT_INSERT + '\n' + content[line_end + 1:]
    print("  [OK] PRESET_CATEGORIES 65종 추가")

    # ── STEP 2: SSS_TIER에 추가 (첫 번째 quint_five_oceans 출현) ──
    idx2 = content.find(SSS_ANCHOR)
    if idx2 == -1:
        print("  [ERROR] SSS_TIER 앵커 미발견!")
        return content
    line_end2 = content.find('\n', idx2)
    content = content[:line_end2 + 1] + SSS_INSERT + '\n' + content[line_end2 + 1:]
    print("  [OK] SSS_TIER 65종 추가")

    # ── STEP 3: SS_TIER에 추가 (두 번째 quint_five_oceans 출현) ──
    # SSS 삽입으로 인해 위치가 밀렸으므로 다시 탐색
    search_start = idx2 + len(SSS_ANCHOR) + len(SSS_INSERT) + 100
    idx3 = content.find(SSS_ANCHOR, search_start)
    if idx3 == -1:
        # 세 번째 출현 탐색 (PRESET_CATEGORIES에도 있음)
        idx3 = content.find(SSS_ANCHOR, idx2 + len(SSS_INSERT) + 500)
    if idx3 == -1:
        print("  [WARN] SS_TIER 앵커 미발견 — SS 추가 스킵")
    else:
        line_end3 = content.find('\n', idx3)
        content = content[:line_end3 + 1] + SS_INSERT + '\n' + content[line_end3 + 1:]
        print("  [OK] SS_TIER 65종 추가")

    return content


def verify(content: str):
    print("\n── 검증 ──────────────────────────────────")
    samples = [
        "duo_earth_hemisphere_bodypaint",
        "duo_dragon_phoenix_bodypaint",
        "duo_sistine_hands_bodypaint",
        "duo_ink_wash_split_bodypaint",
        "trio_stone_bronze_iron_bodypaint",
        "trio_heaven_earth_hell_bodypaint",
        "trio_geisha_odalisque_gisaeng_bodypaint",
        "trio_thesis_antithesis_synthesis_bodypaint",
    ]
    all_ok = True
    for s in samples:
        count = content.count(f'"{s}"')
        ok = count >= 2  # PRESET_CATEGORIES + SSS_TIER 최소 2회
        status = f"✅ {count}회" if ok else f"❌ {count}회"
        print(f"  {s}: {status}")
        if not ok:
            all_ok = False

    total_new = sum(content.count(f'"{s}"') for s in [
        "duo_earth_hemisphere_bodypaint","duo_day_city_night_city_bodypaint",
        "duo_volcano_glacier_bodypaint","duo_storm_eye_bodypaint",
        "trio_stone_bronze_iron_bodypaint","trio_thesis_antithesis_synthesis_bodypaint",
    ])
    print(f"\n  전체 상태: {'✅ 정상' if all_ok else '❌ 오류 있음'}")
    print(f"  샘플 6종 총 출현: {total_new}회 (기대값 12+)")


def main():
    if not DASHBOARD.exists():
        print(f"[ERROR] {DASHBOARD} 없음")
        return

    content = DASHBOARD.read_text(encoding='utf-8')
    BACKUP.parent.mkdir(exist_ok=True)
    BACKUP.write_text(content, encoding='utf-8')
    print(f"[INFO] 백업: {BACKUP}")
    print(f"[INFO] 원본 길이: {len(content):,}자\n")

    print("── 패치 적용 ──────────────────────────────")
    patched = apply_patch(content)

    verify(patched)

    DASHBOARD.write_text(patched, encoding='utf-8')
    print(f"\n[OK] 저장 완료: {DASHBOARD}")
    print(f"     +{len(patched) - len(content):,}자")
    print("\n다음 단계:")
    print("  1. streamlit run dashboard.py 로 동작 확인")
    print("  2. 검증 후:")
    print("     git add dashboard.py")
    print("     git commit -m '멀티바디페인팅 G5연결형듀오30종+G6대비형트리오35종 신설'")


if __name__ == '__main__':
    main()
