"""
patch_editorial_mood_ss_sss.py
================================
적용 대상: C:\\Dev\\LumineX\\dashboard.py
커밋 베이스: aefecae

변경 내용:
1. SSS_TIER — 에디토리얼&무드 SSS 8종 추가
   backlit_silk, mirror_room, eclipse_body, plasma_aura,
   molten_chrome, mercury_pool, snowflake_skin, noir_femme_fatale

2. SS_TIER — 에디토리얼&무드 전체 29종 추가
   그룹1: silhouette_only, back_beauty, collarbone_focus, neck_elegance, long_legs_focus
   그룹2: light_driven, backlit_silk, mirror_goddess, mirror_room, eclipse_body
   그룹3: chrome_skin, neon_body, plasma_aura, molten_chrome, mercury_rising
   그룹4: mercury_pool, titanium_body, snowflake_skin, 80s_power, y2k_chrome
   그룹5: bohemian_paris, origami_couture, wet_glass, smoke_studio, infrared_beauty
   그룹6: grain_film, dreamy_soft_focus, film_noir_glam, noir_femme_fatale

실행:
    python preset_builders/patch_editorial_mood_ss_sss.py
"""

from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

# ── 1. SSS_TIER 추가 ────────────────────────────────────────────────────
SSS_ANCHOR = '''\
    # 2026-06-15 계절&테마 SSS 3종 확정
    "halloween_glam",       # 의상+배경+소품 = 고딕 세계관 완전 융합, 6장 검증
    "new_year_glam",        # 드레스 시퀀 = 폭죽+컨페티 빛 흡수, 타임스퀘어 4장 검증
    "sakura_night_glam",    # 드레스 플로럴 = 벚꽃 터널 패턴 연속, 신사 등불 6장 검증
}'''

SSS_NEW = '''\
    # 2026-06-15 계절&테마 SSS 3종 확정
    "halloween_glam",       # 의상+배경+소품 = 고딕 세계관 완전 융합, 6장 검증
    "new_year_glam",        # 드레스 시퀀 = 폭죽+컨페티 빛 흡수, 타임스퀘어 4장 검증
    "sakura_night_glam",    # 드레스 플로럴 = 벚꽃 터널 패턴 연속, 신사 등불 6장 검증
    # 2026-06-15 에디토리얼&무드 SSS 8종 확정
    "backlit_silk",         # 역광 투과 → 드레스=광원, waitomo_glow 논리 동일
    "mirror_room",          # 실버수트+거울방 경계 소멸, dressing_room_mirror보다 강함
    "eclipse_body",         # 드레스=코로나 발광, 우주현상=의상
    "plasma_aura",          # 플라즈마=의상 완전 융합, 에너지=드레스 (이미지6 기준)
    "molten_chrome",        # 용광로+녹는 크롬 물리적 동조, 소재=환경
    "mercury_pool",         # 수은 인체=수면 유체 연속성, 의상=액체
    "snowflake_skin",       # 아이스 드레스=설원 소재 동화 (이미지5 기준)
    "noir_femme_fatale",    # 흑백+5요소 세계관 완전 구현, halloween_glam 동일 논리
}'''

# ── 2. SS_TIER 추가 ────────────────────────────────────────────────────
SS_ANCHOR = '''\
    # 2026-06-15 계절&테마 그룹4 SS 확정
    "tropical_monsoon",
    "halloween_glam",       # SSS도 SS에 포함
    "new_year_glam",        # SSS도 SS에 포함
    "sakura_night_glam",    # SSS도 SS에 포함
    "monsoon_goddess",
}'''

SS_NEW = '''\
    # 2026-06-15 계절&테마 그룹4 SS 확정
    "tropical_monsoon",
    "halloween_glam",       # SSS도 SS에 포함
    "new_year_glam",        # SSS도 SS에 포함
    "sakura_night_glam",    # SSS도 SS에 포함
    "monsoon_goddess",
    # 2026-06-15 에디토리얼&무드 그룹1 SS 확정
    "silhouette_only",
    "back_beauty",
    "collarbone_focus",
    "neck_elegance",
    "long_legs_focus",
    # 2026-06-15 에디토리얼&무드 그룹2 SS 확정 (SSS 포함)
    "light_driven",
    "backlit_silk",         # SSS도 SS에 포함
    "mirror_goddess",
    "mirror_room",          # SSS도 SS에 포함
    "eclipse_body",         # SSS도 SS에 포함
    # 2026-06-15 에디토리얼&무드 그룹3 SS 확정 (SSS 포함)
    "chrome_skin",
    "neon_body",
    "plasma_aura",          # SSS도 SS에 포함
    "molten_chrome",        # SSS도 SS에 포함
    "mercury_rising",
    # 2026-06-15 에디토리얼&무드 그룹4 SS 확정 (SSS 포함)
    "mercury_pool",         # SSS도 SS에 포함
    "titanium_body",
    "snowflake_skin",       # SSS도 SS에 포함
    "80s_power",
    "y2k_chrome",
    # 2026-06-15 에디토리얼&무드 그룹5 SS 확정
    "bohemian_paris",
    "origami_couture",
    "wet_glass",
    "smoke_studio",
    "infrared_beauty",
    # 2026-06-15 에디토리얼&무드 그룹6 SS 확정 (SSS 포함)
    "grain_film",
    "dreamy_soft_focus",
    "film_noir_glam",
    "noir_femme_fatale",    # SSS도 SS에 포함
}'''


def patch():
    src = DASHBOARD.read_text(encoding="utf-8")

    # ── SSS 패치 ──
    if "2026-06-15 에디토리얼&무드 SSS 8종" in src:
        print("[SKIP] SSS_TIER 에디토리얼&무드 패치 이미 적용됨")
    else:
        if SSS_ANCHOR not in src:
            raise ValueError("SSS_TIER 앵커를 찾을 수 없습니다. dashboard.py 버전을 확인하세요.")
        src = src.replace(SSS_ANCHOR, SSS_NEW, 1)
        print("[OK] SSS_TIER 패치 완료 (에디토리얼&무드 SSS 8종)")

    # ── SS 패치 ──
    if "2026-06-15 에디토리얼&무드 그룹1 SS 확정" in src:
        print("[SKIP] SS_TIER 에디토리얼&무드 패치 이미 적용됨")
    else:
        if SS_ANCHOR not in src:
            raise ValueError("SS_TIER 앵커를 찾을 수 없습니다. dashboard.py 버전을 확인하세요.")
        src = src.replace(SS_ANCHOR, SS_NEW, 1)
        print("[OK] SS_TIER 패치 완료 (에디토리얼&무드 29종)")

    DASHBOARD.write_text(src, encoding="utf-8")
    print(f"\n✅ 패치 완료 → {DASHBOARD}")
    print("다음 단계: Select-String 검증 후 커밋&푸시")


if __name__ == "__main__":
    patch()
