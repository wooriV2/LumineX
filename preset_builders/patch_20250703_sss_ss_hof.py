"""
LumineX 2026-07-03 패치 스크립트
작업: preset_builders/ 에 저장 후 실행

처리 내용:
1. 제거 4종: glitter_pour_body, shibari_silk, chain_only, shower_editorial
2. SSS 52종 반영 (SSS_TIER + SS_TIER 동시)
3. SS 10종 반영 (SS_TIER만)
4. HOF_TIER set 신설 + 12종 추가
"""

import re
from pathlib import Path

DASHBOARD = Path("dashboard.py")

# ── 1. 제거할 프리셋 4종 ──────────────────────────────────
REMOVE_PRESETS = [
    "glitter_pour_body",
    "shibari_silk",
    "chain_only",
    "shower_editorial",
]

# ── 2. SSS 신규 52종 ──────────────────────────────────────
NEW_SSS = [
    # 오일/붓기 SSS 5종
    "champagne_pour_body",
    "wine_pour_body",
    "milk_pour_body",
    "honey_pour_body",
    "gold_paint_body",
    # 웨트/물 SSS 2종
    "hot_tub_goddess",
    "foam_bath_goddess",
    # 의상최소화 SSS 4종
    "pasties_editorial",
    "body_tape_art",
    "wrap_sarong_nude",
    "ribbon_only",
    # 핫환경 SSS 4종
    "desert_heat_nude",
    "jungle_wet_goddess",
    "steam_room_goddess",
    "volcanic_heat_body",
    # 소재 SSS 4종
    "liquid_latex_drip",
    "silver_foil_body",
    "holographic_latex",
    "mirror_latex",
    # 럭셔리 SSS 6종
    "private_pool_villa",
    "rooftop_pool_night",
    "penthouse_pool",
    "yacht_sunset_glam",
    "casino_vip_glam",
    "limo_glam",
    # 에디토리얼 SSS 6종
    "bed_editorial",
    "floor_editorial",
    "chair_editorial",
    "door_frame_glam",
    "staircase_glam",
    "elevator_glam",
    # 트리오A SSS 6종
    "trio_bodypaint_latex_frame",
    "trio_bodypaint_gown_frame",
    "trio_bodypaint_leather_frame",
    "trio_animal_bodypaint_latex",
    "trio_klimt_bodypaint_gold_gown",
    "trio_galaxy_bodypaint_chrome",
    # 듀오B SSS 7종
    "duo_bodypaint_latex",
    "duo_bodypaint_gown",
    "duo_bodypaint_leather",
    "duo_bodypaint_gold_dress",
    "duo_animal_bodypaint_latex",
    "duo_klimt_bodypaint_gown",
    "duo_galaxy_bodypaint_chrome",
    # 트리오C SSS 6종
    "trio_latex_bodypaint_center",
    "trio_gown_bodypaint_center",
    "trio_leather_bodypaint_center",
    "trio_bikini_bodypaint_center",
    "trio_sheer_bodypaint_center",
    "trio_chrome_bodypaint_center",
    # invisible_dress SSS (필터 우회 성공)
    "invisible_dress",
    # neon_latex SSS (필터 우회 성공)
    "neon_latex",
]

# ── 3. SS 전용 10종 (SSS 아님, SS_TIER에만 추가) ─────────
NEW_SS_ONLY = [
    # 오일/붓기 SS 2종
    "paint_pour_goddess",
    "neon_paint_pour",
    # 웨트/물 SS 5종
    "shower_goddess",
    "rain_soaked_nude",
    "waterfall_nude",
    "ocean_nude_editorial",
    "steam_bath_goddess",
    # 의상최소화 SS 1종
    "painted_jeans",
    # 핫환경 SS 1종
    "sauna_nude_editorial",
    # 소재 SS 1종
    "chrome_paint_body",
]

# ── 4. HOF_TIER 12종 ──────────────────────────────────────
HOF_PRESETS = [
    "trio_chrome_bodypaint_center",
    "trio_gown_bodypaint_center",
    "trio_sheer_bodypaint_center",
    "limo_glam",
    "yacht_sunset_glam",
    "staircase_glam",
    "volcanic_heat_body",
    "trio_three_civilizations_bodypaint",
    "trio_ancient_medieval_modern_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_fog_rain_snow_bodypaint",
]


def read_dashboard():
    return DASHBOARD.read_text(encoding="utf-8")


def write_dashboard(content):
    DASHBOARD.write_text(content, encoding="utf-8")


def remove_from_preset_categories(content, preset_name):
    """PRESET_CATEGORIES에서 프리셋 항목 제거"""
    # "preset_name", 또는 "preset_name" (줄 끝) 패턴
    patterns = [
        rf'^\s*"{preset_name}",?\s*\n',
        rf'^\s*"{preset_name}",?\s*#.*\n',
    ]
    for pat in patterns:
        content = re.sub(pat, '', content, flags=re.MULTILINE)
    return content


def remove_from_tier(content, preset_name, tier_name):
    """SSS_TIER 또는 SS_TIER에서 프리셋 제거"""
    patterns = [
        rf'^\s*"{preset_name}",?\s*\n',
        rf'^\s*"{preset_name}",?\s*#.*\n',
    ]
    for pat in patterns:
        content = re.sub(pat, '', content, flags=re.MULTILINE)
    return content


def add_to_sss_tier(content, presets):
    """SSS_TIER set에 새 프리셋 추가"""
    anchor = "# 2026-07-02 퍼포먼스&댄스 G3/G4 SSS (8종)"
    
    new_block = "    # 2026-07-03 신규 SSS 52종 (신규 66종 검증 완료)\n"
    for p in presets:
        new_block += f'    "{p}",\n'
    new_block += "\n"
    
    if anchor in content:
        content = content.replace(anchor, new_block + "    " + anchor)
    else:
        # fallback: SSS_TIER = { 바로 다음에 추가
        content = content.replace(
            "SSS_TIER = {\n",
            "SSS_TIER = {\n" + new_block
        )
    return content


def add_to_ss_tier(content, presets):
    """SS_TIER set에 새 프리셋 추가 (SSS + SS 전용 모두)"""
    anchor = "# 2026-07-02 퍼포먼스&댄스 G3/G4 SS (9종 전체)"
    
    new_block = "    # 2026-07-03 신규 SS 62종 반영 (SSS 52 + SS전용 10)\n"
    for p in presets:
        new_block += f'    "{p}",\n'
    new_block += "\n"
    
    if anchor in content:
        content = content.replace(anchor, new_block + "    " + anchor)
    else:
        content = content.replace(
            "SS_TIER = {\n",
            "SS_TIER = {\n" + new_block
        )
    return content


def add_hof_tier(content):
    """HOF_TIER set 신설 — SSS_TIER 바로 위에 삽입"""
    hof_block = """# HOF tier — Hall of Fame: 실제 검증 이미지 중 최고 퀄리티 선정
# 기준: "와" 하는 반응, 구도/배경/바디페인팅 삼박자 완벽, 즉시 생성 가능
HOF_TIER = {
    "trio_chrome_bodypaint_center",       # 크롬SF+갤럭시 구도 완벽
    "trio_gown_bodypaint_center",         # 황금바로크+이브닝가운 갤러리급
    "trio_sheer_bodypaint_center",        # 시어+플로럴 바디페인팅 최우수
    "limo_glam",                          # 럭셔리 완성도 최상
    "yacht_sunset_glam",                  # 배경+조명+의상 삼박자
    "staircase_glam",                     # 계단구도 에디토리얼 완성도
    "volcanic_heat_body",                 # 화산배경 독보적
    "trio_three_civilizations_bodypaint", # 3색대비+박물관 배경 완벽
    "trio_ancient_medieval_modern_bodypaint", # 배경3분할+시대별 컨셉 독창성 최고
    "trio_creation_of_adam_bodypaint",    # 시스티나+루브르 배경 예술적 완성도 독보적
    "trio_black_white_gray_bodypaint",    # 조각같은 완성도 흑/회/백 대비 압도적
    "trio_fog_rain_snow_bodypaint",       # 색감+통일감 압도적 안개/물/눈 완벽표현
}

"""
    # SSS_TIER 바로 앞에 삽입
    content = content.replace(
        "# SSS tier — ",
        hof_block + "# SSS tier — "
    )
    return content


def update_sidebar_stats(content):
    """사이드바에 HOF 카운트 추가"""
    old = '    st.markdown(f"**SSS tier:** `{len(SSS_TIER)}개`")'
    new = '''    st.markdown(f"**🌟 HOF tier:** `{len(HOF_TIER)}개`")
    st.markdown(f"**SSS tier:** `{len(SSS_TIER)}개`")'''
    content = content.replace(old, new)
    return content


def update_format_preset(content):
    """format_preset 함수에 HOF 배지 추가"""
    old = '''    def format_preset(name):
        if name in SSS_TIER:
            return f"🌟 {name} [SSS]"
        if name in SS_TIER:
            return f"⭐ {name} [SS]"
        return f"• {name}"'''
    
    new = '''    def format_preset(name):
        if name in HOF_TIER:
            return f"👑 {name} [HOF]"
        if name in SSS_TIER:
            return f"🌟 {name} [SSS]"
        if name in SS_TIER:
            return f"⭐ {name} [SS]"
        return f"• {name}"'''
    
    content = content.replace(old, new)
    return content


def add_hof_filter(content):
    """티어 필터에 HOF 옵션 추가"""
    old = '    tier_options = ["전체 티어", "⭐⭐⭐ SSS", "⭐⭐ SS", "• 일반"]'
    new = '    tier_options = ["전체 티어", "👑 HOF", "⭐⭐⭐ SSS", "⭐⭐ SS", "• 일반"]'
    content = content.replace(old, new)
    
    # 필터 로직에 HOF 추가
    old_filter = '''    if selected_tier == "⭐⭐⭐ SSS":
        filtered_presets = [p for p in filtered_presets if p in SSS_TIER]
    elif selected_tier == "⭐⭐ SS":
        filtered_presets = [p for p in filtered_presets if p in SS_TIER and p not in SSS_TIER]
    elif selected_tier == "• 일반":
        filtered_presets = [p for p in filtered_presets if p not in SS_TIER]'''
    
    new_filter = '''    if selected_tier == "👑 HOF":
        filtered_presets = [p for p in filtered_presets if p in HOF_TIER]
    elif selected_tier == "⭐⭐⭐ SSS":
        filtered_presets = [p for p in filtered_presets if p in SSS_TIER]
    elif selected_tier == "⭐⭐ SS":
        filtered_presets = [p for p in filtered_presets if p in SS_TIER and p not in SSS_TIER]
    elif selected_tier == "• 일반":
        filtered_presets = [p for p in filtered_presets if p not in SS_TIER]'''
    
    content = content.replace(old_filter, new_filter)
    return content


def delete_preset_json(preset_name):
    """presets/ 폴더에서 JSON 파일 삭제"""
    path = Path("presets") / f"{preset_name}.json"
    if path.exists():
        path.unlink()
        print(f"  🗑️  삭제: presets/{preset_name}.json")
    else:
        print(f"  ⚠️  없음 (이미 삭제?): presets/{preset_name}.json")


def main():
    print("=" * 60)
    print("LumineX 2026-07-03 패치 시작")
    print("=" * 60)

    # 1. dashboard.py 읽기
    content = read_dashboard()
    print(f"\n✅ dashboard.py 로드 ({len(content):,} chars)")

    # 2. JSON 파일 삭제
    print("\n🗑️  제거 4종 JSON 삭제")
    for p in REMOVE_PRESETS:
        delete_preset_json(p)

    # 3. PRESET_CATEGORIES에서 제거
    print("\n📂 PRESET_CATEGORIES에서 제거")
    for p in REMOVE_PRESETS:
        before = content.count(f'"{p}"')
        content = remove_from_preset_categories(content, p)
        after = content.count(f'"{p}"')
        print(f"  • {p}: {before} → {after}회")

    # 4. SSS_TIER / SS_TIER에서도 제거
    print("\n🏆 tier set에서 제거")
    for p in REMOVE_PRESETS:
        content = remove_from_tier(content, p, "SSS_TIER")
        content = remove_from_tier(content, p, "SS_TIER")
        print(f"  • {p} 제거 완료")

    # 5. HOF_TIER 신설 (SSS_TIER 앞에)
    print("\n👑 HOF_TIER 신설")
    if "HOF_TIER" not in content:
        content = add_hof_tier(content)
        print("  ✅ HOF_TIER set 추가")
    else:
        print("  ⚠️  HOF_TIER 이미 존재, 스킵")

    # 6. SSS 52종 + invisible_dress + neon_latex → SSS_TIER 추가
    print(f"\n🌟 SSS_TIER에 {len(NEW_SSS)}종 추가")
    content = add_to_sss_tier(content, NEW_SSS)
    print(f"  ✅ {len(NEW_SSS)}종 추가")

    # 7. SS_TIER에 SSS 52종 + SS 전용 10종 모두 추가
    all_new_ss = NEW_SSS + NEW_SS_ONLY
    print(f"\n⭐ SS_TIER에 {len(all_new_ss)}종 추가 (SSS+SS전용)")
    content = add_to_ss_tier(content, all_new_ss)
    print(f"  ✅ {len(all_new_ss)}종 추가")

    # 8. format_preset HOF 배지 추가
    print("\n🎨 UI 업데이트")
    content = update_format_preset(content)
    print("  ✅ format_preset에 HOF 배지 추가")

    content = add_hof_filter(content)
    print("  ✅ 티어 필터에 HOF 옵션 추가")

    content = update_sidebar_stats(content)
    print("  ✅ 사이드바 HOF 카운트 추가")

    # 9. 저장
    write_dashboard(content)
    print("\n✅ dashboard.py 저장 완료")

    # 10. 검증
    print("\n📊 검증")
    final = DASHBOARD.read_text(encoding="utf-8")
    
    # 제거 확인
    for p in REMOVE_PRESETS:
        count = final.count(f'"{p}"')
        status = "✅ 제거됨" if count == 0 else f"❌ 아직 {count}회 존재"
        print(f"  {p}: {status}")
    
    # HOF 확인
    hof_count = sum(1 for p in HOF_PRESETS if f'"{p}"' in final)
    print(f"  HOF_TIER 항목: {hof_count}/{len(HOF_PRESETS)}종")
    
    # SSS 샘플 확인
    sample_sss = ["trio_chrome_bodypaint_center", "limo_glam", "volcanic_heat_body"]
    for p in sample_sss:
        in_sss = f'"{p}"' in final
        print(f"  SSS {p}: {'✅' if in_sss else '❌'}")

    print("\n" + "=" * 60)
    print("패치 완료! git add -A && git commit -m '2026-07-03 SSS/SS/HOF 패치' 후 푸시하세요")
    print("=" * 60)


if __name__ == "__main__":
    main()
