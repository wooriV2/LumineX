# -*- coding: utf-8 -*-
"""
presets_meta.py 수정:
1. 3471번 줄 이후 값 없는 키들 제거
2. 이레즈미 + 바디글리터 블록을 올바른 위치에 삽입
"""

import ast

with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Step 1: 값 없는 키 라인들 제거 ──────────────────────
# 이 라인들이 딕셔너리 안에 값 없이 존재해서 문법 오류 발생
ORPHAN_LINES = [
    '    "runway_korean_slim_seoulforest_spring",\n',
    '    "young_korean_pool_pastel",\n',
    '    "young_korean_neon_first_night",\n',
    '    "young_korean_tokyo_first_solo",\n',
    '    "young_korean_tattoo_first_wrist",\n',
    '    "young_korean_gym_first_gains",\n',
    '    "young_korean_campus_spring",\n',
    '    "korean_idol_bukchon_morning",\n',
    '    "korean_idol_jeju_ocean",\n',
    '    "mature_korean_silver_kyoto_bamboo",\n',
    '    "mature_korean_silver_onsen",\n',
]

for line in ORPHAN_LINES:
    content = content.replace(line, '')

print("Step 1 완료: 고아 키 라인 제거")

# ── Step 2: 이레즈미+글리터 블록이 이미 들어가 있는지 확인 ──
if 'irezumi_dragon_wave_black_glam_void' in content:
    print("Step 2: 이레즈미 블록 이미 존재 — 삽입 생략")
else:
    print("Step 2: 이레즈미 블록 없음 — 별도 패치 필요")

# ── Step 3: 문법 검증 ──────────────────────────────────
try:
    ast.parse(content)
    print("Step 3: 문법 OK")
    with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("저장 완료!")
except SyntaxError as e:
    print(f"Step 3: 문법 오류 여전히 존재: {e}")
    print("라인 번호 확인 후 추가 수정 필요")
