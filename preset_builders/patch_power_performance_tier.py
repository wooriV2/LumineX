"""
LumineX SSS/SS Tier 패치
1. 파워 & 엣지 SSS 16종
2. 퍼포먼스 & 댄스 G1+G2 SSS 11종
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

POWER_EDGE_SSS = [
    "valkyrie_storm", "fencer_noir", "martial_arts", "boxing_glamour", "cage_fighter",
    "biker_glam", "riot_goddess", "punk_queen", "steel_warrior", "power_suit",
    "shadow_play", "power_curve", "sculpted_power", "shadow_queen",
    "bioluminescence", "bioluminescent",
]

PERFORMANCE_SSS = [
    "flamenco_queen", "tango_passion", "ribbon_dance", "aerial_silk",
    "kathak_dance", "hula_goddess",
    "circus_performer", "fire_dancer", "masquerade_ball",
    "samba_carnival", "jazz_dance_glam",
]

ALL_NEW = POWER_EDGE_SSS + PERFORMANCE_SSS

# SSS_TIER 앵커 — 마지막 항목
SSS_OLD = '    "black_sea_midnight",\n}'

SSS_NEW = '    "black_sea_midnight",\n\n    # 2026-06-24 파워&엣지 SSS 16종\n'
SSS_NEW += '\n'.join([f'    "{p}",' for p in POWER_EDGE_SSS])
SSS_NEW += '\n\n    # 2026-06-24 퍼포먼스&댄스 G1+G2 SSS 11종\n'
SSS_NEW += '\n'.join([f'    "{p}",' for p in PERFORMANCE_SSS])
SSS_NEW += '\n}'

# SS_TIER 앵커 — 마지막 항목
SS_OLD = '    "tropical_storm",\n}'

SS_NEW = '    "tropical_storm",\n\n    # 2026-06-24 파워&엣지 SSS (SS 포함)\n'
SS_NEW += '\n'.join([f'    "{p}",' for p in POWER_EDGE_SSS])
SS_NEW += '\n\n    # 2026-06-24 퍼포먼스&댄스 G1+G2 SSS (SS 포함)\n'
SS_NEW += '\n'.join([f'    "{p}",' for p in PERFORMANCE_SSS])
SS_NEW += '\n}'


def apply_patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    already = all(f'"{p}"' in content and content.index(f'"{p}"') > content.index("SSS_TIER") for p in POWER_EDGE_SSS[:3])
    if already:
        print("[SKIP] 이미 패치됨")
        return

    success = 0

    if SSS_OLD in content:
        content = content.replace(SSS_OLD, SSS_NEW, 1)
        success += 1
        print("[OK] SSS_TIER 패치 완료")
    else:
        print("[ERROR] SSS_TIER 앵커 미발견")
        # 디버그
        idx = content.find('"black_sea_midnight"')
        if idx > 0:
            print(f"  주변: {repr(content[idx:idx+50])}")

    if SS_OLD in content:
        content = content.replace(SS_OLD, SS_NEW, 1)
        success += 1
        print("[OK] SS_TIER 패치 완료")
    else:
        print("[ERROR] SS_TIER 앵커 미발견")
        idx = content.find('"tropical_storm"')
        while idx > 0:
            snippet = content[idx:idx+30]
            print(f"  tropical_storm 위치 {idx}: {repr(snippet)}")
            idx = content.find('"tropical_storm"', idx+1)

    if success > 0:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n[OK] {success}개 섹션 패치 저장 완료")


def verify_patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    sss_start = content.find("SSS_TIER = {")
    ss_start = content.find("SS_TIER = {")

    print("\n[VERIFY]")
    all_ok = True
    for p in ALL_NEW:
        # SSS_TIER 안에 있는지 확인
        ok = f'"{p}"' in content[sss_start:ss_start]
        mark = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {mark} {p}")

    print(f"\n{'✅ 전체 통과!' if all_ok else '❌ 일부 누락'}")


if __name__ == "__main__":
    print("=" * 55)
    print("파워&엣지 SSS 16종 + 퍼포먼스&댄스 G1/G2 SSS 11종")
    print("=" * 55)
    apply_patch(DASHBOARD_PATH)
    verify_patch(DASHBOARD_PATH)
    print("\n다음:")
    print("  git add dashboard.py")
    print('  git commit -m "feat: 파워&엣지 SSS 16종 + 퍼포먼스&댄스 G1/G2 SSS 11종 tier 패치"')
    print("  git push")
