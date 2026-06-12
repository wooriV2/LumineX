"""
패치: dashboard.py에 SSS/SS tier 필터 추가 (v02 - syntax fix)
실행: python preset_builders/patch_tier_filter_v02.py
"""
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")
content = DASHBOARD.read_text(encoding="utf-8")

# 1. 카테고리 필터 + tier 필터 추가
OLD1 = "    col_cat, col_search = st.columns([2, 1])"
NEW1 = "    col_cat, col_tier, col_search = st.columns([2, 1, 1])"
content = content.replace(OLD1, NEW1, 1)

OLD2 = '        selected_cat = st.selectbox("📂 카테고리 필터", options=all_cats, index=0, key="preset_cat_filter")\n    with col_search:'
NEW2 = '        selected_cat = st.selectbox("📂 카테고리 필터", options=all_cats, index=0, key="preset_cat_filter")\n    with col_tier:\n        tier_options = ["전체 티어", "⭐⭐⭐ SSS", "⭐⭐ SS", "• 일반"]\n        selected_tier = st.selectbox("🏆 티어 필터", options=tier_options, index=0, key="preset_tier_filter")\n    with col_search:'
content = content.replace(OLD2, NEW2, 1)

# 2. 티어 필터 로직 추가 (search_query 바로 위에 삽입)
OLD3 = "    if search_query:\n        filtered_presets = [p for p in filtered_presets if search_query.lower() in p.lower()]"
NEW3 = (
    "    # 티어 필터 적용\n"
    '    if selected_tier == "⭐⭐⭐ SSS":\n'
    "        filtered_presets = [p for p in filtered_presets if p in SSS_TIER]\n"
    '    elif selected_tier == "⭐⭐ SS":\n'
    "        filtered_presets = [p for p in filtered_presets if p in SS_TIER and p not in SSS_TIER]\n"
    '    elif selected_tier == "• 일반":\n'
    "        filtered_presets = [p for p in filtered_presets if p not in SS_TIER]\n"
    "\n"
    "    if search_query:\n"
    "        filtered_presets = [p for p in filtered_presets if search_query.lower() in p.lower()]"
)
content = content.replace(OLD3, NEW3, 1)

# 3. format_preset에 SSS 🌟 표시 추가
OLD4 = (
    "    def format_preset(name):\n"
    "        if name in SS_TIER:\n"
    '            return f"⭐ {name} [SS]"\n'
    '        return f"• {name}"'
)
NEW4 = (
    "    def format_preset(name):\n"
    "        if name in SSS_TIER:\n"
    '            return f"🌟 {name} [SSS]"\n'
    "        if name in SS_TIER:\n"
    '            return f"⭐ {name} [SS]"\n'
    '        return f"• {name}"'
)
content = content.replace(OLD4, NEW4, 1)

# 4. 카테고리 현황 카드 SSS 카운트 추가
OLD5 = "            ss_count = sum(1 for p in filtered_presets if p in SS_TIER)"
NEW5 = (
    "            ss_count = sum(1 for p in filtered_presets if p in SS_TIER and p not in SSS_TIER)\n"
    "            sss_count = sum(1 for p in filtered_presets if p in SSS_TIER)"
)
content = content.replace(OLD5, NEW5, 1)

OLD6 = '  <div style="font-size:0.7rem;color:{TEXT_DIM};">⭐ SS tier {ss_count}개</div>'
NEW6 = (
    '  <div style="font-size:0.7rem;color:#f0c040;">🌟 SSS tier {sss_count}개</div>\n'
    '  <div style="font-size:0.7rem;color:{TEXT_DIM};">⭐ SS tier {ss_count}개</div>'
)
content = content.replace(OLD6, NEW6, 1)

DASHBOARD.write_text(content, encoding="utf-8")
print("✅ tier 필터 패치 완료! (v02)")
print()
print("변경 내용:")
print("  1. 티어 필터 드롭다운 추가 (SSS/SS/일반/전체)")
print("  2. SSS 프리셋 🌟 표시")
print("  3. 카테고리 현황 카드 SSS 카운트 분리")
