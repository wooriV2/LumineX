# -*- coding: utf-8 -*-
"""
dashboard.py 패치 — preset default Cloud 호환 (방식 전면 변경)
key= + index= 동시 사용 제거 → session_state 직접 세팅 방식으로

실행: python preset_builders\patch_preset_default_v3.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────
# 1. _find_key + _load_preset_defaults + _prev_selected 블록 제거
#    (이전 패치 2개로 삽입된 코드 전체 교체)
# ─────────────────────────────────────────────────────────

OLD_LOAD_BLOCK = """    def _find_key(d, val):
        if not val:
            return None
        val_lower = str(val).lower()
        for k, v in d.items():
            v_str = (v.get("gemini", "") if isinstance(v, dict) else str(v)).lower()
            if val_lower in v_str or v_str in val_lower:
                return k
        return None

    def _load_preset_defaults(preset_name):
        try:
            _pdata = load_preset(preset_name)
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

    # 프리셋 변경 또는 첫 로드(Cloud 호환) 시 default 로드
    _prev_selected = st.session_state.get("preset_selected", "")
    if selected_preset != _prev_selected:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""
        _load_preset_defaults(selected_preset)"""

NEW_LOAD_BLOCK = """    # 프리셋 변경 감지 → session_state 초기화 + rerun
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

assert OLD_LOAD_BLOCK in text, "교체 대상 블록을 찾을 수 없어요."
text = text.replace(OLD_LOAD_BLOCK, NEW_LOAD_BLOCK, 1)
print("✅ 로드 블록 교체 완료 (st.rerun() 추가)")

# ─────────────────────────────────────────────────────────
# 2. selectbox에서 index= + _preset_idx 제거 → key= 단독으로
#    session_state가 rerun 후 자동 반영됨
# ─────────────────────────────────────────────────────────

OLD_SELECTBOXES = """    def _preset_idx(options, ss_key):
        val = st.session_state.get(ss_key, NONE)
        return options.index(val) if val in options else 0

    col1, col2, col3 = st.columns(3)
    with col1:
        _opts = [NONE] + list(MODEL_APPEARANCE.keys())
        preset_appearance  = st.selectbox("👩 인종/국적",       _opts, index=_preset_idx(_opts, "preset_appearance"),  key="preset_appearance")
        _opts = [NONE] + list(AGE_APPEARANCE.keys())
        preset_age         = st.selectbox("🎂 연령대",          _opts, index=_preset_idx(_opts, "preset_age"),         key="preset_age")
        _opts = [NONE] + list(MODEL_TYPES.keys())
        preset_body        = st.selectbox("👤 체형",            _opts, index=_preset_idx(_opts, "preset_body"),        key="preset_body")
        _opts = [NONE] + list(OUTFIT_TYPES.keys())
        preset_outfit      = st.selectbox("👗 의상",            _opts, index=_preset_idx(_opts, "preset_outfit"),      key="preset_outfit")
        _opts = [NONE] + list(MATERIALS.keys())
        preset_material    = st.selectbox("🧵 소재",            _opts, index=_preset_idx(_opts, "preset_material"),    key="preset_material")
        _opts = [NONE] + list(FOOTWEAR.keys())
        preset_footwear    = st.selectbox("👠 신발",            _opts, index=_preset_idx(_opts, "preset_footwear"),    key="preset_footwear")
        _opts = [NONE] + list(NAILS.keys())
        preset_nails       = st.selectbox("💅 네일",            _opts, index=_preset_idx(_opts, "preset_nails"),       key="preset_nails")
        _opts = [NONE] + list(SKIN_DETAILS.keys())
        preset_skin_detail = st.selectbox("🌿 피부 디테일",     _opts, index=_preset_idx(_opts, "preset_skin_detail"), key="preset_skin_detail")
        _opts = [NONE] + list(BODY_OIL.keys())
        preset_body_oil    = st.selectbox("✨ 바디 오일",        _opts, index=_preset_idx(_opts, "preset_body_oil"),    key="preset_body_oil")
    with col2:
        _opts = [NONE] + list(HAIR_STYLES.keys())
        preset_hair_style  = st.selectbox("💇 헤어스타일",      _opts, index=_preset_idx(_opts, "preset_hair_style"),  key="preset_hair_style")
        _opts = [NONE] + list(POSES.keys())
        preset_pose        = st.selectbox("💃 포즈",            _opts, index=_preset_idx(_opts, "preset_pose"),        key="preset_pose")
        _opts = [NONE] + list(FRAMING.keys())
        preset_framing     = st.selectbox("🖼️ 프레이밍",        _opts, index=_preset_idx(_opts, "preset_framing"),     key="preset_framing")
        _opts = [NONE] + list(CAMERA_ANGLES.keys())
        preset_angle       = st.selectbox("📸 카메라 앵글",     _opts, index=_preset_idx(_opts, "preset_angle"),       key="preset_angle")
        _opts = [NONE] + list(LIGHTING.keys())
        preset_lighting    = st.selectbox("💡 조명",            _opts, index=_preset_idx(_opts, "preset_lighting"),    key="preset_lighting")
        _opts = [NONE] + list(COLOR_GRADES.keys())
        preset_color_grade = st.selectbox("🎨 색감",            _opts, index=_preset_idx(_opts, "preset_color_grade"), key="preset_color_grade")
        _opts = [NONE] + list(STYLES.keys())
        preset_style       = st.selectbox("🎬 스타일",          _opts, index=_preset_idx(_opts, "preset_style"),       key="preset_style")
        _opts = [NONE] + list(COVER_STYLES.keys())
        preset_cover_style = st.selectbox("📰 커버 스타일",     _opts, index=_preset_idx(_opts, "preset_cover_style"), key="preset_cover_style")
    with col3:
        _opts = [NONE] + list(ENVIRONMENTS.keys())
        preset_environment = st.selectbox("🏙️ 환경",            _opts, index=_preset_idx(_opts, "preset_environment"), key="preset_environment")
        _opts = [NONE] + list(WEATHER.keys())
        preset_weather     = st.selectbox("🌦️ 날씨",            _opts, index=_preset_idx(_opts, "preset_weather"),     key="preset_weather")
        _opts = [NONE] + list(IMAGE_STYLE.keys())
        preset_image_style = st.selectbox("📐 이미지 스타일",   _opts, index=_preset_idx(_opts, "preset_image_style"), key="preset_image_style")
        _opts = [NONE] + list(SPECIAL_EFFECTS.keys())
        preset_special_fx  = st.selectbox("🌈 특수 효과",       _opts, index=_preset_idx(_opts, "preset_special_fx"),  key="preset_special_fx")
        _opts = [NONE] + list(MOOD.keys())
        preset_mood        = st.selectbox("🎭 무드",            _opts, index=_preset_idx(_opts, "preset_mood"),        key="preset_mood")"""

NEW_SELECTBOXES = """    col1, col2, col3 = st.columns(3)
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

assert OLD_SELECTBOXES in text, "selectbox 블록을 찾을 수 없어요."
text = text.replace(OLD_SELECTBOXES, NEW_SELECTBOXES, 1)
print("✅ selectbox index= 제거 완료 (key= 단독, rerun 후 자동 반영)")

DASHBOARD.write_text(text, encoding="utf-8")
print("✅ dashboard.py 저장 완료")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")
assert "st.rerun()" in verify,          "❌ st.rerun() 없음"
assert "_preset_idx" not in verify,     "❌ _preset_idx 잔존"
assert OLD_SELECTBOXES not in verify,   "❌ 구버전 selectbox 잔존"
assert OLD_LOAD_BLOCK not in verify,    "❌ 구버전 로드 블록 잔존"
print("✅ 검증 통과")
print("\n🎉 완료! git add dashboard.py; git commit; git push 후 Cloud reboot")
