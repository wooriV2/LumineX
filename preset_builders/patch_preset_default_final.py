# -*- coding: utf-8 -*-
"""
dashboard.py 패치 — preset default 최종 수정
st.rerun() 제거 (탭 구조 붕괴 원인)
key= 제거, session_state 제거
매 렌더링마다 load_preset() 읽어서 index= 직접 계산

실행: python preset_builders\patch_preset_default_final.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────
# 1. rerun 포함 로드 블록 제거 → 단순 변경 감지만 남기기
# ─────────────────────────────────────────────────────────

OLD_LOAD_BLOCK = """    # 프리셋 변경 감지 → session_state 초기화 + rerun
    if st.session_state.get("preset_selected", "") != selected_preset:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""
        # JSON 로드 후 session_state에 직접 세팅 (rerun 전에)
        def _find_key(d, val):
            if not val:
                return None
            val_lower = str(val).lower()
            for k, v in d.items():
                v_str = (v.get("gemini", "") if isinstance(v, dict) else str(v)).lower()
                if val_lower in v_str or v_str in val_lower:
                    return k
            return None
        try:
            _pdata = load_preset(selected_preset)
            _field_map = {
                "preset_appearance":  (MODEL_APPEARANCE,  _pdata.get("appearance", "")),
                "preset_hair_style":  (HAIR_STYLES,       _pdata.get("hair_style", "")),
                "preset_outfit":      (OUTFIT_TYPES,       _pdata.get("outfit", "")),
                "preset_material":    (MATERIALS,          _pdata.get("material", "")),
                "preset_environment": (ENVIRONMENTS,       _pdata.get("environment", "")),
                "preset_lighting":    (LIGHTING,           _pdata.get("lighting", "")),
                "preset_pose":        (POSES,              _pdata.get("pose", "")),
                "preset_framing":     (FRAMING,            _pdata.get("framing", "")),
                "preset_angle":       (CAMERA_ANGLES,      _pdata.get("angle", "")),
                "preset_style":       (STYLES,             _pdata.get("style", "")),
                "preset_image_style": (IMAGE_STYLE,        _pdata.get("image_style", "")),
                "preset_mood":        (MOOD,               _pdata.get("mood", "")),
                "preset_special_fx":  (SPECIAL_EFFECTS,    _pdata.get("special_fx", "")),
                "preset_weather":     (WEATHER,            _pdata.get("weather", "")),
                "preset_color_grade": (COLOR_GRADES,       _pdata.get("color_grade", "")),
                "preset_cover_style": (COVER_STYLES,       _pdata.get("cover_style", "")),
                "preset_footwear":    (FOOTWEAR,           _pdata.get("footwear", "")),
                "preset_nails":       (NAILS,              _pdata.get("nails", "")),
                "preset_skin_detail": (SKIN_DETAILS,       _pdata.get("skin_detail", "")),
                "preset_body_oil":    (BODY_OIL,           _pdata.get("body_oil", "")),
            }
            for ss_key, (d, raw_val) in _field_map.items():
                matched = _find_key(d, raw_val)
                st.session_state[ss_key] = matched if matched else NONE
        except Exception:
            pass
        st.rerun()"""

NEW_LOAD_BLOCK = """    # 프리셋 변경 감지
    if st.session_state.get("preset_selected", "") != selected_preset:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""

    # 매 렌더링마다 JSON 읽어서 default 계산
    def _pval(d, raw):
        \"\"\"dict에서 raw 값과 매칭되는 key 반환, 없으면 NONE\"\"\"
        if not raw:
            return NONE
        raw_lower = str(raw).lower()
        for k, v in d.items():
            v_str = (v.get("gemini", "") if isinstance(v, dict) else str(v)).lower()
            if raw_lower in v_str or v_str in raw_lower:
                return k
        return NONE

    def _pidx(opts, val):
        \"\"\"options 리스트에서 val의 index 반환, 없으면 0\"\"\"
        return opts.index(val) if val in opts else 0

    try:
        _pd = load_preset(selected_preset)
    except Exception:
        _pd = {}"""

assert OLD_LOAD_BLOCK in text, "로드 블록을 찾을 수 없어요."
text = text.replace(OLD_LOAD_BLOCK, NEW_LOAD_BLOCK, 1)
print("✅ 로드 블록 교체 완료 (rerun 제거, _pval/_pidx 헬퍼 추가)")

# ─────────────────────────────────────────────────────────
# 2. selectbox — key= 없이 index= 직접 계산
# ─────────────────────────────────────────────────────────

OLD_SELECTBOXES = """    col1, col2, col3 = st.columns(3)
    with col1:
        preset_appearance  = st.selectbox("👩 인종/국적",       [NONE] + list(MODEL_APPEARANCE.keys()), key="preset_appearance")
        preset_age         = st.selectbox("🎂 연령대",          [NONE] + list(AGE_APPEARANCE.keys()),   key="preset_age")
        preset_body        = st.selectbox("👤 체형",            [NONE] + list(MODEL_TYPES.keys()),      key="preset_body")
        preset_outfit      = st.selectbox("👗 의상",            [NONE] + list(OUTFIT_TYPES.keys()),     key="preset_outfit")
        preset_material    = st.selectbox("🧵 소재",            [NONE] + list(MATERIALS.keys()),        key="preset_material")
        preset_footwear    = st.selectbox("👠 신발",            [NONE] + list(FOOTWEAR.keys()),         key="preset_footwear")
        preset_nails       = st.selectbox("💅 네일",            [NONE] + list(NAILS.keys()),            key="preset_nails")
        preset_skin_detail = st.selectbox("🌿 피부 디테일",     [NONE] + list(SKIN_DETAILS.keys()),     key="preset_skin_detail")
        preset_body_oil    = st.selectbox("✨ 바디 오일",        [NONE] + list(BODY_OIL.keys()),         key="preset_body_oil")
    with col2:
        preset_hair_style  = st.selectbox("💇 헤어스타일",      [NONE] + list(HAIR_STYLES.keys()),      key="preset_hair_style")
        preset_pose        = st.selectbox("💃 포즈",            [NONE] + list(POSES.keys()),            key="preset_pose")
        preset_framing     = st.selectbox("🖼️ 프레이밍",        [NONE] + list(FRAMING.keys()),          key="preset_framing")
        preset_angle       = st.selectbox("📸 카메라 앵글",     [NONE] + list(CAMERA_ANGLES.keys()),    key="preset_angle")
        preset_lighting    = st.selectbox("💡 조명",            [NONE] + list(LIGHTING.keys()),         key="preset_lighting")
        preset_color_grade = st.selectbox("🎨 색감",            [NONE] + list(COLOR_GRADES.keys()),     key="preset_color_grade")
        preset_style       = st.selectbox("🎬 스타일",          [NONE] + list(STYLES.keys()),           key="preset_style")
        preset_cover_style = st.selectbox("📰 커버 스타일",     [NONE] + list(COVER_STYLES.keys()),     key="preset_cover_style")
    with col3:
        preset_environment = st.selectbox("🏙️ 환경",            [NONE] + list(ENVIRONMENTS.keys()),     key="preset_environment")
        preset_weather     = st.selectbox("🌦️ 날씨",            [NONE] + list(WEATHER.keys()),          key="preset_weather")
        preset_image_style = st.selectbox("📐 이미지 스타일",   [NONE] + list(IMAGE_STYLE.keys()),      key="preset_image_style")
        preset_special_fx  = st.selectbox("🌈 특수 효과",       [NONE] + list(SPECIAL_EFFECTS.keys()),  key="preset_special_fx")
        preset_mood        = st.selectbox("🎭 무드",            [NONE] + list(MOOD.keys()),             key="preset_mood")"""

NEW_SELECTBOXES = """    col1, col2, col3 = st.columns(3)
    with col1:
        _o = [NONE] + list(MODEL_APPEARANCE.keys())
        preset_appearance  = st.selectbox("👩 인종/국적",       _o, index=_pidx(_o, _pval(MODEL_APPEARANCE,  _pd.get("appearance",  ""))))
        _o = [NONE] + list(AGE_APPEARANCE.keys())
        preset_age         = st.selectbox("🎂 연령대",          _o, index=_pidx(_o, _pval(AGE_APPEARANCE,    _pd.get("age",         ""))))
        _o = [NONE] + list(MODEL_TYPES.keys())
        preset_body        = st.selectbox("👤 체형",            _o, index=_pidx(_o, _pval(MODEL_TYPES,       _pd.get("body",        ""))))
        _o = [NONE] + list(OUTFIT_TYPES.keys())
        preset_outfit      = st.selectbox("👗 의상",            _o, index=_pidx(_o, _pval(OUTFIT_TYPES,      _pd.get("outfit",      ""))))
        _o = [NONE] + list(MATERIALS.keys())
        preset_material    = st.selectbox("🧵 소재",            _o, index=_pidx(_o, _pval(MATERIALS,         _pd.get("material",    ""))))
        _o = [NONE] + list(FOOTWEAR.keys())
        preset_footwear    = st.selectbox("👠 신발",            _o, index=_pidx(_o, _pval(FOOTWEAR,          _pd.get("footwear",    ""))))
        _o = [NONE] + list(NAILS.keys())
        preset_nails       = st.selectbox("💅 네일",            _o, index=_pidx(_o, _pval(NAILS,             _pd.get("nails",       ""))))
        _o = [NONE] + list(SKIN_DETAILS.keys())
        preset_skin_detail = st.selectbox("🌿 피부 디테일",     _o, index=_pidx(_o, _pval(SKIN_DETAILS,      _pd.get("skin_detail", ""))))
        _o = [NONE] + list(BODY_OIL.keys())
        preset_body_oil    = st.selectbox("✨ 바디 오일",        _o, index=_pidx(_o, _pval(BODY_OIL,          _pd.get("body_oil",    ""))))
    with col2:
        _o = [NONE] + list(HAIR_STYLES.keys())
        preset_hair_style  = st.selectbox("💇 헤어스타일",      _o, index=_pidx(_o, _pval(HAIR_STYLES,       _pd.get("hair_style",  ""))))
        _o = [NONE] + list(POSES.keys())
        preset_pose        = st.selectbox("💃 포즈",            _o, index=_pidx(_o, _pval(POSES,             _pd.get("pose",        ""))))
        _o = [NONE] + list(FRAMING.keys())
        preset_framing     = st.selectbox("🖼️ 프레이밍",        _o, index=_pidx(_o, _pval(FRAMING,           _pd.get("framing",     ""))))
        _o = [NONE] + list(CAMERA_ANGLES.keys())
        preset_angle       = st.selectbox("📸 카메라 앵글",     _o, index=_pidx(_o, _pval(CAMERA_ANGLES,     _pd.get("angle",       ""))))
        _o = [NONE] + list(LIGHTING.keys())
        preset_lighting    = st.selectbox("💡 조명",            _o, index=_pidx(_o, _pval(LIGHTING,          _pd.get("lighting",    ""))))
        _o = [NONE] + list(COLOR_GRADES.keys())
        preset_color_grade = st.selectbox("🎨 색감",            _o, index=_pidx(_o, _pval(COLOR_GRADES,      _pd.get("color_grade", ""))))
        _o = [NONE] + list(STYLES.keys())
        preset_style       = st.selectbox("🎬 스타일",          _o, index=_pidx(_o, _pval(STYLES,            _pd.get("style",       ""))))
        _o = [NONE] + list(COVER_STYLES.keys())
        preset_cover_style = st.selectbox("📰 커버 스타일",     _o, index=_pidx(_o, _pval(COVER_STYLES,      _pd.get("cover_style", ""))))
    with col3:
        _o = [NONE] + list(ENVIRONMENTS.keys())
        preset_environment = st.selectbox("🏙️ 환경",            _o, index=_pidx(_o, _pval(ENVIRONMENTS,      _pd.get("environment", ""))))
        _o = [NONE] + list(WEATHER.keys())
        preset_weather     = st.selectbox("🌦️ 날씨",            _o, index=_pidx(_o, _pval(WEATHER,           _pd.get("weather",     ""))))
        _o = [NONE] + list(IMAGE_STYLE.keys())
        preset_image_style = st.selectbox("📐 이미지 스타일",   _o, index=_pidx(_o, _pval(IMAGE_STYLE,       _pd.get("image_style", ""))))
        _o = [NONE] + list(SPECIAL_EFFECTS.keys())
        preset_special_fx  = st.selectbox("🌈 특수 효과",       _o, index=_pidx(_o, _pval(SPECIAL_EFFECTS,   _pd.get("special_fx",  ""))))
        _o = [NONE] + list(MOOD.keys())
        preset_mood        = st.selectbox("🎭 무드",            _o, index=_pidx(_o, _pval(MOOD,              _pd.get("mood",        ""))))"""

assert OLD_SELECTBOXES in text, "selectbox 블록을 찾을 수 없어요."
text = text.replace(OLD_SELECTBOXES, NEW_SELECTBOXES, 1)
print("✅ selectbox key= 제거 + index= 직접 계산 완료")

DASHBOARD.write_text(text, encoding="utf-8")
print("✅ dashboard.py 저장 완료")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")
assert "st.rerun()" not in verify or verify.count("st.rerun()") <= 2, "st.rerun() 잔존 확인 필요"
assert "_pval(" in verify,            "❌ _pval 함수 없음"
assert "_pidx(" in verify,            "❌ _pidx 함수 없음"
assert OLD_SELECTBOXES not in verify, "❌ 구버전 selectbox 잔존"
rerun_count = verify.count("st.rerun()")
print(f"✅ 검증 통과 (st.rerun 잔존: {rerun_count}개 — 다른 탭 용도)")
print("\n🎉 완료! git add dashboard.py; git commit; git push 후 Cloud reboot")
