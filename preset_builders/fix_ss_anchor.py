"""
patch: SS anchor 수정본
저장위치: C:\Dev\LumineX\preset_builders\fix_ss_anchor.py
실행: cd C:\Dev\LumineX && python preset_builders/fix_ss_anchor.py
"""

filepath = "dashboard.py"

with open(filepath, encoding="utf-8") as f:
    content = f.read()

SS_NEW = """    # 2026-06-18 엘리멘탈 갓데스 SS 확정 (SSS 포함)
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
    "socotra_alien_glam", "deep_jungle_goddess", "monsoon_goddess",
    # 2026-06-18 엘리멘탈 갓데스 카테고리 SSS 확정"""

a2 = '    "cappadocia_balloons",\n    # 2026-06-18 엘리멘탈 갓데스 카테고리 SSS 확정'
r2 = '    "cappadocia_balloons",\n' + SS_NEW

c2 = content.replace(a2, r2)
print("SS OK" if c2 != content else "SS FAIL")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c2)

print("패치 완료")
