# -*- coding: utf-8 -*-
"""
dashboard.py 완전 재작성 패치
문제1: _pd 로드가 selectbox 아래에 있음
문제2: st.markdown("---") 가 with tab3: 밖에 있어서 탭 오염
문제3: st.markdown footer 중복

실행: python preset_builders\patch_dashboard_clean.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────
# 문제2+3 수정: tab3 닫힌 후 떠있는 st.markdown("---") 제거
# + footer 중복 제거
# ─────────────────────────────────────────────────────────

OLD_STRAY = """        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

st.markdown("---")

# ══════════════════════════════════════════════════════════
# 탭 5: 히스토리 & HOF 배치 생성"""

NEW_STRAY = """        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

# ══════════════════════════════════════════════════════════
# 탭 5: 히스토리 & HOF 배치 생성"""

assert OLD_STRAY in text, "tab3 뒤 stray markdown을 찾을 수 없어요."
text = text.replace(OLD_STRAY, NEW_STRAY, 1)
print("✅ tab3 뒤 stray st.markdown('---') 제거")

# footer 중복 제거
OLD_DOUBLE_FOOTER = """st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v4.4 — AI Fashion Image Engine</div>', unsafe_allow_html=True)


st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v4.4 — AI Fashion Image Engine</div>', unsafe_allow_html=True)"""

NEW_SINGLE_FOOTER = """st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v4.4 — AI Fashion Image Engine</div>', unsafe_allow_html=True)"""

assert OLD_DOUBLE_FOOTER in text, "footer 중복을 찾을 수 없어요."
text = text.replace(OLD_DOUBLE_FOOTER, NEW_SINGLE_FOOTER, 1)
print("✅ footer 중복 제거")

# ─────────────────────────────────────────────────────────
# 문제1 수정: NONE 정의 + _pd 로드를 selectbox 앞으로 이동
# 현재: NONE 정의 → col1,col2,col3 → selectbox(_pd 사용) → _pd 로드
# 수정: NONE 정의 → _pd 로드 → col1,col2,col3 → selectbox
# ─────────────────────────────────────────────────────────

OLD_ORDER = """    NONE = "None — 프리셋 기본값 사용"
    col1, col2, col3 = st.columns(3)
    with col1:
        _o = [NONE] + list(MODEL_APPEARANCE.keys())
        preset_appearance  = st.selectbox("👩 인종/국적",       _o, index=_pidx(_o, _pval(MODEL_APPEARANCE, _pd.get("appearance",  ""), NONE)))"""

NEW_ORDER = """    NONE = "None — 프리셋 기본값 사용"

    # _pd: 매 렌더링마다 선택된 프리셋 JSON 로드 (selectbox index 계산용)
    try:
        _pd = load_preset(selected_preset)
    except Exception:
        _pd = {}

    col1, col2, col3 = st.columns(3)
    with col1:
        _o = [NONE] + list(MODEL_APPEARANCE.keys())
        preset_appearance  = st.selectbox("👩 인종/국적",       _o, index=_pidx(_o, _pval(MODEL_APPEARANCE, _pd.get("appearance",  ""), NONE)))"""

assert OLD_ORDER in text, "NONE 정의 + col1 시작 블록을 찾을 수 없어요."
text = text.replace(OLD_ORDER, NEW_ORDER, 1)
print("✅ _pd 로드를 selectbox 앞으로 이동")

# ─────────────────────────────────────────────────────────
# 기존 _pd 로드 코드 제거 (중복 방지)
# ─────────────────────────────────────────────────────────

OLD_PD_AFTER = """    # 매 렌더링마다 JSON 읽어서 default 계산
    try:
        _pd = load_preset(selected_preset)
    except Exception:
        _pd = {}"""

NEW_PD_AFTER = ""  # 제거

assert OLD_PD_AFTER in text, "기존 _pd 로드 코드를 찾을 수 없어요."
text = text.replace(OLD_PD_AFTER, NEW_PD_AFTER, 1)
print("✅ 기존 _pd 로드 중복 코드 제거")

# ─────────────────────────────────────────────────────────
# 저장 + 검증
# ─────────────────────────────────────────────────────────
DASHBOARD.write_text(text, encoding="utf-8")
print("✅ dashboard.py 저장 완료")

verify = DASHBOARD.read_text(encoding="utf-8")

# _pd 위치가 selectbox보다 앞인지 확인
pd_pos        = verify.index("_pd = load_preset(selected_preset)")
selectbox_pos = verify.index('_o = [NONE] + list(MODEL_APPEARANCE.keys())')
assert pd_pos < selectbox_pos, f"❌ _pd({pd_pos}) 가 selectbox({selectbox_pos}) 보다 뒤에 있음"
print(f"✅ _pd 위치 확인: {pd_pos} < {selectbox_pos}")

# stray markdown 없음
assert 'st.markdown("---")\n\n# ══' not in verify, "❌ stray markdown 잔존"
print("✅ stray markdown 없음")

# footer 중복 없음
assert verify.count("✦ LumineX v4.4 — AI Fashion Image Engine") == 1, "❌ footer 중복 잔존"
print("✅ footer 중복 없음")

print("\n🎉 완료! git add dashboard.py; git commit; git push 후 Cloud reboot")
