# -*- coding: utf-8 -*-
"""
LumineX 공식F 미니멀 오브제 커버 패치
작업 1: presets/ 폴더에 JSON 9개 생성
작업 2: core/presets_meta.py 에 카테고리 + HOF_TIER 추가
실행: python preset_builders/patch_formula_f_minimal.py (프로젝트 루트에서)
"""

import json
import os
import re
from pathlib import Path

PRESETS_DIR = Path("presets")
META_FILE   = Path("core/presets_meta.py")

# ══════════════════════════════════════════════════════════
# 1. 프리셋 JSON 데이터 (9종)
# ══════════════════════════════════════════════════════════

PRESET_DATA = {
    "silk_ribbon_minimal": {
        "name": "🎀 실크 리본 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Pure white seamless studio, soft diffused light from above",
        "outfit": "Single ivory silk ribbon draped across body, NO other clothing, NO fabric",
        "material": "Silk ribbon only — ultra-thin luminous silk, body fully visible",
        "lighting": "High-key soft box, ribbon casting fine shadow on skin",
        "pose": "Standing, ribbon trailing behind like a brushstroke",
        "style": "Minimalist fashion editorial, high-fashion couture",
        "negative": "no dress, no top, no underwear, no bikini, no additional fabric",
    },
    "tropical_flower_minimal": {
        "name": "🌺 트로피컬 플라워 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Lush tropical rainforest, morning mist, dappled sunlight through canopy",
        "outfit": "Single large tropical hibiscus flower held against body, NO clothing",
        "material": "Vivid magenta hibiscus petals, stamens visible, dewdrops on petals",
        "lighting": "Natural forest light, golden rim from behind, skin warm-toned",
        "pose": "Seated on mossy rock, one arm raised holding flower",
        "style": "Nature editorial, botanical fashion photography",
        "negative": "no dress, no top, no swimwear, no fabric, no lei",
    },
    "silver_foil_minimal": {
        "name": "✨ 실버 포일 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Infinite black void studio, mirror floor reflecting silver",
        "outfit": "Single crumpled sheet of silver foil pressed against body, NO clothing",
        "material": "Metallic silver mylar foil — reflective, angular, catching light",
        "lighting": "Dramatic single-source hard light, silver foil creating lens flares",
        "pose": "Standing, foil shaped like abstract sculpture against torso",
        "style": "High-concept editorial, avant-garde fashion, metallic art",
        "negative": "no dress, no top, no silver fabric, no jumpsuit",
    },
    "moss_stone_minimal": {
        "name": "🪨 이끼 스톤 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Ancient stone ruins in deep forest, emerald moss on every surface",
        "outfit": "Single large moss-covered stone slab held in front of body, NO clothing",
        "material": "Textured granite with thick velvet-green moss, soil and stone scent implied",
        "lighting": "Soft overcast forest light, green ambient from surrounding moss",
        "pose": "Standing between carved stone pillars, stone balanced against body",
        "style": "Environmental art editorial, nature goddess photography",
        "negative": "no dress, no clothing, no fabric, no leaves worn as outfit",
    },
    "crystal_geode_minimal": {
        "name": "💎 크리스탈 지오드 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Crystal cave interior, amethyst and quartz formations, purple-blue glow",
        "outfit": "Single large open geode crystal formation held against body, NO clothing",
        "material": "Purple amethyst geode — jagged raw edges, translucent inner crystals",
        "lighting": "Bioluminescent cave glow, crystals backlit in purple and violet",
        "pose": "Kneeling on crystal floor, geode displayed upright against torso",
        "style": "Fantasy editorial, gemstone couture, crystal goddess",
        "negative": "no dress, no crystal outfit, no clothing, no bodysuit",
    },
    "black_feather_minimal": {
        "name": "🖤 블랙 페더 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Dark baroque interior, black velvet drapes, single candelabra",
        "outfit": "Single giant raven feather held against body, NO clothing",
        "material": "Iridescent black crow feather — blue-green sheen, every barb visible",
        "lighting": "Single warm candlelight source, feather casting dramatic shadow",
        "pose": "Reclining on dark settee, feather draped with intention",
        "style": "Dark glamour editorial, noir fashion, baroque atmosphere",
        "negative": "no dress, no feather boa, no top, no clothing, no corset",
    },
    "wet_lotus_pool_minimal": {
        "name": "🪷 웻 로터스 풀 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Tranquil lotus pond at golden hour, pink petals floating on water",
        "outfit": "Single giant open lotus bloom held against body, NO clothing, skin wet",
        "material": "White-pink lotus petals, water droplets beading on petals and skin",
        "lighting": "Warm golden sunset reflected on water, soft fill from sky",
        "pose": "Standing waist-deep in still lotus pond, bloom cradled to chest",
        "style": "Zen nature editorial, water goddess, serene luxury",
        "negative": "no swimwear, no bikini, no dress, no fabric, no clothing",
    },
    "butterfly_wings_minimal": {
        "name": "🦋 버터플라이 윙스 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Sunlit wildflower meadow, soft bokeh of yellow and purple flowers",
        "outfit": "Single pair of enormous butterfly wings held open against body, NO clothing",
        "material": "Monarch butterfly wings — vivid orange and black patterns, wing dust visible",
        "lighting": "Direct afternoon sun through translucent wings, stained-glass effect",
        "pose": "Standing in open field, arms spread holding wings wide",
        "style": "Ethereal nature editorial, butterfly goddess, magical realism",
        "negative": "no costume wings, no fairy costume, no dress, no clothing",
    },
    "seaweed_ocean_minimal": {
        "name": "🌊 씨위드 오션 미니멀",
        "category": "🌿 미니멀 오브제 커버",
        "background": "Dramatic rocky ocean shore at dusk, crashing waves, seafoam on stones",
        "outfit": "Single long strand of ocean kelp wrapped loosely around body, NO clothing",
        "material": "Dark green translucent kelp — wet, glistening, sea salt on skin",
        "lighting": "Dramatic dusk light, backlit spray creating halo, deep blue-green tones",
        "pose": "Standing on wave-washed rocks, kelp flowing in sea breeze",
        "style": "Ocean goddess editorial, wild nature fashion, primordial beauty",
        "negative": "no swimwear, no dress, no clothing, no seaweed outfit",
    },
}

# ══════════════════════════════════════════════════════════
# 2. core/presets_meta.py 패치용 문자열
# ══════════════════════════════════════════════════════════

# PRESET_CATEGORIES 삽입 — 🎀 미니멀 커버 글래머 앞
CATEGORY_ANCHOR = '"🎀 미니멀 커버 글래머"'
CATEGORY_INSERT = \
    '    "🌿 미니멀 오브제 커버": [\n' + \
    ''.join(f'        "{k}",\n' for k in PRESET_DATA) + \
    '    ],\n'

# HOF_TIER 삽입 — body_chain_only_glam 앞 (🎀 첫 HOF)
HOF_ANCHOR = '"body_chain_only_glam"'
HOF_LINES  = \
    '    # 🌿 미니멀 오브제 커버\n' + \
    ''.join(f'    "{k}",\n' for k in PRESET_DATA)


# ══════════════════════════════════════════════════════════
# 3. 실행
# ══════════════════════════════════════════════════════════

def write_json_files():
    """presets/ 폴더에 JSON 9개 생성"""
    if not PRESETS_DIR.exists():
        print(f"❌ presets/ 폴더 없음 — 프로젝트 루트에서 실행하세요")
        return False
    created = []
    skipped = []
    for key, data in PRESET_DATA.items():
        path = PRESETS_DIR / f"{key}.json"
        if path.exists():
            skipped.append(key)
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        created.append(key)
    if created:
        print(f"✅ JSON 생성 ({len(created)}개): {', '.join(created)}")
    if skipped:
        print(f"⚠️  이미 존재 스킵 ({len(skipped)}개): {', '.join(skipped)}")
    return True


def patch_meta():
    """core/presets_meta.py 에 카테고리 + HOF_TIER 추가"""
    if not META_FILE.exists():
        print(f"❌ {META_FILE} 없음")
        return False

    content = META_FILE.read_text(encoding="utf-8")
    original = content
    changed = []

    # ── (A) PRESET_CATEGORIES ──────────────────────────
    if "🌿 미니멀 오브제 커버" in content:
        print("⚠️  PRESET_CATEGORIES 이미 존재 — 스킵")
    else:
        idx = content.find(CATEGORY_ANCHOR)
        if idx == -1:
            print(f"❌ CATEGORY_ANCHOR({CATEGORY_ANCHOR}) 미발견")
            return False
        line_start = content.rfind("\n", 0, idx) + 1
        content = content[:line_start] + CATEGORY_INSERT + content[line_start:]
        changed.append("PRESET_CATEGORIES")
        print("✅ PRESET_CATEGORIES 삽입 완료")

    # ── (B) HOF_TIER ───────────────────────────────────
    first_key = list(PRESET_DATA.keys())[0]
    if f'"{first_key}"' in content and content.count(f'"{first_key}"') >= 1:
        # 이미 HOF_TIER에 있는지 확인 (CATEGORIES에도 있을 수 있으므로 2회 이상이면 스킵)
        if content.count(f'"{first_key}"') >= 2:
            print("⚠️  HOF_TIER 이미 존재 — 스킵")
        else:
            idx = content.find(HOF_ANCHOR)
            if idx == -1:
                print(f"❌ HOF_ANCHOR({HOF_ANCHOR}) 미발견")
                return False
            line_start = content.rfind("\n", 0, idx) + 1
            content = content[:line_start] + HOF_LINES + content[line_start:]
            changed.append("HOF_TIER")
            print("✅ HOF_TIER 삽입 완료")
    else:
        idx = content.find(HOF_ANCHOR)
        if idx == -1:
            print(f"❌ HOF_ANCHOR({HOF_ANCHOR}) 미발견")
            return False
        line_start = content.rfind("\n", 0, idx) + 1
        content = content[:line_start] + HOF_LINES + content[line_start:]
        changed.append("HOF_TIER")
        print("✅ HOF_TIER 삽입 완료")

    if content == original:
        print("⚠️  presets_meta.py 변경사항 없음")
    else:
        META_FILE.write_text(content, encoding="utf-8")
        print(f"💾 {META_FILE} 저장 완료 (변경: {', '.join(changed)})")

    return True


def verify():
    """검증"""
    print("\n── 검증 ──────────────────────────────────────")
    # JSON 파일
    json_count = sum(1 for k in PRESET_DATA if (PRESETS_DIR / f"{k}.json").exists())
    print(f"JSON 파일: {json_count}/{len(PRESET_DATA)}개")
    # presets_meta.py
    if META_FILE.exists():
        content = META_FILE.read_text(encoding="utf-8")
        cat_ok  = "🌿 미니멀 오브제 커버" in content
        hof_ok  = all(f'"{k}"' in content for k in PRESET_DATA)
        key_count = sum(1 for k in PRESET_DATA if f'"{k}"' in content)
        print(f"PRESET_CATEGORIES 등록: {'✅' if cat_ok else '❌'}")
        print(f"HOF_TIER 키 등록: {key_count}/{len(PRESET_DATA)}개 {'✅' if hof_ok else '⚠️'}")
    print("──────────────────────────────────────────────")


if __name__ == "__main__":
    print("=" * 50)
    print("🌿 미니멀 오브제 커버 패치 시작")
    print("=" * 50)
    ok1 = write_json_files()
    ok2 = patch_meta()
    if ok1 and ok2:
        verify()
        print("\n🎉 완료! 다음 명령으로 커밋하세요:")
        print('git add presets/ core/presets_meta.py; git commit -m "🌿 미니멀 오브제 커버 9종 추가 (전종 HOF, 공식F)"; git push')
