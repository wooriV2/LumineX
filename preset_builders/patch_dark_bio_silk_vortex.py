# -*- coding: utf-8 -*-
"""
patch_dark_bio_silk_vortex.py
Dark Fantasy / Bioluminescence / Spider Silk / Vortex
HOF + SSS 패치 + JSON 생성
실행: python preset_builders/patch_dark_bio_silk_vortex.py
"""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# ── 1. HOF/SSS 데이터 ────────────────────────────────────────

NEW_HOF = {
    # 👑 Dark Fantasy
    "dark_super_glamour_succubus",
    "dark_bbw_earth_witch",
    "dark_bust_queen_vampire",
    "dark_vs_angel_fallen_angel",
    "dark_supermodel_ice_witch",
    # 🌊 Bioluminescence
    "bio_amazon_anglerfish_lure",
    "bio_plus_size_jellyfish_bloom",
    "bio_curvy_deep_sea_coral",
    "bio_athletic_comb_jelly_rainbow",
    "bio_supermodel_sea_sparkle",
    "bio_bbw_giant_squid_ink",
    "bio_black_glamour_viper_fish",
    "bio_vs_angel_crystal_medusa",
    # 🕸️ Spider Silk
    "silk_amazon_web_cathedral",
    "silk_petite_dew_drop_web",
    "silk_latina_web_veil",
    "silk_black_glamour_black_widow",
    "silk_vs_angel_dewdrop_cathedral",
    # 🌪️ Vortex
    "vortex_amazon_fire_tornado",
    "vortex_bbw_water_cyclone",
    "vortex_petite_sand_devil",
    "vortex_curvy_rose_tornado",
    "vortex_athletic_lightning_vortex",
    "vortex_latina_petal_whirlwind",
    "vortex_vs_angel_snow_vortex",
}

NEW_SSS = {
    # 👑 Dark Fantasy
    "dark_amazon_valkyrie",
    "dark_miniature_shadow_fairy",
    "dark_latina_blood_moon",
    "dark_black_glamour_void_queen",
    "dark_hot_glamour_dark_siren",
    "dark_brazil_jungle_goddess",
    "dark_powerlifter_war_goddess",
    # 🌊 Bioluminescence
    "bio_petite_firefly_swarm",
    "bio_latina_dinoflagellate",
    "bio_bust_queen_abyss_glow",
    "bio_powerlifter_hydrothermal",
    # 🕸️ Spider Silk
    "silk_bbw_cocoon_emergence",
    "silk_curvy_golden_silk_gown",
    "silk_athletic_web_armor",
    "silk_bbw_funnel_web_throne",
    "silk_powerlifter_web_cage",
    # 🌪️ Vortex
    "vortex_bbw_cloud_column",
    "vortex_bust_queen_aurora_vortex",
    "vortex_powerlifter_magma_vortex",  # 미판정 → SSS 임시
}

# ── 2. presets_meta.py HOF/SSS 패치 ─────────────────────────

META_PATH = ROOT / "core" / "presets_meta.py"
content = META_PATH.read_text(encoding="utf-8")

# SSS_TIER 앵커
SSS_ANCHOR = '"dark_super_glamour_succubus"'  # 이미 있을 경우 스킵

def add_ids_to_tier(content, tier_name, new_ids):
    """tier_name SET에 new_ids 추가 (중복 제외)"""
    import re
    pattern = rf'({tier_name}\s*=\s*\{{)(.*?)(\}})'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  ⚠️ {tier_name} 블록을 찾을 수 없습니다.")
        return content

    existing = match.group(2)
    to_add = []
    for id_ in sorted(new_ids):
        if f'"{id_}"' not in existing:
            to_add.append(f'    "{id_}",')

    if not to_add:
        print(f"  ℹ️ {tier_name}: 추가할 항목 없음 (이미 존재)")
        return content

    new_block = existing.rstrip() + "\n" + "\n".join(to_add) + "\n"
    result = content[:match.start(2)] + new_block + content[match.end(2):]
    print(f"  ✅ {tier_name}: {len(to_add)}개 추가")
    return result

# ── 3. hof_tier.py 패치 ──────────────────────────────────────

HOF_PATH = ROOT / "core" / "hof_tier.py"
hof_content = HOF_PATH.read_text(encoding="utf-8")

def add_ids_to_hof(content, new_ids):
    import re
    pattern = r'(HOF_TIER\s*=\s*\{)(.*?)(\})'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print("  ⚠️ HOF_TIER 블록을 찾을 수 없습니다.")
        return content

    existing = match.group(2)
    to_add = []
    for id_ in sorted(new_ids):
        if f'"{id_}"' not in existing:
            to_add.append(f'    "{id_}",')

    if not to_add:
        print("  ℹ️ HOF_TIER: 추가할 항목 없음")
        return content

    new_block = existing.rstrip() + "\n" + "\n".join(to_add) + "\n"
    result = content[:match.start(2)] + new_block + content[match.end(2):]
    print(f"  ✅ HOF_TIER: {len(to_add)}개 추가")
    return result

# ── 4. presets_meta.py에서 프롬프트 읽어 JSON 생성 ───────────

PRESETS_DIR = ROOT / "presets"

def generate_jsons():
    source = META_PATH.read_text(encoding="utf-8")
    code = compile(source, str(META_PATH), "exec")
    mod = {}
    exec(code, mod)
    PRESET_CATEGORIES = mod.get("PRESET_CATEGORIES", {})

    all_target = NEW_HOF | NEW_SSS
    created = []
    skipped = []

    for category, presets in PRESET_CATEGORIES.items():
        if not isinstance(presets, list):
            continue
        for preset in presets:
            if not isinstance(preset, dict):
                continue
            pid = preset.get("id")
            if pid not in all_target:
                continue
            json_path = PRESETS_DIR / f"{pid}.json"
            if json_path.exists():
                skipped.append(pid)
                continue
            data = {
                "id": pid,
                "prompt": preset.get("prompt", ""),
                "category": category,
            }
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            created.append(pid)

    print(f"\n  ✅ JSON 생성: {len(created)}개")
    print(f"  ⏭️  JSON 스킵: {len(skipped)}개")

# ── 5. 실행 ──────────────────────────────────────────────────

print("\n[ 1/3 ] presets_meta.py SSS_TIER 패치...")
content = add_ids_to_tier(content, "SSS_TIER", NEW_SSS)
META_PATH.write_text(content, encoding="utf-8")

print("\n[ 2/3 ] hof_tier.py HOF_TIER 패치...")
hof_content = add_ids_to_hof(hof_content, NEW_HOF)
HOF_PATH.write_text(hof_content, encoding="utf-8")

print("\n[ 3/3 ] JSON 파일 생성...")
generate_jsons()

print("\n✅ 패치 완료!")
print("다음 명령어로 커밋하세요:")
print('git add core/presets_meta.py core/hof_tier.py presets/')
print('git commit -m "feat: Dark Fantasy/Bio/Silk/Vortex HOF+SSS 패치 + JSON 생성"')
print('git push')
