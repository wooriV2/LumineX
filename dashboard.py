"""
LumineX Dashboard v4.5
����: streamlit run dashboard.py

v4.4 ������� (2026-06-07):
1. ī�װ�� ���� (B��) ? ����/�۷��� 3�з�
   - ?? �۷��� & ���Ÿ� �� ?? ���Ÿ� �۷��� (41��)
   - ?? ���� & ����ƽ �۷��� �� ����
   - ?? �� & ���� �ż� (43��)
   - ?? ����ƽ & ��Ƽ�� �ż� (26��)
2. �� ī�װ������ ���� �迭 ������ �̵� ����

v4.4.1 SS tier ���� ����� (2026-06-07):
- SS ����(S): burlesque, dominatrix_glam, corset_stockings,
  dark_fairy_erotic, tape_bondage, metal_bondage
- SS ����: military_domme (��ġ ��¡ ���� ����ũ ? ������ ���� ���� �ʿ�)
- SS tier 128 �� 121��
"""

import sys
import random
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from core.engine import list_presets, load_preset, build_prompt
from core.prompt_generator import generate_prompt_with_ai
from core.data import (
    ASPECT_RATIOS,
    MODEL_APPEARANCE, AGE_APPEARANCE, MODEL_TYPES,
    BODY_WEIGHT, BUST_SIZE, HIP_SIZE,
    OUTFIT_TYPES, MATERIALS, ENVIRONMENTS, STYLES,
    LIGHTING, CAMERA_ANGLES, FOOTWEAR, CAMERAS,
    HAIR_STYLES, HAIR_COLORS, MODEL_COUNT,
    ERA, CONCEPT, SPECIAL_EFFECTS, IMAGE_STYLE, PROPS,
    MAKEUP, ACCESSORIES, SKIN_TONES,
    POSES, WEATHER, EXPRESSION, TATTOO, BODY_OIL, BG_CROWD,
    COLOR_GRADES, MOOD, TIME_OF_DAY, LENS_EFFECT,
    TOP_TYPES, BOTTOM_TYPES,
    SKIN_DETAILS, NAILS,
    FRAMING,
    COVER_STYLES,
)
from core.combos import GOOD_COMBOS, CONFLICT_RULES, check_conflicts, get_combo_recommendations, auto_filter_check
from core.builders import build_gemini_prompt, build_chatgpt_prompt, build_midjourney_prompt, _build_wearing_line

st.set_page_config(
    page_title="LumineX Dashboard",
    page_icon="?",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ������ ī�װ���� ������ ���� ������������������������������������������������������������������
PRESET_CATEGORIES = {
    "??? �ٵ������� & ��Ų Ʈ������": [
        # ����
        "bioluminescent_ink","klimt_gold_body","vangogh_body","dali_surreal","munch_scream",
        "monet_bloom","mucha_nouveau","hokusai_wave","kandinsky_abstract","pollock_splash",
        "broken_porcelain","marble_veins","henna_goddess_body","oil_slick_body","liquid_chrome_body",
        "ink_wash_body","body_paint_art","watercolor_goddess","fresco_goddess","fresco_awakening",
        "tableau_vivant","coral_reef","leopard_dissolve","peacock_feather","snake_scale",
        "butterfly_wing","deep_ocean_map","dna_helix","star_map","neuron_network","neon_circuit",
        "topographic","maori_moko","aztec_warrior","egypt_hieroglyph","celtic_knotwork",
        "polynesian_tribal","viking_rune","inca_geometric","chinese_dragon","aboriginal_dot",
        "galaxy_skin","crystal_growth","tree_of_life","moonphase_body","shadow_lace",
        "ash_phoenix","half_statue",
        # v12
        "rembrandt_chiaroscuro","klimt_silver","matisse_cutout","mondrian_body","basquiat_street",
        "warhol_pop","lichtenstein_dot","huli_wigman","nuba_body","wodaabe_beauty","mehndi_full",
        "mayan_ritual","haida_totem","aurora_skin","crystal_mineral","tide_pool","magnetic_field",
        "cell_division",
        # v14 ? ������ �ٵ������� 35��
        "melting_chocolate","liquid_gold_drip","silver_mercury_body","ink_pour_body",
        "paint_splash_body","milk_bath_body",
        "rose_petal_body","orchid_body","vine_wrap_body","lotus_body","poison_flower",
        "fire_skin","water_ripple_body","frost_crystallize","storm_static_body","smoke_body_art",
        "lace_body_paint","fishnet_paint","chain_body_paint","jewelry_trompe_loeil","mandala_body",
        "body_calligraphy","zentangle_body","constellation_body","circuit_erotic","tarot_body",
        "moon_tattoo_body","rune_body_art","alchemy_body","henna_erotic",
        "python_scales","jaguar_spots","mermaid_scales","raven_feathers","tiger_stripes_body",
        # v15 ? ��ȭ/�۰� �ۺ�� ������ 14��
        "cezanne_body","gauguin_tropics","toulouse_lautrec","schiele_body","degas_dancer",
        "renoir_soft","botticelli_venus","titian_goddess","rubens_baroque","ingres_odalisque",
        "waterhouse_nymph","rossetti_dante","alma_tadema","vigee_lebrun",
        # v15 ? ����/�ֱ� �۰� 5��
        "keith_haring_body","yayoi_kusama","takashi_murakami",
        "jean_dubuffet","jean_cocteau",
        # v15 ? ����/��ȭ 10��
        "bodi_clay","ndebele_pattern","tuareg_indigo","mursi_lip",
        "surma_body","asaro_mudmen","kayapo_brasil","nuba_scarification","kayan_neck",
        # v15 ? ����/�ڿ� 10��
        "thermal_scan","bioluminescent_deep","microscope_pollen","xray_body","mri_scan_body",
        "neural_map","geologic_strata","crystal_lattice","solar_system_body","dna_double_helix",
        # v18 ? ���� �ٵ������� 50��
        "panther_black","cheetah_speed","snow_leopard","ocelot_wild",
        "chameleon_skin","dragon_scales_red","komodo_dragon","gecko_pattern","crocodile_skin",
        "boa_constrictor","king_cobra_hood",
        "butterfly_monarch","butterfly_morpho","dragonfly_iridescent","scarab_beetle",
        "praying_mantis","luna_moth","atlas_moth",
        "eagle_wings","flamingo_pink","owl_feather","parrot_tropical","hummingbird_iridescent",
        "phoenix_rising","swan_white","macaw_scarlet","bird_of_paradise",
        "octopus_ink","koi_fish","jellyfish_glow","seahorse_fantasy","mantis_shrimp",
        "anglerfish_deep","nudibranch_sea","cuttlefish_chromo",
        "wolf_grey","zebra_stripes","giraffe_pattern","dalmatian_spots","arctic_fox",
        "red_fox","hyena_spots",
        "koi_dragon","unicorn_opal","gryphon_feather","sphinx_cat","basilisk_scales",
        # v19 ? �ѱ� �ٵ��Ʈ 10��
        "dancheong_body","najeonchilgi_body","goryeo_celadon_body","minhwa_body",
        "korean_tiger_body","pojagi_body","taegeuk_body","silla_crown_body",
        "dansaekhwa_body","najeon_abalone",
        # v19 ? �ѱ� ����/�ż� (�ٵ��Ʈ)
        "baekhak_crane","korean_dragon_body","phoenix_jujakk",
        "baekho_white_tiger","hyeonmu_turtle","cheongnyong_dragon",
        # v19 ? �ѱ� �ڿ�/�Ĺ� �ٵ��Ʈ
        "mugunghwa_body","korean_lotus_body","korean_plum_body","korean_bamboo_body",
        # v20 ? ���� �迭 13��
        "world_map_body","topographic_body","ocean_depth_body","thermal_map_body",
        "weather_map_body","subway_map_body","europe_political_body","africa_tribes_body",
        "japan_prefecture_body","ancient_map_body","star_map_body",
        "usa_county_map_body",
        # v20 ? ����/�ڿ����� 5��
        "thermal_scan_body","circuit_board_body","galaxy_nebula_body",
        "crystal_geode_body",
        # v20 ? ����/���� 6��
        "hieroglyph_body","aztec_calendar_body","celtic_knot_body",
        "arabic_calligraphy_body","islamic_geometric_body","greek_mosaic_body",
        # v20 ? �Ĺ�/�ڿ� 3��
        "autumn_leaves_body","coral_reef_body","mushroom_forest_body",
        # v20 ? ����/���� 2��
        "stained_glass_body","bauhaus_body",
        # v20 ? ȯ������ 2��
        "urban_decay_body","forest_stone_body",
        # 2026-06-08 ī�װ�� ���� ����
        "banksy_stencil","shadow_art_nude",
        # v28 ? ����&��ȭ �ٵ������� 52�� (�ߺ� 9�� ����)
        # �Ϻ�
        "geisha_bodypaint","maiko_bodypaint","kimono_bodypaint","noh_bodypaint",
        "kabuki_bodypaint","samurai_bodypaint","geisha_white_bodypaint","ninja_bodypaint",
        # �ѱ�
        "hanbok_bodypaint","joseon_bodypaint","gisaeng_bodypaint",
        "hanbok_modern_bodypaint","korean_shaman_bodypaint",
        # �߱�
        "qipao_bodypaint","cheongsam_bodypaint","hanfu_bodypaint",
        "tang_dynasty_bodypaint","ming_bodypaint",
        # ���ƽþ�/�ߵ�
        "sari_bodypaint","belly_bodypaint","odalisque_bodypaint",
        "harem_bodypaint","mughal_bodypaint",
        "persian_bodypaint","moroccan_bodypaint","ottoman_bodypaint",
        # ������/�߾Ӿ�
        "thai_bodypaint","balinese_bodypaint","kebaya_bodypaint",
        "batik_bodypaint","ikat_bodypaint","ao_dai_bodypaint",
        "tibetan_bodypaint","shaman_bodypaint","scythian_bodypaint",
        # �Ƹ޸�ī/�����ƴϾ�
        "mayan_bodypaint","hopi_bodypaint","olmec_bodypaint",
        "maori_bodypaint","polynesian_bodypaint","haida_bodypaint",
        # ������ī
        "yoruba_bodypaint","kente_bodypaint","dashiki_bodypaint",
        "adinkra_bodypaint","zulu_bodypaint",
        # ����/���
        "scottish_bodypaint","byzantine_bodypaint","flamenco_bodypaint","dirndl_bodypaint",
        "sumerian_bodypaint","voodoo_bodypaint",
        # v23 ? ������ �ٵ������� 20�� (���� ���, �Ź� �ٸ��� ����)
        "body_paint_watercolor_free","body_paint_metallic_free","body_paint_impasto",
        "body_paint_airbrush","body_paint_ink_splatter","body_paint_drip_free",
        "body_paint_monochrome","body_paint_pastel_dream","body_paint_neon_glow",
        "body_paint_earth_tones","body_paint_jewel_tones","body_paint_iridescent_free",
        "body_paint_abstract_expressionist","body_paint_geometric_free","body_paint_organic_flow",
        "body_paint_surreal_free","body_paint_minimalist_free",
        "body_paint_blacklight","body_paint_glitter_free","body_paint_uv_reactive",
    ],
    "?? ���Ÿ� �۷���": [
        "runway_power","red_carpet","editorial_glam","golden_hour_editorial",        "noir_opulence","platinum_elite","ivory_silk","ivory_tower",
        "pearl_essence","velvet_gold","velvet_darkness","all_black_goddess","black_mirror",
        "onyx_tension","phantom_gloss","champagne_mist","couture_heat","silk_wrap","goddess_draped",
        "feather_cascade","feather_touch","golden_oil","golden_nude","gold_temptress","red_temptress",
        "petal_goddess","cobweb_drape",
        # v11
        "casino_royale","black_tie_gala","champagne_tower","fur_coat_only",
        # v16
        "plunge_gown","slit_maxi","cutout_bodysuit","sheer_overlay",
        "jeweled_bikini_top","golden_drape_goddess","crystal_gown","feather_trim_mini",
        # v21 ? ���Ÿ� �۷��� 13��
        "luxury_noir","diamond_couture","velvet_serpent","opera_glam","silver_screen",
        "lace_noir","white_silk_goddess","crystal_bodycon","penthouse_glam",
        "midnight_couture","crimson_gown","serpentine_dress","baroque_glam",
        # 2026-07-02 �ű� �߰�
        "private_pool_villa",
        "rooftop_pool_night",
        "penthouse_pool",
        "yacht_sunset_glam",
        "casino_vip_glam",
        "limo_glam",
    ],
    "?? �� & ����": [
        # ���� ���� & ����ƽ �۷���
        "lingerie_goddess","silk_robe_only","corset_queen","bodycon_power","sheer_negligee","boudoir_noir",
        "wet_silk_gown","oil_goddess_gold","pool_wet_glam","rain_soaked_dress","sweat_glam",
        "micro_dress_only","barely_covered","deep_plunge_gown","backless_extreme","one_strap_gown",
        "pinup_classic","vargas_girl","bombshell_retro","bunny_suit","playboy_glam",
        # ���Ÿ����� �̵�
        "elite_lingerie","lingerie_noir",
        # ��ġ���� �̵�
        "barely_there","wet_look_goddess","thong_bikini","micro_bikini_gold",
        "sarong_goddess","wet_bikini_pool","topless_editorial","nude_beach_art",
        "aqua_bikini","golden_summer","riviera_heat",
        # �������� �̵�
        "snow_queen_erotic","autumn_gold_sensual","christmas_boudoir","summer_solstice_glam",
        # ������/��Ƽ�� ���
        "latex_queen","pvc_goddess","leather_mistress","crystal_mesh_goddess","chain_mail_glam",
        # v21 ? �� & ���� 19��
        "fishnet_goddess","see_through_gown","wet_tshirt","string_bikini","lace_bodysuit",
        "satin_slip","velvet_corset","body_chain_only","strappy_dress","cut_out_swimsuit",
        "monokini_goddess","champagne_drip","neon_bodysuit","bikini_top_only",
        "white_linen_sheer","oil_drip_body","yoga_pants_glam","micro_skirt","halter_glam",
        # 2026-06-08 ���� ����
        "wet_editorial",
        # v27 ? �� & ���� �ű� 17��
        "pool_edge_wet",
        "ocean_wave_body",
        "penthouse_bath",
        "dressing_room_mirror",
        "silk_sheets_morning",
        "spa_private_steam",
        "bar_counter_glam",
        "vip_booth_neon",
        "after_party_suite",
        "tennis_short_dress",
        # 2026-07-02 �ű� �߰�
        "pasties_editorial",
        "body_tape_art",
        "invisible_dress",
        "painted_jeans",
        "wrap_sarong_nude",
        "ribbon_only",
        "desert_heat_nude",
        "jungle_wet_goddess",
        "sauna_nude_editorial",
        "steam_room_goddess",
        "volcanic_heat_body",
    ],
    "?? ����ƽ & ��Ƽ��": [
        # �Ŀ�&�������� �̵�
        "latex_venom","chrome_vixen","chain_goddess",
        "dominatrix_glam","bondage_fashion","strappy_harness","mesh_bodysuit","latex_catsuit",
        "oil_goddess","savage_leather",
        # �����ս����� �̵�
        "burlesque","showgirl","cabaret_star","pole_art","candy_rave",
        "lap_dance_glam","striptease_art","pole_dance_power","midnight_bath","belly_dance_glam",
        # ��Ÿ������ �̵�
        "dark_succubus","vampire_seduction","witch_sensual","dark_fairy_erotic","shadow_seductress",
        # v21 ? ����ƽ & ��Ƽ�� 16��
        "latex_catsuit_red","rubber_goddess","harness_only","rope_bondage_art",
        "vinyl_goddess","corset_stockings","catsuit_zipper","bodystocking",
        "secretary_after_hours","nurse_sensual","maid_sensual","leather_bodysuit",
        "wet_latex","fetish_boots_only","dominatrix_red","fishnet_bodysuit",
        # v22 ? ����ƽ & ��Ƽ�� ��ȭ 26��
        "transparent_dress","sheer_catsuit",
        "latex_transparent","latex_hood_full","pvc_transparent_full",
        "chrome_bodysuit","mirror_dress","liquid_metal_body",
        "suspension_art",
        "dominatrix_full_armor","goddess_throne",
        "teacher_after_class","doctor_sensual","police_dominatrix","stewardess_dark",
        "pole_dance_extreme","fire_goddess",
        "succubus_full","dark_angel_fallen","alien_queen_body",
        "body_paint_nude","micro_thong_only","tape_bondage",
        "metal_bondage","lap_dance_extreme",
        # 2026-07-02 �ű� �߰�
        "liquid_latex_drip",
        "chrome_paint_body",
        "silver_foil_body",
        "holographic_latex",
        "mirror_latex",
        "neon_latex",
    ],
    "?? �ڿ� & ����": [
        "lava_flow","ocean_surge","ice_palace","ice_refraction","frozen_latex","blizzard_queen","sandstorm_veil",
        "storm_couture","heat_shimmer","water_reflection","waterfall_goddess","rain_soaked",
        "mist_goddess","mist_vanguard","winter_forest","desert_mirage","desert_oracle",
        "desert_sand_glam","cliff_edge","arctic_minimal","dawn_awakening","aurora_drape",
        "aurora_spirit","lightning_body","solar_flare","tropical_storm",
        "smoke_veil","liquid_gold_pour","liquid_mirror","prism_light","shattered_glass","zero_gravity",
        # v11
        "volcanic_goddess","storm_lightning","deep_cave","tidal_wave",
        # v25 ? ������ �ڿ� ���
        "son_doong_jungle","waitomo_glow","dead_vlei_ghost","danxia_rainbow",
        "cenote_sacred","socotra_alien","lake_natron","namib_star_desert",
        # v26
        "zhangjiajie_avatar","pamukkale_white","plitvice_cascade","frozen_baikal",
        "rainbow_mountain","wisteria_tunnel","torres_del_paine","ha_long_bay",
        "kelimutu_crater","victoria_falls","fairy_pools","tunnel_of_love","chocolate_hills",
    ],
    "?? ���� & ����Ʈ": [
        "neon_noir","neon_dystopia","neon_rain_goddess","holographic_city","vaporwave_dream",
        "rooftop_midnight","rooftop_party","midnight_goddess","midnight_monolith","nightclub_vip",
        "monaco_nights","miami_afterglow","azure_nights","blue_hour_goddess","candlelight_noir",
        "jazz_club","jazz_age","noir_ballet","urban_vanguard","brutalist_glam","after_dark_minimal",
        "disco_goddess","music_festival","new_year_countdown","cyber_fire","cyber_silk","emerald_city",
        # v11
        "tokyo_shibuya","paris_midnight","subway_editorial","penthouse_view",
        # v25 ? ������ ����/���� ���
        "sheikh_zayed_dawn","livraria_lello_staircase","palacio_de_sal",
        # v26
        "santorini_sunset","cappadocia_balloons","chefchaouen_blue","hallstatt_lake",
        "shirakawa_snow","positano_cliff","bruges_canal","cinque_terre_harbor",
    ],
    "?? �����丮�� & ����": [
        "silhouette_only","back_beauty","collarbone_focus","neck_elegance","long_legs_focus",
        "light_driven","backlit_silk","mirror_goddess","mirror_room","eclipse_body","chrome_skin",
        "neon_body","plasma_aura","molten_chrome","mercury_rising","mercury_pool","titanium_body",
        "snowflake_skin","80s_power","y2k_chrome","bohemian_paris","origami_couture",
        # v11
        "wet_glass","smoke_studio","infrared_beauty","grain_film",
        # 2026-07-02 �ű� �߰�
        "bed_editorial",
        "floor_editorial",
        "chair_editorial",
        "door_frame_glam",
        "staircase_glam",
        "elevator_glam",
        # 2026-06-08 ���� ����
        "dreamy_soft_focus","film_noir_glam","noir_femme_fatale",
    ],
    "?? ���� & ��ȭ": [
        "cleopatra_gold","pharaoh_queen","byzantine_empress","maasai_warrior","nine_tails",
        "moonrise_ceremony","oracle_smoke","ritual_ash","ruins_goddess","renaissance_fantasy",
        "renaissance_nude","cathedral_light","baroque_punk","art_gallery","museum_glamour",
        "library_secret","living_sculpture","living_statue","sculpture_goddess","marble_goddess",
        "marble_minimal","viking_queen",
        # v11
        "sumerian_queen","ming_empress","aztec_sun_goddess","celtic_warrior_queen",
        # v17 ����
        "aphrodite_glam","artemis_huntress","freya_norse","kali_goddess",
        "isis_egypt","lakshmi_goddess","oshun_yoruba","morgan_le_fay",
        # v19 ? �ѱ� �ż�/����
        "haetae_guardian","dokkaebi_spirit","korean_tiger_spirit","gyeongbokgung_night",
        # v20 ? ���� 8��
        "union_jack_body","brazil_flag_body","usa_stars_stripes_body",
        "japan_rising_sun_body","south_africa_flag_body","india_flag_body",
        "mexico_flag_body","ukraine_flag_body",
    ],
    "?? ���� & ��������Ÿ��": [
        "flight_attendant","pilot_glamour","nurse_glamour","lawyer_power","hotel_concierge",
        "cruise_hostess","yacht_captain","yacht_club","sommelier","wine_tasting","casino_dealer",
        "private_jet","helipad","luxury_shopping","golf_glam","golf_caddie","tennis_luxe",
        "tennis_referee","f1_grid_girl","equestrian_glam","cheerleader","architect_chic",
        "fitness_power","yoga_goddess",
        # v11
        "barista_chic","gallery_curator","horse_racing","scuba_instructor",
        # v13 ������
        "ballet_prima","gymnastics_editorial","figure_skater","tennis_champion",
        "archery_goddess","carnival_rio",
    ],
    "?? ��Ÿ�� & ��ũ": [
        "dark_mermaid","vampire_queen","angel_fallen","moon_goddess","demon_goddess","forest_witch",
        "pastel_fairy","medusa_queen","halloween_queen","hologram_ghost","glitch_beauty",
        "void_emergence","void_glamour","void_secret","crystal_goddess","toxic_bloom",
        "zombie_apocalypse","dark_academia","gothic_romance","double_exposure_dark",
        "double_exposure_ethereal","oil_slick_noir",
        # v11
        "witch_ritual","fae_queen","cursed_beauty","shadow_realm",
    ],
    "?? �Ŀ� & ����": [
        "valkyrie_storm","biker_glam","shadow_play",
        "fencer_noir","martial_arts","boxing_glamour","power_curve",
        "power_suit","sculpted_power","shadow_queen","bioluminescence","bioluminescent",
    "duo_aurora_bodypaint",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_jungle_tribal_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    "duo_skeleton_bloom_bodypaint",
    "duo_odalisque_gisaeng_bodypaint",
    "trio_stone_bronze_iron_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint",
        # v11
        "riot_goddess","punk_queen","steel_warrior","cage_fighter",
    ],
    "??? ��ġ & ����Ʈ": [
        "summer_beach","surfer_goddess","pool_goddess",
        "poolside_noir","infinity_pool","beach_bonfire",
        "scuba_goddess","glass_floor","glass_house","ski_chalet","vineyard_harvest","spa_noir",
        "balcony_goddess",
        # v11
        "sunset_cruise","coral_diving","beach_bonfire_night","hammock_resort",
    ],
    "?? �����ս� & ���": [
        "flamenco_queen","tango_passion","circus_performer",
        "ribbon_dance","aerial_silk","fire_dancer","masquerade_ball",
        "opera_night","christmas_glamour","pop_art_glamour","ribbon_goddess","petal_storm",
        # v11
        "ballet_noir","broadway_diva","street_dance","drag_glamour",
        # v17
        "samba_carnival","hula_goddess","jazz_dance_glam","kathak_dance",
    ],
    "?? ���� & ��ȭ�ǻ�": [
        "geisha_noir","geisha_red","maiko_glamour","hanbok_glamour","qipao_noir","sari_goddess",
        "harem_goddess","belly_dancer","odalisque","imperial_silk",
        # v10
        "kimono_silk","ao_dai_sheer","thai_temple","indian_bridal","moroccan_kaftan",
        "persian_court","yoruba_glamour","balinese_goddess","chinese_qipao_slit","scottish_corset",
        # v17 ����
        "hanfu_goddess","cheongsam_slit","kebaya_java","dashiki_glam","kaftan_sheer",
        "flamenco_dress","dirndl_glam","hanbok_modern","ao_dai_glamour","saree_draped_sensual",
        # v19 ? �ѱ� ����/����
        "joseon_queen","joseon_consort","gisaeng_glamour","gisaeng_noir","mudang_shaman",
        "haenyeo_goddess","silla_empress","goguryeo_warrior","goryeo_empress","joseon_painter",
        "korean_shaman_fire","baekje_lotus","silla_gold_crown",
    ],
    "?? ���� & �׸�": [
        "cherry_blossom","lavender_field","spring_rain","tulip_field","autumn_forest",
        "sunflower_field","greenhouse_eden","tropical_night",
        # v10
        "first_snow","golden_autumn","midsummer_heat","rainy_season","harvest_moon",
        "winter_solstice","cherry_blossom_night","tropical_monsoon",
        # v17
        "halloween_glam","new_year_glam","sakura_night_glam","monsoon_goddess",
    ],
    "?? �� & ī����": [
        # v10
        "y2k_fairy","pink_champagne","cotton_candy","angel_baby","idol_stage","kitty_glam",
        "strawberry_milk","cherry_pop","neon_kawaii","fairy_kei",
        # v13
        "gyaru_glam","kogal_style","hime_gyaru","decora_kei","maid_glamour","visual_kei",
        "lolita_gothic","disco_barbie","space_babe","bubblegum_pop","rainbow_rave","glitter_bomb",
        "arcade_queen","virtual_idol","tokimeki_pop","kpop_idol","korean_ulzzang","kbeauty_goddess",
        "kdrama_heroine","manga_girl",
        # v19 ? K-��ó/��Ƽ
        "kpop_girl_crush","hallyu_goddess","kbeauty_glass_skin",
        "kdrama_villain_queen","kdrama_chaebol_heir","gangnam_luxury_glam",
        # 2026-06-08 ���� ����
        "bubble_tea","doll_house","harajuku_doll",
    ],

    "?? �ִ� & �۷���": [
        # v13 �Ϻ� �迭
        "zero_suit","battle_bikini","succubus_anime","catgirl_luxe","dark_magical_girl",
        "witch_apprentice","fallen_angel_anime","kunoichi_glam","oni_warrior","samurai_bride",
        "dragon_princess","android_girl","pilot_suit","neon_android","vampire_seductress",
        # v13 �۷ι� �迭
        "cosmic_warrior_glam","dark_jester_glam","poison_ivy_vines","storm_goddess",
        "dark_sorceress_glam","jessica_rabbit_glam","webtoon_heroine","manhwa_villainess",
        "barbarella_retro","vampirella_dark","ghost_shell","android_2b","street_fighter_chun",
        "dark_elsa","sailor_moon_dark",
        # v24 ? A�� �ǻ� ���� 7�� (Ư�� IP ȸ��, �Ϲ� ��ŰŸ��)
        "anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden","anime_demon_slayer",
        "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja",
        # v24 ? B�� 2D �׸�ü ���Ϸ� 2�� (�ǻ� ���� �׸�ü �׽�Ʈ ? ���� �ʿ�)
        "anime_cel_shaded","anime_webtoon_style",
    ],

    # ���� ?? �ִ� ��Ʈ��Ÿ�� (2026-06-09 �ż�, �׸�ü 32��) ����
    "?? �ִ� ��Ʈ��Ÿ��": [
        'anime_jp_90s_retro',
        'anime_jp_80s_citypop',
        'anime_jp_modern_glossy',
        'anime_jp_shoujo_soft',
        'anime_jp_shounen_action',
        'anime_jp_seinen_gritty',
        'anime_jp_makoto_watercolor',
        'anime_jp_ghibli_soft',
        'anime_jp_ecchi_glossy',
        'anime_jp_gekiga_noir',
        'anime_jp_pinup_retro',
        'anime_kr_webtoon_glossy',
        'anime_kr_romance_soft',
        'anime_kr_action_manhwa',
        'anime_kr_lezhin_mature',
        'anime_kr_pastel_dream',
        'anime_kr_lofi_chill',
        'anime_kr_noir_mature',
        'anime_cn_donghua_xianxia',
        'anime_cn_guofeng_ink',
        'anime_cn_modern_donghua',
        'anime_cn_palace_drama',
        'anime_us_cartoon_bold',
        'anime_us_comic_ink',
        'anime_us_pixar_stylized',
        'anime_us_disney_classic',
        'anime_us_pinup_classic',
        'anime_us_badgirl_comic',
        'anime_eu_ligne_claire',
        'anime_eu_graphic_novel',
        'anime_eu_erotic_bd',
        'anime_noir_silhouette',
    ],

    "?? �Ƿ翧 & ������": [
        "silhouette_spotlight_smoke",
        "silhouette_spotlight_latex",
        "silhouette_spotlight_heels",
        "silhouette_spotlight_hair",
        "silhouette_spotlight_dance",
        "silhouette_spotlight_chair",
        "silhouette_spotlight_back",
        "silhouette_spotlight_pole",
        "silhouette_window_city",
        "silhouette_window_rain",
        "silhouette_window_sheer",
        "silhouette_doorway_light",
        "silhouette_window_sunset",
        "silhouette_window_neon",
        "silhouette_neon_pink",
        "silhouette_neon_blue",
        "silhouette_neon_red",
        "silhouette_neon_purple",
        "silhouette_neon_multicolor",
        "silhouette_sunset_beach",
        "silhouette_sunset_cliff",
        "silhouette_moonlight",
        "silhouette_aurora",
        "silhouette_pool_underwater",
        "silhouette_pool_edge",
        "silhouette_bath_candle",
        "silhouette_rain_wet",
        "silhouette_fire_dark",
        "silhouette_candle_boudoir",
        "silhouette_smoke_studio",
    ],

        "?? �Ұ��� & ������": [
        "storm_eye_editorial",
        "living_fabric",
        "macro_goddess",
        "time_freeze_editorial",
        "gravity_defiance",
        "magnetic_field_goddess",
        "micro_world",
        "mirror_shatter_dress",
        "dissolution",
        "crystallization",
        "giant_flora",
        "supernova_burst",
        "portal_threshold",
        "escher_staircase",
        "aurora_embodied",
        "nebula_goddess",
        "shadow_independent",
        "negative_space",
        "flame_dress",
        "reflection_rebel",
        "time_lapse_body",
        "invisible_outline",
        "waterfall_gown",
        "cloud_couture",
        "weather_maker",
        "gravity_well",
        "double_exposure_self",
        # v25 ? ������ ������ ���
        "richat_eye","marble_caves_water",
    ],

    "??? ���� & ����": [
        "petra_rose","angkor_dawn","tikal_skyrise","bagan_balloon",
        "ellora_rock_temple","derinkuyu_underground","tigers_nest_cliff","naoshima_art_island",
        # v26
        "machu_picchu_cloud","chichen_itza_pyramid","colosseum_dusk","alhambra_palace",
        "borobudur_dawn","karnak_temple","mont_saint_michel","sigiriya_rock",
        "angkor_thom_faces","teotihuacan_pyramid","gobekli_tepe","palmyra_colonnade",
    ],

    "?? ������Ż ������": [
        "uyuni_wet_silk",
        "dead_sea_goddess",
        "iceland_hot_spring",
        "maldives_underwater",
        "niagara_wet_editorial",
        "monsoon_goddess",
        "black_sea_midnight",
    # 2026-06-21 �ڿ�&���� G1~G10 ��ü tier ��ġ

        "amazon_river_goddess",
        "lava_field_latex",
        "sahara_mirage",
        "volcano_edge_glam",
        "desert_heat_body",
        "bonfire_editorial",
        "solar_flare_goddess",
        "trolltunga_edge",
        "zhangjiajie_cloud",
        "aurora_bare",
        "skydive_editorial",
        "cliff_wind_sheer",
        "hot_air_balloon_glam",
        "antelope_light_sheer",
        "waitomo_glow_body",
        "socotra_alien_glam",
        "antarctica_ice_glam",
        "deep_jungle_goddess",
        "coral_reef_sheer",
        "salt_flat_body",
        "thunderstorm_wet",
        "northern_lights_body",
        "meteor_shower_glam",
        "pamukkale_goddess",
        "salar_atacama_flamingo",
        "bioluminescent_bay",
        "cave_waterfall_goddess",
        "red_canyon_goddess",
        "glacier_melt_goddess",
        "wave_barrel_goddess",
        "eruption_silhouette",
        "ice_cave_blue",
        "rainbow_falls_goddess",
    ],

    "?? ��Ʈ & �۷ν�": [
        # ������/Ǯ
        "pool_surface_break", "pool_underwater_up", "pool_edge_dripping",
        "infinity_pool_wet", "hot_spring_steam", "jacuzzi_bubbles",
        # 2026-07-02 �ű� �߰�
        "champagne_pour_body",
        "wine_pour_body",
        "milk_pour_body",
        "honey_pour_body",
        "gold_paint_body",
        "paint_pour_goddess",
        "neon_paint_pour",
        "shower_goddess",
        "rain_soaked_nude",
        "hot_tub_goddess",
        "foam_bath_goddess",
        "waterfall_nude",
        "ocean_nude_editorial",
        "steam_bath_goddess",
        # ��/����
        "rain_window_inside", "rain_street_soaked", "rain_studio_dramatic",
        "monsoon_body", "rain_car_window",
        # ����/�۷ν�
        "oil_pour_studio", "oil_drip_back", "honey_drip_body",
        "chocolate_pour_gloss", "gloss_lips_drip", "chrome_gloss_body",
        # ��/����
        "sweat_studio_light", "after_workout_glow", "heat_mirage_sweat", "sauna_steam_body",
        # ���/�����
        "condensation_skin", "ice_melt_drip", "dew_morning_body", "frost_breath_cold",
        # ��Ÿ ��Ʈ
        "waterfall_direct", "wave_crash_body", "wet_silk_minimal",
        "bubble_bath_gloss", "milk_bath_petals",
    ],

    "??? ��� & ��ƼŬ": [
        # ����ũ/����
        "smoke_machine_club", "dry_ice_floor", "cigarette_smoke_noir",
        "incense_smoke_ritual", "smoke_color_holi", "fog_forest_mystery",
        # �Ŀ��/����Ʈ
        "gold_dust_pour", "holi_powder_explosion", "chalk_dust_sport",
        "flour_dust_studio", "pigment_powder_art",
        # ���/��Ż
        "feather_explosion", "black_feather_dark", "petal_storm_indoor",
        "cherry_blossom_burst", "dried_flower_cascade",
        # �۸���/��ƼŬ
        "glitter_rain_studio", "gold_confetti_burst", "silver_glitter_body",
        "neon_particle_club", "bubble_floating_studio",
        # ��/����ũ
        "sparkler_night_glam", "fire_poi_dance", "ember_glow_dark", "firework_silhouette",
        # �ڿ� ��ƼŬ
        "autumn_leaves_burst", "snow_indoor_studio", "dandelion_blow",
        "firefly_night_field", "seed_pod_floating",
    ],
    "?? �ѱ� ���� & ���� �۷���": [
        # ?? �ﱹ/��� �ս�
        "silla_queen_gold", "silla_dancing_girl", "baekje_lotus_queen",
        "goguryeo_warrior_queen", "gojoseon_shaman_queen", "gaya_iron_goddess",
        "silla_hwarang_girl", "ancient_mural_goddess", "three_kingdoms_spy",
        "dongye_tribal_queen",
        # ?? ��� ����
        "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess",
        "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",
        "mongol_goryeo_queen", "goryeo_haenyeo_silk",
        # ?? ���� �ս�/����
        "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex",
        "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",
        "joseon_merchant_woman", "damo_warrior", "joseon_night_queen",
        "joseon_concubine_red", "changdeok_moonlight", "gyeongbokgung_geisha",
        # ?? ���/����
        "gisaeng_joseon_sheer", "gisaeng_red_lantern", "gisaeng_sword_dance",
        "gisaeng_haiku_bath", "gisaeng_rain_dance", "gisaeng_black_silk",
        "wonhyang_legend", "hwang_jini_glam", "gisaeng_fan_dance",
        "gisaeng_pipa_night", "gisaeng_mirror_boudoir", "pyongyang_gisaeng",
        # ?? ��ȭ & ����
        "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
        "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
        "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
        "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
        # ?? �μ� & ����ǳ��
        "haenyeo_wet_glam", "dano_festival_glam", "ganggangsullae_night",
        "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
        "jeju_shaman_sea", "korean_harvest_goddess",
        # ?? ������ & ����
        "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
        "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
        "goguryeo_fire_warrior", "joseon_spy_sheer",
        # ?? �ٴ� & ǻ��
        "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
        "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
        "hanbok_wet_editorial", "joseon_boudoir",
    ],

    "?? ��Ƽ �ٵ�������": [
        # G1 ����� ��� (2��, �ݴ� �׸� �浹/��ȭ)
        "duo_fire_and_ice_bodypaint",
        "duo_day_and_night_bodypaint",
        "duo_bloom_and_void_bodypaint",
        "duo_gold_and_shadow_bodypaint",
        "duo_ocean_and_desert_bodypaint",
        "duo_circuit_and_nature_bodypaint",
        # G1 ����� ��� �߰� (6��)
        "duo_east_and_west_bodypaint",
        "duo_macro_and_micro_bodypaint",
        "duo_ancient_and_future_bodypaint",
        "duo_poison_and_medicine_bodypaint",
        "duo_deep_sea_bodypaint",
        # G2 ����� Ʈ���� (3��, ��� ���)
        "trio_rgb_trinity_bodypaint",
        "trio_past_present_future_bodypaint",
        "trio_predator_prey_apex_bodypaint",
        "trio_ink_gold_chrome_bodypaint",
        "trio_season_trinity_bodypaint",
        # G2 ����� Ʈ���� �߰� (6��)
        "trio_sun_moon_star_bodypaint",
        "trio_three_oceans_bodypaint",
        "trio_three_civilizations_bodypaint",
        "trio_fire_water_earth_bodypaint",
        "trio_three_big_cats_bodypaint",
        # G3 ������ ��� (2��, ��ġ�� �ϳ��� ��ǰ)
        "duo_butterfly_split_bodypaint",
        "duo_yin_yang_merge_bodypaint",
        "duo_world_map_bodypaint",
        "duo_klimt_tree_bodypaint",
        "duo_galaxy_split_bodypaint",
        "duo_wave_hokusai_bodypaint",
        # G3 ������ ��� �߰� (6��)
        "duo_dna_helix_bodypaint",
        "duo_solar_eclipse_bodypaint",
        "duo_human_shadow_bodypaint",
        "duo_tiger_split_bodypaint",
        "duo_starry_night_split_bodypaint",
        "duo_peacock_split_bodypaint",
        # G4 ������ Ʈ���� (3��, ��ġ�� �Ŵ��� ��ǰ)
        "trio_triptych_klimt_bodypaint",
        "trio_phoenix_rising_bodypaint",
        "trio_world_tree_bodypaint",
        "trio_ocean_depth_bodypaint",
        "trio_aurora_spectrum_bodypaint",
        "trio_cosmic_creation_bodypaint",
        # G4 ������ Ʈ���� �߰� (6��)
        "trio_last_supper_bodypaint",
        "trio_rainbow_arc_bodypaint",
        "trio_milky_way_panorama_bodypaint",
        "trio_coral_reef_zones_bodypaint",
        "trio_creation_of_adam_bodypaint",
        "trio_poles_and_equator_bodypaint",
        # 2026-07-03 �ű� QUAD 8��
        "quad_four_civilizations_bodypaint",
        "quad_four_goddesses_bodypaint",
        "quad_four_ages_bodypaint",
        "quad_four_metals_bodypaint",
        "quad_four_gemstones_bodypaint",
        "quad_cmyk_bodypaint",
        "quad_four_classical_elements_klimt",
        "quad_four_seasons_night_bodypaint",
        # 2026-07-03 �ű� QUINT 7��
        "quint_five_senses_bodypaint",
        "quint_five_worlds_bodypaint",
        "quint_five_elements_wuxing_bodypaint",
        "quint_five_mythologies_bodypaint",
        "quint_five_oceans_deep_bodypaint",
        "quint_five_sacred_colors_bodypaint",
        "quint_five_dance_cultures_bodypaint",
        # 2026-07-03 �ű� HEXA 2��
        "hexa_rainbow_spectrum_bodypaint",
    "trio_inside_outside_bodypaint",
        "hexa_six_chakras_bodypaint",
        # 2026-07-03 �ű� OCTET 1��
        "octet_planets_solar_bodypaint",
        # 2026-07-03 �ű� ���� 4��
        "trio_inside_outside_bodypaint",        "quad_fashion_capitals_bodypaint",
                # 4�� QUAD (5��)
        "quad_four_seasons_bodypaint",
        "quad_four_elements_bodypaint",
        "quad_four_directions_bodypaint",
        "quad_four_seasons_klimt_bodypaint",
        "quad_rgba_spectrum_bodypaint",
        # 5�� QUINT (4��)
        "quint_five_continents_bodypaint",
        "quint_five_elements_asia_bodypaint",
        "quint_rainbow_five_bodypaint",
        "quint_five_oceans_bodypaint",

    # G5 ������ ��� 30�� (���� ����)
    "duo_earth_hemisphere_bodypaint",
    "duo_day_city_night_city_bodypaint",
    "duo_volcano_glacier_bodypaint",
    "duo_storm_eye_bodypaint",
    "duo_aurora_milkyway_bodypaint",
    "duo_coral_abyss_bodypaint",
    "duo_tree_root_bodypaint",
    "duo_eagle_serpent_bodypaint",
    "duo_wolf_moon_bodypaint",
    "duo_butterfly_cocoon_bodypaint",
    "duo_dragon_phoenix_bodypaint",
    "duo_lion_zebra_bodypaint",
    "duo_spider_web_bodypaint",
    "duo_mona_lisa_split_bodypaint",
    "duo_birth_venus_split_bodypaint",
    "duo_yin_yang_koi_bodypaint",
    "duo_chess_board_bodypaint",
    "duo_android_human_bodypaint",
    "duo_black_hole_star_bodypaint",
    "duo_past_future_city_bodypaint",
    "duo_virus_antibody_bodypaint",
    "duo_matrix_reality_bodypaint",
    "duo_crystal_lava_bodypaint",
    "duo_skeleton_bloom_bodypaint",
    "duo_ink_wash_split_bodypaint",
    # G6 ����� Ʈ���� 35�� (���� ����)
    "trio_stone_bronze_iron_bodypaint",
    "trio_ancient_medieval_modern_bodypaint",
    "trio_birth_life_death_bodypaint",
    "trio_seed_tree_ash_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_micro_human_macro_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    "trio_jungle_desert_tundra_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    "trio_heaven_earth_hell_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_valkyrie_siren_medea_bodypaint",
    "trio_amazon_sahara_arctic_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_love_war_peace_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint",

        # G5 ������ ��� (30��) ? �� ���� �������� �ϳ��� �ϼ�ü
        # �ڿ�/����
        "duo_earth_hemisphere_bodypaint",
        "duo_day_city_night_city_bodypaint",
        "duo_volcano_glacier_bodypaint",
        "duo_storm_eye_bodypaint",
        "duo_aurora_milkyway_bodypaint",
        "duo_coral_abyss_bodypaint",
        "duo_tree_root_bodypaint",
        # ����/����
        "duo_eagle_serpent_bodypaint",
        "duo_wolf_moon_bodypaint",
        "duo_butterfly_cocoon_bodypaint",
        "duo_dragon_phoenix_bodypaint",
        "duo_lion_zebra_bodypaint",
        "duo_spider_web_bodypaint",
        # ��ȭ/��ȭ
        "duo_mona_lisa_split_bodypaint",
        "duo_birth_venus_split_bodypaint",
        "duo_yin_yang_koi_bodypaint",
        "duo_chess_board_bodypaint",
        # SF/��Ÿ��
        "duo_android_human_bodypaint",
        "duo_black_hole_star_bodypaint",
        "duo_past_future_city_bodypaint",
        "duo_virus_antibody_bodypaint",
        "duo_matrix_reality_bodypaint",
        "duo_crystal_lava_bodypaint",
        # ��ü/ö��
        "duo_skeleton_bloom_bodypaint",
        "duo_ink_wash_split_bodypaint",
        # G6 ����� Ʈ���� (35��) ? 3 �ش��� �浹/��ȭ
        # �ð�/����
        "trio_stone_bronze_iron_bodypaint",
        "trio_ancient_medieval_modern_bodypaint",
        "trio_birth_life_death_bodypaint",
        "trio_seed_tree_ash_bodypaint",
        # ����/�ڿ�
        "trio_lightning_ocean_earthquake_bodypaint",
        "trio_sand_ice_magma_bodypaint",
        "trio_sky_earth_underground_bodypaint",
        "trio_micro_human_macro_bodypaint",
        "trio_fog_rain_snow_bodypaint",
        "trio_jungle_desert_tundra_bodypaint",
        # ��/��
        "trio_primary_colors_bodypaint",
        "trio_black_white_gray_bodypaint",
        "trio_gold_silver_bronze_bodypaint",
        "trio_sunrise_sunset_moonrise_bodypaint",
        "trio_infrared_visible_uv_bodypaint",
        # ��ȭ/����
        "trio_heaven_earth_hell_bodypaint",
        "trio_creator_preserver_destroyer_bodypaint",
        "trio_fate_three_bodypaint",
        "trio_medusa_sphinx_hydra_bodypaint",
        "trio_valkyrie_siren_medea_bodypaint",
        # ����/����
        "trio_amazon_sahara_arctic_bodypaint",
        "trio_east_west_south_bodypaint",
        "trio_viking_samurai_spartan_bodypaint",
        "trio_nile_amazon_yangtze_bodypaint",
        "trio_rome_babylon_aztec_bodypaint",
        # ����/ö��
        "trio_love_war_peace_bodypaint",
        "trio_fear_anger_joy_bodypaint",
        "trio_order_chaos_void_bodypaint",
        "trio_id_ego_superego_bodypaint",
        "trio_thesis_antithesis_synthesis_bodypaint",
    ],
    "?? ��� �۷���": [
        # G1 ��Ʈ & Ǯ
        "duo_infinity_pool_contrast",
        "duo_rain_neon_soaked",
    "duo_ink_wash_split_bodypaint",
        "duo_pool_bodypaint_micro",
        "duo_wet_glass_divide",
        # G2 �ٵ�����Ʈ ���
        "duo_bodypaint_vs_latex",
        "duo_ocean_bodypaint",
        "duo_golden_desert_bodypaint",
        "duo_aurora_bodypaint",
        "duo_cyberpunk_bodypaint",
        "duo_jungle_tribal_bodypaint",
        # G3 ���ؽ� & ���� ���
        "duo_latex_color_block",
        "duo_latex_storm_opposites",
        "duo_dark_latex_power",
        "duo_flamenco_latex_fusion",
        # G4 ���� & �׸���
        "duo_smoke_noir",
        # G5 ���Ÿ� ��
        "duo_versailles_latex_gold",
        "duo_monaco_yacht",
        "duo_champagne_gala",
        "duo_villa_italy",
        "duo_casino_power",
        # G6 ������Ż ���
        "duo_fire_and_ice",
        "duo_angel_devil",
        "duo_chrome_future",
        # G7 �Ƿ翧 & �̴ϸ�
        "duo_sunset_silhouette",
        "duo_desert_minimal",
        "duo_kpop_stage",
        "duo_penthouse_power",
        "duo_ice_bath_contrast",
    ],
    "?? �ſ� & �ݻ� �۷���": [
        # G1 Ŭ���Ĺ̷�
        "infinity_mirror_goddess",
        "hall_of_mirrors_glam",
        "obsidian_mirror_ritual",
        "venetian_mirror_boudoir",
        "cheval_mirror_reveal",
        "broken_mirror_multiplied",
        # G2 ����ݻ�
        "mercury_lake_reflection",
        "salt_flat_sky_merge",
        "rain_puddle_city_invert",
        "flooded_temple_mirror",
        "infinity_pool_edge_reflect",
        "morning_dew_skin_reflection",
        # G3 ����&������
        "glass_box_all_angles",
        "prism_light_body_split",
        "crystal_cave_skin_facets",
        "two_way_mirror_watcher",
        "window_rain_double",
        "soap_bubble_dome",
        # G4 ũ��&��Ż
        "chrome_sphere_world",
        "polished_obsidian_floor",
        "supercar_chrome_reflect",
        "liquid_metal_pool",
        "foil_room_crush",
        "mirrored_skyscraper_facade",
    ],

    "?? SF & ���̿���ũ": [
        # G1 ũ���̿�&�����
        "cryo_emergence_wet",
        "specimen_amber_suspended",
        "clean_room_latex_protocol",
        "gene_sequencer_data_skin",
        "quarantine_protocol_breach",
        "petri_dish_giant_macro",
        # G2 ����&����ü
        "abyssal_pressure_glam",
        "mycelium_web_consumed",
        "coral_organism_absorption",
        "carnivorous_plant_trap",
        "symbiote_second_skin",
        "jellyfish_bloom_float",
        # G3 Ʈ�����޸�
        "cyborg_partial_reveal",
        "neural_lace_crown",
        "exoskeleton_stripped",
        "prosthetic_art",
        "spine_tech_implant",
        "synthetic_skin_tear",
        # G4 ���̷���&�����̼�
        "mutation_bloom",
        "toxic_spore_cloud",
        "infection_glam",
        "virus_pattern_body",
        "metamorphosis_editorial",
        "alien_host_glam",
    ],

    "?? ȯ�� ��ü �ٵ�������": [
        # G1 ����/���� (6�� SSS)
        # 2026-07-02 �ٵ�������+�ǻ� �ͽ� �ݶ�
        "trio_bodypaint_latex_frame",
        "trio_bodypaint_gown_frame",
        "trio_bodypaint_leather_frame",
        "trio_animal_bodypaint_latex",
        "trio_klimt_bodypaint_gold_gown",
        "trio_galaxy_bodypaint_chrome",
        "duo_bodypaint_latex",
        "duo_bodypaint_gown",
        "duo_bodypaint_leather",
        "duo_bodypaint_gold_dress",
        "duo_animal_bodypaint_latex",
        "duo_klimt_bodypaint_gown",
        "duo_galaxy_bodypaint_chrome",
        "trio_latex_bodypaint_center",
        "trio_gown_bodypaint_center",
        "trio_leather_bodypaint_center",
        "trio_bikini_bodypaint_center",
        "trio_sheer_bodypaint_center",
        "trio_chrome_bodypaint_center",
        # ?? ȯ�� ��ü �ٵ�������
        "merge_butterfly_fabric",
        "merge_floral_wallpaper",
        "merge_leopard_fabric",
        "merge_mandala_carpet",
        "merge_toile_pattern",
        "merge_tartan_plaid",
        # G2 �ڿ�ȯ�� (5�� SSS/SS)
        "merge_salt_flat_sky",
        "merge_autumn_leaves_floor",
        "merge_coral_reef_water",
        "merge_sand_dunes",
        "merge_moss_stone_ground",
        # G3 ����/���� (5�� SSS)
        "merge_clockwork_gears",
        "merge_marble_column_wall",
        "merge_islamic_tile_wall",
        "merge_stained_glass_window",
        "merge_circuit_board",
        # G4 ����/ȸȭ (6�� SSS)
        "merge_klimt_gold_mural",
        "merge_vangogh_starry",
        "merge_ukiyo_wave_print",
        "merge_mondrian_grid",
        "merge_pollock_splatter",
        "merge_byzantine_mosaic",
    ],

}


# HOF tier ? Hall of Fame: ���� ���� �̹��� �� �ְ� ����Ƽ ����
# ����: "��" �ϴ� ����, ����/���/�ٵ������� ����� �Ϻ�, ��� ���� ����
HOF_TIER = {
    "trio_chrome_bodypaint_center",       # ũ��SF+������ ���� �Ϻ�
    "trio_gown_bodypaint_center",         # Ȳ�ݹٷ�ũ+�̺�װ��� ��������
    "trio_sheer_bodypaint_center",        # �þ�+�÷η� �ٵ������� �ֿ��
    "limo_glam",                          # ���Ÿ� �ϼ��� �ֻ�
    "yacht_sunset_glam",                  # ���+����+�ǻ� �����
    "staircase_glam",                     # ��ܱ��� �����丮�� �ϼ���
    "volcanic_heat_body",                 # ȭ���� ������
    "trio_three_civilizations_bodypaint", # 3�����+�ڹ��� ��� �Ϻ�
    "trio_ancient_medieval_modern_bodypaint", # ���3����+�ô뺰 ���� ��â�� �ְ�
    "trio_creation_of_adam_bodypaint",    # �ý�Ƽ��+��긣 ��� ������ �ϼ��� ������
    "trio_black_white_gray_bodypaint",    # �������� �ϼ��� ��/ȸ/�� ��� �е���
    "trio_fog_rain_snow_bodypaint",       # ����+���ϰ� �е��� �Ȱ�/��/�� �Ϻ�ǥ��
    # 2026-07-03 �ű� HOF ? QUAD/QUINT/HEXA ���� �Ϸ�
    "quad_four_ages_bodypaint",               # ��/��/��/ö �׶��̼� ��� �Ϻ�
    "quad_four_classical_elements_klimt",     # Ŭ��Ʈ �ݺ�Ȧ+4���� �Ϻ� ����
    "quad_four_seasons_night_bodypaint",      # 4���� ��� ����+�߰� ���� �е���
    "quint_five_senses_bodypaint",            # 5�� �ٷ�ũȦ 5�� ���� �Ϻ�
    "quint_five_worlds_bodypaint",            # 5���� ������+���� �����
    "quint_five_elements_wuxing_bodypaint",   # ����+�ڱݼ� Ȳ�ݽð� �ְ�
    "hexa_rainbow_spectrum_bodypaint",
    "trio_inside_outside_bodypaint",        # 해부학 3레이어 inside/outside HOF
}

# SSS tier ? "�̰� AI��?" ����. ��ũ�� ���� ����. 4���� �Ϻ� + ������
# ����: ü�� �������̵常���� ��ȭ/����/���� �ڵ��ϼ�, 2�� �̻� �ϰ���, ������ ����Ʈ
SSS_TIER = {
        # 2026-07-03 �ű� QUAD/QUINT/HEXA/OCTET + ���� SSS
    "quad_four_ages_bodypaint",
    "quad_four_classical_elements_klimt",
    "quad_four_seasons_night_bodypaint",
    "quint_five_senses_bodypaint",
    "quint_five_worlds_bodypaint",
    "quint_five_elements_wuxing_bodypaint",
    "hexa_rainbow_spectrum_bodypaint",
    "trio_inside_outside_bodypaint",
    "quad_four_civilizations_bodypaint",
    "quad_four_gemstones_bodypaint",
    "quad_cmyk_bodypaint",
    "quad_four_metals_bodypaint",
    "quint_five_mythologies_bodypaint",
    "quint_five_oceans_deep_bodypaint",
    "quint_five_sacred_colors_bodypaint",
    "hexa_six_chakras_bodypaint",
    "octet_planets_solar_bodypaint",
    "trio_inside_outside_bodypaint",    "quad_fashion_capitals_bodypaint",

        # 2026-07-03 �ű� SSS 52�� (�ű� 66�� ���� �Ϸ�)
    "champagne_pour_body",
    "wine_pour_body",
    "milk_pour_body",
    "honey_pour_body",
    "gold_paint_body",
    "hot_tub_goddess",
    "foam_bath_goddess",
    "pasties_editorial",
    "body_tape_art",
    "wrap_sarong_nude",
    "ribbon_only",
    "desert_heat_nude",
    "jungle_wet_goddess",
    "steam_room_goddess",
    "volcanic_heat_body",
    "liquid_latex_drip",
    "silver_foil_body",
    "holographic_latex",
    "mirror_latex",
    "private_pool_villa",
    "rooftop_pool_night",
    "penthouse_pool",
    "yacht_sunset_glam",
    "casino_vip_glam",
    "limo_glam",
    "bed_editorial",
    "floor_editorial",
    "chair_editorial",
    "door_frame_glam",
    "staircase_glam",
    "elevator_glam",
    "trio_bodypaint_latex_frame",
    "trio_bodypaint_gown_frame",
    "trio_bodypaint_leather_frame",
    "trio_animal_bodypaint_latex",
    "trio_klimt_bodypaint_gold_gown",
    "trio_galaxy_bodypaint_chrome",
    "duo_bodypaint_latex",
    "duo_bodypaint_gown",
    "duo_bodypaint_leather",
    "duo_bodypaint_gold_dress",
    "duo_animal_bodypaint_latex",
    "duo_klimt_bodypaint_gown",
    "duo_galaxy_bodypaint_chrome",
    "trio_latex_bodypaint_center",
    "trio_gown_bodypaint_center",
    "trio_leather_bodypaint_center",
    "trio_bikini_bodypaint_center",
    "trio_sheer_bodypaint_center",
    "trio_chrome_bodypaint_center",
    "invisible_dress",
    "neon_latex",

    # 2026-07-02 �����ս�&��� G3/G4 SSS (8��)
    "opera_night",
    "christmas_glamour",
    "ballet_noir",
    "broadway_diva",
    "street_dance",
    "drag_glamour",
    "ribbon_goddess",
    "petal_storm",

    # 2026-06-29 ��Ƽ �ٵ������� 57�� SSS (���� �Ϸ� 24�� Ȯ�� + 33�� ���� ����)
    # G1 ����� ��� (24�� ���� �Ϸ� SSS)
    "duo_fire_and_ice_bodypaint",
    "duo_day_and_night_bodypaint",
    "duo_bloom_and_void_bodypaint",
    "duo_gold_and_shadow_bodypaint",
    "duo_ocean_and_desert_bodypaint",
    "duo_circuit_and_nature_bodypaint",
    # G2 ����� Ʈ����
    "trio_rgb_trinity_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_predator_prey_apex_bodypaint",
    "trio_ink_gold_chrome_bodypaint",
    "trio_season_trinity_bodypaint",
    # G3 ������ ���
    "duo_butterfly_split_bodypaint",
    "duo_yin_yang_merge_bodypaint",
    "duo_world_map_bodypaint",
    "duo_galaxy_split_bodypaint",
    "duo_wave_hokusai_bodypaint",
    # G3 SS (���� ���� �̴�)
    # "duo_klimt_tree_bodypaint",  # SS ����
    # G4 ������ Ʈ����
    "trio_triptych_klimt_bodypaint",
    "trio_phoenix_rising_bodypaint",
    "trio_world_tree_bodypaint",
    "trio_ocean_depth_bodypaint",
    "trio_aurora_spectrum_bodypaint",
    "trio_cosmic_creation_bodypaint",
    # G1 �߰� (���� ����)
    "duo_east_and_west_bodypaint",
    "duo_macro_and_micro_bodypaint",
    "duo_ancient_and_future_bodypaint",
    "duo_poison_and_medicine_bodypaint",
    "duo_deep_sea_bodypaint",
    # G2 �߰� (���� ����)
    "trio_sun_moon_star_bodypaint",
    "trio_three_oceans_bodypaint",
    "trio_three_civilizations_bodypaint",
    "trio_fire_water_earth_bodypaint",
    "trio_three_big_cats_bodypaint",
    # G3 �߰� (���� ����)
    "duo_dna_helix_bodypaint",
    "duo_solar_eclipse_bodypaint",
    "duo_human_shadow_bodypaint",
    "duo_tiger_split_bodypaint",
    "duo_starry_night_split_bodypaint",
    "duo_peacock_split_bodypaint",
    # G4 �߰� (���� ����)
    "trio_last_supper_bodypaint",
    "trio_rainbow_arc_bodypaint",
    "trio_milky_way_panorama_bodypaint",
    "trio_coral_reef_zones_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_poles_and_equator_bodypaint",
    # QUAD 4�� (���� ����)
    "quad_four_seasons_bodypaint",
    "quad_four_elements_bodypaint",
    "quad_four_directions_bodypaint",
    "quad_four_seasons_klimt_bodypaint",
    "quad_rgba_spectrum_bodypaint",
    # QUINT 5�� (���� ����)
    "quint_five_continents_bodypaint",
    "quint_five_elements_asia_bodypaint",
    "quint_rainbow_five_bodypaint",
    "quint_five_oceans_bodypaint",

    # G5 ������ ��� 30�� (���� ����)
    "duo_earth_hemisphere_bodypaint",
    "duo_day_city_night_city_bodypaint",
    "duo_volcano_glacier_bodypaint",
    "duo_storm_eye_bodypaint",
    "duo_aurora_milkyway_bodypaint",
    "duo_coral_abyss_bodypaint",
    "duo_tree_root_bodypaint",
    "duo_eagle_serpent_bodypaint",
    "duo_wolf_moon_bodypaint",
    "duo_butterfly_cocoon_bodypaint",
    "duo_dragon_phoenix_bodypaint",
    "duo_lion_zebra_bodypaint",
    "duo_spider_web_bodypaint",
    "duo_mona_lisa_split_bodypaint",
    "duo_birth_venus_split_bodypaint",
    "duo_yin_yang_koi_bodypaint",
    "duo_chess_board_bodypaint",
    "duo_android_human_bodypaint",
    "duo_black_hole_star_bodypaint",
    "duo_past_future_city_bodypaint",
    "duo_virus_antibody_bodypaint",
    "duo_matrix_reality_bodypaint",
    "duo_crystal_lava_bodypaint",
    "duo_skeleton_bloom_bodypaint",
    "duo_ink_wash_split_bodypaint",
    # G6 ����� Ʈ���� 35�� (���� ����)
    "trio_stone_bronze_iron_bodypaint",
    "trio_ancient_medieval_modern_bodypaint",
    "trio_birth_life_death_bodypaint",
    "trio_seed_tree_ash_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_micro_human_macro_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    "trio_jungle_desert_tundra_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    "trio_heaven_earth_hell_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_valkyrie_siren_medea_bodypaint",
    "trio_amazon_sahara_arctic_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_love_war_peace_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint",
    # ��� �۷��� SS (SSS 23�� + SS���� 5��)
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_aurora_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    "duo_versailles_latex_gold",
    "duo_champagne_gala",
    "duo_casino_power",
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    "duo_sunset_silhouette",
    "duo_desert_minimal",
    "duo_kpop_stage",
    "duo_penthouse_power",
    "duo_rain_neon_soaked",
    "duo_ink_wash_split_bodypaint",
    "duo_jungle_tribal_bodypaint",
    "duo_monaco_yacht",
    "duo_villa_italy",
    "duo_ice_bath_contrast",
    # ��� �۷��� SSS (23��)
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_aurora_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    "duo_versailles_latex_gold",
    "duo_champagne_gala",
    "duo_casino_power",
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    "duo_sunset_silhouette",
    "duo_desert_minimal",
    "duo_kpop_stage",
    "duo_penthouse_power",
    # 2026-06-20 ����&��������Ÿ�� SS���� 10�� + SSS 24�� ����
    # SS����
    "cruise_hostess", "yacht_club",
    "nurse_glamour", "sommelier", "wine_tasting", "barista_chic",
    "golf_caddie", "fitness_power", "scuba_instructor", "archery_goddess",
    # SSS�� SS�� ���� (��Ģ)
    "flight_attendant", "pilot_glamour", "yacht_captain",
    "private_jet", "helipad", "hotel_concierge",
    "lawyer_power", "architect_chic", "casino_dealer", "gallery_curator",
    "golf_glam", "tennis_luxe", "tennis_referee", "tennis_champion",
    "f1_grid_girl", "equestrian_glam", "horse_racing", "yoga_goddess",
    "cheerleader", "ballet_prima", "gymnastics_editorial",
    "figure_skater", "carnival_rio", "luxury_shopping",

    # 2026-06-20 ����&��������Ÿ�� SSS 24�� Ȯ��
    # A�׷� ? �װ�/�ؾ�/���Ÿ�
    "flight_attendant", "pilot_glamour", "yacht_captain",
    "private_jet", "helipad", "hotel_concierge",
    # B�׷� ? ������
    "lawyer_power", "architect_chic", "casino_dealer", "gallery_curator",
    # C�׷� ? ������/��Ʈ�Ͻ�
    "golf_glam", "tennis_luxe", "tennis_referee", "tennis_champion",
    "f1_grid_girl", "equestrian_glam", "horse_racing", "yoga_goddess",
    # D�׷� ? �����ս�/������2
    "cheerleader", "ballet_prima", "gymnastics_editorial",
    "figure_skater", "carnival_rio", "luxury_shopping",

    "body_paint_nude",
    # 2026-06-11 ��� ������ SSS Ȯ�� (1��)
    "cenote_sacred",         # ���� ���� ���� + ���޶��� �ݻ�, 4�� �ϰ���
    "tikal_skyrise",         # ���� �� �Ƕ�̵� + ���� + ���ƿ� ����
    "angkor_dawn",           # ���� �ݻ� + Ȳ�� ���� + ũ�޸� ����, ���� ��������
    "waitomo_glow",          # �����߱� ���ϼ� õ�� + ���� �ݻ�, ������ ���־�
    # 2026-06-11 ��� ������ SSS Ȯ�� (2��)
    "marble_caves_water",    # �븮�� ���� + �������� ����, �ǻ��� ���� ���
    "bagan_balloon",         # ���ⱸ + Ȳ�� ���� + ��ž ���, 4��� �Ϻ�
    "tigers_nest_cliff",     # ���� ������ + �⵵ ��� + ������� ����
    "sheikh_zayed_dawn",     # �� �� + ������ũ �ٴ� + �ݻ� ���� + ���ƿ�
    "livraria_lello_staircase", # �׶���Ÿ �巹�� + ���� ��� + �����ε�۶� 3�� ����ȭ
    "namib_star_desert",     # ���ϼ� ��ġ + �籸 �ɼ� + ������ ����
    "ellora_rock_temple",    # ���� ���� �� + �׶���Ÿ �巹�� ���� ��ȭ
    # 2026-06-13 v26 ���� ���帶ũ SSS Ȯ��
    "positano_cliff",
    "bruges_canal",
    "colosseum_dusk",
    "alhambra_palace",
    "mont_saint_michel",
    "sigiriya_rock",
    "angkor_thom_faces",
    "teotihuacan_pyramid",
    "palmyra_colonnade",

    # 2026-06-19 �ִϾ�Ʈ��Ÿ�� SSS 31�� Ȯ��
    "anime_jp_90s_retro",
    "anime_jp_80s_citypop",
    "anime_jp_modern_glossy",
    "anime_jp_shoujo_soft",
    "anime_jp_shounen_action",
    "anime_jp_seinen_gritty",
    "anime_jp_makoto_watercolor",
    "anime_jp_ghibli_soft",
    "anime_jp_gekiga_noir",
    "anime_jp_pinup_retro",
    "anime_kr_webtoon_glossy",
    "anime_kr_romance_soft",
    "anime_kr_action_manhwa",
    "anime_kr_lezhin_mature",
    "anime_kr_pastel_dream",
    "anime_kr_lofi_chill",
    "anime_kr_noir_mature",
    "anime_cn_donghua_xianxia",
    "anime_cn_guofeng_ink",
    "anime_cn_modern_donghua",
    "anime_cn_palace_drama",
    "anime_us_cartoon_bold",
    "anime_us_comic_ink",
    "anime_us_pixar_stylized",
    "anime_us_disney_classic",
    "anime_us_pinup_classic",
    "anime_us_badgirl_comic",
    "anime_eu_ligne_claire",
    "anime_eu_graphic_novel",
    "anime_eu_erotic_bd",
    "anime_noir_silhouette",

    # 2026-06-18 ��&���� SSS Ȯ��
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
    "spa_private_steam", "bar_counter_glam", "after_party_suite", "tennis_short_dress",
    # 2026-06-13 v27 ��&���� SSS Ȯ��
    "dressing_room_mirror",
    "vip_booth_neon",
    # 2026-06-13 ��ġ&����Ʈ SSS Ȯ��
    "infinity_pool",
    "scuba_goddess",
    "spa_noir",
    "sunset_cruise",
    # 2026-06-14 ��&ī���� SSS Ȯ��
    "cherry_pop",
    "hime_gyaru",
    "decora_kei",
    "lolita_gothic",
    "space_babe",
    "arcade_queen",
    "virtual_idol",
    "kdrama_villain_queen",
    "bubble_tea",
    "doll_house",
    # 2026-06-15 harajuku_doll SSS �°� (��&ī���� ? ���ɽ�Ÿ �Ÿ� ��ũ 4�� ����)
    "harajuku_doll",
    # 2026-06-15 greenhouse_eden SSS �°� (����&�׸� ? �ٻ�� �巹��=�½� ���°� ���� 6�� ����)
    "greenhouse_eden",
    # 2026-06-15 ����&�׸� SSS 3�� Ȯ��
    "halloween_glam",       # �ǻ�+���+��ǰ = ��� ����� ���� ����, 6�� ����
    "new_year_glam",        # �巹�� ���� = ����+����Ƽ �� ���, Ÿ�ӽ����� 4�� ����
    "sakura_night_glam",    # �巹�� �÷η� = ���� �ͳ� ���� ����, �Ż� ��� 6�� ����
    # 2026-06-15 �����丮��&���� SSS 8�� Ȯ��
    "backlit_silk",         # ���� ���� �� �巹��=����, waitomo_glow ��� ����
    "mirror_room",          # �ǹ���Ʈ+�ſ�� ��� �Ҹ�, dressing_room_mirror���� ����
    "eclipse_body",         # �巹��=�ڷγ� �߱�, ��������=�ǻ�
    "plasma_aura",          # �ö��=�ǻ� ���� ����, ������=�巹�� (�̹���6 ����)
    "molten_chrome",        # �뱤��+��� ũ�� ������ ����, ����=ȯ��
    "mercury_pool",         # ���� ��ü=���� ��ü ���Ӽ�, �ǻ�=��ü
    "snowflake_skin",       # ���̽� �巹��=���� ���� ��ȭ (�̹���5 ����)
    "noir_femme_fatale",    # ���+5��� ����� ���� ����, halloween_glam ���� ���

    # v28 ���빮ȭ �ٵ������� ��ġ (48��)
    # 1�� SSS
    "kabuki_bodypaint",
    "joseon_bodypaint",
    "tibetan_bodypaint",
    "byzantine_bodypaint",
    "mayan_bodypaint",
    # 2�� SSS
    "geisha_bodypaint",
    "ming_bodypaint",
    "thai_bodypaint",
    "ottoman_bodypaint",
    "flamenco_bodypaint",
    "sumerian_bodypaint",
    # 3�� SSS
    "maori_bodypaint",
    "balinese_bodypaint",
    "persian_bodypaint",
    "mughal_bodypaint",
    "hopi_bodypaint",
    "haida_bodypaint",
    # 4�� SSS
    "polynesian_bodypaint",
    "korean_shaman_bodypaint",
    "noh_bodypaint",
    "hanbok_bodypaint",
    "tang_dynasty_bodypaint",
    # 5�� SSS
    "moroccan_bodypaint",
    "batik_bodypaint",
    "ikat_bodypaint",
    "dirndl_bodypaint",
    "ninja_bodypaint",
    "kebaya_bodypaint",
    "scottish_bodypaint",
    # 6�� SSS
    "voodoo_bodypaint",
    "scythian_bodypaint",
    "olmec_bodypaint",
    "odalisque_bodypaint",
    "harem_bodypaint",
    "shaman_bodypaint",
    # 7�� SSS
    "kimono_bodypaint",
    "samurai_bodypaint",
    "geisha_white_bodypaint",
    "hanfu_bodypaint",
    "qipao_bodypaint",
    "cheongsam_bodypaint",
    "gisaeng_bodypaint",
    "hanbok_modern_bodypaint",
    # 8�� SSS
    "ao_dai_bodypaint",
    "zulu_bodypaint",
    "kente_bodypaint",
    "dashiki_bodypaint",
    "belly_bodypaint",

    # v28 ���빮ȭ �ٵ������� ��ġ (3��)
    # SS ����
    "sari_bodypaint",
    "yoruba_bodypaint",
    "maiko_bodypaint",
    # 2026-06-16 �ִ�&�۷��� SSS Ȯ�� (17��)
    "kunoichi_glam",
    "samurai_bride",
    "oni_warrior",
    "cosmic_warrior_glam",
    "dragon_princess",
    "dark_sorceress_glam",
    "neon_android",
    "android_2b",
    "vampire_seductress",
    "vampirella_dark",
    "manhwa_villainess",
    "dark_elsa",
    "anime_battle_angel",
    "poison_ivy_vines",
    "storm_goddess",
    "jessica_rabbit_glam",
    "barbarella_retro",
    "monaco_nights",
    "candlelight_noir",
    "jazz_club",
    "noir_ballet",
    "brutalist_glam",
    "new_year_countdown",
    "emerald_city",
    "tokyo_shibuya",
    "paris_midnight",
    "penthouse_view",
    "palacio_de_sal",
    "chefchaouen_blue",
    "hallstatt_lake",
    "shirakawa_snow",
    "azure_nights",
    "blue_hour_goddess",
    "jazz_age",
    "disco_goddess",
    "urban_vanguard",
    "music_festival",
    "subway_editorial",
    "santorini_sunset",
    "cappadocia_balloons",
    # 2026-06-18 ������Ż ������ SS Ȯ�� (SSS ����)
    "uyuni_wet_silk", "maldives_underwater", "bioluminescent_bay", "rainbow_falls_goddess",
    "trolltunga_edge", "zhangjiajie_cloud", "cliff_wind_sheer", "skydive_editorial",
    "hot_air_balloon_glam", "wave_barrel_goddess", "glacier_melt_goddess",
    "sahara_mirage", "salt_flat_body", "salar_atacama_flamingo", "pamukkale_goddess", "red_canyon_goddess",
    "lava_field_latex", "solar_flare_goddess",
    "aurora_bare", "antarctica_ice_glam", "meteor_shower_glam", "ice_cave_blue",
    "antelope_light_sheer", "waitomo_glow_body", "coral_reef_sheer", "black_sea_midnight",
    # SS ����
    "niagara_wet_editorial", "thunderstorm_wet", "cave_waterfall_goddess",
    "desert_heat_body",
    "volcano_edge_glam", "bonfire_editorial", "eruption_silhouette", "amazon_river_goddess",
    "iceland_hot_spring", "northern_lights_body", "dead_sea_goddess",
    "socotra_alien_glam", "deep_jungle_goddess", "monsoon_goddess",
    # 2026-06-18 ������Ż ������ ī�װ�� SSS Ȯ��
    # G1 ��/����
    "uyuni_wet_silk",        # SS��SSS �±� (��ϻ� �ǻ�+������ �ұݻ縷 ���� ����)
    "maldives_underwater",
    "bioluminescent_bay",
    "rainbow_falls_goddess",
    # G2 ���� �ڿ� (���� SSS)
    "trolltunga_edge",
    "zhangjiajie_cloud",
    "cliff_wind_sheer",
    "skydive_editorial",
    "hot_air_balloon_glam",
    "wave_barrel_goddess",
    "glacier_melt_goddess",
    # G3 �縷/����
    "sahara_mirage",
    "salt_flat_body",
    "salar_atacama_flamingo",
    "pamukkale_goddess",
    "red_canyon_goddess",
    # G4 ȭ��/��/�¾�
    "lava_field_latex",      # SS��SSS �±�
    "solar_flare_goddess",
    # G5 ����/���ζ�/����
    "aurora_bare",           # SS��SSS �±�
    "antarctica_ice_glam",
    "meteor_shower_glam",
    "ice_cave_blue",
    # G6 �̱�/����/�����߱�
    "antelope_light_sheer",  # SS��SSS �±�
    "waitomo_glow_body",
    "coral_reef_sheer",
    "black_sea_midnight",

    # 2026-06-24 �Ŀ�&���� SSS 16��
    "valkyrie_storm",
    "fencer_noir",
    "martial_arts",
    "boxing_glamour",
    "cage_fighter",
    "biker_glam",
    "riot_goddess",
    "punk_queen",
    "steel_warrior",
    "power_suit",
    "shadow_play",
    "power_curve",
    "sculpted_power",
    "shadow_queen",
    "bioluminescence",
    "bioluminescent",
    "duo_aurora_bodypaint",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_jungle_tribal_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    "duo_skeleton_bloom_bodypaint",
    "duo_odalisque_gisaeng_bodypaint",
    "trio_stone_bronze_iron_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint",

    # 2026-06-24 �����ս�&��� G1+G2 SSS 11��
    "flamenco_queen",
    "tango_passion",
    "ribbon_dance",
    "aerial_silk",
    "kathak_dance",
    "hula_goddess",
    "circus_performer",
    "fire_dancer",
    "masquerade_ball",
    "samba_carnival",
    "jazz_dance_glam",
    # 2026-06-25 ���&��ƼŬ 30�� SSS
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
    # 2026-06-25 ����ƽ&��Ƽ�� G1 SSS 8��
    "latex_venom", "latex_catsuit", "latex_catsuit_red", "pvc_transparent_full",
    "latex_hood_full", "latex_transparent", "vinyl_goddess", "rubber_goddess",
    # 2026-06-25 ����ƽ&��Ƽ�� G2 SSS 7��
    "chrome_vixen", "chain_goddess", "savage_leather", "leather_bodysuit",
    "chrome_bodysuit", "mirror_dress", "liquid_metal_body",

    # 2026-06-28 �ѱ� ����&���� �۷��� G1~G4 + G5���ݺ� SSS
    # G1 �ﱹ/��� ? SSS 5��
    "silla_queen_gold", "baekje_lotus_queen", "gojoseon_shaman_queen",
    "gaya_iron_goddess", "ancient_mural_goddess",
    # G2 ��� ���� ? SSS 7��
    "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess",
    "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",
    "mongol_goryeo_queen",
    # G3 ���� �ս�/���� ? SSS 11��
    "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex",
    "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",
    "damo_warrior", "joseon_night_queen", "joseon_concubine_red",
    "changdeok_moonlight", "gyeongbokgung_geisha",
    # G4 ���/���� ? SSS 10��
    "gisaeng_joseon_sheer", "gisaeng_red_lantern", "gisaeng_sword_dance",
    "gisaeng_rain_dance", "gisaeng_black_silk", "wonhyang_legend",
    "hwang_jini_glam", "gisaeng_fan_dance", "gisaeng_pipa_night",
    "pyongyang_gisaeng",
    # G5 ��ȭ&���� ���ݺ� ? SSS 6��
    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
    # G5 ��ȭ&���� �Ĺݺ� ? SSS 6��
    "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
    "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
    # G6 �μ�&����ǳ�� ? SSS 7�� (haenyeo_wet_glam�� SS ����)
    "dano_festival_glam", "ganggangsullae_night",
    "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
    "jeju_shaman_sea", "korean_harvest_goddess",
    # G7 ������&���� ? SSS 8��
    "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
    "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
    "goguryeo_fire_warrior", "joseon_spy_sheer",
    # G8 �ٴ�&ǻ�� ? SSS 8��
    "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
    "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
    "hanbok_wet_editorial", "joseon_boudoir",

    # 2026-06-26 ����ƽ&��Ƽ�� G3~G12 SSS 51��
    # G3 �ϳ׽�/������
    "bondage_fashion", "strappy_harness", "harness_only", "rope_bondage_art",
    "suspension_art", "tape_bondage", "metal_bondage",
    # G4 �޽�/�ý���
    "mesh_bodysuit", "bodystocking", "fishnet_bodysuit", "transparent_dress",
    "sheer_catsuit", "catsuit_zipper", "pvc_transparent_full",
    # G5 ���̳�Ʈ����
    "dominatrix_glam", "dominatrix_full_armor", "dominatrix_red",
    "goddess_throne", "pole_art",
    # G6 �����ս�/���
    "burlesque", "showgirl", "cabaret_star", "candy_rave",
    "lap_dance_glam", "lap_dance_extreme", "striptease_art",
    # G7 ��/���/�轺
    "pole_dance_power", "pole_dance_extreme", "midnight_bath", "belly_dance_glam",
    # G8 ��Ÿ��/��ũ
    "dark_succubus", "vampire_seduction", "witch_sensual",
    "dark_fairy_erotic", "shadow_seductress", "succubus_full",
    # G9 ��ũ����/SF
    "dark_angel_fallen", "alien_queen_body", "fire_goddess",
    # G10 ���� ��Ÿ��
    "secretary_after_hours", "nurse_sensual", "maid_sensual",
    "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",
    # G11 �ٵ�/�̴ϸ�
    "oil_goddess", "micro_thong_only", "fetish_boots_only",
    # G12 �ڸ���
    "corset_stockings",


    # 2026-06-24 ��Ÿ��&��ũ 26�� ���� SSS
    "dark_mermaid","vampire_queen","angel_fallen","moon_goddess","demon_goddess","forest_witch",
    "pastel_fairy","medusa_queen","halloween_queen","hologram_ghost","glitch_beauty",
    "void_emergence","void_glamour","void_secret","crystal_goddess","toxic_bloom",
    "zombie_apocalypse","dark_academia","gothic_romance","double_exposure_dark",
    "double_exposure_ethereal","oil_slick_noir",
    "witch_ritual","fae_queen","cursed_beauty","shadow_realm",

    # 2026-06-24 �Ƿ翧&������ 30�� ���� SSS
    # G1 ����Ʈ����Ʈ
    "silhouette_spotlight_smoke","silhouette_spotlight_latex","silhouette_spotlight_heels",
    "silhouette_spotlight_hair","silhouette_spotlight_dance","silhouette_spotlight_chair",
    "silhouette_spotlight_back","silhouette_spotlight_pole",
    # G2 â��/����
    "silhouette_window_city","silhouette_window_rain","silhouette_window_sheer",
    "silhouette_doorway_light","silhouette_window_sunset","silhouette_window_neon",
    # G3 �׿� �Ƿ翧
    "silhouette_neon_pink","silhouette_neon_blue","silhouette_neon_red",
    "silhouette_neon_purple","silhouette_neon_multicolor",
    # G4 �ڿ���
    "silhouette_sunset_beach","silhouette_sunset_cliff","silhouette_moonlight","silhouette_aurora",
    # G5 ����/��
    "silhouette_pool_underwater","silhouette_pool_edge",
    # G6 �ǳ�/������
    "silhouette_bath_candle","silhouette_rain_wet","silhouette_fire_dark",
    "silhouette_candle_boudoir","silhouette_smoke_studio",

    # 2026-06-24 ��Ʈ&�۷ν� SSS 29��
    # G1 Ǯ/������
    "pool_surface_break","pool_underwater_up","pool_edge_dripping","infinity_pool_wet",
    "hot_spring_steam","jacuzzi_bubbles",
        # 2026-07-02 �ű� �߰�
        "champagne_pour_body",
        "wine_pour_body",
        "milk_pour_body",
        "honey_pour_body",
        "gold_paint_body",
        "paint_pour_goddess",
        "neon_paint_pour",
        "shower_goddess",
        "rain_soaked_nude",
        "hot_tub_goddess",
        "foam_bath_goddess",
        "waterfall_nude",
        "ocean_nude_editorial",
        "steam_bath_goddess",
    # G2 ��/����
    "rain_window_inside","rain_street_soaked","rain_studio_dramatic","monsoon_body","rain_car_window",
    # G3 ����/�۷ν� �帳
    "oil_pour_studio","oil_drip_back","honey_drip_body","chocolate_pour_gloss",
    "gloss_lips_drip","chrome_gloss_body",
    # G4 ��/����
    "sweat_studio_light","heat_mirage_sweat","sauna_steam_body",
    # G5 ���/�ñ�
    "condensation_skin","ice_melt_drip","dew_morning_body","frost_breath_cold",
    # G6 ��Ÿ ��Ʈ
    "waterfall_direct","wave_crash_body","wet_silk_minimal",
    "bubble_bath_gloss","milk_bath_petals",
}

# SS tier
SS_TIER = {
        # 2026-07-03 �ű� QUAD/QUINT/HEXA/OCTET SS ��ü
    "quad_four_ages_bodypaint",
    "quad_four_classical_elements_klimt",
    "quad_four_seasons_night_bodypaint",
    "quint_five_senses_bodypaint",
    "quint_five_worlds_bodypaint",
    "quint_five_elements_wuxing_bodypaint",
    "hexa_rainbow_spectrum_bodypaint",
    "trio_inside_outside_bodypaint",
    "quad_four_civilizations_bodypaint",
    "quad_four_gemstones_bodypaint",
    "quad_cmyk_bodypaint",
    "quad_four_metals_bodypaint",
    "quint_five_mythologies_bodypaint",
    "quint_five_oceans_deep_bodypaint",
    "quint_five_sacred_colors_bodypaint",
    "hexa_six_chakras_bodypaint",
    "octet_planets_solar_bodypaint",
    "quad_four_goddesses_bodypaint",
    "quad_lunar_phases_bodypaint",
    "quint_five_dance_cultures_bodypaint",
    "trio_inside_outside_bodypaint",    "quad_fashion_capitals_bodypaint",

        # 2026-07-03 �ű� SS 62�� �ݿ� (SSS 52 + SS���� 10)
    "champagne_pour_body",
    "wine_pour_body",
    "milk_pour_body",
    "honey_pour_body",
    "gold_paint_body",
    "hot_tub_goddess",
    "foam_bath_goddess",
    "pasties_editorial",
    "body_tape_art",
    "wrap_sarong_nude",
    "ribbon_only",
    "desert_heat_nude",
    "jungle_wet_goddess",
    "steam_room_goddess",
    "volcanic_heat_body",
    "liquid_latex_drip",
    "silver_foil_body",
    "holographic_latex",
    "mirror_latex",
    "private_pool_villa",
    "rooftop_pool_night",
    "penthouse_pool",
    "yacht_sunset_glam",
    "casino_vip_glam",
    "limo_glam",
    "bed_editorial",
    "floor_editorial",
    "chair_editorial",
    "door_frame_glam",
    "staircase_glam",
    "elevator_glam",
    "trio_bodypaint_latex_frame",
    "trio_bodypaint_gown_frame",
    "trio_bodypaint_leather_frame",
    "trio_animal_bodypaint_latex",
    "trio_klimt_bodypaint_gold_gown",
    "trio_galaxy_bodypaint_chrome",
    "duo_bodypaint_latex",
    "duo_bodypaint_gown",
    "duo_bodypaint_leather",
    "duo_bodypaint_gold_dress",
    "duo_animal_bodypaint_latex",
    "duo_klimt_bodypaint_gown",
    "duo_galaxy_bodypaint_chrome",
    "trio_latex_bodypaint_center",
    "trio_gown_bodypaint_center",
    "trio_leather_bodypaint_center",
    "trio_bikini_bodypaint_center",
    "trio_sheer_bodypaint_center",
    "trio_chrome_bodypaint_center",
    "invisible_dress",
    "neon_latex",
    "paint_pour_goddess",
    "neon_paint_pour",
    "shower_goddess",
    "rain_soaked_nude",
    "waterfall_nude",
    "ocean_nude_editorial",
    "steam_bath_goddess",
    "painted_jeans",
    "sauna_nude_editorial",
    "chrome_paint_body",

    # 2026-07-02 �����ս�&��� G3/G4 SS (9�� ��ü)
    "opera_night",
    "christmas_glamour",
    "ballet_noir",
    "broadway_diva",
    "street_dance",
    "drag_glamour",
    "ribbon_goddess",
    "petal_storm",
    "pop_art_glamour",
    # ���� ��ȭ/���� �迭
    "bioluminescent_ink","galaxy_skin","klimt_gold_body","half_statue","vangogh_body",
    "dali_surreal","munch_scream","cherry_blossom_night","kitty_glam","yoruba_glamour",
    "ash_phoenix","lichtenstein_dot","warhol_pop","mondrian_body",
    # v14
    "lace_body_paint","jewelry_trompe_loeil",
    # v15 ��ȭ
    "klimt_silver","botticelli_venus","liquid_gold_drip","mermaid_scales","tiger_stripes_body",
    # v16 ����
    "latex_queen",
    # v18 ���� 1�� �׽�Ʈ
    # v18 ���� SS ? ���� ����� �� Ȯ�� (2026-06-07)
    "mantis_shrimp","phoenix_rising","jellyfish_glow","panther_black",
    "octopus_ink","snow_leopard","scarab_beetle",
    "atlas_moth","eagle_wings","butterfly_monarch",
    "arctic_fox",  # SS Ȯ�� (2026-06-08 ���� ���̽�������+���ǰ� 2�� ���� �Ϸ�)
    # 2026-06-06 ��ȭ/�۰� �׽�Ʈ Ȯ��
    "degas_dancer","toulouse_lautrec","waterhouse_nymph",
    "takashi_murakami","yayoi_kusama","keith_haring_body",
    # 2026-06-06 �ѱ��׸� �׽�Ʈ Ȯ��
    "dancheong_body","najeonchilgi_body","goryeo_celadon_body",
    "minhwa_body","korean_tiger_body","silla_crown_body",
    # 2026-06-06 ����/�ڿ� �׽�Ʈ Ȯ��
    "najeon_abalone","giraffe_pattern","zebra_stripes","dragon_scales_red",
    # 2026-06-06 �߰� �׽�Ʈ Ȯ��
    "alma_tadema","gauguin_tropics","melting_chocolate",
    # 2026-06-06 ����/����/���׽�Ʈ Ȯ�� 7��
    "parrot_tropical","boa_constrictor","king_cobra_hood","cheetah_speed",
    "bird_of_paradise","owl_feather","crocodile_skin",
    # 2026-06-07 �ѱ� �ż� 4��
    "phoenix_jujakk","cheongnyong_dragon","korean_dragon_body","haetae_guardian",
    # 2026-06-07 v20 SS 6��
    "coral_reef_body","galaxy_nebula_body","islamic_geometric_body",
    "aztec_calendar_body","stained_glass_body","mushroom_forest_body",
    # 2026-06-07 ����/����/���� (���� 4���� 2026-06-08 ����)
    "hieroglyph_body","mexico_flag_body",
    "ocelot_wild","ndebele_pattern",
    # 2026-06-08 ���� �迭 SS ����� ? ���� S 4��
    #   (union_jack_body, usa_stars_stripes_body, south_africa_flag_body, brazil_flag_body)
    #   ����: ���� �����=�Ǻ��� ������ ����, ���� ��Ƽ�� ���� �� SS ȸȭ�� �̴�
    #   mexico_flag_body�� SS ���� (�߾� ����=������+�� ����ȭ, ��ȭ/���� �迭�� ����)
    # 2026-06-07 ����/�ڿ�/���� 6��
    "celtic_knot_body","greek_mosaic_body","ocean_depth_body",
    "weather_map_body","bauhaus_body","wolf_grey",
    # 2026-06-07 v22 ����ƽ&��Ƽ�� SS ? ���� ����� �� Ȯ��
    #   (���� S: burlesque, dominatrix_glam, corset_stockings,
    #    dark_fairy_erotic, tape_bondage, metal_bondage)
    #   (����: military_domme ? ��ġ ��¡ ���� ����ũ, ������ ���� �ʿ�)
    # 2026-06-08 ���ؽ�/���ü��� �����: ���� pvc_transparent_full/chrome_vixen/liquid_metal_body,
    #   �°� vampire_seduction/witch_sensual/latex_venom (��0)
    # 2026-06-08 ��ť���� �����: dark_succubus ����(succubus_full�� �ߺ�) �� SS 105��
    "transparent_dress","sheer_catsuit","latex_transparent",
    "chrome_bodysuit","mirror_dress","suspension_art",
    "dominatrix_full_armor","goddess_throne",
    "doctor_sensual","police_dominatrix",
    "pole_dance_extreme","fire_goddess",
    "succubus_full","dark_angel_fallen","alien_queen_body",
    "body_paint_nude",
    "cabaret_star",
    # 2026-06-08 ���ؽ�/���ü��� SS ����� ? �°� 3��
    #   (���� S: pvc_transparent_full, chrome_vixen, liquid_metal_body)
    #   (����: latex_catsuit_red ? �÷� ���ؽ� �ߺ�, ����� ���)
    "vampire_seduction","witch_sensual","latex_venom",
    # 2026-06-19 �ִϾ�Ʈ��Ÿ�� SS ��ü (SSS 31 + SS���� 1)
    "anime_jp_90s_retro",
    "anime_jp_80s_citypop",
    "anime_jp_modern_glossy",
    "anime_jp_shoujo_soft",
    "anime_jp_shounen_action",
    "anime_jp_seinen_gritty",
    "anime_jp_makoto_watercolor",
    "anime_jp_ghibli_soft",
    "anime_jp_gekiga_noir",
    "anime_jp_pinup_retro",
    "anime_kr_webtoon_glossy",
    "anime_kr_romance_soft",
    "anime_kr_action_manhwa",
    "anime_kr_lezhin_mature",
    "anime_kr_pastel_dream",
    "anime_kr_lofi_chill",
    "anime_kr_noir_mature",
    "anime_cn_donghua_xianxia",
    "anime_cn_guofeng_ink",
    "anime_cn_modern_donghua",
    "anime_cn_palace_drama",
    "anime_us_cartoon_bold",
    "anime_us_comic_ink",
    "anime_us_pixar_stylized",
    "anime_us_disney_classic",
    "anime_us_pinup_classic",
    "anime_us_badgirl_comic",
    "anime_eu_ligne_claire",
    "anime_eu_graphic_novel",
    "anime_eu_erotic_bd",
    "anime_noir_silhouette",
    "anime_jp_ecchi_glossy",

    # 2026-06-09 �ִ� ��Ʈ��Ÿ�� SS 10�� Ȯ�� (JP4/KR3/CN2/EU1)
    "anime_jp_80s_citypop","anime_jp_shoujo_soft","anime_jp_seinen_gritty","anime_jp_makoto_watercolor",
    "anime_kr_webtoon_glossy","anime_kr_action_manhwa","anime_kr_lofi_chill",
    "anime_cn_donghua_xianxia","anime_cn_palace_drama",
    "anime_eu_ligne_claire",
    # 2026-06-09 unicorn_opal SS Ȯ�� (2�� �ϰ��� ���� �Ϸ�)
    "unicorn_opal",
    # 2026-06-09 v23 ������ �ٵ������� SS 12�� Ȯ��
    # Ÿ�� 90% (18/20) ? pastel_dream/minimalist_free ���� ����
    "body_paint_watercolor_free","body_paint_metallic_free","body_paint_impasto","body_paint_airbrush",
    "body_paint_monochrome","body_paint_earth_tones","body_paint_jewel_tones","body_paint_iridescent_free",
    "body_paint_geometric_free","body_paint_organic_flow","body_paint_surreal_free","body_paint_glitter_free",
    # 2026-06-09 �ִ� A�� SS 6�� Ȯ�� (v24, 7/7 ���� 0��)
    # demon_slayer ���� (swordmistress�� �ߺ�)
    "anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden",
    "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja",
    # 2026-06-10 ���Ÿ� �۷��� �׷�1 ? ���/��ũ 7��
    "black_mirror","noir_opulence","velvet_darkness","luxury_noir",
    "lace_noir","midnight_couture","velvet_serpent",
    # 2026-06-10 ���Ÿ� �۷��� �׷�2 ? ���/ȭ��Ʈ 9��
    "golden_oil","golden_nude","gold_temptress","golden_hour_editorial",
    "platinum_elite","ivory_silk","pearl_essence","velvet_gold","diamond_couture",
    # 2026-06-10 ���Ÿ� �۷��� �׷�3 ? ����ī��/������ 8��
    "runway_power","red_carpet","red_temptress","crimson_gown",
    "opera_glam","silver_screen","crystal_gown","baroque_glam",

    "feather_cascade",
    "feather_trim_mini",
    "cobweb_drape",
    "petal_goddess",
    "goddess_draped",
    "sheer_overlay",
    "champagne_mist",
    "couture_heat",
    "casino_royale",
    "black_tie_gala",
    "champagne_tower",
    "plunge_gown",
    "slit_maxi",
    "cutout_bodysuit",
    "jeweled_bikini_top",
    "golden_drape_goddess",
    "penthouse_glam",
    "serpentine_dress",
    "valkyrie_storm",
    "shadow_play",
    "power_suit",
    "shadow_queen",
    "punk_queen",
    "uyuni_wet_silk",
    "aurora_bare",
    "antelope_light_sheer",
    "lava_field_latex",
    # 2026-06-11 ��� ������ SS Ȯ��
    "son_doong_jungle", "petra_rose", "danxia_rainbow",
    "dead_vlei_ghost", "lake_natron",
    "socotra_alien", "richat_eye", "derinkuyu_underground",
    "palacio_de_sal", "naoshima_art_island",
    # 2026-06-13 ��ġ&����Ʈ SS/SSS Ȯ��
    "summer_beach",
    "surfer_goddess",
    "pool_goddess",
    "poolside_noir",
    "glass_floor",
    "glass_house",
    "ski_chalet",
    "beach_bonfire",
    "balcony_goddess",
    "coral_diving",
    "beach_bonfire_night",
    "hammock_resort",
    # SSS ��ġ 4���� SS�� ����
    "infinity_pool",
    "scuba_goddess",
    "spa_noir",
    "sunset_cruise",
    # 2026-06-14 ��&ī���� SS Ȯ��
    "y2k_fairy",
    "pink_champagne",
    "cotton_candy",
    "angel_baby",
    "idol_stage",
    "kitty_glam",
    "strawberry_milk",
    "neon_kawaii",
    "fairy_kei",
    "gyaru_glam",
    "kogal_style",
    "maid_glamour",
    "visual_kei",
    "disco_barbie",
    "bubblegum_pop",
    "rainbow_rave",
    "glitter_bomb",
    "tokimeki_pop",
    "kpop_girl_crush",
    "hallyu_goddess",
    "kdrama_chaebol_heir",
    "gangnam_luxury_glam",
    "harajuku_doll",
    # 2026-06-14 ��&ī���� SSS 10���� SS�� ����
    "cherry_pop",
    "hime_gyaru",
    "decora_kei",
    "lolita_gothic",
    "space_babe",
    "arcade_queen",
    "virtual_idol",
    "kdrama_villain_queen",
    "bubble_tea",
    "doll_house",
    # SSS�� SS�� ���� (format_preset ����)
    "angkor_dawn", "tikal_skyrise", "cenote_sacred", "waitomo_glow",
    "marble_caves_water", "bagan_balloon", "tigers_nest_cliff",
    "sheikh_zayed_dawn", "livraria_lello_staircase",
    "namib_star_desert", "ellora_rock_temple",
    # 2026-06-13 v26 ���� ���帶ũ SS/SSS Ȯ��
    "positano_cliff",
    "bruges_canal",
    "colosseum_dusk",
    "alhambra_palace",
    "mont_saint_michel",
    "sigiriya_rock",
    "angkor_thom_faces",
    "teotihuacan_pyramid",
    "palmyra_colonnade",
    "cinque_terre_harbor",
    "karnak_temple",
    "chichen_itza_pyramid",
    "gobekli_tepe",

    # 2026-06-18 ��&���� SS Ȯ�� (SSS ���� ��ü)
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
    "after_party_suite", "tennis_short_dress",
    # 2026-06-13 v27 ��&���� SS/SSS Ȯ��
    "dressing_room_mirror",
    "vip_booth_neon",
    "pool_edge_wet",
    "ocean_wave_body",
    "penthouse_bath",
    "silk_sheets_morning",
    "spa_private_steam",
    "bar_counter_glam",
    "after_party_suite",
    "tennis_short_dress",
    # 2026-06-15 ����&�׸� �׷�1 SS Ȯ�� (cherry_blossom~autumn_forest)
    "cherry_blossom",
    "lavender_field",
    "spring_rain",
    "tulip_field",
    "autumn_forest",
    # 2026-06-15 ����&�׸� �׷�2 SS Ȯ�� (sunflower_field~golden_autumn)
    "sunflower_field",
    "greenhouse_eden",   # SSS�� SS�� ���� (format_preset ����)
    "tropical_night",
    "first_snow",
    "golden_autumn",
    # 2026-06-15 harajuku_doll SSS�� SS�� ����
    "harajuku_doll",
    # 2026-06-15 ����&�׸� �׷�3 SS Ȯ��
    "midsummer_heat",
    "rainy_season",
    "harvest_moon",
    "winter_solstice",
    "cherry_blossom_night",
    # 2026-06-15 ����&�׸� �׷�4 SS Ȯ��
    "tropical_monsoon",
    "halloween_glam",       # SSS�� SS�� ����
    "new_year_glam",        # SSS�� SS�� ����
    "sakura_night_glam",    # SSS�� SS�� ����
    "monsoon_goddess",
    # 2026-06-15 �����丮��&���� �׷�1 SS Ȯ��
    "silhouette_only",
    "back_beauty",
    "collarbone_focus",
    "neck_elegance",
    "long_legs_focus",
    # 2026-06-15 �����丮��&���� �׷�2 SS Ȯ�� (SSS ����)
    "light_driven",
    "backlit_silk",         # SSS�� SS�� ����
    "mirror_goddess",
    "mirror_room",          # SSS�� SS�� ����
    "eclipse_body",         # SSS�� SS�� ����
    # 2026-06-15 �����丮��&���� �׷�3 SS Ȯ�� (SSS ����)
    "chrome_skin",
    "neon_body",
    "plasma_aura",          # SSS�� SS�� ����
    "molten_chrome",        # SSS�� SS�� ����
    "mercury_rising",
    # 2026-06-15 �����丮��&���� �׷�4 SS Ȯ�� (SSS ����)
    "mercury_pool",         # SSS�� SS�� ����
    "titanium_body",
    "snowflake_skin",       # SSS�� SS�� ����
    "80s_power",
    "y2k_chrome",
    # 2026-06-15 �����丮��&���� �׷�5 SS Ȯ��
    "bohemian_paris",
    "origami_couture",
    "wet_glass",
    "smoke_studio",
    "infrared_beauty",
    # 2026-06-15 �����丮��&���� �׷�6 SS Ȯ�� (SSS ����)
    "grain_film",
    "dreamy_soft_focus",
    "film_noir_glam",
    "noir_femme_fatale",    # SSS�� SS�� ����
    # 2026-06-21 �ڿ�&���� G1~G10 SS_TIER ��ġ
    "lava_flow",
    "heat_shimmer",
    "solar_flare",
    "desert_mirage",
    "ocean_surge",
    "waterfall_goddess",
    "water_reflection",
    "liquid_gold_pour",
    "ice_palace",
    "ice_refraction",
    "frozen_latex",
    "blizzard_queen",
    "arctic_minimal",
    "frozen_baikal",
    "sandstorm_veil",
    "desert_oracle",
    "desert_sand_glam",
    "smoke_veil",
    "mist_goddess",
    "storm_couture",
    "storm_lightning",
    "lightning_body",
    "zero_gravity",
    "winter_forest",
    "cliff_edge",
    "deep_cave",
    "dawn_awakening",
    "liquid_mirror",
    "aurora_drape",
    "aurora_spirit",
    "prism_light",
    "shattered_glass",
    "dead_vlei_ghost",
    "son_doong_jungle",
    "danxia_rainbow",
    "socotra_alien",
    "lake_natron",
    "zhangjiajie_avatar",
    "pamukkale_white",
    "plitvice_cascade",
    "rainbow_mountain",
    "kelimutu_crater",
    "victoria_falls",
    "wisteria_tunnel",
    "torres_del_paine",
    "ha_long_bay",
    "fairy_pools",
    "tunnel_of_love",
    "chocolate_hills",
    "volcanic_goddess",
    "santorini_lightning",
    "tidal_wave",
    "rain_soaked",
    "mist_vanguard",
    "tropical_storm",

    # 2026-06-24 �Ŀ�&���� SSS (SS ����)
    "valkyrie_storm",
    "fencer_noir",
    "martial_arts",
    "boxing_glamour",
    "cage_fighter",
    "biker_glam",
    "riot_goddess",
    "punk_queen",
    "steel_warrior",
    "power_suit",
    "shadow_play",
    "power_curve",
    "sculpted_power",
    "shadow_queen",
    "bioluminescence",
    "bioluminescent",
    "duo_aurora_bodypaint",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_jungle_tribal_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    "duo_skeleton_bloom_bodypaint",
    "duo_odalisque_gisaeng_bodypaint",
    "trio_stone_bronze_iron_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint",

    # 2026-06-24 �����ս�&��� G1+G2 SSS (SS ����)
    "flamenco_queen",
    "tango_passion",
    "ribbon_dance",
    "aerial_silk",
    "kathak_dance",
    "hula_goddess",
    "circus_performer",
    "fire_dancer",
    "masquerade_ball",
    "samba_carnival",
    "jazz_dance_glam",
    # 2026-06-25 ���&��ƼŬ 30�� (SS ����)
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
    # 2026-06-25 ����ƽ&��Ƽ�� G1 (SS ����)
    "latex_venom", "latex_catsuit", "latex_catsuit_red", "pvc_transparent_full",
    "latex_hood_full", "latex_transparent", "vinyl_goddess", "rubber_goddess",
    "wet_latex",
    # 2026-06-25 ����ƽ&��Ƽ�� G2 (SS ����)
    "chrome_vixen", "chain_goddess", "savage_leather", "leather_bodysuit",
    "chrome_bodysuit", "mirror_dress", "liquid_metal_body",

    # 2026-06-26 ����ƽ&��Ƽ�� G3~G12 SS (SSS ���� 51��)
    "bondage_fashion", "strappy_harness", "harness_only", "rope_bondage_art",
    "suspension_art", "tape_bondage", "metal_bondage",
    "mesh_bodysuit", "bodystocking", "fishnet_bodysuit", "transparent_dress",
    "sheer_catsuit", "catsuit_zipper", "pvc_transparent_full",
    "dominatrix_glam", "dominatrix_full_armor", "dominatrix_red",
    "goddess_throne", "pole_art",
    "burlesque", "showgirl", "cabaret_star", "candy_rave",
    "lap_dance_glam", "lap_dance_extreme", "striptease_art",
    "pole_dance_power", "pole_dance_extreme", "midnight_bath", "belly_dance_glam",
    "dark_succubus", "vampire_seduction", "witch_sensual",
    "dark_fairy_erotic", "shadow_seductress", "succubus_full",
    "dark_angel_fallen", "alien_queen_body", "fire_goddess",
    "secretary_after_hours", "nurse_sensual", "maid_sensual",
    "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",
    "oil_goddess", "micro_thong_only", "fetish_boots_only",
    "corset_stockings",


    # 2026-06-24 ��Ÿ��&��ũ 26�� (SS ����)
    "dark_mermaid","vampire_queen","angel_fallen","moon_goddess","demon_goddess","forest_witch",
    "pastel_fairy","medusa_queen","halloween_queen","hologram_ghost","glitch_beauty",
    "void_emergence","void_glamour","void_secret","crystal_goddess","toxic_bloom",
    "zombie_apocalypse","dark_academia","gothic_romance","double_exposure_dark",
    "double_exposure_ethereal","oil_slick_noir",
    "witch_ritual","fae_queen","cursed_beauty","shadow_realm",

    # 2026-06-24 �Ƿ翧&������ 30�� (SS ����)
    "silhouette_spotlight_smoke","silhouette_spotlight_latex","silhouette_spotlight_heels",
    "silhouette_spotlight_hair","silhouette_spotlight_dance","silhouette_spotlight_chair",
    "silhouette_spotlight_back","silhouette_spotlight_pole",
    "silhouette_window_city","silhouette_window_rain","silhouette_window_sheer",
    "silhouette_doorway_light","silhouette_window_sunset","silhouette_window_neon",
    "silhouette_neon_pink","silhouette_neon_blue","silhouette_neon_red",
    "silhouette_neon_purple","silhouette_neon_multicolor",
    "silhouette_sunset_beach","silhouette_sunset_cliff","silhouette_moonlight","silhouette_aurora",
    "silhouette_pool_underwater","silhouette_pool_edge",
    "silhouette_bath_candle","silhouette_rain_wet","silhouette_fire_dark",
    "silhouette_candle_boudoir","silhouette_smoke_studio",

    # 2026-06-24 ��Ʈ&�۷ν� 30�� (SS ����, SSS 29�� + SS ���� 1��)
    "pool_surface_break","pool_underwater_up","pool_edge_dripping","infinity_pool_wet",
    "hot_spring_steam","jacuzzi_bubbles",
        # 2026-07-02 �ű� �߰�
        "champagne_pour_body",
        "wine_pour_body",
        "milk_pour_body",
        "honey_pour_body",
        "gold_paint_body",
        "paint_pour_goddess",
        "neon_paint_pour",
        "shower_goddess",
        "rain_soaked_nude",
        "hot_tub_goddess",
        "foam_bath_goddess",
        "waterfall_nude",
        "ocean_nude_editorial",
        "steam_bath_goddess",
    "rain_window_inside","rain_street_soaked","rain_studio_dramatic","monsoon_body","rain_car_window",
    "oil_pour_studio","oil_drip_back","honey_drip_body","chocolate_pour_gloss",
    "gloss_lips_drip","chrome_gloss_body",
    "sweat_studio_light","after_workout_glow","heat_mirage_sweat","sauna_steam_body",
    "condensation_skin","ice_melt_drip","dew_morning_body","frost_breath_cold",
    "waterfall_direct","wave_crash_body","wet_silk_minimal",
    "bubble_bath_gloss","milk_bath_petals",
    # 2026-07-02 ȯ�� ��ü �ٵ������� SS (22�� ��ü)
    # 2026-07-02 �ٵ�������+�ǻ� �ͽ� �ݶ�
        "trio_bodypaint_latex_frame",
        "trio_bodypaint_gown_frame",
        "trio_bodypaint_leather_frame",
        "trio_animal_bodypaint_latex",
        "trio_klimt_bodypaint_gold_gown",
        "trio_galaxy_bodypaint_chrome",
        "duo_bodypaint_latex",
        "duo_bodypaint_gown",
        "duo_bodypaint_leather",
        "duo_bodypaint_gold_dress",
        "duo_animal_bodypaint_latex",
        "duo_klimt_bodypaint_gown",
        "duo_galaxy_bodypaint_chrome",
        "trio_latex_bodypaint_center",
        "trio_gown_bodypaint_center",
        "trio_leather_bodypaint_center",
        "trio_bikini_bodypaint_center",
        "trio_sheer_bodypaint_center",
        "trio_chrome_bodypaint_center",
        # ?? ȯ�� ��ü �ٵ�������
        "merge_butterfly_fabric",
    "merge_floral_wallpaper",
    "merge_leopard_fabric",
    "merge_mandala_carpet",
    "merge_toile_pattern",
    "merge_tartan_plaid",
    "merge_salt_flat_sky",
    "merge_autumn_leaves_floor",
    "merge_coral_reef_water",
    "merge_sand_dunes",
    "merge_moss_stone_ground",
    "merge_clockwork_gears",
    "merge_marble_column_wall",
    "merge_islamic_tile_wall",
    "merge_stained_glass_window",
    "merge_circuit_board",
    "merge_klimt_gold_mural",
    "merge_vangogh_starry",
    "merge_ukiyo_wave_print",
    "merge_mondrian_grid",
    "merge_pollock_splatter",
    "merge_byzantine_mosaic",

    # 2026-06-29 ��Ƽ �ٵ������� SS (57�� ��ü)
    "duo_fire_and_ice_bodypaint",
    "duo_day_and_night_bodypaint",
    "duo_bloom_and_void_bodypaint",
    "duo_gold_and_shadow_bodypaint",
    "duo_ocean_and_desert_bodypaint",
    "duo_circuit_and_nature_bodypaint",
    "duo_east_and_west_bodypaint",
    "duo_macro_and_micro_bodypaint",
    "duo_ancient_and_future_bodypaint",
    "duo_poison_and_medicine_bodypaint",
    "duo_deep_sea_bodypaint",
    "trio_rgb_trinity_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_predator_prey_apex_bodypaint",
    "trio_ink_gold_chrome_bodypaint",
    "trio_season_trinity_bodypaint",
    "trio_sun_moon_star_bodypaint",
    "trio_three_oceans_bodypaint",
    "trio_three_civilizations_bodypaint",
    "trio_fire_water_earth_bodypaint",
    "trio_three_big_cats_bodypaint",
    "duo_butterfly_split_bodypaint",
    "duo_yin_yang_merge_bodypaint",
    "duo_world_map_bodypaint",
    "duo_klimt_tree_bodypaint",
    "duo_galaxy_split_bodypaint",
    "duo_wave_hokusai_bodypaint",
    "duo_dna_helix_bodypaint",
    "duo_solar_eclipse_bodypaint",
    "duo_human_shadow_bodypaint",
    "duo_tiger_split_bodypaint",
    "duo_starry_night_split_bodypaint",
    "duo_peacock_split_bodypaint",
    "trio_triptych_klimt_bodypaint",
    "trio_phoenix_rising_bodypaint",
    "trio_world_tree_bodypaint",
    "trio_ocean_depth_bodypaint",
    "trio_aurora_spectrum_bodypaint",
    "trio_cosmic_creation_bodypaint",
    "trio_last_supper_bodypaint",
    "trio_rainbow_arc_bodypaint",
    "trio_milky_way_panorama_bodypaint",
    "trio_coral_reef_zones_bodypaint",
    "trio_creation_of_adam_bodypaint",
    "trio_poles_and_equator_bodypaint",
    "quad_four_seasons_bodypaint",
    "quad_four_elements_bodypaint",
    "quad_four_directions_bodypaint",
    "quad_four_seasons_klimt_bodypaint",
    "quad_rgba_spectrum_bodypaint",
    "quint_five_continents_bodypaint",
    "quint_five_elements_asia_bodypaint",
    "quint_rainbow_five_bodypaint",
    "quint_five_oceans_bodypaint",
    # 2026-06-26 �ѱ� ���� & ���� �۷��� SS (78�� ��ü)
    "silla_queen_gold", "silla_dancing_girl", "baekje_lotus_queen",
    "goguryeo_warrior_queen", "gojoseon_shaman_queen", "gaya_iron_goddess",
    "silla_hwarang_girl", "ancient_mural_goddess", "three_kingdoms_spy",
    "dongye_tribal_queen",
    "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess",
    "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",
    "mongol_goryeo_queen", "goryeo_haenyeo_silk",
    "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex",
    "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",
    "joseon_merchant_woman", "damo_warrior", "joseon_night_queen",
    "joseon_concubine_red", "changdeok_moonlight", "gyeongbokgung_geisha",
    "gisaeng_joseon_sheer", "gisaeng_red_lantern", "gisaeng_sword_dance",
    "gisaeng_haiku_bath", "gisaeng_rain_dance", "gisaeng_black_silk",
    "wonhyang_legend", "hwang_jini_glam", "gisaeng_fan_dance",
    "gisaeng_pipa_night", "gisaeng_mirror_boudoir", "pyongyang_gisaeng",
    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
    "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
    "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
    "haenyeo_wet_glam", "dano_festival_glam", "ganggangsullae_night",
    "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
    "jeju_shaman_sea", "korean_harvest_goddess",
    "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
    "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
    "goguryeo_fire_warrior", "joseon_spy_sheer",
    "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
    "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
    "hanbok_wet_editorial", "joseon_boudoir",

}

# ������ ��ũ �׸� CSS ��������������������������������������������������������������������������������
BG       = "#1e1e1e"
BG_SIDE  = "#252526"
BG_INPUT = "#2d2d2d"
BG_CARD  = "#2a2a2a"
GOLD     = "#c9a84c"
GOLD_DIM = "#8a6f30"
BORDER   = "#3a3a3a"
TEXT     = "#d4d4d4"
TEXT_DIM = "#888"

st.markdown(f"""
<style>
.stApp, [data-testid="stAppViewContainer"] {{ background-color: {BG} !important; }}
[data-testid="stHeader"] {{ background-color: {BG} !important; }}
[data-testid="stSidebar"] {{ background-color: {BG_SIDE} !important; border-right: 1px solid {BORDER} !important; }}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label {{ color: {TEXT_DIM} !important; font-size: 0.78rem !important; }}
[data-testid="stSidebar"] h3 {{ color: {GOLD_DIM} !important; font-size: 0.65rem !important; letter-spacing: 2.5px !important; text-transform: uppercase !important; }}
h1, h2, h3, h4, h5 {{ color: {GOLD} !important; letter-spacing: 1.5px !important; }}
.stTabs [data-baseweb="tab-list"] {{ background-color: transparent !important; border-bottom: 1px solid {BORDER} !important; gap: 0 !important; }}
.stTabs [data-baseweb="tab"] {{ background-color: transparent !important; color: {TEXT_DIM} !important; font-size: 0.78rem !important; padding: 10px 20px !important; border-bottom: 2px solid transparent !important; }}
.stTabs [aria-selected="true"] {{ color: {GOLD} !important; border-bottom: 2px solid {GOLD} !important; background-color: transparent !important; }}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}
.stSelectbox > div > div {{ background-color: {BG_INPUT} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; color: {TEXT} !important; font-size: 0.8rem !important; }}
.stSelectbox > div > div:hover {{ border-color: rgba(201,168,76,0.4) !important; }}
.stSelectbox > div > div:focus-within {{ border-color: rgba(201,168,76,0.7) !important; box-shadow: 0 0 0 1px rgba(201,168,76,0.2) !important; }}
.stSelectbox label {{ color: {GOLD} !important; font-size: 0.68rem !important; letter-spacing: 1.2px !important; text-transform: uppercase !important; font-weight: 600 !important; }}
.stSelectbox [data-baseweb="select"] span,
.stSelectbox [data-baseweb="select"] div,
.stSelectbox [data-baseweb="select"] input {{ color: {TEXT} !important; }}
[data-baseweb="popover"] [data-baseweb="menu"] {{ background-color: {BG_INPUT} !important; border: 1px solid {BORDER} !important; }}
[data-baseweb="popover"] li {{ background-color: {BG_INPUT} !important; color: {TEXT} !important; font-size: 0.8rem !important; }}
[data-baseweb="popover"] li:hover {{ background-color: rgba(201,168,76,0.1) !important; color: {GOLD} !important; }}
.stButton > button {{ border-radius: 6px !important; font-size: 0.75rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; font-weight: 700 !important; transition: all 0.2s !important; height: 42px !important; }}
.stButton > button[kind="primary"] {{ background: linear-gradient(135deg, {GOLD}, {GOLD_DIM}) !important; border: none !important; color: #111 !important; }}
.stButton > button[kind="primary"]:hover {{ background: linear-gradient(135deg, #e8c96a, {GOLD}) !important; transform: translateY(-1px) !important; }}
.stButton > button[kind="secondary"] {{ background: transparent !important; border: 1px solid rgba(201,168,76,0.4) !important; color: {GOLD} !important; }}
.stButton > button[kind="secondary"]:hover {{ background: rgba(201,168,76,0.08) !important; border-color: rgba(201,168,76,0.7) !important; }}
.stRadio > div {{ gap: 6px !important; }}
.stRadio label {{ background: {BG_CARD} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; padding: 7px 12px !important; font-size: 0.78rem !important; color: {TEXT_DIM} !important; cursor: pointer !important; transition: all 0.2s !important; }}
.stRadio label:has(input:checked) {{ background: rgba(201,168,76,0.12) !important; border-color: rgba(201,168,76,0.5) !important; color: {GOLD} !important; }}
.stTextArea textarea {{ background-color: {BG_INPUT} !important; color: {TEXT} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; font-size: 0.78rem !important; line-height: 1.8 !important; }}
.stTextArea textarea:focus {{ border-color: rgba(201,168,76,0.5) !important; box-shadow: 0 0 0 1px rgba(201,168,76,0.15) !important; }}
.stCode {{ background-color: {BG_INPUT} !important; border: 1px solid rgba(201,168,76,0.25) !important; border-radius: 6px !important; }}
.stCode code {{ color: #ce9178 !important; font-size: 0.75rem !important; line-height: 1.8 !important; }}
.stCode button {{ background: rgba(201,168,76,0.1) !important; border: 1px solid rgba(201,168,76,0.3) !important; color: {GOLD} !important; border-radius: 4px !important; }}
[data-testid="stToggle"] > div {{ background-color: {GOLD} !important; }}
.stAlert {{ background-color: {BG_CARD} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; color: {TEXT_DIM} !important; font-size: 0.78rem !important; }}
hr {{ border-color: {BORDER} !important; margin: 12px 0 !important; }}
.stCaption {{ color: {TEXT_DIM} !important; font-size: 0.7rem !important; }}
p, li, .stMarkdown {{ color: {TEXT} !important; font-size: 0.82rem !important; }}
::-webkit-scrollbar {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER}; border-radius: 2px; }}
::-webkit-scrollbar-thumb:hover {{ background: {GOLD_DIM}; }}
</style>
""", unsafe_allow_html=True)

# ������ ��� ��������������������������������������������������������������������������������������������������
st.markdown('''
<div style="padding:8px 0 20px;">
  <div style="font-size:1.6rem;font-weight:700;letter-spacing:8px;color:#c9a84c;">? LumineX</div>
  <div style="font-size:0.65rem;letter-spacing:3px;color:#555;margin-top:4px;text-transform:uppercase;">AI Fashion Image Engine �� v4.4</div>
</div>
''', unsafe_allow_html=True)

# ������ ���̵�� ������������������������������������������������������������������������������������������
with st.sidebar:
    st.markdown("### ?? ���� ����")
    st.markdown("---")
    global_platform = st.radio("??? ��� �÷���", options=["Gemini", "ChatGPT (DALL-E)", "Midjourney"], index=0)
    global_aspect   = st.selectbox("?? �̹��� ����", options=list(ASPECT_RATIOS.keys()), index=0, help="�� = �⺻�� ����")
    global_realism      = st.toggle("?? �ǻ� ���", value=True)
    global_art_fallback = st.toggle("?? ���� �� ��Ʈ ��Ÿ��", value=False, help="HIGH ���� ���� �� ��äȭ/��� �ڵ� ����")
    st.markdown("---")
    st.markdown("### ?? ���� �÷���")
    global_video_platform = st.radio("���� ���� �÷���", options=["Veo 3 (Gemini)", "Kling AI", "Runway", "Hailuo"], index=0)
    st.markdown("---")
    platform_colors = {"Gemini": "??", "ChatGPT (DALL-E)": "??", "Midjourney": "??"}
    st.markdown(f"**�÷���:** {platform_colors[global_platform]} `{global_platform}`")
    st.markdown(f"**����:** `{global_aspect.split('?')[0].strip()}`")
    if global_platform == "Gemini":
        st.markdown(f"**�ǻ�:** `{'ON ?' if global_realism else 'OFF'}`")
    st.markdown("---")
    st.markdown("### ?? ����")
    st.markdown("1. �÷��� ����\n2. �� ����\n3. ��� ����\n4. **������Ʈ ����** Ŭ��\n5. �ڵ�ڽ� Ŭ�� �� ����\n6. �ش� �÷����� �ٿ��ֱ�")
    st.markdown("---")
    st.markdown("### ?? �÷��� ��")
    if global_platform == "Gemini":
        st.info("�ڿ��� ������. ��� ���Ҽ��� ���ƿ�.")
    elif global_platform == "ChatGPT (DALL-E)":
        st.success("Ű���� �߽�. ª�� �����ϰ�!")
    else:
        st.warning("�±� ���� + --�Ķ���� ���.")
    if global_platform == "Gemini":
        st.markdown("---")
        st.markdown("### ?? Gemini ����")
        if st.button("?? Gemini �� â ����", use_container_width=True, help="���� �ƶ� �ʱ�ȭ"):
            import webbrowser
            webbrowser.open("https://gemini.google.com/app")
        st.caption("?? ���� â �ݺ� ���� �� Ÿ��/��� ���� ����")
    st.markdown("---")
    st.markdown("### ?? ������ ��Ȳ")
    total = sum(len(v) for v in PRESET_CATEGORIES.values())
    st.markdown(f"**�� ������:** `{total}��`")
    st.markdown(f"**?? HOF tier:** `{len(HOF_TIER)}��`")
    st.markdown(f"**SSS tier:** `{len(SSS_TIER)}��`")
    st.markdown(f"**SS tier:** `{len(SS_TIER)}��`")
    st.markdown(f"**ī�װ��:** `{len(PRESET_CATEGORIES)}��`")


def get_prompt(data: dict) -> str:
    if global_platform == "Gemini":
        return build_gemini_prompt(data, global_aspect, global_realism)
    elif global_platform == "ChatGPT (DALL-E)":
        return build_chatgpt_prompt(data, global_aspect)
    else:
        return build_midjourney_prompt(data, global_aspect)


tab1, tab2, tab3, tab4 = st.tabs(["?? ������ ���", "??? ���� ����", "?? ���� ���", "?? ���� ������Ʈ"])

# ??????????????????????????????????????????????????????????
# �� 1: ������ ���
# ??????????????????????????????????????????????????????????
with tab1:
    st.markdown("### ���������� ������Ʈ ����")

    col_cat, col_tier, col_search = st.columns([2, 1, 1])
    with col_cat:
        all_cats = ["?? ��ü"] + list(PRESET_CATEGORIES.keys())
        selected_cat = st.selectbox("?? ī�װ�� ����", options=all_cats, index=0, key="preset_cat_filter")
    with col_tier:
        tier_options = ["��ü Ƽ��", "?? HOF", "??? SSS", "?? SS", "? �Ϲ�"]
        selected_tier = st.selectbox("?? Ƽ�� ����", options=tier_options, index=0, key="preset_tier_filter")
    with col_search:
        search_query = st.text_input("?? ������ �˻�", placeholder="�̸� �˻�...", key="preset_search")

    all_presets = list_presets()
    if selected_cat == "?? ��ü":
        filtered_presets = all_presets
    else:
        cat_list = PRESET_CATEGORIES.get(selected_cat, [])
        filtered_presets = [p for p in all_presets if p in cat_list]

    # Ƽ�� ���� ����
    if selected_tier == "?? HOF":
        filtered_presets = [p for p in filtered_presets if p in HOF_TIER]
    elif selected_tier == "??? SSS":
        filtered_presets = [p for p in filtered_presets if p in SSS_TIER]
    elif selected_tier == "?? SS":
        filtered_presets = [p for p in filtered_presets if p in SS_TIER and p not in SSS_TIER]
    elif selected_tier == "? �Ϲ�":
        filtered_presets = [p for p in filtered_presets if p not in SS_TIER]

    if search_query:
        filtered_presets = [p for p in filtered_presets if search_query.lower() in p.lower()]

    def format_preset(name):
        if name in HOF_TIER:
            return f"?? {name} [HOF]"
        if name in SSS_TIER:
            return f"?? {name} [SSS]"
        if name in SS_TIER:
            return f"? {name} [SS]"
        return f"? {name}"

    col1, col2 = st.columns([2, 1])
    with col1:
        if filtered_presets:
            selected_preset = st.selectbox(
                f"?? ������ ���� ({len(filtered_presets)}��)",
                options=filtered_presets,
                format_func=format_preset
            )
        else:
            st.warning("�ش� ī�װ���� �������� �����.")
            selected_preset = None
    with col2:
        if selected_cat != "?? ��ü":
            ss_count = sum(1 for p in filtered_presets if p in SS_TIER and p not in SSS_TIER)
            sss_count = sum(1 for p in filtered_presets if p in SSS_TIER)
            st.markdown(f"""
<div style="background:{BG_CARD};border:1px solid {BORDER};border-radius:8px;padding:10px 14px;margin-top:28px;">
  <div style="font-size:0.65rem;color:{TEXT_DIM};letter-spacing:1px;">ī�װ�� ��Ȳ</div>
  <div style="font-size:1.1rem;font-weight:700;color:{GOLD};margin-top:4px;">{len(filtered_presets)}��</div>
  <div style="font-size:0.7rem;color:#f0c040;">?? SSS tier {sss_count}��</div>
  <div style="font-size:0.7rem;color:{TEXT_DIM};">? SS tier {ss_count}��</div>
</div>
""", unsafe_allow_html=True)

    if not selected_preset:
        st.stop()

    NONE = "None ? ������ �⺻�� ���"
    col1, col2, col3 = st.columns(3)
    with col1:
        preset_appearance  = st.selectbox("?? ����/����",       [NONE] + list(MODEL_APPEARANCE.keys()), key="preset_appearance")
        preset_age         = st.selectbox("?? ���ɴ�",          [NONE] + list(AGE_APPEARANCE.keys()),   key="preset_age")
        preset_body        = st.selectbox("?? ü��",            [NONE] + list(MODEL_TYPES.keys()),      key="preset_body")
        preset_outfit      = st.selectbox("?? �ǻ�",            [NONE] + list(OUTFIT_TYPES.keys()),     key="preset_outfit")
        preset_material    = st.selectbox("?? ����",            [NONE] + list(MATERIALS.keys()),        key="preset_material")
        preset_footwear    = st.selectbox("?? �Ź�",            [NONE] + list(FOOTWEAR.keys()),         key="preset_footwear")
        preset_nails       = st.selectbox("?? ����",            [NONE] + list(NAILS.keys()),            key="preset_nails")
        preset_skin_detail = st.selectbox("?? �Ǻ� ������",     [NONE] + list(SKIN_DETAILS.keys()),     key="preset_skin_detail")
        preset_body_oil    = st.selectbox("? �ٵ� ����",        [NONE] + list(BODY_OIL.keys()),         key="preset_body_oil")
    with col2:
        preset_hair_style  = st.selectbox("?? ��Ÿ��",      [NONE] + list(HAIR_STYLES.keys()),      key="preset_hair_style")
        preset_pose        = st.selectbox("?? ����",            [NONE] + list(POSES.keys()),            key="preset_pose")
        preset_framing     = st.selectbox("??? �����̹�",        [NONE] + list(FRAMING.keys()),          key="preset_framing")
        preset_angle       = st.selectbox("?? ī�޶� �ޱ�",     [NONE] + list(CAMERA_ANGLES.keys()),    key="preset_angle")
        preset_lighting    = st.selectbox("?? ����",            [NONE] + list(LIGHTING.keys()),         key="preset_lighting")
        preset_color_grade = st.selectbox("?? ����",            [NONE] + list(COLOR_GRADES.keys()),     key="preset_color_grade")
        preset_style       = st.selectbox("?? ��Ÿ��",          [NONE] + list(STYLES.keys()),           key="preset_style")
        preset_cover_style = st.selectbox("?? Ŀ�� ��Ÿ��",     [NONE] + list(COVER_STYLES.keys()),     key="preset_cover_style")
    with col3:
        preset_environment = st.selectbox("??? ȯ��",            [NONE] + list(ENVIRONMENTS.keys()),     key="preset_environment")
        preset_weather     = st.selectbox("??? ����",            [NONE] + list(WEATHER.keys()),          key="preset_weather")
        preset_image_style = st.selectbox("?? �̹��� ��Ÿ��",   [NONE] + list(IMAGE_STYLE.keys()),      key="preset_image_style")
        preset_special_fx  = st.selectbox("?? Ư�� ȿ��",       [NONE] + list(SPECIAL_EFFECTS.keys()),  key="preset_special_fx")
        preset_mood        = st.selectbox("?? ����",            [NONE] + list(MOOD.keys()),             key="preset_mood")

    col_a, col_b, _ = st.columns([1, 1, 2])
    with col_a:
        btn_ai    = st.button("?? AI ����",   use_container_width=True, type="primary", key="preset_btn_ai")
    with col_b:
        btn_quick = st.button("? ���� ����", use_container_width=True, key="preset_btn_quick")

    if "preset_prompt"   not in st.session_state: st.session_state.preset_prompt   = ""
    if "preset_selected" not in st.session_state: st.session_state.preset_selected = ""
    if selected_preset != st.session_state.preset_selected:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""

    def build_preset_overrides() -> dict:
        overrides = {}
        if preset_appearance  != NONE: overrides['appearance']  = MODEL_APPEARANCE[preset_appearance]
        if preset_age         != NONE: overrides['age']         = AGE_APPEARANCE[preset_age]
        if preset_body        != NONE: overrides['body']        = MODEL_TYPES[preset_body]
        if preset_outfit      != NONE:
            od = OUTFIT_TYPES[preset_outfit]
            overrides['outfit'] = od["gemini"] if isinstance(od, dict) else od
        if preset_material    != NONE: overrides['material']    = MATERIALS[preset_material]
        if preset_pose        != NONE: overrides['pose']        = POSES[preset_pose]
        if preset_framing     != NONE: overrides['framing']     = FRAMING[preset_framing]
        if preset_angle       != NONE: overrides['angle']       = CAMERA_ANGLES[preset_angle]
        if preset_footwear    != NONE: overrides['footwear']    = FOOTWEAR[preset_footwear]
        if preset_nails       != NONE: overrides['nails']       = NAILS[preset_nails]
        if preset_skin_detail != NONE: overrides['skin_detail'] = SKIN_DETAILS[preset_skin_detail]
        if preset_body_oil    != NONE: overrides['body_oil']    = BODY_OIL[preset_body_oil]
        if preset_hair_style  != NONE: overrides['hair_style']  = HAIR_STYLES[preset_hair_style]
        if preset_color_grade != NONE: overrides['color_grade'] = COLOR_GRADES[preset_color_grade]
        if preset_lighting    != NONE: overrides['lighting']    = LIGHTING[preset_lighting]
        if preset_style       != NONE: overrides['style']       = STYLES[preset_style]
        if preset_cover_style != NONE: overrides['cover_style'] = COVER_STYLES[preset_cover_style]
        if preset_environment != NONE: overrides['environment'] = ENVIRONMENTS[preset_environment]
        if preset_weather     != NONE: overrides['weather']     = WEATHER[preset_weather]
        if preset_image_style != NONE: overrides['image_style'] = IMAGE_STYLE[preset_image_style]
        if preset_special_fx  != NONE: overrides['special_fx']  = SPECIAL_EFFECTS[preset_special_fx]
        if preset_mood        != NONE: overrides['mood']        = MOOD[preset_mood]
        return overrides

    def apply_overrides_to_prompt(preset: dict, overrides: dict) -> str:
        p = {**preset, **overrides}
        outfit_text   = p.get('outfit', '')
        material_text = p.get('material', '')
        footwear_text = overrides.get('footwear', '')
        wearing_line  = _build_wearing_line(outfit_text, material_text, footwear_text)
        return (
            f"Professional fashion photograph, {overrides.get('framing', 'full body shot')}. "
            f"{'Model appearance: ' + overrides['appearance'] + '. ' if 'appearance' in overrides else ''}"
            f"Model: {p.get('subject', 'a stunning female model')}. Body: {p.get('body', '')}. "
            f"{'Pose: ' + overrides['pose'] + '. ' if 'pose' in overrides else ''}"
            f"{wearing_line} "
            f"Environment: {p.get('environment', '')}. Lighting: {p.get('lighting', '')}. Style: {p.get('style', '')}. "
            f"{'Color grade: ' + overrides['color_grade'] + '. ' if 'color_grade' in overrides else ''}"
            f"{p.get('quality', 'ultra-sharp, 8K, professional photography')}."
        ).strip()

    if btn_ai and selected_preset:
        st.session_state.preset_prompt = ""
        with st.spinner("Claude�� ������Ʈ ���� ��..."):
            try:
                raw       = generate_prompt_with_ai(selected_preset)
                overrides = build_preset_overrides()
                prefix    = []
                if 'appearance' in overrides: prefix.append(overrides['appearance'].split(',')[0])
                if 'body'       in overrides: prefix.append(overrides['body'].split(',')[0])
                if prefix: raw = f"Model: {', '.join(prefix)}. " + raw
                aspect_desc = ASPECT_RATIOS.get(global_aspect, "")
                if aspect_desc: raw += f" {aspect_desc}."
                st.session_state.preset_prompt = raw
            except Exception as e:
                st.error(f"����: {str(e)}")

    if btn_quick and selected_preset:
        st.session_state.preset_prompt = ""
        raw = apply_overrides_to_prompt(load_preset(selected_preset), build_preset_overrides())
        aspect_desc = ASPECT_RATIOS.get(global_aspect, "portrait 2:3 vertical")
        if global_platform == "Gemini":
            raw += f" {aspect_desc}."
        elif global_platform == "ChatGPT (DALL-E)":
            raw += f" {aspect_desc}. Photorealistic, hyperrealistic skin texture, award-winning fashion photography."
        else:
            ar = {"���� 2:3 ? �ι� �⺻":"2:3","���� 3:4 ? ���ż�":"3:4","���� 16:9 ? �ó׸�ƽ":"16:9","���� 4:3 ? ȭ��":"4:3","������ 1:1 ? �ν�Ÿ":"1:1"}.get(global_aspect, "2:3")
            raw += f" --ar {ar} --style raw --q 2"
        st.session_state.preset_prompt = raw

    if st.session_state.preset_prompt:
        st.text_area("������ ������Ʈ", value=st.session_state.preset_prompt, height=160)
        st.code(st.session_state.preset_prompt, language=None)
        st.caption(f"?? ���� �� {global_platform}�� �ٿ���������!")

# ??????????????????????????????????????????????????????????
# �� 2: ���� ����
# ??????????????????????????????????????????????????????????
with tab2:
    st.markdown("### ��Һ� ���� ����")
    st.caption("?? �ٽ� ���(�ܸ�/ü��/�ǻ�/ȯ��)�� �����ص� ���� ������Ʈ�� ���Ϳ�.")

    if st.button("?? ��ü �������� ä���"):
        def rnd(d):
            keys = [k for k in d.keys() if k != "����"]
            return random.choice(keys) if keys else "����"
        st.session_state.r_appearance  = rnd(MODEL_APPEARANCE)
        st.session_state.r_model       = rnd(MODEL_TYPES)
        st.session_state.r_outfit      = rnd(OUTFIT_TYPES)
        st.session_state.r_material    = rnd(MATERIALS)
        st.session_state.r_env         = rnd(ENVIRONMENTS)
        st.session_state.r_light       = rnd(LIGHTING)
        st.session_state.r_framing     = rnd(FRAMING)
        st.session_state.r_angle       = rnd(CAMERA_ANGLES)
        st.session_state.r_style       = rnd(STYLES)
        st.session_state.r_cover_style = "����"
        st.session_state.r_camera      = rnd(CAMERAS)
        st.session_state.r_pose        = rnd(POSES)
        st.session_state.r_expression  = rnd(EXPRESSION)
        st.session_state.r_skin_tone   = rnd(SKIN_TONES)
        st.session_state.r_hair_style  = rnd(HAIR_STYLES)
        st.session_state.r_hair_color  = rnd(HAIR_COLORS)
        st.session_state.r_makeup      = rnd(MAKEUP)
        def rnd_maybe(d, prob=0.5):
            return rnd(d) if random.random() < prob else "����"
        st.session_state.r_footwear        = rnd_maybe(FOOTWEAR,       0.50)
        st.session_state.r_color_grade     = rnd_maybe(COLOR_GRADES,   0.50)
        st.session_state.r_accessories     = rnd_maybe(ACCESSORIES,    0.40)
        st.session_state.r_body_oil        = rnd_maybe(BODY_OIL,       0.30)
        st.session_state.r_weather         = rnd_maybe(WEATHER,        0.30)
        st.session_state.r_bg_crowd        = rnd_maybe(BG_CROWD,       0.30)
        st.session_state.r_mood            = rnd_maybe(MOOD,           0.30)
        st.session_state.r_time_of_day     = rnd_maybe(TIME_OF_DAY,   0.30)
        st.session_state.r_tattoo          = rnd_maybe(TATTOO,         0.15)
        st.session_state.r_special_effects = rnd_maybe(SPECIAL_EFFECTS,0.15)
        st.session_state.r_props           = rnd_maybe(PROPS,          0.15)
        st.session_state.r_image_style     = rnd_maybe(IMAGE_STYLE,    0.15)
        st.session_state.r_era             = rnd_maybe(ERA,            0.15)
        st.session_state.r_concept         = rnd_maybe(CONCEPT,        0.15)
        st.session_state.r_lens_effect     = rnd_maybe(LENS_EFFECT,    0.15)
        st.session_state.r_skin_detail     = rnd_maybe(SKIN_DETAILS,   0.20)
        st.session_state.r_nails           = rnd_maybe(NAILS,          0.30)
        st.session_state.r_cover_style     = rnd_maybe(COVER_STYLES,   0.20)
        st.session_state.r_age         = "����"
        st.session_state.r_model_count = "1�� ? �̱� �� (�⺻)"
        st.session_state.r_body_weight = "����"
        st.session_state.r_bust_size   = "����"
        st.session_state.r_hip_size    = "����"
        st.session_state["use_separate_outfit"] = st.session_state.get("use_separate_outfit", False)
        if st.session_state.get("use_separate_outfit", False):
            top_keys = [k for k in TOP_TYPES.keys() if k != "���� (�ǻ� Ÿ�� ���)"]
            bot_keys = [k for k in BOTTOM_TYPES.keys() if k != "���� (�ǻ� Ÿ�� ���)"]
            if top_keys: st.session_state["r_top_type"] = random.choice(top_keys)
            if bot_keys: st.session_state["r_bottom_type"] = random.choice(bot_keys)
        st.rerun()

    def idx(d, key, default=0):
        keys = list(d.keys())
        val  = st.session_state.get(key, keys[default])
        return keys.index(val) if val in keys else default

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("##### ?? ��")
        appearance  = st.selectbox("?? �ܸ� ? ����/����",          list(MODEL_APPEARANCE.keys()), index=idx(MODEL_APPEARANCE, "r_appearance"))
        age         = st.selectbox("?? ���ɴ�",                     list(AGE_APPEARANCE.keys()),   index=idx(AGE_APPEARANCE,   "r_age"))
        model_type  = st.selectbox("?? ü���� ����",               list(MODEL_TYPES.keys()),       index=idx(MODEL_TYPES,      "r_model"))
        body_weight = st.selectbox("?? ü�� ����",                 list(BODY_WEIGHT.keys()),       index=idx(BODY_WEIGHT,      "r_body_weight"))
        bust_size   = st.selectbox("?? ���� ����",                  list(BUST_SIZE.keys()),         index=idx(BUST_SIZE,        "r_bust_size"))
        hip_size    = st.selectbox("?? �� ����",                   list(HIP_SIZE.keys()),          index=idx(HIP_SIZE,         "r_hip_size"))
        skin_tone   = st.selectbox("?? �Ǻ� ��/����",              list(SKIN_TONES.keys()),        index=idx(SKIN_TONES,       "r_skin_tone"))
        body_oil    = st.selectbox("? �ٵ� ����/�۷ν�",           list(BODY_OIL.keys()),          index=idx(BODY_OIL,         "r_body_oil"))
        expression  = st.selectbox("?? ǥ��/����",                 list(EXPRESSION.keys()),        index=idx(EXPRESSION,       "r_expression"))
        tattoo      = st.selectbox("?? ����/�ٵ��Ʈ",              list(TATTOO.keys()),            index=idx(TATTOO,           "r_tattoo"))
        skin_detail = st.selectbox("?? �Ǻ� ������",               list(SKIN_DETAILS.keys()),      index=idx(SKIN_DETAILS,     "r_skin_detail"))
        nails       = st.selectbox("?? ����",                      list(NAILS.keys()),             index=idx(NAILS,            "r_nails"))
        model_count = st.selectbox("?? �� ��",                   list(MODEL_COUNT.keys()),       index=idx(MODEL_COUNT,      "r_model_count"))
    with col2:
        st.markdown("##### ?? ��Ÿ��")
        use_separate = st.checkbox("?? ������ �и� ����", value=False, key="use_separate_outfit", help="����+���Ǹ� ���� ������ ����")
        if use_separate:
            top_type    = st.selectbox("?? ����",  list(TOP_TYPES.keys()),    index=0, key="r_top_type")
            bottom_type = st.selectbox("?? ����",  list(BOTTOM_TYPES.keys()), index=0, key="r_bottom_type")
            top_label    = top_type.split("?")[0].strip()    if top_type    != "���� (�ǻ� Ÿ�� ���)" else "����"
            bottom_label = bottom_type.split("?")[0].strip() if bottom_type != "���� (�ǻ� Ÿ�� ���)" else "����"
            st.markdown(f"""
<div style="background:#2a2a2a;border:1px solid #c9a84c33;border-radius:8px;padding:8px 12px;margin:4px 0;">
  <span style="font-size:0.7rem;color:#888;letter-spacing:1px;">���õ� ����</span><br>
  <span style="background:#c9a84c22;border:1px solid #c9a84c55;border-radius:4px;padding:2px 8px;font-size:0.78rem;color:#c9a84c;margin-right:4px;">?? {top_label}</span>
  <span style="color:#555;margin-right:4px;">+</span>
  <span style="background:#c9a84c22;border:1px solid #c9a84c55;border-radius:4px;padding:2px 8px;font-size:0.78rem;color:#c9a84c;">?? {bottom_label}</span>
</div>
""", unsafe_allow_html=True)
            outfit = list(OUTFIT_TYPES.keys())[0]
        else:
            outfit      = st.selectbox("?? �ǻ� Ÿ��",  list(OUTFIT_TYPES.keys()), index=idx(OUTFIT_TYPES, "r_outfit"))
            top_type    = "���� (�ǻ� Ÿ�� ���)"
            bottom_type = "���� (�ǻ� Ÿ�� ���)"
        material    = st.selectbox("?? ���� ? �ʰ� ����",          list(MATERIALS.keys()),         index=idx(MATERIALS,        "r_material"))
        footwear    = st.selectbox("?? �Ź�",                      list(FOOTWEAR.keys()),          index=idx(FOOTWEAR,         "r_footwear"))
        pose        = st.selectbox("?? ���� ? �ڼ��� ����",        list(POSES.keys()),             index=idx(POSES,            "r_pose"))
        hair_style  = st.selectbox("?? ��Ÿ��",                list(HAIR_STYLES.keys()),       index=idx(HAIR_STYLES,      "r_hair_style"))
        hair_color  = st.selectbox("?? ����÷�",                 list(HAIR_COLORS.keys()),       index=idx(HAIR_COLORS,      "r_hair_color"))
        makeup      = st.selectbox("?? ����ũ��",                  list(MAKEUP.keys()),            index=idx(MAKEUP,           "r_makeup"))
        accessories = st.selectbox("?? �׼�����",                  list(ACCESSORIES.keys()),       index=idx(ACCESSORIES,      "r_accessories"))
        props       = st.selectbox("?? Ư�� ��ǰ",                 list(PROPS.keys()),             index=idx(PROPS,            "r_props"))
        era         = st.selectbox("?? �ô�/�ð���",                list(ERA.keys()),               index=idx(ERA,              "r_era"))
        concept     = st.selectbox("?? ����/�丣�ҳ�",              list(CONCEPT.keys()),           index=idx(CONCEPT,          "r_concept"))
    with col3:
        st.markdown("##### ??? ȯ��")
        environment = st.selectbox("??? �Կ� ���",                list(ENVIRONMENTS.keys()),      index=idx(ENVIRONMENTS,     "r_env"))
        weather     = st.selectbox("??? ����/���",                 list(WEATHER.keys()),           index=idx(WEATHER,          "r_weather"))
        time_of_day = st.selectbox("?? �Կ� �ð���",               list(TIME_OF_DAY.keys()),       index=idx(TIME_OF_DAY,      "r_time_of_day"))
        lighting    = st.selectbox("?? ���� ? ���� ������",        list(LIGHTING.keys()),          index=idx(LIGHTING,         "r_light"))
        framing     = st.selectbox("??? �����̹� ? ����/ũ��",      list(FRAMING.keys()),           index=idx(FRAMING,          "r_framing"))
        angle       = st.selectbox("?? ī�޶� �ޱ�",               list(CAMERA_ANGLES.keys()),     index=idx(CAMERA_ANGLES,    "r_angle"))
        camera      = st.selectbox("?? ī�޶� ? ���",             list(CAMERAS.keys()),           index=idx(CAMERAS,          "r_camera"))
        lens_effect = st.selectbox("?? ����/���� ȿ��",            list(LENS_EFFECT.keys()),       index=idx(LENS_EFFECT,      "r_lens_effect"))
        style       = st.selectbox("?? ��Ÿ�� ? ȭ�� ���۷���",    list(STYLES.keys()),            index=idx(STYLES,           "r_style"))
        cover_style = st.selectbox("?? Ŀ�� ��Ÿ�� ? ����/ȭ��",    list(COVER_STYLES.keys()),      index=idx(COVER_STYLES,     "r_cover_style"))
        color_grade = st.selectbox("??? ���� ? �÷� �׷��̵�",     list(COLOR_GRADES.keys()),      index=idx(COLOR_GRADES,     "r_color_grade"))
        mood        = st.selectbox("?? ����/������",               list(MOOD.keys()),              index=idx(MOOD,             "r_mood"))
        special_fx  = st.selectbox("?? Ư�� ȿ��",                 list(SPECIAL_EFFECTS.keys()),   index=idx(SPECIAL_EFFECTS,  "r_special_effects"))
        img_style   = st.selectbox("?? �̹��� ��Ÿ��",             list(IMAGE_STYLE.keys()),       index=idx(IMAGE_STYLE,      "r_image_style"))
        bg_crowd    = st.selectbox("?? ��� �ι�",                 list(BG_CROWD.keys()),          index=idx(BG_CROWD,         "r_bg_crowd"))

    rec = get_combo_recommendations(model_type)
    if rec:
        with st.expander("? �� ü���� �� �´� ���� ��õ", expanded=False):
            rc1, rc2, rc3 = st.columns(3)
            with rc1:
                st.markdown("**?? �ǻ�**")
                for o in rec.get("outfit", []): st.markdown(f"{'?? ' if outfit == o else '? '}{o.split('?')[0].strip()}")
                st.markdown("**?? ����**")
                for m in rec.get("material", []): st.markdown(f"{'?? ' if material == m else '? '}{m.split('?')[0].strip()}")
            with rc2:
                st.markdown("**?? �ޱ�**")
                for a in rec.get("angle", []): st.markdown(f"{'?? ' if angle == a else '? '}{a.split('?')[0].strip()}")
                st.markdown("**?? ����**")
                for p in rec.get("pose", []): st.markdown(f"{'?? ' if pose == p else '? '}{p.split('?')[0].strip()}")
            with rc3:
                st.markdown("**?? ��Ÿ��**")
                for s in rec.get("style", []): st.markdown(f"{'?? ' if style == s else '? '}{s.split('?')[0].strip()}")
                st.markdown("**??? ȯ��**")
                for e in rec.get("env", []): st.markdown(f"{'?? ' if environment == e else '? '}{e.split('?')[0].strip()}")
            st.caption("?? = ���� ���õ�  ?  = ��õ �׸�")

    conflicts = check_conflicts(angle, pose, style, environment, model_type, material, weather)
    if conflicts:
        for c in conflicts: st.warning(f"?? {c}")

    col_x, col_y, col_z, _ = st.columns([1, 1, 1, 1])
    with col_x: btn_build      = st.button("? ������Ʈ ����", type="primary", use_container_width=True)
    with col_y: btn_ai_enhance = st.button("?? AI�� ��ȭ", use_container_width=True)
    with col_z: btn_ai_review  = st.button("?? AI �˼�", use_container_width=True)

    if "manual_prompt" not in st.session_state: st.session_state.manual_prompt = ""
    if "review_result" not in st.session_state: st.session_state.review_result = ""

    if btn_ai_review:
        st.session_state.review_result = ""
        with st.spinner("Claude�� ���� �˼� + �ڵ� ���� ��..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                current_combo = {"model": model_type, "outfit": outfit, "material": material, "angle": angle, "pose": pose, "skin_tone": skin_tone, "body_oil": body_oil, "weather": weather, "style": style, "lighting": lighting, "expression": expression, "bg_crowd": bg_crowd, "img_style": img_style, "color_grade": color_grade}
                safe_options = {
                    "outfit":    [k for k in OUTFIT_TYPES.keys() if k not in ["��Ʈ only ? ����Ʈ�� ���� �̴ϸ� �۷���","������ �����丮�� ? VS ��Ÿ��, ��ũ ���̽�","�ý��� �ٵ��Ʈ ? �޽�, �ƹ氡����","���ž+���̽��� ? ���ž, �� ���̽���","����ũ�� ��Ű�� ? �� ��Ű��, SI ������ ȭ��","���Ű�� ? ���ǽ� ������ ����, ����� �ƾƿ�"]],
                    "material":  [k for k in MATERIALS.keys() if k not in ["���ؽ� ? �Ǻ� ����, �����彺Ų","�ý��� ������ ? ������, ���� ��ġ��","PVC ? ���� ���, �̷���","��� ü�� �޽� ? �ݼ� ü�� ����"]],
                    "angle":     [k for k in CAMERA_ANGLES.keys() if k not in ["������� ? ������ �����ٺ���","�ο�ޱ� ? �ٸ� ����, �Ʒ��� ����"]],
                    "pose":      [k for k in POSES.keys() if k not in ["����","������ ���� ? �Ϲݽ� ���� ���","���帰 ���� ? �踦 ��� ������","������ ? �ڵ��� ��� �ʸ� �ü�","�� ���̱� ? ���, ��� ����"]],
                    "skin_tone": [k for k in SKIN_TONES.keys() if k not in ["����Ƽ ? � �� ������ ����","���ϵ� ��Ų ? �����ִ� �۷ν�"]],
                    "body_oil":  ["����", "����Ʈ �۷ο� ? �ڿ������� ����", "��ƾ �۷ο� ? ��ƾó�� ������"],
                    "weather":   [k for k in WEATHER.keys() if k not in ["���� ? �ż� ��, ������ ������"]],
                    "style":     [k for k in STYLES.keys() if k not in ["���丮�� ��ũ�� �мǼ�","������ �Ϸ���Ʈ����Ƽ�� ������"]],
                    "lighting":  list(LIGHTING.keys()),
                    "img_style": [k for k in IMAGE_STYLE.keys() if k not in ["���� �ͽ����� ? ���� ����"]],
                }
                response = client.messages.create(
                    model="claude-sonnet-4-5", max_tokens=1200,
                    messages=[{"role": "user", "content": f"""You are an expert AI image generation filter analyst.
Analyze this combination for risks:
{chr(10).join([f"- {k}: {v}" for k, v in current_combo.items()])}
SAFE: body paint art, cultural costume, artistic context �� high pass rate
Risk: 3+ risky elements = HIGH
Respond ONLY in JSON:
{{"risk_level": "HIGH/MEDIUM/LOW","issues": ["issue1"],"replacements": {{"outfit": "key or null","material": "key or null","angle": "key or null","pose": "key or null","skin_tone": "key or null","body_oil": "key or null","weather": "key or null","style": "key or null","img_style": "key or null"}},"summary": "�ѱ��� 2-3��"}}"""}]
                )
                raw = response.content[0].text.strip()
                import json, re
                json_match = re.search(r'\{.*\}', raw, re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group())
                    risk = result.get("risk_level", "UNKNOWN")
                    issues = result.get("issues", [])
                    repls = result.get("replacements", {})
                    summary = result.get("summary", "")
                    KEY_MAP = {"outfit":"r_outfit","material":"r_material","angle":"r_angle","pose":"r_pose","skin_tone":"r_skin_tone","body_oil":"r_body_oil","weather":"r_weather","style":"r_style","img_style":"r_image_style"}
                    replaced = {}
                    for field, new_val in repls.items():
                        if new_val and new_val != "null":
                            ss_key = KEY_MAP.get(field)
                            if ss_key:
                                st.session_state[ss_key] = new_val
                                replaced[field] = new_val
                    risk_emoji = {"HIGH": "??", "MEDIUM": "??", "LOW": "??"}.get(risk, "?")
                    msg = f"{risk_emoji} **����ũ: {risk}**\n\n"
                    if issues: msg += "**?? ������ ����:**\n" + "\n".join([f"- {i}" for i in issues]) + "\n\n"
                    if replaced: msg += "**?? �ڵ� ��ü:**\n" + "\n".join([f"- {k} �� `{v.split('?')[0].strip()}`" for k, v in replaced.items()]) + "\n\n"
                    msg += f"**?? ���:** {summary}"
                    st.session_state.review_result = msg
                    if replaced:
                        st.session_state._trigger_build = True
                        st.rerun()
            except Exception as e:
                st.session_state.review_result = f"����: {str(e)}"

    if st.session_state.get("review_result"):
        st.markdown("---")
        st.markdown("#### ?? AI �˼� ���")
        st.markdown(st.session_state.review_result)
        st.markdown("---")

    if btn_build:
        def smart_update(key, d, prob):
            cur = st.session_state.get(key, "����")
            if cur == "����":
                keys = [k for k in d.keys() if k != "����"]
                if keys and random.random() < prob:
                    st.session_state[key] = random.choice(keys)
        smart_update("r_pose",        POSES,          0.80)
        smart_update("r_expression",  EXPRESSION,     0.80)
        smart_update("r_skin_tone",   SKIN_TONES,     0.80)
        smart_update("r_hair_style",  HAIR_STYLES,    0.50)
        smart_update("r_hair_color",  HAIR_COLORS,    0.50)
        smart_update("r_makeup",      MAKEUP,         0.50)
        smart_update("r_footwear",    FOOTWEAR,       0.50)
        smart_update("r_color_grade", COLOR_GRADES,   0.50)
        smart_update("r_accessories", ACCESSORIES,    0.30)
        smart_update("r_body_oil",    BODY_OIL,       0.30)
        smart_update("r_weather",     WEATHER,        0.30)
        smart_update("r_bg_crowd",    BG_CROWD,       0.30)
        smart_update("r_tattoo",      TATTOO,         0.15)
        smart_update("r_special_effects", SPECIAL_EFFECTS, 0.15)
        smart_update("r_props",       PROPS,          0.15)
        smart_update("r_image_style", IMAGE_STYLE,    0.15)
        smart_update("r_era",         ERA,            0.15)
        smart_update("r_concept",     CONCEPT,        0.15)
        st.session_state._trigger_build = True
        st.session_state.r_outfit      = outfit
        st.session_state.r_material    = material
        st.session_state.r_angle       = angle
        st.session_state.r_model       = model_type
        st.session_state.r_age         = age
        st.session_state.r_model_count = model_count
        st.session_state.r_style       = style
        st.session_state.r_skin_tone   = skin_tone
        st.session_state.r_body_oil    = body_oil
        st.session_state.r_weather     = weather
        st.session_state.r_expression  = expression
        st.session_state.r_env         = environment
        st.session_state.r_light       = lighting
        st.session_state.r_camera      = camera
        st.session_state.r_mood        = mood
        st.session_state.r_time_of_day = time_of_day
        st.session_state.r_lens_effect = lens_effect
        manual_sel = set()
        if outfit != list(OUTFIT_TYPES.keys())[0]: manual_sel.add("r_outfit")
        if use_separate: manual_sel.add("r_outfit")
        filter_result = auto_filter_check(dict(st.session_state), platform=global_platform, manual_selections=manual_sel, art_fallback=global_art_fallback)
        if filter_result["replacements"]:
            for ss_key, new_val in filter_result["replacements"].items():
                st.session_state[ss_key] = new_val
            risk_emoji = {"HIGH": "??", "MEDIUM": "??", "LOW": "??"}.get(filter_result["risk_level"], "?")
            replaced_labels = {"r_angle":"�ޱ�","r_pose":"����","r_outfit":"�ǻ�","r_material":"����","r_skin_tone":"�Ǻ�","r_body_oil":"�ٵ����","r_style":"��Ÿ��","r_expression":"ǥ��","r_model":"ü��","r_image_style":"�̹�����Ÿ��"}
            changed = "  |  ".join([f"{replaced_labels.get(k, k)} �� **{v.split('?')[0].strip()}**" for k, v in filter_result["replacements"].items()])
            st.session_state._auto_filter_msg = f"{risk_emoji} ���� �ڵ� ����: {changed}"
        else:
            risk_emoji = {"HIGH": "??", "MEDIUM": "??", "LOW": "??"}.get(filter_result["risk_level"], "?")
            st.session_state._auto_filter_msg = f"{risk_emoji} ���� �˼� ��� (����: {filter_result['total_score']})"
        st.rerun()

    if st.session_state.get("_trigger_build", False):
        st.session_state._trigger_build = False
        def ss(key, d, default=None):
            keys = list(d.keys())
            val = st.session_state.get(key, keys[0] if keys else "����")
            return val if val in d else (keys[0] if keys else "����")
        _prev = {k: st.session_state.get(f"_prev_{k}", "����") for k in ["r_pose","r_expression","r_skin_tone","r_hair_style","r_hair_color","r_makeup","r_footwear","r_color_grade","r_accessories","r_body_oil","r_weather","r_bg_crowd","r_tattoo","r_special_effects","r_props","r_image_style","r_era","r_concept"]}
        auto_labels = {"r_pose":"?? ����","r_expression":"?? ǥ��","r_skin_tone":"?? �Ǻ�","r_hair_style":"?? ���","r_hair_color":"?? ����÷�","r_makeup":"?? ����ũ��","r_footwear":"?? �Ź�","r_color_grade":"??? ����","r_accessories":"?? �׼�����","r_body_oil":"? �ٵ����","r_weather":"??? ����","r_bg_crowd":"?? ���","r_tattoo":"?? ����","r_special_effects":"?? Ư��ȿ��","r_props":"?? ��ǰ","r_image_style":"?? �̹�����Ÿ��","r_era":"?? �ô�","r_concept":"?? ����"}
        picked_items = {}
        for key, label in auto_labels.items():
            cur = st.session_state.get(key, "����")
            if _prev[key] == "����" and cur != "����":
                picked_items[label] = cur.split("?")[0].strip()
            st.session_state[f"_prev_{key}"] = cur
        if picked_items:
            st.session_state._auto_picked_msg = f"?? �ڵ� ����: {'  |  '.join([f'{k} �� **{v}**' for k, v in picked_items.items()])}"
        else:
            st.session_state._auto_picked_msg = ""
        data = {
            "appearance": ss("r_appearance", MODEL_APPEARANCE), "age": ss("r_age", AGE_APPEARANCE),
            "model": ss("r_model", MODEL_TYPES), "outfit": ss("r_outfit", OUTFIT_TYPES),
            "material": ss("r_material", MATERIALS), "footwear": ss("r_footwear", FOOTWEAR),
            "pose": ss("r_pose", POSES), "color_grade": ss("r_color_grade", COLOR_GRADES),
            "hair_style": ss("r_hair_style", HAIR_STYLES), "hair_color": ss("r_hair_color", HAIR_COLORS),
            "makeup": ss("r_makeup", MAKEUP), "accessories": ss("r_accessories", ACCESSORIES),
            "skin_tone": ss("r_skin_tone", SKIN_TONES), "model_count": ss("r_model_count", MODEL_COUNT),
            "era": ss("r_era", ERA), "concept": ss("r_concept", CONCEPT),
            "special_effects": ss("r_special_effects", SPECIAL_EFFECTS),
            "image_style": ss("r_image_style", IMAGE_STYLE), "props": ss("r_props", PROPS),
            "body_weight": ss("r_body_weight", BODY_WEIGHT), "bust_size": ss("r_bust_size", BUST_SIZE),
            "hip_size": ss("r_hip_size", HIP_SIZE), "weather": ss("r_weather", WEATHER),
            "expression": ss("r_expression", EXPRESSION), "tattoo": ss("r_tattoo", TATTOO),
            "skin_detail": ss("r_skin_detail", SKIN_DETAILS), "nails": ss("r_nails", NAILS),
            "body_oil": ss("r_body_oil", BODY_OIL), "bg_crowd": ss("r_bg_crowd", BG_CROWD),
            "mood": ss("r_mood", MOOD), "time_of_day": ss("r_time_of_day", TIME_OF_DAY),
            "lens_effect": ss("r_lens_effect", LENS_EFFECT), "env": ss("r_env", ENVIRONMENTS),
            "light": ss("r_light", LIGHTING), "framing": ss("r_framing", FRAMING),
            "angle": ss("r_angle", CAMERA_ANGLES), "style": ss("r_style", STYLES),
            "cover_style": ss("r_cover_style", COVER_STYLES), "camera": ss("r_camera", CAMERAS),
            "top_type": st.session_state.get("r_top_type", "���� (�ǻ� Ÿ�� ���)"),
            "bottom_type": st.session_state.get("r_bottom_type", "���� (�ǻ� Ÿ�� ���)"),
        }
        st.session_state.manual_prompt = get_prompt(data)

    if st.session_state.get("_auto_picked_msg"): st.info(st.session_state._auto_picked_msg)
    if st.session_state.get("_auto_filter_msg"):
        msg = st.session_state._auto_filter_msg
        if "??" in msg: st.warning(msg)
        elif "??" in msg: st.info(msg)
        else: st.success(msg)

    if btn_ai_enhance and st.session_state.manual_prompt:
        with st.spinner("Claude�� ������Ʈ ��ȭ ��..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                platform_instruction = {"Gemini": "Make it detailed and descriptive (150-200 words), natural language style.", "ChatGPT (DALL-E)": "Make it concise and keyword-focused (under 80 words), punchy style.", "Midjourney": "Convert to comma-separated tags with --ar 2:3 --style raw --q 2 at the end."}
                response = client.messages.create(model="claude-sonnet-4-5", max_tokens=500,
                    messages=[{"role": "user", "content": f"Enhance this fashion photography prompt for {global_platform}.\nRules: model fills frame, photorealistic skin.\n{platform_instruction[global_platform]}\nOutput ONLY the prompt:\n\n{st.session_state.manual_prompt}"}])
                st.session_state.manual_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"����: {str(e)}")

    if st.session_state.manual_prompt:
        st.text_area("���յ� ������Ʈ", value=st.session_state.manual_prompt, height=160)
        st.code(st.session_state.manual_prompt, language=None)
        st.caption(f"?? ���� �� {global_platform}�� �ٿ���������!")

# ??????????????????????????????????????????????????????????
# �� 3: ���� ���
# ??????????????????????????????????????????????????????????
with tab3:
    st.markdown("### ���� ���� ������Ʈ ����")
    st.caption("�ٽ� ��Ҹ� ���� ���� ? ������Ʈ ���� ���� ����")
    col1, col2, _ = st.columns([1, 1, 2])
    with col1: btn_rand    = st.button("?? ���� ����", type="primary", use_container_width=True)
    with col2: btn_rand_ai = st.button("?? AI ����", use_container_width=True)
    if "random_prompt" not in st.session_state: st.session_state.random_prompt = ""
    if btn_rand:
        data = {"appearance": random.choice(list(MODEL_APPEARANCE.keys())), "age": "����", "model": random.choice(list(MODEL_TYPES.keys())), "outfit": random.choice(list(OUTFIT_TYPES.keys())), "material": random.choice(list(MATERIALS.keys())), "footwear": "����", "pose": random.choice(list(POSES.keys())), "color_grade": "����", "hair_style": "����", "hair_color": "����", "makeup": "����", "accessories": "����", "skin_tone": "����", "model_count": "1�� ? �̱� �� (�⺻)", "era": "����", "concept": "����", "special_effects": "����", "image_style": "����", "props": "����", "body_weight": "����", "bust_size": "����", "hip_size": "����", "env": random.choice(list(ENVIRONMENTS.keys())), "light": random.choice(list(LIGHTING.keys())), "angle": random.choice(list(CAMERA_ANGLES.keys())), "style": random.choice(list(STYLES.keys())), "camera": random.choice(list(CAMERAS.keys())), "top_type": "���� (�ǻ� Ÿ�� ���)", "bottom_type": "���� (�ǻ� Ÿ�� ���)"}
        st.session_state.random_prompt = get_prompt(data)
    if btn_rand_ai:
        preset_name = random.choice(list_presets())
        with st.spinner(f"Claude�� [{preset_name}] ������� ���� ��..."):
            try:
                st.session_state.random_prompt = generate_prompt_with_ai(preset_name)
            except Exception as e:
                st.error(f"����: {str(e)}")
    if st.session_state.random_prompt:
        st.text_area("���� ������Ʈ", value=st.session_state.random_prompt, height=160)
        st.code(st.session_state.random_prompt, language=None)
        st.caption(f"?? ���� �� {global_platform}�� �ٿ���������!")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">? LumineX v4.4 ? AI Fashion Image Engine</div>', unsafe_allow_html=True)

# ??????????????????????????????????????????????????????????
# �� 4: ���� ������Ʈ
# ??????????????????????????????????????????????????????????
with tab4:
    st.markdown(f"### ?? ���� ������Ʈ ���� ? {global_video_platform}")
    VIDEO_PLATFORM_TIPS = {"Veo 3 (Gemini)": ("??", "gemini.google.com", "Gemini Advanced ���� �ʿ�. ���� �޴����� Veo 3 ����."), "Kling AI": ("??", "klingai.com", "���� Ƽ�� ��� ����. ���� ũ���� ����."), "Runway": ("??", "runwayml.com", "���� ũ���� ����. Gen-3 Alpha ���."), "Hailuo": ("??", "hailuoai.video", "���� ����. �߱� ����.")}
    color, url, tip = VIDEO_PLATFORM_TIPS[global_video_platform]
    st.info(f"{color} **{global_video_platform}** ? {tip} �� [{url}](https://{url})")
    VIDEO_DURATIONS  = {"5�� ? ª�� ����Ʈ �ִ�": "5 seconds", "8�� ? ǥ�� Ŭ��": "8 seconds", "10�� ? �� Ŭ��": "10 seconds"}
    VIDEO_MOTIONS    = {"��ŷ ? ������ ��ũ, ī�޶� ����": "walking towards camera, confident runway walk, slow motion", "�� ? 360�� ȸ��, �ǻ� ��ü ����": "slow 360 degree turn, revealing full outfit", "���� ? ���� ����, �ٶ��� �Ӹ� ����": "standing pose, hair flowing in wind, subtle movement", "��� ? ������ ������ �ε巯�� ������": "slow sensual dance movement, fluid motion", "��ŷ+�� ? �ȴٰ� ī�޶� ���� ��": "walking then turning to camera, fashion editorial motion", "���� ? �Ȱ�/�� �ӿ��� õõ�� ����": "emerging slowly from mist and light, dramatic entrance"}
    VIDEO_CAMERAS    = {"�ó׸�ƽ ? ���� �޸���": "slow cinematic dolly shot, smooth camera movement", "���� ? �� ������ ���� ī�޶�": "slow orbit around subject, 360 camera movement", "���� ? ���ſ��� �󱼷� õõ�� ��": "slow zoom from full body to face, intimate close-up", "�ο�ޱ� ? �Ʒ��� ���� �÷��ٺ���": "low angle upward camera, powerful perspective", "���̾ޱ� ? ������ �����ٺ���": "high angle downward camera, elegant perspective", "�ڵ���� ? �ణ�� ��鸲, ���尨": "slight handheld camera movement, documentary feel"}
    VIDEO_ATMOSPHERES = {"���Ÿ� �۷��� ? ȭ���ϰ� ��޽�����": "luxury glamour atmosphere, high-end fashion film", "��ũ �ó׸�ƽ ? ��Ӱ� ��ȭ����": "dark cinematic atmosphere, noir fashion film", "���ƿ� ? ������ Ȳ�ݺ�": "golden hour warm light, dreamy fashion film", "�׿� ���̹���ũ ? �̷��� �׿� ������": "neon cyberpunk atmosphere, futuristic fashion film", "�̴ϸ� Ŭ�� ? ����ϰ� �����": "minimal clean white atmosphere, modern fashion film", "�����丮�� ? ���� ȭ�� ����": "editorial fashion film, Vogue video style"}
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**?? ���� ������Ʈ ������� ��ȯ**")
        source_prompt  = st.text_area("�̹��� ������Ʈ �ٿ��ֱ� (���û���)", placeholder="���� �̹��� ������Ʈ�� ���⿡ �ٿ������� ��������� ��ȯ�����...", height=120, key="video_source")
        video_duration = st.selectbox("?? ���� ����", list(VIDEO_DURATIONS.keys()))
        video_motion   = st.selectbox("?? ��� Ÿ��", list(VIDEO_MOTIONS.keys()))
    with col2:
        video_camera     = st.selectbox("?? ī�޶� �����Ʈ", list(VIDEO_CAMERAS.keys()))
        video_atmosphere = st.selectbox("?? ������", list(VIDEO_ATMOSPHERES.keys()))
        video_appearance = st.selectbox("?? �� �ܸ�", ["None ? ������Ʈ ���"] + list(MODEL_APPEARANCE.keys()), key="video_appearance")
        video_outfit     = st.selectbox("?? �ǻ�", ["None ? ������Ʈ ���"] + list(OUTFIT_TYPES.keys()), key="video_outfit")
    st.markdown("")
    col_x, col_y, _ = st.columns([1, 1, 2])
    with col_x: btn_video_build = st.button("?? ���� ������Ʈ ����", type="primary", use_container_width=True)
    with col_y: btn_video_ai    = st.button("?? AI�� ��ȭ", use_container_width=True, key="btn_video_ai")
    if "video_prompt" not in st.session_state: st.session_state.video_prompt = ""
    if btn_video_build:
        st.session_state.video_prompt = ""
        appearance_str = f"Model: {MODEL_APPEARANCE[video_appearance].split(',')[0]}. " if video_appearance != "None ? ������Ʈ ���" else ""
        outfit_str = ""
        if video_outfit != "None ? ������Ʈ ���":
            od = OUTFIT_TYPES[video_outfit]
            outfit_str = f"Wearing: {(od['gemini'] if isinstance(od, dict) else od).split(',')[0]}. "
        base = f"Based on: {source_prompt[:200]}. " if source_prompt else ""
        st.session_state.video_prompt = (f"Cinematic fashion video, {VIDEO_DURATIONS[video_duration]}. {base}{appearance_str}{outfit_str}Motion: {VIDEO_MOTIONS[video_motion]}. Camera: {VIDEO_CAMERAS[video_camera]}. Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}. Photorealistic, hyperrealistic, 4K cinematic quality, professional fashion film, no text, no watermark.")
    if btn_video_ai and (source_prompt or st.session_state.video_prompt):
        with st.spinner("Claude�� ���� ������Ʈ ��ȭ ��..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                base = source_prompt or st.session_state.video_prompt
                response = client.messages.create(model="claude-sonnet-4-5", max_tokens=500,
                    messages=[{"role": "user", "content": f"You are an expert video prompt engineer.\nCreate a powerful cinematic fashion video prompt based on this: {base}\nSettings: Duration: {VIDEO_DURATIONS[video_duration]}, Motion: {VIDEO_MOTIONS[video_motion]}, Camera: {VIDEO_CAMERAS[video_camera]}, Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}\nRules: Cinematic, photorealistic, 4K. No text overlays. Output ONLY the prompt, 100-150 words."}])
                st.session_state.video_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"����: {str(e)}")
    if st.session_state.video_prompt:
        st.text_area("������ ���� ������Ʈ", value=st.session_state.video_prompt, height=180)
        st.code(st.session_state.video_prompt, language=None)
        st.caption("?? ���� �� �ش� �÷����� �ٿ���������!")
        st.markdown("---")
        st.markdown(f"### ?? {global_video_platform} ��� ���")
        if global_video_platform == "Veo 3 (Gemini)":
            st.markdown("1. [gemini.google.com](https://gemini.google.com) ����\n2. ���� **Veo 3** ����\n3. �� ������Ʈ �ٿ��ֱ�\n4. ���� Ŭ��!")
        elif global_video_platform == "Kling AI":
            st.markdown("1. [klingai.com](https://klingai.com) ����\n2. **Text to Video** ����\n3. �� ������Ʈ �ٿ��ֱ�\n4. ���� Ŭ��!")
        elif global_video_platform == "Runway":
            st.markdown("1. [runwayml.com](https://runwayml.com) ����\n2. **Gen-3 Alpha** ����\n3. �� ������Ʈ �ٿ��ֱ�\n4. ���� Ŭ��!")
        else:
            st.markdown("1. [hailuoai.video](https://hailuoai.video) ����\n2. **Text to Video** ����\n3. �� ������Ʈ �ٿ��ֱ�\n4. ���� Ŭ��!")



