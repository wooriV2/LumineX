# -*- coding: utf-8 -*-
"""
LumineX 통합 패치 스크립트
작업 1: hof_tier.py - vortex_powerlifter_magma_vortex HOF 추가
작업 2: presets_meta.py - Dark Fantasy / Bioluminescence / Spider Silk / Vortex 카테고리 블록 추가

실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_vortex_final_and_new_categories.py
"""

import sys
import os

HOF_FILE = "core/hof_tier.py"
META_FILE = "core/presets_meta.py"

# ──────────────────────────────────────────────
# 작업 1: hof_tier.py 패치
# ──────────────────────────────────────────────

HOF_ANCHOR = '    "vortex_vs_angel_snow_vortex",'
HOF_INSERT = '''    "vortex_vs_angel_snow_vortex",
    "vortex_powerlifter_magma_vortex",'''

def patch_hof():
    with open(HOF_FILE, encoding="utf-8") as f:
        content = f.read()

    if "vortex_powerlifter_magma_vortex" in content:
        print("[HOF] 이미 존재: vortex_powerlifter_magma_vortex — 스킵")
        return

    if HOF_ANCHOR not in content:
        print(f"[HOF] ERROR: 앵커를 찾을 수 없습니다: {HOF_ANCHOR}")
        sys.exit(1)

    content = content.replace(HOF_ANCHOR, HOF_INSERT)

    with open(HOF_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print("[HOF] ✅ vortex_powerlifter_magma_vortex HOF 추가 완료")


# ──────────────────────────────────────────────
# 작업 2: presets_meta.py - 4개 카테고리 블록 추가
# ──────────────────────────────────────────────

NEW_CATEGORIES = '''
    "🌑 Dark Fantasy Glamour": [
        "dark_super_glamour_succubus",
        "dark_bbw_earth_witch",
        "dark_bust_queen_vampire",
        "dark_vs_angel_fallen_angel",
        "dark_supermodel_ice_witch",
        "dark_amazon_valkyrie",
        "dark_miniature_shadow_fairy",
        "dark_latina_blood_moon",
        "dark_black_glamour_void_queen",
        "dark_hot_glamour_dark_siren",
        "dark_brazil_jungle_goddess",
        "dark_powerlifter_war_goddess",
    ],

    "🌊 Bioluminescence Glamour": [
        "bio_amazon_anglerfish_lure",
        "bio_plus_size_jellyfish_bloom",
        "bio_curvy_deep_sea_coral",
        "bio_athletic_comb_jelly_rainbow",
        "bio_supermodel_sea_sparkle",
        "bio_bbw_giant_squid_ink",
        "bio_black_glamour_viper_fish",
        "bio_vs_angel_crystal_medusa",
        "bio_petite_firefly_swarm",
        "bio_latina_dinoflagellate",
        "bio_bust_queen_abyss_glow",
        "bio_powerlifter_hydrothermal",
    ],

    "🕸️ Spider Silk Glamour": [
        "silk_amazon_web_cathedral",
        "silk_petite_dew_drop_web",
        "silk_latina_web_veil",
        "silk_black_glamour_black_widow",
        "silk_vs_angel_dewdrop_cathedral",
        "silk_bbw_cocoon_emergence",
        "silk_curvy_golden_silk_gown",
        "silk_athletic_web_armor",
        "silk_bbw_funnel_web_throne",
        "silk_powerlifter_web_cage",
        "silk_supermodel_spiral_web",
        "silk_bust_queen_orb_web",
    ],

    "🌪️ Vortex Glamour": [
        "vortex_amazon_fire_tornado",
        "vortex_bbw_water_cyclone",
        "vortex_petite_sand_devil",
        "vortex_curvy_rose_tornado",
        "vortex_athletic_lightning_vortex",
        "vortex_latina_petal_whirlwind",
        "vortex_vs_angel_snow_vortex",
        "vortex_powerlifter_magma_vortex",
        "vortex_bbw_cloud_column",
        "vortex_bust_queen_aurora_vortex",
        "vortex_supermodel_galaxy_spiral",
        "vortex_black_glamour_void_spiral",
    ],
'''

# presets_meta.py 삽입 앵커: from core.hof_tier import HOF_TIER 바로 위
META_ANCHOR = 'from core.hof_tier import HOF_TIER'

def patch_meta():
    with open(META_FILE, encoding="utf-8-sig") as f:
        content = f.read()

    # 이미 추가됐는지 확인
    already = []
    for marker in ['"🌑 Dark Fantasy Glamour"', '"🌊 Bioluminescence Glamour"',
                   '"🕸️ Spider Silk Glamour"', '"🌪️ Vortex Glamour"']:
        if marker in content:
            already.append(marker)

    if len(already) == 4:
        print("[META] 4개 카테고리 모두 이미 존재 — 스킵")
        return

    if already:
        print(f"[META] 일부 카테고리 이미 존재: {already}")
        print("[META] 나머지만 추가하려면 수동 확인 필요. 스킵.")
        return

    if META_ANCHOR not in content:
        print(f"[META] ERROR: 앵커를 찾을 수 없습니다: {META_ANCHOR}")
        sys.exit(1)

    # PRESET_CATEGORIES 닫는 } 바로 앞에 삽입
    # 앵커: 'from core.hof_tier import HOF_TIER' 직전의 '}\n\n\n'
    # 더 안전하게: PRESET_CATEGORIES 딕셔너리 마지막 } 찾기
    # hof_tier import 바로 위에 카테고리 블록 삽입
    insert_target = '\n}\n\n\n# HOF tier'
    insert_replacement = NEW_CATEGORIES + '\n}\n\n\n# HOF tier'

    if insert_target not in content:
        # 대안 앵커
        insert_target = '\n}\n\n\nfrom core.hof_tier import HOF_TIER'
        insert_replacement = NEW_CATEGORIES + '\n}\n\n\nfrom core.hof_tier import HOF_TIER'

    if insert_target not in content:
        print("[META] ERROR: 삽입 위치를 찾을 수 없습니다.")
        print("[META] 수동으로 PRESET_CATEGORIES 딕셔너리 끝 부분에 카테고리를 추가해주세요.")
        # 그래도 내용은 출력
        print("\n[META] 추가할 카테고리 블록:")
        print(NEW_CATEGORIES)
        sys.exit(1)

    content = content.replace(insert_target, insert_replacement, 1)

    with open(META_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print("[META] ✅ 4개 신규 카테고리 블록 추가 완료")
    print("       - 🌑 Dark Fantasy Glamour (12종: HOF 5, SSS 7)")
    print("       - 🌊 Bioluminescence Glamour (12종: HOF 8, SSS 4)")
    print("       - 🕸️ Spider Silk Glamour (12종: HOF 5, SSS 5, SS 2)")
    print("       - 🌪️ Vortex Glamour (12종: HOF 8, SSS 2, SS 2)")


# ──────────────────────────────────────────────
# SSS/SS 티어 추가 (presets_meta.py)
# ──────────────────────────────────────────────

NEW_SSS = """
    # 2026-07-14 Dark Fantasy / Bioluminescence / Spider Silk / Vortex SSS
    # Dark Fantasy SSS 7종
    "dark_amazon_valkyrie",
    "dark_miniature_shadow_fairy",
    "dark_latina_blood_moon",
    "dark_black_glamour_void_queen",
    "dark_hot_glamour_dark_siren",
    "dark_brazil_jungle_goddess",
    "dark_powerlifter_war_goddess",
    # Bioluminescence SSS 4종
    "bio_petite_firefly_swarm",
    "bio_latina_dinoflagellate",
    "bio_bust_queen_abyss_glow",
    "bio_powerlifter_hydrothermal",
    # Spider Silk SSS 5종
    "silk_bbw_cocoon_emergence",
    "silk_curvy_golden_silk_gown",
    "silk_athletic_web_armor",
    "silk_bbw_funnel_web_throne",
    "silk_powerlifter_web_cage",
    # Vortex SSS 2종
    "vortex_bbw_cloud_column",
    "vortex_bust_queen_aurora_vortex",
"""

NEW_SS = """
    # 2026-07-14 Spider Silk SS 2종 / Vortex SS 2종
    "silk_supermodel_spiral_web",
    "silk_bust_queen_orb_web",
    "vortex_supermodel_galaxy_spiral",
    "vortex_black_glamour_void_spiral",
"""

def patch_sss_ss():
    with open(META_FILE, encoding="utf-8-sig") as f:
        content = f.read()

    # SSS 삽입 확인
    if '"dark_amazon_valkyrie"' in content:
        print("[SSS] 이미 존재 — 스킵")
    else:
        # SSS_TIER = { 바로 다음 줄에 삽입
        sss_anchor = 'SSS_TIER = {'
        if sss_anchor in content:
            content = content.replace(sss_anchor, sss_anchor + NEW_SSS, 1)
            print("[SSS] ✅ 신규 카테고리 SSS 18종 추가 완료")
        else:
            print("[SSS] ERROR: SSS_TIER 앵커 없음")

    # SS 삽입 확인
    if '"silk_supermodel_spiral_web"' in content:
        print("[SS] 이미 존재 — 스킵")
    else:
        ss_anchor = 'SS_TIER = {'
        if ss_anchor in content:
            content = content.replace(ss_anchor, ss_anchor + NEW_SS, 1)
            print("[SS] ✅ SS 4종 추가 완료")
        else:
            print("[SS] ERROR: SS_TIER 앵커 없음")

    with open(META_FILE, "w", encoding="utf-8") as f:
        f.write(content)


# ──────────────────────────────────────────────
# 메인 실행
# ──────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("LumineX 통합 패치 시작")
    print("=" * 55)

    if not os.path.exists(HOF_FILE):
        print(f"ERROR: {HOF_FILE} 없음. LumineX 루트에서 실행하세요.")
        sys.exit(1)
    if not os.path.exists(META_FILE):
        print(f"ERROR: {META_FILE} 없음. LumineX 루트에서 실행하세요.")
        sys.exit(1)

    patch_hof()
    patch_meta()
    patch_sss_ss()

    print("=" * 55)
    print("모든 패치 완료!")
    print()
    print("다음 단계:")
    print("  1. JSON 생성: python preset_builders/generate_new_category_jsons.py")
    print("  2. 커밋:")
    print("     git add core/hof_tier.py core/presets_meta.py presets/")
    print('     git commit -m "feat: Vortex HOF 최종확정 + Dark Fantasy/Bio/Silk/Vortex 카테고리 추가"')
    print("     git push")
    print("=" * 55)
