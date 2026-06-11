"""
패치: dashboard.py에 🏛️ 유적&문명 카테고리 추가
실행: python preset_builders/patch_dashboard_heritage_v01.py
"""
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

content = DASHBOARD.read_text(encoding="utf-8")

# ── 1. PRESET_CATEGORIES에 🏛️ 유적&문명 추가 ──────────────────
# "🌋 익스트림 글래머" 블록 직전에 삽입
OLD = '    "🌋 익스트림 글래머": ['

NEW = '''    "🏛️ 유적 & 문명": [
        "petra_rose","angkor_dawn","tikal_skyrise","bagan_balloon",
        "ellora_rock_temple","derinkuyu_underground","tigers_nest_cliff","naoshima_art_island",
    ],

    "🌋 익스트림 글래머": ['''

content = content.replace(OLD, NEW, 1)

# ── 2. 🌿 자연 카테고리에 신규 자연 프리셋 추가 ──────────────────
OLD2 = '''        # v11
        "volcanic_goddess","storm_lightning","deep_cave","tidal_wave",
    ],'''

NEW2 = '''        # v11
        "volcanic_goddess","storm_lightning","deep_cave","tidal_wave",
        # v25 — 개방형 자연 배경
        "son_doong_jungle","waitomo_glow","dead_vlei_ghost","danxia_rainbow",
        "cenote_sacred","socotra_alien","lake_natron","namib_star_desert",
    ],'''

content = content.replace(OLD2, NEW2, 1)

# ── 3. 🌃 도시 카테고리에 신규 도시 프리셋 추가 ──────────────────
OLD3 = '''        # v11
        "tokyo_shibuya","paris_midnight","subway_editorial","penthouse_view",
    ],'''

NEW3 = '''        # v11
        "tokyo_shibuya","paris_midnight","subway_editorial","penthouse_view",
        # v25 — 개방형 건축/도시 배경
        "sheikh_zayed_dawn","livraria_lello_staircase","palacio_de_sal",
    ],'''

content = content.replace(OLD3, NEW3, 1)

# ── 4. 🌌 불가능&초현실에 신규 초현실 프리셋 추가 ──────────────────
OLD4 = '''        "double_exposure_self",
    ],'''

NEW4 = '''        "double_exposure_self",
        # v25 — 개방형 초현실 배경
        "richat_eye","marble_caves_water",
    ],'''

content = content.replace(OLD4, NEW4, 1)

# ── 5. 사이드바 SSS tier 카운트 표시 추가 ──────────────────────
OLD5 = '    st.markdown(f"**SS tier:** `{len(SS_TIER)}개`")'

NEW5 = '''    st.markdown(f"**SSS tier:** `{len(SSS_TIER)}개`")
    st.markdown(f"**SS tier:** `{len(SS_TIER)}개`")'''

content = content.replace(OLD5, NEW5, 1)

# ── 저장 ──────────────────────────────────────────────────────
DASHBOARD.write_text(content, encoding="utf-8")
print("✅ dashboard.py 패치 완료!")
print()
print("변경 내용:")
print("  1. 🏛️ 유적 & 문명 카테고리 신설 (8개)")
print("  2. 🌿 자연에 개방형 배경 8개 추가")
print("  3. 🌃 도시에 개방형 배경 3개 추가")
print("  4. 🌌 불가능&초현실에 개방형 배경 2개 추가")
print("  5. 사이드바 SSS tier 카운트 표시 추가")
