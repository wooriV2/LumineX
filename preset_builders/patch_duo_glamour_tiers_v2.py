"""
LumineX — 듀오 글래머 티어 패치 v2
SSS_TIER / SS_TIER 가 set{} 구조임을 반영하여 수정
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

SSS_NEW = [
    # G1
    "duo_infinity_pool_contrast", "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide", "duo_bodypaint_vs_latex",
    "duo_ocean_bodypaint", "duo_golden_desert_bodypaint",
    "duo_aurora_bodypaint", "duo_cyberpunk_bodypaint",
    "duo_latex_color_block", "duo_latex_storm_opposites",
    "duo_dark_latex_power", "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    # G5
    "duo_versailles_latex_gold", "duo_champagne_gala", "duo_casino_power",
    # G6
    "duo_fire_and_ice", "duo_angel_devil", "duo_chrome_future",
    # G7
    "duo_sunset_silhouette", "duo_desert_minimal",
    "duo_kpop_stage", "duo_penthouse_power",
]

SS_ONLY_NEW = [
    "duo_rain_neon_soaked", "duo_jungle_tribal_bodypaint",
    "duo_monaco_yacht", "duo_villa_italy",
    "duo_ice_bath_contrast",
]

# SS_TIER에는 SSS 22종 + SS전용 5종 모두 등재
SS_ALL_NEW = SSS_NEW + SS_ONLY_NEW


def make_block(presets, label):
    lines = ",\n    ".join(f'"{p}"' for p in presets)
    return f"\n    # 듀오 글래머 {label}\n    {lines},"


def patch_set(content, tier_name, new_presets, label):
    """SSS_TIER = { 또는 SS_TIER = { 다음 첫 번째 항목 앞에 삽입"""
    anchor = f"{tier_name} = {{"
    idx = content.find(anchor)
    if idx == -1:
        print(f"⚠️  {anchor} 를 찾을 수 없습니다.")
        return content

    # { 바로 다음 위치
    insert_pos = idx + len(anchor)
    block = make_block(new_presets, label)
    content = content[:insert_pos] + block + content[insert_pos:]
    print(f"✅ {tier_name} 패치 완료 — {len(new_presets)}종 추가")
    return content


def patch_dashboard():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    content = patch_set(content, "SSS_TIER", SSS_NEW, "SSS (23종)")
    content = patch_set(content, "SS_TIER", SS_ALL_NEW, "SS (SSS 23종 + SS전용 5종)")

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n총 SSS: {len(SSS_NEW)}종 / SS 등재: {len(SS_ALL_NEW)}종")


if __name__ == "__main__":
    patch_dashboard()
