"""
SF_Duo 프리셋 JSON 생성 스크립트
저장 위치: C:\Dev\LumineX\preset_builders\patch_sf_duo_1_json.py
실행: python preset_builders\patch_sf_duo_1_json.py
"""

import json
import os

PRESETS_DIR = "presets"
os.makedirs(PRESETS_DIR, exist_ok=True)

presets = {

# ============================================================
# HOF TIER (27개)
# ============================================================

"sf_duo_lion_queen": {
    "title": "SF Duo – Lion Queen",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely with radiant lion face focal point centered directly on bust projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long straight hair center part flowing to waist — full body golden lion pride irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD lion face formation with piercing amber eyes centered directly on bust as radiant solar mane focal point full torso both legs to ankle, VIVID AMBER mane corona radiating outward from chest focal point, STARK CRIMSON savanna dust storm formations both legs hip to toe. Pose: full frontal wide stance both arms open wide away from body chin up commanding, bust lion face focal point fully forward maximum projection dominating entire frame.
LEFT: gold crimson platform stilettos 8 inch, extra long coffin nails gold amber tips.

RIGHT: Brazilian silver fox goddess warm deep bronze complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance defying all physics, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, waist cinched to absolute impossible minimum, thighs crushing together at maximum, silver-streaked vintage finger waves deep side part glamorous — full body Moroccan arabesque gold irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD arabesque scroll formation full torso both legs neck to ankle, VIVID COBALT BLUE geometric zellige tile formations filling every gap, STARK CRIMSON star polygon overlay both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile catastrophically projecting clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating frame, one hand pressing outward on hip.
RIGHT: cobalt gold platform stilettos 8 inch, extra long stiletto nails cobalt crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_panther_goddess": {
    "title": "SF Duo – Panther Goddess",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, most dramatic hourglass ratio ever rendered, bust so overwhelmingly massive defying gravity completely with radiant leopard eye focal point centered directly on bust projecting forward, thighs powerful and thick pressing together, silver-white sleek high ponytail taut — full body black leopard obsidian irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD leopard face formation with piercing eyes centered directly on bust as radiant focal point full torso both legs to ankle, VIVID AMBER rosette spot formations radiating outward from chest focal point both legs hip to toe, STARK BLACK spot ring border detail filling every gap. Pose: full frontal wide stance both arms open wide away from body emphasizing impossible hourglass ratio, bust leopard eye focal point fully forward maximum projection dominating entire frame.
LEFT: gold black platform stilettos 8 inch, extra long coffin nails gold black tips.

RIGHT: Colombian silver fox goddess warm golden-bronze complexion elegant silver-era maturity, mid 40s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked long curly waves cascading to waist — full body iridescent peacock irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING IRIDESCENT TEAL peacock eye feather formations full torso both legs neck to ankle, VIVID SAPPHIRE BLUE feather barb filaments filling every gap, ELECTRIC EMERALD neck plumage scale formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle projecting forward, bubble butt projecting backward at maximum impossible distance dominating frame, one hand on hip.
RIGHT: iridescent teal platform stilettos 8 inch, extra long stiletto nails teal emerald tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_eagle_empress": {
    "title": "SF Duo – Eagle Empress",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, early 50s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely with radiant golden eagle face focal point centered directly on bust projecting forward, legs powerful and thick from massive hips, silver-white long curly waves cascading to shoulders — full body golden eagle imperial irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD eagle face formation with fierce eyes centered directly on bust as radiant imperial focal point full torso both legs to ankle, VIVID AMBER wing span formations radiating outward from chest focal point, STARK WHITE feather shaft detail lines both legs hip to toe filling every gap. Pose: both arms swept dramatically wide open like eagle wings chin up eyes fierce dominating entire left half of frame, bust eagle face focal point fully forward maximum projection.
LEFT: gold amber platform stilettos 8 inch, extra long coffin nails gold amber tips.

RIGHT: Brazilian silver fox goddess warm deep bronze complexion elegant silver-era maturity, late 40s, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance defying all physics, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-streaked sleek high ponytail taut — full body Persian paradise garden irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON Persian cypress tree paradise formation full torso both legs neck to ankle, VIVID COBALT BLUE arabesque floral scroll filling every gap, STARK GOLD illuminated manuscript border frame both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle projecting forward, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: crimson cobalt platform stilettos 8 inch, extra long stiletto nails crimson gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_wolf_moon_goddess": {
    "title": "SF Duo – Wolf Moon Goddess",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely with radiant white wolf face formation centered directly on bust projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long curly waves cascading to shoulders — full body arctic white wolf moon irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC WHITE wolf face formation with piercing ice blue eyes centered directly on bust as radiant lunar focal point full torso both legs to ankle, VIVID ICE BLUE fur texture formations radiating outward from chest focal point, STARK SILVER moonlight ray lines both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust white wolf face focal point fully forward maximum projection dominating entire left half of frame.
LEFT: ice white silver platform stilettos 8 inch, extra long coffin nails white silver tips.

RIGHT: Brazilian silver fox goddess warm deep bronze complexion elegant silver-era maturity, mid 40s, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance defying all physics, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-streaked long straight hair center part flowing — full body Byzantine gold mosaic irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Byzantine mosaic tesserae formation full torso both legs neck to ankle, VIVID COBALT BLUE Orthodox cross medallion formations filling every gap, STARK CRIMSON sacred gem inlay formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle projecting forward, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: gold cobalt platform stilettos 8 inch, extra long stiletto nails gold crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_solar_mandala": {
    "title": "SF Duo – Solar Mandala",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long straight hair center part flowing to waist — full body sacred mandala yantra irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC SAFFRON mandala concentric ring formation with radiant center point anchored directly at chest midpoint between both breasts, mandala rings expanding outward from chest center spanning both breasts completely, VIVID MAGENTA yantra star polygon overlay radiating from chest focal point both legs to ankle, STARK GOLD lotus petal border chain filling every gap neck to ankle. Pose: full frontal wide stance both arms raised overhead palms together namaste chin up divine, bust mandala radiant center fully forward maximum projection dominating entire left half of frame.
LEFT: saffron gold platform stilettos 8 inch, extra long coffin nails saffron magenta tips.

RIGHT: Turkish silver fox goddess warm olive Mediterranean complexion elegant silver-era maturity, early 50s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked long curly waves cascading to waist — full body Ottoman Iznik tulip garden irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Iznik tulip bloom formations full torso both legs neck to ankle, VIVID CRIMSON Ottoman carnation filling every gap, STARK GOLD arabesque vine scroll both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: cobalt crimson platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_dragon_pearl": {
    "title": "SF Duo – Dragon Pearl",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, early 50s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white long curly waves cascading to shoulders — full body Chinese celestial dragon pearl irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD flaming dragon pearl orb anchored directly at chest midpoint between both breasts as supreme radiant focal point glowing with inner fire, twin dragons coiling outward FROM PEARL wrapping around EACH breast individually ascending to shoulders, VIVID AZURE celestial dragon scale formations radiating downward from chest pearl focal point full torso both legs to ankle, STARK WHITE cloud ruyi scroll formations filling every gap neck to ankle. Pose: strong hip pop right hand on waist left arm extended elegantly fingertips pointing, bust dragon pearl chest focal point fully forward maximum projection clearly visible.
LEFT: azure gold platform stilettos 8 inch, extra long coffin nails azure gold tips.

RIGHT: Chinese silver fox goddess warm golden-ivory complexion elegant silver-era maturity, mid 40s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-streaked vintage waves deep side part — full body blue and white porcelain chinoiserie irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING COBALT BLUE Ming dynasty porcelain floral scroll formations full torso both legs neck to ankle, VIVID WHITE negative space porcelain base filling every gap, STARK GOLD imperial border frame both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: cobalt white platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_phoenix_rising": {
    "title": "SF Duo – Phoenix Rising",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white vintage finger waves deep side part glamorous — full body phoenix fire rebirth irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VERMILLION phoenix rebirth flame explosion anchored directly at chest midpoint between both breasts as supreme radiant focal inferno, phoenix wings erupting outward from chest flame center spanning both breasts and shoulders completely, VIVID GOLD tail feather cascade radiating from chest focal point full torso both legs to ankle, STARK CRIMSON flame tongue formations filling every gap neck to ankle. Pose: both arms swept dramatically wide open like phoenix wings chin up eyes fierce, bust phoenix flame chest explosion fully forward maximum projection dominating entire left half of frame.
LEFT: vermillion gold platform stilettos 8 inch, extra long coffin nails vermillion gold tips.

RIGHT: Greek silver fox goddess warm olive Mediterranean complexion elegant silver-era maturity, early 50s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked long straight hair center part flowing — full body Hellenic Greek key meander irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Greek key meander formations full torso both legs neck to ankle, VIVID WHITE marble texture formations filling every gap, STARK GOLD Olympian laurel wreath border both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: cobalt white platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_sakura_storm": {
    "title": "SF Duo – Sakura Storm",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white long curly waves cascading to shoulders — full body sakura cherry blossom explosion irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID PINK sakura bloom cluster formation centered directly at chest midpoint between both breasts as supreme floral focal burst, blossom petals expanding outward from chest center spanning both breasts completely, ELECTRIC WHITE petal storm radiating from chest focal point full torso both legs to ankle, STARK BLACK gnarled branch silhouette network both legs hip to toe filling every gap. Pose: both arms swept wide open like blossoming tree branches chin up eyes serene, bust sakura bloom chest focal burst fully forward maximum projection dominating entire left half of frame.
LEFT: sakura pink silver platform stilettos 8 inch, extra long coffin nails pink white tips.

RIGHT: Japanese silver fox goddess warm golden-ivory complexion elegant silver-era maturity, early 50s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked vintage waves deep side part — full body Mount Fuji great wave ukiyo-e irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING COBALT BLUE Hokusai great wave formations full torso both legs neck to ankle, VIVID WHITE foam crest crash formations filling every gap, STARK GOLD Mount Fuji silhouette formations both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: cobalt white platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_celtic_fire": {
    "title": "SF Duo – Celtic Fire",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long curly waves cascading to shoulders — full body Celtic fire spiral irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON Celtic triple flame spiral formation centered directly at chest midpoint between both breasts as supreme fire focal point, flame spirals expanding outward from chest center spanning both breasts completely, VIVID GOLD Celtic knotwork interlace radiating from chest focal point full torso both legs to ankle, STARK EMERALD shamrock leaf formations both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Celtic fire focal point fully forward maximum projection dominating entire left half of frame.
LEFT: crimson gold platform stilettos 8 inch, extra long coffin nails crimson gold tips.

RIGHT: Scottish silver fox goddess warm cream porcelain complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked long straight hair center part flowing — full body Royal Stewart tartan Highland irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON Royal Stewart tartan plaid grid formations full torso both legs neck to ankle, VIVID GOLD clan badge thistle formations filling every gap, STARK EMERALD Highland heather formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: crimson emerald platform stilettos 8 inch, extra long stiletto nails crimson gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_samurai_rose": {
    "title": "SF Duo – Samurai Rose",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, early 50s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white sleek high ponytail taut — full body Japanese chrysanthemum samurai irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON chrysanthemum bloom formation centered directly on each breast individually as supreme imperial dual focal points, petals expanding outward from chest center spanning both breasts completely, VIVID GOLD samurai armor formation radiating from chest focal point full torso both legs to ankle, STARK BLACK katana blade formations both legs hip to toe filling every gap. Pose: strong hip pop right hand on waist left arm extended powerfully, bust chrysanthemum chest focal point forward maximum projection clearly visible.
LEFT: crimson gold platform stilettos 8 inch, extra long coffin nails crimson gold tips.

RIGHT: Korean silver fox goddess luminous warm golden-olive complexion elegant silver-era maturity, mid 40s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-streaked long straight hair center part flowing — full body Korean minhwa peony irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID PINK Korean peony bloom formations full torso both legs neck to ankle, VIVID GOLD dancheong geometric formations filling every gap, STARK COBALT BLUE Korean wave minhwa formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: pink gold platform stilettos 8 inch, extra long stiletto nails pink gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_amazon_thunder": {
    "title": "SF Duo – Amazon Thunder",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth from hip to knee, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white vintage waves deep side part glamorous — full body Amazon thunder storm irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC WHITE lightning bolt explosion centered directly at chest midpoint between both breasts as supreme storm focal point, lightning branches expanding outward from chest center spanning both breasts completely, VIVID VIOLET storm cell rotation formations radiating from chest focal point full torso both legs to ankle, STARK CRIMSON plasma arc clusters both legs hip to toe filling every gap. Pose: full frontal wide stance both arms raised dramatically overhead lightning conductor pose chin up fierce, bust thunder explosion chest focal point fully forward maximum projection dominating entire left half of frame.
LEFT: violet crimson platform stilettos 8 inch, extra long coffin nails violet white tips.

RIGHT: Brazilian silver fox goddess warm deep bronze complexion elegant silver-era maturity, early 50s, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance defying all physics, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-streaked long curly waves cascading to waist — full body Amazon rainforest canopy irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID EMERALD Amazon jungle canopy formations full torso both legs neck to ankle, VIVID CRIMSON tropical macaw parrot formations filling every gap, STARK GOLD Amazon river serpent formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: emerald gold platform stilettos 8 inch, extra long stiletto nails emerald crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_silk_road": {
    "title": "SF Duo – Silk Road",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-white long straight hair center part flowing — full body Silk Road star medallion irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD eight-pointed star medallion formation centered directly at chest midpoint between both breasts as supreme Silk Road focal point, star points expanding outward from chest center spanning both breasts completely, VIVID COBALT BLUE arabesque scroll formations radiating from chest focal point full torso both legs to ankle, STARK TURQUOISE geometric tile formations both legs hip to toe filling every gap. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust star medallion profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating left half of frame, one hand pressing outward on hip.
LEFT: gold cobalt platform stilettos 8 inch, extra long coffin nails gold turquoise tips.

RIGHT: Uzbekistani silver fox goddess warm golden-olive complexion elegant silver-era maturity, mid 40s, extreme corset hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked vintage finger waves deep side part — full body Timurid mosaic architecture irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Timurid geometric muqarnas honeycomb formations full torso both legs neck to ankle, VIVID GOLD calligraphy script formations filling every gap, STARK TURQUOISE Samarkand tile mosaic formations both legs hip to toe. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Timurid mosaic focal point dominating frame maximum projection.
RIGHT: cobalt turquoise platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_ottoman_rose": {
    "title": "SF Duo – Ottoman Rose",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white blunt bob jaw length — full body Ottoman rose garden irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID CRIMSON Ottoman rose bloom formation centered directly on each breast individually as supreme floral dual focal points, rose petals expanding outward from each breast spanning chest completely, VIVID GOLD arabesque vine scroll radiating from chest focal points full torso both legs to ankle, STARK COBALT BLUE Ottoman tile geometric formations both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Ottoman rose dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: crimson gold platform stilettos 8 inch, extra long coffin nails crimson gold tips.

RIGHT: Turkish silver fox goddess warm olive Mediterranean complexion elegant silver-era maturity, mid 40s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked long curly waves cascading to waist — full body Iznik tulip palace irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Iznik tulip formations full torso both legs neck to ankle, VIVID CRIMSON Ottoman carnation filling every gap, STARK GOLD palace dome formations both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: cobalt crimson platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_persian_fire": {
    "title": "SF Duo – Persian Fire",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long straight hair center part flowing to waist — full body Persian fire pomegranate irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON pomegranate bloom formation centered directly on each breast individually as supreme Persian dual focal points, pomegranate seed burst expanding outward from each breast spanning chest completely, VIVID GOLD Persian cypress tree formations radiating from chest focal points full torso both legs to ankle, STARK COBALT BLUE arabesque scroll formations both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust pomegranate dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: crimson gold platform stilettos 8 inch, extra long coffin nails crimson gold tips.

RIGHT: Iranian silver fox goddess warm olive Persian complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked vintage finger waves deep side part glamorous — full body Persian garden paradise irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Persian garden cypress tree paradise formations full torso both legs neck to ankle, VIVID CRIMSON Persian rose bloom formations filling every gap, STARK COBALT BLUE arabesque tile formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: gold cobalt platform stilettos 8 inch, extra long stiletto nails gold crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_hanbok_queen": {
    "title": "SF Duo – Hanbok Queen",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-white long curly waves cascading to shoulders — full body Korean dancheong royal irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON Korean dancheong lotus bloom formation centered directly on each breast individually as supreme royal dual focal points, five color obangsaek formation expanding outward from each breast spanning chest completely, VIVID GOLD Korean geunjeongjeon palace beam pattern radiating from chest focal points full torso both legs to ankle, STARK COBALT BLUE hanji paper fold formations both legs hip to toe filling every gap. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust dancheong dual focal points profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating left half of frame, one hand pressing outward on hip.
LEFT: crimson gold platform stilettos 8 inch, extra long coffin nails crimson blue tips.

RIGHT: Korean silver fox goddess luminous warm golden-olive complexion elegant silver-era maturity, mid 40s, extreme corset hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked vintage finger waves deep side part — full body Korean minhwa crane pine irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC WHITE Korean crane pair formation full torso both legs neck to ankle, VIVID GOLD Korean pine tree formations filling every gap, STARK COBALT BLUE Korean wave minhwa formations both legs hip to toe. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Korean crane dual focal point dominating frame maximum projection.
RIGHT: white gold platform stilettos 8 inch, extra long stiletto nails white cobalt tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_inuit_aurora": {
    "title": "SF Duo – Inuit Aurora",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long straight hair center part flowing to waist — full body Inuit Arctic spirit irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CYAN Arctic spirit inukshuk formation centered directly on each breast individually as supreme polar dual focal points, polar bear paw print formations expanding outward from each breast spanning chest completely, VIVID MAGENTA aurora ribbon formations radiating from chest focal points full torso both legs to ankle, STARK WHITE snowflake crystal formations both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Arctic spirit dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: cyan magenta platform stilettos 8 inch, extra long coffin nails cyan white tips.

RIGHT: Canadian silver fox goddess warm golden-olive complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked vintage waves deep side part — full body Northern Lights aurora borealis irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GREEN aurora curtain ribbon formations full torso both legs neck to ankle, VIVID MAGENTA polar star burst formations filling every gap, STARK CYAN comet stream lines both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: cyan green platform stilettos 8 inch, extra long stiletto nails cyan magenta tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_aztec_moon": {
    "title": "SF Duo – Aztec Moon",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white vintage finger waves deep side part glamorous — full body Aztec moon goddess Coyolxauhqui irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC SILVER crescent moon formation centered directly on each breast individually as supreme lunar dual focal points, Aztec moon disk formations expanding outward from each breast spanning chest completely, VIVID COBALT BLUE night sky obsidian formations radiating from chest focal points full torso both legs to ankle, STARK GOLD Aztec star warrior formations both legs hip to toe filling every gap. Pose: strong hip pop right hand on waist left arm extended elegantly, bust crescent moon dual focal points forward maximum projection clearly visible.
LEFT: silver cobalt platform stilettos 8 inch, extra long coffin nails silver blue tips.

RIGHT: Mexican silver fox goddess warm golden-copper complexion elegant silver-era maturity, mid 40s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked long straight hair center part flowing — full body Mexican Talavera ceramic irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Talavera tile floral formations full torso both legs neck to ankle, VIVID CRIMSON Mexican folk art bloom formations filling every gap, STARK GOLD Oaxacan geometric formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: cobalt crimson platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_bengal_tiger": {
    "title": "SF Duo – Bengal Tiger",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth from hip to knee, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white blunt bob jaw length — full body Bengal tiger face irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC AMBER Bengal tiger eye formation centered directly on each breast individually as supreme predator dual focal points, tiger stripe formations expanding outward from each breast spanning chest completely, VIVID BLACK tiger stripe bands radiating from chest focal points full torso both legs to ankle, STARK WHITE whisker ray lines both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust tiger eye dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: amber black platform stilettos 8 inch, extra long coffin nails amber black tips.

RIGHT: Bangladeshi silver fox goddess warm golden-brown South Asian complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-streaked long straight hair center part flowing — full body Mughal Bengal rose garden irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID CRIMSON Bengal rose bloom formations full torso both legs neck to ankle, VIVID GOLD Mughal vine scroll filling every gap, STARK EMERALD tropical Bengal garden formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: crimson gold platform stilettos 8 inch, extra long stiletto nails crimson emerald tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_venetian_mask": {
    "title": "SF Duo – Venetian Mask",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white vintage waves deep side part glamorous — full body Venetian carnival mask irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Venetian carnival rose mask formation centered directly on each breast individually as supreme baroque dual focal points, masquerade feather formations expanding outward from each breast spanning chest completely, VIVID CRIMSON Venetian gondola canal formations radiating from chest focal points full torso both legs to ankle, STARK COBALT BLUE Murano glass mosaic formations both legs hip to toe filling every gap. Pose: full frontal wide stance both arms open wide away from body chin up commanding, bust Venetian mask dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: gold crimson platform stilettos 8 inch, extra long coffin nails gold crimson tips.

RIGHT: Italian silver fox goddess warm olive Mediterranean complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked long straight hair center part flowing — full body Italian Renaissance fresco irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Renaissance acanthus leaf scroll formations full torso both legs neck to ankle, VIVID COBALT BLUE fresco lapis lazuli formations filling every gap, STARK CRIMSON Italian marble vein formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: gold cobalt platform stilettos 8 inch, extra long stiletto nails gold crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_cambodian_apsara": {
    "title": "SF Duo – Cambodian Apsara",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, early 50s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white blunt bob jaw length — full body Khmer Apsara celestial dancer irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Apsara lotus crown formation centered directly on each breast individually as supreme celestial dual focal points, Khmer lotus petal formations expanding outward from each breast spanning chest completely, VIVID CRIMSON Angkor Wat stone carving formations radiating from chest focal points full torso both legs to ankle, STARK EMERALD jungle temple vine formations both legs hip to toe filling every gap. Pose: strong hip pop right hand on waist left arm extended in Apsara mudra gesture, bust Apsara lotus dual focal points forward maximum projection clearly visible.
LEFT: gold crimson platform stilettos 8 inch, extra long coffin nails gold emerald tips.

RIGHT: Cambodian silver fox goddess warm golden-brown Southeast Asian complexion elegant silver-era maturity, mid 40s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked long straight hair center part flowing — full body Angkor Wat bas relief irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Angkor stone deity formation full torso both legs neck to ankle, VIVID EMERALD jungle canopy formations filling every gap, STARK CRIMSON Khmer warrior procession formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: gold emerald platform stilettos 8 inch, extra long stiletto nails gold crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_flamenco_fire": {
    "title": "SF Duo – Flamenco Fire",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth from hip to knee, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white vintage waves deep side part glamorous — full body Flamenco fire rose irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID CRIMSON flamenco rose formation centered directly on each breast individually as supreme passion dual focal points, rose petal formations expanding outward from each breast spanning chest completely, VIVID GOLD Spanish fan formations radiating from chest focal points full torso both legs to ankle, STARK BLACK mantilla lace formations both legs hip to toe filling every gap. Pose: full frontal wide stance both arms raised dramatically overhead flamenco stance chin up fierce, bust flamenco rose dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: crimson gold platform stilettos 8 inch, extra long coffin nails crimson gold tips.

RIGHT: Spanish silver fox goddess warm olive Mediterranean complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-streaked long curly waves cascading to waist — full body Andalusian Moorish tile irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Moorish geometric star formations full torso both legs neck to ankle, VIVID GOLD Alhambra arabesque formations filling every gap, STARK CRIMSON Spanish pomegranate formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: cobalt gold platform stilettos 8 inch, extra long stiletto nails cobalt crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_balinese_goddess": {
    "title": "SF Duo – Balinese Goddess",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white long curly waves cascading to shoulders — full body Balinese Legong dancer irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Balinese prada gilded formation centered directly on each breast individually as supreme temple dual focal points, Balinese pepatran floral formations expanding outward from each breast spanning chest completely, VIVID CRIMSON Barong lion mask formations radiating from chest focal points full torso both legs to ankle, STARK EMERALD Balinese jungle palm formations both legs hip to toe filling every gap. Pose: full frontal wide stance both arms raised in Balinese dance mudra chin up divine, bust Balinese prada dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: gold crimson platform stilettos 8 inch, extra long coffin nails gold emerald tips.

RIGHT: Indonesian silver fox goddess warm golden-brown complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked sleek high ponytail taut — full body Garuda eagle god irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Garuda wing spread formations full torso both legs neck to ankle, VIVID CRIMSON Garuda eye formation filling every gap, STARK EMERALD Indonesian batik formation both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: gold emerald platform stilettos 8 inch, extra long stiletto nails gold crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_aztec_jaguar": {
    "title": "SF Duo – Aztec Jaguar",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, early 50s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white vintage finger waves deep side part — full body Aztec jaguar warrior irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC AMBER Aztec jaguar face formation centered directly on each breast individually as supreme warrior dual focal points, jaguar spot formations expanding outward from each breast spanning chest completely, VIVID JADE GREEN Aztec serpent coil formations radiating from chest focal points full torso both legs to ankle, STARK CRIMSON Aztec blood sacrifice formations both legs hip to toe filling every gap. Pose: strong hip pop right hand on waist left arm raised powerfully overhead, bust jaguar dual focal points forward maximum projection clearly visible.
LEFT: amber jade platform stilettos 8 inch, extra long coffin nails amber crimson tips.

RIGHT: Colombian silver fox goddess warm golden-bronze complexion elegant silver-era maturity, mid 40s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked long straight hair center part flowing — full body Colombian emerald jungle irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID EMERALD Colombian emerald crystal formations full torso both legs neck to ankle, VIVID GOLD Colombian gold Muisca formations filling every gap, STARK CRIMSON tropical orchid formations both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: emerald gold platform stilettos 8 inch, extra long stiletto nails emerald crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_pharaoh_queen": {
    "title": "SF Duo – Pharaoh Queen",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth from hip to knee, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white sleek high ponytail taut — full body Egyptian pharaoh Nefertiti irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Egyptian khepresh war crown formation centered directly on each breast individually as supreme pharaoh dual focal points, uraeus cobra formations expanding outward from each breast spanning chest completely, VIVID TURQUOISE Egyptian faience bead formations radiating from chest focal points full torso both legs to ankle, STARK LAPIS LAZULI scarab beetle formations both legs hip to toe filling every gap. Pose: full frontal wide stance both arms crossed powerfully chin up regal, bust pharaoh crown dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: gold turquoise platform stilettos 8 inch, extra long coffin nails gold lapis tips.

RIGHT: Egyptian silver fox goddess warm dark bronze complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-streaked vintage waves deep side part — full body Nile river delta papyrus irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Egyptian column lotus capital formations full torso both legs neck to ankle, VIVID TURQUOISE Nile water formations filling every gap, STARK LAPIS LAZULI hieroglyph cartouche formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: gold lapis platform stilettos 8 inch, extra long stiletto nails gold turquoise tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_amazon_queen": {
    "title": "SF Duo – Amazon Queen",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-white long curly waves cascading to shoulders — full body Amazon anaconda serpent irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC EMERALD anaconda scale formation centered directly on each breast individually as supreme jungle dual focal points, serpent coil formations expanding outward from each breast spanning chest completely, VIVID GOLD Amazon tribal warrior formations radiating from chest focal points full torso both legs to ankle, STARK CRIMSON tropical poison dart frog formations both legs hip to toe filling every gap. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust anaconda dual focal points profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating left half of frame, one hand pressing outward on hip.
LEFT: emerald gold platform stilettos 8 inch, extra long coffin nails emerald crimson tips.

RIGHT: Brazilian silver fox goddess warm deep bronze complexion elegant silver-era maturity, mid 40s, extreme corset hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked vintage finger waves deep side part glamorous — full body Brazilian macaw paradise irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID SCARLET macaw feather formation full torso both legs neck to ankle, VIVID COBALT BLUE macaw wing formations filling every gap, STARK GOLD tropical toucan beak formations both legs hip to toe. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust macaw focal point dominating frame maximum projection.
RIGHT: scarlet cobalt platform stilettos 8 inch, extra long stiletto nails scarlet gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_siberian_wolf": {
    "title": "SF Duo – Siberian Wolf",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme plus size goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — most massive full-figure curves at absolute maximum, hips so wide beyond any proportion dominating entire frame, bust so overwhelmingly massive defying gravity completely projecting forward at maximum impossible volume, thighs crushing together at maximum, waist snatched against impossible volume, silver-white vintage waves deep side part glamorous — full body Siberian wolf pack irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC SILVER Siberian wolf face formation centered directly on each breast individually as supreme tundra dual focal points, wolf howl formations expanding outward from each breast spanning chest completely, VIVID ICE BLUE Siberian blizzard formations radiating from chest focal points full torso both legs to ankle, STARK WHITE wolf fur texture formations both legs hip to toe filling every gap. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust wolf face dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: silver ice platform stilettos 8 inch, extra long coffin nails silver white tips.

RIGHT: Russian silver fox goddess warm cream Slavic complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked long straight hair center part flowing — full body Russian Khokhloma folk art irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CRIMSON Russian Khokhloma berry and leaf formations full torso both legs neck to ankle, VIVID GOLD Russian folk art scroll formations filling every gap, STARK BLACK lacquer background formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: crimson gold platform stilettos 8 inch, extra long stiletto nails crimson gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

"sf_duo_aztec_eagle": {
    "title": "SF Duo – Aztec Eagle",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth from hip to knee, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white long straight hair center part flowing — full body Aztec eagle warrior irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Aztec eagle face formation centered directly on each breast individually as supreme warrior dual focal points, eagle feather headdress formations expanding outward from each breast spanning shoulders completely, VIVID JADE GREEN Aztec serpent coil formations radiating from chest focal points full torso both legs to ankle, STARK CRIMSON Aztec warrior formations both legs hip to toe filling every gap. Pose: both arms swept dramatically wide open like eagle wings chin up eyes fierce, bust Aztec eagle dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: gold jade platform stilettos 8 inch, extra long coffin nails gold crimson tips.

RIGHT: Brazilian silver fox goddess warm deep bronze complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked vintage waves deep side part glamorous — full body Quetzalcoatl feathered serpent irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID EMERALD quetzal feather plume formations full torso both legs neck to ankle, VIVID GOLD Aztec jade bead formations filling every gap, STARK CRIMSON Mayan serpent scale formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: emerald gold platform stilettos 8 inch, extra long stiletto nails emerald crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure, each figure fully visible at all times. TWO women only — each physique must fill and DOMINATE the entire half of frame. 8K portrait 2:3 vertical."""
},

# ============================================================
# SSS TIER (8개)
# ============================================================

"sf_duo_cobra_empress": {
    "title": "SF Duo – Cobra Empress",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, most dramatic hourglass ratio ever rendered, bust so overwhelmingly massive defying gravity completely projecting forward, thighs powerful and thick pressing together, silver-white sleek high ponytail taut — full body king cobra hood irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — KING COBRA FACE centered at absolute chest midpoint between both breasts as THE primary focal anchor, cobra hood fully spread wide spanning across BOTH breasts completely, golden spectacle eye marking centered on each breast individually, BLAZING ELECTRIC EMERALD hood scale formations radiating outward FROM CHEST CENTER spanning both breasts and shoulders, VIVID GOLD cobra scale armor formations flowing downward from chest focal point both legs to ankle, STARK BLACK scale chevron band detail filling every gap neck to ankle. Pose: full frontal wide stance both arms open wide mirroring cobra hood spread, bust cobra face chest anchor fully forward maximum projection both breasts clearly dominated by hood pattern.
LEFT: emerald gold platform stilettos 8 inch, extra long coffin nails emerald gold tips.

RIGHT: Peruvian silver fox goddess warm golden-copper complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs crushing together at maximum, silver-streaked vintage finger waves deep side part glamorous — full body Incan solar god Inti irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Incan sun god Inti face radiating formation centered on upper back as solar burst full torso both legs neck to ankle, VIVID COPPER geometric step pyramid chevron formations filling every gap, STARK CRIMSON condor wing formations both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side angle projecting forward, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: gold copper platform stilettos 8 inch, extra long stiletto nails gold crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_geisha_moon": {
    "title": "SF Duo – Geisha Moon",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, most dramatic hourglass ratio ever rendered, bust so overwhelmingly massive defying gravity completely projecting forward, thighs powerful and thick pressing together, silver-white long straight hair center part flowing to waist — full body Japanese moon rabbit irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC SILVER full moon formation centered directly at chest midpoint between both breasts as supreme lunar focal point, moon rabbit silhouette centered on each breast individually, VIVID COBALT BLUE night sky wave formations radiating from chest focal point full torso both legs to ankle, STARK WHITE moonbeam ray lines both legs hip to toe filling every gap. Pose: full frontal wide stance both arms extended wide open chin up eyes fierce, bust full moon chest focal point fully forward maximum projection dominating entire left half of frame.
LEFT: silver cobalt platform stilettos 8 inch, extra long coffin nails silver blue tips.

RIGHT: Japanese silver fox goddess warm golden-ivory complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, silver-streaked vintage waves deep side part glamorous — full body Mount Fuji sakura moonlight irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID PINK sakura bloom formations full torso both legs neck to ankle, VIVID COBALT BLUE Fuji silhouette formations filling every gap, STARK GOLD moonlight shimmer both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: pink cobalt platform stilettos 8 inch, extra long stiletto nails pink gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_mughal_empress": {
    "title": "SF Duo – Mughal Empress",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-white vintage finger waves deep side part glamorous — full body Mughal empire floral arch irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Mughal jali lattice arch formation centered directly on each breast individually as supreme imperial dual focal points, pietra dura inlay formations expanding outward from each breast spanning chest completely, VIVID CRIMSON Mughal poppy bloom radiating from chest focal points full torso both legs to ankle, STARK TURQUOISE Taj Mahal marble inlay formations both legs hip to toe filling every gap. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating left half of frame, one hand pressing outward on hip.
LEFT: gold crimson platform stilettos 8 inch, extra long coffin nails gold turquoise tips.

RIGHT: Pakistani silver fox goddess warm olive South Asian complexion elegant silver-era maturity, early 50s, extreme corset hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked long straight hair center part flowing — full body Kashmir paisley shawl irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING VIVID CRIMSON Kashmir paisley teardrop formations full torso both legs neck to ankle, VIVID GOLD Mughal botanical vine scroll filling every gap, STARK TURQUOISE cashmere shawl border formations both legs hip to toe. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Kashmir paisley focal point dominating frame maximum projection.
RIGHT: crimson turquoise platform stilettos 8 inch, extra long stiletto nails crimson gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_northern_star": {
    "title": "SF Duo – Northern Star",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-white short crop cut razor sharp — full body aurora borealis polar star irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC CYAN aurora polar star burst anchored directly at chest midpoint between both breasts as supreme radiant focal point, polar star rays expanding outward from chest center spanning both breasts completely, VIVID MAGENTA aurora ribbon formations radiating from chest star focal point full torso both legs to ankle, STARK GREEN aurora curtain formations filling every gap neck to ankle. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust aurora polar star chest focal point fully forward maximum projection dominating entire left half of frame.
LEFT: cyan magenta platform stilettos 8 inch, extra long coffin nails cyan magenta tips.

RIGHT: Nordic silver fox goddess pale porcelain complexion elegant silver-era maturity, mid 40s, extreme hourglass bubble butt physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-white long straight hair center part flowing — full body Viking Vegvisir runic compass irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC SILVER Vegvisir runic compass formations full torso both legs neck to ankle, VIVID ICE BLUE Elder Futhark rune formations filling every gap, STARK WHITE Norse knotwork interlace both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: silver ice platform stilettos 8 inch, extra long stiletto nails silver white tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_nile_goddess": {
    "title": "SF Duo – Nile Goddess",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, most dramatic hourglass ratio ever rendered, bust so overwhelmingly massive defying gravity completely projecting forward, thighs powerful and thick pressing together, silver-white blunt bob jaw length — full body Nile lotus papyrus irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Nile lotus bloom formation fully open centered directly at chest midpoint between both breasts as supreme sacred focal point, lotus petals expanding outward from chest center spanning both breasts completely, VIVID TURQUOISE papyrus reed formations radiating from chest focal point full torso both legs to ankle, STARK LAPIS LAZULI scarab beetle formations both legs hip to toe filling every gap. Pose: leaning slightly forward chin dropped direct fierce eye contact both arms hanging naturally, bust Nile lotus chest focal point forward maximum projection fully visible.
LEFT: gold turquoise platform stilettos 8 inch, extra long coffin nails gold turquoise tips.

RIGHT: Sudanese silver fox goddess warm rich dark mahogany complexion elegant silver-era maturity, mid 40s, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together at maximum, waist snatched to impossible minimum, silver-streaked vintage finger waves deep side part glamorous — full body Nubian gold meroe pyramid irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Nubian pyramid formation full torso both legs neck to ankle, VIVID CRIMSON Kushite royal cartouche formations filling every gap, STARK TURQUOISE Meroe geometric diamond formations both legs hip to toe. Pose: back three-quarter turned face over left shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: gold crimson platform stilettos 8 inch, extra long stiletto nails gold turquoise tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_yoruba_goddess": {
    "title": "SF Duo – Yoruba Goddess",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, mid 40s silver fox goddess, extreme thick thigh temptress physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — thighs so impossibly massively thick crushing together at absolute maximum girth from hip to knee, hips wide and commanding, bust so overwhelmingly massive defying gravity completely projecting forward, waist dramatically snatched, silver-white vintage waves deep side part glamorous — full body Yoruba Oshun river goddess irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Oshun sacred mirror formation centered directly on each breast individually as supreme Orisha dual focal points, river current formations expanding outward from each breast spanning chest completely, VIVID AMBER honey drip formations radiating from chest focal points full torso both legs to ankle, STARK CRIMSON Yoruba adire textile formations both legs hip to toe filling every gap. Pose: full frontal wide stance both arms raised overhead offering pose chin up divine, bust Oshun sacred mirror dual focal points fully forward maximum projection dominating entire left half of frame.
LEFT: gold amber platform stilettos 8 inch, extra long coffin nails gold amber tips.

RIGHT: Nigerian silver fox goddess rich warm dark ebony complexion elegant silver-era maturity, early 50s, extreme bubble butt hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs crushing together, silver-streaked long straight hair center part flowing — full body Ogun iron warrior irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC SILVER iron chain formation full torso both legs neck to ankle, VIVID GOLD Yoruba geometric adinkra formations filling every gap, STARK CRIMSON warrior scarification mark formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand pressing outward on hip.
RIGHT: silver crimson platform stilettos 8 inch, extra long stiletto nails silver gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_georgian_vine": {
    "title": "SF Duo – Georgian Vine",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, early 50s silver fox goddess, extreme wide hip narrow waist physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — hips so dramatically wide extending beyond frame, waist cinched to absolute impossible minimum, bust so overwhelmingly massive defying gravity completely projecting forward, legs powerful and thick from massive hips, silver-white vintage finger waves deep side part — full body Georgian grapevine Bolnisi cross irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Georgian Bolnisi cross formation centered directly on each breast individually as supreme sacred dual focal points, grapevine leaf cluster formations expanding outward from each breast spanning chest completely, VIVID CRIMSON Georgian wine grape cluster formations radiating from chest focal points full torso both legs to ankle, STARK EMERALD Georgian vine scroll formations both legs hip to toe filling every gap. Pose: strong hip pop right hand on waist left arm extended elegantly, bust Bolnisi cross dual focal points forward maximum projection clearly visible.
LEFT: gold crimson platform stilettos 8 inch, extra long coffin nails gold emerald tips.

RIGHT: Georgian silver fox goddess warm olive Caucasian complexion elegant silver-era maturity, mid 40s, extreme bubble butt corset physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle, thighs powerfully thick pressing together, silver-streaked long straight hair center part flowing — full body Georgian polyphony manuscript irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Georgian Asomtavruli script formations full torso both legs neck to ankle, VIVID GOLD Georgian church fresco formations filling every gap, STARK CRIMSON Georgian enamel cloisonné formations both legs hip to toe. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating right half of frame, one hand on hip.
RIGHT: cobalt gold platform stilettos 8 inch, extra long stiletto nails cobalt crimson tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

"sf_duo_zulu_lion": {
    "title": "SF Duo – Zulu Lion",
    "category": "🦁 Silver Fox DUO",
    "platform": "gemini",
    "aspect_ratio": "2:3",
    "prompt": """Professional fashion photograph, full body shot. TWO women standing side by side.

LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, late 40s silver fox goddess, extreme bubble butt goddess physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — bubble butt so impossibly enormous projecting backward at maximum impossible distance, hips so wide extending beyond frame, bust so overwhelmingly massive defying gravity completely projecting forward, thighs crushing together at maximum, waist snatched to impossible minimum, silver-white long curly waves cascading to shoulders — full body Zulu lion pride irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC GOLD Zulu lion face formation centered directly on each breast individually as supreme African dual focal points, lion mane corona formation expanding outward from each breast spanning chest completely, VIVID CRIMSON African sunset savanna formations radiating from chest focal points full torso both legs to ankle, STARK AMBER acacia tree silhouette formations both legs hip to toe filling every gap. Pose: back three-quarter turned face over right shoulder smoldering direct eye contact, bust lion face dual focal points profile clearly visible from side angle, bubble butt projecting backward at maximum impossible distance dominating left half of frame, one hand pressing outward on hip.
LEFT: gold amber platform stilettos 8 inch, extra long coffin nails gold crimson tips.

RIGHT: South African silver fox goddess warm dark mahogany complexion elegant silver-era maturity, mid 40s, extreme corset hourglass physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — waist cinched to absolute impossible corset minimum, hips AND bust simultaneously flaring to absolute maximum, bust so overwhelmingly massive defying gravity completely with bust profile clearly visible from side angle projecting forward, thighs powerfully thick pressing together, silver-streaked vintage finger waves deep side part — full body Ndebele geometric wall art irezumi covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION. Bold black ink outlines — BLAZING ELECTRIC COBALT BLUE Ndebele geometric triangle formations full torso both legs neck to ankle, VIVID CRIMSON Ndebele bold outline formations filling every gap, STARK GOLD Ndebele beadwork formations both legs hip to toe. Pose: full frontal wide stance both fists on outer hips pressing outward chin up commanding, bust Ndebele geometric focal point dominating frame maximum projection.
RIGHT: cobalt crimson platform stilettos 8 inch, extra long stiletto nails cobalt gold tips.

All: extreme high-gloss oil. MANDATORY pure pitch black void background only. NO arm crossing over chest, NO pose blocking adjacent figure. TWO women only. 8K portrait 2:3 vertical."""
},

}  # end presets dict

# JSON 파일 개별 생성
for key, data in presets.items():
    filepath = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Created: {filepath}")

print(f"\n🎉 총 {len(presets)}개 JSON 파일 생성 완료!")
print(f"   HOF: 27개 / SSS: 8개")
