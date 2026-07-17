# -*- coding: utf-8 -*-
"""
presets_meta.py 전체 정리
1. dict 카테고리 -> id 키만 추출
2. Duo Glamour 중복 병합 (원본 파일에서 두 블록 직접 파싱)
3. Minimal Object Cover + Minimal Cover Glamour 병합
4. 각 카테고리 중복 키 제거
"""
import ast, re
from collections import OrderedDict

TARGET = 'core/presets_meta.py'
content = open(TARGET, encoding='utf-8').read()

# 원본에서 Duo Glamour 두 블록 키 직접 추출
duo_all_keys = []
lines = content.splitlines()
i = 0
duo_count = 0
while i < len(lines):
    line = lines[i]
    if 'Duo Glamour' in line and ': [' in line:
        duo_count += 1
        depth = line.count('[') - line.count(']')
        i += 1
        while i < len(lines) and depth > 0:
            depth += lines[i].count('[') - lines[i].count(']')
            matches = re.findall(r'"([a-z][a-z0-9_]*)"', lines[i])
            duo_all_keys.extend(matches)
            i += 1
        continue
    i += 1

print(f"Duo Glamour 블록 {duo_count}개, 총 {len(duo_all_keys)}키 발견")

def dedup(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen and isinstance(x, str):
            seen.add(x)
            result.append(x)
    return result

duo_merged = dedup(duo_all_keys)
print(f"Duo 병합 후: {len(duo_merged)}키")

# PRESET_CATEGORIES 로드
exec_globals = {}
exec(compile(content, TARGET, 'exec'), exec_globals)
cats = exec_globals['PRESET_CATEGORIES']

# 정리
SKIP = set()  # 제거할 카테고리 이름
seen_base = set()
new_cats = OrderedDict()

for name, keys in cats.items():
    base = re.sub(r'[^\w\s횞]', '', name).strip()

    # Duo Glamour: 병합 버전으로 교체, 두 번째는 스킵
    if 'Duo Glamour' in name:
        if 'Duo Glamour' not in seen_base:
            seen_base.add('Duo Glamour')
            new_cats[name] = duo_merged
        continue

    # Minimal Cover Glamour 제거 (Minimal Object Cover로 통합)
    if 'Minimal Cover Glamour' in name and 'Object' not in name:
        SKIP.add(name)
        continue

    # 중복 카테고리 스킵
    if base in seen_base:
        continue
    seen_base.add(base)

    # dict 카테고리 → id만 추출
    clean_keys = []
    for k in keys:
        if isinstance(k, str):
            clean_keys.append(k)
        elif isinstance(k, dict) and 'id' in k:
            clean_keys.append(k['id'])

    # Minimal Object Cover에 Minimal Cover Glamour 키 병합
    if 'Minimal Object Cover' in name:
        for orig_name, orig_keys in cats.items():
            if 'Minimal Cover Glamour' in orig_name and 'Object' not in orig_name:
                for k in orig_keys:
                    if isinstance(k, str):
                        clean_keys.append(k)

    new_cats[name] = dedup(clean_keys)

print(f"\n정리 후 카테고리: {len(new_cats)}개")
print(f"총 키: {sum(len(v) for v in new_cats.values())}개")

# 파일 재생성
out = ['# -*- coding: utf-8 -*-\n']
out.append('"""\nLumineX Preset Metadata\n카테고리별 프리셋 키 목록 + HOF / SSS / SS 분류\n\ndashboard.py 에서 임포트 (A형)\n상위 파일을 변경하면 배포 설정도 확인\n"""\n\n')
out.append('PRESET_CATEGORIES = {\n')

for cat_name, keys in new_cats.items():
    out.append(f'    "{cat_name}": [\n')
    for i in range(0, len(keys), 8):
        chunk = keys[i:i+8]
        out.append('        ' + ', '.join(f'"{k}"' for k in chunk) + ',\n')
    out.append('    ],\n\n')

out.append('}\n\n')
out.append('from core.hof_tier import HOF_TIER  # HOF 추가는 core/hof_tier.py에서\n')

new_content = ''.join(out)

try:
    ast.parse(new_content)
    open(TARGET, 'w', encoding='utf-8').write(new_content)
    line_count = len(new_content.splitlines())
    print(f"\n저장 완료! {line_count}줄")

    # 카테고리별 키 수 출력
    print("\n카테고리별 키 수:")
    for k, v in new_cats.items():
        print(f"  {k[:35]:35s}: {len(v)}키")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
