"""
patch_season_theme_group34_sss.py
==================================
적용 대상: C:\\Dev\\LumineX\\dashboard.py
커밋 베이스: 5a6e5cd

변경 내용:
1. SSS_TIER — halloween_glam / new_year_glam / sakura_night_glam 승격
2. SS_TIER  — 계절&테마 그룹3 SS 추가
   midsummer_heat, rainy_season, harvest_moon, winter_solstice, cherry_blossom_night
3. SS_TIER  — 계절&테마 그룹4 SS 추가
   tropical_monsoon, halloween_glam, new_year_glam, sakura_night_glam, monsoon_goddess

실행:
    python preset_builders/patch_season_theme_group34_sss.py
"""

from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

# ── 1. SSS_TIER 추가 블록 ────────────────────────────────────────────────
SSS_ANCHOR = '''\
    # 2026-06-15 harajuku_doll SSS 승격 (팝&카와이 — 다케시타 거리 싱크 4장 검증)
    "harajuku_doll",
    # 2026-06-15 greenhouse_eden SSS 승격 (계절&테마 — 잎사귀 드레스=온실 생태계 융합 6장 검증)
    "greenhouse_eden",
}'''

SSS_NEW = '''\
    # 2026-06-15 harajuku_doll SSS 승격 (팝&카와이 — 다케시타 거리 싱크 4장 검증)
    "harajuku_doll",
    # 2026-06-15 greenhouse_eden SSS 승격 (계절&테마 — 잎사귀 드레스=온실 생태계 융합 6장 검증)
    "greenhouse_eden",
    # 2026-06-15 계절&테마 SSS 3종 확정
    "halloween_glam",       # 의상+배경+소품 = 고딕 세계관 완전 융합, 6장 검증
    "new_year_glam",        # 드레스 시퀀 = 폭죽+컨페티 빛 흡수, 타임스퀘어 4장 검증
    "sakura_night_glam",    # 드레스 플로럴 = 벚꽃 터널 패턴 연속, 신사 등불 6장 검증
}'''

# ── 2. SS_TIER 추가 블록 ────────────────────────────────────────────────
SS_ANCHOR = '''\
    # 2026-06-15 계절&테마 그룹1 SS 확정 (cherry_blossom~autumn_forest)
    "cherry_blossom",
    "lavender_field",
    "spring_rain",
    "tulip_field",
    "autumn_forest",
    # 2026-06-15 계절&테마 그룹2 SS 확정 (sunflower_field~golden_autumn)
    "sunflower_field",
    "greenhouse_eden",   # SSS도 SS에 포함 (format_preset 로직)
    "tropical_night",
    "first_snow",
    "golden_autumn",
    # 2026-06-15 harajuku_doll SSS도 SS에 포함
    "harajuku_doll",
}'''

SS_NEW = '''\
    # 2026-06-15 계절&테마 그룹1 SS 확정 (cherry_blossom~autumn_forest)
    "cherry_blossom",
    "lavender_field",
    "spring_rain",
    "tulip_field",
    "autumn_forest",
    # 2026-06-15 계절&테마 그룹2 SS 확정 (sunflower_field~golden_autumn)
    "sunflower_field",
    "greenhouse_eden",   # SSS도 SS에 포함 (format_preset 로직)
    "tropical_night",
    "first_snow",
    "golden_autumn",
    # 2026-06-15 harajuku_doll SSS도 SS에 포함
    "harajuku_doll",
    # 2026-06-15 계절&테마 그룹3 SS 확정
    "midsummer_heat",
    "rainy_season",
    "harvest_moon",
    "winter_solstice",
    "cherry_blossom_night",
    # 2026-06-15 계절&테마 그룹4 SS 확정
    "tropical_monsoon",
    "halloween_glam",       # SSS도 SS에 포함
    "new_year_glam",        # SSS도 SS에 포함
    "sakura_night_glam",    # SSS도 SS에 포함
    "monsoon_goddess",
}'''


def patch():
    src = DASHBOARD.read_text(encoding="utf-8")

    # ── SSS 패치 ──
    if "2026-06-15 계절&테마 SSS 3종" in src:
        print("[SKIP] SSS_TIER 그룹4 패치 이미 적용됨")
    else:
        if SSS_ANCHOR not in src:
            raise ValueError("SSS_TIER 앵커를 찾을 수 없습니다. dashboard.py 버전을 확인하세요.")
        src = src.replace(SSS_ANCHOR, SSS_NEW, 1)
        print("[OK] SSS_TIER 패치 완료 (halloween_glam, new_year_glam, sakura_night_glam)")

    # ── SS 패치 ──
    if "2026-06-15 계절&테마 그룹3 SS 확정" in src:
        print("[SKIP] SS_TIER 그룹3+4 패치 이미 적용됨")
    else:
        if SS_ANCHOR not in src:
            raise ValueError("SS_TIER 앵커를 찾을 수 없습니다. dashboard.py 버전을 확인하세요.")
        src = src.replace(SS_ANCHOR, SS_NEW, 1)
        print("[OK] SS_TIER 패치 완료 (그룹3+4 10종 추가)")

    DASHBOARD.write_text(src, encoding="utf-8")
    print(f"\n✅ 패치 완료 → {DASHBOARD}")
    print("다음 단계: Select-String 검증 후 커밋&푸시")


if __name__ == "__main__":
    patch()
