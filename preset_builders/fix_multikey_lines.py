# -*- coding: utf-8 -*-
"""
presets_meta.py 추가 수정:
한 줄에 여러 고아 키가 나란히 있는 패턴 제거
예: "key1",    "key2",
"""

import ast
import re

with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 패턴 1: 한 줄에 두 개 이상 키가 콤마로 나열된 라인
# 예: "trio_inside_outside_bodypaint",    "quad_fashion_capitals_bodypaint",
multi_key_pattern = re.compile(r'^\s*"[a-zA-Z0-9_]+".*"[a-zA-Z0-9_]+"\s*,?\s*$')

# 패턴 2: 단일 고아 키 (값 없는 것) - 이전 스크립트가 못 잡은 것
orphan_pattern = re.compile(r'^\s+"[a-zA-Z0-9_]+",\s*$')

removed = []
new_lines = []
for i, line in enumerate(lines, start=1):
    if multi_key_pattern.match(line) and ':' not in line:
        removed.append((i, line.strip()))
        print(f"제거(다중키): {i}: {line.strip()}")
    elif orphan_pattern.match(line):
        removed.append((i, line.strip()))
        print(f"제거(단일키): {i}: {line.strip()}")
    else:
        new_lines.append(line)

print(f"\n총 {len(removed)}개 라인 제거")

content = ''.join(new_lines)
# 연속 빈줄 정리
content = re.sub(r'\n{4,}', '\n\n\n', content)

try:
    ast.parse(content)
    print("문법 OK — 저장합니다")
    with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("저장 완료!")
except SyntaxError as e:
    print(f"문법 오류 여전히 존재: {e}")
    err_lines = content.split('\n')
    err_line = e.lineno
    print(f"\n오류 주변 ({err_line-3}~{err_line+3}):")
    for i, l in enumerate(err_lines[max(0,err_line-4):err_line+3], start=max(1,err_line-3)):
        print(f"  {i}: {l}")
