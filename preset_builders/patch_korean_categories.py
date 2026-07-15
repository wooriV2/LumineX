# -*- coding: utf-8 -*-
"""
LumineX 패치 스크립트 v2
세션 2026-07-15 검증 완료분 반영
카테고리 블록 앵커 수정버전

실행 방법:
  $env:PYTHONUTF8 = "1"
  python preset_builders/patch_korean_categories.py
"""

from pathlib import Path

ROOT = Path(__file__).parent.parent
META = ROOT / "core" / "presets_meta.py"
HOF_FILE = ROOT / "core" / "hof_tier.py"

# ──────────────────────────────────────────────
# 1. 신규 카테고리 프리셋 키 정의
# ──────────────────────────────────────────────

KIDOL_NEW = [
    "korean_idol_gangnam_latex",
    "korean_idol_holographic_stage",
    "korean_idol_bukchon_morning",
    "korean_idol_cyber_dongdaemun",
    "korean_idol_jeju_ocean",
]

MATURE_GODDESS_NEW = [
    "mature_korean_silver_penthouse",
    "mature_korean_silver_onsen",
    "mature_korean_silver_paris_window",
    "mature_korean_silver_dubai_pool",
    "mature_korean_silver_void_studio",
    "mature_korean_silver_bali_temple",
    "mature_korean_silver_newyork_rooftop",
    "mature_korean_silver_jeju_cliff",
    "mature_korean_silver_kyoto_bamboo",
    "mature_korean_silver_london_rain",
    "mature_korean_silver_maldives_overwater",
    "mature_korean_silver_milan_fashion",
    "mature_korean_silver_istanbul_hammam",
    "mature_korean_silver_rio_carnival",
    "mature_korean_silver_alaska_aurora",
    "mature_korean_silver_tokyo_shibuya",
    "mature_korean_silver_sahara_sunset",
    "mature_korean_silver_monaco_yacht",
    "mature_korean_silver_berlin_techno",
    "mature_korean_silver_crystal_gala",
]

ELDER_GODDESS_NEW = [
    "elder_korean_silver_void_studio",
    "elder_korean_silver_jeju_wind",
    "elder_korean_silver_hanok_dawn",
    "elder_korean_silver_paris_cafe",
    "elder_korean_silver_tokyo_garden",
    "elder_korean_silver_maldives_sunrise",
    "elder_korean_silver_nyc_museum",
    "elder_korean_silver_rio_beach",
    "elder_korean_silver_dubai_desert",
    "elder_korean_70s_cliff_wind",
]

FITNESS_KOREAN_NEW = [
    "fitness_korean_black_sand_wave",
    "fitness_korean_chrome_gym_mirror",
    "fitness_korean_tattoo_bali_pool",
    "fitness_korean_gold_dubai_sunrise",
    "fitness_korean_tattoo_void_red",
    "fitness_korean_30s_tokyo_neon",
    "fitness_korean_abs_maldives_crystal",
    "fitness_korean_tattoo_collar_paris",
    "fitness_korean_powerglam_lasvegas",
    "fitness_korean_bikini_pro_stage",
]

NEW_HOF = {
    "night_bust_queen_dubai",
    "night_powerlifter_lasvegas",
    "korean_idol_holographic_stage",
    "mature_korean_silver_paris_window",
    "mature_korean_silver_void_studio",
    "mature_korean_silver_newyork_rooftop",
    "mature_korean_silver_jeju_cliff",
    "mature_korean_silver_maldives_overwater",
    "mature_korean_silver_milan_fashion",
    "mature_korean_silver_istanbul_hammam",
    "mature_korean_silver_alaska_aurora",
    "mature_korean_silver_sahara_sunset",
    "mature_korean_silver_crystal_gala",
    "elder_korean_silver_void_studio",
    "elder_korean_silver_jeju_wind",
    "elder_korean_silver_maldives_sunrise",
    "elder_korean_silver_nyc_museum",
    "elder_korean_silver_dubai_desert",
    "elder_korean_70s_cliff_wind",
    "fitness_korean_black_sand_wave",
    "fitness_korean_chrome_gym_mirror",
    "fitness_korean_gold_dubai_sunrise",
    "fitness_korean_tattoo_void_red",
    "fitness_korean_abs_maldives_crystal",
    "fitness_korean_powerglam_lasvegas",
    "fitness_korean_bikini_pro_stage",
}

NEW_SSS = {
    "night_brazil_tokyo_neon",
    "night_supermodel_paris_rooftop",
    "korean_idol_gangnam_latex",
    "korean_idol_cyber_dongdaemun",
    "mature_korean_silver_penthouse",
    "mature_korean_silver_dubai_pool",
    "mature_korean_silver_bali_temple",
    "mature_korean_silver_london_rain",
    "mature_korean_silver_rio_carnival",
    "mature_korean_silver_tokyo_shibuya",
    "mature_korean_silver_monaco_yacht",
    "mature_korean_silver_berlin_techno",
    "elder_korean_silver_hanok_dawn",
    "elder_korean_silver_paris_cafe",
    "elder_korean_silver_tokyo_garden",
    "elder_korean_silver_rio_beach",
    "fitness_korean_tattoo_bali_pool",
    "fitness_korean_30s_tokyo_neon",
    "fitness_korean_tattoo_collar_paris",
}

NEW_SS = {
    "korean_idol_bukchon_morning",
    "korean_idol_jeju_ocean",
    "mature_korean_silver_onsen",
    "mature_korean_silver_kyoto_bamboo",
}

# ──────────────────────────────────────────────
# 2. presets_meta.py 패치
# ──────────────────────────────────────────────

def patch_meta():
    text = META.read_text(encoding="utf-8-sig")
    changed = False

    # 2-1. 신규 카테고리 블록 — "from core.hof_tier import HOF_TIER" 바로 앞에 삽입
    anchor = "from core.hof_tier import HOF_TIER"

    if '"🎤 K-Idol 한국인"' not in text:
        new_block = (
            '    "🎤 K-Idol 한국인": [\n'
            + "".join(f'        "{k}",\n' for k in KIDOL_NEW)
            + "    ],\n"
            + '    "👵 Mature Goddess 한국인": [\n'
            + "".join(f'        "{k}",\n' for k in MATURE_GODDESS_NEW)
            + "    ],\n"
            + '    "👴 Elder Goddess 한국인": [\n'
            + "".join(f'        "{k}",\n' for k in ELDER_GODDESS_NEW)
            + "    ],\n"
            + '    "💪 Fitness Model 한국인": [\n'
            + "".join(f'        "{k}",\n' for k in FITNESS_KOREAN_NEW)
            + "    ],\n"
            + "}\n\n\n"
        )
        # PRESET_CATEGORIES 닫는 } 찾아서 그 앞에 삽입
        # 마지막 '] \n}' 패턴 찾기
        close_idx = text.rfind("\n}\n")
        if close_idx != -1:
            text = text[:close_idx] + "\n" + new_block + anchor
            # anchor 이후 기존 내용 붙이기
            orig_anchor_idx = text.find(anchor + "\n")
            if orig_anchor_idx == -1:
                # anchor가 이미 삽입되어 있으니 중복 제거
                pass
            changed = True
            print("✅ 신규 카테고리 4개 블록 추가")
        else:
            print("❌ PRESET_CATEGORIES 닫는 } 를 찾지 못했어요")
    else:
        print("⚠️ 카테고리 이미 존재 — 스킵")

    # 2-2. SSS_TIER 추가
    sss_open = "SSS_TIER = {"
    sss_insert = "\n    # 2026-07-15 한국인 신규 SSS\n" + "".join(f'    "{k}",\n' for k in sorted(NEW_SSS))
    if sss_open in text and list(NEW_SSS)[0] not in text:
        text = text.replace(sss_open, sss_open + sss_insert, 1)
        changed = True
        print(f"✅ SSS_TIER {len(NEW_SSS)}종 추가")
    else:
        print("⚠️ SSS 이미 존재 또는 앵커 없음")

    # 2-3. SS_TIER 추가
    ss_open = "SS_TIER = {"
    ss_insert = "\n    # 2026-07-15 한국인 신규 SS\n" + "".join(f'    "{k}",\n' for k in sorted(NEW_SS))
    if ss_open in text and list(NEW_SS)[0] not in text:
        text = text.replace(ss_open, ss_open + ss_insert, 1)
        changed = True
        print(f"✅ SS_TIER {len(NEW_SS)}종 추가")
    else:
        print("⚠️ SS 이미 존재 또는 앵커 없음")

    if changed:
        META.write_text(text, encoding="utf-8")
        print("✅ presets_meta.py 저장 완료")

# ──────────────────────────────────────────────
# 3. hof_tier.py 패치
# ──────────────────────────────────────────────

def patch_hof():
    text = HOF_FILE.read_text(encoding="utf-8-sig")
    anchor = "HOF_TIER = {"
    insert = "\n    # 2026-07-15 한국인 신규 HOF\n" + "".join(f'    "{k}",\n' for k in sorted(NEW_HOF))

    if anchor in text and list(NEW_HOF)[0] not in text:
        text = text.replace(anchor, anchor + insert, 1)
        HOF_FILE.write_text(text, encoding="utf-8")
        print(f"✅ HOF_TIER {len(NEW_HOF)}종 추가")
        print("✅ hof_tier.py 저장 완료")
    else:
        print("⚠️ HOF 이미 존재 또는 앵커 없음")

# ──────────────────────────────────────────────
# 4. 검증
# ──────────────────────────────────────────────

def verify():
    meta_text = META.read_text(encoding="utf-8-sig")
    hof_text  = HOF_FILE.read_text(encoding="utf-8-sig")

    print("\n── 검증 ──────────────────────────────────")

    hof_ok  = all(k in hof_text  for k in NEW_HOF)
    sss_ok  = all(k in meta_text for k in NEW_SSS)
    ss_ok   = all(k in meta_text for k in NEW_SS)

    print(f"{'✅' if hof_ok  else '❌'} HOF  {len(NEW_HOF)}종")
    print(f"{'✅' if sss_ok  else '❌'} SSS  {len(NEW_SSS)}종")
    print(f"{'✅' if ss_ok   else '❌'} SS   {len(NEW_SS)}종")

    for cat in ['"🎤 K-Idol 한국인"', '"👵 Mature Goddess 한국인"',
                '"👴 Elder Goddess 한국인"', '"💪 Fitness Model 한국인"']:
        print(f"{'✅' if cat in meta_text else '❌'} 카테고리 {cat}")

    print("──────────────────────────────────────────")

# ──────────────────────────────────────────────
# 5. 실행
# ──────────────────────────────────────────────

if __name__ == "__main__":
    print("=== LumineX 한국인 카테고리 패치 v2 (2026-07-15) ===")
    print(f"META : {META}")
    print(f"HOF  : {HOF_FILE}\n")
    patch_meta()
    print()
    patch_hof()
    verify()
    print("\n✅ 완료! 다음 단계:")
    print("  python preset_builders/generate_new_category_jsons.py")
