"""
패치: dashboard.py에 location v02 프리셋 카테고리 등록
실행: python preset_builders/patch_dashboard_location_v02.py
"""
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")
content = DASHBOARD.read_text(encoding="utf-8")

# 🏛️ 유적&문명에 v02 추가
OLD = '''        "petra_rose","angkor_dawn","tikal_skyrise","bagan_balloon",
        "ellora_rock_temple","derinkuyu_underground","tigers_nest_cliff","naoshima_art_island",
    ],'''

NEW = '''        "petra_rose","angkor_dawn","tikal_skyrise","bagan_balloon",
        "ellora_rock_temple","derinkuyu_underground","tigers_nest_cliff","naoshima_art_island",
        # v26
        "machu_picchu_cloud","chichen_itza_pyramid","colosseum_dusk","alhambra_palace",
        "borobudur_dawn","karnak_temple","mont_saint_michel","sigiriya_rock",
        "angkor_thom_faces","teotihuacan_pyramid","gobekli_tepe","palmyra_colonnade",
    ],'''

content = content.replace(OLD, NEW, 1)

# 🌿 자연에 v02 추가
OLD2 = '''        # v25 — 개방형 자연 배경
        "son_doong_jungle","waitomo_glow","dead_vlei_ghost","danxia_rainbow",
        "cenote_sacred","socotra_alien","lake_natron","namib_star_desert",
    ],'''

NEW2 = '''        # v25 — 개방형 자연 배경
        "son_doong_jungle","waitomo_glow","dead_vlei_ghost","danxia_rainbow",
        "cenote_sacred","socotra_alien","lake_natron","namib_star_desert",
        # v26
        "zhangjiajie_avatar","pamukkale_white","plitvice_cascade","frozen_baikal",
        "rainbow_mountain","wisteria_tunnel","torres_del_paine","ha_long_bay",
        "kelimutu_crater","victoria_falls","fairy_pools","tunnel_of_love","chocolate_hills",
    ],'''

content = content.replace(OLD2, NEW2, 1)

# 🌃 도시에 v02 추가
OLD3 = '''        # v25 — 개방형 건축/도시 배경
        "sheikh_zayed_dawn","livraria_lello_staircase","palacio_de_sal",
    ],'''

NEW3 = '''        # v25 — 개방형 건축/도시 배경
        "sheikh_zayed_dawn","livraria_lello_staircase","palacio_de_sal",
        # v26
        "santorini_sunset","cappadocia_balloons","chefchaouen_blue","hallstatt_lake",
        "shirakawa_snow","positano_cliff","bruges_canal","cinque_terre_harbor",
    ],'''

content = content.replace(OLD3, NEW3, 1)

DASHBOARD.write_text(content, encoding="utf-8")
print("✅ dashboard.py v02 카테고리 등록 완료!")
print()
print("추가 내용:")
print("  🏛️ 유적&문명 +12개 (마추픽추, 치첸이사, 콜로세움 등)")
print("  🌿 자연 +13개 (장가계, 파묵칼레, 플리트비체 등)")
print("  🌃 도시 +8개 (산토리니, 카파도키아, 쉐프샤우엔 등)")
print("  총 +33개")
