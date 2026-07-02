"""
LumineX 신규 프리셋 66종 생성 + dashboard.py 패치

[47종 기존 카테고리 추가]
- 💧 웨트&글로스: 오일/붓기 8종 + 웨트/물 8종 = 16종
- 🔥 핫&섹시: 의상최소화 8종 + 핫환경 5종 = 13종
- ✨ 소재: 소재 6종 (💋 에로틱&페티쉬)
- 💫 럭셔리글래머: 글래머환경 6종
- 🎬 에디토리얼&무드: 포즈/공간 6종

[19종 멀티 바디페인팅 추가]
- 바디페인팅 2명 + 의상 1명 트리오 6종
- 바디페인팅 1명 + 의상 1명 듀오 7종
- 의상 2명 + 바디페인팅 1명 트리오 3종 (+ 추가 3종)

실행: python preset_builders/build_new_presets_66.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(r"C:\Dev\LumineX\presets")

PRESETS = {

    # ════════════════════════════════
    # 💧 웨트&글로스 — 오일/붓기 8종
    # ════════════════════════════════

    "champagne_pour_body": {
        "tag": "Champagne Pour Body",
        "subject": "a stunning goddess-like female model",
        "body": "toned glamorous figure, full body shot",
        "outfit": "champagne being poured over her body, golden sparkling champagne cascading down her skin, soaking wet glistening",
        "material": "liquid champagne, golden sparkling droplets, wet skin",
        "environment": "luxury penthouse, marble floor, champagne bottles, celebration atmosphere",
        "lighting": "warm golden studio light, sparkling champagne highlights",
        "style": "luxury fashion editorial, champagne pour art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "wine_pour_body": {
        "tag": "Wine Pour Body",
        "subject": "a seductive glamorous female model",
        "body": "voluptuous figure, full body shot",
        "outfit": "deep red wine being poured and dripping over her body, crimson wine streams cascading down bare skin, wine-soaked glistening",
        "material": "liquid red wine, crimson drips, wet glistening skin",
        "environment": "dark luxury wine cellar, stone walls, wine barrels, dramatic atmosphere",
        "lighting": "dramatic red-toned lighting, deep shadows, wine-colored glow",
        "style": "dark luxury editorial, wine pour fine art photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "milk_pour_body": {
        "tag": "Milk Pour Body",
        "subject": "a ethereal goddess-like female model",
        "body": "slim elegant figure, full body shot",
        "outfit": "pure white milk being poured over her body, creamy white streams cascading down bare skin, milk-soaked glistening",
        "material": "liquid white milk, creamy drips, luminous wet skin",
        "environment": "pure white minimalist studio, seamless white backdrop",
        "lighting": "bright clean studio light, high key white tones",
        "style": "avant-garde fashion editorial, milk pour fine art photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    "honey_pour_body": {
        "tag": "Honey Pour Body",
        "subject": "a sensual goddess-like female model",
        "body": "voluptuous toned figure, full body shot",
        "outfit": "golden honey being poured and dripping over her body, thick amber honey streams slowly cascading down bare skin, honey-glazed glistening",
        "material": "thick liquid honey, amber golden drips, glossy honey-coated skin",
        "environment": "warm golden studio, honeycomb backdrop, amber lighting",
        "lighting": "warm amber golden light, honey-toned glow",
        "style": "luxury sensual editorial, honey pour fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "gold_paint_body": {
        "tag": "Gold Paint Body",
        "subject": "a powerful goddess-like female model",
        "body": "athletic toned figure, full body shot",
        "outfit": "liquid gold paint being poured and splashed over her body, metallic gold streams and drips covering bare skin, gold paint-soaked",
        "material": "liquid metallic gold paint, golden drips and splatter, gold-covered skin",
        "environment": "dark dramatic studio, black backdrop, gold accents",
        "lighting": "dramatic spotlight, metallic gold reflections, high contrast",
        "style": "artistic fashion editorial, gold paint pour fine art photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "paint_pour_goddess": {
        "tag": "Paint Pour Goddess",
        "subject": "an artistic goddess-like female model",
        "body": "slim elegant figure, full body shot",
        "outfit": "multiple vivid colored paints being poured simultaneously over her body, rainbow paint streams in red blue yellow green cascading down bare skin",
        "material": "liquid acrylic paints, multicolor drips and streams, paint-covered skin",
        "environment": "artist's studio, paint-splattered floor, canvas backdrop",
        "lighting": "bright even studio light, vivid color saturation",
        "style": "avant-garde art editorial, paint pour fine art photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "glitter_pour_body": {
        "tag": "Glitter Pour Body",
        "subject": "a dazzling goddess-like female model",
        "body": "slim toned figure, full body shot",
        "outfit": "cascading glitter being poured over her body, millions of gold and silver glitter particles raining down and sticking to bare skin, glitter-covered glistening",
        "material": "fine gold and silver glitter, sparkling particles, glitter-dusted luminous skin",
        "environment": "dark studio, black backdrop, glitter particles floating in air",
        "lighting": "sparkle-enhancing studio light, glitter catching light dramatically",
        "style": "glamour fashion editorial, glitter pour fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "neon_paint_pour": {
        "tag": "Neon Paint Pour",
        "subject": "a electric goddess-like female model",
        "body": "athletic slim figure, full body shot",
        "outfit": "neon fluorescent paints being poured over her body under UV blacklight, electric pink cyan yellow neon paint streams covering bare skin, UV-reactive glowing",
        "material": "UV-reactive neon fluorescent paint, electric drips and streams, neon-glowing skin",
        "environment": "dark UV blacklight studio, black backdrop, neon glow atmosphere",
        "lighting": "UV blacklight, neon fluorescent glow, electric vivid colors",
        "style": "cyberpunk art editorial, UV neon paint pour photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════
    # 💧 웨트&글로스 — 웨트/물 8종
    # ════════════════════════════════

    "shower_goddess": {
        "tag": "Shower Goddess",
        "subject": "a sensual goddess-like female model",
        "body": "toned glamorous figure, full body shot",
        "outfit": "standing in a luxury shower, water cascading over bare body, soaking wet glistening skin, water streams flowing down curves",
        "material": "flowing water, wet glistening bare skin, steam",
        "environment": "luxury marble shower, glass walls, rain shower head, steam atmosphere",
        "lighting": "soft warm shower light through steam, wet skin glow",
        "style": "luxury sensual editorial, shower fine art photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "shower_editorial": {
        "tag": "Shower Editorial",
        "subject": "a high-fashion female model",
        "body": "slim elegant figure, full body shot",
        "outfit": "standing in designer shower fully clothed in sheer wet dress, clothes soaking wet and clinging to body, editorial wet look",
        "material": "soaking wet sheer fabric clinging to body, water-drenched editorial",
        "environment": "ultra-modern minimal shower, clean white tiles, rain shower",
        "lighting": "crisp white editorial light, wet fabric highlights",
        "style": "high fashion wet editorial, shower fashion photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "rain_soaked_nude": {
        "tag": "Rain Soaked Nude",
        "subject": "a powerful goddess-like female model",
        "body": "athletic toned figure, full body shot",
        "outfit": "standing in heavy rain completely soaked, bare skin glistening with rain droplets, rain streaming down body, dramatic wet look",
        "material": "rain water, wet glistening bare skin, rain droplets",
        "environment": "dramatic outdoor night rain, wet street, rain puddle reflections, stormy atmosphere",
        "lighting": "dramatic stormy light, rain backlit by streetlights, wet pavement glow",
        "style": "dramatic fashion editorial, rain soaked fine art photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "hot_tub_goddess": {
        "tag": "Hot Tub Goddess",
        "subject": "a luxurious goddess-like female model",
        "body": "voluptuous glamorous figure, upper body shot",
        "outfit": "reclining in luxury hot tub, bubbling water and steam surrounding bare upper body, shoulders and décolletage above water, sensual wet look",
        "material": "hot tub water, steam, wet glistening bare skin, bubbles",
        "environment": "luxury outdoor hot tub, mountain or city view, night sky, steam rising",
        "lighting": "soft warm underwater hot tub light, steam glow, night atmosphere",
        "style": "luxury lifestyle editorial, hot tub fine art photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "foam_bath_goddess": {
        "tag": "Foam Bath Goddess",
        "subject": "a sensual goddess-like female model",
        "body": "glamorous figure, upper body shot",
        "outfit": "reclining in luxury bath overflowing with white foam bubbles, foam barely covering bare body, shoulders and face above foam, seductive foam bath",
        "material": "white bath foam bubbles, wet glistening bare skin above foam",
        "environment": "opulent marble bathroom, gold fixtures, candles, rose petals, luxury atmosphere",
        "lighting": "warm candlelight glow, soft romantic lighting, golden tones",
        "style": "luxury boudoir editorial, foam bath fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "waterfall_nude": {
        "tag": "Waterfall Nude",
        "subject": "a nature goddess-like female model",
        "body": "athletic toned figure, full body shot",
        "outfit": "standing under cascading tropical waterfall, powerful water falling over bare body, completely soaked, waterfall spray and mist",
        "material": "cascading waterfall water, wet glistening bare skin, mist spray",
        "environment": "lush tropical waterfall, jungle setting, crystal clear pool below, mist and spray",
        "lighting": "natural dappled tropical light through mist, waterfall glow",
        "style": "nature fine art editorial, waterfall goddess photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "ocean_nude_editorial": {
        "tag": "Ocean Nude Editorial",
        "subject": "a beach goddess-like female model",
        "body": "toned athletic figure, full body shot",
        "outfit": "emerging from ocean waves, bare body glistening with sea water, waves crashing around legs, ocean-soaked wet look",
        "material": "ocean sea water, wet glistening bare skin, sea spray",
        "environment": "dramatic ocean shore, powerful waves, golden hour beach, sea foam",
        "lighting": "golden hour warm sunlight, ocean light reflections, wave backlighting",
        "style": "beach fine art editorial, ocean goddess photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "steam_bath_goddess": {
        "tag": "Steam Bath Goddess",
        "subject": "a mysterious goddess-like female model",
        "body": "slender elegant figure, full body shot",
        "outfit": "standing in dense white steam, bare body partially obscured by swirling steam, ethereal steam-shrouded silhouette",
        "material": "white steam mist, wet glistening bare skin through steam",
        "environment": "luxury hammam or onsen, white marble, steam rising from pools",
        "lighting": "soft diffused light through steam, ethereal white glow, mysterious atmosphere",
        "style": "ethereal luxury editorial, steam bath fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════
    # 🔥 핫&섹시 — 의상 최소화 8종
    # ════════════════════════════════

    "pasties_editorial": {
        "tag": "Pasties Editorial",
        "subject": "a bold high-fashion female model",
        "body": "slim toned figure, full body shot",
        "outfit": "wearing only designer pasties and minimal bottoms, avant-garde minimal coverage editorial, artistic coverage",
        "material": "designer rhinestone pasties, minimal coverage",
        "environment": "high fashion minimalist studio, white seamless backdrop",
        "lighting": "professional fashion editorial lighting, sharp shadows",
        "style": "avant-garde fashion editorial, minimal coverage fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "body_tape_art": {
        "tag": "Body Tape Art",
        "subject": "a daring high-fashion female model",
        "body": "toned athletic figure, full body shot",
        "outfit": "strategic coverage using only black fashion tape applied as artistic design, tape as sole covering in geometric patterns, bold body tape editorial",
        "material": "black fashion body tape in artistic geometric patterns",
        "environment": "sleek dark editorial studio, dramatic backdrop",
        "lighting": "dramatic high contrast editorial lighting",
        "style": "avant-garde fashion editorial, body tape fine art photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "shibari_silk": {
        "tag": "Shibari Silk",
        "subject": "a captivating artistic female model",
        "body": "elegant slim figure, full body shot",
        "outfit": "intricate silk rope shibari bondage art wrapped decoratively around body, artistic rope patterns as sole covering, elegant rope art fashion",
        "material": "luxury silk rope in intricate decorative patterns, artistic bondage fashion",
        "environment": "minimalist Japanese-inspired studio, shoji screens, soft zen atmosphere",
        "lighting": "soft diffused Japanese aesthetic lighting, warm tones",
        "style": "avant-garde fashion editorial, shibari silk fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "invisible_dress": {
        "tag": "Invisible Dress",
        "subject": "a ethereal high-fashion female model",
        "body": "slim elegant figure, full body shot",
        "outfit": "wearing a completely transparent crystal-clear PVC dress that appears invisible, body fully visible through dress, only the dress structure faintly visible",
        "material": "completely transparent crystal-clear PVC, invisible dress effect",
        "environment": "ultra-clean white minimalist studio, seamless white backdrop",
        "lighting": "bright even white studio light highlighting transparency",
        "style": "avant-garde fashion editorial, invisible dress concept photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    "painted_jeans": {
        "tag": "Painted Jeans",
        "subject": "a bold artistic female model",
        "body": "toned figure, full body shot",
        "outfit": "topless wearing only hyper-realistic painted-on jeans as body paint, denim texture painted directly on bare legs and hips, painted jeans bodypaint with bare torso",
        "material": "trompe l'oeil body paint, hyper-realistic denim texture painted on bare skin",
        "environment": "urban street art studio, graffiti backdrop, raw concrete",
        "lighting": "urban editorial lighting, street photography feel",
        "style": "street art fashion editorial, trompe l'oeil body paint photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "wrap_sarong_nude": {
        "tag": "Wrap Sarong Nude",
        "subject": "a tropical goddess-like female model",
        "body": "toned beach figure, full body shot",
        "outfit": "wearing only a minimal sheer sarong wrap barely covering body, tropical fabric loosely draped, maximum skin exposure",
        "material": "sheer transparent tropical sarong fabric, minimal draping",
        "environment": "tropical beach paradise, turquoise ocean, white sand, palm trees",
        "lighting": "golden hour tropical sunlight, warm beach glow",
        "style": "beach luxury editorial, tropical sarong fine art photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "chain_only": {
        "tag": "Chain Only",
        "subject": "a powerful goddess-like female model",
        "body": "toned athletic figure, full body shot",
        "outfit": "wearing only strategically draped gold chain jewelry as sole covering, chains wrapped around body as artistic coverage, chain goddess editorial",
        "material": "heavy gold chain links draped as body covering, metallic chain art",
        "environment": "dark dramatic studio, black marble backdrop, edgy atmosphere",
        "lighting": "dramatic gold-enhancing spotlight, metallic chain highlights",
        "style": "dark luxury fashion editorial, chain goddess fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "ribbon_only": {
        "tag": "Ribbon Only",
        "subject": "a graceful artistic female model",
        "body": "slim elegant figure, full body shot",
        "outfit": "wearing only colorful silk ribbons wrapped and flowing around body as sole covering, ribbons as artistic coverage, ribbon goddess editorial",
        "material": "flowing silk ribbons in multiple colors wrapped around bare body",
        "environment": "clean white studio, ribbons flowing in air, dynamic movement",
        "lighting": "bright clean studio light, ribbon color saturation",
        "style": "avant-garde fashion editorial, ribbon goddess fine art photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════
    # 🔥 핫&섹시 — 핫 환경 5종
    # ════════════════════════════════

    "desert_heat_nude": {
        "tag": "Desert Heat Nude",
        "subject": "a sun-goddess female model",
        "body": "bronzed toned figure, full body shot",
        "outfit": "bare skin glistening with desert heat and sweat, minimal coverage, desert goddess editorial",
        "material": "bare bronzed sun-kissed skin, desert sand, heat shimmer",
        "environment": "vast Saharan desert, towering sand dunes, heat mirage shimmering, blazing sun",
        "lighting": "harsh midday desert sun, heat haze glow, bleached golden light",
        "style": "nature fine art editorial, desert heat nude photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "jungle_wet_goddess": {
        "tag": "Jungle Wet Goddess",
        "subject": "a wild goddess-like female model",
        "body": "athletic toned figure, full body shot",
        "outfit": "bare skin soaked from jungle rain and humidity, wet glistening body in dense tropical jungle, primal wet look",
        "material": "jungle rain water, wet glistening bare skin, tropical humidity",
        "environment": "dense tropical rainforest, giant ferns and vines, jungle rain, lush green",
        "lighting": "dappled jungle light through canopy, green-toned humid glow",
        "style": "primal nature editorial, jungle wet goddess photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "sauna_nude_editorial": {
        "tag": "Sauna Nude Editorial",
        "subject": "a sensual goddess-like female model",
        "body": "slim toned figure, full body shot",
        "outfit": "bare skin glistening with sauna heat and sweat, steam rising from hot skin, sauna goddess editorial",
        "material": "sauna steam, perspiration glistening on bare skin",
        "environment": "luxury Finnish sauna, wooden walls, hot stones, steam rising, low amber light",
        "lighting": "warm amber sauna glow, steam diffused light, intimate atmosphere",
        "style": "luxury wellness editorial, sauna nude fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "steam_room_goddess": {
        "tag": "Steam Room Goddess",
        "subject": "a mysterious goddess-like female model",
        "body": "elegant figure, full body shot",
        "outfit": "bare body surrounded by dense white steam in luxury steam room, steam partially revealing silhouette, ethereal steam goddess",
        "material": "white steam, wet glistening bare skin, steam mist",
        "environment": "luxury spa steam room, white marble tiles, intense steam atmosphere",
        "lighting": "white diffused steam light, ethereal misty glow",
        "style": "luxury spa editorial, steam room goddess photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "volcanic_heat_body": {
        "tag": "Volcanic Heat Body",
        "subject": "a fierce elemental goddess-like female model",
        "body": "powerful toned figure, full body shot",
        "outfit": "bare skin illuminated by volcanic red orange glow, skin glistening from volcanic heat, fire goddess editorial",
        "material": "volcanic heat glow on bare skin, molten light",
        "environment": "active volcanic landscape, lava flows, volcanic rock, intense orange red glow",
        "lighting": "dramatic volcanic fire glow, intense red orange illumination, extreme contrast",
        "style": "elemental fine art editorial, volcanic heat photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════
    # 💋 에로틱&페티쉬 — 소재 6종
    # ════════════════════════════════

    "liquid_latex_drip": {
        "tag": "Liquid Latex Drip",
        "subject": "a fierce goddess-like female model",
        "body": "toned athletic figure, full body shot",
        "outfit": "liquid latex being poured and dripping over body, black latex dripping and setting on bare skin, latex second-skin forming",
        "material": "liquid black latex dripping and hardening on skin, wet latex sheen",
        "environment": "dark dramatic studio, black backdrop, industrial atmosphere",
        "lighting": "dramatic high contrast spotlight, latex shine highlights",
        "style": "dark fashion editorial, liquid latex fine art photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "chrome_paint_body": {
        "tag": "Chrome Paint Body",
        "subject": "a futuristic goddess-like female model",
        "body": "slim toned figure, full body shot",
        "outfit": "entire body painted in chrome mirror silver paint, chrome body paint covering all skin, living chrome statue editorial",
        "material": "chrome mirror silver body paint, metallic reflective surface",
        "environment": "minimalist white studio, reflective surfaces, futuristic atmosphere",
        "lighting": "multi-directional chrome-enhancing light, mirror-like reflections",
        "style": "futuristic fashion editorial, chrome body paint photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    "silver_foil_body": {
        "tag": "Silver Foil Body",
        "subject": "a avant-garde goddess-like female model",
        "body": "elegant figure, full body shot",
        "outfit": "body wrapped and draped in crinkled silver metallic foil as artistic covering, silver foil sculptural fashion editorial",
        "material": "crinkled silver metallic foil sculptural draping",
        "environment": "dark studio with silver reflections, dramatic atmosphere",
        "lighting": "dramatic metallic-enhancing studio light, silver foil catch light",
        "style": "avant-garde art fashion editorial, silver foil sculpture photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "holographic_latex": {
        "tag": "Holographic Latex",
        "subject": "a futuristic goddess-like female model",
        "body": "slim toned figure, full body shot",
        "outfit": "skin-tight holographic iridescent latex catsuit, rainbow holographic shine shifting colors, second-skin holographic latex",
        "material": "holographic iridescent latex, rainbow color-shifting surface",
        "environment": "dark futuristic studio, neon accents, holographic light projections",
        "lighting": "rainbow holographic enhancing light, iridescent color play",
        "style": "futuristic fashion editorial, holographic latex photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "mirror_latex": {
        "tag": "Mirror Latex",
        "subject": "a striking goddess-like female model",
        "body": "toned figure, full body shot",
        "outfit": "mirror-finish latex outfit, perfectly reflective mirror surface latex, like wearing a liquid mirror, reflections of studio visible in outfit",
        "material": "mirror-finish ultra-reflective latex, liquid mirror surface",
        "environment": "minimalist studio, white backdrop, clean reflective surfaces",
        "lighting": "crisp multi-directional light maximizing mirror reflections",
        "style": "high concept fashion editorial, mirror latex photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    "neon_latex": {
        "tag": "Neon Latex",
        "subject": "a electric goddess-like female model",
        "body": "athletic slim figure, full body shot",
        "outfit": "neon UV-reactive fluorescent latex catsuit glowing under blacklight, electric neon pink or cyan latex second-skin",
        "material": "UV-reactive neon fluorescent latex, electric glow surface",
        "environment": "dark UV blacklight club or studio, neon atmosphere",
        "lighting": "UV blacklight, electric neon fluorescent glow, dark atmosphere",
        "style": "cyberpunk fashion editorial, neon latex UV photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════
    # 💫 럭셔리글래머 — 글래머 환경 6종
    # ════════════════════════════════

    "private_pool_villa": {
        "tag": "Private Pool Villa",
        "subject": "a luxury goddess-like female model",
        "body": "glamorous toned figure, full body shot",
        "outfit": "minimal luxury swimwear or barely-there coverage, poolside luxury goddess",
        "material": "luxury designer minimal swimwear",
        "environment": "ultra-private luxury villa infinity pool, Bali or Santorini, lush tropical or Mediterranean setting, stunning view",
        "lighting": "golden hour warm sunlight, pool water reflections, luxury glow",
        "style": "luxury lifestyle editorial, private villa pool photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "rooftop_pool_night": {
        "tag": "Rooftop Pool Night",
        "subject": "a sleek goddess-like female model",
        "body": "slim toned figure, full body shot",
        "outfit": "minimal luxury swimwear, rooftop pool night goddess",
        "material": "luxury minimal swimwear, wet look",
        "environment": "luxury rooftop infinity pool, city skyline at night, skyscrapers glowing, urban night view",
        "lighting": "city night glow, pool underwater light, ambient city lights",
        "style": "urban luxury editorial, rooftop pool night photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "penthouse_pool": {
        "tag": "Penthouse Pool",
        "subject": "a ultra-luxury goddess-like female model",
        "body": "glamorous elegant figure, full body shot",
        "outfit": "ultra-minimal luxury coverage, penthouse indoor pool goddess",
        "material": "designer minimal swimwear or luxury robe barely worn",
        "environment": "ultra-luxury penthouse private indoor pool, floor-to-ceiling windows, city panorama, marble and gold",
        "lighting": "soft luxury interior light, pool shimmer, golden hour cityscape",
        "style": "ultra-luxury lifestyle editorial, penthouse pool photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    "yacht_sunset_glam": {
        "tag": "Yacht Sunset Glam",
        "subject": "a glamorous goddess-like female model",
        "body": "toned glamorous figure, full body shot",
        "outfit": "minimal luxury yacht wear, barely-there bikini or sheer coverup, superyacht goddess",
        "material": "designer minimal yacht wear, luxury fabrics",
        "environment": "luxury superyacht deck, Mediterranean sunset, golden orange sky, ocean horizon",
        "lighting": "dramatic sunset golden hour, warm Mediterranean glow, ocean reflections",
        "style": "superyacht luxury editorial, sunset yacht photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "casino_vip_glam": {
        "tag": "Casino VIP Glam",
        "subject": "a powerful glamorous female model",
        "body": "voluptuous elegant figure, full body shot",
        "outfit": "ultra-glamorous casino VIP gown, deep plunge neckline, high slit, diamonds",
        "material": "luxury sequined or satin gown, diamond jewelry",
        "environment": "exclusive VIP casino floor, Monte Carlo or Las Vegas, roulette tables, chandeliers, opulent gold interior",
        "lighting": "warm casino chandelier glow, dramatic luxury lighting",
        "style": "casino luxury editorial, VIP glamour photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic"
    },

    "limo_glam": {
        "tag": "Limo Glam",
        "subject": "a commanding glamorous female model",
        "body": "elegant slim figure, full body shot",
        "outfit": "ultra-glamorous red carpet gown or minimal sexy ensemble inside limousine",
        "material": "luxury satin or sequined gown, designer accessories",
        "environment": "interior of stretch limousine, leather seats, champagne, ambient interior lighting, city lights through tinted windows",
        "lighting": "moody ambient limo interior light, city glow through windows",
        "style": "celebrity lifestyle editorial, limousine glamour photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════
    # 🎬 에디토리얼&무드 — 포즈/공간 6종
    # ════════════════════════════════

    "bed_editorial": {
        "tag": "Bed Editorial",
        "subject": "a sensual high-fashion female model",
        "body": "glamorous figure, full body shot",
        "outfit": "minimal silk lingerie or barely-there coverage, luxury bed editorial",
        "material": "luxury silk or satin minimal coverage",
        "environment": "ultra-luxury hotel suite or penthouse bedroom, white silk sheets, plush bedding, floor-to-ceiling windows",
        "lighting": "soft morning light through sheer curtains, intimate bedroom glow",
        "style": "luxury boudoir editorial, bed fashion photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "floor_editorial": {
        "tag": "Floor Editorial",
        "subject": "a striking high-fashion female model",
        "body": "slim elegant figure, full body shot lying or posed on floor",
        "outfit": "avant-garde fashion editorial outfit or minimal coverage, floor pose editorial",
        "material": "luxury editorial fashion or minimal coverage",
        "environment": "marble or parquet luxury interior floor, architectural space, dramatic empty room",
        "lighting": "dramatic architectural lighting from above, strong shadows on floor",
        "style": "high fashion editorial, floor composition photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    "chair_editorial": {
        "tag": "Chair Editorial",
        "subject": "a commanding high-fashion female model",
        "body": "elegant figure, full body shot",
        "outfit": "power fashion editorial outfit, seated or draped over iconic designer chair",
        "material": "luxury editorial fashion, designer accessories",
        "environment": "minimalist studio or luxury interior featuring iconic designer chair — Eames, Barcelona or throne",
        "lighting": "precise editorial lighting, dramatic shadows",
        "style": "high concept fashion editorial, chair composition photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "door_frame_glam": {
        "tag": "Door Frame Glam",
        "subject": "a seductive glamorous female model",
        "body": "toned glamorous figure, full body shot",
        "outfit": "minimal glamorous outfit or lingerie, leaning in doorframe editorial",
        "material": "minimal luxury coverage, designer details",
        "environment": "ornate hotel suite or luxury villa doorframe, dramatic threshold, light and shadow split",
        "lighting": "dramatic split light from doorway, half lit half shadow, cinematic",
        "style": "cinematic glamour editorial, door frame photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic"
    },

    "staircase_glam": {
        "tag": "Staircase Glam",
        "subject": "a commanding glamorous female model",
        "body": "elegant figure, full body shot",
        "outfit": "dramatic evening gown or ultra-glamorous outfit on grand staircase",
        "material": "luxury evening gown, dramatic trailing fabric",
        "environment": "grand ornate staircase — opera house, palace or luxury hotel, marble steps, gilded railings",
        "lighting": "grand chandelier light, dramatic staircase illumination, golden tones",
        "style": "old Hollywood glamour editorial, grand staircase photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic"
    },

    "elevator_glam": {
        "tag": "Elevator Glam",
        "subject": "a striking glamorous female model",
        "body": "slim toned figure, full body shot",
        "outfit": "ultra-chic minimal editorial outfit, mirror elevator editorial",
        "material": "sleek editorial fashion, luxury minimal",
        "environment": "luxury mirror elevator interior, reflections multiplying infinitely, gold or chrome finishes",
        "lighting": "elevator ceiling light, infinite mirror reflections, sleek modern glow",
        "style": "urban luxury editorial, elevator mirror photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic"
    },

    # ════════════════════════════════════════════════════════
    # 🎨 멀티 바디페인팅 — 바디페인팅+의상 믹스 콜라보 19종
    # ════════════════════════════════════════════════════════

    # A) 바디페인팅 2명 + 의상 1명 트리오 6종
    "trio_bodypaint_latex_frame": {
        "tag": "Trio Bodypaint Latex Frame",
        "subject": "three stunning female models — two with full body paint flanking one in latex",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: full body paint in dark abstract pattern. CENTER: skin-tight black latex catsuit as focal point. RIGHT: full body paint mirroring left in contrasting pattern. Two bodypaint models frame the latex center.",
        "material": "body paint pigments on two outer models, latex on center model",
        "environment": "dark dramatic studio, black backdrop, trio formation",
        "lighting": "dramatic trio lighting, center model spotlit, outer models in complementary light",
        "style": "avant-garde fashion editorial, bodypaint and latex trio photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_bodypaint_gown_frame": {
        "tag": "Trio Bodypaint Gown Frame",
        "subject": "three stunning female models — two with full body paint flanking one in evening gown",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: full body paint in floral or nature pattern. CENTER: dramatic gold evening gown as focal point. RIGHT: full body paint in complementary pattern. Two bodypaint models frame the gown center.",
        "material": "body paint pigments on two outer models, luxury satin gown on center",
        "environment": "glamorous studio or ballroom setting, luxury backdrop",
        "lighting": "warm glamorous trio lighting, center gown catching chandelier light",
        "style": "luxury fashion editorial, bodypaint and gown trio photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_bodypaint_leather_frame": {
        "tag": "Trio Bodypaint Leather Frame",
        "subject": "three powerful female models — two with full body paint flanking one in leather",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: full body paint in dark tribal pattern. CENTER: black leather bodysuit as powerful focal point. RIGHT: full body paint mirroring left. Two bodypaint models frame the leather center.",
        "material": "body paint on two outer models, black leather on center model",
        "environment": "dark industrial studio, dramatic dark backdrop",
        "lighting": "dramatic power lighting, hard shadows, leather shine on center",
        "style": "dark power fashion editorial, bodypaint and leather trio photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_animal_bodypaint_latex": {
        "tag": "Trio Animal Bodypaint Latex",
        "subject": "three fierce female models — two with animal body paint flanking one in latex",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: full body leopard or tiger print body paint. CENTER: skin-tight animal print latex catsuit. RIGHT: full body zebra or snake body paint. Animal theme throughout.",
        "material": "animal print body paint on outer models, animal print latex on center",
        "environment": "jungle or savanna inspired dramatic studio",
        "lighting": "wild dramatic lighting, animal energy, high contrast",
        "style": "wild fashion editorial, animal bodypaint and latex trio photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_klimt_bodypaint_gold_gown": {
        "tag": "Trio Klimt Bodypaint Gold Gown",
        "subject": "three artistic female models — two with Klimt body paint flanking one in gold gown",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: full body Klimt gold mosaic body paint. CENTER: dramatic gold sequined evening gown. RIGHT: full body Klimt pattern body paint mirroring left. Art Nouveau harmony.",
        "material": "Klimt gold body paint on outer models, gold sequined gown on center",
        "environment": "Art Nouveau inspired luxurious setting, gold accents",
        "lighting": "warm golden gallery light, Art Nouveau atmosphere",
        "style": "Art Nouveau fashion editorial, Klimt bodypaint trio photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_galaxy_bodypaint_chrome": {
        "tag": "Trio Galaxy Bodypaint Chrome",
        "subject": "three futuristic female models — two with galaxy body paint flanking one in chrome",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: full body galaxy nebula body paint, stars and cosmos. CENTER: mirror chrome catsuit as futuristic focal point. RIGHT: full body galaxy body paint mirroring left. Cosmic sci-fi theme.",
        "material": "galaxy body paint on outer models, chrome mirror catsuit on center",
        "environment": "futuristic dark studio, cosmic atmosphere, star projections",
        "lighting": "cosmic sci-fi lighting, chrome reflections, galaxy glow",
        "style": "sci-fi fashion editorial, galaxy bodypaint and chrome trio photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    # B) 바디페인팅 1명 + 의상 1명 듀오 7종
    "duo_bodypaint_latex": {
        "tag": "Duo Bodypaint Latex",
        "subject": "two stunning female models — one with full body paint, one in latex",
        "body": "two models side by side, full body shot, duo composition",
        "outfit": "LEFT: elaborate full body paint design covering entire body. RIGHT: skin-tight latex catsuit in contrasting or complementary color. Bodypaint meets latex.",
        "material": "body paint pigments on left model, latex on right model",
        "environment": "dramatic dark studio, split lighting backdrop",
        "lighting": "dramatic duo lighting highlighting both body paint and latex textures",
        "style": "avant-garde fashion editorial, bodypaint vs latex duo photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    "duo_bodypaint_gown": {
        "tag": "Duo Bodypaint Gown",
        "subject": "two stunning female models — one with full body paint, one in evening gown",
        "body": "two models, full body shot, duo composition",
        "outfit": "LEFT: full body paint in artistic pattern. RIGHT: dramatic luxury evening gown. Art meets haute couture.",
        "material": "body paint on left model, luxury gown on right model",
        "environment": "glamorous studio or gallery setting",
        "lighting": "warm glamorous duo lighting",
        "style": "luxury art fashion editorial, bodypaint and gown duo photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    "duo_bodypaint_leather": {
        "tag": "Duo Bodypaint Leather",
        "subject": "two powerful female models — one with full body paint, one in leather",
        "body": "two models, full body shot, duo composition",
        "outfit": "LEFT: full body paint in dark abstract or tribal pattern. RIGHT: black leather bodysuit or jacket. Raw art meets dark fashion.",
        "material": "dark body paint on left model, black leather on right model",
        "environment": "dark industrial editorial studio",
        "lighting": "dramatic high contrast duo lighting",
        "style": "dark fashion editorial, bodypaint and leather duo photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    "duo_bodypaint_gold_dress": {
        "tag": "Duo Bodypaint Gold Dress",
        "subject": "two dazzling female models — one with Klimt gold body paint, one in gold dress",
        "body": "two models, full body shot, duo composition",
        "outfit": "LEFT: full body Klimt-inspired gold mosaic body paint. RIGHT: gold sequined or metallic evening dress. Gold harmony.",
        "material": "gold body paint on left model, gold metallic dress on right model",
        "environment": "luxurious gold-accented setting, warm gallery atmosphere",
        "lighting": "warm golden duo lighting, gold-enhancing illumination",
        "style": "luxury art fashion editorial, gold bodypaint and dress duo photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    "duo_animal_bodypaint_latex": {
        "tag": "Duo Animal Bodypaint Latex",
        "subject": "two fierce female models — one with animal body paint, one in animal print latex",
        "body": "two models, full body shot, duo composition",
        "outfit": "LEFT: full body leopard or tiger body paint. RIGHT: leopard or tiger print latex catsuit. Wild animal duo.",
        "material": "animal body paint on left model, animal print latex on right model",
        "environment": "wild dramatic studio, jungle or savanna inspired",
        "lighting": "wild dramatic duo lighting",
        "style": "wild fashion editorial, animal bodypaint and latex duo photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    "duo_klimt_bodypaint_gown": {
        "tag": "Duo Klimt Bodypaint Gown",
        "subject": "two artistic female models — one with Klimt body paint, one in Art Nouveau gown",
        "body": "two models, full body shot, duo composition",
        "outfit": "LEFT: full body Klimt gold mosaic body paint with spiral motifs. RIGHT: Art Nouveau inspired luxury gown with gold embroidery. Klimt painting come to life.",
        "material": "Klimt gold body paint on left model, Art Nouveau luxury gown on right",
        "environment": "Art Nouveau gallery or luxury setting, gold accents",
        "lighting": "warm Art Nouveau gallery lighting",
        "style": "Art Nouveau fashion editorial, Klimt bodypaint duo photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    "duo_galaxy_bodypaint_chrome": {
        "tag": "Duo Galaxy Bodypaint Chrome",
        "subject": "two futuristic female models — one with galaxy body paint, one in chrome outfit",
        "body": "two models, full body shot, duo composition",
        "outfit": "LEFT: full body galaxy nebula body paint, cosmic stars and nebula. RIGHT: mirror chrome metallic catsuit. Cosmos meets technology.",
        "material": "galaxy body paint on left model, chrome mirror outfit on right",
        "environment": "futuristic dark cosmic studio",
        "lighting": "cosmic sci-fi duo lighting, chrome and galaxy contrast",
        "style": "sci-fi fashion editorial, galaxy bodypaint and chrome duo photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic, duo composition"
    },

    # C) 의상 2명 + 바디페인팅 1명 트리오 6종
    "trio_latex_bodypaint_center": {
        "tag": "Trio Latex Bodypaint Center",
        "subject": "three powerful female models — two in latex flanking one with full body paint",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: black latex catsuit. CENTER: spectacular full body paint as explosive focal point. RIGHT: contrasting color latex catsuit. Body paint explodes between latex.",
        "material": "latex on outer models, body paint on center model",
        "environment": "dark dramatic studio, power atmosphere",
        "lighting": "center body paint spotlit dramatically, latex models in flanking light",
        "style": "power fashion editorial, latex and bodypaint trio photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_gown_bodypaint_center": {
        "tag": "Trio Gown Bodypaint Center",
        "subject": "three elegant female models — two in evening gowns flanking one with full body paint",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: luxury evening gown in rich color. CENTER: spectacular full body paint as artistic focal point. RIGHT: contrasting luxury gown. Body art between haute couture.",
        "material": "luxury gowns on outer models, body paint on center",
        "environment": "glamorous gallery or ballroom setting",
        "lighting": "warm glamorous trio lighting, center body paint highlighted",
        "style": "luxury art fashion editorial, gown and bodypaint trio photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_leather_bodypaint_center": {
        "tag": "Trio Leather Bodypaint Center",
        "subject": "three fierce female models — two in leather flanking one with full body paint",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: black leather bodysuit. CENTER: dramatic dark body paint as fierce focal point. RIGHT: leather jacket and minimal. Dark power trio.",
        "material": "leather on outer models, dark body paint on center",
        "environment": "dark industrial studio, raw power atmosphere",
        "lighting": "dramatic hard trio lighting, strong shadows",
        "style": "dark power editorial, leather and bodypaint trio photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_bikini_bodypaint_center": {
        "tag": "Trio Bikini Bodypaint Center",
        "subject": "three stunning female models — two in luxury bikinis flanking one with full body paint",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: luxury designer bikini. CENTER: full body paint as dazzling focal point. RIGHT: contrasting designer bikini. Swimwear meets body art.",
        "material": "designer bikinis on outer models, full body paint on center",
        "environment": "luxury pool or beach setting, tropical or resort atmosphere",
        "lighting": "bright tropical sunlight or luxury pool lighting",
        "style": "luxury swimwear editorial, bikini and bodypaint trio photography",
        "quality": "shot on Hasselblad, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_sheer_bodypaint_center": {
        "tag": "Trio Sheer Bodypaint Center",
        "subject": "three ethereal female models — two in sheer outfits flanking one with full body paint",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: sheer organza or mesh editorial outfit. CENTER: elaborate full body paint as artistic centerpiece. RIGHT: sheer contrasting outfit. Transparency meets art.",
        "material": "sheer transparent fabric on outer models, body paint on center",
        "environment": "ethereal white studio or luxury setting",
        "lighting": "soft ethereal backlit trio lighting, transparency emphasized",
        "style": "ethereal fashion editorial, sheer and bodypaint trio photography",
        "quality": "shot on Phase One, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

    "trio_chrome_bodypaint_center": {
        "tag": "Trio Chrome Bodypaint Center",
        "subject": "three futuristic female models — two in chrome outfits flanking one with galaxy body paint",
        "body": "three models, full body shot, trio composition",
        "outfit": "LEFT: mirror chrome catsuit. CENTER: spectacular galaxy or cosmic body paint as sci-fi centerpiece. RIGHT: chrome metallic outfit. Cosmos between technology.",
        "material": "chrome on outer models, cosmic galaxy body paint on center",
        "environment": "futuristic dark cosmic studio, sci-fi atmosphere",
        "lighting": "cosmic sci-fi trio lighting, chrome and galaxy contrast dramatic",
        "style": "sci-fi fashion editorial, chrome and bodypaint trio photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, hyperrealistic, trio composition"
    },

}

# ── 카테고리 배치 ──
CATEGORY_MAP = {
    "💧 웨트 & 글로스": [
        "champagne_pour_body", "wine_pour_body", "milk_pour_body",
        "honey_pour_body", "gold_paint_body", "paint_pour_goddess",
        "glitter_pour_body", "neon_paint_pour",
        "shower_goddess", "shower_editorial", "rain_soaked_nude",
        "hot_tub_goddess", "foam_bath_goddess", "waterfall_nude",
        "ocean_nude_editorial", "steam_bath_goddess",
    ],
    "🔥 핫 & 섹시": [
        "pasties_editorial", "body_tape_art", "shibari_silk",
        "invisible_dress", "painted_jeans", "wrap_sarong_nude",
        "chain_only", "ribbon_only",
        "desert_heat_nude", "jungle_wet_goddess", "sauna_nude_editorial",
        "steam_room_goddess", "volcanic_heat_body",
    ],
    "💋 에로틱 & 페티쉬": [
        "liquid_latex_drip", "chrome_paint_body", "silver_foil_body",
        "holographic_latex", "mirror_latex", "neon_latex",
    ],
    "💫 럭셔리 글래머": [
        "private_pool_villa", "rooftop_pool_night", "penthouse_pool",
        "yacht_sunset_glam", "casino_vip_glam", "limo_glam",
    ],
    "🎬 에디토리얼 & 무드": [
        "bed_editorial", "floor_editorial", "chair_editorial",
        "door_frame_glam", "staircase_glam", "elevator_glam",
    ],
    "🎨 멀티 바디페인팅": [
        # A) 바디페인팅 2명 + 의상 1명
        "trio_bodypaint_latex_frame", "trio_bodypaint_gown_frame",
        "trio_bodypaint_leather_frame", "trio_animal_bodypaint_latex",
        "trio_klimt_bodypaint_gold_gown", "trio_galaxy_bodypaint_chrome",
        # B) 바디페인팅 1명 + 의상 1명
        "duo_bodypaint_latex", "duo_bodypaint_gown", "duo_bodypaint_leather",
        "duo_bodypaint_gold_dress", "duo_animal_bodypaint_latex",
        "duo_klimt_bodypaint_gown", "duo_galaxy_bodypaint_chrome",
        # C) 의상 2명 + 바디페인팅 1명
        "trio_latex_bodypaint_center", "trio_gown_bodypaint_center",
        "trio_leather_bodypaint_center", "trio_bikini_bodypaint_center",
        "trio_sheer_bodypaint_center", "trio_chrome_bodypaint_center",
    ],
}


def save_presets(presets: dict, output_dir: Path) -> list:
    output_dir.mkdir(parents=True, exist_ok=True)
    saved = []
    for name, data in presets.items():
        path = output_dir / f"{name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        saved.append(name)
        print(f"  ✅ {name}.json")
    return saved


def patch_dashboard(dashboard_path: str, category_map: dict) -> None:
    with open(dashboard_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "champagne_pour_body" in content:
        print("[SKIP] dashboard.py 이미 패치됨")
        return

    # 각 카테고리에 프리셋 추가
    patches = {
        # 💧 웨트&글로스 — jacuzzi_bubbles 뒤에 추가
        '"jacuzzi_bubbles",': '"jacuzzi_bubbles",\n        # 2026-07-02 신규 추가\n        ' +
            '\n        '.join([f'"{p}",' for p in category_map["💧 웨트 & 글로스"]]),

        # 🔥 핫&섹시 — tennis_short_dress 뒤에 추가
        '"tennis_short_dress",\n    ],': '"tennis_short_dress",\n        # 2026-07-02 신규 추가\n        ' +
            '\n        '.join([f'"{p}",' for p in category_map["🔥 핫 & 섹시"]]) + '\n    ],',

        # 💋 에로틱&페티쉬 — lap_dance_extreme 뒤에 추가
        '"lap_dance_extreme",\n    ],': '"lap_dance_extreme",\n        # 2026-07-02 신규 추가\n        ' +
            '\n        '.join([f'"{p}",' for p in category_map["💋 에로틱 & 페티쉬"]]) + '\n    ],',

        # 💫 럭셔리글래머 — baroque_glam 뒤에 추가
        '"baroque_glam",\n    ],': '"baroque_glam",\n        # 2026-07-02 신규 추가\n        ' +
            '\n        '.join([f'"{p}",' for p in category_map["💫 럭셔리 글래머"]]) + '\n    ],',

        # 🎬 에디토리얼&무드 — grain_film 뒤에 추가
        '"grain_film",\n        # 2026-06-08': '"grain_film",\n        # 2026-07-02 신규 추가\n        ' +
            '\n        '.join([f'"{p}",' for p in category_map["🎬 에디토리얼 & 무드"]]) + '\n        # 2026-06-08',
    }

    for old, new in patches.items():
        if old in content:
            content = content.replace(old, new)
            print(f"  [OK] 패치: {old[:40]}...")
        else:
            print(f"  [WARN] 앵커 미발견: {old[:40]}...")

    # 멀티 바디페인팅 — trio_chrome_bodypaint_center 추가 (환경일체 바디페인팅 앞에)
    multi_presets = '\n        '.join([f'"{p}",' for p in category_map["🎨 멀티 바디페인팅"]])
    old_multi = '"merge_butterfly_fabric",'
    new_multi = f'# 2026-07-02 바디페인팅+의상 믹스 콜라보\n        {multi_presets}\n        # 🌀 환경 일체 바디페인팅\n        "merge_butterfly_fabric",'
    if old_multi in content:
        content = content.replace(old_multi, new_multi)
        print(f"  [OK] 멀티 바디페인팅 추가")
    else:
        print(f"  [WARN] 멀티 바디페인팅 앵커 미발견")

    # SSS_TIER 추가 — 콜라보 트리오/듀오는 검증 필요하므로 패스
    # (검증 후 별도 패치)

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ dashboard.py 패치 완료")


def verify(dashboard_path: str) -> None:
    with open(dashboard_path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        "champagne_pour_body", "shower_goddess", "pasties_editorial",
        "liquid_latex_drip", "private_pool_villa", "bed_editorial",
        "duo_bodypaint_latex", "trio_bodypaint_gown_frame",
    ]
    print("\n=== 검증 ===")
    for k in checks:
        count = content.count(f'"{k}"')
        print(f"{'✅' if count >= 1 else '❌'} {k}: {count}회")


if __name__ == "__main__":
    DASHBOARD = r"C:\Dev\LumineX\dashboard.py"
    print(f"🚀 신규 프리셋 {len(PRESETS)}종 생성 + dashboard.py 패치")
    print()
    answer = input("진행할까요? (y/n): ")
    if answer.lower() != "y":
        print("취소됨")
        exit()

    print("\n[1/2] JSON 프리셋 생성...")
    saved = save_presets(PRESETS, PRESETS_DIR)
    print(f"\n✅ {len(saved)}개 JSON 저장 완료")

    print("\n[2/2] dashboard.py 패치...")
    patch_dashboard(DASHBOARD, CATEGORY_MAP)

    verify(DASHBOARD)

    print(f"\n🎉 완료! 총 {len(saved)}종 추가")
    print("다음: git add -A && git commit && git push")
