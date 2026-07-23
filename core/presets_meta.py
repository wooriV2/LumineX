# -*- coding: utf-8 -*-
"""
LumineX Preset Metadata
카테고리별 프리셋 키 목록 + HOF / SSS / SS 분류

dashboard.py 에서 임포트 (A형)
상위 파일을 변경하면 배포 설정도 확인
"""

PRESET_CATEGORIES = {
    "?뼂截?Body Paint & Skin Transform": [
        "bioluminescent_ink", "klimt_gold_body", "vangogh_body", "dali_surreal", "munch_scream", "monet_bloom", "mucha_nouveau", "hokusai_wave",
        "kandinsky_abstract", "pollock_splash", "broken_porcelain", "marble_veins", "henna_goddess_body", "oil_slick_body", "liquid_chrome_body", "ink_wash_body",
        "body_paint_art", "watercolor_goddess", "fresco_goddess", "fresco_awakening", "tableau_vivant", "coral_reef", "leopard_dissolve", "peacock_feather",
        "snake_scale", "butterfly_wing", "deep_ocean_map", "dna_helix", "star_map", "neuron_network", "neon_circuit", "topographic",
        "maori_moko", "aztec_warrior", "egypt_hieroglyph", "celtic_knotwork", "polynesian_tribal", "viking_rune", "inca_geometric", "chinese_dragon",
        "aboriginal_dot", "galaxy_skin", "crystal_growth", "tree_of_life", "moonphase_body", "shadow_lace", "ash_phoenix", "half_statue",
        "rembrandt_chiaroscuro", "klimt_silver", "matisse_cutout", "mondrian_body", "basquiat_street", "warhol_pop", "lichtenstein_dot", "huli_wigman",
        "nuba_body", "wodaabe_beauty", "mehndi_full", "mayan_ritual", "haida_totem", "aurora_skin", "crystal_mineral", "tide_pool",
        "magnetic_field", "cell_division", "melting_chocolate", "liquid_gold_drip", "silver_mercury_body", "ink_pour_body", "paint_splash_body", "milk_bath_body",
        "rose_petal_body", "orchid_body", "vine_wrap_body", "lotus_body", "poison_flower", "fire_skin", "water_ripple_body", "frost_crystallize",
        "storm_static_body", "smoke_body_art", "lace_body_paint", "fishnet_paint", "chain_body_paint", "jewelry_trompe_loeil", "mandala_body", "body_calligraphy",
        "zentangle_body", "constellation_body", "circuit_erotic", "tarot_body", "moon_tattoo_body", "rune_body_art", "alchemy_body", "henna_erotic",
        "python_scales", "jaguar_spots", "mermaid_scales", "raven_feathers", "tiger_stripes_body", "cezanne_body", "gauguin_tropics", "toulouse_lautrec",
        "schiele_body", "degas_dancer", "renoir_soft", "botticelli_venus", "titian_goddess", "rubens_baroque", "ingres_odalisque", "waterhouse_nymph",
        "rossetti_dante", "alma_tadema", "vigee_lebrun", "keith_haring_body", "yayoi_kusama", "takashi_murakami", "jean_dubuffet", "jean_cocteau",
        "bodi_clay", "ndebele_pattern", "tuareg_indigo", "mursi_lip", "surma_body", "asaro_mudmen", "kayapo_brasil", "nuba_scarification",
        "kayan_neck", "thermal_scan", "bioluminescent_deep", "microscope_pollen", "xray_body", "mri_scan_body", "neural_map", "geologic_strata",
        "crystal_lattice", "solar_system_body", "dna_double_helix", "panther_black", "cheetah_speed", "snow_leopard", "ocelot_wild", "chameleon_skin",
        "dragon_scales_red", "komodo_dragon", "gecko_pattern", "crocodile_skin", "boa_constrictor", "king_cobra_hood", "butterfly_monarch", "butterfly_morpho",
        "dragonfly_iridescent", "scarab_beetle", "praying_mantis", "luna_moth", "atlas_moth", "eagle_wings", "flamingo_pink", "owl_feather",
        "parrot_tropical", "hummingbird_iridescent", "phoenix_rising", "swan_white", "macaw_scarlet", "bird_of_paradise", "octopus_ink", "koi_fish",
        "jellyfish_glow", "seahorse_fantasy", "mantis_shrimp", "anglerfish_deep", "nudibranch_sea", "cuttlefish_chromo", "wolf_grey", "zebra_stripes",
        "giraffe_pattern", "dalmatian_spots", "arctic_fox", "red_fox", "hyena_spots", "koi_dragon", "unicorn_opal", "gryphon_feather",
        "sphinx_cat", "basilisk_scales", "dancheong_body", "najeonchilgi_body", "goryeo_celadon_body", "minhwa_body", "korean_tiger_body", "pojagi_body",
        "taegeuk_body", "silla_crown_body", "dansaekhwa_body", "najeon_abalone", "baekhak_crane", "korean_dragon_body", "phoenix_jujakk", "baekho_white_tiger",
        "hyeonmu_turtle", "cheongnyong_dragon", "mugunghwa_body", "korean_lotus_body", "korean_plum_body", "korean_bamboo_body", "world_map_body", "topographic_body",
        "ocean_depth_body", "thermal_map_body", "weather_map_body", "subway_map_body", "europe_political_body", "africa_tribes_body", "japan_prefecture_body", "ancient_map_body",
        "star_map_body", "usa_county_map_body", "thermal_scan_body", "circuit_board_body", "galaxy_nebula_body", "crystal_geode_body", "hieroglyph_body", "aztec_calendar_body",
        "celtic_knot_body", "arabic_calligraphy_body", "islamic_geometric_body", "greek_mosaic_body", "autumn_leaves_body", "coral_reef_body", "mushroom_forest_body", "stained_glass_body",
        "bauhaus_body", "urban_decay_body", "forest_stone_body", "banksy_stencil", "shadow_art_nude", "geisha_bodypaint", "maiko_bodypaint", "kimono_bodypaint",
        "noh_bodypaint", "kabuki_bodypaint", "samurai_bodypaint", "geisha_white_bodypaint", "ninja_bodypaint", "hanbok_bodypaint", "joseon_bodypaint", "gisaeng_bodypaint",
        "hanbok_modern_bodypaint", "korean_shaman_bodypaint", "qipao_bodypaint", "cheongsam_bodypaint", "hanfu_bodypaint", "tang_dynasty_bodypaint", "ming_bodypaint", "sari_bodypaint",
        "belly_bodypaint", "odalisque_bodypaint", "harem_bodypaint", "mughal_bodypaint", "persian_bodypaint", "moroccan_bodypaint", "ottoman_bodypaint", "thai_bodypaint",
        "balinese_bodypaint", "kebaya_bodypaint", "batik_bodypaint", "ikat_bodypaint", "ao_dai_bodypaint", "tibetan_bodypaint", "shaman_bodypaint", "scythian_bodypaint",
        "mayan_bodypaint", "hopi_bodypaint", "olmec_bodypaint", "maori_bodypaint", "polynesian_bodypaint", "haida_bodypaint", "yoruba_bodypaint", "kente_bodypaint",
        "dashiki_bodypaint", "adinkra_bodypaint", "zulu_bodypaint", "scottish_bodypaint", "byzantine_bodypaint", "flamenco_bodypaint", "dirndl_bodypaint", "sumerian_bodypaint",
        "voodoo_bodypaint", "body_paint_watercolor_free", "body_paint_metallic_free", "body_paint_impasto", "body_paint_airbrush", "body_paint_ink_splatter", "body_paint_drip_free", "body_paint_monochrome",
        "body_paint_pastel_dream", "body_paint_neon_glow", "body_paint_earth_tones", "body_paint_jewel_tones", "body_paint_iridescent_free", "body_paint_abstract_expressionist", "body_paint_geometric_free", "body_paint_organic_flow",
        "body_paint_surreal_free", "body_paint_minimalist_free", "body_paint_blacklight", "body_paint_glitter_free", "body_paint_uv_reactive",
    ],

    "?뮟 Luxury Glamour": [
        "runway_power", "red_carpet", "editorial_glam", "golden_hour_editorial", "noir_opulence", "platinum_elite", "ivory_silk", "ivory_tower",
        "pearl_essence", "velvet_gold", "velvet_darkness", "all_black_goddess", "black_mirror", "onyx_tension", "phantom_gloss", "champagne_mist",
        "couture_heat", "silk_wrap", "goddess_draped", "feather_cascade", "feather_touch", "golden_oil", "golden_nude", "gold_temptress",
        "red_temptress", "petal_goddess", "cobweb_drape", "casino_royale", "black_tie_gala", "champagne_tower", "fur_coat_only", "plunge_gown",
        "slit_maxi", "cutout_bodysuit", "sheer_overlay", "jeweled_bikini_top", "golden_drape_goddess", "crystal_gown", "feather_trim_mini", "luxury_noir",
        "diamond_couture", "velvet_serpent", "opera_glam", "silver_screen", "lace_noir", "white_silk_goddess", "crystal_bodycon", "penthouse_glam",
        "midnight_couture", "crimson_gown", "serpentine_dress", "baroque_glam", "private_pool_villa", "rooftop_pool_night", "penthouse_pool", "yacht_sunset_glam",
        "casino_vip_glam", "limo_glam",
    ],

    "?뵦 Hot & Sexy": [
        "lingerie_goddess", "silk_robe_only", "corset_queen", "bodycon_power", "sheer_negligee", "boudoir_noir", "wet_silk_gown", "oil_goddess_gold",
        "pool_wet_glam", "rain_soaked_dress", "sweat_glam", "micro_dress_only", "barely_covered", "deep_plunge_gown", "backless_extreme", "one_strap_gown",
        "pinup_classic", "vargas_girl", "bombshell_retro", "bunny_suit", "playboy_glam", "elite_lingerie", "lingerie_noir", "barely_there",
        "wet_look_goddess", "thong_bikini", "micro_bikini_gold", "sarong_goddess", "wet_bikini_pool", "topless_editorial", "nude_beach_art", "aqua_bikini",
        "golden_summer", "riviera_heat", "snow_queen_erotic", "autumn_gold_sensual", "christmas_boudoir", "summer_solstice_glam", "latex_queen", "pvc_goddess",
        "leather_mistress", "crystal_mesh_goddess", "chain_mail_glam", "fishnet_goddess", "see_through_gown", "wet_tshirt", "string_bikini", "lace_bodysuit",
        "satin_slip", "velvet_corset", "body_chain_only", "strappy_dress", "cut_out_swimsuit", "monokini_goddess", "champagne_drip", "neon_bodysuit",
        "bikini_top_only", "white_linen_sheer", "oil_drip_body", "yoga_pants_glam", "micro_skirt", "halter_glam", "wet_editorial", "pool_edge_wet",
        "ocean_wave_body", "penthouse_bath", "dressing_room_mirror", "silk_sheets_morning", "spa_private_steam", "bar_counter_glam", "vip_booth_neon", "after_party_suite",
        "tennis_short_dress", "pasties_editorial", "body_tape_art", "invisible_dress", "painted_jeans", "wrap_sarong_nude", "ribbon_only", "desert_heat_nude",
        "jungle_wet_goddess", "sauna_nude_editorial", "steam_room_goddess", "volcanic_heat_body",
    ],

    "?뭼 Erotic & Fetish": [
        "latex_venom", "chrome_vixen", "chain_goddess", "dominatrix_glam", "bondage_fashion", "strappy_harness", "mesh_bodysuit", "latex_catsuit",
        "oil_goddess", "savage_leather", "burlesque", "showgirl", "cabaret_star", "pole_art", "candy_rave", "lap_dance_glam",
        "striptease_art", "pole_dance_power", "midnight_bath", "belly_dance_glam", "dark_succubus", "vampire_seduction", "witch_sensual", "dark_fairy_erotic",
        "shadow_seductress", "latex_catsuit_red", "rubber_goddess", "harness_only", "rope_bondage_art", "vinyl_goddess", "corset_stockings", "catsuit_zipper",
        "bodystocking", "secretary_after_hours", "nurse_sensual", "maid_sensual", "leather_bodysuit", "wet_latex", "fetish_boots_only", "dominatrix_red",
        "fishnet_bodysuit", "transparent_dress", "sheer_catsuit", "latex_transparent", "latex_hood_full", "pvc_transparent_full", "chrome_bodysuit", "mirror_dress",
        "liquid_metal_body", "suspension_art", "dominatrix_full_armor", "goddess_throne", "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",
        "pole_dance_extreme", "fire_goddess", "succubus_full", "dark_angel_fallen", "alien_queen_body", "body_paint_nude", "micro_thong_only", "tape_bondage",
        "metal_bondage", "lap_dance_extreme", "liquid_latex_drip", "chrome_paint_body", "silver_foil_body", "holographic_latex", "mirror_latex", "neon_latex",
    ],

    "?뙼 Nature & Elements": [
        "lava_flow", "ocean_surge", "ice_palace", "ice_refraction", "frozen_latex", "blizzard_queen", "sandstorm_veil", "storm_couture",
        "heat_shimmer", "water_reflection", "waterfall_goddess", "rain_soaked", "mist_goddess", "mist_vanguard", "winter_forest", "desert_mirage",
        "desert_oracle", "desert_sand_glam", "cliff_edge", "arctic_minimal", "dawn_awakening", "aurora_drape", "aurora_spirit", "lightning_body",
        "solar_flare", "tropical_storm", "smoke_veil", "liquid_gold_pour", "liquid_mirror", "prism_light", "shattered_glass", "zero_gravity",
        "volcanic_goddess", "storm_lightning", "deep_cave", "tidal_wave", "son_doong_jungle", "waitomo_glow", "dead_vlei_ghost", "danxia_rainbow",
        "cenote_sacred", "socotra_alien", "lake_natron", "namib_star_desert", "zhangjiajie_avatar", "pamukkale_white", "plitvice_cascade", "frozen_baikal",
        "rainbow_mountain", "wisteria_tunnel", "torres_del_paine", "ha_long_bay", "kelimutu_crater", "victoria_falls", "fairy_pools", "tunnel_of_love",
        "chocolate_hills",
    ],

    "?똽 City & Night": [
        "neon_noir", "neon_dystopia", "neon_rain_goddess", "holographic_city", "vaporwave_dream", "rooftop_midnight", "rooftop_party", "midnight_goddess",
        "midnight_monolith", "nightclub_vip", "monaco_nights", "miami_afterglow", "azure_nights", "blue_hour_goddess", "candlelight_noir", "jazz_club",
        "jazz_age", "noir_ballet", "urban_vanguard", "brutalist_glam", "after_dark_minimal", "disco_goddess", "music_festival", "new_year_countdown",
        "cyber_fire", "cyber_silk", "emerald_city", "tokyo_shibuya", "paris_midnight", "subway_editorial", "penthouse_view", "sheikh_zayed_dawn",
        "livraria_lello_staircase", "palacio_de_sal", "santorini_sunset", "cappadocia_balloons", "chefchaouen_blue", "hallstatt_lake", "shirakawa_snow", "positano_cliff",
        "bruges_canal", "cinque_terre_harbor",
    ],

    "?렗 Editorial & Mood": [
        "silhouette_only", "back_beauty", "collarbone_focus", "neck_elegance", "long_legs_focus", "light_driven", "backlit_silk", "mirror_goddess",
        "mirror_room", "eclipse_body", "chrome_skin", "neon_body", "plasma_aura", "molten_chrome", "mercury_rising", "mercury_pool",
        "titanium_body", "snowflake_skin", "80s_power", "y2k_chrome", "bohemian_paris", "origami_couture", "wet_glass", "smoke_studio",
        "infrared_beauty", "grain_film", "bed_editorial", "floor_editorial", "chair_editorial", "door_frame_glam", "staircase_glam", "elevator_glam",
        "dreamy_soft_focus", "film_noir_glam", "noir_femme_fatale",
    ],

    "?뤊 Civilization & Myth": [
        "cleopatra_gold", "pharaoh_queen", "byzantine_empress", "maasai_warrior", "nine_tails", "moonrise_ceremony", "oracle_smoke", "ritual_ash",
        "ruins_goddess", "renaissance_fantasy", "renaissance_nude", "cathedral_light", "baroque_punk", "art_gallery", "museum_glamour", "library_secret",
        "living_sculpture", "living_statue", "sculpture_goddess", "marble_goddess", "marble_minimal", "viking_queen", "sumerian_queen", "ming_empress",
        "aztec_sun_goddess", "celtic_warrior_queen", "aphrodite_glam", "artemis_huntress", "freya_norse", "kali_goddess", "isis_egypt", "lakshmi_goddess",
        "oshun_yoruba", "morgan_le_fay", "haetae_guardian", "dokkaebi_spirit", "korean_tiger_spirit", "gyeongbokgung_night", "union_jack_body", "brazil_flag_body",
        "usa_stars_stripes_body", "japan_rising_sun_body", "south_africa_flag_body", "india_flag_body", "mexico_flag_body", "ukraine_flag_body",
    ],

    "?덌툘 Career & Lifestyle": [
        "flight_attendant", "pilot_glamour", "nurse_glamour", "lawyer_power", "hotel_concierge", "cruise_hostess", "yacht_captain", "yacht_club",
        "sommelier", "wine_tasting", "casino_dealer", "private_jet", "helipad", "luxury_shopping", "golf_glam", "golf_caddie",
        "tennis_luxe", "tennis_referee", "f1_grid_girl", "equestrian_glam", "cheerleader", "architect_chic", "fitness_power", "yoga_goddess",
        "barista_chic", "gallery_curator", "horse_racing", "scuba_instructor", "ballet_prima", "gymnastics_editorial", "figure_skater", "tennis_champion",
        "archery_goddess", "carnival_rio",
    ],

    "?뵰 Fantasy & Dark": [
        "dark_mermaid", "vampire_queen", "angel_fallen", "moon_goddess", "demon_goddess", "forest_witch", "pastel_fairy", "medusa_queen",
        "halloween_queen", "hologram_ghost", "glitch_beauty", "void_emergence", "void_glamour", "void_secret", "crystal_goddess", "toxic_bloom",
        "zombie_apocalypse", "dark_academia", "gothic_romance", "double_exposure_dark", "double_exposure_ethereal", "oil_slick_noir", "witch_ritual", "fae_queen",
        "cursed_beauty", "shadow_realm",
    ],

    "?뷂툘 Power & Edge": [
        "valkyrie_storm", "biker_glam", "shadow_play", "fencer_noir", "martial_arts", "boxing_glamour", "power_curve", "power_suit",
        "sculpted_power", "shadow_queen", "bioluminescence", "bioluminescent", "duo_aurora_bodypaint", "duo_ocean_bodypaint", "duo_golden_desert_bodypaint", "duo_cyberpunk_bodypaint",
        "duo_jungle_tribal_bodypaint", "duo_latex_color_block", "duo_latex_storm_opposites", "duo_dark_latex_power", "duo_flamenco_latex_fusion", "duo_smoke_noir", "duo_infinity_pool_contrast", "duo_pool_bodypaint_micro",
        "duo_wet_glass_divide", "duo_bodypaint_vs_latex", "duo_fire_and_ice", "duo_angel_devil", "duo_chrome_future", "duo_skeleton_bloom_bodypaint", "duo_odalisque_gisaeng_bodypaint", "trio_stone_bronze_iron_bodypaint",
        "trio_past_present_future_bodypaint", "trio_sunrise_sunset_moonrise_bodypaint", "trio_lightning_ocean_earthquake_bodypaint", "trio_sand_ice_magma_bodypaint", "trio_sky_earth_underground_bodypaint", "trio_fog_rain_snow_bodypaint", "trio_primary_colors_bodypaint", "trio_black_white_gray_bodypaint",
        "trio_gold_silver_bronze_bodypaint", "trio_infrared_visible_uv_bodypaint", "trio_creator_preserver_destroyer_bodypaint", "trio_fate_three_bodypaint", "trio_medusa_sphinx_hydra_bodypaint", "trio_creation_of_adam_bodypaint", "trio_east_west_south_bodypaint", "trio_viking_samurai_spartan_bodypaint",
        "trio_nile_amazon_yangtze_bodypaint", "trio_rome_babylon_aztec_bodypaint", "trio_fear_anger_joy_bodypaint", "trio_order_chaos_void_bodypaint", "trio_id_ego_superego_bodypaint", "trio_thesis_antithesis_synthesis_bodypaint", "riot_goddess", "punk_queen",
        "steel_warrior", "cage_fighter",
    ],

    "?룚截?Beach & Resort": [
        "summer_beach", "surfer_goddess", "pool_goddess", "poolside_noir", "infinity_pool", "beach_bonfire", "scuba_goddess", "glass_floor",
        "glass_house", "ski_chalet", "vineyard_harvest", "spa_noir", "balcony_goddess", "sunset_cruise", "coral_diving", "beach_bonfire_night",
        "hammock_resort",
    ],

    "?렚 Performance & Dance": [
        "flamenco_queen", "tango_passion", "circus_performer", "ribbon_dance", "aerial_silk", "fire_dancer", "masquerade_ball", "opera_night",
        "christmas_glamour", "pop_art_glamour", "ribbon_goddess", "petal_storm", "ballet_noir", "broadway_diva", "street_dance", "drag_glamour",
        "samba_carnival", "hula_goddess", "jazz_dance_glam", "kathak_dance",
    ],

    "?몮 Traditional Costume": [
        "geisha_noir", "geisha_red", "maiko_glamour", "hanbok_glamour", "qipao_noir", "sari_goddess", "harem_goddess", "belly_dancer",
        "odalisque", "imperial_silk", "kimono_silk", "ao_dai_sheer", "thai_temple", "indian_bridal", "moroccan_kaftan", "persian_court",
        "yoruba_glamour", "balinese_goddess", "chinese_qipao_slit", "scottish_corset", "hanfu_goddess", "cheongsam_slit", "kebaya_java", "dashiki_glam",
        "kaftan_sheer", "flamenco_dress", "dirndl_glam", "hanbok_modern", "ao_dai_glamour", "saree_draped_sensual", "joseon_queen", "joseon_consort",
        "gisaeng_glamour", "gisaeng_noir", "mudang_shaman", "haenyeo_goddess", "silla_empress", "goguryeo_warrior", "goryeo_empress", "joseon_painter",
        "korean_shaman_fire", "baekje_lotus", "silla_gold_crown",
    ],

    "?뙵 Season & Theme": [
        "cherry_blossom", "lavender_field", "spring_rain", "tulip_field", "autumn_forest", "sunflower_field", "greenhouse_eden", "tropical_night",
        "first_snow", "golden_autumn", "midsummer_heat", "rainy_season", "harvest_moon", "winter_solstice", "cherry_blossom_night", "tropical_monsoon",
        "halloween_glam", "new_year_glam", "sakura_night_glam", "monsoon_goddess",
    ],

    "?뜫 Pop & Kawaii": [
        "y2k_fairy", "pink_champagne", "cotton_candy", "angel_baby", "idol_stage", "kitty_glam", "strawberry_milk", "cherry_pop",
        "neon_kawaii", "fairy_kei", "gyaru_glam", "kogal_style", "hime_gyaru", "decora_kei", "maid_glamour", "visual_kei",
        "lolita_gothic", "disco_barbie", "space_babe", "bubblegum_pop", "rainbow_rave", "glitter_bomb", "arcade_queen", "virtual_idol",
        "tokimeki_pop", "kpop_idol", "korean_ulzzang", "kbeauty_goddess", "kdrama_heroine", "manga_girl", "kpop_girl_crush", "hallyu_goddess",
        "kbeauty_glass_skin", "kdrama_villain_queen", "kdrama_chaebol_heir", "gangnam_luxury_glam", "bubble_tea", "doll_house", "harajuku_doll",
    ],

    "?럩 Anime & Glamour": [
        "zero_suit", "battle_bikini", "succubus_anime", "catgirl_luxe", "dark_magical_girl", "witch_apprentice", "fallen_angel_anime", "kunoichi_glam",
        "oni_warrior", "samurai_bride", "dragon_princess", "android_girl", "pilot_suit", "neon_android", "vampire_seductress", "cosmic_warrior_glam",
        "dark_jester_glam", "poison_ivy_vines", "storm_goddess", "dark_sorceress_glam", "jessica_rabbit_glam", "webtoon_heroine", "manhwa_villainess", "barbarella_retro",
        "vampirella_dark", "ghost_shell", "android_2b", "street_fighter_chun", "dark_elsa", "sailor_moon_dark", "anime_swordmistress", "anime_mecha_pilot",
        "anime_shrine_maiden", "anime_demon_slayer", "anime_galaxy_idol", "anime_battle_angel", "anime_cyber_ninja", "anime_cel_shaded", "anime_webtoon_style",
    ],

    "?렓 Anime Art Style": [
        "anime_jp_90s_retro", "anime_jp_80s_citypop", "anime_jp_modern_glossy", "anime_jp_shoujo_soft", "anime_jp_shounen_action", "anime_jp_seinen_gritty", "anime_jp_makoto_watercolor", "anime_jp_ghibli_soft",
        "anime_jp_ecchi_glossy", "anime_jp_gekiga_noir", "anime_jp_pinup_retro", "anime_kr_webtoon_glossy", "anime_kr_romance_soft", "anime_kr_action_manhwa", "anime_kr_lezhin_mature", "anime_kr_pastel_dream",
        "anime_kr_lofi_chill", "anime_kr_noir_mature", "anime_cn_donghua_xianxia", "anime_cn_guofeng_ink", "anime_cn_modern_donghua", "anime_cn_palace_drama", "anime_us_cartoon_bold", "anime_us_comic_ink",
        "anime_us_pixar_stylized", "anime_us_disney_classic", "anime_us_pinup_classic", "anime_us_badgirl_comic", "anime_eu_ligne_claire", "anime_eu_graphic_novel", "anime_eu_erotic_bd", "anime_noir_silhouette",
    ],

    "?뙌 Silhouette & Shadow": [
        "silhouette_spotlight_smoke", "silhouette_spotlight_latex", "silhouette_spotlight_heels", "silhouette_spotlight_hair", "silhouette_spotlight_dance", "silhouette_spotlight_chair", "silhouette_spotlight_back", "silhouette_spotlight_pole",
        "silhouette_window_city", "silhouette_window_rain", "silhouette_window_sheer", "silhouette_doorway_light", "silhouette_window_sunset", "silhouette_window_neon", "silhouette_neon_pink", "silhouette_neon_blue",
        "silhouette_neon_red", "silhouette_neon_purple", "silhouette_neon_multicolor", "silhouette_sunset_beach", "silhouette_sunset_cliff", "silhouette_moonlight", "silhouette_aurora", "silhouette_pool_underwater",
        "silhouette_pool_edge", "silhouette_bath_candle", "silhouette_rain_wet", "silhouette_fire_dark", "silhouette_candle_boudoir", "silhouette_smoke_studio",
    ],

    "?뙆 Impossible & Surreal": [
        "storm_eye_editorial", "living_fabric", "macro_goddess", "time_freeze_editorial", "gravity_defiance", "magnetic_field_goddess", "micro_world", "mirror_shatter_dress",
        "dissolution", "crystallization", "giant_flora", "supernova_burst", "portal_threshold", "escher_staircase", "aurora_embodied", "nebula_goddess",
        "shadow_independent", "negative_space", "flame_dress", "reflection_rebel", "time_lapse_body", "invisible_outline", "waterfall_gown", "cloud_couture",
        "weather_maker", "gravity_well", "double_exposure_self", "richat_eye", "marble_caves_water",
    ],

    "?룢截?Ruins & Civilization": [
        "petra_rose", "angkor_dawn", "tikal_skyrise", "bagan_balloon", "ellora_rock_temple", "derinkuyu_underground", "tigers_nest_cliff", "naoshima_art_island",
        "machu_picchu_cloud", "chichen_itza_pyramid", "colosseum_dusk", "alhambra_palace", "borobudur_dawn", "karnak_temple", "mont_saint_michel", "sigiriya_rock",
        "angkor_thom_faces", "teotihuacan_pyramid", "gobekli_tepe", "palmyra_colonnade",
    ],

    "?뙅 Elemental Goddess": [
        "uyuni_wet_silk", "dead_sea_goddess", "iceland_hot_spring", "maldives_underwater", "niagara_wet_editorial", "monsoon_goddess", "black_sea_midnight", "amazon_river_goddess",
        "lava_field_latex", "sahara_mirage", "volcano_edge_glam", "desert_heat_body", "bonfire_editorial", "solar_flare_goddess", "trolltunga_edge", "zhangjiajie_cloud",
        "aurora_bare", "skydive_editorial", "cliff_wind_sheer", "hot_air_balloon_glam", "antelope_light_sheer", "waitomo_glow_body", "socotra_alien_glam", "antarctica_ice_glam",
        "deep_jungle_goddess", "coral_reef_sheer", "salt_flat_body", "thunderstorm_wet", "northern_lights_body", "meteor_shower_glam", "pamukkale_goddess", "salar_atacama_flamingo",
        "bioluminescent_bay", "cave_waterfall_goddess", "red_canyon_goddess", "glacier_melt_goddess", "wave_barrel_goddess", "eruption_silhouette", "ice_cave_blue", "rainbow_falls_goddess",
    ],

    "?뮛 Wet & Gloss": [
        "pool_surface_break", "pool_underwater_up", "pool_edge_dripping", "infinity_pool_wet", "hot_spring_steam", "jacuzzi_bubbles", "champagne_pour_body", "wine_pour_body",
        "milk_pour_body", "honey_pour_body", "gold_paint_body", "paint_pour_goddess", "neon_paint_pour", "shower_goddess", "rain_soaked_nude", "hot_tub_goddess",
        "foam_bath_goddess", "waterfall_nude", "ocean_nude_editorial", "steam_bath_goddess", "rain_window_inside", "rain_street_soaked", "rain_studio_dramatic", "monsoon_body",
        "rain_car_window", "oil_pour_studio", "oil_drip_back", "honey_drip_body", "chocolate_pour_gloss", "gloss_lips_drip", "chrome_gloss_body", "sweat_studio_light",
        "after_workout_glow", "heat_mirage_sweat", "sauna_steam_body", "condensation_skin", "ice_melt_drip", "dew_morning_body", "frost_breath_cold", "waterfall_direct",
        "wave_crash_body", "wet_silk_minimal", "bubble_bath_gloss", "milk_bath_petals",
    ],

    "?뙧截?Atmosphere & Particle": [
        "smoke_machine_club", "dry_ice_floor", "cigarette_smoke_noir", "incense_smoke_ritual", "smoke_color_holi", "fog_forest_mystery", "gold_dust_pour", "holi_powder_explosion",
        "chalk_dust_sport", "flour_dust_studio", "pigment_powder_art", "feather_explosion", "black_feather_dark", "petal_storm_indoor", "cherry_blossom_burst", "dried_flower_cascade",
        "glitter_rain_studio", "gold_confetti_burst", "silver_glitter_body", "neon_particle_club", "bubble_floating_studio", "sparkler_night_glam", "fire_poi_dance", "ember_glow_dark",
        "firework_silhouette", "autumn_leaves_burst", "snow_indoor_studio", "dandelion_blow", "firefly_night_field", "seed_pod_floating",
    ],

    "?몣 Korean History & Court": [
        "silla_queen_gold", "silla_dancing_girl", "baekje_lotus_queen", "goguryeo_warrior_queen", "gojoseon_shaman_queen", "gaya_iron_goddess", "silla_hwarang_girl", "ancient_mural_goddess",
        "three_kingdoms_spy", "dongye_tribal_queen", "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess", "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",
        "mongol_goryeo_queen", "goryeo_haenyeo_silk", "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex", "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",
        "joseon_merchant_woman", "damo_warrior", "joseon_night_queen", "joseon_concubine_red", "changdeok_moonlight", "gyeongbokgung_geisha", "gisaeng_joseon_sheer", "gisaeng_red_lantern",
        "gisaeng_sword_dance", "gisaeng_haiku_bath", "gisaeng_rain_dance", "gisaeng_black_silk", "wonhyang_legend", "hwang_jini_glam", "gisaeng_fan_dance", "gisaeng_pipa_night",
        "gisaeng_mirror_boudoir", "pyongyang_gisaeng", "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam", "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
        "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent", "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix", "haenyeo_wet_glam", "dano_festival_glam",
        "ganggangsullae_night", "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat", "jeju_shaman_sea", "korean_harvest_goddess", "joseon_female_assassin", "goryeo_archer_queen",
        "silla_female_hwarang", "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior", "goguryeo_fire_warrior", "joseon_spy_sheer", "joseon_modern_fusion", "gisaeng_cyberpunk",
        "hanbok_latex_queen", "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern", "hanbok_wet_editorial", "joseon_boudoir",
    ],

    "?렓 Multi Body Paint": [
        "duo_fire_and_ice_bodypaint", "duo_day_and_night_bodypaint", "duo_bloom_and_void_bodypaint", "duo_gold_and_shadow_bodypaint", "duo_ocean_and_desert_bodypaint", "duo_circuit_and_nature_bodypaint", "duo_east_and_west_bodypaint", "duo_macro_and_micro_bodypaint",
        "duo_ancient_and_future_bodypaint", "duo_poison_and_medicine_bodypaint", "duo_deep_sea_bodypaint", "trio_rgb_trinity_bodypaint", "trio_past_present_future_bodypaint", "trio_predator_prey_apex_bodypaint", "trio_ink_gold_chrome_bodypaint", "trio_season_trinity_bodypaint",
        "trio_sun_moon_star_bodypaint", "trio_three_oceans_bodypaint", "trio_three_civilizations_bodypaint", "trio_fire_water_earth_bodypaint", "trio_three_big_cats_bodypaint", "duo_butterfly_split_bodypaint", "duo_yin_yang_merge_bodypaint", "duo_world_map_bodypaint",
        "duo_klimt_tree_bodypaint", "duo_galaxy_split_bodypaint", "duo_wave_hokusai_bodypaint", "duo_dna_helix_bodypaint", "duo_solar_eclipse_bodypaint", "duo_human_shadow_bodypaint", "duo_tiger_split_bodypaint", "duo_starry_night_split_bodypaint",
        "duo_peacock_split_bodypaint", "trio_triptych_klimt_bodypaint", "trio_phoenix_rising_bodypaint", "trio_world_tree_bodypaint", "trio_ocean_depth_bodypaint", "trio_aurora_spectrum_bodypaint", "trio_cosmic_creation_bodypaint", "trio_last_supper_bodypaint",
        "trio_rainbow_arc_bodypaint", "trio_milky_way_panorama_bodypaint", "trio_coral_reef_zones_bodypaint", "trio_creation_of_adam_bodypaint", "trio_poles_and_equator_bodypaint", "quad_four_civilizations_bodypaint", "feather_body_cover", "mushroom_moss_cover",
        "butterfly_swarm_cover", "seashell_body_cover", "silver_chain_mirror_room", "desert_sand_sculpture", "ice_crystal_gown", "autumn_leaves_cover", "leaf_draping_cover", "quad_four_goddesses_bodypaint",
        "quad_four_ages_bodypaint", "quad_four_metals_bodypaint", "quad_four_gemstones_bodypaint", "quad_cmyk_bodypaint", "quad_four_classical_elements_klimt", "quad_four_seasons_night_bodypaint", "quint_five_senses_bodypaint", "quint_five_worlds_bodypaint",
        "quint_five_elements_wuxing_bodypaint", "quint_five_mythologies_bodypaint", "quint_five_oceans_deep_bodypaint", "quint_five_sacred_colors_bodypaint", "quint_five_dance_cultures_bodypaint", "hexa_rainbow_spectrum_bodypaint", "club_vip_neon_goddess", "club_rooftop_citylight",
        "micro_sequin_club", "rooftop_micro_night", "night_brazil_tokyo_neon", "night_supermodel_paris_rooftop", "night_powerlifter_lasvegas", "silk_slip_dawn_hotel", "satin_slip_vanity_noir", "satin_slip_micro",
        "leopard_power_editorial", "leopard_micro_studio", "snake_micro_marble", "snakeskin_latex_glam", "gyeongbokgung_night_couture", "bukchon_rain_editorial", "namsan_tower_dusk", "dongdaemun_neon_rain",
        "haeinsa_temple_dawn", "jeju_volcanic_coast", "fushimi_inari_crimson", "arashiyama_bamboo_mist", "osaka_dotonbori_neon", "mount_fuji_dawn_silk", "japanese_garden_autumn", "kabukiza_backstage_glam",
        "forbidden_city_golden_hour", "li_river_karst_mist", "shanghai_bund_noir", "zhangjiajie_cloud_forest", "west_lake_lotus_dawn", "bali_tanah_lot_sunset", "hoi_an_lantern_rain", "bangkok_wat_arun_gold",
        "singapore_marina_bay_night", "luang_prabang_monk_dawn", "rice_terrace_banaue_mist", "opera_house_goddess", "venetian_carnival_palazzo", "flamenco_tablao_fire", "broadway_red_curtain", "scottish_castle_mist",
        "sahara_dune_queen", "ballet_stage_noir", "silk_ribbon_minimal", "tropical_flower_minimal", "silver_foil_minimal", "moss_stone_minimal", "crystal_geode_minimal", "black_feather_minimal",
        "wet_lotus_pool_minimal", "butterfly_wings_minimal", "seaweed_ocean_minimal", "trio_inside_outside_bodypaint", "hexa_six_chakras_bodypaint", "octet_planets_solar_bodypaint", "quad_fashion_capitals_bodypaint", "quad_four_seasons_bodypaint",
        "quad_four_elements_bodypaint", "quad_four_directions_bodypaint", "quad_four_seasons_klimt_bodypaint", "quad_rgba_spectrum_bodypaint", "quint_five_continents_bodypaint", "quint_five_elements_asia_bodypaint", "quint_rainbow_five_bodypaint", "quint_five_oceans_bodypaint",
        "duo_earth_hemisphere_bodypaint", "duo_day_city_night_city_bodypaint", "duo_volcano_glacier_bodypaint", "duo_storm_eye_bodypaint", "duo_aurora_milkyway_bodypaint", "duo_coral_abyss_bodypaint", "duo_tree_root_bodypaint", "duo_eagle_serpent_bodypaint",
        "duo_wolf_moon_bodypaint", "duo_butterfly_cocoon_bodypaint", "duo_dragon_phoenix_bodypaint", "duo_lion_zebra_bodypaint", "duo_spider_web_bodypaint", "duo_mona_lisa_split_bodypaint", "duo_birth_venus_split_bodypaint", "duo_yin_yang_koi_bodypaint",
        "duo_chess_board_bodypaint", "duo_android_human_bodypaint", "duo_black_hole_star_bodypaint", "duo_past_future_city_bodypaint", "duo_virus_antibody_bodypaint", "duo_matrix_reality_bodypaint", "duo_crystal_lava_bodypaint", "duo_skeleton_bloom_bodypaint",
        "duo_ink_wash_split_bodypaint", "trio_stone_bronze_iron_bodypaint", "trio_ancient_medieval_modern_bodypaint", "trio_birth_life_death_bodypaint", "trio_seed_tree_ash_bodypaint", "trio_lightning_ocean_earthquake_bodypaint", "trio_sand_ice_magma_bodypaint", "trio_sky_earth_underground_bodypaint",
        "trio_micro_human_macro_bodypaint", "trio_fog_rain_snow_bodypaint", "trio_jungle_desert_tundra_bodypaint", "trio_primary_colors_bodypaint", "trio_black_white_gray_bodypaint", "trio_gold_silver_bronze_bodypaint", "trio_sunrise_sunset_moonrise_bodypaint", "trio_infrared_visible_uv_bodypaint",
        "trio_heaven_earth_hell_bodypaint", "trio_creator_preserver_destroyer_bodypaint", "trio_fate_three_bodypaint", "trio_medusa_sphinx_hydra_bodypaint", "trio_valkyrie_siren_medea_bodypaint", "trio_amazon_sahara_arctic_bodypaint", "trio_east_west_south_bodypaint", "trio_viking_samurai_spartan_bodypaint",
        "trio_nile_amazon_yangtze_bodypaint", "trio_rome_babylon_aztec_bodypaint", "trio_love_war_peace_bodypaint", "trio_fear_anger_joy_bodypaint", "trio_order_chaos_void_bodypaint", "trio_id_ego_superego_bodypaint", "trio_thesis_antithesis_synthesis_bodypaint",
    ],

    "?뫍 Duo Glamour": [
        "duo_infinity_pool_contrast", "duo_rain_neon_soaked", "duo_ink_wash_split_bodypaint", "duo_pool_bodypaint_micro", "duo_wet_glass_divide", "duo_bodypaint_vs_latex", "duo_ocean_bodypaint", "duo_golden_desert_bodypaint",
        "duo_aurora_bodypaint", "duo_cyberpunk_bodypaint", "duo_jungle_tribal_bodypaint", "duo_latex_color_block", "duo_latex_storm_opposites", "duo_dark_latex_power", "duo_flamenco_latex_fusion", "duo_smoke_noir",
        "duo_versailles_latex_gold", "duo_monaco_yacht", "duo_champagne_gala", "duo_villa_italy", "duo_casino_power", "duo_fire_and_ice", "duo_angel_devil", "duo_chrome_future",
        "duo_sunset_silhouette", "duo_desert_minimal", "duo_kpop_stage", "duo_penthouse_power", "duo_ice_bath_contrast",
        "korean_silverfox_duo_irezumi_crimson_jeonju",
        "korean_silverfox_duo_irezumi_crimson_void",
        "korean_silverfox_duo_dancheong_emerald_bukchon",
        "korean_silverfox_duo_minhwa_obsidian_deoksugung",
        "korean_silverfox_duo_haetae_violet_aurora",
        "korean_silverfox_duo_dragon_teal_namsan",
        "korean_silverfox_duo_lotus_gold_versailles",
        "korean_silverfox_duo_celadon_silver_monaco",
        "korean_silverfox_duo_phoenix_crimson_gyeongju",
        "korean_silverfox_duo_minhwa_teal_bukhansan",
        "korean_silverfox_duo_haetae_gold_jongmyo",
        "korean_silverfox_duo_dragon_violet_void",
        "korean_silverfox_duo_celadon_crimson_busan",
        "korean_silverfox_duo_dancheong_teal_changdeokgung",
        "korean_silverfox_duo_skull_chrysanthemum_obsidian_void",
        "korean_silverfox_duo_koi_maple_gold_suncheon",
        "korean_silverfox_duo_baekja_emerald_jeju",
        "korean_silverfox_duo_dragon_phoenix_void",
        "korean_silverfox_duo_dancheong_violet_gyeongbokgung",
        "korean_silverfox_duo_minhwa_crimson_dongdaemun",
        "korean_silverfox_duo_haetae_gold_aurora",
        "korean_silverfox_duo_lotus_obsidian_bukchon",
        "korean_silverfox_duo_dragon_silver_shibuya",
        "korean_silverfox_duo_minhwa_emerald_monaco",
        "korean_silverfox_duo_dancheong_teal_void",
        "korean_silverfox_duo_haetae_emerald_void",
        "korean_silverfox_duo_dragon_gold_changdeokgung",
        "korean_silverfox_duo_minhwa_obsidian_aurora",
        "korean_silverfox_duo_celadon_violet_bukhansan",
        "korean_silverfox_duo_irezumi_gold_deoksugung",
        "korean_silverfox_duo_lotus_teal_suncheon",
        "korean_silverfox_duo_dragon_crimson_namsan",
        "korean_silverfox_duo_celadon_gold_versailles",
        "korean_silverfox_duo_irezumi_teal_void",
        "korean_silverfox_duo_dancheong_crimson_busan",
        "korean_silverfox_duo_minhwa_gold_aurora",
        "korean_silverfox_duo_haetae_teal_dongdaemun",
        "korean_silverfox_duo_dragon_obsidian_gyeongbokgung",
        "korean_silverfox_duo_lotus_crimson_aurora",
        "korean_silverfox_duo_dancheong_gold_bukchon",
        "korean_silverfox_duo_dancheong_gold_void",
        "korean_silverfox_duo_irezumi_obsidian_deoksugung",
        "korean_silverfox_duo_minhwa_violet_aurora", "duo_penthouse_black", "duo_pool_wet_night", "duo_couture_sheer",
        "duo_mirror_boudoir", "duo_jungle_primal", "duo_champagne_pour", "duo_ice_bath_noir", "duo_versailles_gold", "duo_neon_cage",
    ],

    "?첑 Mirror & Reflection": [
        "infinity_mirror_goddess", "hall_of_mirrors_glam", "obsidian_mirror_ritual", "venetian_mirror_boudoir", "cheval_mirror_reveal", "broken_mirror_multiplied", "mercury_lake_reflection", "salt_flat_sky_merge",
        "rain_puddle_city_invert", "flooded_temple_mirror", "infinity_pool_edge_reflect", "morning_dew_skin_reflection", "glass_box_all_angles", "prism_light_body_split", "crystal_cave_skin_facets", "two_way_mirror_watcher",
        "window_rain_double", "soap_bubble_dome", "chrome_sphere_world", "polished_obsidian_floor", "supercar_chrome_reflect", "liquid_metal_pool", "foil_room_crush", "mirrored_skyscraper_facade",
    ],

    "?㎚ Sci-Fi & Biopunk": [
        "cryo_emergence_wet", "specimen_amber_suspended", "clean_room_latex_protocol", "gene_sequencer_data_skin", "quarantine_protocol_breach", "petri_dish_giant_macro", "abyssal_pressure_glam", "mycelium_web_consumed",
        "coral_organism_absorption", "carnivorous_plant_trap", "symbiote_second_skin", "jellyfish_bloom_float", "cyborg_partial_reveal", "neural_lace_crown", "exoskeleton_stripped", "prosthetic_art",
        "spine_tech_implant", "mutation_bloom", "toxic_spore_cloud", "infection_glam", "virus_pattern_body", "metamorphosis_editorial", "alien_host_glam",
    ],

    "?? Environment Merge": [
        "trio_bodypaint_latex_frame", "trio_bodypaint_gown_frame", "trio_bodypaint_leather_frame", "trio_animal_bodypaint_latex", "trio_klimt_bodypaint_gold_gown", "trio_galaxy_bodypaint_chrome", "duo_bodypaint_latex", "duo_bodypaint_gown",
        "duo_bodypaint_leather", "duo_bodypaint_gold_dress", "duo_animal_bodypaint_latex", "duo_klimt_bodypaint_gown", "duo_galaxy_bodypaint_chrome", "trio_latex_bodypaint_center", "trio_gown_bodypaint_center", "trio_leather_bodypaint_center",
        "trio_bikini_bodypaint_center", "trio_sheer_bodypaint_center", "trio_chrome_bodypaint_center", "merge_butterfly_fabric", "merge_floral_wallpaper", "merge_leopard_fabric", "merge_mandala_carpet", "merge_toile_pattern",
        "merge_tartan_plaid", "merge_salt_flat_sky", "merge_autumn_leaves_floor", "merge_coral_reef_water", "merge_sand_dunes", "merge_moss_stone_ground", "merge_clockwork_gears", "merge_marble_column_wall",
        "merge_islamic_tile_wall", "merge_stained_glass_window", "merge_circuit_board", "merge_klimt_gold_mural", "merge_vangogh_starry", "merge_ukiyo_wave_print", "merge_mondrian_grid", "merge_pollock_splatter",
        "merge_byzantine_mosaic",
    ],

    "?뙔 Night Glamour": [
        "club_vip_neon_goddess", "club_rooftop_citylight", "micro_sequin_club", "rooftop_micro_night",
    ],

    "?몭 Slip Dress Glamour": [
        "silk_slip_dawn_hotel", "satin_slip_vanity_noir", "satin_slip_micro",
    ],

    "?릤 Animal Print Glamour": [
        "leopard_power_editorial", "leopard_micro_studio", "snake_micro_marble", "snakeskin_latex_glam",
    ],

    "?렚 Theatrical Glamour": [
        "gyeongbokgung_night_couture", "bukchon_rain_editorial", "namsan_tower_dusk", "dongdaemun_neon_rain", "haeinsa_temple_dawn", "jeju_volcanic_coast", "fushimi_inari_crimson", "arashiyama_bamboo_mist",
        "osaka_dotonbori_neon", "mount_fuji_dawn_silk", "japanese_garden_autumn", "kabukiza_backstage_glam", "forbidden_city_golden_hour", "li_river_karst_mist", "shanghai_bund_noir", "zhangjiajie_cloud_forest",
        "west_lake_lotus_dawn", "bali_tanah_lot_sunset", "hoi_an_lantern_rain", "bangkok_wat_arun_gold", "singapore_marina_bay_night", "luang_prabang_monk_dawn", "rice_terrace_banaue_mist", "opera_house_goddess",
        "venetian_carnival_palazzo", "flamenco_tablao_fire", "broadway_red_curtain", "scottish_castle_mist", "sahara_dune_queen", "ballet_stage_noir",
    ],

    "?뙼 Minimal Object Cover": [
        "silk_ribbon_minimal", "tropical_flower_minimal", "silver_foil_minimal", "moss_stone_minimal", "crystal_geode_minimal", "black_feather_minimal", "wet_lotus_pool_minimal", "butterfly_wings_minimal",
        "seaweed_ocean_minimal", "body_chain_only_glam", "flower_body_only", "rope_art_editorial", "ribbon_wrap_glam", "crystal_body_cover", "maldives_bikini_editorial", "seaweed_coral_body",
    ],

    "?썎 Spa & Body Glamour": [
        "oil_massage_table", "mud_spa_clay", "hammam_marble_glam", "ryokan_hinoki_bath", "chocolate_spa_drip", "champagne_bubble_bath", "rose_petal_bath", "honey_drip_spa",
        "gold_leaf_spa", "salt_scrub_steam",
    ],

    "?뙅 Hot Spring & Underwater": [
        "yunoko_bamboo_onsen", "pamukkale_travertine", "bhutan_himalaya_pool", "blue_lagoon_silica", "greenland_glacier_pool", "japan_snow_onsen", "hot_spring_nude_editorial", "new_zealand_geyser",
        "costa_rica_jungle_pool",
    ],

    "?뮚 Pool & Emergence": [
        "niagara_mist_goddess", "greek_sea_emergence", "morocco_riad_pool", "lagoon_surface_break",
    ],

    "?뙢截?Wet Dress Glamour": [
        "dubai_rooftop_storm", "amalfi_cliff_storm", "santorini_aegean_storm", "venice_acqua_alta", "lisbon_rain_tiles", "kuala_lumpur_monsoon", "cape_town_atlantic_storm", "rio_corcovado_storm",
        "mumbai_monsoon_sari", "monaco_wet_silk", "bali_rain_wet", "bangkok_monsoon_silk", "new_york_rooftop_rain",
    ],

    "?렚 Archetype Glamour": [
        "bond_girl_casino", "spy_rooftop_latex", "spy_hotel_noir", "dark_queen_cliff", "villain_penthouse", "assassin_rain", "goddess_warrior", "rockstar_stage",
    ],

    "?렚 Trio Glamour": [
        "trio_glacier_emergence", "trio_colosseum_dawn", "trio_tokyo_shibuya_rain", "trio_underwater_temple", "trio_volcano_crater", "trio_opera_house_stage", "trio_desert_salt_flat", "trio_cherry_blossom_storm",
        "trio_aurora_iceland", "trio_art_museum_after_hours", "trio_penthouse_pool_dawn",
        "korean_silverfox_trio_dragon_celadon_crimson_void",
        "korean_silverfox_trio_minhwa_haetae_gold_bukchon",
        "korean_silverfox_trio_irezumi_dancheong_violet_namsan",
        "korean_silverfox_trio_dancheong_crimson_void",
        "korean_silverfox_trio_minhwa_teal_aurora",
        "korean_silverfox_trio_irezumi_celadon_violet_void",
        "korean_silverfox_trio_haetae_minhwa_emerald_bukchon",
        "korean_silverfox_trio_dragon_phoenix_obsidian_void",
        "korean_silverfox_trio_dancheong_irezumi_gold_jongmyo",
        "korean_silverfox_trio_minhwa_celadon_crimson_gyeongju",
        "korean_silverfox_trio_haetae_dragon_violet_aurora",
    ],

    "?똿 Golden Hour Glamour": [
        "golden_hour_cliff_goddess", "golden_hour_salt_flat_goddess", "golden_hour_dune_goddess", "golden_hour_wheat_field", "golden_hour_iceland_waterfall", "golden_hour_lavender_field", "golden_hour_amazon_cliff", "golden_hour_curvy_desert",
        "golden_hour_latina_wheat", "golden_hour_bust_salt_flat", "golden_hour_pear_tulip_field", "golden_hour_petite_iceland", "golden_hour_hourglass_volcano",
    ],

    "?룢截?Ancient Temple Glamour": [
        "marble_awakening_goddess", "karnak_gold_fusion", "angkor_relief_emergence", "petra_sandstone_dissolve", "ephesus_marble_split", "chichen_itza_serpent_merge", "nefertiti_gold_petrify",
    ],

    "?뭿 Figure Glamour": [
        "super_lingerie_glamour", "super_sheer_glamour", "super_slit_glamour", "super_corset_glamour", "hot_bikini_glamour", "hot_lingerie_glamour", "hot_sheer_glamour", "hot_slit_glamour",
        "hot_corset_glamour", "angel_bikini_glamour", "angel_lingerie_glamour", "angel_sheer_glamour", "angel_slit_glamour", "angel_corset_glamour", "black_bikini_glamour", "black_lingerie_glamour",
        "black_sheer_glamour", "black_slit_glamour", "black_corset_glamour", "brazil_bikini_glamour", "brazil_lingerie_glamour", "brazil_sheer_glamour", "brazil_slit_glamour", "brazil_corset_glamour",
        "latina_lingerie_glamour", "latina_sheer_glamour", "latina_slit_glamour", "latina_corset_glamour", "bust_bikini_glamour", "bust_slit_glamour", "bust_sheer_glamour", "bust_corset_glamour",
        "amazon_bikini_glamour", "amazon_lingerie_glamour", "amazon_sheer_glamour", "amazon_slit_glamour", "amazon_corset_glamour",
    ],

    "?㎠ Ferrofluid Glamour": [
        "ferrofluid_crown_spikes", "ferrofluid_latex_emergence", "ferrofluid_gown_river", "ferrofluid_spiderweb_silk", "ferrofluid_sheer_column", "ferrofluid_couture_armor", "ferrofluid_mirror_pool", "ferrofluid_plus_size_latex_column_goddess",
        "ferrofluid_amazon_couture_train_goddess", "ferrofluid_athletic_full_armor_goddess", "ferrofluid_petite_ballgown_spikes_goddess", "ferrofluid_curvy_wet_look_emergence_goddess",
    ],

    "?맔 Murmuration Glamour": [
        "murmuration_silk_gown", "murmuration_latex_cliff", "murmuration_sheer_field", "murmuration_couture_atrium", "murmuration_bodypaint_goddess", "murmuration_ruins_editorial", "murmuration_desert_goddess", "murmuration_plus_size_fur_coat_goddess",
        "murmuration_athletic_latex_goddess", "murmuration_amazon_sequin_gown_goddess", "murmuration_petite_wedding_goddess", "murmuration_curvy_trench_boots_goddess",
    ],

    "?렦 Cymatics Glamour": [
        "cymatics_water_column", "cymatics_sand_goddess", "cymatics_silk_frequency", "cymatics_latex_resonance", "cymatics_couture_wave", "cymatics_neon_pool", "cymatics_crystal_chamber", "cymatics_amazon_metallic_bodysuit_goddess",
        "cymatics_plus_size_couture_gown_frequency_goddess", "cymatics_petite_wetsuit_deep_frequency_goddess", "cymatics_curvy_mirror_dress_goddess", "cymatics_athletic_sand_body_overlay_goddess",
    ],

    "?뵮 Micro Scale Glamour": [
        "micro_spiderweb_dew_goddess", "micro_pollen_goddess", "micro_salt_crystal_goddess", "micro_feather_barb_goddess", "micro_snowflake_goddess", "micro_sand_grain_goddess", "micro_silk_fiber_goddess", "micro_amazon_space_suit_vessel_goddess",
        "micro_plus_size_crystal_cave_lattice_goddess", "micro_petite_butterfly_scale_goddess", "micro_curvy_soap_film_goddess", "micro_athletic_tardigrade_goddess",
    ],

    "?ェ Mycelium Glamour": [
        "mycelium_forest_goddess", "mycelium_silk_network", "mycelium_latex_roots", "mycelium_couture_spores", "mycelium_bodypaint_threads", "mycelium_ruins_colonized", "mycelium_glow_editorial", "mycelium_amazon_leather_armor_goddess",
        "mycelium_plus_size_haute_couture_mushroom_goddess", "mycelium_curvy_velvet_coat_goddess", "mycelium_petite_lace_communion_goddess", "mycelium_athletic_neon_bodysuit_network_goddess",
    ],

    "?뵄 Acoustic Levitation Glamour": [
        "acoustic_amazon_glass_shard_levitation", "acoustic_plus_size_water_sphere_cloud", "acoustic_petite_salt_crystal_formation", "acoustic_curvy_rose_petal_orbit", "acoustic_athletic_steel_ball_precision", "acoustic_amazon_mercury_drop_curtain", "acoustic_plus_size_golden_dust_suspension", "acoustic_petite_ink_drop_suspension",
        "acoustic_curvy_champagne_bubble_levitation", "acoustic_athletic_fire_ember_levitation", "acoustic_amazon_flower_petal_vortex", "acoustic_plus_size_ice_shard_armor",
    ],

    "?뵄 Acoustic Levitation Glamour 2": [
        "acoustic_super_glamour_diamond_dust", "acoustic_bbw_soap_bubble_galaxy", "acoustic_latina_silk_thread_web", "acoustic_bust_queen_crystal_shard", "acoustic_amazon_lightning_arc", "acoustic_vs_angel_feather_vortex", "acoustic_black_glamour_obsidian_float", "acoustic_hot_glamour_ember_silk",
        "acoustic_brazil_petal_carnival", "acoustic_supermodel_glass_bead_curtain", "acoustic_powerlifter_steel_chain", "acoustic_miniature_snow_globe",
    ],

    "?뵦 Body 횞 Element Glamour": [
        "element_super_glamour_fire_goddess", "element_bbw_water_goddess", "element_amazon_lightning_goddess", "element_petite_wind_goddess", "element_bust_queen_lava_goddess", "element_latina_storm_goddess", "element_vs_angel_ice_goddess", "element_black_glamour_void_goddess",
        "element_hot_glamour_plasma_goddess", "element_brazil_earth_goddess", "element_supermodel_aurora_goddess", "element_powerlifter_volcano_goddess",
    ],

    "?뭴 Body 횞 Luxury Setting Glamour": [
        "luxury_super_glamour_versailles", "luxury_bbw_monaco_yacht", "luxury_amazon_dubai_penthouse", "luxury_latina_rio_carnival", "luxury_bust_queen_milan_couture", "luxury_vs_angel_paris_runway", "luxury_black_glamour_nyc_rooftop", "luxury_hot_glamour_tokyo_penthouse",
        "luxury_brazil_maldives_overwater", "luxury_supermodel_london_couture", "luxury_miniature_shanghai_skyline", "luxury_powerlifter_greek_colosseum",
    ],

    "?截?Plasma & Solar Flare Glamour": [
        "plasma_amazon_solar_wind_train", "plasma_plus_size_corona_loop_goddess", "plasma_petite_prominence_pillar", "plasma_curvy_granulation_skin", "plasma_athletic_flare_eruption", "plasma_amazon_chromosphere_gown", "plasma_plus_size_sunspot_vortex", "plasma_petite_heliosphere_emergence",
        "plasma_curvy_magnetic_reconnection", "plasma_athletic_solar_minimum", "plasma_amazon_magnetosphere_armor", "plasma_plus_size_solar_flare_crown", "plasma_curvy_solar_wind_wet",
    ],

    "?뙌 Dark Fantasy Glamour": [
        "dark_super_glamour_succubus", "dark_bbw_earth_witch", "dark_bust_queen_vampire", "dark_vs_angel_fallen_angel", "dark_supermodel_ice_witch", "dark_amazon_valkyrie", "dark_miniature_shadow_fairy", "dark_latina_blood_moon",
        "dark_black_glamour_void_queen", "dark_hot_glamour_dark_siren", "dark_brazil_jungle_goddess", "dark_powerlifter_war_goddess",
    ],

    "?뙄 Bioluminescence Glamour": [
        "bio_amazon_anglerfish_lure", "bio_plus_size_jellyfish_bloom", "bio_curvy_deep_sea_coral", "bio_athletic_comb_jelly_rainbow", "bio_supermodel_sea_sparkle", "bio_bbw_giant_squid_ink", "bio_black_glamour_viper_fish", "bio_vs_angel_crystal_medusa",
        "bio_petite_firefly_swarm", "bio_latina_dinoflagellate", "bio_bust_queen_abyss_glow", "bio_powerlifter_hydrothermal",
    ],

    "?빖截?Spider Silk Glamour": [
        "silk_amazon_web_cathedral", "silk_petite_dew_drop_web", "silk_latina_web_veil", "silk_black_glamour_black_widow", "silk_vs_angel_dewdrop_cathedral", "silk_bbw_cocoon_emergence", "silk_curvy_golden_silk_gown", "silk_athletic_web_armor",
        "silk_bbw_funnel_web_throne", "silk_powerlifter_web_cage", "silk_supermodel_spiral_web", "silk_bust_queen_orb_web",
    ],

    "?뙦截?Vortex Glamour": [
        "vortex_amazon_fire_tornado", "vortex_bbw_water_cyclone", "vortex_petite_sand_devil", "vortex_curvy_rose_tornado", "vortex_athletic_lightning_vortex", "vortex_latina_petal_whirlwind", "vortex_vs_angel_snow_vortex", "vortex_powerlifter_magma_vortex",
        "vortex_bbw_cloud_column", "vortex_bust_queen_aurora_vortex", "vortex_supermodel_galaxy_spiral", "vortex_black_glamour_void_spiral",
    ],

}

from core.hof_tier import HOF_TIER  # HOF 추가는 core/hof_tier.py에서

# ── 이레즈미 + 바디글리터 프리셋 (2026-07-17 추가) ──
PRESETS_IREZUMI_GLITTER = {
    "irezumi_crane_peony_mature_luxury_monaco",
    "irezumi_crane_peony_slim_elegance_white",
    "irezumi_crane_peony_southeast_asian_beach",
    "irezumi_crane_peony_super_glam_versailles",
    "irezumi_dragon_wave_black_glam_void",
    "irezumi_dragon_wave_power_fitness_strobe",
    "irezumi_dragon_wave_slim_runway_neon",
    "irezumi_dragon_wave_sports_glam_onsen",
    "irezumi_dragon_wave_super_glam_dubai",
    "irezumi_dragon_wave_vs_angel_santorini",
    "irezumi_koi_sakura_colombian_monaco",
    "irezumi_koi_sakura_korean_void",
    "irezumi_koi_sakura_vs_angel_kyoto_rain",
    "irezumi_phoenix_chrysanthemum_ballerina_steam",
    "irezumi_phoenix_chrysanthemum_black_glam_desert",
    "irezumi_phoenix_chrysanthemum_hot_glam_riad",
    "irezumi_phoenix_chrysanthemum_latina_miami",
    "irezumi_phoenix_chrysanthemum_nordic_aurora",
    "irezumi_phoenix_chrysanthemum_vs_angel_versailles",
    "irezumi_tiger_bamboo_african_desert",
    "irezumi_tiger_bamboo_brazilian_pool",
    "irezumi_tiger_bamboo_hot_glam_neon",
    "irezumi_tiger_bamboo_sports_glam_void",
    "irezumi_tiger_bamboo_vs_angel_dubai",
    "bodyglitter_black_void_fitness",
    "bodyglitter_blue_bali_temple",
    "bodyglitter_blue_holographic_pool",
    "bodyglitter_blue_monaco_colombian",
    "bodyglitter_blue_santorini_mature",
    "bodyglitter_blue_void_runway",
    "bodyglitter_bronze_fitness_strobe",
    "bodyglitter_bronze_kyoto_rain",
    "bodyglitter_champagne_versailles_mature",
    "bodyglitter_cobalt_cape_town",
    "bodyglitter_copper_rio_carnival",
    "bodyglitter_copper_santorini_sunset",
    "bodyglitter_copper_void_milf",
    "bodyglitter_coral_rio_carnival",
    "bodyglitter_crimson_vegas_strip",
    "bodyglitter_emerald_dubai_rooftop",
    "bodyglitter_emerald_kyoto_rain",
    "bodyglitter_emerald_monaco_milf",
    "bodyglitter_gold_cape_town_black_glam",
    "bodyglitter_gold_maldives_vs_angel",
    "bodyglitter_gold_onsen_mature",
    "bodyglitter_gold_rio_carnival",
    "bodyglitter_gold_tokyo_runway",
    "bodyglitter_gold_versailles_colombian",
    "bodyglitter_gold_void_black_glam",
    "bodyglitter_green_forest_goddess",
    "bodyglitter_ice_blue_onsen_mature",
    "bodyglitter_ice_blue_paris_runway",
    "bodyglitter_ice_blue_void_ballerina",
    "bodyglitter_jade_bali_temple",
    "bodyglitter_lavender_tokyo_shibuya",
    "bodyglitter_magenta_new_york_loft",
    "bodyglitter_orange_marrakech",
    "bodyglitter_platinum_paris_rooftop",
    "bodyglitter_platinum_void_black_glam",
    "bodyglitter_purple_aurora_nordic",
    "bodyglitter_purple_marrakech_mature",
    "bodyglitter_purple_monaco_night",
    "bodyglitter_purple_void_black_glam",
    "bodyglitter_rainbow_aurora_nordic",
    "bodyglitter_rainbow_void_fitness",
    "bodyglitter_red_dubai_black_glam",
    "bodyglitter_red_marrakech_colombian",
    "bodyglitter_red_void_colombian",
    "bodyglitter_rose_gold_amalfi_ballerina",
    "bodyglitter_rose_gold_dubai_sports",
    "bodyglitter_rose_gold_maldives",
    "bodyglitter_rose_gold_versailles",
    "bodyglitter_silver_aurora_runway",
    "bodyglitter_silver_cape_town_sports",
    "bodyglitter_silver_dubai_milf",
    "bodyglitter_silver_marrakech_sports",
    "bodyglitter_silver_neon_cyberpunk",
    "bodyglitter_silver_onsen_steam",
    "bodyglitter_silver_tokyo_fitness",
    "bodyglitter_silver_versailles_runway",
    "bodyglitter_teal_amalfi_cliff",
    "bodyglitter_white_void_ballerina_korean",
}


# 2026-07-18 이레즈미 F. 뱀+연꽃 / G. 파도+후지산 신규 추가
PRESETS_IREZUMI_SNAKE_LOTUS = {
    k: {"tier": "HOF" if k in (
        "irezumi_snake_lotus_black_glam_void",
        "irezumi_snake_lotus_ballerina_paris",
        "irezumi_snake_lotus_runway_tokyo",
        "irezumi_snake_lotus_vs_angel_aurora",
    ) else "SS" if k in (
        "irezumi_snake_lotus_vs_angel_bali",
        "irezumi_snake_lotus_colombian_rio",
        "irezumi_snake_lotus_sports_cape_town",
    ) else "S"}
    for k in [
        "irezumi_snake_lotus_black_glam_void",
        "irezumi_snake_lotus_vs_angel_bali",
        "irezumi_snake_lotus_colombian_rio",
        "irezumi_snake_lotus_ballerina_paris",
        "irezumi_snake_lotus_fitness_strobe",
        "irezumi_snake_lotus_runway_tokyo",
        "irezumi_snake_lotus_milf_monaco",
        "irezumi_snake_lotus_mature_onsen",
        "irezumi_snake_lotus_sports_cape_town",
        "irezumi_snake_lotus_vs_angel_aurora",
    ]
}

PRESETS_IREZUMI_WAVE_FUJI = {
    k: {"tier": "HOF" if k in (
        "irezumi_wave_fuji_black_glam_void",
        "irezumi_wave_fuji_vs_angel_santorini",
        "irezumi_wave_fuji_runway_neon",
        "irezumi_wave_fuji_colombian_versailles",
        "irezumi_wave_fuji_fitness_strobe",
        "irezumi_wave_fuji_ballerina_aurora",
    ) else "SS" if k in (
        "irezumi_wave_fuji_sports_onsen",
    ) else "S"}
    for k in [
        "irezumi_wave_fuji_black_glam_void",
        "irezumi_wave_fuji_vs_angel_santorini",
        "irezumi_wave_fuji_runway_neon",
        "irezumi_wave_fuji_sports_onsen",
        "irezumi_wave_fuji_colombian_versailles",
        "irezumi_wave_fuji_fitness_strobe",
        "irezumi_wave_fuji_mature_kyoto",
        "irezumi_wave_fuji_ballerina_aurora",
    ]
}


# 2026-07-18 ✨ Bare Art Ensemble 카테고리 신설 (듀오 25종)
PRESETS_BARE_ART_ENSEMBLE_DUO = {
    "duo_irezumi_dragon_glitter_gold_void": {},
    "duo_irezumi_wave_glitter_indigo_santorini": {},
    "duo_irezumi_phoenix_glitter_crimson_shibuya": {},
    "duo_irezumi_koi_glitter_coral_maldives": {},
    "duo_irezumi_snake_glitter_emerald_versailles": {},
    "duo_irezumi_peacock_glitter_teal_monaco": {},
    "duo_irezumi_skull_glitter_obsidian_kyoto": {},
    "duo_irezumi_samurai_glitter_silver_tokyo": {},
    "duo_irezumi_dragon_klimt_versailles": {},
    "duo_irezumi_phoenix_vangogh_aurora": {},
    "duo_irezumi_wave_pollock_void": {},
    "duo_irezumi_koi_klimt_silver_budapest": {},
    "duo_irezumi_snake_mucha_paris": {},
    "duo_irezumi_peacock_kandinsky_monaco": {},
    "duo_irezumi_skull_dali_kyoto": {},
    "duo_glitter_gold_klimt_void": {},
    "duo_glitter_crimson_vangogh_aurora": {},
    "duo_glitter_silver_pollock_shibuya": {},
    "duo_glitter_teal_mucha_maldives": {},
    "duo_glitter_obsidian_dali_versailles": {},
    "duo_glitter_violet_kandinsky_kyoto": {},
    "duo_glitter_emerald_vangogh_budapest": {},
    "duo_irezumi_glitter_aurora": {},
    "duo_irezumi_snake_dragon_monaco": {},
    "duo_irezumi_wave_phoenix_shibuya": {},
    "duo_glitter_gold_obsidian_void": {},
    "duo_glitter_fire_ice_cape_town": {},
}


# ── Bare Art Ensemble: Trio bae1 ──────────────────────────────────────
BARE_ART_TRIO_BAE1 = {
    "trio_bae1_dragon_gold_klimt_versailles": {"name": "trio_bae1_dragon_gold_klimt_versailles", "tier": "HOF"},
    "trio_bae1_phoenix_teal_vangogh_aurora": {"name": "trio_bae1_phoenix_teal_vangogh_aurora", "tier": "HOF"},
    "trio_bae1_wave_obsidian_pollock_void": {"name": "trio_bae1_wave_obsidian_pollock_void", "tier": "HOF"},
    "trio_bae1_skull_violet_dali_monaco": {"name": "trio_bae1_skull_violet_dali_monaco", "tier": "HOF"},
    "trio_bae1_samurai_emerald_kandinsky_kyoto": {"name": "trio_bae1_samurai_emerald_kandinsky_kyoto", "tier": "SS"},
    "trio_bae1_snake_fire_dali_shibuya": {"name": "trio_bae1_snake_fire_dali_shibuya", "tier": "SS"},
}

# ── Bare Art Ensemble: Trio bae2 ──────────────────────────────────────
BARE_ART_TRIO_BAE2 = {
    "trio_bae2_phoenix_snake_violet_aurora": {"name": "trio_bae2_phoenix_snake_violet_aurora", "tier": "HOF"},
    "trio_bae2_gold_teal_obsidian_monaco": {"name": "trio_bae2_gold_teal_obsidian_monaco", "tier": "HOF"},
    "trio_bae2_crimson_emerald_silver_void": {"name": "trio_bae2_crimson_emerald_silver_void", "tier": "HOF"},
    "trio_bae2_wave_peacock_silver_versailles": {"name": "trio_bae2_wave_peacock_silver_versailles", "tier": "SS"},
    "trio_bae2_dragon_phoenix_crimson_shibuya": {"name": "trio_bae2_dragon_phoenix_crimson_shibuya", "tier": "SS"},
    "trio_bae2_skull_samurai_vangogh_kyoto": {"name": "trio_bae2_skull_samurai_vangogh_kyoto", "tier": "SS"},
    "trio_bae2_gold_violet_klimt_dali_aurora": {"name": "trio_bae2_gold_violet_klimt_dali_aurora", "tier": "SS"},
}

# ── Bare Art Ensemble: Trio bae3 ──────────────────────────────────────
BARE_ART_TRIO_BAE3 = {
    "trio_bae3_koi_samurai_emerald_aurora": {"name": "trio_bae3_koi_samurai_emerald_aurora", "tier": "HOF"},
    "trio_bae3_snake_peacock_crimson_versailles": {"name": "trio_bae3_snake_peacock_crimson_versailles", "tier": "HOF"},
    "trio_bae3_gold_silver_crimson_shibuya": {"name": "trio_bae3_gold_silver_crimson_shibuya", "tier": "HOF"},
    "trio_bae3_phoenix_skull_violet_void": {"name": "trio_bae3_phoenix_skull_violet_void", "tier": "SS"},
    "trio_bae3_teal_violet_obsidian_kyoto": {"name": "trio_bae3_teal_violet_obsidian_kyoto", "tier": "SS"},
    "trio_bae3_dragon_koi_pollock_aurora": {"name": "trio_bae3_dragon_koi_pollock_aurora", "tier": "SS"},
    "trio_bae3_wave_phoenix_vangogh_versailles": {"name": "trio_bae3_wave_phoenix_vangogh_versailles", "tier": "SS"},
}


# ── Bare Art Ensemble: Quad bae1 ──────────────────────────────────────
BARE_ART_QUAD_BAE1 = {
    "quad_bae1_dragon_gold_klimt_obsidian_void": {"name": "quad_bae1_dragon_gold_klimt_obsidian_void", "tier": "HOF"},
    "quad_bae1_koi_violet_dali_emerald_monaco": {"name": "quad_bae1_koi_violet_dali_emerald_monaco", "tier": "HOF"},
    "quad_bae1_snake_peacock_gold_silver_void": {"name": "quad_bae1_snake_peacock_gold_silver_void", "tier": "HOF"},
    "quad_bae1_gold_silver_crimson_emerald_versailles": {"name": "quad_bae1_gold_silver_crimson_emerald_versailles", "tier": "HOF"},
    "quad_bae1_dragon_wave_gold_obsidian_shibuya": {"name": "quad_bae1_dragon_wave_gold_obsidian_shibuya", "tier": "HOF"},
    "quad_bae1_phoenix_teal_vangogh_silver_aurora": {"name": "quad_bae1_phoenix_teal_vangogh_silver_aurora", "tier": "SS"},
    "quad_bae1_wave_skull_crimson_pollock_versailles": {"name": "quad_bae1_wave_skull_crimson_pollock_versailles", "tier": "SS"},
    "quad_bae1_samurai_gold_teal_vangogh_kyoto": {"name": "quad_bae1_samurai_gold_teal_vangogh_kyoto", "tier": "SS"},
    "quad_bae1_dragon_phoenix_crimson_violet_shibuya": {"name": "quad_bae1_dragon_phoenix_crimson_violet_shibuya", "tier": "SS"},
    "quad_bae1_koi_samurai_teal_pollock_aurora": {"name": "quad_bae1_koi_samurai_teal_pollock_aurora", "tier": "SS"},
    "quad_bae1_snake_gold_violet_vangogh_monaco": {"name": "quad_bae1_snake_gold_violet_vangogh_monaco", "tier": "SS"},
    "quad_bae1_phoenix_skull_emerald_silver_kyoto": {"name": "quad_bae1_phoenix_skull_emerald_silver_kyoto", "tier": "SS"},
    "quad_bae1_wave_peacock_crimson_klimt_versailles": {"name": "quad_bae1_wave_peacock_crimson_klimt_versailles", "tier": "SS"},
    "🖤 DeepBlack Trio": [
        "deepblack_trio_dragon_phoenix_tiger_void",
        "deepblack_trio_koi_dragon_phoenix_aurora",
        "deepblack_trio_dragon_celadon_phoenix_void",
        "deepblack_trio_koi_crane_phoenix_aurora",
        "deepblack_trio_dragon_goldleaf_phoenix_void",
        "deepblack_trio_tiger_uvneon_koi_void",
        "deepblack_trio_uvneon_dragon_phoenix_tiger_void",
            "deepblack_trio_crossover_dragon_phoenix_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_koi_tiger_uvneon_voidbl",
        "deepblack_trio_crossover_snake_lotus_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_crane_wave_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_peony_maple_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_dragon_wisteria_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_koi_sakura_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_phoenix_peony_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_wave_fuji_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_tiger_maple_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_dragon_phoenix_koi_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_koi_wave_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_tiger_snake_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_crane_dragon_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_phoenix_tiger_irezumi_uvneon_voidbl",
        "deepblack_trio_crossover_wisteria_crane_peony_irezumi_galaxy_uvneon_voidbl",
        "deepblack_trio_crossover_plum_chrysanthemum_bamboo_irezumi_biopunk_uvneon_voidbl",
        "deepblack_trio_crossover_lotus_sakura_maple_irezumi_aurora_uvneon_voidbl",
        "deepblack_trio_crossover_wave_peony_wisteria_irezumi_cosmos_uvneon_voidbl",
        "deepblack_trio_crossover_chrysanthemum_plum_crane_irezumi_crystal_uvneon_voidbl",
        "deepblack_trio_crossover_dragon_lotus_irezumi_holographic_uvneon_voidbl",
        "deepblack_trio_crossover_tiger_wisteria_irezumi_plasma_uvneon_voidbl",
        "deepblack_trio_crossover_koi_phoenix_irezumi_nebula_uvneon_voidbl",
        "deepblack_trio_crossover_snake_crane_irezumi_bioluminescent_uvneon_voidbl",
        "deepblack_trio_crossover_peony_bamboo_irezumi_aurora_crystal_uvneon_voidbl",
        "deepblack_trio_crossover_dragon_chrysanthemum_irezumi_ferrofluid_uvneon_voidbl",
        "deepblack_trio_crossover_phoenix_maple_irezumi_murmuration_uvneon_voidbl",
        "deepblack_trio_crossover_koi_plum_irezumi_cymatics_uvneon_voidbl",
        "deepblack_trio_crossover_tiger_lotus_irezumi_mycelium_uvneon_voidbl",
        "deepblack_trio_crossover_crane_peony_irezumi_micro_scale_uvneon_voidbl",
],

    "🦊 Silver Fox TRIO": [
        "silverfox_trio_black_koi_lotus_gold_void",
        "silverfox_trio_black_haetae_dragon_crimson_capetown",
        "silverfox_trio_black_koi_lotus_gold_bali",
        "silverfox_trio_black_haetae_phoenix_crimson_cairo",
        "silverfox_trio_black_dragon_dancheong_gold_shanghai",
        "silverfox_trio_black_tiger_crane_crimson_aurora",
        "silverfox_trio_black_phoenix_haetae_gold_angkor",
        "silverfox_trio_black_dragon_minhwa_crimson_istanbul",
        "silverfox_trio_black_phoenix_crane_gold_machu_picchu",
        "silverfox_trio_black_tiger_minhwa_crimson_void",
        "silverfox_trio_black_dragon_lotus_gold_petra",
        "silverfox_trio_black_haetae_phoenix_crimson_paris",
        "silverfox_trio_black_tiger_celadon_gold_kyoto",
        "silverfox_trio_black_dragon_haetae_crimson_rio",
        "silverfox_trio_black_phoenix_lotus_gold_void",
            "silverfox_trio_korean_crimson_lightning_dragon_peony_bioluminescent_void",
        "silverfox_trio_korean_violet_nebula_phoenix_wisteria_aurora_void",
        "silverfox_trio_korean_cyan_circuit_tiger_lotus_orange_solar_void",
        "silverfox_trio_korean_ferrofluid_phoenix_sakura_violet_nebula_void",
        "silverfox_trio_korean_aurora_crystal_koi_sakura_crimson_lightning_void",
        "silverfox_trio_korean_murmuration_phoenix_wisteria_aurora_crystal_void",
        "silverfox_trio_orange_solar_tiger_maple_bioluminescent_void",
        "silverfox_trio_latina_plasma_pink_phoenix_sakura_gold_cymatics_void",
        "silverfox_trio_aurora_crystal_dragon_peony_murmuration_void",
        "silverfox_trio_latina_crimson_lightning_koi_sakura_holographic_void",
        "silverfox_trio_bioluminescent_snake_chrysanthemum_crimson_lightning_void",
        "silverfox_trio_plasma_pink_crane_wave_holographic_void",
        "silverfox_trio_murmuration_tiger_lotus_gold_cymatics_void",
        "silverfox_trio_violet_nebula_dragon_wisteria_aurora_crystal_void",
        "silverfox_trio_crimson_lightning_dragon_peony_violet_nebula_blackbrazilian_void",
        "silverfox_trio_gold_cymatics_tiger_lotus_bioluminescent_blackscandinavian_void",
        "silverfox_trio_korean_gold_cymatics_crane_wave_mycelium_void",
        "silverfox_trio_korean_holographic_snake_chrysanthemum_gold_cymatics_void",
        "silverfox_trio_violet_nebula_crane_wave_ferrofluid_void",
        "silverfox_trio_ferrofluid_koi_maple_orange_solar_void",
],

    "🦁 Silver Fox DUO": [
        "sf_duo_lion_queen",
        "sf_duo_panther_goddess",
        "sf_duo_eagle_empress",
        "sf_duo_wolf_moon_goddess",
        "sf_duo_solar_mandala",
        "sf_duo_dragon_pearl",
        "sf_duo_phoenix_rising",
        "sf_duo_sakura_storm",
        "sf_duo_celtic_fire",
        "sf_duo_samurai_rose",
        "sf_duo_amazon_thunder",
        "sf_duo_silk_road",
        "sf_duo_ottoman_rose",
        "sf_duo_persian_fire",
        "sf_duo_hanbok_queen",
        "sf_duo_inuit_aurora",
        "sf_duo_aztec_moon",
        "sf_duo_bengal_tiger",
        "sf_duo_venetian_mask",
        "sf_duo_cambodian_apsara",
        "sf_duo_flamenco_fire",
        "sf_duo_balinese_goddess",
        "sf_duo_aztec_jaguar",
        "sf_duo_pharaoh_queen",
        "sf_duo_amazon_queen",
        "sf_duo_siberian_wolf",
        "sf_duo_aztec_eagle",
        "sf_duo_cobra_empress",
        "sf_duo_geisha_moon",
        "sf_duo_mughal_empress",
        "sf_duo_northern_star",
        "sf_duo_nile_goddess",
        "sf_duo_yoruba_goddess",
        "sf_duo_georgian_vine",
        "sf_duo_zulu_lion",
    ],

    "sf_duo_persian_jade": {"key": "sf_duo_persian_jade", "category": "🦁 Silver Fox DUO"},
    "sf_duo_berber_flame": {"key": "sf_duo_berber_flame", "category": "🦁 Silver Fox DUO"},
    "sf_duo_babylon_goddess": {"key": "sf_duo_babylon_goddess", "category": "🦁 Silver Fox DUO"},
    "sf_duo_phoenician_cedar": {"key": "sf_duo_phoenician_cedar", "category": "🦁 Silver Fox DUO"},
    "sf_duo_sheba_queen": {"key": "sf_duo_sheba_queen", "category": "🦁 Silver Fox DUO"},
    "sf_duo_carthage_queen": {"key": "sf_duo_carthage_queen", "category": "🦁 Silver Fox DUO"},
    "sf_duo_magyar_rose": {"key": "sf_duo_magyar_rose", "category": "🦁 Silver Fox DUO"},
    "sf_duo_dacian_wolf": {"key": "sf_duo_dacian_wolf", "category": "🦁 Silver Fox DUO"},
    "sf_duo_thracian_rose": {"key": "sf_duo_thracian_rose", "category": "🦁 Silver Fox DUO"},
    "sf_duo_serbian_orthodox": {"key": "sf_duo_serbian_orthodox", "category": "🦁 Silver Fox DUO"},
    "sf_duo_mayan_jaguar": {"key": "sf_duo_mayan_jaguar", "category": "🦁 Silver Fox DUO"},
    "sf_duo_polish_amber": {"key": "sf_duo_polish_amber", "category": "🦁 Silver Fox DUO"},
    "sf_duo_mesopotamian_fire": {"key": "sf_duo_mesopotamian_fire", "category": "🦁 Silver Fox DUO"},
    "sf_duo_carthage_fire": {"key": "sf_duo_carthage_fire", "category": "🦁 Silver Fox DUO"},
    "sf_duo_lebanese_rose": {"key": "sf_duo_lebanese_rose", "category": "🦁 Silver Fox DUO"},
    "sf_duo_amazon_thunder": {"key": "sf_duo_amazon_thunder", "category": "🦁 Silver Fox DUO"},
    "sf_duo_dragon_lotus": {"key": "sf_duo_dragon_lotus", "category": "🦁 Silver Fox DUO"},
    "sf_duo_nabataean_rose": {"key": "sf_duo_nabataean_rose", "category": "🦁 Silver Fox DUO"},
    "sf_duo_arabian_nights": {"key": "sf_duo_arabian_nights", "category": "🦁 Silver Fox DUO"},
    "sf_duo_bohemian_crystal": {"key": "sf_duo_bohemian_crystal", "category": "🦁 Silver Fox DUO"},
    "sf_duo_dalmatian_queen": {"key": "sf_duo_dalmatian_queen", "category": "🦁 Silver Fox DUO"},
    "sf_duo_finnish_aurora": {"key": "sf_duo_finnish_aurora", "category": "🦁 Silver Fox DUO"},
    "sf_duo_scottish_highland": {"key": "sf_duo_scottish_highland", "category": "🦁 Silver Fox DUO"},
    "sf_duo_polynesian_storm": {"key": "sf_duo_polynesian_storm", "category": "🦁 Silver Fox DUO"},
    "sf_duo_byzantine_queen": {"key": "sf_duo_byzantine_queen", "category": "🦁 Silver Fox DUO"},
    "sf_duo_anatolian_goddess": {"key": "sf_duo_anatolian_goddess", "category": "🦁 Silver Fox DUO"},
    "sf_duo_roman_goddess": {"key": "sf_duo_roman_goddess", "category": "🦁 Silver Fox DUO"},
}