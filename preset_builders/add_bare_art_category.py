# -*- coding: utf-8 -*-
"""
PRESET_CATEGORIES 딕셔너리에 ✨ Bare Art Ensemble 카테고리 추가
"""
import ast, os

META_PATH = r"C:\Dev\LumineX\core\presets_meta.py"

CATEGORY_BLOCK = """
    "✨ Bare Art Ensemble": [
        "duo_irezumi_dragon_glitter_gold_void",
        "duo_irezumi_wave_glitter_indigo_santorini",
        "duo_irezumi_phoenix_glitter_crimson_shibuya",
        "duo_irezumi_koi_glitter_coral_maldives",
        "duo_irezumi_snake_glitter_emerald_versailles",
        "duo_irezumi_peacock_glitter_teal_monaco",
        "duo_irezumi_skull_glitter_obsidian_kyoto",
        "duo_irezumi_samurai_glitter_silver_tokyo",
        "duo_irezumi_dragon_klimt_versailles",
        "duo_irezumi_phoenix_vangogh_aurora",
        "duo_irezumi_wave_pollock_void",
        "duo_irezumi_koi_klimt_silver_budapest",
        "duo_irezumi_snake_mucha_paris",
        "duo_irezumi_peacock_kandinsky_monaco",
        "duo_irezumi_skull_dali_kyoto",
        "duo_glitter_gold_klimt_void",
        "duo_glitter_crimson_vangogh_aurora",
        "duo_glitter_silver_pollock_shibuya",
        "duo_glitter_teal_mucha_maldives",
        "duo_glitter_obsidian_dali_versailles",
        "duo_glitter_violet_kandinsky_kyoto",
        "duo_glitter_emerald_vangogh_budapest",
        "duo_irezumi_glitter_aurora",
        "duo_irezumi_snake_dragon_monaco",
        "duo_irezumi_wave_phoenix_shibuya",
        "duo_glitter_gold_obsidian_void",
        "duo_glitter_fire_ice_cape_town",
    ],
"""

ANCHOR = "from core.hof_tier import HOF_TIER"

with open(META_PATH, "r", encoding="utf-8-sig") as f:
    content = f.read()

if "Bare Art Ensemble" in content:
    print("이미 추가됨 — SKIP")
elif ANCHOR not in content:
    print(f"앵커 문자열을 찾을 수 없음: {ANCHOR}")
else:
    new_content = content.replace(ANCHOR, CATEGORY_BLOCK + ANCHOR, 1)
    with open(META_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("카테고리 추가 완료")

# 검증
with open(META_PATH, "r", encoding="utf-8-sig") as f:
    src = f.read()
try:
    ast.parse(src)
    print("문법 검증: OK")
except SyntaxError as e:
    print(f"문법 오류: {e}")
