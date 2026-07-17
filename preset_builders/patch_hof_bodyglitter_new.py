# -*- coding: utf-8 -*-
import ast

TARGET = 'core/hof_tier.py'
content = open(TARGET, encoding='utf-8').read()

# 중복 삽입 방지
if 'bodyglitter_platinum_paris_rooftop' in content:
    print("이미 패치됨 — 종료")
    exit(0)

NEW_KEYS = [
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
]

NEW_BLOCK = '\n    # ── 바디글리터 신규 HOF (2026-07-17 추가) ──\n'
for key in NEW_KEYS:
    NEW_BLOCK += f'    "{key}",\n'

# 마지막 } 앞에 삽입
last_brace = content.rfind('\n}')
new_content = content[:last_brace] + NEW_BLOCK + content[last_brace:]

try:
    ast.parse(new_content)
    open(TARGET, 'w', encoding='utf-8').write(new_content)
    print(f"완료! 바디글리터 HOF {len(NEW_KEYS)}종 추가")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
