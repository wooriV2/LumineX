# -*- coding: utf-8 -*-
import ast, os, json, glob

TARGET = 'core/presets_meta.py'

content = open(TARGET, encoding='utf-8').read()

# 중복 삽입 방지
if 'irezumi_dragon_wave_black_glam_void' in content:
    print("이미 패치됨 — 종료")
    exit(0)

HOF_KEYS = {
    # 이레즈미 HOF
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
    # 바디글리터 HOF
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

def make_block(key):
    path = f'presets/{key}.json'
    if not os.path.exists(path):
        print(f"WARNING: {path} 없음 — 스킵")
        return ''
    d = json.load(open(path, encoding='utf-8'))
    tier = "HOF" if key in HOF_KEYS else "SSS"
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

print(f"이레즈미 {len(irezumi_keys)}종, 바디글리터 {len(glitter_keys)}종 발견")

# 블록 조립
NEW_BLOCK = '\n    # ── 이레즈미 전신 타투 (2026-07-17 추가) ──\n'
for key in irezumi_keys:
    block = make_block(key)
    if block:
        NEW_BLOCK += block + '\n'

NEW_BLOCK += '\n    # ── 바디글리터 (2026-07-17 추가) ──\n'
for key in glitter_keys:
    block = make_block(key)
    if block:
        NEW_BLOCK += block + '\n'

# 안전한 삽입: 줄 단위로 마지막 단독 } 찾기
lines = content.splitlines(keepends=True)
insert_pos = None
for i in range(len(lines)-1, -1, -1):
    if lines[i].strip() == '}':
        insert_pos = i
        break

if insert_pos is None:
    print("ERROR: 삽입 위치를 찾을 수 없습니다")
    exit(1)

print(f"삽입 위치: {insert_pos+1}줄")

new_lines = lines[:insert_pos] + [NEW_BLOCK] + [lines[insert_pos]]
new_content = ''.join(new_lines)

try:
    ast.parse(new_content)
    open(TARGET, 'w', encoding='utf-8').write(new_content)
    print(f"완료! 이레즈미 {len(irezumi_keys)}종 + 바디글리터 {len(glitter_keys)}종 삽입")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
