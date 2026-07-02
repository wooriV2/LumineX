"""
LumineX dashboard.py 패치
🎭 퍼포먼스 & 댄스 G3/G4 tier 반영 (앵커 수정본)

SSS (8종): opera_night, christmas_glamour, ballet_noir, broadway_diva,
           street_dance, drag_glamour, ribbon_goddess, petal_storm
SS  (1종): pop_art_glamour

실행: python preset_builders/patch_performance_dance_g3g4.py
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

SSS_NEW = '''    # 2026-07-02 퍼포먼스&댄스 G3/G4 SSS (8종)
    "opera_night",
    "christmas_glamour",
    "ballet_noir",
    "broadway_diva",
    "street_dance",
    "drag_glamour",
    "ribbon_goddess",
    "petal_storm",'''

SS_NEW = '''    # 2026-07-02 퍼포먼스&댄스 G3/G4 SS (9종 전체)
    "opera_night",
    "christmas_glamour",
    "ballet_noir",
    "broadway_diva",
    "street_dance",
    "drag_glamour",
    "ribbon_goddess",
    "petal_storm",
    "pop_art_glamour",'''

SSS_ANCHOR = 'SSS_TIER = {\n    # 2026-06-29 멀티 바디페인팅'
SS_ANCHOR_FULL = '# SS tier\nSS_TIER = {'


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if '# 2026-07-02 퍼포먼스&댄스 G3/G4 SSS' in content:
        print("[SKIP] 이미 패치됨")
        return

    if SSS_ANCHOR in content:
        content = content.replace(
            SSS_ANCHOR,
            f"SSS_TIER = {{\n{SSS_NEW}\n\n    # 2026-06-29 멀티 바디페인팅"
        )
        print("[OK] SSS_TIER 추가")
    else:
        print("[ERROR] SSS 앵커 미발견")
        return

    if SS_ANCHOR_FULL in content:
        content = content.replace(
            SS_ANCHOR_FULL,
            f"# SS tier\nSS_TIER = {{\n{SS_NEW}"
        )
        print("[OK] SS_TIER 추가")
    else:
        print("[ERROR] SS 앵커 미발견")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ 패치 완료: {path}")


def verify(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("opera_night", 3),
        ("ballet_noir", 3),
        ("petal_storm", 3),
        ("drag_glamour", 3),
        ("pop_art_glamour", 2),
    ]
    print("\n=== 검증 ===")
    for keyword, expected in checks:
        count = content.count(f'"{keyword}"')
        status = "✅" if count >= expected else "⚠️"
        print(f"{status} {keyword}: {count}회 발견 (기대: {expected}+)")


if __name__ == "__main__":
    print("🎭 퍼포먼스&댄스 G3/G4 패치 (수정본)")
    print(f"대상: {DASHBOARD_PATH}")
    print()
    answer = input("패치 진행할까요? (y/n): ")
    if answer.lower() == "y":
        apply_patch(DASHBOARD_PATH)
        verify(DASHBOARD_PATH)
    else:
        print("취소됨")
