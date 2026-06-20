"""
LumineX 애니아트스타일 tier 패치 스크립트
- SSS 31종 SSS_TIER에 추가
- SS 1종 (anime_jp_ecchi_glossy) SS_TIER에 추가
- SSS는 SS_TIER에도 반드시 포함 (format_preset 로직)
실행: python preset_builders\patch_anime_artstyle_tier.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

# ── SSS 31종 ──────────────────────────────────────────────
SSS_LIST = [
    "anime_jp_90s_retro",
    "anime_jp_80s_citypop",
    "anime_jp_modern_glossy",
    "anime_jp_shoujo_soft",
    "anime_jp_shounen_action",
    "anime_jp_seinen_gritty",
    "anime_jp_makoto_watercolor",
    "anime_jp_ghibli_soft",
    "anime_jp_gekiga_noir",
    "anime_jp_pinup_retro",
    "anime_kr_webtoon_glossy",
    "anime_kr_romance_soft",
    "anime_kr_action_manhwa",
    "anime_kr_lezhin_mature",
    "anime_kr_pastel_dream",
    "anime_kr_lofi_chill",
    "anime_kr_noir_mature",
    "anime_cn_donghua_xianxia",
    "anime_cn_guofeng_ink",
    "anime_cn_modern_donghua",
    "anime_cn_palace_drama",
    "anime_us_cartoon_bold",
    "anime_us_comic_ink",
    "anime_us_pixar_stylized",
    "anime_us_disney_classic",
    "anime_us_pinup_classic",
    "anime_us_badgirl_comic",
    "anime_eu_ligne_claire",
    "anime_eu_graphic_novel",
    "anime_eu_erotic_bd",
    "anime_noir_silhouette",
]

# ── SS 1종 (SSS 아닌 것) ──────────────────────────────────
SS_ONLY_LIST = [
    "anime_jp_ecchi_glossy",
]

def patch_dashboard():
    with open(DASHBOARD, "r", encoding="utf-8") as f:
        content = f.read()

    # ── SSS_TIER 앵커 ──────────────────────────────────────
    sss_anchor = "    # 2026-06-18 핫&섹시 SSS 확정"

    sss_lines = "\n    # 2026-06-19 애니아트스타일 SSS 31종 확정\n"
    for name in SSS_LIST:
        sss_lines += f'    "{name}",\n'

    if sss_anchor not in content:
        print("❌ SSS_TIER 앵커 찾기 실패")
        return

    # 이미 패치됐는지 확인
    if "anime_jp_90s_retro" in content:
        print("⚠️  애니아트스타일 SSS 이미 존재 — SSS_TIER 스킵")
    else:
        content = content.replace(sss_anchor, sss_lines + sss_anchor)
        print(f"✅ SSS_TIER에 {len(SSS_LIST)}종 추가")

    # ── SS_TIER 앵커 ──────────────────────────────────────
    ss_anchor = "    # 2026-06-09 애니 아트스타일 SS 10종 확정 (JP4/KR3/CN2/EU1)"

    ss_lines = "\n    # 2026-06-19 애니아트스타일 SS 전체 (SSS 포함)\n"
    # SSS도 SS에 포함
    for name in SSS_LIST:
        ss_lines += f'    "{name}",\n'
    # SS 전용
    for name in SS_ONLY_LIST:
        ss_lines += f'    "{name}",\n'

    if ss_anchor not in content:
        print("❌ SS_TIER 앵커 찾기 실패")
        return

    if "anime_jp_90s_retro" in content and "anime_kr_webtoon_glossy" in content:
        print("⚠️  애니아트스타일 SS 이미 존재 — SS_TIER 스킵")
    else:
        content = content.replace(ss_anchor, ss_lines + ss_anchor)
        print(f"✅ SS_TIER에 {len(SSS_LIST) + len(SS_ONLY_LIST)}종 추가 (SSS 31 + SS 1)")

    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(content)

    print("\n📋 검증 PowerShell 명령:")
    print('Select-String -Path "C:\\Dev\\LumineX\\dashboard.py" -Pattern "anime_jp_90s_retro"')
    print('Select-String -Path "C:\\Dev\\LumineX\\dashboard.py" -Pattern "anime_jp_ecchi_glossy"')

if __name__ == "__main__":
    print("=" * 50)
    print("LumineX 애니아트스타일 Tier 패치")
    print("=" * 50)
    patch_dashboard()
    print("\n🎉 패치 완료! streamlit run dashboard.py 로 확인하세요.")
