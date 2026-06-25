"""
패치 v2 — 라인 번호 기반 직접 삽입
SSS_TIER 블록 마지막 항목 "jazz_dance_glam" 바로 뒤에 삽입
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

NEW_SSS_BLOCK = '''
    # 2026-06-25 대기&파티클 30종 SSS
    "smoke_machine_club", "dry_ice_floor", "cigarette_smoke_noir",
    "incense_smoke_ritual", "smoke_color_holi", "fog_forest_mystery",
    "gold_dust_pour", "holi_powder_explosion", "chalk_dust_sport",
    "flour_dust_studio", "pigment_powder_art",
    "feather_explosion", "black_feather_dark", "petal_storm_indoor",
    "cherry_blossom_burst", "dried_flower_cascade",
    "glitter_rain_studio", "gold_confetti_burst", "silver_glitter_body",
    "neon_particle_club", "bubble_floating_studio",
    "sparkler_night_glam", "fire_poi_dance", "ember_glow_dark", "firework_silhouette",
    "autumn_leaves_burst", "snow_indoor_studio", "dandelion_blow",
    "firefly_night_field", "seed_pod_floating",
    # 2026-06-25 에로틱&페티쉬 G1 SSS 8종
    "latex_venom", "latex_catsuit", "latex_catsuit_red", "pvc_transparent_full",
    "latex_hood_full", "latex_transparent", "vinyl_goddess", "rubber_goddess",
    # 2026-06-25 에로틱&페티쉬 G2 SSS 7종
    "chrome_vixen", "chain_goddess", "savage_leather", "leather_bodysuit",
    "chrome_bodysuit", "mirror_dress", "liquid_metal_body",
'''

NEW_SS_BLOCK = '''
    # 2026-06-25 대기&파티클 30종 (SS 포함)
    "smoke_machine_club", "dry_ice_floor", "cigarette_smoke_noir",
    "incense_smoke_ritual", "smoke_color_holi", "fog_forest_mystery",
    "gold_dust_pour", "holi_powder_explosion", "chalk_dust_sport",
    "flour_dust_studio", "pigment_powder_art",
    "feather_explosion", "black_feather_dark", "petal_storm_indoor",
    "cherry_blossom_burst", "dried_flower_cascade",
    "glitter_rain_studio", "gold_confetti_burst", "silver_glitter_body",
    "neon_particle_club", "bubble_floating_studio",
    "sparkler_night_glam", "fire_poi_dance", "ember_glow_dark", "firework_silhouette",
    "autumn_leaves_burst", "snow_indoor_studio", "dandelion_blow",
    "firefly_night_field", "seed_pod_floating",
    # 2026-06-25 에로틱&페티쉬 G1 (SS 포함)
    "latex_venom", "latex_catsuit", "latex_catsuit_red", "pvc_transparent_full",
    "latex_hood_full", "latex_transparent", "vinyl_goddess", "rubber_goddess",
    "wet_latex",
    # 2026-06-25 에로틱&페티쉬 G2 (SS 포함)
    "chrome_vixen", "chain_goddess", "savage_leather", "leather_bodysuit",
    "chrome_bodysuit", "mirror_dress", "liquid_metal_body",
'''

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# SSS_TIER 앵커: "jazz_dance_glam", 뒤에 삽입
SSS_ANCHOR = '    "jazz_dance_glam",'
if SSS_ANCHOR not in content:
    print("❌ SSS 앵커 없음")
else:
    content = content.replace(SSS_ANCHOR, SSS_ANCHOR + NEW_SSS_BLOCK, 1)
    print("✅ SSS_TIER 삽입 완료")

# SS_TIER 앵커: "jazz_dance_glam", (SS_TIER 블록 내) 뒤에 삽입
# SS_TIER에서 jazz_dance_glam은 두 번째 등장
idx1 = content.find(SSS_ANCHOR)
idx2 = content.find(SSS_ANCHOR, idx1 + 1)
if idx2 == -1:
    print("❌ SS 앵커 없음")
else:
    content = content[:idx2] + content[idx2:].replace(SSS_ANCHOR, SSS_ANCHOR + NEW_SS_BLOCK, 1)
    print("✅ SS_TIER 삽입 완료")

with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 패치 완료")
