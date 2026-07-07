# -*- coding: utf-8 -*-
"""
dashboard.py 패치 — preset selectbox index= 파라미터 추가
Streamlit Cloud에서 preset default 값이 표시되지 않는 문제 수정

원인: session_state에 값을 넣어도 index= 없으면 selectbox가 무시함
수정: 각 selectbox에 index= st.session_state.get(key, NONE) 추가

실행: python preset_builders\patch_preset_selectbox_index.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────
# 교체 대상: preset 탭의 selectbox 20개
# 패턴: st.selectbox("...", [NONE] + list(DICT.keys()), key="preset_KEY")
# 수정: index= 파라미터 추가
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

NEW_SELECTBOXES = """    def _preset_idx(options, ss_key):
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

assert OLD_SELECTBOXES in text, "교체 대상 selectbox 블록을 찾을 수 없어요."
text = text.replace(OLD_SELECTBOXES, NEW_SELECTBOXES, 1)

DASHBOARD.write_text(text, encoding="utf-8")
print("✅ preset selectbox index= 파라미터 추가 완료 (23개)")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")
assert "_preset_idx" in verify,       "❌ _preset_idx 함수 없음"
assert OLD_SELECTBOXES not in verify, "❌ 구버전 코드 잔존"
count = verify.count("_preset_idx(")
print(f"✅ _preset_idx 호출 {count}개 확인")
print("\n🎉 완료! git add dashboard.py; git commit; git push 후 Cloud reboot")
