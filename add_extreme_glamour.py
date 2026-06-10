"""
add_extreme_glamour.py
=======================
🌋 익스트림 글래머 카테고리 신설 — 40종
극한 장소 × 핫&섹시 퓨전
개방형 설계 + subject/body에 섹시함 고정

실행: python add_extreme_glamour.py
"""

import json
import re
from pathlib import Path

PRESETS_DIR = Path("presets")
DASHBOARD = Path("dashboard.py")

PRESETS = {
    # ── 💧 물/젖음 계열 ────────────────────────────────────
    "uyuni_wet_silk": {
        "tag": "Uyuni Wet Silk",
        "subject": "a sensual goddess woman, wet skin glistening, soaked silk clinging to every curve",
        "body": "body-skimming silhouette, wet fabric revealing form, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Bolivia Uyuni salt flat, perfect mirror reflection of sky, infinite horizon, shallow water layer creating flawless sky reflection",
        "lighting": "golden hour light reflected in salt flat mirror, warm glow on wet skin, breathtaking symmetry",
        "style": "wet editorial fashion photography, sensual luxury salt flat, body-conscious glamour",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "dead_sea_goddess": {
        "tag": "Dead Sea Goddess",
        "subject": "a powerful sensual woman effortlessly floating, salt crystals adorning skin",
        "body": "glistening skin covered in white salt crystals, barely-there coverage, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Dead Sea at golden hour, impossibly buoyant water, white salt crystal formations on shore, hazy mineral atmosphere",
        "lighting": "warm golden hour light on crystallized skin, mineral haze glow, otherworldly atmosphere",
        "style": "salt crystal editorial, sensual mineral luxury photography, Dead Sea goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "iceland_hot_spring": {
        "tag": "Iceland Hot Spring",
        "subject": "a sensual ethereal woman emerging from geothermal waters, steam rising around her",
        "body": "wet skin glistening with mineral water, sheer wet fabric clinging, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Iceland Blue Lagoon geothermal hot spring, milky blue mineral water, volcanic rock formations, steam mist, aurora borealis faintly visible above",
        "lighting": "ethereal steam diffusion, aurora glow, milky blue water reflection on wet skin",
        "style": "geothermal goddess editorial, sensual steam luxury photography, Iceland mineral glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "maldives_underwater": {
        "tag": "Maldives Underwater",
        "subject": "a breathtaking sensual woman underwater, hair flowing like silk",
        "body": "flowing underwater silhouette, sheer fabric transparent in water, full body shot",
        "outfit": "",
        "material": "",
        "environment": "crystal clear Maldives underwater, coral reef, tropical fish, shafts of sunlight piercing turquoise water, white sand below",
        "lighting": "underwater sunlight shafts, caustic light patterns on skin, turquoise tropical glow",
        "style": "underwater fashion editorial, sensual aquatic luxury photography, Maldives goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "niagara_wet_editorial": {
        "tag": "Niagara Wet Editorial",
        "subject": "a fierce powerful woman standing before massive waterfall, completely drenched",
        "body": "soaking wet body, fabric plastered to skin, hair drenched, full body shot",
        "outfit": "",
        "material": "",
        "environment": "base of Niagara Falls, massive wall of white water behind her, spray and mist everywhere, rainbow in the mist",
        "lighting": "dramatic backlight from waterfall spray, rainbow mist glow, raw power atmosphere",
        "style": "waterfall power editorial, drenched luxury fashion photography, force of nature glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "monsoon_goddess": {
        "tag": "Monsoon Goddess",
        "subject": "a sensual woman embracing monsoon rain, soaking wet, ecstatic expression",
        "body": "rain-drenched silhouette, wet fabric transparent and clinging, full body shot",
        "outfit": "",
        "material": "",
        "environment": "tropical monsoon downpour, warm heavy rain, dramatic storm clouds, flooded street reflections, lush tropical vegetation",
        "lighting": "dramatic storm light, rain catching light like diamonds, wet pavement reflections",
        "style": "monsoon goddess editorial, rain-soaked luxury fashion photography, tropical storm glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "black_sea_midnight": {
        "tag": "Black Sea Midnight",
        "subject": "a mysterious sensual woman emerging from dark midnight waters",
        "body": "wet emerging silhouette, dark water streaming down body, barely-there coverage, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Black Sea at midnight, dark dramatic waves, moonlight on water, distant storm on horizon, dramatic dark clouds",
        "lighting": "moonlight on wet skin, dark dramatic atmosphere, silver light on black water",
        "style": "midnight emergence editorial, dark sensual luxury photography, black sea goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "amazon_river_goddess": {
        "tag": "Amazon River Goddess",
        "subject": "a primal sensual goddess rising from the Amazon, wild and untamed",
        "body": "jungle-wet skin glistening, body adorned with water droplets, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Amazon river at dawn, dense jungle canopy, morning mist on water, exotic birds, ancient trees reflected in dark water",
        "lighting": "filtered jungle dawn light, mist diffusion, green golden glow through canopy",
        "style": "amazon primal editorial, wild sensual luxury photography, jungle goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── 🔥 불/열 계열 ──────────────────────────────────────
    "lava_field_latex": {
        "tag": "Lava Field Latex",
        "subject": "a fearless sensual woman standing on active lava field, heat shimmer around her",
        "body": "second-skin silhouette, heat haze distorting edges, powerful stance, full body shot",
        "outfit": "",
        "material": "",
        "environment": "active Hawaiian lava field at night, glowing red orange lava flows, volcanic rock, intense heat shimmer, steam vents, molten glow",
        "lighting": "red orange lava glow on skin, dramatic contrast with dark volcanic rock, heat shimmer distortion",
        "style": "volcanic goddess editorial, heat shimmer luxury fashion photography, lava glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "sahara_mirage": {
        "tag": "Sahara Mirage",
        "subject": "a mirage-like sensual goddess shimmering in desert heat, barely real",
        "body": "heat-haze silhouette, sun-kissed glistening skin, barely-there coverage, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Sahara desert at peak noon heat, golden sand dunes, intense heat shimmer making everything ripple, distant mirages, blazing sun",
        "lighting": "brutal overhead desert sun, heat shimmer distortion, golden sand reflection on skin",
        "style": "desert mirage editorial, heat shimmer sensual luxury photography, Sahara goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "volcano_edge_glam": {
        "tag": "Volcano Edge Glam",
        "subject": "a fearless sensual woman at the edge of an active volcano crater",
        "body": "volcanic glow on skin, second-skin silhouette against inferno, full body shot",
        "outfit": "",
        "material": "",
        "environment": "active volcano crater edge, molten lava lake below glowing deep red, volcanic ash in air, dramatic smoke plumes, hellish beauty",
        "lighting": "infernal red orange glow from lava lake below, dramatic upward lighting, volcanic ash haze",
        "style": "volcano edge editorial, infernal luxury fashion photography, crater goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "desert_heat_body": {
        "tag": "Desert Heat Body",
        "subject": "a sun-goddess woman in extreme desert heat, skin glistening with sweat",
        "body": "sun-bronzed glistening skin, heat shimmer around silhouette, barely-there, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Death Valley salt flats at peak heat, cracked earth patterns, intense heat waves, bleached white ground, blazing sky",
        "lighting": "harsh overhead sun, bleached white ground reflection, heat distortion lines",
        "style": "desert heat editorial, extreme temperature sensual luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "bonfire_editorial": {
        "tag": "Bonfire Editorial",
        "subject": "a wild sensual woman dancing around a massive bonfire, firelight on skin",
        "body": "firelit glistening skin, dynamic movement, barely-there coverage in firelight, full body shot",
        "outfit": "",
        "material": "",
        "environment": "massive beach bonfire at night, dramatic fire sparks flying, dark ocean behind, ember glow, primal atmosphere",
        "lighting": "warm orange firelight on skin, flying sparks, deep dramatic shadows beyond fire radius",
        "style": "bonfire goddess editorial, primal fire luxury fashion photography, firelight glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "solar_flare_goddess": {
        "tag": "Solar Flare Goddess",
        "subject": "a radiant goddess woman bathed in extreme solar light, luminous beyond natural",
        "body": "luminous skin beyond human glow, sun-drenched silhouette, full body shot",
        "outfit": "",
        "material": "",
        "environment": "extreme solar environment, massive solar flare erupting behind her, corona light, impossible proximity to the sun, solar wind",
        "lighting": "blinding white gold solar light, corona halo, extreme luminosity on skin",
        "style": "solar goddess editorial, extreme light luxury fashion photography, sun goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── 💨 높이/바람 계열 ──────────────────────────────────
    "trolltunga_edge": {
        "tag": "Trolltunga Edge",
        "subject": "a fearless sensual woman at the tip of Trolltunga cliff, wind whipping fabric",
        "body": "wind-whipped silhouette, fabric flying dramatically, daring pose at cliff edge, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Norway Trolltunga cliff rock tongue 700m above fjord, dramatic valley below, moody Norwegian sky, wind-swept landscape",
        "lighting": "dramatic Nordic sky light, depth of cliff emphasizing scale, moody atmospheric glow",
        "style": "cliff edge editorial, extreme altitude sensual luxury photography, Norwegian goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "zhangjiajie_cloud": {
        "tag": "Zhangjiajie Cloud",
        "subject": "a ethereal sensual woman above the clouds on a floating mountain pillar",
        "body": "cloud-level silhouette, fabric dissolving into mist, otherworldly presence, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Zhangjiajie floating mountain pillars above cloud sea, Avatar landscape, misty valleys far below, ancient trees clinging to vertical cliffs",
        "lighting": "soft cloud-filtered light, mist diffusion, ethereal floating mountain atmosphere",
        "style": "floating mountain editorial, cloud goddess luxury fashion photography, Avatar glamour",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "aurora_bare": {
        "tag": "Aurora Bare",
        "subject": "a luminous sensual woman under the full northern lights, skin aglow",
        "body": "aurora-lit glistening skin, barely-there coverage, luminous presence, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Iceland arctic tundra, massive northern lights display in greens purples and pinks, snow-covered landscape, frozen lake reflection doubling the aurora",
        "lighting": "full aurora borealis color wash on bare skin, green purple pink light play, arctic starfield",
        "style": "aurora goddess editorial, northern lights sensual luxury photography, arctic bare glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "skydive_editorial": {
        "tag": "Skydive Editorial",
        "subject": "a fearless sensual woman in freefall, fabric and hair defying gravity",
        "body": "freefall silhouette, fabric streaming upward, adrenaline goddess, full body shot",
        "outfit": "",
        "material": "",
        "environment": "high altitude freefall above clouds, earth curvature visible below, blue sky above, clouds rushing past, pure freedom",
        "lighting": "high altitude intense sunlight, cloud formations below, dramatic sky perspective",
        "style": "freefall fashion editorial, extreme altitude sensual luxury photography, sky goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "cliff_wind_sheer": {
        "tag": "Cliff Wind Sheer",
        "subject": "a wild sensual woman on dramatic coastal cliff, gale force wind",
        "body": "wind-torn barely-there silhouette, fabric horizontal in gale, raw power, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dramatic Irish coastal cliffs, massive waves crashing hundreds of feet below, gale force wind, stormy dramatic sky, wild Atlantic",
        "lighting": "dramatic storm light, spray catching light, moody Atlantic atmosphere",
        "style": "coastal gale editorial, extreme wind sensual luxury photography, wild cliff goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "hot_air_balloon_glam": {
        "tag": "Hot Air Balloon Glam",
        "subject": "a glamorous sensual woman standing in hot air balloon basket above the world",
        "body": "elevated goddess silhouette, fabric caught in altitude wind, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Cappadocia Turkey at dawn, hundreds of colorful hot air balloons filling the sky, fairy chimney rock formations below, golden sunrise",
        "lighting": "golden Cappadocia sunrise, balloon fire glow, dawn light on skin",
        "style": "balloon goddess editorial, altitude luxury fashion photography, Cappadocia glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── 🌑 극한 자연 계열 ──────────────────────────────────
    "antelope_light_sheer": {
        "tag": "Antelope Light Sheer",
        "subject": "a sensual woman inside Antelope Canyon, light beams piercing sheer fabric",
        "body": "light-pierced translucent silhouette, shafts of light revealing form, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Lower Antelope Canyon Arizona, dramatic light beams descending from narrow slot canyon opening, swirling orange red sandstone walls, dust particles in beams",
        "lighting": "dramatic natural light shafts penetrating canyon, orange sandstone glow, dust-particle beam effect",
        "style": "canyon light editorial, light-pierced sensual luxury photography, Antelope goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "waitomo_glow_body": {
        "tag": "Waitomo Glow Body",
        "subject": "a luminous sensual woman in glowworm cave, skin reflecting thousand lights",
        "body": "skin reflecting glowworm constellation, barely-there coverage in magical darkness, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Waitomo glowworm caves New Zealand, thousands of tiny blue glowworms covering cave ceiling like stars, dark underground lake reflection, magical silence",
        "lighting": "thousands of tiny blue bioluminescent glowworm points on skin, cave darkness, water reflection doubling the lights",
        "style": "glowworm cave editorial, bioluminescent sensual luxury photography, cave goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "socotra_alien_glam": {
        "tag": "Socotra Alien Glam",
        "subject": "a otherworldly sensual woman among alien dragon blood trees",
        "body": "exotic alien-world silhouette, barely-there coverage in otherworldly setting, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Socotra Island Yemen, surreal dragon blood trees with mushroom canopy, alien landscape, dramatic sky, endemic plants found nowhere else on Earth",
        "lighting": "alien world light, dragon blood tree canopy filtering strange light, otherworldly atmosphere",
        "style": "alien world editorial, otherworldly sensual luxury photography, Socotra goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "antarctica_ice_glam": {
        "tag": "Antarctica Ice Glam",
        "subject": "a fearless sensual ice goddess in Antarctica, extreme cold beauty",
        "body": "ice-kissed luminous skin, barely-there against extreme cold backdrop, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Antarctica icebergs, impossibly blue glacial ice, penguin colony in distance, dramatic ice formations, midnight sun",
        "lighting": "Antarctica midnight sun, glacial blue ice glow, extreme clarity of polar light on skin",
        "style": "Antarctic ice editorial, extreme cold sensual luxury photography, ice goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "deep_jungle_goddess": {
        "tag": "Deep Jungle Goddess",
        "subject": "a primal sensual goddess deep in ancient jungle, wild and untamed",
        "body": "jungle-dappled skin, primal barely-there coverage, wild presence, full body shot",
        "outfit": "",
        "material": "",
        "environment": "ancient Borneo rainforest, massive tree roots, bioluminescent fungi, mist between giant trees, exotic flowers, primordial jungle atmosphere",
        "lighting": "filtered jungle light through dense canopy, bioluminescent fungi glow, green golden atmospheric light",
        "style": "jungle goddess editorial, primal sensual luxury photography, ancient rainforest glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "coral_reef_sheer": {
        "tag": "Coral Reef Sheer",
        "subject": "a sensual mermaid-like woman floating above vibrant coral reef",
        "body": "underwater flowing silhouette, sheer fabric transparent in water, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Great Barrier Reef at peak color, massive coral formations in every color, tropical fish schools, crystal clear tropical water, sunlight shafts",
        "lighting": "underwater tropical sunlight, coral color reflection on skin, caustic light patterns",
        "style": "coral reef editorial, underwater sensual luxury photography, reef goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "salt_flat_body": {
        "tag": "Salt Flat Body",
        "subject": "a sensual geometric goddess on perfect hexagonal salt flat patterns",
        "body": "clean geometric contrast against white salt, sun-kissed barely-there, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Salar de Uyuni Bolivia dry season, perfect white hexagonal salt crystal patterns, infinite white horizon, impossible blue sky contrast",
        "lighting": "brutal overhead sun on white salt, maximum contrast, perfect shadow geometry",
        "style": "salt geometry editorial, graphic sensual luxury photography, white desert goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "thunderstorm_wet": {
        "tag": "Thunderstorm Wet",
        "subject": "a powerful sensual woman in the heart of a lightning thunderstorm, drenched",
        "body": "storm-drenched silhouette, fabric plastered to body by rain, electrified presence, full body shot",
        "outfit": "",
        "material": "",
        "environment": "middle of dramatic lightning thunderstorm, multiple lightning strikes illuminating sky, heavy rain, dramatic storm clouds, raw electrical atmosphere",
        "lighting": "multiple lightning strikes illuminating everything in white, rain catching light, electric atmosphere",
        "style": "thunderstorm goddess editorial, electrified sensual luxury photography, storm drenched glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "northern_lights_body": {
        "tag": "Northern Lights Body",
        "subject": "a transcendent sensual woman with aurora colors washing over bare skin",
        "body": "aurora color-washed skin, barely-there in arctic splendor, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Norway Tromsø arctic wilderness, massive aurora borealis filling entire sky, snow-covered pine forest, frozen fjord reflection, perfect stillness",
        "lighting": "full spectrum aurora wash — green purple pink blue on skin, snow reflection, starfield above",
        "style": "aurora body editorial, northern lights sensual luxury photography, arctic goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "meteor_shower_glam": {
        "tag": "Meteor Shower Glam",
        "subject": "a cosmic sensual woman under a peak meteor shower, skin lit by falling stars",
        "body": "starlight-kissed skin, meteor trails reflecting on body, barely-there cosmic, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Atacama Desert peak meteor shower, hundreds of meteor trails crossing sky, Milky Way visible, zero light pollution, ancient desert silence",
        "lighting": "meteor trail light on skin, Milky Way glow, starfield reflection, cosmic silence",
        "style": "meteor shower editorial, cosmic sensual luxury photography, falling star goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "pamukkale_goddess": {
        "tag": "Pamukkale Goddess",
        "subject": "a sensual goddess in turquoise thermal pools on white calcium terraces",
        "body": "thermal-water-kissed skin, barely-there in mineral luxury, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Pamukkale Turkey cotton castle, blinding white calcium carbonate terraces, turquoise thermal mineral pools, dramatic valley below, cotton-white landscape",
        "lighting": "white travertine reflection, turquoise water glow on skin, dramatic Turkish sky",
        "style": "Pamukkale goddess editorial, thermal mineral sensual luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "salar_atacama_flamingo": {
        "tag": "Salar Atacama Flamingo",
        "subject": "a surreal sensual woman among pink flamingos in salt lake, exotic beauty",
        "body": "sun-bronzed barely-there, flamingo-pink atmosphere on skin, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Salar de Atacama Chile, thousands of pink flamingos in mineral salt lake, Andes volcanoes in background, pink salt water, alien landscape",
        "lighting": "pink flamingo color wash on skin, high altitude Atacama sun, volcanic backdrop",
        "style": "flamingo lake editorial, exotic sensual luxury photography, Atacama goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "bioluminescent_bay": {
        "tag": "Bioluminescent Bay",
        "subject": "a sensual goddess swimming in bioluminescent bay, body glowing blue",
        "body": "bioluminescent blue glow on wet skin, barely-there in magical waters, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Puerto Rico bioluminescent bay at midnight, every movement creating blue glowing light in water, mangrove silhouettes, star reflection, magical dinoflagellate glow",
        "lighting": "blue bioluminescent water light on skin, ripple glow patterns, midnight darkness beyond",
        "style": "bioluminescent bay editorial, glowing water sensual luxury photography, light goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "cave_waterfall_goddess": {
        "tag": "Cave Waterfall Goddess",
        "subject": "a sensual goddess behind a hidden cave waterfall, water cascading over her",
        "body": "waterfall-drenched silhouette, water streaming over skin, barely-there coverage, full body shot",
        "outfit": "",
        "material": "",
        "environment": "secret cave behind massive waterfall, looking out through curtain of falling water, lush green beyond, filtered green light, tropical paradise",
        "lighting": "green-filtered light through waterfall curtain, water catching light, emerald cave glow",
        "style": "hidden cave editorial, waterfall sensual luxury photography, secret paradise goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "red_canyon_goddess": {
        "tag": "Red Canyon Goddess",
        "subject": "a primal sensual goddess in red rock canyon, sun-baked and wild",
        "body": "sun-bronzed barely-there against red rock, primal beauty, full body shot",
        "outfit": "",
        "material": "",
        "environment": "American Southwest red rock canyon, towering vermillion sandstone walls, dramatic cloud shadows, ancient geological formations, Southwest light",
        "lighting": "dramatic Southwest canyon light, red rock color wash on skin, deep canyon shadows",
        "style": "red canyon editorial, primal sensual luxury photography, Southwest goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "glacier_melt_goddess": {
        "tag": "Glacier Melt Goddess",
        "subject": "a powerful sensual woman on ancient glacier, surrounded by meltwater",
        "body": "glacier-cold luminous skin, barely-there in ancient ice landscape, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Iceland Vatnajokull glacier, electric blue meltwater channels, ancient ice formations, crevasses of impossible blue, dramatic arctic sky",
        "lighting": "glacial blue ice reflection on skin, arctic clarity of light, electric blue meltwater glow",
        "style": "glacier goddess editorial, glacial sensual luxury photography, ancient ice glam",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "wave_barrel_goddess": {
        "tag": "Wave Barrel Goddess",
        "subject": "a fearless sensual goddess inside a massive breaking wave barrel",
        "body": "water-surrounded barely-there, inside the perfect wave tube, full body shot",
        "outfit": "",
        "material": "",
        "environment": "inside perfect breaking wave barrel, Teahupo'o Tahiti, turquoise wave wall curling overhead, coral reef visible below, white water behind",
        "lighting": "turquoise filtered light through wave wall, water caustics, emerald barrel glow on skin",
        "style": "wave barrel editorial, surfing sensual luxury photography, ocean goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "eruption_silhouette": {
        "tag": "Eruption Silhouette",
        "subject": "a fearless sensual goddess silhouetted against volcanic eruption",
        "body": "dramatic eruption-backlit silhouette, volcanic glow on skin edges, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Kilauea Hawaii active eruption, massive lava fountain behind her, ash cloud rising kilometers high, pyroclastic glow, end-of-world beauty",
        "lighting": "volcanic eruption backlight, lava fountain glow, ash cloud illuminated from within, hellish beauty",
        "style": "volcanic eruption editorial, apocalyptic sensual luxury photography, eruption goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "ice_cave_blue": {
        "tag": "Ice Cave Blue",
        "subject": "a luminous sensual woman inside electric blue glacier ice cave",
        "body": "glacial blue light on skin, barely-there in ancient ice, ethereal presence, full body shot",
        "outfit": "",
        "material": "",
        "environment": "Iceland glacier ice cave, electric blue ancient ice formations, cathedral-like ice chambers, translucent blue walls glowing from within, perfect silence",
        "lighting": "electric blue ice glow from all directions, translucent ice walls, ethereal blue wash on skin",
        "style": "ice cave editorial, glacial blue sensual luxury photography, ancient ice goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "rainbow_falls_goddess": {
        "tag": "Rainbow Falls Goddess",
        "subject": "a radiant sensual woman in a waterfall rainbow, prismatic light on skin",
        "body": "rainbow light spectrum on bare skin, waterfall mist kisses, barely-there, full body shot",
        "outfit": "",
        "material": "",
        "environment": "massive tropical waterfall with perfect rainbow, Iguazu Falls Brazil, jungle surrounding, mist clouds, prismatic light everywhere",
        "lighting": "full spectrum rainbow light on skin, waterfall mist diffusion, prismatic color wash",
        "style": "rainbow waterfall editorial, prismatic sensual luxury photography, rainbow goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
}

# ── 카테고리 목록 ──────────────────────────────────────────
CATEGORY_LIST = list(PRESETS.keys())

print("=" * 55)
print("add_extreme_glamour.py 시작")
print(f"총 {len(PRESETS)}종 프리셋 생성")
print("=" * 55)

# ── 1. JSON 파일 생성 ──────────────────────────────────────
created = []
skipped = []
for name, data in PRESETS.items():
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        skipped.append(name)
    else:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        created.append(name)

print(f"\n✅ 새로 생성: {len(created)}종")
if skipped:
    print(f"⚠️  이미 존재 (스킵): {skipped}")

# ── 2. dashboard.py 카테고리 추가 ─────────────────────────
content = DASHBOARD.read_text(encoding="utf-8")

if "익스트림 글래머" in content:
    print("\n⚠️  카테고리 이미 존재 — 스킵")
else:
    new_category = '\n    "🌋 익스트림 글래머": [\n'
    for name in CATEGORY_LIST:
        new_category += f'        "{name}",\n'
    new_category += '    ],\n'

    pattern = r'(PRESET_CATEGORIES\s*=\s*\{.*?)(^\})'
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        new_content = content[:match.end(1)] + new_category + content[match.end(1):]
        DASHBOARD.write_text(new_content, encoding="utf-8")
        print("✅ 카테고리 추가 완료: 🌋 익스트림 글래머")
    else:
        print("❌ PRESET_CATEGORIES 패턴 매칭 실패 — 수동 추가 필요")

# ── 3. 검증 ───────────────────────────────────────────────
print("\n[ 검증 ]")
for name in CATEGORY_LIST:
    path = PRESETS_DIR / f"{name}.json"
    status = "✅" if path.exists() else "❌"
    print(f"  {status} {name}.json")

verify = DASHBOARD.read_text(encoding="utf-8")
cat_status = "✅" if "익스트림 글래머" in verify else "❌"
print(f"\n  {cat_status} dashboard.py 카테고리 등록")
print(f"  총 {len(CATEGORY_LIST)}종")

print("\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "feat: 🌋 익스트림 글래머 카테고리 신설 (40종)"')
print('  git push')
