"""
패치: dashboard.py에 SSS/SS tier 필터 추가
실행: python preset_builders/patch_tier_filter_v01.py
"""
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")
content = DASHBOARD.read_text(encoding="utf-8")

# 카테고리 필터 + tier 필터 추가
OLD = '''    col_cat, col_search = st.columns([2, 1])
    with col_cat:
        all_cats = ["🌟 전체"] + list(PRESET_CATEGORIES.keys())
        selected_cat = st.selectbox("📂 카테고리 필터", options=all_cats, index=0, key="preset_cat_filter")
    with col_search:
        search_query = st.text_input("🔍 프리셋 검색", placeholder="이름 검색...", key="preset_search")

    all_presets = list_presets()
    if selected_cat == "🌟 전체":
        filtered_presets = all_presets
    else:
        cat_list = PRESET_CATEGORIES.get(selected_cat, [])
        filtered_presets = [p for p in all_presets if p in cat_list]

    if search_query:
        filtered_presets = [p for p in filtered_presets if search_query.lower() in p.lower()]'''

NEW = '''    col_cat, col_tier, col_search = st.columns([2, 1, 1])
    with col_cat:
        all_cats = ["🌟 전체"] + list(PRESET_CATEGORIES.keys())
        selected_cat = st.selectbox("📂 카테고리 필터", options=all_cats, index=0, key="preset_cat_filter")
    with col_tier:
        tier_options = ["전체 티어", "⭐⭐⭐ SSS", "⭐⭐ SS", "• 일반"]
        selected_tier = st.selectbox("🏆 티어 필터", options=tier_options, index=0, key="preset_tier_filter")
    with col_search:
        search_query = st.text_input("🔍 프리셋 검색", placeholder="이름 검색...", key="preset_search")

    all_presets = list_presets()
    if selected_cat == "🌟 전체":
        filtered_presets = all_presets
    else:
        cat_list = PRESET_CATEGORIES.get(selected_cat, [])
        filtered_presets = [p for p in all_presets if p in cat_list]

    # 티어 필터 적용
    if selected_tier == "⭐⭐⭐ SSS":
        filtered_presets = [p for p in filtered_presets if p in SSS_TIER]
    elif selected_tier == "⭐⭐ SS":
        filtered_presets = [p for p in filtered_presets if p in SS_TIER and p not in SSS_TIER]
    elif selected_tier == "• 일반":
        filtered_presets = [p for p in filtered_presets if p not in SS_TIER]

    if search_query:
        filtered_presets = [p for p in filtered_presets if search_query.lower() in p.lower()]'''

content = content.replace(OLD, NEW, 1)

# format_preset에 SSS 표시 추가
OLD2 = '''    def format_preset(name):
        if name in SS_TIER:
            return f"⭐ {name} [SS]"
        return f"• {name}"'''

NEW2 = '''    def format_preset(name):
        if name in SSS_TIER:
            return f"🌟 {name} [SSS]"
        if name in SS_TIER:
            return f"⭐ {name} [SS]"
        return f"• {name}"'''

content = content.replace(OLD2, NEW2, 1)

# 카테고리 현황 카드에 SSS 카운트 추가
OLD3 = '''            ss_count = sum(1 for p in filtered_presets if p in SS_TIER)
            st.markdown(f"""
<div style="background:{BG_CARD};border:1px solid {BORDER};border-radius:8px;padding:10px 14px;margin-top:28px;">
  <div style="font-size:0.65rem;color:{TEXT_DIM};letter-spacing:1px;">카테고리 현황</div>
  <div style="font-size:1.1rem;font-weight:700;color:{GOLD};margin-top:4px;">{len(filtered_presets)}개</div>
  <div style="font-size:0.7rem;color:{TEXT_DIM};">⭐ SS tier {ss_count}개</div>
</div>
''', unsafe_allow_html=True)'''

NEW3 = '''            ss_count = sum(1 for p in filtered_presets if p in SS_TIER and p not in SSS_TIER)
            sss_count = sum(1 for p in filtered_presets if p in SSS_TIER)
            st.markdown(f"""
<div style="background:{BG_CARD};border:1px solid {BORDER};border-radius:8px;padding:10px 14px;margin-top:28px;">
  <div style="font-size:0.65rem;color:{TEXT_DIM};letter-spacing:1px;">카테고리 현황</div>
  <div style="font-size:1.1rem;font-weight:700;color:{GOLD};margin-top:4px;">{len(filtered_presets)}개</div>
  <div style="font-size:0.7rem;color:#f0c040;">🌟 SSS tier {sss_count}개</div>
  <div style="font-size:0.7rem;color:{TEXT_DIM};">⭐ SS tier {ss_count}개</div>
</div>
''', unsafe_allow_html=True)'''

content = content.replace(OLD3, NEW3, 1)

DASHBOARD.write_text(content, encoding="utf-8")
print("✅ tier 필터 패치 완료!")
print()
print("변경 내용:")
print("  1. 카테고리 필터 옆에 티어 필터 추가 (SSS/SS/일반/전체)")
print("  2. 프리셋 목록에 SSS는 🌟 표시")
print("  3. 카테고리 현황 카드에 SSS 카운트 추가")
