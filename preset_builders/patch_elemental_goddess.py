import re

filepath = r"C:\Dev\LumineX\dashboard.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── SSS_TIER 추가 ───
SSS_NEW = '''
    # 2026-06-18 엘리멘탈 갓데스 카테고리 SSS 확정
    # G1 물/습기
    "uyuni_wet_silk",        # SS→SSS 승급 (용암색 의상+우유니 소금사막 완전 합일)
    "maldives_underwater",
    "bioluminescent_bay",
    "rainbow_falls_goddess",
    # G2 극한 자연 (전종 SSS)
    "trolltunga_edge",
    "zhangjiajie_cloud",
    "cliff_wind_sheer",
    "skydive_editorial",
    "hot_air_balloon_glam",
    "wave_barrel_goddess",
    "glacier_melt_goddess",
    # G3 사막/열기
    "sahara_mirage",
    "salt_flat_body",
    "salar_atacama_flamingo",
    "pamukkale_goddess",
    "red_canyon_goddess",
    # G4 화산/불/태양
    "lava_field_latex",      # SS→SSS 승급
    "solar_flare_goddess",
    # G5 빙하/오로라/우주
    "aurora_bare",           # SS→SSS 승급
    "antarctica_ice_glam",
    "meteor_shower_glam",
    "ice_cave_blue",
    # G6 이국/정글/생물발광
    "antelope_light_sheer",  # SS→SSS 승급
    "waitomo_glow_body",
    "coral_reef_sheer",
    "black_sea_midnight",'''

# SSS_TIER 블록 끝 찾아서 추가
anchor = '    "santorini_sunset",\n    "cappadocia_balloons",\n}'
replacement = '    "santorini_sunset",\n    "cappadocia_balloons",' + SSS_NEW + '\n}'

if anchor in content:
    content = content.replace(anchor, replacement)
    print("SSS_TIER 추가 완료")
else:
    print("SSS_TIER anchor 못 찾음")

# ─── SS_TIER 추가 ───
SS_NEW = '''
    # 2026-06-18 엘리멘탈 갓데스 카테고리 SS 확정
    # SSS도 SS에 포함
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
    "socotra_alien_glam", "deep_jungle_goddess", "monsoon_goddess",'''

anchor2 = '    "cappadocia_balloons",\n    "chefchaouen_blue",'
replacement2 = '    "cappadocia_balloons",\n    "chefchaouen_blue",' + SS_NEW

if anchor2 in content:
    content = content.replace(anchor2, replacement2)
    print("SS_TIER 추가 완료")
else:
    print("SS_TIER anchor 못 찾음")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("패치 완료")
