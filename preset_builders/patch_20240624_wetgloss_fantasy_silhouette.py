"""
LumineX 패치 스크립트
날짜: 2026-06-24
대상: 판타지&다크(26종) + 실루엣&섀도우(30종) + 웨트&글로스(30종)
커밋 기준: 3d2699c

실행: python preset_builders/patch_20240624_wetgloss_fantasy_silhouette.py
"""

from pathlib import Path

DASHBOARD = Path(__file__).parent.parent / "dashboard.py"

# ─── SSS_TIER 추가 블록 ───────────────────────────────────
SSS_ANCHOR = '    "jazz_dance_glam",\n}'

SSS_NEW = '''    "jazz_dance_glam",

    # 2026-06-24 판타지&다크 26종 전원 SSS
    "dark_mermaid","vampire_queen","angel_fallen","moon_goddess","demon_goddess","forest_witch",
    "pastel_fairy","medusa_queen","halloween_queen","hologram_ghost","glitch_beauty",
    "void_emergence","void_glamour","void_secret","crystal_goddess","toxic_bloom",
    "zombie_apocalypse","dark_academia","gothic_romance","double_exposure_dark",
    "double_exposure_ethereal","oil_slick_noir",
    "witch_ritual","fae_queen","cursed_beauty","shadow_realm",

    # 2026-06-24 실루엣&섀도우 30종 전원 SSS
    # G1 스포트라이트
    "silhouette_spotlight_smoke","silhouette_spotlight_latex","silhouette_spotlight_heels",
    "silhouette_spotlight_hair","silhouette_spotlight_dance","silhouette_spotlight_chair",
    "silhouette_spotlight_back","silhouette_spotlight_pole",
    # G2 창문/도어
    "silhouette_window_city","silhouette_window_rain","silhouette_window_sheer",
    "silhouette_doorway_light","silhouette_window_sunset","silhouette_window_neon",
    # G3 네온 실루엣
    "silhouette_neon_pink","silhouette_neon_blue","silhouette_neon_red",
    "silhouette_neon_purple","silhouette_neon_multicolor",
    # G4 자연광
    "silhouette_sunset_beach","silhouette_sunset_cliff","silhouette_moonlight","silhouette_aurora",
    # G5 수중/물
    "silhouette_pool_underwater","silhouette_pool_edge",
    # G6 실내/분위기
    "silhouette_bath_candle","silhouette_rain_wet","silhouette_fire_dark",
    "silhouette_candle_boudoir","silhouette_smoke_studio",

    # 2026-06-24 웨트&글로스 SSS 29종
    # G1 풀/수영장
    "pool_surface_break","pool_underwater_up","pool_edge_dripping","infinity_pool_wet",
    "hot_spring_steam","jacuzzi_bubbles",
    # G2 비/빗속
    "rain_window_inside","rain_street_soaked","rain_studio_dramatic","monsoon_body","rain_car_window",
    # G3 오일/글로스 드립
    "oil_pour_studio","oil_drip_back","honey_drip_body","chocolate_pour_gloss",
    "gloss_lips_drip","chrome_gloss_body",
    # G4 땀/열기
    "sweat_studio_light","heat_mirage_sweat","sauna_steam_body",
    # G5 결로/냉기
    "condensation_skin","ice_melt_drip","dew_morning_body","frost_breath_cold",
    # G6 기타 웨트
    "waterfall_direct","wave_crash_body","wet_silk_minimal",
    "bubble_bath_gloss","milk_bath_petals",
}'''

# ─── SS_TIER 추가 블록 ───────────────────────────────────
SS_ANCHOR = '    # 2026-06-24 퍼포먼스&댄스 G1+G2 SSS (SS 포함)\n    "flamenco_queen",\n    "tango_passion",\n    "ribbon_dance",\n    "aerial_silk",\n    "kathak_dance",\n    "hula_goddess",\n    "circus_performer",\n    "fire_dancer",\n    "masquerade_ball",\n    "samba_carnival",\n    "jazz_dance_glam",\n}'

SS_NEW = '''    # 2026-06-24 퍼포먼스&댄스 G1+G2 SSS (SS 포함)
    "flamenco_queen",
    "tango_passion",
    "ribbon_dance",
    "aerial_silk",
    "kathak_dance",
    "hula_goddess",
    "circus_performer",
    "fire_dancer",
    "masquerade_ball",
    "samba_carnival",
    "jazz_dance_glam",

    # 2026-06-24 판타지&다크 26종 (SS 포함)
    "dark_mermaid","vampire_queen","angel_fallen","moon_goddess","demon_goddess","forest_witch",
    "pastel_fairy","medusa_queen","halloween_queen","hologram_ghost","glitch_beauty",
    "void_emergence","void_glamour","void_secret","crystal_goddess","toxic_bloom",
    "zombie_apocalypse","dark_academia","gothic_romance","double_exposure_dark",
    "double_exposure_ethereal","oil_slick_noir",
    "witch_ritual","fae_queen","cursed_beauty","shadow_realm",

    # 2026-06-24 실루엣&섀도우 30종 (SS 포함)
    "silhouette_spotlight_smoke","silhouette_spotlight_latex","silhouette_spotlight_heels",
    "silhouette_spotlight_hair","silhouette_spotlight_dance","silhouette_spotlight_chair",
    "silhouette_spotlight_back","silhouette_spotlight_pole",
    "silhouette_window_city","silhouette_window_rain","silhouette_window_sheer",
    "silhouette_doorway_light","silhouette_window_sunset","silhouette_window_neon",
    "silhouette_neon_pink","silhouette_neon_blue","silhouette_neon_red",
    "silhouette_neon_purple","silhouette_neon_multicolor",
    "silhouette_sunset_beach","silhouette_sunset_cliff","silhouette_moonlight","silhouette_aurora",
    "silhouette_pool_underwater","silhouette_pool_edge",
    "silhouette_bath_candle","silhouette_rain_wet","silhouette_fire_dark",
    "silhouette_candle_boudoir","silhouette_smoke_studio",

    # 2026-06-24 웨트&글로스 30종 (SS 포함, SSS 29종 + SS 전용 1종)
    "pool_surface_break","pool_underwater_up","pool_edge_dripping","infinity_pool_wet",
    "hot_spring_steam","jacuzzi_bubbles",
    "rain_window_inside","rain_street_soaked","rain_studio_dramatic","monsoon_body","rain_car_window",
    "oil_pour_studio","oil_drip_back","honey_drip_body","chocolate_pour_gloss",
    "gloss_lips_drip","chrome_gloss_body",
    "sweat_studio_light","after_workout_glow","heat_mirage_sweat","sauna_steam_body",
    "condensation_skin","ice_melt_drip","dew_morning_body","frost_breath_cold",
    "waterfall_direct","wave_crash_body","wet_silk_minimal",
    "bubble_bath_gloss","milk_bath_petals",
}'''


def patch():
    src = DASHBOARD.read_text(encoding="utf-8")

    # ── SSS_TIER 패치 ──
    if SSS_ANCHOR not in src:
        print("❌ SSS_TIER 앵커를 찾을 수 없습니다.")
        print("   앵커 문자열:", repr(SSS_ANCHOR))
        return
    src_sss = src.replace(SSS_ANCHOR, SSS_NEW, 1)
    if src_sss == src:
        print("⚠️  SSS_TIER 변경 없음 (이미 적용됐을 수 있음)")
    else:
        print("✅ SSS_TIER 패치 완료")

    # ── SS_TIER 패치 ──
    if SS_ANCHOR not in src_sss:
        print("❌ SS_TIER 앵커를 찾을 수 없습니다.")
        print("   앵커 문자열:", repr(SS_ANCHOR))
        return
    src_final = src_sss.replace(SS_ANCHOR, SS_NEW, 1)
    if src_final == src_sss:
        print("⚠️  SS_TIER 변경 없음 (이미 적용됐을 수 있음)")
    else:
        print("✅ SS_TIER 패치 완료")

    # ── 저장 ──
    DASHBOARD.write_text(src_final, encoding="utf-8")
    print("\n✅ dashboard.py 저장 완료")

    # ── 검증 ──
    verify = DASHBOARD.read_text(encoding="utf-8")
    checks = [
        ("판타지&다크", "dark_mermaid"),
        ("실루엣&섀도우", "silhouette_spotlight_smoke"),
        ("웨트&글로스 SSS", "pool_surface_break"),
        ("웨트&글로스 SS전용", "after_workout_glow"),
        ("frost_breath_cold", "frost_breath_cold"),
    ]
    print("\n── 디스크 검증 ──")
    for label, key in checks:
        count = verify.count(f'"{key}"')
        status = "✅" if count >= 1 else "❌"
        print(f"  {status} {label} ({key}): {count}회")

    # SSS/SS 중복 확인
    sss_count = verify.count('"pool_surface_break"')
    print(f"\n  pool_surface_break SSS+SS 합계: {sss_count}회 (SSS=1, SS=1 → 정상=2)")


if __name__ == "__main__":
    patch()
