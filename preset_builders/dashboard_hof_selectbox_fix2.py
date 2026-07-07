"""
dashboard_hof_selectbox_fix.py
HOF 랜덤 버튼 → selectbox index 연동 수정
"""
from pathlib import Path

TARGET = Path("C:/Dev/LumineX/dashboard.py")
content = TARGET.read_text(encoding="utf-8")

# ── selectbox에 index 파라미터 추가 ──
OLD = '''        if filtered_presets:
            selected_preset = st.selectbox(
                f"🎨 프리셋 선택 ({len(filtered_presets)}개)",
                options=filtered_presets,
                format_func=format_preset
            )'''

NEW = '''        if filtered_presets:
            # HOF 랜덤 버튼으로 세팅된 프리셋이 있으면 해당 index로 이동
            _hof_target = st.session_state.get("preset_selected", "")
            _preset_index = 0
            if _hof_target and _hof_target in filtered_presets:
                _preset_index = filtered_presets.index(_hof_target)
            selected_preset = st.selectbox(
                f"🎨 프리셋 선택 ({len(filtered_presets)}개)",
                options=filtered_presets,
                index=_preset_index,
                format_func=format_preset
            )'''

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    print("✅ [1/2] selectbox index 연동 완료")
else:
    print("❌ [1/2] selectbox 블록을 찾지 못했습니다")

# ── 티어 필터도 HOF 랜덤 시 자동으로 HOF로 세팅 ──
OLD_BTN = '''        st.session_state.preset_selected  = _hof_pick
        st.session_state.preset_prompt    = ""
        # 빠른 생성 자동 트리거 플래그
        st.session_state._hof_quick_fire  = True
        st.rerun()'''

NEW_BTN = '''        st.session_state.preset_selected  = _hof_pick
        st.session_state.preset_prompt    = ""
        # 티어 필터를 HOF로 세팅 → filtered_presets에 HOF 프리셋 포함되도록
        st.session_state["preset_tier_filter"] = "👑 HOF"
        # 카테고리 필터 전체로 세팅 → HOF 프리셋이 어느 카테고리든 포함
        st.session_state["preset_cat_filter"]  = "🌟 전체"
        # 빠른 생성 자동 트리거 플래그
        st.session_state._hof_quick_fire  = True
        st.rerun()'''

if OLD_BTN in content:
    content = content.replace(OLD_BTN, NEW_BTN, 1)
    print("✅ [2/2] HOF 티어/카테고리 필터 자동 세팅 완료")
elif "preset_tier_filter" in content and "👑 HOF" in content:
    print("⏭️  [2/2] 이미 적용됨 — 건너뜀")
else:
    print("❌ [2/2] HOF 버튼 블록을 찾지 못했습니다")

TARGET.write_text(content, encoding="utf-8")
print("\n🎉 수정 완료! streamlit run dashboard.py 로 확인하세요.")
print("   HOF 랜덤 → 티어필터 자동 HOF + 해당 프리셋 자동 선택")
