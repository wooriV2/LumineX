# migrate_inline_to_json.py
# presets_meta.py 인라인 프리셋 82개를 JSON 파일로 마이그레이션
# 실행 위치: C:\Dev\LumineX\
# 실행: python preset_builders/migrate_inline_to_json.py

import os
import json
import ast
import re

META_FILE = "core/presets_meta.py"
PRESETS_DIR = "presets"

# ── 1. presets_meta.py 읽기 ───────────────────────────────────────────────
with open(META_FILE, encoding="utf-8-sig") as f:
    source = f.read()

# ── 2. 인라인 프리셋 추출 ─────────────────────────────────────────────────
# presets_meta.py를 실행해서 딕셔너리 직접 파싱
# 인라인 프리셋은 PRESET_CATEGORIES 외부에 별도 딕셔너리로 존재
# "subject" 키를 가진 딕셔너리 블록을 찾아서 추출

# ast로 파싱해서 딕셔너리 찾기
tree = ast.parse(source)

inline_presets = {}  # key -> {subject, prompt, environment, lighting, style, quality}

for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        # 변수명이 단일 Name인 경우
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            var_name = node.targets[0].id
            # 값이 딕셔너리인 경우
            if isinstance(node.value, ast.Dict):
                outer_dict = node.value
                # 외부 딕셔너리의 키-값 순회
                for k, v in zip(outer_dict.keys, outer_dict.values):
                    if isinstance(k, ast.Constant) and isinstance(v, ast.Dict):
                        preset_key = k.value
                        # 내부 딕셔너리에 "subject" 키가 있으면 인라인 프리셋
                        inner_keys = [
                            ik.value for ik in v.keys
                            if isinstance(ik, ast.Constant)
                        ]
                        if "subject" in inner_keys:
                            preset_data = {}
                            for ik, iv in zip(v.keys, v.values):
                                if isinstance(ik, ast.Constant) and isinstance(iv, ast.Constant):
                                    preset_data[ik.value] = iv.value
                            inline_presets[preset_key] = preset_data
                            print(f"발견: {preset_key}")

print(f"\n총 인라인 프리셋: {len(inline_presets)}개")

# ── 3. JSON 파일 생성 ─────────────────────────────────────────────────────
created = 0
skipped = 0

for key, data in inline_presets.items():
    json_path = os.path.join(PRESETS_DIR, f"{key}.json")
    if os.path.exists(json_path):
        print(f"⚠️  이미 존재 스킵: {key}.json")
        skipped += 1
        continue

    # JSON 필드 정리
    json_data = {
        "subject": data.get("subject", ""),
        "prompt": data.get("prompt", ""),
        "environment": data.get("environment", ""),
        "lighting": data.get("lighting", ""),
        "style": data.get("style", ""),
        "quality": data.get("quality", ""),
    }
    # 빈 필드 제거
    json_data = {k: v for k, v in json_data.items() if v}

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"✅ 생성: {key}.json")
    created += 1

print(f"\nJSON 생성: {created}개 / 스킵: {skipped}개")

# ── 4. presets_meta.py에서 인라인 데이터 제거 ────────────────────────────
# 인라인 딕셔너리 블록을 찾아서 키 리스트만 남기기
# 패턴: VARNAME = { "key": { "subject": ..., ... }, ... }
# → VARNAME = { ... } 내부의 subject 포함 딕셔너리를 키만 남기도록 변환

new_source = source

for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            var_name = node.targets[0].id
            if isinstance(node.value, ast.Dict):
                outer_dict = node.value
                has_inline = False
                for k, v in zip(outer_dict.keys, outer_dict.values):
                    if isinstance(k, ast.Constant) and isinstance(v, ast.Dict):
                        inner_keys = [
                            ik.value for ik in v.keys
                            if isinstance(ik, ast.Constant)
                        ]
                        if "subject" in inner_keys:
                            has_inline = True
                            break

                if has_inline:
                    # 이 딕셔너리 블록 전체를 키 리스트만 남기도록 재작성
                    keys_only = []
                    for k, v in zip(outer_dict.keys, outer_dict.values):
                        if isinstance(k, ast.Constant):
                            keys_only.append(k.value)

                    # 원본 블록의 시작/끝 위치 찾기 (줄 번호 기반)
                    start_line = node.lineno
                    end_line = node.end_lineno

                    lines = new_source.split("\n")
                    # 변수명 줄부터 end_line까지 교체
                    new_block_lines = [f"{var_name} = {{"]
                    for key in keys_only:
                        new_block_lines.append(f'    "{key}",')
                    new_block_lines.append("}")

                    # 원본 줄 교체 (1-indexed → 0-indexed)
                    lines[start_line - 1:end_line] = new_block_lines
                    new_source = "\n".join(lines)
                    print(f"✅ {var_name} 인라인 → 키 리스트 변환")

# ── 5. 검증 후 저장 ───────────────────────────────────────────────────────
try:
    ast.parse(new_source)
    print("\n✅ AST 검증 통과")
except SyntaxError as e:
    print(f"\n❌ AST 검증 실패: {e}")
    print("presets_meta.py 저장 취소 — JSON 파일만 생성됨")
    exit(1)

with open(META_FILE, "w", encoding="utf-8") as f:
    f.write(new_source)

print(f"✅ presets_meta.py 업데이트 완료")

# ── 6. 최종 확인 ──────────────────────────────────────────────────────────
remaining = 0
with open(META_FILE, encoding="utf-8") as f:
    for line in f:
        if '"subject":' in line:
            remaining += 1

total_json = len([f for f in os.listdir(PRESETS_DIR) if f.endswith(".json")])

print(f"\n=== 마이그레이션 결과 ===")
print(f"JSON 파일 총계: {total_json}개")
print(f"presets_meta.py 남은 인라인: {remaining}개")
print(f"\n다음 단계:")
print("python -c \"import ast; ast.parse(open('core/presets_meta.py',encoding='utf-8').read()); print('OK')\"")
print("(Get-ChildItem presets\\*.json).Count")
print("git add -A")
print("git commit -m \"refactor: 인라인 프리셋 82개 JSON 마이그레이션\"")
print("git push")
