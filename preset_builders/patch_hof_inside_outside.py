"""
LumineX HOF 패치 - trio_inside_outside_bodypaint HOF_TIER 추가
UTF-8 인코딩 안전 버전
실행: python preset_builders/patch_hof_inside_outside.py (C:\Dev\LumineX\ 에서)
"""

DASHBOARD_PATH = "dashboard.py"
TARGET = "trio_inside_outside_bodypaint"
ANCHOR = '"hexa_rainbow_spectrum_bodypaint",'


def patch():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 이미 HOF_TIER에 있는지 확인
    hof_start = content.find("HOF_TIER = {")
    hof_end = content.find("}", hof_start)
    hof_block = content[hof_start:hof_end]

    if TARGET in hof_block:
        print(f"⚠️  '{TARGET}' 이미 HOF_TIER에 존재합니다.")
        return

    # ANCHOR 뒤에 삽입
    insert_line = f'\n    "{TARGET}",        # 해부학 3레이어(피부/근육/골격) + 박물관 배경 HOF'
    new_content = content.replace(ANCHOR, ANCHOR + insert_line, 1)

    if new_content == content:
        print(f"❌ 앵커 '{ANCHOR}' 를 찾지 못했습니다.")
        return

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ HOF_TIER에 '{TARGET}' 추가 완료")
    print("\n📋 검증:")
    print(f'  Select-String -Path dashboard.py -Pattern "{TARGET}"')


if __name__ == "__main__":
    print("=" * 55)
    print("LumineX HOF 패치: trio_inside_outside_bodypaint")
    print("=" * 55)
    patch()
