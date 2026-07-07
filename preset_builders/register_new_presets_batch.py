"""
register_new_presets_batch.py
공식 A/B/C/D + rain 시리즈 전체 등록
- JSON 파일 생성
- PRESET_CATEGORIES 추가
- HOF/SSS/SS tier 등록
"""
import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")
DASHBOARD   = Path("C:/Dev/LumineX/dashboard.py")

# ══════════════════════════════════════════════════════════
# 프리셋 데이터
# ══════════════════════════════════════════════════════════
PRESETS = {

    # ── 공식 A: 스파/바디 ──────────────────────────────────
    "oil_massage_table": {
        "tag": "Oil Massage Table",
        "subject": "a stunning female model lying face down on a luxury marble massage table",
        "body": "VS Angel body, toned flat abs, model-perfect proportions, deeply oiled bare back",
        "outfit": "lying face down on luxury marble massage table, back completely bare and glistening with massage oil, only a small white towel draped across hips, luxury spa editorial",
        "material": "white spa towel, massage oil, bare skin",
        "environment": "high-end luxury spa, marble surfaces, white orchids, warm candlelight, soft towels",
        "lighting": "soft beauty dish light, warm candlelight, skin luminosity and oil sheen",
        "style": "Harper's Bazaar sensual fashion editorial, luxury spa campaign",
        "quality": "shot on Hasselblad H6D, warm spa grade, portrait 2:3 vertical"
    },
    "mud_spa_clay": {
        "tag": "Mud Spa Clay",
        "subject": "a stunning female model lying on a luxury marble spa table covered in white clay mud mask",
        "body": "soft glamour model, polished feminine curves, bare back glistening under clay",
        "outfit": "lying on luxury marble spa table, upper body covered in white clay mud mask treatment, bare back and shoulders glistening, small white towel draped across hips only, luxury spa editorial",
        "material": "white clay mud mask, spa towel, bare skin, gold bangles",
        "environment": "high-end spa treatment room, marble surfaces, white orchids, warm candlelight, soft towels",
        "lighting": "soft beauty dish light, warm candlelight, skin luminosity beneath clay",
        "style": "Harper's Bazaar sensual fashion editorial, luxury spa campaign",
        "quality": "shot on Canon EOS R5, warm spa grade, portrait 2:3 vertical"
    },
    "hammam_marble_glam": {
        "tag": "Hammam Marble Glam",
        "subject": "a stunning female model lying on a hot marble hammam slab in an ornate Ottoman bath",
        "body": "slim toned model, lean athletic build, skin glistening with soap foam and steam",
        "outfit": "lying on hot marble hammam slab, draped only in a white cotton pestemal towel across hips, bare back and shoulders exposed, skin glistening with soap foam and steam",
        "material": "white cotton pestemal towel, soap foam, bare skin",
        "environment": "ornate Ottoman hammam, marble dome with star-shaped skylights, candlelight through steam, ancient marble slabs",
        "lighting": "soft light through marble dome skylights, steam diffusing warm glow",
        "style": "Vogue Italia high-fashion editorial, Ottoman luxury campaign",
        "quality": "shot on Phase One XT, warm marble grade, portrait 2:3 vertical"
    },
    "ryokan_hinoki_bath": {
        "tag": "Ryokan Hinoki Bath",
        "subject": "a stunning female model submerged in a traditional Japanese hinoki wooden bathtub",
        "body": "slender elegant model, graceful delicate figure, bare shoulders and collarbone visible",
        "outfit": "submerged to chest level in traditional Japanese hinoki wooden bathtub, bare shoulders and collarbone visible above steaming water, wet hair pinned up with wooden chopstick, serene expression",
        "material": "hinoki cypress wood bath, mineral water, steam",
        "environment": "traditional Japanese ryokan, hinoki cypress wood bath, bamboo garden view, snow outside shoji screen, lantern light",
        "lighting": "warm golden lantern light, steam diffusing soft glow, snow light through shoji",
        "style": "Vogue Japan high-fashion editorial, Japanese luxury onsen campaign",
        "quality": "shot on Canon EOS R5, warm Japanese grade, portrait 2:3 vertical"
    },
    "chocolate_spa_drip": {
        "tag": "Chocolate Spa Drip",
        "subject": "a stunning female model seated on a marble spa table with warm dark chocolate being poured over bare shoulders",
        "body": "athletic fitness model, defined abs, toned physique glistening with chocolate",
        "outfit": "seated on marble spa table, warm dark chocolate being poured and dripping across bare shoulders and chest, chocolate coating glistening skin, minimal white towel at hips only",
        "material": "warm dark chocolate, white spa towel, copper fondue pot",
        "environment": "luxury spa, dark marble interior, gold accents, warm amber lighting, chocolate fondue pots, orchids",
        "lighting": "warm amber candlelight, chocolate catching warm light, skin gloss and definition",
        "style": "Harper's Bazaar sensual fashion editorial, luxury chocolate spa campaign",
        "quality": "shot on Hasselblad H6D, warm amber grade, portrait 2:3 vertical"
    },
    "champagne_bubble_bath": {
        "tag": "Champagne Bubble Bath",
        "subject": "a stunning female model reclining in a luxury bathtub filled with champagne bubbles overlooking a city skyline",
        "body": "VS Angel body, toned flat abs, bare shoulders emerging from foam, diamond jewelry",
        "outfit": "reclining in oversized luxury bathtub filled with champagne bubbles, bare shoulders emerging from foam, champagne glass in hand, diamond necklace and bracelet",
        "material": "champagne foam bubbles, diamond jewelry, champagne glass",
        "environment": "penthouse bathroom, floor-to-ceiling windows, New York City skyline at night, marble bathtub, Dom Perignon, rose petals, candles",
        "lighting": "golden city lights through windows, candlelight, skin luminosity above foam",
        "style": "Vogue Paris luxury editorial, penthouse glamour campaign",
        "quality": "shot on Canon EOS R5, golden city grade, portrait 2:3 vertical"
    },
    "rose_petal_bath": {
        "tag": "Rose Petal Bath",
        "subject": "a stunning female model reclining in a deep marble bathtub filled with red and pink rose petals",
        "body": "soft glamour model, polished feminine curves, bare shoulders and collarbone visible above petal-covered water",
        "outfit": "reclining in deep marble bathtub filled with red and pink rose petals floating on water, bare shoulders and collarbone fully visible above petal-covered water, hair dramatically wet",
        "material": "red and pink rose petals, water, marble bathtub",
        "environment": "luxury villa bathroom, marble bathtub, rose petals scattered everywhere, dozens of candles, mirror walls, golden fixtures",
        "lighting": "warm candlelight, rose petals catching soft light, skin luminosity",
        "style": "Harper's Bazaar sensual fashion editorial, romantic luxury campaign",
        "quality": "shot on Canon EOS R5, warm candlelight grade, portrait 2:3 vertical"
    },

    # ── 공식 A: SSS 3종 ───────────────────────────────────
    "honey_drip_spa": {
        "tag": "Honey Drip Spa",
        "subject": "a stunning female model seated on a marble spa table with warm golden honey being poured across bare shoulders",
        "body": "VS Angel body, toned flat abs, bare back and shoulders glistening with honey",
        "outfit": "seated on marble spa table, warm golden honey being poured across bare shoulders and back, honey dripping down glistening skin, draped only in minimal white towel at hips",
        "material": "warm golden honey, white spa towel, bare skin",
        "environment": "luxury spa, warm amber lighting, marble surfaces, golden honey jars, candles, fresh flowers",
        "lighting": "warm amber candlelight, honey catching golden light, skin luminosity",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "shot on Canon EOS R5, warm amber grade, portrait 2:3 vertical"
    },
    "gold_leaf_spa": {
        "tag": "Gold Leaf Spa",
        "subject": "a stunning female model in a luxury gold spa with gold leaf flakes applied across shoulders",
        "body": "hot glamour model, dramatically cinched narrow waist, gold shimmer covering skin",
        "outfit": "gold leaf flakes applied across bare shoulders and upper body, golden shimmer covering skin, small gold silk cloth draped minimally, 24k gold spa editorial",
        "material": "24k gold leaf flakes, gold silk cloth, rhinestones",
        "environment": "ultra-luxury gold spa, mirrored walls, gold mosaic surfaces, champagne, orchids, candles",
        "lighting": "dramatic chiaroscuro, gold leaf catching warm light, skin luminosity",
        "style": "Versace campaign bold luxury glamour",
        "quality": "shot on Hasselblad H6D, golden grade, portrait 2:3 vertical"
    },
    "salt_scrub_steam": {
        "tag": "Salt Scrub Steam",
        "subject": "a stunning female model standing in a luxury steam room with sea salt scrub applied across bare back",
        "body": "slim toned model, lean athletic build, skin glistening red from heat and scrub",
        "outfit": "standing in luxury steam room, sea salt scrub applied across bare back and shoulders, skin glistening from heat, small white towel wrapped minimally at hips, steam surrounding body",
        "material": "sea salt scrub, white spa towel, eucalyptus branches",
        "environment": "luxury steam room, eucalyptus branches, marble walls, soft steam, warm candlelight, wooden spa bucket",
        "lighting": "soft warm steam-diffused light, skin glow from heat, candlelight",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "shot on Canon EOS R5, warm steam grade, portrait 2:3 vertical"
    },

    # ── 공식 B: 자연 온천/수중 ────────────────────────────
    "yunoko_bamboo_onsen": {
        "tag": "Yunoko Bamboo Onsen",
        "subject": "a stunning female model submerged in a natural outdoor hot spring surrounded by snow-covered bamboo forest",
        "body": "slender elegant model, graceful delicate figure, bare shoulders visible above steaming water",
        "outfit": "submerged to chest level in natural outdoor hot spring, bare shoulders and collarbone visible above steaming water, snow falling gently, wet hair, serene powerful expression",
        "material": "natural mineral hot spring water, steam, snow",
        "environment": "Yunoko natural hot spring Japan, snow-covered bamboo forest, stone lanterns, winter silence, steam rising dramatically",
        "lighting": "soft winter light through bamboo, steam diffusing glow, skin luminosity",
        "style": "Vogue Japan high-fashion editorial, Japanese onsen campaign",
        "quality": "shot on Canon EOS R5, cool winter grade, portrait 2:3 vertical"
    },
    "pamukkale_travertine": {
        "tag": "Pamukkale Travertine",
        "subject": "a stunning female model standing in a shallow travertine thermal pool at Pamukkale Turkey",
        "body": "VS Angel body, toned flat abs, upper body glistening, wearing minimal luxury swimwear",
        "outfit": "standing in shallow travertine thermal pool, lower body submerged in crystal blue water, luxury designer swimwear, white calcium terraces surrounding",
        "material": "luxury swimwear, thermal mineral water, white calcium travertine",
        "environment": "Pamukkale travertine terraces Turkey, white calcium formations, shallow thermal pools, sunset sky, Hierapolis ruins in distance",
        "lighting": "golden hour sunset, warm amber light, calcium terraces reflecting light",
        "style": "Vogue Italia high-fashion editorial, luxury travel campaign",
        "quality": "shot on Phase One XT, golden sunset grade, portrait 2:3 vertical"
    },
    "bhutan_himalaya_pool": {
        "tag": "Bhutan Himalaya Pool",
        "subject": "a stunning female model submerged in a sacred Himalayan hot spring with snow-capped peaks above",
        "body": "slender elegant model, graceful delicate figure, bare shoulders and collarbone visible",
        "outfit": "submerged to shoulders in sacred Himalayan hot spring, bare shoulders and collarbone visible, dramatic high altitude atmosphere",
        "material": "natural hot spring water, steam, prayer flags",
        "environment": "Bhutan Himalayan hot spring, snow-capped peaks, Buddhist prayer flags, pristine mountain air, sacred atmosphere, dramatic altitude",
        "lighting": "high altitude clear light, mountain snow reflecting, mystical atmosphere",
        "style": "Vogue high-fashion editorial, Himalayan luxury campaign",
        "quality": "shot on Canon EOS R5, high altitude grade, portrait 2:3 vertical"
    },
    "blue_lagoon_silica": {
        "tag": "Blue Lagoon Silica",
        "subject": "a stunning female model submerged in the milky blue Iceland Blue Lagoon with aurora borealis above",
        "body": "slim toned model, lean athletic build, bare shoulders visible, white silica mask on face",
        "outfit": "submerged to chest in milky blue silica geothermal lagoon, bare shoulders and collarbone visible above opaque blue water, white silica mud mask on face, aurora borealis dancing above",
        "material": "milky blue silica geothermal water, white silica mask, steam",
        "environment": "Blue Lagoon Iceland, milky turquoise geothermal water, lava rock formations, aurora borealis sky, steam rising dramatically, bridge walkway",
        "lighting": "aurora borealis ethereal glow, steam diffusing light, blue lagoon luminosity",
        "style": "Vogue editorial, Iceland luxury campaign",
        "quality": "shot on Canon EOS R5, aurora grade, portrait 2:3 vertical"
    },
    "greenland_glacier_pool": {
        "tag": "Greenland Glacier Pool",
        "subject": "a stunning female model submerged in a natural hot spring pool surrounded by glaciers and icebergs",
        "body": "slim toned model, lean athletic build, bare shoulders visible, steam rising from warm water",
        "outfit": "submerged to chest in natural hot spring pool surrounded by glaciers, bare shoulders visible, dramatic contrast of warm water steam against arctic ice",
        "material": "natural hot spring water, steam, arctic minerals",
        "environment": "Greenland arctic hot spring, glaciers and icebergs surrounding, midnight sun golden sky, pristine arctic landscape",
        "lighting": "midnight sun golden arctic light, steam catching gold glow, dramatic contrast ice vs warmth",
        "style": "Vogue high-fashion editorial, arctic luxury campaign",
        "quality": "shot on Phase One XT, arctic golden grade, portrait 2:3 vertical"
    },
    "japan_snow_onsen": {
        "tag": "Japan Snow Onsen",
        "subject": "a stunning female model submerged in a Japanese outdoor rotenburo hot spring under full moon snowfall",
        "body": "slender elegant model, graceful delicate figure, bare shoulders and collarbone visible above water",
        "outfit": "submerged to chest in outdoor rotenburo hot spring, bare shoulders and collarbone visible, heavy snowfall surrounding, snow accumulating on rocks beside pool, full moon overhead",
        "material": "natural hot spring water, steam, snow, moon light",
        "environment": "Japanese outdoor rotenburo onsen, heavy snowfall, snow-covered pine forest, stone lanterns, full moon, winter silence",
        "lighting": "moonlight through snowfall, warm lantern glow reflecting on water, skin luminosity",
        "style": "Vogue Japan high-fashion editorial, Japanese winter onsen campaign",
        "quality": "shot on Canon EOS R5, moonlit winter grade, portrait 2:3 vertical"
    },
    "hot_spring_nude_editorial": {
        "tag": "Hot Spring Nude Editorial",
        "subject": "a stunning female model submerged to chest in a natural Iceland hot spring under aurora borealis",
        "body": "soft glamour model, polished feminine curves, bare shoulders emerging from steaming mineral water",
        "outfit": "submerged to chest level in natural hot spring, bare shoulders and collarbone fully visible, steam rising around body, volcanic rock surroundings, mineral water",
        "material": "natural volcanic hot spring water, steam, mineral deposits",
        "environment": "Iceland natural hot spring, steam, volcanic black rocks, aurora borealis sky",
        "lighting": "golden hour warm backlight, steam diffusing light, skin luminosity",
        "style": "Vogue Italia high-fashion editorial, Iceland luxury campaign",
        "quality": "shot on Phase One XT, aurora grade, portrait 2:3 vertical"
    },

    # ── 공식 B: SSS 2종 ───────────────────────────────────
    "new_zealand_geyser": {
        "tag": "New Zealand Geyser",
        "subject": "a stunning female model standing waist-deep in a geothermal hot spring pool with geyser erupting behind",
        "body": "athletic fitness model, defined abs, bare shoulders and upper body visible",
        "outfit": "standing waist-deep in geothermal hot spring pool, wearing luxury athletic swimwear, bare shoulders visible, dramatic geyser erupting behind",
        "material": "luxury athletic swimwear, geothermal mineral water",
        "environment": "Rotorua New Zealand geothermal area, active geysers erupting, mineral pools, volcanic terrain, steam vents, dramatic sky",
        "lighting": "dramatic backlight through steam, volcanic glow, rim light",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "shot on Canon EOS R5, volcanic drama grade, portrait 2:3 vertical"
    },
    "costa_rica_jungle_pool": {
        "tag": "Costa Rica Jungle Pool",
        "subject": "a stunning female model in a natural jungle hot spring pool with tropical waterfall nearby",
        "body": "soft glamour model, polished feminine curves, wearing luxury tropical swimwear",
        "outfit": "submerged to chest in natural jungle hot spring pool, wearing luxury tropical print bikini, bare shoulders visible above emerald water, tropical waterfall cascading nearby",
        "material": "luxury tropical bikini, emerald mineral water, tropical flowers",
        "environment": "Costa Rica jungle thermal pool, tropical waterfall, ferns and jungle vines, exotic birds, emerald mineral water, lush vegetation",
        "lighting": "dappled jungle light, golden shafts through canopy, skin luminosity",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "shot on Canon EOS R5, tropical jungle grade, portrait 2:3 vertical"
    },

    # ── 공식 C: 풀/이머전스 ───────────────────────────────
    "niagara_mist_goddess": {
        "tag": "Niagara Mist Goddess",
        "subject": "a stunning female model standing near Niagara Falls soaked by waterfall mist",
        "body": "soft glamour model, polished feminine curves, wearing minimal white string bikini soaked by mist",
        "outfit": "standing near Niagara Falls, wearing minimal white string bikini, fabric soaked and semi-transparent from waterfall mist, water streaming down skin, dramatic waterfall behind",
        "material": "white string bikini, waterfall mist, water spray",
        "environment": "Niagara Falls viewpoint, massive cascading waterfalls, rainbow in mist, dramatic water spray, rocky cliffs",
        "lighting": "dramatic waterfall backlight, rainbow light through mist, water spray catching light",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "shot on Canon EOS R5, dramatic waterfall grade, portrait 2:3 vertical"
    },
    "greek_sea_emergence": {
        "tag": "Greek Sea Emergence",
        "subject": "a stunning female model emerging from the crystal clear Aegean sea near a Greek island village",
        "body": "hot glamour model, dramatically cinched narrow waist, wearing minimal white string bikini soaked by sea",
        "outfit": "emerging from crystal clear Aegean sea, walking toward rocky shore, water streaming from body, wearing minimal white string bikini, soaking wet",
        "material": "white string bikini, Aegean sea water",
        "environment": "Greek island rocky coastline, crystal clear Aegean sea, white village on cliff above, bougainvillea flowers, golden hour sunset",
        "lighting": "golden Mediterranean sunset, water catching golden light, rim light from sun",
        "style": "Sports Illustrated swimsuit editorial, Greek luxury campaign",
        "quality": "shot on Canon EOS R5, golden Mediterranean grade, portrait 2:3 vertical"
    },
    "morocco_riad_pool": {
        "tag": "Morocco Riad Pool",
        "subject": "a stunning female model emerging from an ornate Moroccan riad pool wearing gold string bikini",
        "body": "luxury glamour model, sophisticated voluptuous elegance, wearing gold metallic string bikini",
        "outfit": "emerging from ornate Moroccan riad pool, wearing minimal gold metallic string bikini, water streaming down skin, intricate tilework surrounding pool, orange blossom petals floating on water",
        "material": "gold metallic string bikini, riad pool water, orange blossom petals",
        "environment": "luxury Moroccan riad, ornate zellige tilework pool, orange blossom petals on water, golden lanterns, carved archways, night atmosphere",
        "lighting": "warm lantern light reflecting on water and skin, soft Moroccan evening light",
        "style": "Vogue Paris luxury editorial, Moroccan luxury campaign",
        "quality": "shot on Phase One XT, warm Moroccan lantern grade, portrait 2:3 vertical"
    },

    # ── 공식 C: SSS 1종 ───────────────────────────────────
    "lagoon_surface_break": {
        "tag": "Lagoon Surface Break",
        "subject": "a stunning female model breaking through a turquoise lagoon surface in a dynamic splash",
        "body": "VS Angel body, toned flat abs, wearing minimal string bikini, dynamic water action",
        "outfit": "breaking through turquoise lagoon surface, arms raised, water exploding around her, wearing minimal string bikini, dynamic action shot",
        "material": "minimal string bikini, crystal turquoise lagoon water",
        "environment": "crystal turquoise lagoon, coral reef below surface, dramatic blue sky, tropical paradise",
        "lighting": "tropical midday sun, water refracting bright light, dramatic overhead sun through water",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "shot on Canon EOS R5, tropical action grade, portrait 2:3 vertical"
    },

    # ── 공식 D: 웨트 드레스 ───────────────────────────────
    "dubai_rooftop_storm": {
        "tag": "Dubai Rooftop Storm",
        "subject": "a stunning female model in a rain-soaked silk dress on a Dubai penthouse rooftop with lightning",
        "body": "hot glamour model, dramatically cinched narrow waist, wet hair dramatically plastered",
        "outfit": "wearing ivory silk bias-cut gown caught in sudden rooftop downpour, rain-saturated luxury fashion campaign, wet hair dramatically plastered, fabric darkened and weighted by rainfall, wet couture editorial",
        "material": "ivory silk bias-cut gown, rain-soaked fabric",
        "environment": "Dubai luxury penthouse rooftop, Burj Khalifa view, heavy rainfall, lightning in distance, wet marble floor reflections, city lights bokeh",
        "lighting": "dramatic rim backlight, lightning illumination, rain streaks catching light",
        "style": "Versace campaign bold luxury glamour",
        "quality": "shot on Phase One XT, dramatic storm grade, portrait 2:3 vertical"
    },
    "amalfi_cliff_storm": {
        "tag": "Amalfi Cliff Storm",
        "subject": "a stunning female model in a rain-soaked white lace dress on an Amalfi Coast cliff during a storm",
        "body": "slim toned model, lean athletic build, wet hair, intense storm expression",
        "outfit": "wearing white silk chiffon maxi dress soaked by Mediterranean storm, wet couture editorial, rain-drenched luxury fashion, fabric clinging and darkened by water, sheer from rain",
        "material": "white silk chiffon maxi dress, rain-soaked lace",
        "environment": "Amalfi Coast cliff terrace, Positano village behind, Mediterranean sea below, dramatic storm clouds, rain-soaked terrace, lightning",
        "lighting": "dramatic storm backlight, lightning illumination, Mediterranean storm light",
        "style": "Dolce and Gabbana Italian glamour editorial",
        "quality": "shot on Canon EOS R5, dramatic Italian storm grade, portrait 2:3 vertical"
    },
    "santorini_aegean_storm": {
        "tag": "Santorini Aegean Storm",
        "subject": "a stunning female model in a rain-soaked white dress on Santorini cliff during an Aegean storm",
        "body": "slim elegant model, graceful delicate figure, wind-blown hair, rain-soaked",
        "outfit": "wearing white linen dress soaked by Aegean storm, wet Mediterranean fashion editorial, fabric semi-transparent from rain, hair dramatically wind-blown, cliffside drama",
        "material": "white linen dress, rain-soaked fabric",
        "environment": "Santorini cliff, blue dome church, Aegean sea stormy below, dramatic storm clouds, rain-soaked white buildings, lightning over sea",
        "lighting": "dramatic storm backlight over Aegean, lightning illumination, wet white surfaces reflecting",
        "style": "Vogue Paris luxury editorial",
        "quality": "shot on Phase One XT, Aegean storm grade, portrait 2:3 vertical"
    },
    "venice_acqua_alta": {
        "tag": "Venice Acqua Alta",
        "subject": "a stunning female model in a gold evening gown standing in flooded Venice Piazza San Marco",
        "body": "hot glamour model, dramatically cinched narrow waist, luxury evening glamour",
        "outfit": "wearing gold silk evening gown standing in flooded Venice Piazza San Marco, wet couture editorial, ankles in floodwater, fabric spreading dramatically in shallow floodwater",
        "material": "gold silk evening gown, Venice floodwater",
        "environment": "Venice flooded Piazza San Marco, St Mark's Basilica behind, ankle-deep floodwater reflecting golden palace lights, night atmosphere, lanterns",
        "lighting": "golden palace light reflecting in flood water, dramatic night editorial light",
        "style": "Dolce and Gabbana Italian glamour",
        "quality": "shot on Phase One XT, golden Venice night grade, portrait 2:3 vertical"
    },
    "lisbon_rain_tiles": {
        "tag": "Lisbon Rain Tiles",
        "subject": "a stunning female model in a rain-soaked red silk dress walking Lisbon cobblestone streets with yellow tram",
        "body": "slender elegant model, graceful delicate figure, wet hair, red lips",
        "outfit": "wearing deep red silk dress soaked by Lisbon rain, wet Portuguese fashion editorial, rain-drenched luxury silk campaign, fabric darkened and clinging dramatically",
        "material": "deep red silk dress, rain-soaked fabric",
        "environment": "Lisbon historic Alfama district, ornate azulejo tile buildings, wet cobblestone street, yellow tram 28E in background, heavy rain, warm building lights",
        "lighting": "warm street lamp light in rain, wet tile reflecting light, dramatic rain atmosphere",
        "style": "Vogue Paris sensual fashion editorial",
        "quality": "shot on Canon EOS R5, warm Lisbon night grade, portrait 2:3 vertical"
    },
    "kuala_lumpur_monsoon": {
        "tag": "Kuala Lumpur Monsoon",
        "subject": "a stunning female model in a rain-soaked silver metallic mini dress on a KL rooftop with Petronas Towers",
        "body": "VS Angel body, toned flat abs, silver metallic dress soaked by monsoon",
        "outfit": "wearing silver metallic mini dress soaked by tropical monsoon, wet luxury metallic fashion editorial, rain-saturated couture campaign, metallic fabric darkened and reflecting in rain",
        "material": "silver metallic mini dress, monsoon rain",
        "environment": "Kuala Lumpur luxury rooftop, Petronas Twin Towers behind, tropical monsoon downpour, lightning, wet marble surface",
        "lighting": "dramatic lightning backlight, Petronas towers illuminated, rain catching metallic light",
        "style": "Versace campaign bold luxury glamour",
        "quality": "shot on Phase One XT, dramatic KL storm grade, portrait 2:3 vertical"
    },
    "cape_town_atlantic_storm": {
        "tag": "Cape Town Atlantic Storm",
        "subject": "a stunning female model in a rain-soaked white shirt dress on Cape Town clifftop during Atlantic storm",
        "body": "athletic fitness model, defined abs, wet semi-transparent shirt dress, windswept energy",
        "outfit": "wearing white silk shirt dress completely soaked by Atlantic storm, wet couture editorial, fabric semi-transparent and windswept from storm, powerful windswept energy",
        "material": "white silk shirt dress, Atlantic storm rain",
        "environment": "Cape Town clifftop, Table Mountain looming behind in storm clouds, Atlantic Ocean stormy below, dramatic storm light, rain-soaked grass",
        "lighting": "dramatic storm backlight, Atlantic storm light, powerful natural drama",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "shot on Canon EOS R5, dramatic Atlantic storm grade, portrait 2:3 vertical"
    },
    "rio_corcovado_storm": {
        "tag": "Rio Corcovado Storm",
        "subject": "a stunning female model in a rain-soaked emerald green gown at Christ the Redeemer viewpoint during storm",
        "body": "hot glamour model, dramatically cinched narrow waist, wet emerald silk gown",
        "outfit": "wearing emerald green silk gown soaked by tropical storm, wet luxury couture editorial, fabric darkened and dramatic from tropical downpour, hair wild from wind and rain",
        "material": "emerald green silk gown, tropical storm rain",
        "environment": "Rio de Janeiro Christ the Redeemer viewpoint, jungle below in storm clouds, tropical lightning, heavy tropical downpour, dramatic elevated viewpoint",
        "lighting": "dramatic tropical storm backlight, lightning illumination, emerald fabric catching storm light",
        "style": "Versace campaign bold luxury glamour",
        "quality": "shot on Phase One XT, tropical storm grade, portrait 2:3 vertical"
    },
    "mumbai_monsoon_sari": {
        "tag": "Mumbai Monsoon Sari",
        "subject": "a stunning female model in a rain-soaked silk sari at Gateway of India during Mumbai monsoon",
        "body": "soft glamour model, polished feminine curves, wearing soaked silk sari, traditional Indian jewelry",
        "outfit": "wearing traditional silk sari soaked by Mumbai monsoon, wet Indian luxury fashion editorial, rain-saturated silk sari campaign, fabric clinging and darkened by heavy monsoon rain",
        "material": "silk sari, monsoon rain, traditional Indian gold jewelry",
        "environment": "Mumbai Gateway of India, Arabian Sea stormy behind, heavy monsoon rain, wet colonial architecture, dramatic storm clouds, monsoon puddle reflections",
        "lighting": "dramatic monsoon backlight, colonial building lights reflecting in rain, warm storm glow",
        "style": "Vogue India luxury editorial",
        "quality": "shot on Canon EOS R5, Mumbai monsoon grade, portrait 2:3 vertical"
    },

    # ── 공식 D: SSS 2종 ───────────────────────────────────
    "bangkok_monsoon_silk": {
        "tag": "Bangkok Monsoon Silk",
        "subject": "a stunning female model in traditional Thai silk dress walking through Bangkok temple in monsoon rain",
        "body": "VS Angel body, toned flat abs, wet hair, intense monsoon expression",
        "outfit": "wearing traditional Thai silk dress soaked by tropical monsoon, wet luxury silk editorial, rain-saturated Thai silk fashion campaign, fabric reacting dramatically to tropical downpour",
        "material": "traditional Thai silk dress, monsoon rain",
        "environment": "Bangkok golden temple courtyard Wat Phra Kaew, tropical monsoon rain, golden pagoda behind, wet temple stones, rain puddle reflections",
        "lighting": "dramatic monsoon backlight, golden temple light, rain catching warm glow",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "shot on Canon EOS R5, Thai temple storm grade, portrait 2:3 vertical"
    },
    "new_york_rooftop_rain": {
        "tag": "New York Rooftop Rain",
        "subject": "a stunning female model in a rain-soaked black silk dress on a New York City rooftop during storm",
        "body": "hot glamour model, dramatically cinched narrow waist, wet black silk dress, confident stance",
        "outfit": "wearing black silk slip dress completely soaked by heavy rain, wet luxury fashion editorial, rain-drenched couture campaign, fabric darkened and clinging, powerful confident stance despite storm",
        "material": "black silk slip dress, rain-soaked fabric",
        "environment": "New York City luxury rooftop, Manhattan skyline at night with Empire State Building, heavy rain, lightning, wet rooftop surface reflecting city lights",
        "lighting": "dramatic city light backlight, lightning flash, rain streaks catching light",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "shot on Canon EOS R5, NYC night storm grade, portrait 2:3 vertical"
    },

    # ── Rain 시리즈 ────────────────────────────────────────
    "monaco_wet_silk": {
        "tag": "Monaco Wet Silk",
        "subject": "a stunning female model in a rain-soaked ivory silk gown walking Monaco terrace during storm",
        "body": "hot glamour model, dramatically cinched narrow waist, wet silk clinging to body",
        "outfit": "wearing ivory silk bias-cut gown completely soaked, wet couture editorial, rain-saturated luxury fashion, fabric darkened and clinging to every curve, Monaco harbor storm",
        "material": "ivory silk bias-cut gown, storm rain",
        "environment": "Monaco luxury terrace overlooking harbor, heavy rain, wet marble floor, stormy Mediterranean night, superyachts in harbor below",
        "lighting": "strong rim backlight silhouette, rain streaks in light, dramatic storm atmosphere",
        "style": "Harper's Bazaar sensual fashion editorial, cinematic glamour",
        "quality": "shot on Phase One XT, Monaco storm grade, portrait 2:3 vertical"
    },
    "bali_rain_wet": {
        "tag": "Bali Rain Wet",
        "subject": "a stunning female model in a rain-soaked white dress on a Bali infinity pool during tropical downpour",
        "body": "VS Angel body, toned flat abs, wet white dress, tropical storm energy",
        "outfit": "wearing white bodycon mini dress soaked by Bali tropical downpour, wet fashion editorial in the rain, wet fabric editorial, luxury rain campaign, water streaming down body and dress",
        "material": "white bodycon mini dress, tropical storm rain",
        "environment": "luxury Bali rooftop infinity pool, tropical downpour, golden sunset behind storm clouds, ocean horizon, palm trees bending in wind",
        "lighting": "golden backlight through rain, rim light, dramatic wet atmosphere",
        "style": "Sports Illustrated swimsuit editorial, luxury fashion campaign",
        "quality": "shot on Canon EOS R5, Bali storm grade, portrait 2:3 vertical"
    },
}

# ── tier 분류 ──────────────────────────────────────────────
HOF_PRESETS = {
    "oil_massage_table", "mud_spa_clay", "hammam_marble_glam",
    "ryokan_hinoki_bath", "chocolate_spa_drip", "champagne_bubble_bath",
    "rose_petal_bath",
    "yunoko_bamboo_onsen", "pamukkale_travertine", "bhutan_himalaya_pool",
    "blue_lagoon_silica", "greenland_glacier_pool", "japan_snow_onsen",
    "hot_spring_nude_editorial",
    "niagara_mist_goddess", "greek_sea_emergence", "morocco_riad_pool",
    "dubai_rooftop_storm", "amalfi_cliff_storm", "santorini_aegean_storm",
    "venice_acqua_alta", "lisbon_rain_tiles", "kuala_lumpur_monsoon",
    "cape_town_atlantic_storm", "rio_corcovado_storm", "mumbai_monsoon_sari",
    "monaco_wet_silk", "bali_rain_wet",
}

SSS_PRESETS = HOF_PRESETS | {
    "honey_drip_spa", "gold_leaf_spa", "salt_scrub_steam",
    "new_zealand_geyser", "costa_rica_jungle_pool",
    "lagoon_surface_break",
    "bangkok_monsoon_silk", "new_york_rooftop_rain",
}

SS_PRESETS = SSS_PRESETS

# ── 카테고리 구조 ──────────────────────────────────────────
CATEGORIES = {
    "🛁 스파 & 바디 글래머": [
        "oil_massage_table", "mud_spa_clay", "hammam_marble_glam",
        "ryokan_hinoki_bath", "chocolate_spa_drip", "champagne_bubble_bath",
        "rose_petal_bath", "honey_drip_spa", "gold_leaf_spa", "salt_scrub_steam",
    ],
    "🌋 자연 온천 & 수중": [
        "yunoko_bamboo_onsen", "pamukkale_travertine", "bhutan_himalaya_pool",
        "blue_lagoon_silica", "greenland_glacier_pool", "japan_snow_onsen",
        "hot_spring_nude_editorial", "new_zealand_geyser", "costa_rica_jungle_pool",
    ],
    "💦 풀 & 이머전스": [
        "niagara_mist_goddess", "greek_sea_emergence", "morocco_riad_pool",
        "lagoon_surface_break",
    ],
    "🌧️ 웨트 드레스 글래머": [
        "dubai_rooftop_storm", "amalfi_cliff_storm", "santorini_aegean_storm",
        "venice_acqua_alta", "lisbon_rain_tiles", "kuala_lumpur_monsoon",
        "cape_town_atlantic_storm", "rio_corcovado_storm", "mumbai_monsoon_sari",
        "monaco_wet_silk", "bali_rain_wet",
        "bangkok_monsoon_silk", "new_york_rooftop_rain",
    ],
}

# ══════════════════════════════════════════════════════════
# 1. JSON 파일 생성
# ══════════════════════════════════════════════════════════
print("=" * 60)
print("[1/3] JSON 파일 생성")
created = 0
skipped = 0
for name, data in PRESETS.items():
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        skipped += 1
        continue
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {name}.json")
    created += 1
print(f"  → 생성 {created}개 / 건너뜀 {skipped}개")

# ══════════════════════════════════════════════════════════
# 2. dashboard.py — 카테고리 추가
# ══════════════════════════════════════════════════════════
print("\n[2/3] dashboard.py 카테고리 등록")
content = DASHBOARD.read_text(encoding="utf-8")

for cat_name, presets in CATEGORIES.items():
    if cat_name in content:
        print(f"  ⏭️  {cat_name} 이미 존재")
        continue
    preset_lines = "\n".join([f'        "{p}",' for p in presets])
    NEW_CAT = f'\n    "{cat_name}": [\n{preset_lines}\n    ],\n'
    # PRESET_CATEGORIES 마지막 항목 뒤에 삽입
    # 안전한 앵커: 마지막 카테고리 끝 } 앞
    anchors = ["\n}\n\n\n# HOF tier", "\n}\n\n# HOF tier", "\n}\n\n# SSS", "\n}\n\n# SS_"]
    inserted = False
    for anchor in anchors:
        if anchor in content:
            content = content.replace(anchor, NEW_CAT + anchor, 1)
            print(f"  ✅ {cat_name}")
            inserted = True
            break
    if not inserted:
        print(f"  ❌ {cat_name} — 삽입 위치 없음")

# ══════════════════════════════════════════════════════════
# 3. tier 등록
# ══════════════════════════════════════════════════════════
print("\n[3/3] tier 등록")

def add_to_tier(content, tier_var, presets_set):
    marker = f"{tier_var} = {{"
    pos = content.find(marker)
    if pos == -1:
        return content, False
    eol = content.find("\n", pos) + 1
    # 이미 등록된 항목 제외
    new_entries = []
    for p in sorted(presets_set):
        if f'"{p}"' not in content[pos:pos+5000]:
            new_entries.append(f'    "{p}",')
    if not new_entries:
        return content, None
    block = "\n".join(new_entries) + "\n"
    content = content[:eol] + block + content[eol:]
    return content, len(new_entries)

content, n = add_to_tier(content, "HOF_TIER", HOF_PRESETS)
if n is True or isinstance(n, int) and n > 0:
    print(f"  ✅ HOF_TIER {n}종 추가")
elif n is None:
    print("  ⏭️  HOF_TIER 이미 존재")
else:
    print("  ❌ HOF_TIER 위치 없음")

content, n = add_to_tier(content, "SSS_TIER", SSS_PRESETS)
if n is True or isinstance(n, int) and n > 0:
    print(f"  ✅ SSS_TIER {n}종 추가")
elif n is None:
    print("  ⏭️  SSS_TIER 이미 존재")
else:
    print("  ❌ SSS_TIER 위치 없음")

content, n = add_to_tier(content, "SS_TIER", SS_PRESETS)
if n is True or isinstance(n, int) and n > 0:
    print(f"  ✅ SS_TIER {n}종 추가")
elif n is None:
    print("  ⏭️  SS_TIER 이미 존재")
else:
    print("  ❌ SS_TIER 위치 없음")

DASHBOARD.write_text(content, encoding="utf-8")
print("\n✅ dashboard.py 저장 완료")
print("=" * 60)
print(f"🎉 완료!")
print(f"   JSON: {len(PRESETS)}종")
print(f"   카테고리: {len(CATEGORIES)}개 신설")
print(f"   HOF: {len(HOF_PRESETS)}종 / SSS: {len(SSS_PRESETS)}종")
