# -*- coding: utf-8 -*-
"""
presets_meta.py 고아 키 전체 제거
값(:) 없이 키만 있는 라인을 모두 찾아서 제거
"""

import ast
import re

with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 고아 키 패턴: 공백 + "키이름", 로 끝나는 라인 (값이 없는 것)
# 정상 라인은 "key": { 또는 "key": "value" 형태
orphan_pattern = re.compile(r'^\s+"[a-zA-Z0-9_]+",\s*$')

removed = []
new_lines = []
for i, line in enumerate(lines, start=1):
    if orphan_pattern.match(line):
        removed.append((i, line.strip()))
        print(f"제거: 라인 {i}: {line.strip()}")
    else:
        new_lines.append(line)

print(f"\n총 {len(removed)}개 고아 키 라인 제거")

# 빈 줄 연속 3개 이상이면 2개로 줄이기 (선택적 정리)
content = ''.join(new_lines)
content = re.sub(r'\n{4,}', '\n\n\n', content)

# 문법 검증
try:
    ast.parse(content)
    print("문법 OK — 저장합니다")
    with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("저장 완료!")
except SyntaxError as e:
    print(f"문법 오류 여전히 존재: {e}")
    # 오류 라인 주변 출력
    err_lines = content.split('\n')
    err_line = e.lineno
    print(f"\n오류 주변 ({err_line-3}~{err_line+3}):")
    for i, l in enumerate(err_lines[max(0,err_line-4):err_line+3], start=max(1,err_line-3)):
        print(f"  {i}: {l}")
