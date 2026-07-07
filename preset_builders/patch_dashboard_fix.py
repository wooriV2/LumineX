# -*- coding: utf-8 -*-
"""
dashboard.py 버그 수정 패치
버그1: tab4/tab5 순서 교체 (탭 렌더링 오류)
버그2: 프리셋 선택 시 JSON 값으로 selectbox default 채우기

실행: python preset_builders\patch_dashboard_fix.py
위치: C:\Dev\LumineX\ 에서 실행
"""

import re
from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py를 찾을 수 없어요. 프로젝트 루트에서 실행하세요."

text = DASHBOARD.read_text(encoding="utf-8")
original = text

# ─────────────────────────────────────────────────────────
# 버그1 FIX: tab4/tab5 블록 순서 교체
# 현재: tab5(히스토리) → tab4(영상) 순서로 정의됨
# 수정: tab4(영상) → tab5(히스토리) 순서로 교체
# ─────────────────────────────────────────────────────────

# tab5 블록 시작 마커
TAB5_HEADER = "# ══════════════════════════════════════════════════════════\n# 탭 5: 히스토리 & HOF 배치 생성\n# ══════════════════════════════════════════════════════════\nwith tab5:"

# tab4 블록 시작 마커
TAB4_HEADER = "# ══════════════════════════════════════════════════════════\n# 탭 4: 영상 프롬프트\n# ══════════════════════════════════════════════════════════\nwith tab4:"

# footer (두 탭 뒤에 오는 공통 footer)
FOOTER_MARKER = "\nst.markdown('<div style=\"text-align:center"

assert TAB5_HEADER in text, "tab5 헤더를 찾을 수 없어요."
assert TAB4_HEADER in text, "tab4 헤더를 찾을 수 없어요."
assert FOOTER_MARKER in text, "footer를 찾을 수 없어요."

# tab5 블록 추출
tab5_start = text.index(TAB5_HEADER)
tab4_start = text.index(TAB4_HEADER)
footer_start = text.index(FOOTER_MARKER)

tab5_block = text[tab5_start:tab4_start]
tab4_block = text[tab4_start:footer_start]
footer_block = text[footer_start:]
before_tabs = text[:tab5_start]

# 순서 교체: tab4 먼저, tab5 나중
text = before_tabs + tab4_block + tab5_block + footer_block

print("✅ 버그1 FIX: tab4/tab5 순서 교체 완료")

# ─────────────────────────────────────────────────────────
# 버그2 FIX: 프리셋 선택 시 JSON 필드 값으로 selectbox default 채우기
#
# 현재: selected_preset이 바뀌면 preset_prompt만 초기화
# 수정: load_preset()으로 JSON 읽어서 session_state에 매핑값 저장
#       → 각 selectbox가 해당 값을 default로 표시
# ─────────────────────────────────────────────────────────

OLD_PRESET_CHANGE = """    if selected_preset != st.session_state.preset_selected:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""
"""

NEW_PRESET_CHANGE = """    if selected_preset != st.session_state.preset_selected:
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
            pass  # JSON 없는 프리셋은 기본값 유지
"""

assert OLD_PRESET_CHANGE in text, "preset 변경 감지 코드를 찾을 수 없어요."
text = text.replace(OLD_PRESET_CHANGE, NEW_PRESET_CHANGE, 1)
print("✅ 버그2 FIX: 프리셋 선택 시 JSON default 로드 코드 삽입 완료")

# ─────────────────────────────────────────────────────────
# 저장
# ─────────────────────────────────────────────────────────
if text == original:
    print("⚠️  변경사항 없음 — 이미 패치 적용됐거나 코드가 다릅니다.")
else:
    DASHBOARD.write_text(text, encoding="utf-8")
    print(f"✅ dashboard.py 저장 완료")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")

# 탭 순서 검증
tab4_pos = verify.index("with tab4:")
tab5_pos = verify.index("with tab5:")
assert tab4_pos < tab5_pos, "❌ tab 순서 여전히 잘못됨"
print(f"✅ 검증: tab4({tab4_pos}) < tab5({tab5_pos}) — 순서 정상")

# 버그2 검증
assert "_find_key" in verify, "❌ 버그2 패치 코드 없음"
print("✅ 검증: preset default 로드 코드 존재 확인")

print("\n🎉 패치 완료! streamlit run dashboard.py 로 재시작하세요.")
