# -*- coding: utf-8 -*-
"""
presets_meta.py 패치 - 4개 신규 카테고리 + SSS/SS 추가
실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_meta_categories.py
"""

import sys
import os

META_FILE = "core/presets_meta.py"

NEW_CATEGORIES = """
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

    "\U0001f578\ufe0f Spider Silk Glamour": [
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

    "\U0001f32a\ufe0f Vortex Glamour": [
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
}"""

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

if not os.path.exists(META_FILE):
    print(f"ERROR: {META_FILE} 없음. LumineX 루트에서 실행하세요.")
    sys.exit(1)

with open(META_FILE, encoding="utf-8-sig") as f:
    content = f.read()

changed = False

# ── 1. 카테고리 블록 추가 ──────────────────────────
if "Dark Fantasy Glamour" in content:
    print("[META] 카테고리 이미 존재 — 스킵")
else:
    ANCHOR = "from core.hof_tier import HOF_TIER  # HOF 추가는 core/hof_tier.py에서"

    if ANCHOR not in content:
        print("[META] ERROR: from core.hof_tier 앵커 없음")
        sys.exit(1)

    anchor_idx = content.index(ANCHOR)
    before_anchor = content[:anchor_idx]
    last_brace_idx = before_anchor.rfind("}")

    if last_brace_idx == -1:
        print("[META] ERROR: PRESET_CATEGORIES 닫는 } 없음")
        sys.exit(1)

    content = content[:last_brace_idx] + NEW_CATEGORIES + "\n\n\n" + content[anchor_idx:]
    print("[META] ✅ 4개 카테고리 블록 추가 완료")
    print("       - Dark Fantasy Glamour (12종)")
    print("       - Bioluminescence Glamour (12종)")
    print("       - Spider Silk Glamour (12종)")
    print("       - Vortex Glamour (12종)")
    changed = True

# ── 2. SSS 추가 ────────────────────────────────────
if '"dark_amazon_valkyrie"' in content:
    print("[SSS] 이미 존재 — 스킵")
else:
    SSS_ANCHOR = "SSS_TIER = {"
    if SSS_ANCHOR not in content:
        print("[SSS] ERROR: SSS_TIER 앵커 없음")
        sys.exit(1)
    content = content.replace(SSS_ANCHOR, SSS_ANCHOR + NEW_SSS, 1)
    print("[SSS] ✅ SSS 18종 추가 완료")
    changed = True

# ── 3. SS 추가 ─────────────────────────────────────
if '"silk_supermodel_spiral_web"' in content:
    print("[SS] 이미 존재 — 스킵")
else:
    SS_ANCHOR = "SS_TIER = {"
    if SS_ANCHOR not in content:
        print("[SS] ERROR: SS_TIER 앵커 없음")
        sys.exit(1)
    content = content.replace(SS_ANCHOR, SS_ANCHOR + NEW_SS, 1)
    print("[SS] ✅ SS 4종 추가 완료")
    changed = True

# ── 저장 ───────────────────────────────────────────
if changed:
    with open(META_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("\n✅ presets_meta.py 저장 완료")
else:
    print("\n변경사항 없음")

print("\n다음 단계:")
print("  python preset_builders/generate_new_category_jsons.py")
print('  git add core/hof_tier.py core/presets_meta.py presets/')
print('  git commit -m "feat: Dark Fantasy/Bio/Silk/Vortex 카테고리+SSS/SS 티어 추가"')
print("  git push")
