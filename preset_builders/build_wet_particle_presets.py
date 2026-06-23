"""
LumineX 신규 카테고리 프리셋 빌더
💧 웨트 & 글로스 (30종)
🌫️ 대기 & 파티클 (30종)

실행: python preset_builders/build_wet_particle_presets.py
출력: presets/ 하위 각 JSON 파일 생성
"""

import json
import os
from pathlib import Path

PRESET_DIR = Path(r"C:\Dev\LumineX\presets")

# ══════════════════════════════════════════════════════════
# 💧 웨트 & 글로스 (30종)
# ══════════════════════════════════════════════════════════
WET_GLOSS_PRESETS = {

    # ── 수영장/풀 (6종) ───────────────────────────────────
    "pool_surface_break": {
        "tag": "Pool Surface Break",
        "subject": "a stunning female model erupting through water surface",
        "body": "athletic toned figure, water-drenched skin, explosive energy",
        "outfit": "minimal wet swimwear, water streaming down body, skin fully revealed",
        "material": "wet lycra swimwear, water droplets, glistening skin",
        "environment": "luxury swimming pool, crystal blue water, dramatic splash explosion",
        "lighting": "bright overhead sunlight, water refraction light patterns, golden glints",
        "style": "high-speed fashion photography, Sports Illustrated aquatic editorial",
        "quality": "shot on Nikon Z9, ultra-fast shutter speed, water droplets frozen mid-air, portrait 2:3 vertical"
    },

    "pool_underwater_up": {
        "tag": "Pool Underwater Up",
        "subject": "a breathtaking female model submerged in pool, shot from below",
        "body": "graceful elongated figure, hair floating, underwater goddess",
        "outfit": "sheer wet swimsuit, fabric transparent underwater, ethereal draping",
        "material": "sheer wet nylon, water refraction, bubbles",
        "environment": "luxury pool underwater, turquoise water, light rays from surface",
        "lighting": "caustic underwater light patterns, shimmering surface light from above",
        "style": "underwater fashion editorial, ethereal aquatic photography",
        "quality": "underwater housing camera, surreal color grade, 8K clarity, portrait 2:3 vertical"
    },

    "pool_edge_dripping": {
        "tag": "Pool Edge Dripping",
        "subject": "a gorgeous female model draped over pool edge, water dripping",
        "body": "sensual curved figure, wet glistening skin, languid pose",
        "outfit": "barely-there wet bikini, water streaming down curves",
        "material": "wet fabric skin-tight, water droplets cascading",
        "environment": "infinity pool edge, city skyline beyond, golden hour",
        "lighting": "golden hour backlight, rim lighting on wet skin, deep shadows",
        "style": "luxury resort editorial, wet glamour photography",
        "quality": "shot on Phase One, ultra-sharp skin texture, portrait 2:3 vertical"
    },

    "infinity_pool_wet": {
        "tag": "Infinity Pool Wet",
        "subject": "a glamorous female model standing at infinity pool edge, soaking wet",
        "body": "tall statuesque figure, drenched hair, powerful wet presence",
        "outfit": "wet designer swimwear, water clinging to every curve",
        "material": "wet luxury fabric, metallic sheen when wet",
        "environment": "rooftop infinity pool, city skyline at dusk, water merging with horizon",
        "lighting": "dusk city glow, pool underwater lighting, blue-gold contrast",
        "style": "high-end resort campaign, architectural wet editorial",
        "quality": "shot on Hasselblad X2D, cinematic color grade, portrait 2:3 vertical"
    },

    "hot_spring_steam": {
        "tag": "Hot Spring Steam",
        "subject": "a mesmerizing female model in natural hot spring, surrounded by steam",
        "body": "relaxed sensual figure, flushed dewy skin, steam-kissed",
        "outfit": "minimal wet fabric draped, steam obscuring details elegantly",
        "material": "wet silk draping, steam condensation on skin",
        "environment": "natural volcanic hot spring, mineral blue water, steam rising",
        "lighting": "soft diffused steam light, warm mineral glow, misty atmosphere",
        "style": "natural luxury spa editorial, ethereal steam photography",
        "quality": "shot on Sony A1, dreamy soft focus, steam bokeh, portrait 2:3 vertical"
    },

    "jacuzzi_bubbles": {
        "tag": "Jacuzzi Bubbles",
        "subject": "a stunning female model in jacuzzi, surrounded by bubbles and foam",
        "body": "lush sensual figure, glowing wet skin, playful energy",
        "outfit": "bubbles strategically placed, foam partially covering, wet hair",
        "material": "foam bubbles, wet skin, champagne bubbles",
        "environment": "luxury hotel jacuzzi, marble surroundings, candles and champagne",
        "lighting": "warm candlelight, underwater jacuzzi lights, golden glow",
        "style": "boudoir luxury editorial, playful wet glamour",
        "quality": "shot on Canon R5, warm color grade, ultra-sharp bubbles, portrait 2:3 vertical"
    },

    # ── 비/폭우 (5종) ─────────────────────────────────────
    "rain_window_inside": {
        "tag": "Rain Window Inside",
        "subject": "a beautiful female model pressed against rain-streaked window glass",
        "body": "graceful lean figure, intimate presence, longing expression",
        "outfit": "sheer wet fabric against glass, rain outside, warm inside",
        "material": "sheer fabric, rain droplets on glass, condensation",
        "environment": "interior side of rain-streaked window, city lights blurred outside",
        "lighting": "neon city lights refracted through rain droplets, warm interior glow",
        "style": "cinematic noir editorial, intimate rain photography",
        "quality": "shot on Leica M11, rain bokeh, cinematic color grade, portrait 2:3 vertical"
    },

    "rain_street_soaked": {
        "tag": "Rain Street Soaked",
        "subject": "a fierce female model completely soaked in urban rain storm",
        "body": "powerful athletic figure, rain-drenched, unapologetic confidence",
        "outfit": "soaked designer outfit clinging to body, rain-transparent fabric",
        "material": "drenched fabric skin-tight, rain streaming, puddle reflections",
        "environment": "rain-slicked city street at night, neon reflections in puddles",
        "lighting": "neon signs reflected in wet pavement, dramatic street lighting",
        "style": "urban wet editorial, fashion storm photography",
        "quality": "shot on Nikon Z8, high contrast, rain streaks sharp, portrait 2:3 vertical"
    },

    "rain_studio_dramatic": {
        "tag": "Rain Studio Dramatic",
        "subject": "a dramatic female model under studio rain rig, theatrical downpour",
        "body": "sculpted powerful figure, rain-slicked skin, dramatic tension",
        "outfit": "minimal wet fashion, rain making fabric translucent",
        "material": "rain-soaked sheer fabric, water cascading",
        "environment": "dark studio setup, controlled rain rig, black background",
        "lighting": "dramatic key light catching rain streams, backlit rain curtain",
        "style": "high fashion studio wet editorial, dramatic rain photography",
        "quality": "shot on Phase One IQ4, rain streams frozen, ultra-sharp, portrait 2:3 vertical"
    },

    "monsoon_body": {
        "tag": "Monsoon Body",
        "subject": "a wild beautiful female model in tropical monsoon downpour",
        "body": "sensual natural figure, monsoon-soaked, primal energy",
        "outfit": "thin wet dress completely transparent from rain, clinging to body",
        "material": "monsoon-soaked thin cotton, completely wet through",
        "environment": "tropical street in monsoon, palm trees, warm rain",
        "lighting": "warm tropical light through rain, dramatic storm sky",
        "style": "tropical editorial, natural monsoon fashion photography",
        "quality": "shot on Canon R3, tropical color grade, rain motion blur, portrait 2:3 vertical"
    },

    "rain_car_window": {
        "tag": "Rain Car Window",
        "subject": "a mysterious female model glimpsed through rain-covered car window",
        "body": "elegant silhouette through glass, mysterious presence",
        "outfit": "sophisticated outfit glimpsed through rain distortion",
        "material": "rain-streaked glass distortion effect",
        "environment": "car interior, rain-covered window, blurred city outside",
        "lighting": "city lights distorted through rain droplets, moody interior",
        "style": "cinematic automotive editorial, mysterious rain photography",
        "quality": "shot on Sony A9III, rain bokeh, cinematic, portrait 2:3 vertical"
    },

    # ── 오일/글로스 (6종) ─────────────────────────────────
    "oil_pour_studio": {
        "tag": "Oil Pour Studio",
        "subject": "a breathtaking female model with golden oil being poured over body",
        "body": "sculpted goddess figure, oil-drenched gleaming skin, pure luxury",
        "outfit": "minimal coverage, golden oil coating entire body",
        "material": "golden body oil, liquid metal effect on skin",
        "environment": "minimal dark studio, black seamless background",
        "lighting": "dramatic side lighting catching oil sheen, golden rim light",
        "style": "luxury body oil campaign, high-gloss fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp oil texture, gold color grade, portrait 2:3 vertical"
    },

    "oil_drip_back": {
        "tag": "Oil Drip Back",
        "subject": "a stunning female model, back to camera, oil dripping down spine",
        "body": "perfect back musculature, oil highlighting every curve of spine",
        "outfit": "minimal, back fully exposed, oil the only adornment",
        "material": "clear body oil, slow drip, glistening skin",
        "environment": "dark minimalist studio, seamless background",
        "lighting": "side rim lighting emphasizing oil drips and back musculature",
        "style": "body art editorial, minimalist back photography",
        "quality": "shot on Phase One, macro oil detail, ultra-sharp, portrait 2:3 vertical"
    },

    "honey_drip_body": {
        "tag": "Honey Drip Body",
        "subject": "a sensual female model with thick golden honey dripping over her",
        "body": "lush curved figure, honey coating skin in thick golden streams",
        "outfit": "minimal, honey as adornment, golden sticky coating",
        "material": "thick raw honey, golden viscous drips, sticky gloss",
        "environment": "warm golden studio, honeycomb props, amber lighting",
        "lighting": "warm amber backlight through honey, golden hour studio",
        "style": "surreal food art editorial, honey goddess photography",
        "quality": "shot on Canon R5, macro honey texture, amber color grade, portrait 2:3 vertical"
    },

    "chocolate_pour_gloss": {
        "tag": "Chocolate Pour Gloss",
        "subject": "a gorgeous female model with dark chocolate being poured over body",
        "body": "sensual figure, chocolate coating curves in rich dark streams",
        "outfit": "minimal, chocolate as couture, dark glossy coating",
        "material": "liquid dark chocolate, glossy rich coating, sensual texture",
        "environment": "dark studio, chocolate brown tones, minimal props",
        "lighting": "dramatic single source catching chocolate sheen, deep shadows",
        "style": "surreal editorial, luxury chocolate campaign photography",
        "quality": "shot on Sony A1, ultra-sharp chocolate texture, rich color grade, portrait 2:3 vertical"
    },

    "gloss_lips_drip": {
        "tag": "Gloss Lips Drip",
        "subject": "a captivating female model, extreme close-up, gloss dripping from lips",
        "body": "perfect facial features, glossy lips, intimate close-up presence",
        "outfit": "not visible, extreme beauty close-up",
        "material": "thick lip gloss, dripping slowly, wet shine",
        "environment": "dark seamless studio, minimal",
        "lighting": "beauty ring light, front-lit for maximum gloss shine",
        "style": "extreme beauty editorial, luxury lip campaign macro",
        "quality": "shot on Canon R5 100mm macro, ultra-sharp lip texture, portrait 2:3 vertical"
    },

    "chrome_gloss_body": {
        "tag": "Chrome Gloss Body",
        "subject": "a futuristic female model with chrome-like gloss coating entire body",
        "body": "perfect proportioned figure, chrome-mirrored skin, robotic beauty",
        "outfit": "chrome body paint or ultra-glossy latex, mirror-like surface",
        "material": "chrome body paint, mirror-finish latex, liquid metal",
        "environment": "white infinity studio, minimal, reflective floor",
        "lighting": "multiple light sources creating chrome reflections, studio strobes",
        "style": "futuristic editorial, chrome body art photography",
        "quality": "shot on Phase One IQ4, chrome reflections sharp, portrait 2:3 vertical"
    },

    # ── 땀/열기 (4종) ─────────────────────────────────────
    "sweat_studio_light": {
        "tag": "Sweat Studio Light",
        "subject": "a powerful female model glistening with sweat under dramatic studio light",
        "body": "athletic muscular figure, sweat highlighting every muscle definition",
        "outfit": "minimal athletic wear, sweat-drenched and clinging",
        "material": "sweat-soaked athletic fabric, glistening skin",
        "environment": "dark studio, black background, gym equipment hints",
        "lighting": "hard dramatic side light catching every sweat droplet",
        "style": "athletic body editorial, fitness glamour photography",
        "quality": "shot on Nikon Z9, ultra-sharp sweat detail, high contrast, portrait 2:3 vertical"
    },

    "after_workout_glow": {
        "tag": "After Workout Glow",
        "subject": "a radiant female model post-workout, natural sweat glow",
        "body": "fit toned figure, flushed skin, natural beauty in effort",
        "outfit": "sport bra and leggings, post-workout disheveled perfection",
        "material": "sweat-damp athletic wear, natural skin glow",
        "environment": "luxury gym interior, equipment background, natural light",
        "lighting": "natural window light, warm golden glow on sweaty skin",
        "style": "authentic fitness editorial, natural glow photography",
        "quality": "shot on Sony A7R5, natural skin tones, warm color grade, portrait 2:3 vertical"
    },

    "heat_mirage_sweat": {
        "tag": "Heat Mirage Sweat",
        "subject": "a powerful female model in desert heat, sweat and mirage distortion",
        "body": "sensual athletic figure, heat-flushed sweating skin, primal power",
        "outfit": "minimal desert fashion, sweat-soaked, heat-distressed",
        "material": "heat-worn fabric, sweat-transparent, sun-bleached",
        "environment": "desert landscape, heat mirage shimmer, blinding sun",
        "lighting": "harsh midday desert sun, heat shimmer distortion, bleached highlights",
        "style": "desert survival editorial, extreme heat fashion photography",
        "quality": "shot on Canon R3, heat distortion effect, bleached color grade, portrait 2:3 vertical"
    },

    "sauna_steam_body": {
        "tag": "Sauna Steam Body",
        "subject": "a glowing female model in private sauna, steam and sweat glow",
        "body": "relaxed sensual figure, heat-flushed dewy skin, sauna goddess",
        "outfit": "sauna towel draped minimally, steam covering strategically",
        "material": "cotton sauna towel, steam, skin glow",
        "environment": "luxury private sauna, wooden walls, steam billowing",
        "lighting": "warm sauna amber light, steam diffusion, intimate glow",
        "style": "luxury spa editorial, intimate sauna photography",
        "quality": "shot on Leica SL3, warm amber grade, steam soft focus, portrait 2:3 vertical"
    },

    # ── 결로/물방울 (4종) ─────────────────────────────────
    "condensation_skin": {
        "tag": "Condensation Skin",
        "subject": "a cool mysterious female model with condensation water droplets on skin",
        "body": "smooth perfect skin, tiny water droplets covering surface like dew",
        "outfit": "minimal, skin as canvas for condensation droplets",
        "material": "water condensation droplets on skin, cold mist effect",
        "environment": "cold minimalist studio, icy blue tones, mist",
        "lighting": "macro beauty lighting catching individual droplets, cool blue cast",
        "style": "extreme beauty editorial, macro condensation photography",
        "quality": "shot on Canon R5 macro, individual droplet sharp, cool color grade, portrait 2:3 vertical"
    },

    "ice_melt_drip": {
        "tag": "Ice Melt Drip",
        "subject": "a striking female model with ice melting and dripping across body",
        "body": "cool sculptural figure, ice water trails across skin",
        "outfit": "minimal, ice as adornment, meltwater dripping",
        "material": "melting ice, cold water trails, frost",
        "environment": "cold dark studio, ice blocks, minimal",
        "lighting": "cold blue dramatic light, ice crystal caustics",
        "style": "elemental editorial, ice art fashion photography",
        "quality": "shot on Phase One, ice crystal sharp, cold blue grade, portrait 2:3 vertical"
    },

    "dew_morning_body": {
        "tag": "Dew Morning Body",
        "subject": "a fresh ethereal female model at dawn, morning dew on skin",
        "body": "natural dewy skin, morning fresh, delicate presence",
        "outfit": "sheer morning fabric, dew-kissed, translucent in dawn light",
        "material": "morning dew droplets on skin and fabric, fresh moisture",
        "environment": "garden at dawn, morning mist, first light",
        "lighting": "soft golden dawn light, morning mist glow, dew sparkle",
        "style": "ethereal morning editorial, natural beauty photography",
        "quality": "shot on Sony A7R5, golden morning grade, dew macro detail, portrait 2:3 vertical"
    },

    "frost_breath_cold": {
        "tag": "Frost Breath Cold",
        "subject": "a fierce female model in extreme cold, breath visible, frost forming",
        "body": "strong powerful figure, cold-flushed skin, frost on eyelashes",
        "outfit": "minimal in cold, frost crystallizing on fabric",
        "material": "frost-covered fabric, ice crystals forming on hair and lashes",
        "environment": "extreme cold environment, sub-zero air, visible breath clouds",
        "lighting": "cold hard light, breath vapor backlit, ice crystal sparkle",
        "style": "extreme editorial, winter survival fashion photography",
        "quality": "shot on Nikon Z9, breath vapor frozen, cold blue grade, portrait 2:3 vertical"
    },

    # ── 기타 웨트 (5종) ───────────────────────────────────
    "waterfall_direct": {
        "tag": "Waterfall Direct",
        "subject": "a powerful female model standing directly under waterfall cascade",
        "body": "strong athletic figure, water pounding down, immovable power",
        "outfit": "minimal wet, waterfall force revealing every curve",
        "material": "water-drenched minimal fabric, force of waterfall",
        "environment": "natural waterfall, tropical or mountain setting",
        "lighting": "natural light through water spray, rainbow in mist",
        "style": "nature power editorial, waterfall fashion photography",
        "quality": "shot on Canon R3, water force frozen, natural grade, portrait 2:3 vertical"
    },

    "wave_crash_body": {
        "tag": "Wave Crash Body",
        "subject": "a dramatic female model hit by crashing ocean wave",
        "body": "powerful athletic figure, wave impact, force of ocean",
        "outfit": "minimal swimwear, wave making everything transparent",
        "material": "saltwater soaked, ocean force fabric",
        "environment": "ocean shore, massive wave crashing, sea foam",
        "lighting": "harsh ocean sunlight, water spray backlit, sea glare",
        "style": "ocean power editorial, Sports Illustrated wave photography",
        "quality": "shot on Nikon Z9 1/4000s, wave frozen, natural color grade, portrait 2:3 vertical"
    },

    "wet_silk_minimal": {
        "tag": "Wet Silk Minimal",
        "subject": "a refined female model in wet silk that clings perfectly to form",
        "body": "elegant sculpted figure, silk revealing every contour when wet",
        "outfit": "pure silk dress completely wet, fabric second skin",
        "material": "wet pure silk, transparent and clinging, liquid drape",
        "environment": "minimalist studio or rain setting, elegant",
        "lighting": "soft dramatic light catching wet silk texture",
        "style": "luxury wet silk editorial, refined fashion photography",
        "quality": "shot on Hasselblad, wet silk texture ultra-sharp, portrait 2:3 vertical"
    },

    "bubble_bath_gloss": {
        "tag": "Bubble Bath Gloss",
        "subject": "a luxurious female model in glamorous bubble bath, glossy and sensual",
        "body": "lush sensual figure, glowing wet skin, decadent indulgence",
        "outfit": "strategic foam bubbles, wet hair, pearl accessories",
        "material": "bath foam, glossy wet skin, champagne bubbles",
        "environment": "ornate luxury bathroom, marble tub, candles, rose petals",
        "lighting": "warm candlelight, bathroom ambient glow, golden tones",
        "style": "boudoir luxury editorial, bath glamour photography",
        "quality": "shot on Canon R5, warm golden grade, bubble detail sharp, portrait 2:3 vertical"
    },

    "milk_bath_petals": {
        "tag": "Milk Bath Petals",
        "subject": "a goddess-like female model in milk bath surrounded by floating flowers",
        "body": "ethereal porcelain figure, milk-white skin merging with bath",
        "outfit": "submerged in milk bath, flowers as adornment",
        "material": "whole milk bath, flower petals floating, pearl white",
        "environment": "artistic milk bath setup, flowers, white marble",
        "lighting": "soft overhead light, milk luminosity, dreamy soft",
        "style": "art photography editorial, milk bath fashion",
        "quality": "shot on Sony A7R5, milk texture luminous, dreamy grade, portrait 2:3 vertical"
    },
}

# ══════════════════════════════════════════════════════════
# 🌫️ 대기 & 파티클 (30종)
# ══════════════════════════════════════════════════════════
PARTICLE_PRESETS = {

    # ── 스모크/연기 (6종) ─────────────────────────────────
    "smoke_machine_club": {
        "tag": "Smoke Machine Club",
        "subject": "a fierce female model emerging from thick club smoke machine fog",
        "body": "powerful sensual figure, smoke swirling around body",
        "outfit": "club fashion, smoke partially obscuring, dramatic reveal",
        "material": "club outfit with smoke interaction, fabric catching light through fog",
        "environment": "nightclub dance floor, smoke machines, neon lights",
        "lighting": "neon colored lights through smoke, laser beams, strobes",
        "style": "club editorial, nightlife fashion photography",
        "quality": "shot on Sony A9III, smoke bokeh, neon color grade, portrait 2:3 vertical"
    },

    "dry_ice_floor": {
        "tag": "Dry Ice Floor",
        "subject": "a mysterious female model standing in dry ice floor fog, ankles to knees in cloud",
        "body": "statuesque elegant figure, rising above floor fog cloud",
        "outfit": "dramatic fashion emerging from dry ice cloud, theatrical",
        "material": "luxury fabric above fog, dry ice mist interaction",
        "environment": "dark stage or studio, dry ice covering entire floor",
        "lighting": "dramatic overhead spot, fog lit from below, theatrical",
        "style": "theatrical fashion editorial, dry ice photography",
        "quality": "shot on Phase One, fog detail sharp, dramatic grade, portrait 2:3 vertical"
    },

    "cigarette_smoke_noir": {
        "tag": "Cigarette Smoke Noir",
        "subject": "a noir femme fatale with cigarette smoke curling around her face",
        "body": "languid dangerous figure, smoke as accessory",
        "outfit": "noir fashion, cigarette holder, smoke-wreathed glamour",
        "material": "dark luxurious fabric, smoke interaction",
        "environment": "dark jazz club or boudoir, moody noir setting",
        "lighting": "single moody light source, smoke backlit, deep noir shadows",
        "style": "film noir editorial, classic Hollywood glamour photography",
        "quality": "shot on Leica M11, black and white or desaturated, noir grade, portrait 2:3 vertical"
    },

    "incense_smoke_ritual": {
        "tag": "Incense Smoke Ritual",
        "subject": "a mystical female model surrounded by ritual incense smoke",
        "body": "ethereal spiritual figure, smoke coiling around body",
        "outfit": "ritual or spiritual fashion, incense smoke as veil",
        "material": "flowing fabric interacting with incense smoke",
        "environment": "temple or ritual space, incense burners, spiritual setting",
        "lighting": "warm amber temple light, smoke catching light rays",
        "style": "spiritual editorial, ritual fashion photography",
        "quality": "shot on Sony A7R5, incense smoke sharp, warm amber grade, portrait 2:3 vertical"
    },

    "smoke_color_holi": {
        "tag": "Smoke Color Holi",
        "subject": "a joyful fierce female model in explosion of colored holi smoke",
        "body": "dynamic energetic figure, colored smoke covering body",
        "outfit": "white outfit becoming canvas for colored smoke",
        "material": "white fabric saturated with color powder smoke",
        "environment": "outdoor holi festival, colored smoke bombs, celebration",
        "lighting": "bright natural sunlight through colored smoke, vivid colors",
        "style": "holi festival editorial, color explosion photography",
        "quality": "shot on Canon R3, vivid color grade, smoke frozen, portrait 2:3 vertical"
    },

    "fog_forest_mystery": {
        "tag": "Fog Forest Mystery",
        "subject": "a mysterious female model in dense forest morning fog",
        "body": "ethereal elegant figure, fog partially revealing and concealing",
        "outfit": "flowing dark fashion emerging from forest fog",
        "material": "fog-damp fabric, mysterious draping",
        "environment": "ancient forest, dense morning fog, tall trees",
        "lighting": "diffused fog light, god rays through mist, mysterious",
        "style": "dark fairy tale editorial, forest mystery photography",
        "quality": "shot on Sony A7R5, fog atmosphere deep, moody grade, portrait 2:3 vertical"
    },

    # ── 파우더/더스트 (5종) ───────────────────────────────
    "gold_dust_pour": {
        "tag": "Gold Dust Pour",
        "subject": "a goddess female model with gold dust being poured and swirling around her",
        "body": "divine sculpted figure, gold particles catching light on skin",
        "outfit": "minimal golden, gold dust as adornment swirling",
        "material": "fine gold dust particles, metallic shimmer in air",
        "environment": "dark studio, black background, gold dust explosion",
        "lighting": "dramatic side light catching gold particle glints, luxury",
        "style": "luxury gold editorial, particle art photography",
        "quality": "shot on Phase One, gold particle detail ultra-sharp, portrait 2:3 vertical"
    },

    "holi_powder_explosion": {
        "tag": "Holi Powder Explosion",
        "subject": "a radiant female model at center of massive holi powder color explosion",
        "body": "joyful powerful figure, color powder covering everything",
        "outfit": "white outfit completely transformed by color powder",
        "material": "vivid color powders coating white fabric",
        "environment": "outdoor celebration, multiple color powder explosions",
        "lighting": "bright sunlight through colored powder clouds",
        "style": "celebration editorial, maximum color impact photography",
        "quality": "shot on Nikon Z9, frozen powder explosion, maximum saturation, portrait 2:3 vertical"
    },

    "chalk_dust_sport": {
        "tag": "Chalk Dust Sport",
        "subject": "a powerful athletic female model with chalk dust explosion from hands",
        "body": "muscular athletic figure, chalk dust on hands and body",
        "outfit": "athletic minimal, chalk dust as power signature",
        "material": "gym chalk dust, athletic wear, power presence",
        "environment": "dark gym or black studio, chalk cloud explosion",
        "lighting": "dramatic hard light catching chalk dust particles",
        "style": "athletic power editorial, sport chalk photography",
        "quality": "shot on Canon R3, chalk frozen mid-explosion, high contrast, portrait 2:3 vertical"
    },

    "flour_dust_studio": {
        "tag": "Flour Dust Studio",
        "subject": "a dramatic female model in flour dust explosion, ghostly and powerful",
        "body": "strong dramatic figure, flour coating hair and skin",
        "outfit": "dark contrasting outfit with white flour coating",
        "material": "fine flour dust, white coating on dark fabric",
        "environment": "dark studio, flour explosion, ghostly white cloud",
        "lighting": "hard side light cutting through flour dust cloud",
        "style": "art editorial, flour dust explosion photography",
        "quality": "shot on Sony A1, flour particle ultra-sharp, high contrast grade, portrait 2:3 vertical"
    },

    "pigment_powder_art": {
        "tag": "Pigment Powder Art",
        "subject": "a vibrant female model with artist pigment powder exploding in rainbow",
        "body": "dynamic artistic figure, multiple colors coating body",
        "outfit": "minimal white becoming color canvas",
        "material": "artist pigment powders, vivid multi-color explosion",
        "environment": "white studio, pigment powder explosion from multiple directions",
        "lighting": "bright studio strobes, maximum color saturation",
        "style": "color art editorial, pigment explosion photography",
        "quality": "shot on Phase One, pigment particle sharp, maximum color, portrait 2:3 vertical"
    },

    # ── 페더/페탈 (5종) ───────────────────────────────────
    "feather_explosion": {
        "tag": "Feather Explosion",
        "subject": "a ethereal female model at center of white feather explosion",
        "body": "angelic graceful figure, feathers swirling around body",
        "outfit": "white or minimal, feathers as fashion",
        "material": "white goose feathers, soft floating swirl",
        "environment": "white studio or bed, feathers filling entire frame",
        "lighting": "soft diffused white light, feather translucency",
        "style": "angelic fashion editorial, feather explosion photography",
        "quality": "shot on Sony A7R5, individual feather sharp, white soft grade, portrait 2:3 vertical"
    },

    "black_feather_dark": {
        "tag": "Black Feather Dark",
        "subject": "a dark powerful female model surrounded by black feather storm",
        "body": "commanding dark figure, black feathers as power aura",
        "outfit": "dark fashion, black feathers merging with outfit",
        "material": "black raven feathers, dark glossy, dramatic",
        "environment": "dark studio, black feathers against dark background",
        "lighting": "dramatic rim light catching feather sheen, deep shadows",
        "style": "dark editorial, black feather fashion photography",
        "quality": "shot on Leica SL3, feather detail sharp, dark moody grade, portrait 2:3 vertical"
    },

    "petal_storm_indoor": {
        "tag": "Petal Storm Indoor",
        "subject": "a romantic powerful female model in indoor rose petal storm",
        "body": "sensual elegant figure, petals swirling and landing on skin",
        "outfit": "romantic fashion with petal interaction",
        "material": "red rose petals, soft landing on fabric",
        "environment": "ornate interior, thousands of red rose petals in air",
        "lighting": "warm romantic light, petals backlit, golden atmosphere",
        "style": "romantic editorial, indoor petal storm photography",
        "quality": "shot on Canon R5, petals frozen in air, warm romantic grade, portrait 2:3 vertical"
    },

    "cherry_blossom_burst": {
        "tag": "Cherry Blossom Burst",
        "subject": "a radiant female model in burst of cherry blossom petals",
        "body": "delicate powerful figure, pink petals touching skin",
        "outfit": "Japanese-inspired or white fashion, petal interaction",
        "material": "sakura petals, pink cloud surrounding body",
        "environment": "cherry blossom garden, wind-burst of petals",
        "lighting": "soft spring light, pink petal diffusion, golden hour",
        "style": "Japanese spring editorial, sakura burst photography",
        "quality": "shot on Sony A7R5, petal detail soft sharp, spring color grade, portrait 2:3 vertical"
    },

    "dried_flower_cascade": {
        "tag": "Dried Flower Cascade",
        "subject": "a bohemian elegant female model with dried flowers cascading around her",
        "body": "natural bohemian figure, dried flowers as natural adornment",
        "outfit": "earthy natural fashion, dried flower integration",
        "material": "dried wildflowers, earthy textures, natural palette",
        "environment": "rustic or studio setting, dried flower cascade from above",
        "lighting": "warm earthy natural light, dried flower translucency",
        "style": "bohemian editorial, dried flower art photography",
        "quality": "shot on Leica M11, flower detail earthy sharp, warm natural grade, portrait 2:3 vertical"
    },

    # ── 글리터/파티클 (5종) ───────────────────────────────
    "glitter_rain_studio": {
        "tag": "Glitter Rain Studio",
        "subject": "a glamorous female model in studio glitter rain shower",
        "body": "showstopping glamorous figure, glitter catching every light",
        "outfit": "glam fashion, glitter coating entire look",
        "material": "fine glitter rain, holographic sparkle",
        "environment": "dark studio, glitter falling from above like rain",
        "lighting": "multiple strobes catching glitter at maximum sparkle",
        "style": "maximum glamour editorial, glitter rain photography",
        "quality": "shot on Phase One, individual glitter sharp, maximum sparkle grade, portrait 2:3 vertical"
    },

    "gold_confetti_burst": {
        "tag": "Gold Confetti Burst",
        "subject": "a celebratory glamorous female model in gold confetti explosion",
        "body": "joyful powerful figure, gold confetti filling frame",
        "outfit": "gold fashion, confetti merging with look",
        "material": "gold metallic confetti, celebration explosion",
        "environment": "celebration venue or studio, gold confetti cannon burst",
        "lighting": "bright celebration lighting, confetti catching light",
        "style": "celebration editorial, New Year glamour photography",
        "quality": "shot on Nikon Z9, confetti frozen, gold celebration grade, portrait 2:3 vertical"
    },

    "silver_glitter_body": {
        "tag": "Silver Glitter Body",
        "subject": "a futuristic female model with silver glitter coating entire body",
        "body": "statuesque figure, silver glitter as second skin",
        "outfit": "silver glitter body coating, minimal underneath",
        "material": "fine silver glitter on skin, metallic dust",
        "environment": "dark studio, silver glitter floor, minimal",
        "lighting": "dramatic light maximizing silver sparkle, strobes",
        "style": "futuristic editorial, silver glitter body art photography",
        "quality": "shot on Phase One, glitter detail maximum, silver grade, portrait 2:3 vertical"
    },

    "neon_particle_club": {
        "tag": "Neon Particle Club",
        "subject": "a fierce female model surrounded by neon light particles in club",
        "body": "powerful dynamic figure, neon particles orbiting body",
        "outfit": "neon-reactive club fashion, particle interaction",
        "material": "UV-reactive fabric, neon particle glow",
        "environment": "underground club, neon particles from UV lighting system",
        "lighting": "UV black lights, neon particle glow, deep dark",
        "style": "underground club editorial, neon particle photography",
        "quality": "shot on Sony A9III, neon particle trails, electric color grade, portrait 2:3 vertical"
    },

    "bubble_floating_studio": {
        "tag": "Bubble Floating Studio",
        "subject": "a whimsical glamorous female model surrounded by floating soap bubbles",
        "body": "playful elegant figure, bubbles reflecting miniature worlds",
        "outfit": "iridescent fashion, bubble reflections matching outfit",
        "material": "iridescent fabric, soap bubble interaction",
        "environment": "white or pastel studio, hundreds of floating soap bubbles",
        "lighting": "soft studio light, bubble iridescence, rainbow reflections",
        "style": "whimsical fashion editorial, soap bubble photography",
        "quality": "shot on Canon R5, bubble reflection macro sharp, iridescent grade, portrait 2:3 vertical"
    },

    # ── 불/스파크 (4종) ───────────────────────────────────
    "sparkler_night_glam": {
        "tag": "Sparkler Night Glam",
        "subject": "a dazzling female model holding sparklers at night, light trails surrounding",
        "body": "glamorous radiant figure, sparkler light painting body",
        "outfit": "evening glamour, sparkler light complementing look",
        "material": "luxury evening wear, sparkler light interaction",
        "environment": "dark outdoor night setting, sparkler light only",
        "lighting": "sparkler light trails only, golden sparks, total darkness around",
        "style": "long exposure fashion editorial, sparkler light painting",
        "quality": "shot on Sony A7R5 long exposure, sparkler trails perfect, dark night grade, portrait 2:3 vertical"
    },

    "fire_poi_dance": {
        "tag": "Fire Poi Dance",
        "subject": "a powerful female model spinning fire poi, flame trails encircling body",
        "body": "athletic dancer figure, fire orbiting body in perfect arcs",
        "outfit": "fire dancer costume, flame-trail interaction",
        "material": "heat-resistant performance wear, fire light glow",
        "environment": "dark beach or stage, fire poi only light source",
        "lighting": "fire poi trails as only light, warm flame color",
        "style": "performance art editorial, fire poi long exposure photography",
        "quality": "shot on Nikon Z8 long exposure, fire trails perfect circles, portrait 2:3 vertical"
    },

    "ember_glow_dark": {
        "tag": "Ember Glow Dark",
        "subject": "a smoldering female model lit only by ember and fire glow in darkness",
        "body": "mysterious dangerous figure, ember light revealing curves",
        "outfit": "dark minimal, ember glow illuminating",
        "material": "dark fabric catching ember glow warmth",
        "environment": "complete darkness, burning embers only light source",
        "lighting": "ember and fire glow only, deep warm orange, dramatic shadows",
        "style": "dark moody editorial, ember glow photography",
        "quality": "shot on Sony A7S III high ISO, ember detail, dark warm grade, portrait 2:3 vertical"
    },

    "firework_silhouette": {
        "tag": "Firework Silhouette",
        "subject": "a dramatic female model silhouetted against massive firework explosion",
        "body": "powerful silhouette figure, firework sky as backdrop",
        "outfit": "dark silhouette only, firework as costume of light",
        "material": "silhouette, firework light",
        "environment": "outdoor night, massive firework display directly behind",
        "lighting": "firework explosion as sole backlight, total silhouette front",
        "style": "silhouette editorial, firework fashion photography",
        "quality": "shot on Canon R3, firework explosion sharp, silhouette perfect, portrait 2:3 vertical"
    },

    # ── 자연 파티클 (5종) ─────────────────────────────────
    "autumn_leaves_burst": {
        "tag": "Autumn Leaves Burst",
        "subject": "a vibrant female model in explosion of autumn leaves",
        "body": "dynamic energetic figure, leaves swirling in autumn wind",
        "outfit": "autumn fashion, leaf color palette matching",
        "material": "autumn fabric tones, leaf interaction",
        "environment": "forest or park, autumn wind burst of fallen leaves",
        "lighting": "golden autumn light, leaves backlit and glowing",
        "style": "autumn editorial, seasonal fashion photography",
        "quality": "shot on Sony A7R5, leaf detail crisp, warm autumn grade, portrait 2:3 vertical"
    },

    "snow_indoor_studio": {
        "tag": "Snow Indoor Studio",
        "subject": "a winter goddess female model in indoor artificial snow fall",
        "body": "ethereal winter figure, snowflakes landing on skin and hair",
        "outfit": "winter fashion with snowflake interaction",
        "material": "winter fabric, snowflakes on dark clothing contrasting",
        "environment": "dark studio with snow machine, controlled snowfall",
        "lighting": "dramatic light catching individual snowflakes",
        "style": "winter editorial, indoor snow fashion photography",
        "quality": "shot on Phase One, individual snowflake sharp, cool winter grade, portrait 2:3 vertical"
    },

    "dandelion_blow": {
        "tag": "Dandelion Blow",
        "subject": "a whimsical beautiful female model blowing dandelion seeds into wind",
        "body": "free-spirited ethereal figure, dandelion seeds floating away",
        "outfit": "soft natural fashion, dandelion seed interaction",
        "material": "natural flowing fabric, dandelion lightness",
        "environment": "summer field, dandelions everywhere, soft breeze",
        "lighting": "golden hour backlight, dandelion seeds backlit like stars",
        "style": "romantic nature editorial, dandelion photography",
        "quality": "shot on Sony A7R5, dandelion seed detail, golden hour grade, portrait 2:3 vertical"
    },

    "firefly_night_field": {
        "tag": "Firefly Night Field",
        "subject": "a magical female model in summer night field surrounded by fireflies",
        "body": "dreamy enchanting figure, firefly light dotting around body",
        "outfit": "flowing summer dress, firefly glow interaction",
        "material": "light summer fabric glowing in firefly light",
        "environment": "summer night field, hundreds of fireflies, dark sky",
        "lighting": "firefly bioluminescence only, magical dotted light",
        "style": "magical nature editorial, firefly night photography",
        "quality": "shot on Sony A7S III, firefly glow captured, magical night grade, portrait 2:3 vertical"
    },

    "seed_pod_floating": {
        "tag": "Seed Pod Floating",
        "subject": "a serene beautiful female model surrounded by floating seed pods and cotton",
        "body": "peaceful ethereal figure, seeds drifting past body",
        "outfit": "minimal natural fashion, seed pod floating interaction",
        "material": "natural fabric, seed pod lightness around",
        "environment": "natural outdoor, seed pods floating on breeze",
        "lighting": "soft natural backlight, seed pods translucent in light",
        "style": "nature art editorial, floating seed photography",
        "quality": "shot on Canon R5, seed detail backlit sharp, soft natural grade, portrait 2:3 vertical"
    },
}


def save_presets(presets: dict, category_folder: str) -> None:
    folder = PRESET_DIR / category_folder
    folder.mkdir(parents=True, exist_ok=True)

    saved = 0
    skipped = 0
    for name, data in presets.items():
        path = folder / f"{name}.json"
        if path.exists():
            print(f"  [SKIP] {name}.json (이미 존재)")
            skipped += 1
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  [OK]   {name}.json")
            saved += 1

    print(f"\n  저장: {saved}종 / 스킵: {skipped}종")


if __name__ == "__main__":
    print("=" * 60)
    print("💧 웨트 & 글로스 프리셋 생성")
    print("=" * 60)
    save_presets(WET_GLOSS_PRESETS, "웨트글로스")

    print()
    print("=" * 60)
    print("🌫️ 대기 & 파티클 프리셋 생성")
    print("=" * 60)
    save_presets(PARTICLE_PRESETS, "대기파티클")

    print()
    print("총 프리셋:", len(WET_GLOSS_PRESETS) + len(PARTICLE_PRESETS), "종")
    print()
    print("다음 단계:")
    print("  1. dashboard.py PRESET_CATEGORIES에 두 카테고리 추가")
    print("  2. core/engine.py 카테고리 폴더 인식 확인")
    print("  3. Gemini 테스트 후 tier 검증")
