# -*- coding: utf-8 -*-
import ast, os, json, glob

TARGET = 'core/presets_meta.py'

# 중복 삽입 방지
content = open(TARGET, encoding='utf-8').read()
if 'irezumi_dragon_wave_black_glam_void' in content:
    print("이미 패치됨 — 종료")
    exit(0)

# HOF 확정 목록 (인계 메모 기준)
IREZUMI_HOF = {
    "irezumi_dragon_wave_black_glam_void",
    "irezumi_dragon_wave_sports_glam_onsen",
    "irezumi_dragon_wave_power_fitness_strobe",
    "irezumi_dragon_wave_vs_angel_santorini",
    "irezumi_dragon_wave_slim_runway_neon",
    "irezumi_phoenix_chrysanthemum_ballerina_steam",
    "irezumi_phoenix_chrysanthemum_hot_glam_riad",
    "irezumi_phoenix_chrysanthemum_black_glam_desert",
    "irezumi_koi_sakura_vs_angel_kyoto_rain",
    "irezumi_koi_sakura_colombian_monaco",
    "irezumi_crane_peony_super_glam_versailles",
    "irezumi_tiger_bamboo_sports_glam_void",
    "irezumi_tiger_bamboo_vs_angel_dubai",
    "irezumi_tiger_bamboo_african_desert",
}
GLITTER_HOF = {
    "bodyglitter_silver_neon_cyberpunk",
    "bodyglitter_gold_void_black_glam",
    "bodyglitter_rose_gold_versailles",
    "bodyglitter_blue_holographic_pool",
    "bodyglitter_silver_onsen_steam",
    "bodyglitter_rainbow_aurora_nordic",
    "bodyglitter_emerald_dubai_rooftop",
    "bodyglitter_copper_santorini_sunset",
    "bodyglitter_purple_monaco_night",
    "bodyglitter_red_void_colombian",
    "bodyglitter_ice_blue_void_ballerina",
}

def make_block(key, hof_set):
    path = f'presets/{key}.json'
    if not os.path.exists(path):
        print(f"WARNING: {path} 없음 — 스킵")
        return ''
    d = json.load(open(path, encoding='utf-8'))
    tier = "HOF" if key in hof_set else "SSS"
    lines = [f'    "{key}": {{']
    lines.append(f'        "tier": "{tier}",')
    for field in ("subject", "prompt", "environment", "lighting", "style", "quality"):
        if field in d:
            val = d[field].replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'        "{field}": "{val}",')
    lines.append('    },')
    return '\n'.join(lines)

# JSON 파일 목록
irezumi_keys = sorted([
    os.path.basename(p).replace('.json', '')
    for p in glob.glob('presets/irezumi_*.json')
])
glitter_keys = sorted([
    os.path.basename(p).replace('.json', '')
    for p in glob.glob('presets/bodyglitter_*.json')
])

print(f"이레즈미 {len(irezumi_keys)}종, 글리터 {len(glitter_keys)}종 발견")

# 삽입 블록 조립
NEW_BLOCK = '\n    # ── 이레즈미 전신 타투 (2026-07-17 추가) ──\n'
for key in irezumi_keys:
    block = make_block(key, IREZUMI_HOF)
    if block:
        NEW_BLOCK += block + '\n'

NEW_BLOCK += '\n    # ── 바디글리터 (2026-07-17 추가) ──\n'
for key in glitter_keys:
    block = make_block(key, GLITTER_HOF)
    if block:
        NEW_BLOCK += block + '\n'

# 마지막 } 앞에 삽입
last_brace = content.rfind('\n}')
new_content = content[:last_brace] + NEW_BLOCK + content[last_brace:]

# 문법 검증 후 저장
try:
    ast.parse(new_content)
    open(TARGET, 'w', encoding='utf-8').write(new_content)
    print(f"완료! 이레즈미 {len(irezumi_keys)}종 + 글리터 {len(glitter_keys)}종 삽입")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
