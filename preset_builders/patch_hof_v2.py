"""
LumineX HOF 패치 v2 - trio_inside_outside_bodypaint HOF_TIER 정밀 추가
HOF_TIER 블록 closing brace 바로 앞에 삽입
실행: python preset_builders/patch_hof_v2.py (C:\Dev\LumineX\ 에서)
"""

DASHBOARD_PATH = "dashboard.py"
TARGET = '"trio_inside_outside_bodypaint"'
COMMENT = "        # 해부학 3레이어(피부/근육/골격) + 박물관 배경 HOF"
ANCHOR = '"hexa_rainbow_spectrum_bodypaint",'


def patch():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # HOF_TIER 블록 찾기
    hof_start = None
    hof_end = None
    for i, line in enumerate(lines):
        if "HOF_TIER = {" in line:
            hof_start = i
        if hof_start and i > hof_start and line.strip() == "}":
            hof_end = i
            break

    if hof_start is None or hof_end is None:
        print("❌ HOF_TIER 블록을 찾지 못했습니다.")
        return

    print(f"HOF_TIER 블록: {hof_start+1}번 ~ {hof_end+1}번 줄")

    # 이미 있는지 확인
    hof_block = "".join(lines[hof_start:hof_end])
    if "trio_inside_outside_bodypaint" in hof_block:
        print("⚠️  이미 HOF_TIER 블록 내에 존재합니다.")
        return

    # ANCHOR 줄 찾기 (HOF_TIER 블록 내에서)
    anchor_line = None
    for i in range(hof_start, hof_end):
        if ANCHOR in lines[i]:
            anchor_line = i
            break

    if anchor_line is None:
        print(f"❌ 앵커 '{ANCHOR}'를 HOF_TIER 블록 내에서 찾지 못했습니다.")
        print("HOF_TIER 블록 내 마지막 항목 앞에 삽입합니다...")
        insert_pos = hof_end
        new_line = f'    {TARGET},{COMMENT}\n'
        lines.insert(insert_pos, new_line)
    else:
        insert_pos = anchor_line + 1
        new_line = f'    {TARGET},{COMMENT}\n'
        lines.insert(insert_pos, new_line)
        print(f"✅ {anchor_line+1}번 줄 뒤에 삽입")

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✅ HOF_TIER에 'trio_inside_outside_bodypaint' 추가 완료")
    print("\n📋 검증:")
    print('  Select-String -Path dashboard.py -Pattern "HOF_TIER = {" -Context 0,25')


if __name__ == "__main__":
    print("=" * 55)
    print("LumineX HOF 패치 v2")
    print("=" * 55)
    patch()
