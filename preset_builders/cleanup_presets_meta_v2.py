# -*- coding: utf-8 -*-
"""
presets_meta.py 카테고리 정리
1. Duo Glamour 중복 병합 (1910줄 + 2396줄)
2. Minimal Object Cover + Minimal Cover Glamour 병합
3. Multi Body Paint 내부 중복 키 제거
4. 전체 카테고리 중복 키 제거
"""
import ast, re
from collections import OrderedDict

TARGET = 'core/presets_meta.py'

# 실행해서 PRESET_CATEGORIES 로드
content = open(TARGET, encoding='utf-8').read()
exec_globals = {}
exec(compile(content, TARGET, 'exec'), exec_globals)
cats = exec_globals['PRESET_CATEGORIES']

print(f"로드된 카테고리: {len(cats)}개")
print(f"총 키: {sum(len(v) for v in cats.values())}개")

# 1. Duo Glamour 중복 — 현재는 9키짜리가 남아있음
# 원본 파일에서 두 Duo Glamour 블록 모두 읽어서 병합

# 파일을 직접 파싱해서 두 Duo Glamour 블록 키 수집
duo_keys = []
duo_blocks = []
in_duo = False
depth = 0
current_block = []

for line in content.splitlines():
    if '"Duo Glamour"' in line and ': [' in line:
        in_duo = True
        depth = 0
        current_block = []

    if in_duo:
        current_block.append(line)
        depth += line.count('[') - line.count(']')
        if depth <= 0 and len(current_block) > 1:
            in_duo = False
            duo_blocks.append('\n'.join(current_block))
            # 키 추출
            for l in current_block:
                matches = re.findall(r'"([a-z][a-z0-9_]*)"', l)
                duo_keys.extend(matches)

print(f"\nDuo Glamour 블록 {len(duo_blocks)}개 발견, 총 {len(duo_keys)}키")

# 중복 제거 순서 유지
def dedup(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

duo_merged = dedup(duo_keys)
print(f"중복 제거 후: {len(duo_merged)}키")

# 2. Minimal 병합
minimal_keys = dedup(
    cats.get('🌿 Minimal Object Cover', []) +
    cats.get('🎀 Minimal Cover Glamour', [])
)
print(f"\nMinimal 병합: {len(minimal_keys)}키")

# 3. 전체 카테고리 재구성
# 원본 순서 유지하되:
# - Duo Glamour: 첫 번째 위치에 병합된 버전
# - Minimal Object Cover: 병합, Minimal Cover Glamour 제거
# - 두 번째 Duo Glamour 제거

SKIP_CATS = {'🎀 Minimal Cover Glamour'}
MERGED = {
    '👯 Duo Glamour': duo_merged,
    '🌿 Minimal Object Cover': minimal_keys,
}

seen_cats = set()
new_cats = OrderedDict()

for name, keys in cats.items():
    # 이모지 포함 이름 정규화
    if name in SKIP_CATS:
        continue

    # Duo Glamour 중복 처리
    base = re.sub(r'[^\w\s]', '', name).strip()
    if base in seen_cats:
        continue
    seen_cats.add(base)

    if name in MERGED:
        new_cats[name] = dedup(MERGED[name])
    else:
        new_cats[name] = dedup(keys)

print(f"\n정리 후 카테고리: {len(new_cats)}개")
print(f"총 키: {sum(len(v) for v in new_cats.values())}개")

# 파일 재생성
lines = ['# -*- coding: utf-8 -*-\n']
lines.append('"""\nLumineX Preset Metadata\n카테고리별 프리셋 키 목록 + HOF / SSS / SS 분류\n\ndashboard.py 에서 임포트 (A형)\n상위 파일을 변경하면 배포 설정도 확인\n"""\n\n')
lines.append('PRESET_CATEGORIES = {\n')

for cat_name, keys in new_cats.items():
    lines.append(f'    "{cat_name}": [\n')
    # 8개씩 줄 나눔
    for i in range(0, len(keys), 8):
        chunk = keys[i:i+8]
        lines.append('        ' + ', '.join(f'"{k}"' for k in chunk) + ',\n')
    lines.append('    ],\n\n')

lines.append('}\n\n')
lines.append('from core.hof_tier import HOF_TIER  # HOF 추가는 core/hof_tier.py에서\n')

new_content = ''.join(lines)

# 검증
try:
    ast.parse(new_content)
    print("\nAST 파싱 OK")
    open(TARGET, 'w', encoding='utf-8').write(new_content)
    print(f"저장 완료!")

    # 줄 수 확인
    line_count = len(new_content.splitlines())
    print(f"새 파일: {line_count}줄")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
