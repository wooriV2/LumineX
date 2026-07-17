# -*- coding: utf-8 -*-
import ast, os, json, glob

TARGET = 'core/presets_meta.py'

content = open(TARGET, encoding='utf-8').read()
if 'bodyglitter_platinum_paris_rooftop' in content:
    print("이미 패치됨 — 종료")
    exit(0)

HOF_KEYS = {
    "bodyglitter_platinum_paris_rooftop",
    "bodyglitter_black_void_fitness",
    "bodyglitter_coral_rio_carnival",
    "bodyglitter_cobalt_cape_town",
    "bodyglitter_platinum_void_black_glam",
    "bodyglitter_purple_aurora_nordic",
    "bodyglitter_gold_rio_carnival",
    "bodyglitter_gold_cape_town_black_glam",
    "bodyglitter_red_dubai_black_glam",
    "bodyglitter_gold_maldives_vs_angel",
}

SSS_KEYS = {
    "bodyglitter_jade_bali_temple",
    "bodyglitter_teal_amalfi_cliff",
    "bodyglitter_lavender_tokyo_shibuya",
    "bodyglitter_champagne_versailles_mature",
    "bodyglitter_crimson_vegas_strip",
    "bodyglitter_white_void_ballerina_korean",
    "bodyglitter_orange_marrakech",
    "bodyglitter_magenta_new_york_loft",
    "bodyglitter_green_forest_goddess",
    "bodyglitter_bronze_fitness_strobe",
    "bodyglitter_gold_onsen_mature",
    "bodyglitter_silver_cape_town_sports",
    "bodyglitter_rose_gold_maldives",
    "bodyglitter_blue_void_runway",
    "bodyglitter_emerald_kyoto_rain",
    "bodyglitter_copper_void_milf",
    "bodyglitter_silver_dubai_milf",
    "bodyglitter_rose_gold_dubai_sports",
    "bodyglitter_blue_santorini_mature",
    "bodyglitter_silver_aurora_runway",
    "bodyglitter_gold_versailles_colombian",
    "bodyglitter_rainbow_void_fitness",
    "bodyglitter_emerald_monaco_milf",
    "bodyglitter_copper_rio_carnival",
    "bodyglitter_blue_bali_temple",
    "bodyglitter_purple_void_black_glam",
    "bodyglitter_ice_blue_onsen_mature",
    "bodyglitter_silver_versailles_runway",
    "bodyglitter_gold_tokyo_runway",
    "bodyglitter_rose_gold_amalfi_ballerina",
    "bodyglitter_blue_monaco_colombian",
    "bodyglitter_purple_marrakech_mature",
    "bodyglitter_ice_blue_paris_runway",
    "bodyglitter_silver_tokyo_fitness",
}

# SS: 나머지
SS_KEYS = {
    "bodyglitter_bronze_kyoto_rain",
    "bodyglitter_silver_marrakech_sports",
    "bodyglitter_red_marrakech_colombian",
    "bodyglitter_gold_cape_town_black_glam",  # HOF로 이미 위에 있음 — 중복 방지용
}
# 실제 SS (HOF/SSS 제외)
SS_KEYS = {
    "bodyglitter_bronze_kyoto_rain",
    "bodyglitter_silver_marrakech_sports",
    "bodyglitter_red_marrakech_colombian",
}

def get_tier(key):
    if key in HOF_KEYS:
        return "HOF"
    if key in SSS_KEYS:
        return "SSS"
    return "SS"

def make_block(key):
    path = f'presets/{key}.json'
    if not os.path.exists(path):
        print(f"WARNING: {path} 없음 — 스킵")
        return ''
    d = json.load(open(path, encoding='utf-8'))
    tier = get_tier(key)
    lines = [f'    "{key}": {{']
    lines.append(f'        "tier": "{tier}",')
    for field in ("subject", "prompt", "environment", "lighting", "style", "quality"):
        if field in d:
            val = d[field].replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'        "{field}": "{val}",')
    lines.append('    },')
    return '\n'.join(lines)

keys = sorted([
    os.path.basename(p).replace('.json', '')
    for p in glob.glob('presets/bodyglitter_*.json')
])

print(f"바디글리터 JSON {len(keys)}종 발견")

NEW_BLOCK = '\n    # ── 바디글리터 (2026-07-17 추가) ──\n'
for key in keys:
    block = make_block(key)
    if block:
        NEW_BLOCK += block + '\n'

last_brace = content.rfind('\n}')
new_content = content[:last_brace] + NEW_BLOCK + content[last_brace:]

try:
    ast.parse(new_content)
    open(TARGET, 'w', encoding='utf-8').write(new_content)
    print(f"완료! 바디글리터 {len(keys)}종 삽입")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
