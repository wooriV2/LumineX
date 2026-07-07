# -*- coding: utf-8 -*-
"""
dashboard.py 버그 수정 — Streamlit Cloud preset default 미표시
원인: session_state.preset_selected 미존재 시 _find_key 미실행
수정: 선택된 프리셋이 바뀌었거나 preset_loaded 플래그 없을 때 항상 로드

실행: python preset_builders\patch_preset_default_cloud.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────
# 기존 코드 (버그2 패치로 삽입된 버전)
# ─────────────────────────────────────────────────────────
OLD = """    if selected_preset != st.session_state.preset_selected:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""
        # 프리셋 JSON 값을 selectbox default로 로드
        try:
            _pdata = load_preset(selected_preset)
            # 역방향 매핑 헬퍼: 값(value)으로 키(label) 찾기
            def _find_key(d, val):
                if not val:
                    return None
                val_lower = str(val).lower()
                for k, v in d.items():
                    v_str = (v.get("gemini", "") if isinstance(v, dict) else str(v)).lower()
                    if val_lower in v_str or v_str in val_lower:
                        return k
                return None
            # 각 필드 매핑
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
            pass  # JSON 없는 프리셋은 기본값 유지"""

# ─────────────────────────────────────────────────────────
# 수정 코드 — preset_selected 변경 OR 첫 로드 시 항상 실행
# ─────────────────────────────────────────────────────────
NEW = """    def _find_key(d, val):
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

assert OLD in text, "교체 대상 코드를 찾을 수 없어요. 이미 패치됐거나 코드가 다릅니다."

text = text.replace(OLD, NEW, 1)
DASHBOARD.write_text(text, encoding="utf-8")
print("✅ preset default 로드 로직 수정 완료 (Streamlit Cloud 호환)")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")
assert "_load_preset_defaults" in verify, "❌ 함수 삽입 실패"
assert "_prev_selected" in verify,        "❌ 첫 로드 조건 삽입 실패"
assert OLD not in verify,                 "❌ 구버전 코드 잔존"
print("✅ 검증 통과")
print("\n🎉 완료! git push 후 Streamlit Cloud reboot 하세요.")
