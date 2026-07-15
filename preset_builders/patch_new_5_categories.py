# -*- coding: utf-8 -*-
"""
LumineX 신규 5개 카테고리 패치
- 🌙 Night Glamour (8종)
- 👗 Slip Dress Glamour (9종)
- 🐆 Animal Print Glamour (8종)
- ⚔️ Power & Edge Glamour (8종)
- 🏖️ Beach & Resort Glamour (12종)

HOF: 17종 / SSS: 28종

실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_new_5_categories.py
"""

import json
import os
import sys

PRESETS_DIR = "presets"
META_FILE = "core/presets_meta.py"
HOF_FILE = "core/hof_tier.py"

# ──────────────────────────────────────────────
# 프롬프트 데이터
# ──────────────────────────────────────────────

PRESETS = {

    # ── 🌙 Night Glamour ──────────────────────────────────────────
    "night_super_glamour_penthouse": {
        "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess, impossibly cinched waist, maximum curves, mid-20s, Middle Eastern features, warm caramel skin gleaming, voluminous jet-black waves. Wearing: ultra-minimal black micro sequin triangle bikini top barely covering, matching micro sequin thong, black patent thigh-high platform stiletto boots 6-inch heel. Environment: ultra-luxury penthouse, floor-to-ceiling glass wall, city blazing below in full night blue-gold, interior chandelier warm above. Lighting: city ambient blue-gold through glass + warm chandelier overhead, caramel skin luminous, sequins catching city light as living constellation on curves. Style: supreme glamour night penthouse editorial, maximum curves commanding city night. Shot on Hasselblad X2D, 8K UHD, night city grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "penthouse", "sequin", "city", "super_glamour"],
        "aspect_ratio": "2:3"
    },
    "night_bbw_jazz_club": {
        "prompt": "Professional fashion photograph, full body shot. Model: super BBW goddess, massively full voluminous curves, late-20s, West African features, deep ebony skin, voluminous natural locs piled high. Wearing: ultra-minimal deep red satin micro slip dress riding high on full thighs, spaghetti straps barely there, red patent thigh-high platform stiletto boots 6-inch heel, gold hoop earrings, gold chain choker. Environment: intimate jazz club stage, saxophone player silhouette in warm amber behind, candles on tables, audience in dark, microphone stand at side. Lighting: single overhead amber spot on stage + candle warm from tables, deep ebony skin blazing in amber spotlight, red satin catching warm light as liquid crimson on full curves. Style: BBW night jazz club stage glamour, full figure owning the spotlight. Shot on Phase One XF IQ4, 8K UHD, jazz amber grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "jazz", "bbw", "stage", "red"],
        "aspect_ratio": "2:3"
    },
    "night_amazon_rooftop_rain": {
        "prompt": "Professional fashion photograph, full body shot. Model: amazon goddess, 185cm towering powerful physique, extreme muscle definition with feminine curves, mid-20s, East African features, deep bronze-copper skin soaked in rain, natural afro rain-wild and electric. Wearing: ultra-minimal silver chainmail micro dress soaking and clinging to every powerful muscle, micro thong visible through soaked silver, silver chrome thigh-high platform stiletto boots 6-inch heel in rooftop rain puddles, single silver cuff. Environment: luxury rooftop in heavy storm, neon city blazing below in rain, lightning splitting storm sky, rain cascading everywhere, wet concrete mirror-reflecting neon. Lighting: neon city rainbow from below through rain + lightning flash backlit, rain streaks as silver lines, soaked bronze skin blazing between neon and lightning. Style: amazon night rooftop storm editorial, towering power in rain. Shot on Hasselblad X2D, 8K UHD, storm neon grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "rain", "amazon", "rooftop", "storm", "silver"],
        "aspect_ratio": "2:3"
    },
    "night_latina_neon_alley": {
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass goddess, maximum sculpted curves, early-20s, Latina features, warm olive-bronze skin, long voluminous dark waves with natural burgundy, full lips. Wearing: ultra-minimal holographic micro dress shifting pink-purple neon colors, plunging neckline, skirt barely below hips, gold chrome thigh-high platform stiletto boots 6-inch heel in neon rain puddles, crystal ear cuffs. Environment: neon-drenched cyberpunk alleyway, pink and purple neon signs covering every surface, rain puddles reflecting neon city glow below boots, wires overhead, city depth receding behind. Lighting: full pink-purple neon from all alley sign positions + neon puddle reflection from below, olive-bronze skin in total neon color saturation, holographic dress shifting with every neon source. Style: Colombian night neon alley cyberpunk glamour, maximum curves in neon city. Shot on Phase One XF IQ4, 8K UHD, cyberpunk neon grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "neon", "latina", "cyberpunk", "holographic"],
        "aspect_ratio": "2:3"
    },
    "night_vs_angel_casino": {
        "prompt": "Professional fashion photograph, full body shot. Model: VS Angel goddess, flawless perfect hourglass, long legs, mid-20s, Northern European features, sun-kissed golden skin, long tousled beach waves, sharp cheekbones. Wearing: ultra-minimal ivory satin bias-cut micro slip dress with thigh-high slit, spaghetti straps, white platform stiletto ankle boots 5-inch heel on marble casino floor, diamond drop earrings, diamond tennis bracelet. Environment: grand luxury casino floor, massive crystal chandelier dominating above, mirror ceiling reflecting figure below chandeliers, roulette tables active behind, dealers in tuxedos. Lighting: chandelier crystal warm gold from above + mirror ceiling reflection duplicating figure, golden skin luminous in casino chandelier light, ivory satin as white flame on long figure. Style: VS Angel night casino luxury editorial, flawless figure owning the casino floor. Shot on Hasselblad X2D, 8K UHD, casino crystal grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "casino", "vs_angel", "chandelier", "ivory"],
        "aspect_ratio": "2:3"
    },
    "night_black_glamour_moonrise": {
        "prompt": "Professional fashion photograph, full body shot. Model: black glamour goddess, maximum ebony hourglass, spectacular curves, late-20s, Southern African features, deepest jet-black skin, voluminous natural coils with silver moonlight edges. Wearing: ultra-minimal midnight velvet micro off-shoulder dress barely covering maximum curves, micro length on full thighs, black patent thigh-high platform stiletto boots 6-inch heel on cliff rock, moonstone choker glowing silver. Environment: dramatic cliff edge at full moonrise, full silver moon dominating entire sky behind figure, dark ocean far below, silver moon path on water stretching to horizon. Lighting: full moon silver from rising position behind + reflected moon path from ocean below, jet-black skin silver-edge lit by moonrise on every curve, moonstone choker as only warm light point. Style: black glamour night cliff moonrise editorial, jet curves against silver moon. Shot on Phase One XF IQ4, 8K UHD, moonrise silver grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "moon", "cliff", "black_glamour", "silver"],
        "aspect_ratio": "2:3"
    },
    "night_hot_glamour_club_vip": {
        "prompt": "Professional fashion photograph, full body shot. Model: hot glamour goddess, dramatic cinched hourglass, perfectly sculpted curves, early-20s, Southeast Asian features, warm honey-bronze skin, long straight glossy black hair with subtle waves, full lips. Wearing: ultra-minimal black latex micro bodycon dress vacuum-tight on every curve, dress barely below hips, plunging V neckline, black stiletto thigh-high platform boots 5-inch heel, gold body chain at waist, gold ear studs. Environment: VIP nightclub booth elevated above dance floor, magenta and gold strobe lights, bottle service with sparklers, crowd below VIP level, velvet ropes. Lighting: magenta-gold strobe from club positions cutting through smoke + golden bottle service sparkler glow, honey-bronze skin blazing in club strobe color, latex dress catching every light as black mirror on curves. Style: hot glamour VIP nightclub latex editorial, maximum curves in club strobe. Shot on Hasselblad X2D, 8K UHD, club strobe grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "club", "vip", "latex", "hot_glamour"],
        "aspect_ratio": "2:3"
    },
    "night_miniature_starlight_terrace": {
        "prompt": "Professional fashion photograph, full body shot. Model: miniature goddess, ultra-petite compact perfect figure, early-20s, East Asian features, porcelain skin, long straight platinum-dyed hair loose, doe eyes, tiny waist. Wearing: ultra-minimal white ruched micro bodycon dress barely below hips, thin spaghetti straps, white crystal platform ankle strap heels 4-inch, star-drop crystal earrings, delicate gold ankle bracelet. Environment: luxury rooftop terrace under perfect starfield, warm fairy lights strung overhead in canopy, city glow at distant horizon, potted jasmine and olive trees, intimate warm night atmosphere. Lighting: fairy light warm amber from overhead string canopy + Milky Way cool ambient from above, porcelain skin glowing warm below and cool above, fairy lights bokeh surrounding figure. Style: miniature night starlight terrace glamour, tiny perfect figure commanding star-filled sky. Shot on Phase One XF IQ4, 8K UHD, starlight fairy grade, portrait 2:3 vertical.",
        "category": "🌙 Night Glamour",
        "tags": ["night", "starlight", "terrace", "miniature", "fairy_lights"],
        "aspect_ratio": "2:3"
    },

    # ── 👗 Slip Dress Glamour ─────────────────────────────────────
    "slip_super_glamour_marble": {
        "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess, impossibly cinched waist, maximum curves, mid-20s, Middle Eastern features, warm olive-golden skin gleaming oiled, voluminous jet-black waves cascading to waist, smoky cat eye makeup, full lips glossed. Wearing: ultra-minimal ivory silk slip dress bias-cut, spaghetti straps barely there, dress riding dangerously high on full thighs, deep V neckline plunging, gold stiletto thigh-high platform boots 6-inch heel on marble floor, single diamond ear stud, gold body chain at waist. Environment: ultra-luxury Carrara marble bathroom, floor-to-ceiling white marble, frosted glass window with sharp morning side light, minimalist luxury space, zero clutter. Lighting: sharp morning side light through frosted glass, olive-golden skin luminous in marble-reflected white light, silk slip catching light as liquid ivory on maximum curves. Style: supreme glamour marble morning slip dress editorial, maximum curves in minimalist luxury. Shot on Hasselblad X2D, 8K UHD, marble morning grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "marble", "morning", "super_glamour", "ivory"],
        "aspect_ratio": "2:3"
    },
    "slip_bbw_champagne_bedroom": {
        "prompt": "Professional fashion photograph, full body shot. Model: super BBW goddess, massively full voluminous curves commanding entire frame, late-20s, West African features, rich deep ebony skin, voluminous natural locs loose and heavy, bold lips, strong jaw. Wearing: ultra-minimal champagne satin slip dress pooling at floor, spaghetti straps disappearing into full shoulders, satin vacuum-tight on every magnificent curve before pooling, bare feet with gold toe ring, gold layered chains at neck, gold cuff bracelet. Environment: king suite bedroom, silk sheets in ivory spilling off bed, golden morning light flooding through sheer curtains, champagne flute on nightstand, rumpled luxury atmosphere. Lighting: warm golden morning through sheer curtains flooding frame, deep ebony skin blazing in morning gold, champagne satin as liquid gold over full magnificent curves. Style: BBW champagne morning slip dress boudoir, full goddess in morning gold. Shot on Phase One XF IQ4, 8K UHD, morning gold grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "champagne", "bedroom", "bbw", "morning"],
        "aspect_ratio": "2:3"
    },
    "slip_amazon_rain_window": {
        "prompt": "Professional fashion photograph, full body shot. Model: amazon goddess, 185cm towering powerful physique, extreme muscle definition with feminine curves, mid-20s, East African features, deep bronze skin, natural afro pressed flat against window frame light, severe expression, sharp cheekbones. Wearing: ultra-minimal charcoal silk slip dress stretched over defined muscle groups, spaghetti straps thin on powerful shoulders, slip pulling tight across broad back visible from side angle, silver chrome thigh-high platform stiletto boots 6-inch heel on dark hardwood floor, single geometric silver ear cuff. Environment: luxury high-rise interior, floor-to-ceiling rain-streaked window, grey storm city outside, rain cascading down glass in rivers, moody dark interior, height visible far below. Lighting: grey storm-diffused city light through rain-streaked glass, bronze skin in cool grey storm light, rain streaks creating silver texture behind powerful silhouette. Style: amazon rain window slip dress power editorial, towering muscle in storm light. Shot on Hasselblad X2D, 8K UHD, rain window grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "rain", "window", "amazon", "storm"],
        "aspect_ratio": "2:3"
    },
    "slip_bust_queen_vanity": {
        "prompt": "Professional fashion photograph, full body shot. Model: bust queen goddess, legendary full bust with perfect cinched waist, early-30s, South Asian features, warm honey-bronze skin, long glossy black hair loose and wavy, kohl-lined eyes, deep red lips. Wearing: ultra-minimal blush pink satin slip dress with delicate lace trim, one strap slipping naturally off shoulder revealing full décolletage, dress micro-short on full thighs, red patent platform stiletto mules 5-inch heel on vintage rug, pearl drop earrings, pearl bracelet, crystal perfume bottle held in hand. Environment: antique Hollywood vanity with bulb mirror, pearl necklaces and crystal perfume bottles covering surface, warm amber bulb light, plush velvet stool, old Hollywood intimate boudoir atmosphere. Lighting: Hollywood vanity amber bulbs from mirror position wrapping figure in warm glow, honey-bronze skin luminous in old Hollywood light, blush satin shimmering warm on legendary curves. Style: bust queen old Hollywood vanity slip dress boudoir, legendary figure in amber glamour. Shot on Phase One XF IQ4, 8K UHD, old Hollywood grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "vanity", "bust_queen", "hollywood", "boudoir"],
        "aspect_ratio": "2:3"
    },
    "slip_latina_poolside_dawn": {
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass goddess, maximum sculpted curves, early-20s, Latina features, warm olive-bronze skin, long dark waves loose in dawn breeze, full lips, fierce brow. Wearing: ultra-minimal coral silk slip dress, spaghetti straps, dress hem skimming perfectly still pool surface at feet, deep side slit to hip revealing full thigh, coral gold stiletto platform mules 5-inch heel at pool edge, minimal gold ear studs, gold ankle bracelet. Environment: luxury resort pool at dawn, perfectly still water reflecting sunrise coral and gold colors, palm trees silhouetted against sunrise horizon, resort absolute silence at first light. Lighting: sunrise golden-coral from horizon behind flooding frame + pool water golden reflection rippling upward from below, olive-bronze skin lit from both above and below in golden dawn. Style: Colombian poolside dawn slip dress resort editorial, dramatic curves in golden dawn light. Shot on Hasselblad X2D, 8K UHD, dawn gold grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "pool", "dawn", "latina", "coral"],
        "aspect_ratio": "2:3"
    },
    "slip_vs_angel_hotel_corridor": {
        "prompt": "Professional fashion photograph, full body shot. Model: VS Angel goddess, flawless perfect hourglass, long endless legs, early-20s, Brazilian features, sun-kissed golden-bronze skin, long beach waves moving in corridor air, full lips, expression ethereal-walking. Wearing: ultra-minimal white silk slip dress barely containing perfect hourglass, dress hem above mid-thigh on long legs, deep V front and deep V back plunge, white platform stiletto mules 5-inch heel on marble corridor floor, single delicate gold chain necklace, diamond stud earrings. Environment: five-star luxury hotel corridor, symmetrical warm wall sconces receding to perfect infinity vanishing point, ivory marble floor reflecting figure below. Lighting: warm wall sconces from both sides creating symmetrical warm glow receding to infinity, golden-bronze skin warm in sconce light bilateral, white silk dress as glowing white flame on perfect figure in corridor. Style: VS Angel hotel corridor slip dress ethereal editorial, perfect figure in symmetrical luxury. Shot on Phase One XF IQ4, 8K UHD, corridor symmetry grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "hotel", "corridor", "vs_angel", "symmetry"],
        "aspect_ratio": "2:3"
    },
    "slip_black_glamour_midnight_terrace": {
        "prompt": "Professional fashion photograph, full body shot. Model: black glamour goddess, maximum ebony hourglass, spectacular curves, late-20s, Kenyan features, deepest jet-black skin, voluminous natural coils loose in warm night air, bold lip, strong features. Wearing: ultra-minimal black silk slip dress with thin gold spaghetti straps barely visible against jet skin, dress micro-short revealing full thighs, black patent platform stiletto mules 5-inch heel on terrace stone, single gold ring on finger. Environment: private luxury penthouse terrace at midnight, pillar candles flickering on stone railing in line, distant city lights warm amber at horizon, jasmine potted plants. Lighting: pillar candle warm amber from railing line + distant city warm ambient glow, jet-black skin absorbing everything except gold strap-lines catching candle flame. Style: black glamour midnight terrace slip dress editorial, jet curves in candlelight gold. Shot on Hasselblad X2D, 8K UHD, midnight candle grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "midnight", "terrace", "black_glamour", "candle"],
        "aspect_ratio": "2:3"
    },
    "slip_hot_glamour_silk_sheets": {
        "prompt": "Professional fashion photograph, full body shot. Model: hot glamour goddess, dramatic perfectly cinched hourglass, sculpted curves everywhere, mid-20s, Persian features, warm golden-caramel skin, long dark waves spread across pillow, heavy-lidded expression, full lips slightly parted. Wearing: ultra-minimal dusty rose satin slip dress ridden up on full hips in reclining position, one strap falling off shoulder, dress barely covering curves in recline, rose gold platform stiletto mules 4-inch heel visible at silk sheet edge, rose gold chain bracelet. Environment: ultra-luxury bedroom, ivory and cream silk sheets pooling everywhere, afternoon sun casting long golden shadow bars across bed and figure. Lighting: late afternoon golden through window casting long warm shadow bars across silk sheets and reclining figure, golden-caramel skin warm in afternoon gold between shadow bars. Style: hot glamour silk sheets afternoon slip dress boudoir, sculpted curves in afternoon gold. Shot on Phase One XF IQ4, 8K UHD, boudoir afternoon grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "silk_sheets", "boudoir", "hot_glamour", "afternoon"],
        "aspect_ratio": "2:3"
    },
    "slip_supermodel_airport_lounge": {
        "prompt": "Professional fashion photograph, full body shot. Model: supermodel tall goddess, 185cm+ extreme tall frame, impossibly long legs, mid-20s, Northern European features, alabaster skin, sleek center-part silver-blonde hair severe, sharp cheekbones cutting, cold editorial expression. Wearing: ultra-minimal camel silk slip dress hanging in perfect drape on extreme tall frame, dress midi-length on tall figure revealing long legs from knee down, deep side slit, clear platform stiletto mules 6-inch heel on private lounge marble, single architectural gold geometric ear cuff, oversized sunglasses carried in hand, minimal gold watch. Environment: private aviation terminal lounge, floor-to-ceiling glass wall overlooking private jets on tarmac, cool blue-grey pre-dawn light, minimalist luxury lounge furniture. Lighting: cool blue-grey pre-dawn through terminal glass from tarmac side, alabaster skin in cool aviation pre-dawn light, private jets silhouetted behind tall goddess figure. Style: supermodel private aviation slip dress travel editorial, extreme tall goddess in cool luxury. Shot on Hasselblad X2D, 8K UHD, aviation lounge grade, portrait 2:3 vertical.",
        "category": "👗 Slip Dress Glamour",
        "tags": ["slip_dress", "airport", "supermodel", "aviation", "camel"],
        "aspect_ratio": "2:3"
    },

    # ── 🐆 Animal Print Glamour ───────────────────────────────────
    "animal_super_glamour_leopard_gown": {
        "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess, impossibly cinched waist, maximum curves, mid-20s, Iranian features, warm olive-golden skin gleaming oiled, voluminous jet-black waves cascading to waist, smoky cat eye makeup, full lips glossed. Wearing: ultra-minimal leopard print silk micro gown, plunging neckline to navel, thigh-high slit revealing full leg, barely containing maximum curves, gold stiletto thigh-high platform boots 6-inch heel, gold leopard-spot choker, gold cuff bracelet. Environment: black infinity studio backdrop, single hard overhead spot from above, nothing but figure and leopard print, pure editorial darkness. Lighting: single hard overhead spot, leopard print in full graphic predator detail on maximum curves, olive-golden skin warm between leopard panels, dramatic chiaroscuro total. Style: supreme glamour leopard silk gown predator editorial, maximum curves as apex predator. Shot on Hasselblad X2D, 8K UHD, predator glamour grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "leopard", "gown", "super_glamour", "studio"],
        "aspect_ratio": "2:3"
    },
    "animal_bbw_zebra_bodycon": {
        "prompt": "Professional fashion photograph, full body shot. Model: super BBW goddess, massively full voluminous curves filling entire frame, late-20s, Nigerian features, deep rich ebony skin, voluminous natural afro puff high, bold full lips, strong jaw. Wearing: ultra-minimal zebra print latex micro bodycon dress vacuum-tight on every full curve, high-contrast black and white graphic wrapping magnificent figure, black patent thigh-high platform stiletto boots 6-inch heel, white geometric oversized ear studs. Environment: pure white infinity studio backdrop, graphic fashion editorial space, white seamless floor. Lighting: hard white fashion editorial overhead + white fill from both sides, maximum contrast zebra graphic on full magnificent curves, deep ebony skin rich against stark black-white graphic. Style: BBW zebra latex bodycon graphic power editorial, full figure as graphic art. Shot on Phase One XF IQ4, 8K UHD, graphic fashion grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "zebra", "bodycon", "bbw", "latex"],
        "aspect_ratio": "2:3"
    },
    "animal_amazon_cheetah_latex": {
        "prompt": "Professional fashion photograph, full body shot. Model: amazon goddess, 185cm towering powerful physique, extreme muscle definition with feminine curves, early-20s, Ethiopian features, deep bronze-copper skin oiled and gleaming, natural afro wild and electric, fierce bone structure. Wearing: ultra-minimal cheetah print latex micro bodysuit, latex vacuum-tight on every muscle group, cheetah spots catching amber light as speed on powerful frame, amber chrome thigh-high platform stiletto boots 6-inch heel, amber crystal forearm cuffs. Environment: African savanna at dusk, amber horizon blazing, acacia tree silhouettes dark against amber sky, dusk atmosphere total, power stance in golden grass. Lighting: amber-gold dusk from blazing horizon behind + hard frontal spot, cheetah latex catching dusk amber as liquid gold on muscle, bronze-copper skin blazing in savanna dusk. Style: amazon cheetah latex savanna power editorial, towering muscle as apex predator. Shot on Hasselblad X2D, 8K UHD, savanna dusk grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "cheetah", "latex", "amazon", "savanna"],
        "aspect_ratio": "2:3"
    },
    "animal_bust_queen_snakeskin_dress": {
        "prompt": "Professional fashion photograph, full body shot. Model: bust queen goddess, legendary full bust with perfect cinched waist, early-30s, Brazilian features, warm honey-caramel skin, long glossy dark waves with subtle auburn highlights, kohl-lined eyes, deep berry lips. Wearing: ultra-minimal emerald green snakeskin print micro wrap dress, deep V neckline plunging between legendary bust, wrap barely covering full thighs, emerald patent thigh-high platform stiletto boots 5-inch heel, emerald drop earrings, gold snake armband. Environment: luxury penthouse interior, floor-to-ceiling glass, tropical city below, warm editorial interior. Lighting: warm penthouse interior spot from above + tropical city ambient from glass behind, honey-caramel skin warm in luxury light, emerald snakeskin rich and saturated as jewel. Style: bust queen snakeskin wrap luxury penthouse editorial, legendary curves in reptile luxury. Shot on Phase One XF IQ4, 8K UHD, reptile luxury grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "snakeskin", "wrap_dress", "bust_queen", "emerald"],
        "aspect_ratio": "2:3"
    },
    "animal_latina_tiger_mini": {
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass goddess, maximum sculpted curves, early-20s, Colombian features, warm bronze-terra cotta skin, voluminous dark waves with copper highlights wild in jungle air, full lips, fierce brow arch. Wearing: ultra-minimal orange tiger stripe micro mini dress, skirt micro-short barely covering hips, tiger stripe vacuum-tight on every extreme curve, amber gold stiletto thigh-high platform boots 6-inch heel, amber crystal drop earrings, gold tiger claw pendant. Environment: lush tropical jungle interior, dappled golden-green light through dense canopy, massive jungle leaves framing figure, warm humid atmosphere. Lighting: dappled golden-green jungle canopy from above filtering, tiger stripe catching golden jungle light as warm fire pattern on dramatic curves, bronze-terra cotta skin warm in tropical dapple. Style: Colombian tiger mini jungle predator editorial, maximum curves commanding jungle. Shot on Hasselblad X2D, 8K UHD, tropical predator grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "tiger", "mini", "latina", "jungle"],
        "aspect_ratio": "2:3"
    },
    "animal_vs_angel_leopard_boudoir": {
        "prompt": "Professional fashion photograph, full body shot. Model: VS Angel goddess, flawless perfect hourglass, long endless legs, early-20s, Venezuelan features, sun-kissed golden-bronze skin, long tousled beach waves loose, full lips slightly parted, expression intimate-fierce. Wearing: ultra-minimal leopard print satin micro bra and matching micro thong set, matching leopard satin robe open and trailing behind, white patent platform stiletto mules 5-inch heel, gold leopard-print hoop earrings, delicate gold body chain. Environment: luxury boudoir, ivory silk draped everywhere, warm candle clusters on surfaces, satin and velvet textures, leopard print accent pillow visible. Lighting: warm candle amber from multiple candle positions wrapping figure in warm glow, golden-bronze skin luminous in candle warmth, leopard satin set catching warm light as rich print pattern. Style: VS Angel leopard satin boudoir intimate editorial, perfect figure in candlelit predator luxury. Shot on Phase One XF IQ4, 8K UHD, boudoir luxury grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "leopard", "boudoir", "vs_angel", "satin"],
        "aspect_ratio": "2:3"
    },
    "animal_black_glamour_panther_catsuit": {
        "prompt": "Professional fashion photograph, full body shot. Model: black glamour goddess, maximum ebony hourglass, spectacular curves, mid-20s, Sudanese features, deepest jet-black skin, voluminous natural coils sculpted high, bold purple lip, high cheekbones cutting. Wearing: ultra-minimal all-black panther print velvet micro catsuit, velvet texture creating pattern-in-darkness on jet skin, catsuit micro-short cut high on full thighs, black patent thigh-high platform stiletto boots 6-inch heel, single neon purple geometric ear cuff, purple nail lacquer only other color. Environment: obsidian black infinity studio, pure black void, figure emerging from darkness. Lighting: single neon purple rim light from behind right, panther velvet texture visible only in purple rim, purple ear cuff catching same light, jet skin and black velvet as absolute dark void. Style: black glamour panther velvet void editorial, jet curves in purple darkness. Shot on Hasselblad X2D, 8K UHD, absolute void grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "panther", "catsuit", "black_glamour", "velvet"],
        "aspect_ratio": "2:3"
    },
    "animal_powerlifter_croc_bodysuit": {
        "prompt": "Professional fashion photograph, full body shot. Model: powerlifter goddess, extreme defined musculature with feminine curves, late-20s, Russian features, cool ivory-alabaster skin, platinum hair scraped back in severe tight bun, ice-cold expression, sharp jaw. Wearing: ultra-minimal structured crocodile print leather micro bodysuit, leather panels conforming to every muscle group definition, croc texture catching hard light as sculptural relief on iron physique, matte black platform combat stiletto boots 5-inch heel, croc-leather wide forearm cuffs, single croc-leather choker. Environment: dark industrial luxury studio, raw concrete and brushed steel surfaces, single hard overhead industrial spot, steam barely visible at edges. Lighting: single hard overhead industrial spot, croc leather texture in full sculptural chiaroscuro on iron physique, ivory-alabaster skin cold in industrial hard light. Style: powerlifter crocodile leather industrial power editorial, iron physique in reptile structure. Shot on Phase One XF IQ4, 8K UHD, industrial power grade, portrait 2:3 vertical.",
        "category": "🐆 Animal Print Glamour",
        "tags": ["animal_print", "crocodile", "bodysuit", "powerlifter", "industrial"],
        "aspect_ratio": "2:3"
    },

    # ── ⚔️ Power & Edge Glamour ───────────────────────────────────
    "edge_super_glamour_chrome_armor": {
        "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess, impossibly cinched waist, maximum curves, mid-20s, Lebanese features, warm olive-gold skin oiled and gleaming, voluminous jet-black waves, smoky eye, bold lip. Wearing: ultra-minimal chrome mirror sculptural micro armor dress, armor panels barely covering maximum curves, each panel reflecting everything as living mirror, deep plunge between armor plates, gold stiletto thigh-high platform boots 6-inch heel, chrome mirror choker. Environment: dark industrial studio, single piercing overhead hard spot, pure darkness around figure. Lighting: single hard overhead spot only, chrome panels creating blinding reflection constellation around maximum curves, olive-gold skin blazing through chrome gaps, absolute chiaroscuro. Style: supreme glamour chrome mirror armor power editorial, maximum curves as chrome weapon. Shot on Hasselblad X2D, 8K UHD, chrome mirror grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "chrome", "armor", "super_glamour", "mirror"],
        "aspect_ratio": "2:3"
    },
    "edge_bbw_leather_commander": {
        "prompt": "Professional fashion photograph, full body shot. Model: super BBW goddess, massively full commanding figure, early-30s, Jamaican features, deep rich brown skin, voluminous locs whipping in rooftop wind, bold fierce expression, strong jaw. Wearing: ultra-minimal structured black leather micro jacket open over matching leather micro shorts, jacket barely covering full chest, shorts riding high on massive thighs, black patent thigh-high platform stiletto boots 6-inch heel, bold gold chain choker stacked triple, gold knuckle rings. Environment: luxury penthouse rooftop at dusk, city skyline full behind, wind whipping locs, dusk amber-purple sky, total city command. Lighting: dusk amber-purple from city horizon behind + hard frontal key, deep brown skin blazing in command dusk light, leather structure catching golden edge light. Style: BBW leather commander rooftop dusk editorial, full figure commanding city. Shot on Phase One XF IQ4, 8K UHD, command dusk grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "leather", "commander", "bbw", "rooftop"],
        "aspect_ratio": "2:3"
    },
    "edge_amazon_warrior_ruins": {
        "prompt": "Professional fashion photograph, full body shot. Model: amazon goddess, 185cm towering powerful physique, extreme muscle definition, late-20s, Nubian features, deep bronze-copper oiled skin, severe warrior braids with gold beads, battle-fierce expression. Wearing: ultra-minimal black gladiator-strap micro bodysuit, straps cutting across defined muscle groups, hardware gold on black straps, bodysuit high-cut revealing full powerful thighs, gold stiletto thigh-high platform warrior boots 6-inch heel on ancient stone, gold armband cuffs wide, gold warrior collar. Environment: ancient stone ruins at dramatic dusk, massive fallen columns, torch fire from ground positions, warrior goddess domain. Lighting: torch fire warm orange from low positions on ground + dramatic overhead hard spot, oiled bronze skin in torch chiaroscuro, gold hardware catching fire. Style: amazon warrior ruins gladiator editorial, towering power in ancient fire. Shot on Hasselblad X2D, 8K UHD, ancient warrior grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "warrior", "ruins", "amazon", "gladiator"],
        "aspect_ratio": "2:3"
    },
    "edge_latina_moto_latex": {
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass goddess, maximum sculpted curves, early-20s, Colombian features, warm olive-bronze skin, dark waves wild in garage atmosphere, full lips, fierce attitude. Wearing: ultra-minimal burgundy latex micro moto jacket, jacket barely zipped over full chest revealing deep cleavage, matching burgundy latex high-waist micro shorts vacuum-tight on every curve, burgundy patent thigh-high platform stiletto boots 6-inch heel, matte black motorcycle helmet held in one hand, gold stud earrings only. Environment: dark private garage, vintage motorcycle silhouette behind, single overhead industrial pendant light, raw concrete floor. Lighting: single overhead industrial pendant from above, latex catching as hard burgundy specular highlights on every curve, bronze-terra cotta skin in industrial chiaroscuro. Style: Colombian moto latex garage power editorial, maximum curves on chrome edge. Shot on Phase One XF IQ4, 8K UHD, industrial edge grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "moto", "latex", "latina", "garage"],
        "aspect_ratio": "2:3"
    },
    "edge_vs_angel_crystal_harness": {
        "prompt": "Professional fashion photograph, full body shot. Model: VS Angel goddess, flawless perfect hourglass, long endless legs, early-20s, Argentine features, warm golden-caramel skin, long blonde-highlighted waves, expression angel-meets-edge. Wearing: ultra-minimal nude micro bodysuit — crystal and silver chain harness overlay as architectural sculpture across perfect figure, harness framing bust and hips as jewelry-garment, white platform stiletto boots 5-inch heel, crystal chandelier ear cuffs, crystal choker, harness as hero piece against nude base. Environment: dark abstract studio, blue-white crystal architectural lighting from above positions. Lighting: blue-white crystal hard spots from upper multiple positions, crystal harness creating prismatic scatter across studio, golden-caramel skin warm between crystal lines. Style: VS Angel crystal chain harness high fashion edge editorial, perfect figure in crystal architecture. Shot on Hasselblad X2D, 8K UHD, crystal edge grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "crystal", "harness", "vs_angel", "architectural"],
        "aspect_ratio": "2:3"
    },
    "edge_black_glamour_obsidian_gown": {
        "prompt": "Professional fashion photograph, full body shot. Model: black glamour goddess, maximum ebony hourglass, spectacular curves, mid-20s, Congolese features, deepest jet-black skin, voluminous natural coils architectural high, bold red lip only color, high cheekbones cutting. Wearing: ultra-minimal structured obsidian black asymmetric micro gown, one shoulder architectural sharp point, gown micro-short on full thighs revealing maximum leg, thigh-high slit, black patent platform stiletto boots 6-inch heel, single fire opal choker glowing red-orange as only warmth in absolute dark. Environment: volcanic rock cliff edge at dusk, lava glow at horizon rim fire, volcanic darkness total, power domain. Lighting: lava fire rim orange from distant horizon behind + single hard front key, fire opal choker catching only warm light in total dark composition, jet skin volcanic edge-lit. Style: black glamour obsidian volcanic power editorial, jet curves at world's edge. Shot on Phase One XF IQ4, 8K UHD, volcanic dark grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "obsidian", "gown", "black_glamour", "volcanic"],
        "aspect_ratio": "2:3"
    },
    "edge_hot_glamour_cage_dress": {
        "prompt": "Professional fashion photograph, full body shot. Model: hot glamour goddess, dramatic perfectly cinched hourglass, sculpted curves everywhere, mid-20s, Turkish features, warm honey-olive skin, long dark waves with copper highlights, heavy-lidded expression, full glossed lips. Wearing: ultra-minimal black metal cage-structured micro dress, cage bars 3-5mm steel framing dramatic curves as living sculpture, crimson micro bodysuit visible through cage bars, cage skirt micro-short revealing full thighs, black stiletto thigh-high platform boots 5-inch heel, cage-bar choker matching, crimson nail lacquer echoing bodysuit. Environment: dark avant-garde editorial studio, dramatic red from one side + cold white from opposite side creating split color. Lighting: red gel from camera left + hard white from camera right, cage bars casting red-white shadow grid on honey-olive skin and crimson bodysuit, split color drama absolute. Style: hot glamour cage dress split-color avant-garde editorial, sculpted curves in steel cage. Shot on Hasselblad X2D, 8K UHD, avant-garde split grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "cage_dress", "hot_glamour", "avant_garde", "split_color"],
        "aspect_ratio": "2:3"
    },
    "edge_powerlifter_titanium_suit": {
        "prompt": "Professional fashion photograph, full body shot. Model: powerlifter goddess, extreme defined musculature with feminine power curves, late-20s, Ukrainian features, cool ivory skin with muscle definition visible everywhere, platinum hair severe center-part slicked, ice-cold expression, sharp angular jaw. Wearing: ultra-minimal sculptural titanium-finish micro bodysuit, bodysuit cut high on powerful thighs, titanium panels following every muscle contour, exoskeleton ribbing detail on titanium surface, matte black platform combat stiletto boots 5-inch heel, titanium wide forearm cuffs matching suit, titanium collar piece. Environment: dark sci-fi industrial corridor, cool metallic blue ambient, pipes and steel structure behind, absolute strength domain. Lighting: cool metallic blue from multiple corridor positions, titanium suit creating complex metallic specular over every extreme muscle definition, ivory skin cold in blue titanium light. Style: powerlifter titanium exoskeleton sci-fi power editorial, iron physique in titanium armor. Shot on Phase One XF IQ4, 8K UHD, titanium sci-fi grade, portrait 2:3 vertical.",
        "category": "⚔️ Power & Edge Glamour",
        "tags": ["power_edge", "titanium", "powerlifter", "sci_fi", "exoskeleton"],
        "aspect_ratio": "2:3"
    },

    # ── 🏖️ Beach & Resort Glamour ─────────────────────────────────
    "beach_super_glamour_maldives": {
        "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess, impossibly cinched waist, maximum curves, mid-20s, Moroccan features, warm golden-olive skin oiled and gleaming, voluminous dark waves in tropical breeze, smoky eye, full glossed lips. Wearing: ultra-minimal white micro string bikini, triangle top barely containing maximum curves, matching micro thong, gold stiletto platform heeled sandals 6-inch heel on overwater teak deck, gold wave choker, gold anklet. Environment: Maldives overwater villa deck, turquoise Indian Ocean infinity in every direction, crystal water below deck visible through glass panel, golden hour beginning at horizon. Lighting: golden hour tropical from warm horizon flooding frame + turquoise water reflection upward from below, golden-olive skin lit from both above and below in paradise gold. Style: supreme glamour Maldives overwater paradise editorial, maximum curves commanding Indian Ocean. Shot on Hasselblad X2D, 8K UHD, tropical paradise grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "maldives", "overwater", "super_glamour", "white_bikini"],
        "aspect_ratio": "2:3"
    },
    "beach_bbw_santorini": {
        "prompt": "Professional fashion photograph, full body shot. Model: super BBW goddess, massively full magnificent curves, late-20s, Ghanaian features, rich deep brown skin, voluminous locs loose in Aegean breeze, bold full lips. Wearing: ultra-minimal white micro string bikini barely covering full magnificent figure, open white linen micro cover-up jacket fully open, gold platform wedge sandals 5-inch heel on Santorini stone path, bold gold layered necklace, gold hoop earrings. Environment: Santorini Oia cliffside, iconic blue dome directly behind, white cycladic architecture, Caldera dropping away below, Mediterranean blazing blue sky and sea. Lighting: warm Mediterranean afternoon sun from low angle behind blue dome + Caldera reflection from below, deep brown skin blazing in Mediterranean golden, blue dome-white architecture as perfect frame behind full figure. Style: BBW Santorini Mediterranean luxury resort editorial, full goddess commanding Aegean. Shot on Phase One XF IQ4, 8K UHD, Mediterranean gold grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "santorini", "bbw", "mediterranean", "blue_dome"],
        "aspect_ratio": "2:3"
    },
    "beach_amazon_bali_surf": {
        "prompt": "Professional fashion photograph, full body shot. Model: amazon goddess, 185cm towering powerful physique, extreme muscle definition, mid-20s, Kenyan features, deep bronze skin soaked and gleaming in surf, natural afro water-wild and massive. Wearing: ultra-minimal bronze micro string bikini, soaked fabric vacuum-tight on powerful muscular frame, bronze chrome platform wedge sandals 5-inch heel at shoreline, single bronze arm cuff. Environment: Bali beach at golden hour, massive perfect breaking wave receding behind towering figure, volcanic black sand, golden afternoon surf light. Lighting: late Bali afternoon sun from low side angle, wet bronze skin blazing in surf golden light, wave water catching sun behind towering powerful figure. Style: amazon Bali surf goddess power editorial, towering muscle commanding ocean. Shot on Hasselblad X2D, 8K UHD, Bali surf grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "bali", "surf", "amazon", "bronze"],
        "aspect_ratio": "2:3"
    },
    "beach_bust_queen_tulum": {
        "prompt": "Professional fashion photograph, full body shot. Model: bust queen goddess, legendary full bust with perfect cinched waist, early-30s, Mexican features, warm honey-caramel skin, long dark waves with highlights floating in crystal cenote water, kohl-lined eyes, deep berry lips. Wearing: ultra-minimal turquoise micro string bikini, triangle top barely containing legendary bust, gold platform wedge sandals 4-inch heel on cenote limestone ledge, turquoise drop earrings, gold layered chains. Environment: Tulum sacred cenote, shafts of jungle light piercing crystal blue-green water from jungle opening above, ancient stone walls covered in lush vines, legendary bust partially submerged in crystal water. Lighting: shaft of jungle light from above piercing crystal water creating beam of light across legendary figure, honey-caramel skin luminous in cenote blue-green light. Style: bust queen Tulum sacred cenote editorial, legendary proportions in sacred water. Shot on Phase One XF IQ4, 8K UHD, cenote sacred grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "tulum", "cenote", "bust_queen", "turquoise"],
        "aspect_ratio": "2:3"
    },
    "beach_latina_rio": {
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass goddess, maximum sculpted curves, early-20s, Colombian features, rich warm terra-cotta skin, voluminous dark waves with copper highlights in Rio beach wind, full lips, fierce expression. Wearing: ultra-minimal red and gold Brazilian micro string bikini, gold platform wedge sandals 5-inch heel in Ipanema wet sand, gold ear drops, gold body chain at waist. Environment: Ipanema beach at golden sunset, Dois Irmãos twin mountains behind in silhouette, Rio de Janeiro skyline visible, carnival energy in air, golden wet sand mirror at feet reflecting sunset. Lighting: Rio golden sunset from behind twin mountains, warm terra-cotta skin blazing in total golden Rio sunset, wet sand mirror reflecting sunset upward from below. Style: Colombian Rio Ipanema beach glamour editorial, maximum curves commanding Rio sunset. Shot on Hasselblad X2D, 8K UHD, Rio sunset grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "rio", "ipanema", "latina", "sunset"],
        "aspect_ratio": "2:3"
    },
    "beach_vs_angel_capri": {
        "prompt": "Professional fashion photograph, full body shot. Model: VS Angel goddess, flawless perfect hourglass, long endless legs, early-20s, Italian features, sun-kissed golden Mediterranean skin, long tousled beach waves in sea breeze, expression coastal-angel. Wearing: ultra-minimal ivory crochet micro bikini top and matching micro bottom, matching ivory sarong open at hip revealing full leg, white platform stiletto wedge sandals 5-inch heel on yacht teak deck, delicate gold star ear studs, gold anklet. Environment: luxury yacht bow near Capri, iconic Faraglioni rock stacks in direct view, turquoise Tyrrhenian Sea, Capri coastline. Lighting: Mediterranean noon direct bright from above + turquoise sea reflection upward from below, golden Mediterranean skin perfect in coastal light, Faraglioni rocks as iconic frame behind perfect angel figure. Style: VS Angel Capri yacht Italian coastal editorial, perfect figure on European luxury sea. Shot on Phase One XF IQ4, 8K UHD, Capri coastal grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "capri", "yacht", "vs_angel", "ivory"],
        "aspect_ratio": "2:3"
    },
    "beach_black_glamour_bioluminescent": {
        "prompt": "Professional fashion photograph, full body shot. Model: black glamour goddess, maximum ebony hourglass, spectacular curves, mid-20s, Somali features, deepest jet-black skin, voluminous natural coils loose in midnight beach air, bold red lip only color. Wearing: ultra-minimal black micro string bikini invisible against jet skin, bioluminescent electric blue wave fire rising around jet figure from surf below, black patent platform stiletto wedge 5-inch heel in blue-fire surf, single moonstone choker glowing against jet skin. Environment: dark beach at midnight, bioluminescent waves breaking in electric blue fire at feet and around figure, sea sparkle blue carpet on wet sand, dark ocean behind, full moon silver from above. Lighting: bioluminescent wave electric blue fire from surf below + full moon silver from above, jet-black skin edge-lit by blue bioluminescent fire on every curve, moonstone choker as single warm point in electric blue scene. Style: black glamour bioluminescent midnight beach editorial, jet curves in electric ocean fire. Shot on Hasselblad X2D, 8K UHD, bioluminescent night grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "bioluminescent", "midnight", "black_glamour", "moon"],
        "aspect_ratio": "2:3"
    },
    "beach_hot_glamour_infinity_pool": {
        "prompt": "Professional fashion photograph, full body shot. Model: hot glamour goddess, dramatic perfectly cinched hourglass, sculpted curves, mid-20s, Thai features, warm honey-bronze skin, long straight glossy black hair with subtle waves, full lips. Wearing: ultra-minimal neon orange micro string bikini, triangle top and micro thong, orange chrome platform stiletto heeled sandals 5-inch heel at pool infinity edge, minimal gold body chain, gold ear studs. Environment: luxury jungle resort infinity pool, tropical jungle canopy dropping away below infinity edge creating dramatic drop, late afternoon golden light filtering through canopy. Lighting: late tropical afternoon golden filtering through jungle canopy from above + turquoise infinity pool reflection upward from below, honey-bronze skin lit from both above and below in golden-turquoise. Style: hot glamour Thai jungle infinity pool editorial, dramatic curves commanding tropical luxury. Shot on Phase One XF IQ4, 8K UHD, tropical luxury grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "infinity_pool", "jungle", "hot_glamour", "orange"],
        "aspect_ratio": "2:3"
    },
    "beach_supermodel_mykonos": {
        "prompt": "Professional fashion photograph, full body shot. Model: supermodel tall goddess, 185cm+ extreme tall frame, impossibly long legs, mid-20s, Greek features, warm olive-golden skin, tousled dark honey-blonde beach hair, sharp cheekbones, cold editorial expression. Wearing: ultra-minimal white micro string bikini, matching white micro cover-up shirt fully open, clear platform stiletto wedge mules 5-inch heel on Mykonos cobblestone, single geometric silver ear cuff, dark aviator sunglasses in hand. Environment: Mykonos iconic windmill directly behind, white cycladic architecture, bright Aegean noon sky blazing blue. Lighting: Mykonos hard Aegean noon sun from directly above, harsh bright light on olive-golden skin and white architecture creating high contrast, windmill as iconic monumental backdrop. Style: supermodel Mykonos Greek island editorial, extreme tall goddess commanding Aegean noon. Shot on Hasselblad X2D, 8K UHD, Aegean noon grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "mykonos", "windmill", "supermodel", "white"],
        "aspect_ratio": "2:3"
    },
    "beach_colombia_caribbean": {
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian body goddess, sculpted full Colombian curves, early-20s, Afro-Colombian features, warm rich brown skin, voluminous natural curls with flowers, full lips, expression Caribbean-dreaming. Wearing: ultra-minimal floral micro string bikini, Caribbean tropical colors, platform wedge sandals 4-inch heel dangling from one hand as figure reclines, gold layered necklace, tropical flower in hair. Environment: Caribbean beach hammock between two perfect palms, turquoise Caribbean water behind through palms, white sand below, dappled palm shade. Lighting: dappled warm palm shade from above filtering golden + turquoise Caribbean water reflection from behind through palm gaps, warm rich brown skin in tropical dappled golden light. Style: Afro-Colombian Caribbean hammock beach editorial, full curves in Caribbean paradise. Shot on Phase One XF IQ4, 8K UHD, Caribbean paradise grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "caribbean", "hammock", "colombia", "tropical"],
        "aspect_ratio": "2:3"
    },
    "beach_miniature_hawaii": {
        "prompt": "Professional fashion photograph, full body shot. Model: miniature goddess, ultra-petite compact perfect figure, early-20s, Japanese-Hawaiian features, warm honey skin, long dark hair soaked in waterfall spray with plumeria flower, wide doe eyes, tiny frame. Wearing: ultra-minimal pastel yellow micro string bikini, tiny triangle top and micro bottom, clear platform wedge sandals 4-inch heel on tropical rock, plumeria flower tucked in wet hair, delicate gold anklet. Environment: lush Hawaii jungle waterfall, massive tropical waterfall dramatically larger than tiny figure — scale contrast maximum, rainbow in mist above, lush green tropical vegetation towering above. Lighting: diffused soft jungle light through waterfall mist + rainbow color in mist above, honey skin warm in soft mist-filtered tropical light, waterfall massive scale creating maximum contrast with tiny perfect figure. Style: miniature Japanese-Hawaiian waterfall editorial, tiny goddess commanding massive tropical scale. Shot on Hasselblad X2D, 8K UHD, Hawaii waterfall grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "hawaii", "waterfall", "miniature", "rainbow"],
        "aspect_ratio": "2:3"
    },
    "beach_brazil_booty_golden_hour": {
        "prompt": "Professional fashion photograph, full body shot. Model: Brazil booty goddess, maximum dramatic hip-to-waist ratio, extreme full hips, early-20s, Brazilian features, rich warm terra-cotta-bronze skin, voluminous dark waves in golden beach wind, full lips. Wearing: ultra-minimal strappy gold micro string bikini, straps cutting into full dramatic hips, micro thong maximum exposure on legendary Brazilian curves, gold platform stiletto wedge sandals 5-inch heel in wet reflective sand, minimal gold ear studs. Environment: Brazilian beach at golden hour, ocean wave just retreated leaving wet sand mirror perfect, sun at direct horizon blazing, total golden atmosphere. Lighting: golden hour sun at direct horizon from exact side casting long warm shadow across wet sand and figure + wet sand mirror reflection from below, terra-cotta-bronze skin blazing in total dual golden-hour light, maximum golden saturation. Style: Brazil booty golden hour beach editorial, legendary Brazilian curves commanding golden sunset. Shot on Phase One XF IQ4, 8K UHD, golden hour grade, portrait 2:3 vertical.",
        "category": "🏖️ Beach & Resort Glamour",
        "tags": ["beach", "brazil", "golden_hour", "booty", "wet_sand"],
        "aspect_ratio": "2:3"
    },
}

# ──────────────────────────────────────────────
# HOF / SSS 판정 결과
# ──────────────────────────────────────────────

HOF_PRESETS = {
    # 🌙 Night Glamour HOF
    "night_super_glamour_penthouse",
    "night_amazon_rooftop_rain",
    "night_latina_neon_alley",
    "night_black_glamour_moonrise",
    # 👗 Slip Dress HOF
    "slip_super_glamour_marble",
    "slip_amazon_rain_window",
    "slip_latina_poolside_dawn",
    # 🐆 Animal Print HOF
    "animal_super_glamour_leopard_gown",
    "animal_amazon_cheetah_latex",
    "animal_black_glamour_panther_catsuit",
    # ⚔️ Power & Edge HOF
    "edge_super_glamour_chrome_armor",
    "edge_amazon_warrior_ruins",
    "edge_black_glamour_obsidian_gown",
    # 🏖️ Beach & Resort HOF
    "beach_amazon_bali_surf",
    "beach_latina_rio",
    "beach_black_glamour_bioluminescent",
    "beach_brazil_booty_golden_hour",
}

SSS_PRESETS = {
    # 🌙 Night Glamour SSS
    "night_bbw_jazz_club",
    "night_vs_angel_casino",
    "night_hot_glamour_club_vip",
    "night_miniature_starlight_terrace",
    # 👗 Slip Dress SSS
    "slip_bbw_champagne_bedroom",
    "slip_bust_queen_vanity",
    "slip_vs_angel_hotel_corridor",
    "slip_black_glamour_midnight_terrace",
    "slip_hot_glamour_silk_sheets",
    "slip_supermodel_airport_lounge",
    # 🐆 Animal Print SSS
    "animal_bbw_zebra_bodycon",
    "animal_bust_queen_snakeskin_dress",
    "animal_latina_tiger_mini",
    "animal_vs_angel_leopard_boudoir",
    "animal_powerlifter_croc_bodysuit",
    # ⚔️ Power & Edge SSS
    "edge_bbw_leather_commander",
    "edge_latina_moto_latex",
    "edge_vs_angel_crystal_harness",
    "edge_hot_glamour_cage_dress",
    "edge_powerlifter_titanium_suit",
    # 🏖️ Beach & Resort SSS
    "beach_super_glamour_maldives",
    "beach_bbw_santorini",
    "beach_bust_queen_tulum",
    "beach_vs_angel_capri",
    "beach_hot_glamour_infinity_pool",
    "beach_supermodel_mykonos",
    "beach_colombia_caribbean",
    "beach_miniature_hawaii",
}

# ──────────────────────────────────────────────
# PRESET_CATEGORIES 블록
# ──────────────────────────────────────────────

NEW_CATEGORIES = """
    "🌙 Night Glamour": [
        "night_super_glamour_penthouse",
        "night_bbw_jazz_club",
        "night_amazon_rooftop_rain",
        "night_latina_neon_alley",
        "night_vs_angel_casino",
        "night_black_glamour_moonrise",
        "night_hot_glamour_club_vip",
        "night_miniature_starlight_terrace",
    ],
    "👗 Slip Dress Glamour": [
        "slip_super_glamour_marble",
        "slip_bbw_champagne_bedroom",
        "slip_amazon_rain_window",
        "slip_bust_queen_vanity",
        "slip_latina_poolside_dawn",
        "slip_vs_angel_hotel_corridor",
        "slip_black_glamour_midnight_terrace",
        "slip_hot_glamour_silk_sheets",
        "slip_supermodel_airport_lounge",
    ],
    "\\U0001f406 Animal Print Glamour": [
        "animal_super_glamour_leopard_gown",
        "animal_bbw_zebra_bodycon",
        "animal_amazon_cheetah_latex",
        "animal_bust_queen_snakeskin_dress",
        "animal_latina_tiger_mini",
        "animal_vs_angel_leopard_boudoir",
        "animal_black_glamour_panther_catsuit",
        "animal_powerlifter_croc_bodysuit",
    ],
    "\\u2694\\ufe0f Power & Edge Glamour": [
        "edge_super_glamour_chrome_armor",
        "edge_bbw_leather_commander",
        "edge_amazon_warrior_ruins",
        "edge_latina_moto_latex",
        "edge_vs_angel_crystal_harness",
        "edge_black_glamour_obsidian_gown",
        "edge_hot_glamour_cage_dress",
        "edge_powerlifter_titanium_suit",
    ],
    "\\U0001f3d6\\ufe0f Beach & Resort Glamour": [
        "beach_super_glamour_maldives",
        "beach_bbw_santorini",
        "beach_amazon_bali_surf",
        "beach_bust_queen_tulum",
        "beach_latina_rio",
        "beach_vs_angel_capri",
        "beach_black_glamour_bioluminescent",
        "beach_hot_glamour_infinity_pool",
        "beach_supermodel_mykonos",
        "beach_colombia_caribbean",
        "beach_miniature_hawaii",
        "beach_brazil_booty_golden_hour",
    ],
}"""

NEW_HOF = """
    # 2026-07-14 신규 5개 카테고리 HOF 17종
    # 🌙 Night Glamour HOF
    "night_super_glamour_penthouse",
    "night_amazon_rooftop_rain",
    "night_latina_neon_alley",
    "night_black_glamour_moonrise",
    # 👗 Slip Dress HOF
    "slip_super_glamour_marble",
    "slip_amazon_rain_window",
    "slip_latina_poolside_dawn",
    # 🐆 Animal Print HOF
    "animal_super_glamour_leopard_gown",
    "animal_amazon_cheetah_latex",
    "animal_black_glamour_panther_catsuit",
    # ⚔️ Power & Edge HOF
    "edge_super_glamour_chrome_armor",
    "edge_amazon_warrior_ruins",
    "edge_black_glamour_obsidian_gown",
    # 🏖️ Beach & Resort HOF
    "beach_amazon_bali_surf",
    "beach_latina_rio",
    "beach_black_glamour_bioluminescent",
    "beach_brazil_booty_golden_hour",
"""

NEW_SSS = """
    # 2026-07-14 신규 5개 카테고리 SSS 28종
    # 🌙 Night Glamour SSS
    "night_bbw_jazz_club",
    "night_vs_angel_casino",
    "night_hot_glamour_club_vip",
    "night_miniature_starlight_terrace",
    # 👗 Slip Dress SSS
    "slip_bbw_champagne_bedroom",
    "slip_bust_queen_vanity",
    "slip_vs_angel_hotel_corridor",
    "slip_black_glamour_midnight_terrace",
    "slip_hot_glamour_silk_sheets",
    "slip_supermodel_airport_lounge",
    # 🐆 Animal Print SSS
    "animal_bbw_zebra_bodycon",
    "animal_bust_queen_snakeskin_dress",
    "animal_latina_tiger_mini",
    "animal_vs_angel_leopard_boudoir",
    "animal_powerlifter_croc_bodysuit",
    # ⚔️ Power & Edge SSS
    "edge_bbw_leather_commander",
    "edge_latina_moto_latex",
    "edge_vs_angel_crystal_harness",
    "edge_hot_glamour_cage_dress",
    "edge_powerlifter_titanium_suit",
    # 🏖️ Beach & Resort SSS
    "beach_super_glamour_maldives",
    "beach_bbw_santorini",
    "beach_bust_queen_tulum",
    "beach_vs_angel_capri",
    "beach_hot_glamour_infinity_pool",
    "beach_supermodel_mykonos",
    "beach_colombia_caribbean",
    "beach_miniature_hawaii",
"""

# ──────────────────────────────────────────────
# 실행
# ──────────────────────────────────────────────

def check_paths():
    if not os.path.exists(PRESETS_DIR):
        print(f"ERROR: {PRESETS_DIR} 폴더 없음. LumineX 루트에서 실행하세요.")
        sys.exit(1)
    if not os.path.exists(META_FILE):
        print(f"ERROR: {META_FILE} 없음.")
        sys.exit(1)
    if not os.path.exists(HOF_FILE):
        print(f"ERROR: {HOF_FILE} 없음.")
        sys.exit(1)


def generate_jsons():
    created = 0
    skipped = 0
    for key, data in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{key}.json")
        if os.path.exists(path):
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "id": key,
                "prompt": data["prompt"],
                "category": data["category"],
                "tags": data["tags"],
                "aspect_ratio": data.get("aspect_ratio", "2:3")
            }, f, ensure_ascii=False, indent=2)
        created += 1
    print(f"[JSON] ✅ 생성: {created}개 / 스킵: {skipped}개")


def patch_meta():
    with open(META_FILE, encoding="utf-8-sig") as f:
        content = f.read()

    if "Night Glamour" in content and "Slip Dress Glamour" in content:
        print("[META] 카테고리 이미 존재 — 스킵")
        return

    ANCHOR = "from core.hof_tier import HOF_TIER  # HOF 추가는 core/hof_tier.py에서"
    if ANCHOR not in content:
        print("[META] ERROR: 앵커 없음")
        sys.exit(1)

    anchor_idx = content.index(ANCHOR)
    before_anchor = content[:anchor_idx]
    last_brace_idx = before_anchor.rfind("}")

    content = content[:last_brace_idx] + NEW_CATEGORIES + "\n\n\n" + content[anchor_idx:]

    # SSS 추가
    if '"night_super_glamour_penthouse"' not in content:
        content = content.replace("SSS_TIER = {", "SSS_TIER = {" + NEW_SSS, 1)
        print("[SSS] ✅ SSS 28종 추가")

    # SS_TIER에도 추가 (SS_TIER는 SSS와 동일하게 포함)
    if '"night_super_glamour_penthouse"' not in content.split("SS_TIER")[1]:
        content = content.replace("SS_TIER = {", "SS_TIER = {" + NEW_SSS, 1)

    with open(META_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("[META] ✅ 5개 카테고리 블록 추가 완료")


def patch_hof():
    with open(HOF_FILE, encoding="utf-8") as f:
        content = f.read()

    if "night_super_glamour_penthouse" in content:
        print("[HOF] 이미 존재 — 스킵")
        return

    # HOF_TIER = { 다음에 삽입
    content = content.replace("HOF_TIER = {", "HOF_TIER = {" + NEW_HOF, 1)

    with open(HOF_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("[HOF] ✅ HOF 17종 추가 완료")


if __name__ == "__main__":
    print("=" * 55)
    print("LumineX 신규 5개 카테고리 패치 시작")
    print("총 45종 (HOF 17 + SSS 28)")
    print("=" * 55)

    check_paths()
    generate_jsons()
    patch_meta()
    patch_hof()

    print("=" * 55)
    print("✅ 모든 패치 완료!")
    print()
    print("다음 단계:")
    print("  git add core/hof_tier.py core/presets_meta.py presets/")
    print('  git commit -m "feat: 나이트/슬립드레스/애니멀/파워엣지/비치 5카테고리 45종 추가"')
    print("  git push")
    print("=" * 55)
