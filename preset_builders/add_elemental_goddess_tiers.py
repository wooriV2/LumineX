"""
patch: 엘리멘탈 갓데스 카테고리 티어 확정
저장위치: C:\Dev\LumineX\preset_builders\add_elemental_goddess_tiers.py
실행: cd C:\Dev\LumineX && python preset_builders/add_elemental_goddess_tiers.py
"""

filepath = "dashboard.py"

with open(filepath, encoding="utf-8") as f:
    content = f.read()

# ── SSS 추가 ──
SSS_NEW = """
    # 2026-06-18 엘리멘탈 갓데스 SSS 확정
    # G1 물/습기
    "uyuni_wet_silk", "maldives_underwater", "bioluminescent_bay", "rainbow_falls_goddess",
    # G2 극한 자연 (전종 SSS)
    "trolltunga_edge", "zhangjiajie_cloud", "cliff_wind_sheer", "skydive_editorial",
    "hot_air_balloon_glam", "wave_barrel_goddess", "glacier_melt_goddess",
    # G3 사막/열기
    "sahara_mirage", "salt_flat_body", "salar_atacama_flamingo", "pamukkale_goddess", "red_canyon_goddess",
    # G4 화산/불/태양
    "lava_field_latex", "solar_flare_goddess",
    # G5 빙하/오로라/우주
    "aurora_bare", "antarctica_ice_glam", "meteor_shower_glam", "ice_cave_blue",
    # G6 이국/정글/생물발광
    "antelope_light_sheer", "waitomo_glow_body", "coral_reef_sheer", "black_sea_midnight","""

a1 = '    "santorini_sunset",\n    "cappadocia_balloons",\n}'
r1 = '    "santorini_sunset",\n    "cappadocia_balloons",' + SSS_NEW + '\n}'

c2 = content.replace(a1, r1)
print("SSS OK" if c2 != content else "SSS FAIL — anchor 못 찾음")

# ── SS 추가 ──
SS_NEW = """
    # 2026-06-18 엘리멘탈 갓데스 SS 확정 (SSS 포함)
    "uyuni_wet_silk", "maldives_underwater", "bioluminescent_bay", "rainbow_falls_goddess",
    "trolltunga_edge", "zhangjiajie_cloud", "cliff_wind_sheer", "skydive_editorial",
    "hot_air_balloon_glam", "wave_barrel_goddess", "glacier_melt_goddess",
    "sahara_mirage", "salt_flat_body", "salar_atacama_flamingo", "pamukkale_goddess", "red_canyon_goddess",
    "lava_field_latex", "solar_flare_goddess",
    "aurora_bare", "antarctica_ice_glam", "meteor_shower_glam", "ice_cave_blue",
    "antelope_light_sheer", "waitomo_glow_body", "coral_reef_sheer", "black_sea_midnight",
    # SS 전용
    "niagara_wet_editorial", "thunderstorm_wet", "cave_waterfall_goddess",
    "desert_heat_body",
    "volcano_edge_glam", "bonfire_editorial", "eruption_silhouette", "amazon_river_goddess",
    "iceland_hot_spring", "northern_lights_body", "dead_sea_goddess",
    "socotra_alien_glam", "deep_jungle_goddess", "monsoon_goddess","""

a2 = '    "cappadocia_balloons",\n    "chefchaouen_blue",'
r2 = '    "cappadocia_balloons",' + SS_NEW + '\n    "chefchaouen_blue",'

c3 = c2.replace(a2, r2)
print("SS OK" if c3 != c2 else "SS FAIL — anchor 못 찾음")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c3)

print("패치 완료")
