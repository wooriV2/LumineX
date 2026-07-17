# -*- coding: utf-8 -*-
"""
presets_meta.py 카테고리 정리 스크립트
- 중복 카테고리 병합
- 잘못 끼어든 항목 제거
- 중복 키 제거
"""
import ast, re

TARGET = 'core/presets_meta.py'
content = open(TARGET, encoding='utf-8').read()

# 백업
open(TARGET + '.bak', 'w', encoding='utf-8').write(content)
print("백업 완료: core/presets_meta.py.bak")

# 1. Environment Merge 카테고리 안에 끼어든 Night/Slip/Animal/Theatrical 인라인 블록 제거
# 2205~2212줄 해당 부분
content = re.sub(
    r'\n\s+"[🌙👗🐆🎭][^"]*":\s+\[.*?\],?\n(?=\s+"[🎭🌿🎀])',
    '\n',
    content,
    flags=re.DOTALL
)

lines = content.splitlines(keepends=True)

# 카테고리별 키 수집
def extract_category(lines, start_line):
    """start_line(0-indexed)에서 카테고리 키 목록 추출, 끝 줄 반환"""
    keys = []
    i = start_line
    depth = 0
    started = False
    while i < len(lines):
        line = lines[i]
        if '[' in line and not started:
            depth += line.count('[') - line.count(']')
            started = True
        elif started:
            depth += line.count('[') - line.count(']')
            # 키 추출
            matches = re.findall(r'"([a-z][a-z0-9_]*)"', line)
            keys.extend(matches)
        if started and depth <= 0:
            return keys, i
        i += 1
    return keys, i

# 카테고리 위치 찾기
cat_pattern = re.compile(r'^\s+"[^"]+": \[')
cat_positions = []
for i, line in enumerate(lines):
    if cat_pattern.match(line):
        cat_name = re.search(r'"([^"]+)"', line).group(1)
        cat_positions.append((i, cat_name))

print(f"\n전체 카테고리 {len(cat_positions)}개 발견")

# 중복 카테고리 찾기
from collections import defaultdict
cat_groups = defaultdict(list)
for pos, name in cat_positions:
    # 이모지 제거해서 비교
    clean = re.sub(r'[^\w\s]', '', name).strip()
    cat_groups[clean].append((pos, name))

print("\n중복 카테고리:")
for clean, group in cat_groups.items():
    if len(group) > 1:
        print(f"  '{clean}': {[f'줄{p+1}' for p, n in group]}")

# 중복 카테고리 중 두 번째 이후를 제거하는 방식으로 처리
# 단순하게: ast로 파싱해서 딕셔너리 키 중복 확인
try:
    tree = ast.parse(content)
    print("\nAST 파싱 성공 — 문법 정상")
except SyntaxError as e:
    print(f"\nAST 파싱 실패: {e}")
    print("문법 오류가 있어 정리를 진행할 수 없습니다.")
    exit(1)

# Python 딕셔너리에서 중복 키는 마지막 값이 우선
# PRESET_CATEGORIES 딕셔너리를 직접 eval해서 병합된 상태 확인
exec_globals = {}
try:
    exec(compile(content, TARGET, 'exec'), exec_globals)
    cats = exec_globals.get('PRESET_CATEGORIES', {})
    print(f"\n실제 로드된 카테고리 수: {len(cats)}")
    for k, v in cats.items():
        print(f"  {k[:30]:30s}: {len(v)}키")
except Exception as e:
    print(f"exec 실패: {e}")
