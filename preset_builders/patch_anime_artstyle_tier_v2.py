"""
LumineX 애니아트스타일 tier 패치 스크립트 v2
- SSS 31종 SSS_TIER에 추가
- SS 32종 SS_TIER에 추가 (SSS 31 + SS전용 1)
실행: python preset_builders\patch_anime_artstyle_tier_v2.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

SSS_LIST = [
    "anime_jp_90s_retro", "anime_jp_80s_citypop", "anime_jp_modern_glossy",
    "anime_jp_shoujo_soft", "anime_jp_shounen_action", "anime_jp_seinen_gritty",
    "anime_jp_makoto_watercolor", "anime_jp_ghibli_soft", "anime_jp_gekiga_noir",
    "anime_jp_pinup_retro", "anime_kr_webtoon_glossy", "anime_kr_romance_soft",
    "anime_kr_action_manhwa", "anime_kr_lezhin_mature", "anime_kr_pastel_dream",
    "anime_kr_lofi_chill", "anime_kr_noir_mature", "anime_cn_donghua_xianxia",
    "anime_cn_guofeng_ink", "anime_cn_modern_donghua", "anime_cn_palace_drama",
    "anime_us_cartoon_bold", "anime_us_comic_ink", "anime_us_pixar_stylized",
    "anime_us_disney_classic", "anime_us_pinup_classic", "anime_us_badgirl_comic",
    "anime_eu_ligne_claire", "anime_eu_graphic_novel", "anime_eu_erotic_bd",
    "anime_noir_silhouette",
]

SS_ONLY_LIST = ["anime_jp_ecchi_glossy"]

def patch_dashboard():
    with open(DASHBOARD, "r", encoding="utf-8") as f:
        content = f.read()

    # ── SSS_TIER 패치 ─────────────────────────────────────
    sss_anchor = "    # 2026-06-18 핫&섹시 SSS 확정"
    sss_tag = "# 2026-06-19 애니아트스타일 SSS 31종 확정"

    if sss_tag in content:
        print("⚠️  SSS_TIER 이미 패치됨 — 스킵")
    elif sss_anchor not in content:
        print("❌ SSS_TIER 앵커 찾기 실패")
        return
    else:
        sss_lines = f"    {sss_tag}\n"
        for name in SSS_LIST:
            sss_lines += f'    "{name}",\n'
        sss_lines += "\n"
        content = content.replace(sss_anchor, sss_lines + sss_anchor)
        print(f"✅ SSS_TIER에 {len(SSS_LIST)}종 추가")

    # ── SS_TIER 패치 ──────────────────────────────────────
    ss_anchor = "    # 2026-06-09 애니 아트스타일 SS 10종 확정 (JP4/KR3/CN2/EU1)"
    ss_tag = "# 2026-06-19 애니아트스타일 SS 전체 (SSS 31 + SS전용 1)"

    if ss_tag in content:
        print("⚠️  SS_TIER 이미 패치됨 — 스킵")
    elif ss_anchor not in content:
        print("❌ SS_TIER 앵커 찾기 실패")
        return
    else:
        ss_lines = f"    {ss_tag}\n"
        for name in SSS_LIST:
            ss_lines += f'    "{name}",\n'
        for name in SS_ONLY_LIST:
            ss_lines += f'    "{name}",\n'
        ss_lines += "\n"
        content = content.replace(ss_anchor, ss_lines + ss_anchor)
        print(f"✅ SS_TIER에 {len(SSS_LIST) + len(SS_ONLY_LIST)}종 추가")

    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(content)

    print("\n📋 검증:")
    print('Select-String -Path "C:\\Dev\\LumineX\\dashboard.py" -Pattern "anime_jp_90s_retro" | Select-Object LineNumber, Line')

if __name__ == "__main__":
    print("=" * 50)
    print("LumineX 애니아트스타일 Tier 패치 v2")
    print("=" * 50)
    patch_dashboard()
    print("\n🎉 완료!")
