"""
add_duo_category.py
dashboard.py에 👯 듀오 글래머 카테고리 추가
실행: python add_duo_category.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

# ── 1. PRESET_CATEGORIES에 듀오 카테고리 추가 ──
# 앵커: 한국 역사 카테고리 마지막 줄 바로 뒤
CAT_ANCHOR = '''        "hanbok_wet_editorial", "joseon_boudoir",
    ],

}'''

CAT_REPLACEMENT = '''        "hanbok_wet_editorial", "joseon_boudoir",
    ],

    "👯 듀오 글래머": [
        # G1 웨트 & 풀
        "duo_infinity_pool_contrast",
        "duo_rain_neon_soaked",
        "duo_pool_bodypaint_micro",
        "duo_wet_glass_divide",
        # G2 바디페인트 대결
        "duo_bodypaint_vs_latex",
        "duo_ocean_bodypaint",
        "duo_golden_desert_bodypaint",
        "duo_aurora_bodypaint",
        "duo_cyberpunk_bodypaint",
        "duo_jungle_tribal_bodypaint",
        # G3 라텍스 & 소재 대비
        "duo_latex_color_block",
        "duo_latex_storm_opposites",
        "duo_dark_latex_power",
        "duo_flamenco_latex_fusion",
        # G4 오일 & 그림자
        "duo_oiled_shadows",
        "duo_smoke_noir",
        # G5 럭셔리 씬
        "duo_versailles_latex_gold",
        "duo_monaco_yacht",
        "duo_champagne_gala",
        "duo_villa_italy",
        "duo_casino_power",
        # G6 엘리멘탈 대비
        "duo_fire_and_ice",
        "duo_angel_devil",
        "duo_chrome_future",
        # G7 실루엣 & 미니멀
        "duo_sunset_silhouette",
        "duo_desert_minimal",
        "duo_kpop_stage",
        "duo_penthouse_power",
        "duo_ice_bath_contrast",
    ],

}'''

def patch():
    text = DASHBOARD.read_text(encoding="utf-8")
    original = text

    # PRESET_CATEGORIES 패치
    if CAT_ANCHOR in text:
        text = text.replace(CAT_ANCHOR, CAT_REPLACEMENT)
        print("[PRESET_CATEGORIES] 👯 듀오 글래머 29종 추가 완료")
    else:
        print("[PRESET_CATEGORIES] 앵커를 찾지 못했습니다. 수동 확인 필요.")
        return

    if text != original:
        DASHBOARD.write_text(text, encoding="utf-8")
        print("✅ dashboard.py 저장 완료")
    else:
        print("⚠️  변경 없음")

if __name__ == "__main__":
    patch()
