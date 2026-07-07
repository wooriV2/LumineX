"""
LumineX 삭제 패치 스크립트
삭제 대상: quad_four_horsewomen_apocalypse, trio_human_evolution_bodypaint
사유: 이미지 생성 불가
실행: python preset_builders/patch_delete_2종.py (C:\Dev\LumineX\ 에서)
"""

import re

DASHBOARD_PATH = "dashboard.py"

DELETE_KEYS = [
    "quad_four_horsewomen_apocalypse",
    "trio_human_evolution_bodypaint",
]

def remove_from_set(content: str, set_name: str, key: str) -> tuple[str, bool]:
    """Python set 블록에서 key를 제거. 제거 성공 시 True 반환."""
    # "key", 또는 'key', 형태 모두 처리
    pattern = rf'(\s*["\']){re.escape(key)}(["\'],?\n?)'
    new_content, count = re.subn(pattern, "", content)
    return new_content, count > 0

def remove_json_entry(content: str, key: str) -> tuple[str, bool]:
    """
    builders.py 스타일 dict/JSON 블록에서 "key": {...} 엔트리 제거.
    중괄호 중첩을 고려하여 해당 블록 전체를 제거.
    """
    start_pattern = rf'(\s*["\']){re.escape(key)}(["\'])\s*:\s*\{{'
    match = re.search(start_pattern, content)
    if not match:
        return content, False

    brace_start = content.index("{", match.start())
    depth = 0
    i = brace_start
    while i < len(content):
        if content[i] == "{":
            depth += 1
        elif content[i] == "}":
            depth -= 1
            if depth == 0:
                brace_end = i
                break
        i += 1

    # 엔트리 전체 (키+값+후행 쉼표/개행) 제거
    entry_start = match.start()
    entry_end = brace_end + 1
    # 후행 쉼표 제거
    tail = content[entry_end:]
    tail_stripped = tail.lstrip()
    if tail_stripped.startswith(","):
        entry_end += tail.index(",") + 1

    new_content = content[:entry_start] + content[entry_end:]
    return new_content, True


def patch_file(path: str, keys: list[str]):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    report = []

    for key in keys:
        changed_any = False

        # 1) SSS_TIER set에서 제거
        content, ok = remove_from_set(content, "SSS_TIER", key)
        if ok:
            report.append(f"  ✅ SSS_TIER에서 '{key}' 제거")
            changed_any = True

        # 2) SS_TIER set에서 제거
        content, ok = remove_from_set(content, "SS_TIER", key)
        if ok:
            report.append(f"  ✅ SS_TIER에서 '{key}' 제거")
            changed_any = True

        # 3) HOF_TIER set에서 제거
        content, ok = remove_from_set(content, "HOF_TIER", key)
        if ok:
            report.append(f"  ✅ HOF_TIER에서 '{key}' 제거")
            changed_any = True

        # 4) JSON/dict 엔트리 제거
        content, ok = remove_json_entry(content, key)
        if ok:
            report.append(f"  ✅ JSON 엔트리 '{key}' 제거")
            changed_any = True

        if not changed_any:
            report.append(f"  ⚠️  '{key}' — 해당 항목을 찾지 못했습니다 (이미 삭제됐거나 키 이름 확인 필요)")

    if content == original:
        print("변경 사항 없음. 파일을 저장하지 않았습니다.")
        for r in report:
            print(r)
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {path} 패치 완료\n")
    for r in report:
        print(r)


if __name__ == "__main__":
    print("=" * 55)
    print("LumineX 삭제 패치: 생성불가 프리셋 2종 제거")
    print("=" * 55)
    patch_file(DASHBOARD_PATH, DELETE_KEYS)
    print("\n📋 다음 단계:")
    print("  1. Select-String으로 키 잔존 여부 확인")
    print('     Select-String -Path dashboard.py -Pattern "quad_four_horsewomen_apocalypse|trio_human_evolution_bodypaint"')
    print("  2. 판정 대기 2종 이미지 결과 반영 후 최종 커밋")
