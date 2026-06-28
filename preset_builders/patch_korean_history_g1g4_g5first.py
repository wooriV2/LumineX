"""
patch_korean_history_g1g4_g5first.py
한국 역사&궁중 글래머 G1~G4 + G5 전반부 SSS/SS 패치
검증일: 2026-06-28
"""

with open(r"C:\Dev\LumineX\dashboard.py", "r", encoding="utf-8") as f:
    content = f.read()

# ── SSS 추가 앵커 ──
SSS_NEW = '''    # 2026-06-28 한국 역사&궁중 글래머 G1~G4 + G5전반부 SSS
    # G1 삼국/고대 — SSS 5종
    "silla_queen_gold", "baekje_lotus_queen", "gojoseon_shaman_queen",
    "gaya_iron_goddess", "ancient_mural_goddess",
    # G2 고려 궁중 — SSS 7종
    "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess",
    "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",
    "mongol_goryeo_queen",
    # G3 조선 왕실/궁중 — SSS 11종
    "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex",
    "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",
    "damo_warrior", "joseon_night_queen", "joseon_concubine_red",
    "changdeok_moonlight", "gyeongbokgung_geisha",
    # G4 기생/예인 — SSS 10종
    "gisaeng_joseon_sheer", "gisaeng_red_lantern", "gisaeng_sword_dance",
    "gisaeng_rain_dance", "gisaeng_black_silk", "wonhyang_legend",
    "hwang_jini_glam", "gisaeng_fan_dance", "gisaeng_pipa_night",
    "pyongyang_gisaeng",
    # G5 신화&정령 전반부 — SSS 6종
    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
'''

ANCHOR = '    # 2026-06-26 에로틱&페티쉬 G3~G12 SSS 51종'
content = content.replace(ANCHOR, SSS_NEW + '\n' + ANCHOR)

with open(r"C:\Dev\LumineX\dashboard.py", "w", encoding="utf-8") as f:
    f.write(content)

print("패치 완료")
