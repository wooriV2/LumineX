"""
LumineX — 듀오 글래머 티어 패치 스크립트
커밋 대상: a3802a5 이후

작업 내용:
1. dashboard.py SSS_TIER에 22종 추가
2. dashboard.py SS_TIER에 4종 추가 (SS 3종 + SSS는 SS에도 중복 등재 규칙 적용)
3. PRESET_CATEGORIES에서 duo_oiled_shadows 제거

SSS (22종):
  G1: duo_infinity_pool_contrast, duo_pool_bodypaint_micro,
      duo_wet_glass_divide, duo_bodypaint_vs_latex,
      duo_ocean_bodypaint, duo_golden_desert_bodypaint,
      duo_aurora_bodypaint, duo_cyberpunk_bodypaint,
      duo_latex_color_block, duo_latex_storm_opposites,
      duo_dark_latex_power, duo_flamenco_latex_fusion,
      duo_smoke_noir
  G5: duo_versailles_latex_gold, duo_champagne_gala, duo_casino_power
  G6: duo_fire_and_ice, duo_angel_devil, duo_chrome_future
  G7: duo_sunset_silhouette, duo_desert_minimal,
      duo_kpop_stage, duo_penthouse_power

SS (SS전용 4종 — SSS는 별도로 SS에도 등재됨):
  G1: duo_rain_neon_soaked, duo_jungle_tribal_bodypaint
  G5: duo_monaco_yacht, duo_villa_italy
  G7: duo_ice_bath_contrast
"""

import re

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ── 1. SSS 22종 ──────────────────────────────────────────────
SSS_NEW = [
    # G1
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_aurora_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    # G5
    "duo_versailles_latex_gold",
    "duo_champagne_gala",
    "duo_casino_power",
    # G6
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    # G7
    "duo_sunset_silhouette",
    "duo_desert_minimal",
    "duo_kpop_stage",
    "duo_penthouse_power",
]

# ── 2. SS전용 5종 (SSS는 SS에도 자동 등재되므로 여기선 SS전용만) ──
SS_ONLY_NEW = [
    "duo_rain_neon_soaked",
    "duo_jungle_tribal_bodypaint",
    "duo_monaco_yacht",
    "duo_villa_italy",
    "duo_ice_bath_contrast",
]

# ── 3. 삭제 대상 ──────────────────────────────────────────────
DELETE_PRESET = "duo_oiled_shadows"


def patch_dashboard():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # ── SSS_TIER 패치 ──────────────────────────────────────────
    sss_block = ",\n    ".join(f'"{p}"' for p in SSS_NEW)
    sss_insert = f"\n    # 듀오 글래머 SSS\n    {sss_block},"

    # 앵커: SSS_TIER 리스트 마지막 ] 직전에 삽입
    # 앵커 패턴: SSS_TIER = [ ... ] 구조에서 마지막 항목 뒤
    sss_anchor = "# SSS_TIER_END"
    if sss_anchor in content:
        content = content.replace(sss_anchor, f"{sss_insert}\n{sss_anchor}")
    else:
        # 앵커 없을 경우: SSS_TIER 리스트 닫는 ] 바로 앞에 삽입
        content = re.sub(
            r'(SSS_TIER\s*=\s*\[)(.*?)(\n\])',
            lambda m: m.group(1) + m.group(2) + sss_insert + m.group(3),
            content,
            flags=re.DOTALL
        )

    # ── SS_TIER 패치 ───────────────────────────────────────────
    # SSS 22종도 SS에 등재 (LumineX 규칙: SSS는 항상 SS에도 포함)
    ss_all = SSS_NEW + SS_ONLY_NEW
    ss_block = ",\n    ".join(f'"{p}"' for p in ss_all)
    ss_insert = f"\n    # 듀오 글래머 SS (SSS 포함)\n    {ss_block},"

    ss_anchor = "# SS_TIER_END"
    if ss_anchor in content:
        content = content.replace(ss_anchor, f"{ss_insert}\n{ss_anchor}")
    else:
        content = re.sub(
            r'(SS_TIER\s*=\s*\[)(.*?)(\n\])',
            lambda m: m.group(1) + m.group(2) + ss_insert + m.group(3),
            content,
            flags=re.DOTALL
        )

    # ── duo_oiled_shadows 삭제 ─────────────────────────────────
    # PRESET_CATEGORIES 내 항목 제거 (줄 단위)
    lines = content.split("\n")
    filtered = [
        line for line in lines
        if f'"{DELETE_PRESET}"' not in line and f"'{DELETE_PRESET}'" not in line
    ]
    content = "\n".join(filtered)

    if content == original:
        print("⚠️  변경 없음 — 앵커 패턴을 확인하세요.")
        return

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ 패치 완료")
    print(f"   SSS 추가: {len(SSS_NEW)}종")
    print(f"   SS 추가 (SSS 포함): {len(ss_all)}종")
    print(f"   삭제: {DELETE_PRESET}")


def verify():
    """패치 결과 검증 — PowerShell 명령어 출력"""
    checks = SSS_NEW[:3] + SS_ONLY_NEW[:2] + [DELETE_PRESET]
    print("\n📋 PowerShell 검증 명령어:")
    for key in checks:
        print(f'  Select-String -Path dashboard.py -Pattern "{key}"')
    print(f'\n  # {DELETE_PRESET} 은 0건이어야 정상')


if __name__ == "__main__":
    patch_dashboard()
    verify()
