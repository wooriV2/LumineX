"""
LumineX Tier 패치 스크립트
- quad_fashion_capitals_bodypaint → SSS_TIER 추가
- trio_inside_outside_bodypaint   → HOF_TIER 추가
실행: python preset_builders/patch_tier_final.py (C:\Dev\LumineX\ 에서)
"""

DASHBOARD_PATH = "dashboard.py"

ADD_SSS = ["quad_fashion_capitals_bodypaint"]
ADD_HOF = ["trio_inside_outside_bodypaint"]


def add_to_set(content: str, set_name: str, key: str) -> tuple[str, bool]:
    """set_name = { ... } 블록 안에 key 추가 (중복 방지)."""
    if f'"{key}"' in content or f"'{key}'" in content:
        return content, False  # 이미 존재

    # set 여는 중괄호 다음 줄에 삽입
    import re
    pattern = rf'({re.escape(set_name)}\s*=\s*\{{)'
    match = re.search(pattern, content)
    if not match:
        return content, False

    insert_pos = match.end()
    new_content = content[:insert_pos] + f'\n    "{key}",' + content[insert_pos:]
    return new_content, True


def patch_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    report = []

    for key in ADD_SSS:
        content, ok = add_to_set(content, "SSS_TIER", key)
        report.append(f"  {'✅' if ok else '⚠️ 이미 존재'} SSS_TIER ← '{key}'")

    for key in ADD_HOF:
        content, ok = add_to_set(content, "HOF_TIER", key)
        report.append(f"  {'✅' if ok else '⚠️ 이미 존재'} HOF_TIER ← '{key}'")

    if content == original:
        print("변경 사항 없음.")
        for r in report:
            print(r)
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {path} 패치 완료\n")
    for r in report:
        print(r)

    print("\n📋 검증 명령어:")
    print('  Select-String -Path dashboard.py -Pattern "quad_fashion_capitals_bodypaint|trio_inside_outside_bodypaint"')


if __name__ == "__main__":
    print("=" * 55)
    print("LumineX Tier 패치: SSS 1종 + HOF 1종")
    print("=" * 55)
    patch_file(DASHBOARD_PATH)
