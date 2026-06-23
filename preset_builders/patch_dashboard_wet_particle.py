"""
LumineX dashboard.py 신규 카테고리 추가 패치
💧 웨트 & 글로스 (30종)
🌫️ 대기 & 파티클 (30종)

대상: C:\Dev\LumineX\dashboard.py
방식: str.replace 앵커
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ── 카테고리 프리셋 리스트 ─────────────────────────────────

WET_GLOSS_LIST = '''    "💧 웨트 & 글로스": [
        # 수영장/풀
        "pool_surface_break", "pool_underwater_up", "pool_edge_dripping",
        "infinity_pool_wet", "hot_spring_steam", "jacuzzi_bubbles",
        # 비/폭우
        "rain_window_inside", "rain_street_soaked", "rain_studio_dramatic",
        "monsoon_body", "rain_car_window",
        # 오일/글로스
        "oil_pour_studio", "oil_drip_back", "honey_drip_body",
        "chocolate_pour_gloss", "gloss_lips_drip", "chrome_gloss_body",
        # 땀/열기
        "sweat_studio_light", "after_workout_glow", "heat_mirage_sweat", "sauna_steam_body",
        # 결로/물방울
        "condensation_skin", "ice_melt_drip", "dew_morning_body", "frost_breath_cold",
        # 기타 웨트
        "waterfall_direct", "wave_crash_body", "wet_silk_minimal",
        "bubble_bath_gloss", "milk_bath_petals",
    ],'''

PARTICLE_LIST = '''    "🌫️ 대기 & 파티클": [
        # 스모크/연기
        "smoke_machine_club", "dry_ice_floor", "cigarette_smoke_noir",
        "incense_smoke_ritual", "smoke_color_holi", "fog_forest_mystery",
        # 파우더/더스트
        "gold_dust_pour", "holi_powder_explosion", "chalk_dust_sport",
        "flour_dust_studio", "pigment_powder_art",
        # 페더/페탈
        "feather_explosion", "black_feather_dark", "petal_storm_indoor",
        "cherry_blossom_burst", "dried_flower_cascade",
        # 글리터/파티클
        "glitter_rain_studio", "gold_confetti_burst", "silver_glitter_body",
        "neon_particle_club", "bubble_floating_studio",
        # 불/스파크
        "sparkler_night_glam", "fire_poi_dance", "ember_glow_dark", "firework_silhouette",
        # 자연 파티클
        "autumn_leaves_burst", "snow_indoor_studio", "dandelion_blow",
        "firefly_night_field", "seed_pod_floating",
    ],'''

# ── 앵커: PRESET_CATEGORIES 딕셔너리 닫는 } 바로 앞 마지막 카테고리 끝 ──
# dashboard.py 기준 마지막 카테고리: 🌋 엘리멘탈 갓데스
# 해당 카테고리 마지막 항목
ANCHOR = '''        "rainbow_falls_goddess",
    ],
}'''

REPLACEMENT = '''        "rainbow_falls_goddess",
    ],

''' + WET_GLOSS_LIST + '''

''' + PARTICLE_LIST + '''

}'''


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "💧 웨트 & 글로스" in content:
        print("[SKIP] 이미 패치됨 (웨트 & 글로스 존재)")
        return

    if ANCHOR not in content:
        print("[ERROR] 앵커를 찾을 수 없습니다.")
        print("  → dashboard.py의 PRESET_CATEGORIES 마지막 항목을 확인하세요.")
        print(f"  찾는 앵커:\n{ANCHOR}")
        return

    content = content.replace(ANCHOR, REPLACEMENT, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] PRESET_CATEGORIES 패치 완료")
    print("     💧 웨트 & 글로스 (30종) 추가")
    print("     🌫️ 대기 & 파티클 (30종) 추가")


def verify_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("💧 웨트 & 글로스", "카테고리"),
        ("🌫️ 대기 & 파티클", "카테고리"),
        ('"pool_surface_break"', "웨트 첫 프리셋"),
        ('"milk_bath_petals"', "웨트 마지막 프리셋"),
        ('"smoke_machine_club"', "파티클 첫 프리셋"),
        ('"seed_pod_floating"', "파티클 마지막 프리셋"),
    ]

    print("\n[VERIFY]")
    all_ok = True
    for pattern, label in checks:
        ok = pattern in content
        mark = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {mark} {label}: {pattern}")

    print("\n✅ 검증 통과!" if all_ok else "\n❌ 일부 누락")


if __name__ == "__main__":
    print("=" * 60)
    print("dashboard.py 신규 카테고리 추가 패치")
    print("=" * 60)
    apply_patch(DASHBOARD_PATH)
    verify_patch(DASHBOARD_PATH)
    print("\n다음 단계:")
    print("  1. streamlit run dashboard.py 로 카테고리 표시 확인")
    print("  2. core/engine.py 폴더명 인식 확인")
    print("  3. git add . && git commit")
