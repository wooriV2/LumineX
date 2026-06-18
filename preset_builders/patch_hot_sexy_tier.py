import re

path = "C:/Dev/LumineX/dashboard.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

sss_new = """
    # 2026-06-18 핫&섹시 SSS 확정
    "bodycon_power", "boudoir_noir", "wet_silk_gown", "oil_goddess_gold",
    "rain_soaked_dress", "micro_dress_only", "deep_plunge_gown", "backless_extreme",
    "one_strap_gown", "pinup_classic", "vargas_girl", "bombshell_retro",
    "playboy_glam", "lingerie_noir", "barely_there", "wet_look_goddess",
    "micro_bikini_gold", "sarong_goddess", "nude_beach_art", "aqua_bikini",
    "golden_summer", "riviera_heat", "snow_queen_erotic", "autumn_gold_sensual",
    "christmas_boudoir", "summer_solstice_glam", "latex_queen", "pvc_goddess",
    "leather_mistress", "crystal_mesh_goddess", "chain_mail_glam",
    "fishnet_goddess", "lace_bodysuit", "satin_slip", "velvet_corset",
    "body_chain_only", "strappy_dress", "cut_out_swimsuit", "monokini_goddess",
    "champagne_drip", "neon_bodysuit", "bikini_top_only", "white_linen_sheer",
    "oil_drip_body", "yoga_pants_glam", "halter_glam", "wet_editorial",
    "pool_edge_wet", "ocean_wave_body", "penthouse_bath", "silk_sheets_morning",
    "spa_private_steam", "bar_counter_glam", "after_party_suite", "tennis_short_dress","""

ss_new = """
    # 2026-06-18 핫&섹시 SS 확정 (SSS 포함 전체)
    "bodycon_power", "boudoir_noir", "lingerie_goddess", "silk_robe_only",
    "corset_queen", "sheer_negligee", "wet_silk_gown", "oil_goddess_gold",
    "rain_soaked_dress", "pool_wet_glam", "sweat_glam", "micro_dress_only",
    "deep_plunge_gown", "backless_extreme", "one_strap_gown", "barely_covered",
    "pinup_classic", "vargas_girl", "bombshell_retro", "playboy_glam",
    "bunny_suit", "lingerie_noir", "elite_lingerie", "barely_there",
    "wet_look_goddess", "micro_bikini_gold", "sarong_goddess", "thong_bikini",
    "wet_bikini_pool", "nude_beach_art", "aqua_bikini", "golden_summer",
    "riviera_heat", "snow_queen_erotic", "autumn_gold_sensual", "christmas_boudoir",
    "summer_solstice_glam", "latex_queen", "pvc_goddess", "leather_mistress",
    "crystal_mesh_goddess", "chain_mail_glam", "fishnet_goddess", "see_through_gown",
    "wet_tshirt", "string_bikini", "lace_bodysuit", "satin_slip", "velvet_corset",
    "body_chain_only", "strappy_dress", "cut_out_swimsuit", "monokini_goddess",
    "champagne_drip", "neon_bodysuit", "bikini_top_only", "white_linen_sheer",
    "oil_drip_body", "yoga_pants_glam", "micro_skirt", "halter_glam",
    "wet_editorial", "pool_edge_wet", "ocean_wave_body", "penthouse_bath",
    "silk_sheets_morning", "spa_private_steam", "bar_counter_glam",
    "after_party_suite", "tennis_short_dress","""

# SSS anchor
sss_anchor = '    # 2026-06-13 v27 핫&섹시 SSS 확정'
content = content.replace(sss_anchor, sss_new + "\n" + sss_anchor)

# SS anchor  
ss_anchor = '    # 2026-06-13 v27 핫&섹시 SS/SSS 확정'
content = content.replace(ss_anchor, ss_new + "\n" + ss_anchor)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 핫&섹시 SSS/SS 패치 완료")
