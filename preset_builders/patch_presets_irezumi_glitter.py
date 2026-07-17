# -*- coding: utf-8 -*-
"""
presets_meta.py 패치: 이레즈미 30종 + 바디글리터 11종
SSS/SS 티어 포함 전체 추가
"""

import ast

# ── 검증 먼저 ──────────────────────────────────────────
with open('core/presets_meta.py', 'r', encoding='utf-8-sig') as f:
    content = f.read()

try:
    ast.parse(content)
    print("presets_meta.py 문법 OK")
except SyntaxError as e:
    print(f"문법 오류: {e}")
    exit(1)

# ── 이레즈미 프리셋 블록 ───────────────────────────────
IREZUMI_BLOCK = '''
    # ── 이레즈미 전신 타투 (2026-07-17 추가) ──
    # A그룹: 용+파도
    "irezumi_dragon_wave_black_glam_void": {
        "tier": "HOF",
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — body fully covered in Japanese irezumi tattoos: massive dragon coiling up from ankles with scales rendered in obsessive detail, crashing ocean waves filling every gap between dragon coils from thigh to shoulder, tattoos as the only covering — jet black afro voluminous and commanding, expression fierce and untouchable. Wearing: tattoos only, black stiletto heels elongating inked powerful legs, black long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight, deep shadows carving hourglass definition, high gloss body oil making dragon scales and wave crests electric against deep skin, tattoo colors blazing in contrast. Style: Black goddess irezumi dragon void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian dragon grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_dragon_wave_sports_glam_onsen": {
        "tier": "HOF",
        "subject": "Japanese beauty, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, sports glamour physique — toned athletic curves, round lifted hips, flat defined abs — body fully covered in Japanese irezumi tattoos: twin dragons spiraling up both legs meeting at the spine, powerful ocean waves crashing across flat abs and chest, tattoos blanketing every inch of athletic skin — wet-slicked dark hair pulled severely back, expression commanding and sensual. Wearing: tattoos only, barefoot on wet marble, classic red long almond nails. Environment: Budapest thermal bath, marble columns, steam rising from glowing pool surface, warm amber lantern light. Lighting: volumetric steam fog warm amber, extreme wet-look thermal water streaming down dragon tattoos making colors saturated and vivid, steam swirling around athletic inked figure. Style: Japanese sports goddess irezumi thermal steam editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, thermal dragon grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog warm amber",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    "irezumi_dragon_wave_super_glam_dubai": {
        "tier": "SSS",
        "subject": "Middle Eastern beauty, mid-20s, super glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern beauty, mid-20s, super glamour physique — impossibly tiny corseted waist, extremely wide round heavy hips, maximum pinup hourglass — body fully covered in Japanese irezumi tattoos: enormous dragon wrapping entire hourglass figure — tail at ankle, body coiling around dramatic hips and cinched waist, head resting at collarbone — deep ocean waves filling every gap in rich color, tattoos mapping every dramatic curve — long jet black wavy hair cascading, expression half-lidded and devastating. Wearing: tattoos only, gold metallic stiletto heels, gold long almond nails. Environment: Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa glowing in distance. Lighting: strong rim backlight from Dubai city glow, high gloss body oil making dragon and wave tattoos gleam, gold heels catching distant city lights. Style: Dubai super glamour irezumi dragon night editorial. Shot on Sony A7R V 50mm f/1.4, 8K UHD, Dubai dragon grade, portrait 2:3 vertical.",
        "environment": "Dubai luxury penthouse rooftop",
        "lighting": "strong rim backlight from Dubai city glow",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_dragon_wave_power_fitness_strobe": {
        "tier": "HOF",
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — very muscular defined body, strong arms and legs, powerful commanding frame — body fully covered in Japanese irezumi tattoos: fierce dragon with open jaw mapped across powerful back and shoulders, ocean waves crashing between muscular arms and legs, tattoos following every muscle contour — slick-back severe hair tight and architectural, expression dominant and fierce. Wearing: tattoos only, black platform boots, black long stiletto nails. Environment: pure black void. Lighting: harsh direct strobe from above, high-contrast shadows carving muscle definition under dragon tattoos, high gloss body oil making every muscle and scale catch strobe light. Style: power fitness irezumi dragon strobe editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, strobe dragon grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "harsh direct strobe",
        "style": "Balmain power glamour",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_dragon_wave_vs_angel_santorini": {
        "tier": "HOF",
        "subject": "Mixed race exotic beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, Victoria's Secret Angel body — toned flat abs, model-perfect proportions, legs over 90cm — body fully covered in Japanese irezumi tattoos: golden dragon ascending from bare feet up impossibly long legs, ocean waves in deep indigo and teal filling the space between dragon coils, tattoos burning in Aegean sunset light — windswept dark hair streaming dramatically in sea breeze, expression goddess-like and confident. Wearing: tattoos only, gladiator sandals lacing up inked calves, gold long almond nails. Environment: Santorini cliff edge at golden hour, white architecture and blue dome church, Aegean sea glittering amber and gold. Lighting: golden hour warm backlight from Aegean sunset — dragon gold scales burning amber — tanning oil sheen on sun-kissed inked skin. Style: Santorini VS Angel irezumi dragon sunset editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Santorini dragon grade, portrait 2:3 vertical.",
        "environment": "Santorini cliff edge at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_dragon_wave_slim_runway_neon": {
        "tier": "HOF",
        "subject": "Korean runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, early 20s, slim runway physique 185cm+ — disproportionately long legs dominating silhouette, slender waist, narrow hips, towering editorial presence — body fully covered in Japanese irezumi tattoos: slender dragon winding elegantly up impossibly long legs, delicate ocean waves mapping the elongated torso, tattoos emphasizing extreme height and length — wet look severe slick-back hair, expression cold and untouchable. Wearing: tattoos only, extreme stiletto heels, black long stiletto nails. Environment: Shinjuku neon-lit rainy alley, Tokyo cyberpunk night, rain-soaked pavement reflections. Lighting: multi-colored neon edge glow — pink neon left, blue neon right — extreme wet-look rain making dragon tattoos electric on pale tall figure. Style: Korean runway irezumi dragon neon Tokyo editorial. Shot on Sony A7R V 50mm f/1.4, 8K UHD, neon dragon grade, portrait 2:3 vertical.",
        "environment": "Shinjuku neon-lit rainy alley",
        "lighting": "multi-colored neon edge glow",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K",
    },
    # B그룹: 봉황+국화
    "irezumi_phoenix_chrysanthemum_vs_angel_versailles": {
        "tier": "SSS",
        "subject": "Japanese beauty, late 20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, late 20s, Victoria's Secret Angel body — model-perfect proportions, runway-ready athletic glamour, glowing healthy skin — body fully covered in Japanese irezumi tattoos: magnificent phoenix with wings fully spread across entire back visible through frontal pose, chrysanthemum blooms in rich crimson and gold filling chest and shoulders, phoenix tail feathers cascading down long legs — elegant geisha updo with gold ornament, expression serene and powerful. Wearing: tattoos only, gold metallic stiletto heels, deep red long almond nails. Environment: Palace of Versailles golden hall, ornate chandeliers, gilded mirrors reflecting inked figure infinitely, marble floors. Lighting: dramatic chiaroscuro candlelight, Versailles gold reflections warming phoenix colors, satin skin glow. Style: Versailles VS Angel irezumi phoenix editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Versailles phoenix grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles golden hall",
        "lighting": "dramatic chiaroscuro candlelight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_phoenix_chrysanthemum_ballerina_steam": {
        "tier": "HOF",
        "subject": "Japanese beauty, early 20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, early 20s, ballerina physique — slender elongated figure, visible shoulder blade definition, graceful dancer's carriage — body fully covered in Japanese irezumi tattoos: phoenix rising from feet with wings spreading across slender back, chrysanthemums in soft pink and white blooming delicately across pale elongated torso and arms, tattoos following every graceful line — loose romantic updo with hair ornaments, expression melancholic and dreamy. Wearing: tattoos only, barefoot in steam, classic red short square nails. Environment: Budapest thermal bath, steam rising, marble columns, warm amber water reflections. Lighting: volumetric steam fog warm amber, extreme wet-look thermal mist on pale inked ballerina skin, steam swirling around elongated inked figure. Style: ballerina irezumi phoenix steam thermal editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, thermal phoenix grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog warm amber",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "Leica SL2 50mm f/1.4 Summilux, hyperrealistic photography, 8K",
    },
    "irezumi_phoenix_chrysanthemum_hot_glam_riad": {
        "tier": "HOF",
        "subject": "Middle Eastern beauty, mid-20s, hot glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern beauty, mid-20s, hot glamour physique — dramatically cinched narrow waist, explosively wide round hips, smoldering hourglass — body fully covered in Japanese irezumi tattoos: phoenix in full flight mapped across dramatic curves — wings spanning wide hips, tail feathers wrapping narrow waist, chrysanthemum gardens blooming across chest — warm olive skin making crimson and gold tattoos luminous — ornate geisha updo with gold pins, expression exotic and commanding. Wearing: tattoos only, gold metallic stiletto heels, gold long stiletto nails. Environment: Moroccan luxury riad, intricate zellige tile walls, carved plaster archways, candles and lanterns warm amber, central fountain. Lighting: Moroccan lantern warm amber from multiple positions, olive skin in amber light, phoenix crimson and gold tattoos blazing. Style: Moroccan riad hot glamour irezumi phoenix editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Moroccan phoenix grade, portrait 2:3 vertical.",
        "environment": "Moroccan luxury riad",
        "lighting": "Moroccan lantern warm amber",
        "style": "Gucci eclectic maximalism",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    "irezumi_phoenix_chrysanthemum_latina_miami": {
        "tier": "SSS",
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — extreme hourglass, explosively wide dramatic hips, impossibly tiny waist, thick powerful thighs — body fully covered in Japanese irezumi tattoos: phoenix rising dramatically up from powerful legs, wings spreading across explosive hips, chrysanthemums blooming in vivid color across bronzed torso — long dark wavy hair windswept in ocean breeze, expression Latin fire and confidence. Wearing: tattoos only, strappy high heel sandals on Miami sand, red long stiletto nails. Environment: Miami Beach at sunset, Ocean Drive, warm pink and orange sky blazing. Lighting: golden hour amber, tanning oil bronzing Latin skin. Style: Miami Latina irezumi phoenix sunset editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Miami phoenix grade, portrait 2:3 vertical.",
        "environment": "Miami Beach at sunset",
        "lighting": "golden hour warm amber",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_phoenix_chrysanthemum_nordic_aurora": {
        "tier": "SSS",
        "subject": "Scandinavian beauty, mid-20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian beauty, mid-20s, ballerina physique — slender elongated figure, pale porcelain skin — body fully covered in Japanese irezumi tattoos: phoenix rising against aurora colors — wings in deep indigo and violet matching northern lights above, chrysanthemums in icy blue and silver across pale slender torso — platinum blonde hair windswept in arctic wind, expression cold and otherworldly. Wearing: tattoos only, barefoot in arctic snow, deep blue long stiletto nails. Environment: Iceland glacier at midnight, northern lights aurora borealis dancing overhead. Lighting: aurora borealis curtain of light washing over pale inked figure. Style: Iceland aurora irezumi phoenix nordic editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora phoenix grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier, northern lights",
        "lighting": "aurora borealis curtain of light",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    "irezumi_phoenix_chrysanthemum_black_glam_desert": {
        "tier": "HOF",
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — body fully covered in Japanese irezumi tattoos: magnificent phoenix with wings fully spread across powerful back, chrysanthemum blooms in rich crimson and gold filling chest and shoulders, phoenix tail feathers cascading down thick powerful thighs — natural afro hair enormous and windswept against desert sky, expression ancient and untouchable, warrior queen energy. Wearing: tattoos only, barefoot in hot red sand, gold long stiletto nails. Environment: Namib desert red dunes at golden hour, dramatic African landscape, surreal orange sky. Lighting: golden hour warm backlight creating blazing halo around afro, strong rim backlight on deep skin making phoenix and chrysanthemum tattoos electric, tanning oil making deep skin and phoenix colors burn. Style: Black goddess irezumi phoenix desert editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Namib phoenix grade, portrait 2:3 vertical.",
        "environment": "Namib desert red dunes at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    # C그룹: 잉어+벚꽃
    "irezumi_koi_sakura_korean_void": {
        "tier": "SSS",
        "subject": "Korean beauty, mid-20s, slim runway physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, mid-20s, slim runway physique — disproportionately long legs, slender elegant frame, small delicate face — body fully covered in Japanese irezumi tattoos: crimson and gold koi fish leaping up impossibly long legs, pink cherry blossoms scattered across pale slender torso like falling snow, koi and sakura filling every inch of porcelain skin — elegant geisha updo with gold hairpin, expression cold runway steel. Wearing: tattoos only, extreme black stiletto heels, black long stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: dramatic chiaroscuro single spotlight, high gloss body oil making koi scales and cherry blossoms electric on pale porcelain skin. Style: Korean runway irezumi koi sakura void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, koi sakura void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_koi_sakura_vs_angel_kyoto_rain": {
        "tier": "HOF",
        "subject": "Japanese beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, Victoria's Secret Angel body — model-perfect proportions, legs over 90cm — body fully covered in Japanese irezumi tattoos: massive red and white koi fish leaping up from ankles, cherry blossoms falling across chest and shoulders in pink and white, rain-soaked skin making colors saturated and vivid — loose romantic updo with hair ornaments slipping in downpour, expression melancholic and breathtaking. Wearing: tattoos only, traditional wooden geta sandals in rain puddles, classic red short square nails. Environment: rain-soaked traditional Japanese street at night, Kyoto alley, paper lanterns glowing warm amber through downpour, wet cobblestones reflecting orange light. Lighting: volumetric rain fog, warm paper lantern amber, extreme wet-look rain streaming down koi and sakura tattoos. Style: Kyoto rain VS Angel irezumi koi sakura editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Kyoto koi rain grade, portrait 2:3 vertical.",
        "environment": "rain-soaked Kyoto alley at night",
        "lighting": "volumetric rain fog warm amber lantern",
        "style": "Dolce and Gabbana Italian glamour",
        "quality": "Leica SL2 50mm f/1.4 Summilux, hyperrealistic photography, 8K",
    },
    "irezumi_koi_sakura_colombian_monaco": {
        "tier": "HOF",
        "subject": "Colombian Latina beauty, early 30s, luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina beauty, early 30s, luxury glamour physique — defined waist, wide round hips, sophisticated voluptuous elegance — body fully covered in Japanese irezumi tattoos: golden koi fish leaping dramatically across voluptuous curves, cherry blossoms in pale pink and white scattered across sophisticated torso — side-swept old Hollywood hair dramatically draped, expression enigmatic and impossibly chic. Wearing: tattoos only, diamond necklace and earrings as only additions, gold metallic stiletto heels, black and gold nail art. Environment: Monaco luxury terrace at night, Mediterranean sea glittering below, superyachts in harbor, city of Monaco illuminated. Lighting: strong rim backlight halo from Monaco nightscape, diamond jewelry catching lights and sparkling, satin skin glow on koi and sakura inked curves. Style: Monaco luxury irezumi koi sakura diamond night editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Monaco koi grade, portrait 2:3 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco nightscape rim backlight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    # D그룹: 학+모란
    "irezumi_crane_peony_slim_elegance_white": {
        "tier": "SSS",
        "subject": "Korean beauty, mid-20s, slender elegant physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, mid-20s, slender elegant physique — slim narrow frame, graceful delicate figure, refined fashion presence — body fully covered in Japanese irezumi tattoos: elegant cranes in flight mapping slender arms and long neck, lush peonies in deep crimson and blush blooming across delicate torso, crane wings spanning across pale back — long straight silky black hair sleek and smooth, expression fresh and pure. Wearing: tattoos only, nude stiletto heels, nude long almond nails. Environment: pure white minimalist studio, seamless white backdrop. Lighting: soft beauty dish even flattering illumination, light natural skin glow making crane and peony tattoos delicate and precise. Style: white studio slender elegance irezumi crane peony editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, white studio crane grade, portrait 2:3 vertical.",
        "environment": "pure white minimalist studio",
        "lighting": "soft beauty dish",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_crane_peony_super_glam_versailles": {
        "tier": "HOF",
        "subject": "Eastern European bombshell, mid-20s, super glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Eastern European bombshell, mid-20s, super glamour physique — impossibly tiny waist, extremely wide round heavy hips, maximum pinup hourglass — body fully covered in Japanese irezumi tattoos: cranes soaring across dramatic wide hips with wings spread, deep crimson peonies blooming across cinched waist and full chest, golden crane feathers cascading down heavy thighs — long jet black wavy hair cascading, expression half-lidded and devastating. Wearing: tattoos only, gold metallic stiletto heels, deep red long almond nails. Environment: Palace of Versailles golden hall, ornate chandeliers, gilded mirrors reflecting curves infinitely. Lighting: Versailles candlelight chiaroscuro, deep shadows and sharp highlights on dramatic tattooed hourglass, satin skin glow, peony crimson blazing in baroque gold atmosphere. Style: Versailles super glamour irezumi crane peony editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Versailles crane grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles golden hall",
        "lighting": "Versailles candlelight chiaroscuro",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_crane_peony_southeast_asian_beach": {
        "tier": "SSS",
        "subject": "Southeast Asian beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Southeast Asian beauty, mid-20s, Victoria's Secret Angel body — model-perfect proportions, golden tan glowing skin — body fully covered in Japanese irezumi tattoos: white cranes soaring up golden tan legs, lush pink peonies blooming across glowing chest, crane feathers delicate against warm tropical skin — windswept long wavy hair sea-salted and free, expression paradise goddess alluring. Wearing: tattoos only, strappy high heel sandals, gold long almond nails. Environment: French Riviera cliff at golden hour, azure Mediterranean sea below, golden sunlight. Lighting: golden hour warm backlight, tanning oil on golden skin making white crane and pink peony tattoos vivid. Style: Riviera Southeast Asian irezumi crane peony golden editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Riviera crane grade, portrait 2:3 vertical.",
        "environment": "French Riviera cliff at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_crane_peony_mature_luxury_monaco": {
        "tier": "SSS",
        "subject": "French European beauty, early 30s, luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: French European beauty, early 30s, luxury glamour physique — defined waist, wide round hips, sophisticated mature elegance — body fully covered in Japanese irezumi tattoos: cranes in elegant flight across sophisticated curves, deep crimson peonies blooming with painterly detail across refined torso and hips — side-swept old Hollywood hair, expression sophisticated and enigmatic. Wearing: tattoos only, diamond jewelry as sole addition, gold metallic stiletto heels, black and gold nail art. Environment: Monaco luxury terrace at night, Mediterranean sea glittering below, superyachts in harbor. Lighting: Monaco nightscape rim backlight, diamond jewelry sparkling, satin skin glow. Style: Monaco mature luxury irezumi crane peony editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Monaco crane grade, portrait 2:3 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco nightscape rim backlight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Leica SL2 50mm f/1.4 Summilux, hyperrealistic photography, 8K",
    },
    # E그룹: 호랑이+대나무
    "irezumi_tiger_bamboo_sports_glam_void": {
        "tier": "HOF",
        "subject": "Korean beauty, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, mid-20s, sports glamour physique — athletic toned curves, round lifted hips, defined abs, powerful yet feminine — body fully covered in Japanese irezumi tattoos: fierce tiger prowling up athletic legs with burning amber eyes, bamboo forest rising along torso, tiger stripes flowing with muscle definition, snarling tiger face across powerful back — elegant geisha updo with gold pin, expression fierce and commanding. Wearing: tattoos only, black stiletto heels, black long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro, deep shadows carving athletic definition, high gloss body oil making tiger stripes and bamboo electric on toned skin, amber tiger eyes glowing in darkness. Style: sports glamour irezumi tiger bamboo void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, tiger void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_tiger_bamboo_vs_angel_dubai": {
        "tier": "HOF",
        "subject": "Mixed race exotic beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, Victoria's Secret Angel body — model-perfect proportions, legs over 90cm, runway-ready glamour — body fully covered in Japanese irezumi tattoos: powerful tiger ascending impossibly long legs, bamboo reaching up elongated torso, tiger tail wrapping narrow waist, fierce face emerging at shoulder — high sleek ponytail severe and polished, expression smoldering and powerful. Wearing: tattoos only, gold metallic stiletto heels, gold long stiletto nails. Environment: Dubai luxury penthouse rooftop at night, Burj Khalifa glowing in distance, city skyline electric. Lighting: strong rim backlight from Dubai city glow, high gloss body oil on VS Angel inked body gleaming in city light. Style: Dubai VS Angel irezumi tiger bamboo night editorial. Shot on Sony A7R V 50mm f/1.4, 8K UHD, Dubai tiger grade, portrait 2:3 vertical.",
        "environment": "Dubai luxury penthouse rooftop at night",
        "lighting": "strong rim backlight from Dubai city glow",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_tiger_bamboo_hot_glam_neon": {
        "tier": "SSS",
        "subject": "Japanese beauty, mid-20s, hot glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, hot glamour physique — dramatically cinched waist, explosively wide round hips, smoldering hourglass — body fully covered in Japanese irezumi tattoos: roaring tiger mapped across dramatic curves — stripes following the cinched waist and wide hips — bamboo rising along torso, tiger face fierce across chest — wet look slick-back hair severe, expression smoldering intensity. Wearing: tattoos only, black stiletto heels, red long stiletto nails. Environment: Shinjuku neon-lit rainy street, Tokyo night, rain-soaked pavement. Lighting: pink neon from left, blue neon from right, multi-colored neon edge glow slicing across tiger stripe tattoos, extreme wet-look rain on inked curves. Style: Tokyo neon hot glamour irezumi tiger editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, neon tiger grade, portrait 2:3 vertical.",
        "environment": "Shinjuku neon-lit rainy street",
        "lighting": "multi-colored neon edge glow",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K",
    },
    "irezumi_tiger_bamboo_african_desert": {
        "tier": "HOF",
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — extremely wide round hips, ultra-narrow waist, deep luminous rich skin — body fully covered in Japanese irezumi tattoos: massive tiger in full prowl mapped across powerful body — amber and black tiger stripes following dramatic curves, bamboo forest rising from powerful thighs to shoulders, tiger face fierce across upper back — natural afro enormous and windswept, expression ancient warrior power. Wearing: tattoos only, barefoot in hot red sand, gold long stiletto nails. Environment: Namib desert red dunes at golden hour, surreal orange sky, elemental African landscape. Lighting: golden hour warm backlight blazing halo around afro, strong rim light making deep skin and amber tiger stripes electric, tanning oil making tiger and bamboo burn in desert light. Style: Namib Black goddess irezumi tiger bamboo desert editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Namib tiger grade, portrait 2:3 vertical.",
        "environment": "Namib desert red dunes at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    "irezumi_tiger_bamboo_brazilian_pool": {
        "tier": "SSS",
        "subject": "Brazilian goddess, mid-20s, Brazilian carnival physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Brazilian goddess, mid-20s, Brazilian carnival physique — massive round hips dominating silhouette, extremely wide hips, powerfully thick thighs, bronzed tropical skin — body fully covered in Japanese irezumi tattoos: powerful tiger mapped across massive curves — stripes following enormous round hips and thick powerful thighs, bamboo rising up bronzed torso, tiger roaring across powerful chest — big dark voluminous hair wild and alive, expression carnival queen fierce. Wearing: tattoos only, barefoot on wet pool edge, gold long almond nails. Environment: luxury infinity pool edge, tropical resort at golden hour, turquoise water. Lighting: golden hour warm backlight, extreme wet-look pool water streaming down tiger tattoos, tanning oil making tiger stripes vivid on tropical skin. Style: tropical Brazilian irezumi tiger bamboo pool editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, tropical tiger grade, portrait 2:3 vertical.",
        "environment": "luxury infinity pool edge",
        "lighting": "golden hour warm backlight",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K",
    },
'''

GLITTER_BLOCK = '''
    # ── 바디글리터 (2026-07-17 추가) ──
    "bodyglitter_silver_neon_cyberpunk": {
        "tier": "HOF",
        "subject": "Mixed race exotic runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic runway goddess, early 20s, slim runway physique 185cm+ — disproportionately long legs, slender waist, elongated graceful frame — entire body covered in dense silver holographic glitter from neck to toe, skin transformed into galaxy surface, silver and holographic glitter densely packed from collarbone to toe, body catching neon light from every microscopic facet — wet look slicked back hair severe, expression cold and cybernetic. Wearing: dense silver holographic glitter covering entire body as sole garment — glitter so densely applied it creates second skin effect, iridescent color shifts from silver to pink to blue — crystal PVC platform boots, holographic long stiletto nails. Environment: cyberpunk neon city street at night, rain-soaked alley, neon signs reflecting in wet pavement. Lighting: multi-colored neon edge glow — pink neon left, blue neon right — holographic glitter refracting neon into thousands of rainbow points across entire body, rain drops on glitter surface catching additional light. Style: holographic glitter cyberpunk goddess editorial. Shot on Sony A7R V 50mm f/1.4, 8K UHD, holographic glitter cyberpunk grade, portrait 2:3 vertical.",
        "environment": "cyberpunk neon city street at night",
        "lighting": "multi-colored neon edge glow",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_gold_void_black_glam": {
        "tier": "HOF",
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — entire body covered in dense gold holographic glitter from neck to toe, deep skin beneath gold glitter creating warm amber bronze tones, glitter so densely packed skin becomes living gold sculpture, natural afro hair voluminous and commanding with gold glitter dust at edges, expression fierce and untouchable. Wearing: dense gold holographic glitter covering entire body as sole garment, gold glitter second skin from collarbone to ankle, black stiletto heels, black long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight, gold glitter blazing in single beam against total darkness, every glitter facet catching light creating thousands of gold sparks across deep skin, deep shadows carving hourglass into dramatic relief. Style: gold glitter Black goddess void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, gold glitter void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_rose_gold_versailles": {
        "tier": "HOF",
        "subject": "Eastern European bombshell, mid-20s, super glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Eastern European bombshell, mid-20s, super glamour physique — impossibly tiny corseted waist, extremely wide round heavy hips, maximum pinup hourglass — entire body covered in dense rose gold iridescent glitter from neck to toe, porcelain pale skin beneath rose gold glitter creating warm peach tones, glitter shifting from pink to gold to copper as body moves, long jet black wavy hair cascading dramatically, expression half-lidded and devastating. Wearing: dense rose gold holographic glitter covering entire body as sole garment, glitter second skin maximum coverage, gold metallic stiletto heels, deep red long almond nails. Environment: Palace of Versailles golden hall, ornate chandeliers, gilded mirrors reflecting glitter infinitely, marble floors. Lighting: Versailles chandelier light catching every rose gold glitter facet — thousands of pink and gold light refractions dancing — gilded mirrors multiplying glitter sparkle infinitely. Style: rose gold glitter Versailles bombshell editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, rose gold glitter Versailles grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles golden hall",
        "lighting": "Versailles chandelier light",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_blue_holographic_pool": {
        "tier": "HOF",
        "subject": "Mixed race exotic beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, Victoria's Secret Angel body — toned flat abs, model-perfect proportions, legs over 90cm — entire body covered in dense blue holographic glitter from neck to toe, golden tan skin beneath blue glitter creating electric teal tones, glitter shifting from deep blue to aqua to violet as light catches, windswept long wavy dark hair, expression goddess-like and confident. Wearing: dense blue holographic glitter covering entire body as sole garment, glitter so packed it creates iridescent second skin, barefoot on wet pool edge, nude long almond nails dusted in matching blue glitter. Environment: luxury infinity pool edge at golden hour, turquoise water below, tropical resort, palm trees. Lighting: golden hour warm backlight from horizon, pool water reflections casting aqua light upward on glitter-covered body, blue holographic glitter refracting both golden and aqua light simultaneously. Style: blue holographic glitter infinity pool VS Angel editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, blue glitter pool grade, portrait 2:3 vertical.",
        "environment": "luxury infinity pool edge at golden hour",
        "lighting": "golden hour backlight with pool water reflections",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_silver_onsen_steam": {
        "tier": "HOF",
        "subject": "Japanese beauty, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, sports glamour physique — toned athletic curves, round lifted hips, flat defined abs — entire body covered in dense silver platinum glitter from neck to toe, warm ivory skin beneath silver glitter creating pearl luminous tones, steam making glitter glisten and sparkle with every breath, wet look slicked back dark hair severe and sleek, expression commanding and sensual. Wearing: dense silver platinum holographic glitter covering entire body as sole garment, glitter second skin steaming and glistening, barefoot on wet marble, classic red long almond nails dusted in silver glitter. Environment: Budapest thermal bath, marble columns, steam rising from glowing pool surface, warm amber lantern light reflecting in water. Lighting: volumetric steam fog warm amber, steam catching silver glitter and making it glow from within, amber lantern light turning silver glitter warm gold at edges, extreme wet-look steam condensation on glitter surface. Style: silver glitter thermal steam Japanese goddess editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver glitter onsen grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog warm amber",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    "bodyglitter_rainbow_aurora_nordic": {
        "tier": "HOF",
        "subject": "Scandinavian beauty, mid-20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian beauty, mid-20s, ballerina physique — slender elongated figure, graceful elegant posture, pale porcelain skin — entire body covered in dense rainbow holographic glitter from neck to toe, pale skin beneath rainbow glitter creating ethereal iridescent tones, glitter shifting through every color of aurora spectrum — green violet pink blue — matching the sky above, platinum blonde windswept hair with rainbow glitter dust, expression cold and otherworldly. Wearing: dense rainbow holographic glitter covering entire body as sole garment, glitter matching aurora colors above, barefoot in arctic snow, deep blue long stiletto nails dusted in matching glitter. Environment: Iceland glacier at midnight, northern lights aurora borealis dancing overhead in green and violet ribbons, ancient ice formations, mystical arctic landscape. Lighting: aurora borealis curtain of light washing over glitter-covered pale figure — green and violet aurora light refracting through rainbow glitter creating supernatural color explosion — glitter and aurora colors perfectly synchronized. Style: rainbow glitter aurora Nordic goddess editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, rainbow glitter aurora grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier, northern lights aurora",
        "lighting": "aurora borealis curtain of light",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
    "bodyglitter_emerald_dubai_rooftop": {
        "tier": "HOF",
        "subject": "Middle Eastern goddess, mid-20s, hot glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern goddess, mid-20s, hot glamour physique — dramatically cinched narrow waist, explosively wide round hips, smoldering hourglass — entire body covered in dense emerald green holographic glitter from neck to toe, warm olive skin beneath emerald glitter creating rich jewel-tone depth, glitter shifting from deep forest green to electric lime to gold as light catches, high sleek ponytail severe and polished with emerald glitter dust, expression smoldering and powerful. Wearing: dense emerald holographic glitter covering entire body as sole garment, glitter second skin maximum coverage, gold metallic stiletto heels, gold long stiletto nails. Environment: Dubai luxury penthouse rooftop at night, city skyline blazing below, Burj Khalifa glowing in distance. Lighting: strong rim backlight from Dubai city glow, emerald glitter refracting gold and amber city lights creating electric green-gold color explosion across olive skin. Style: emerald glitter Dubai rooftop goddess editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, emerald glitter Dubai grade, portrait 2:3 vertical.",
        "environment": "Dubai luxury penthouse rooftop at night",
        "lighting": "strong rim backlight from Dubai city glow",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_copper_santorini_sunset": {
        "tier": "HOF",
        "subject": "Mixed race exotic beauty, mid-20s, VS Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, VS Angel body — toned flat abs, model-perfect proportions, legs over 90cm — entire body covered in dense copper bronze holographic glitter from neck to toe, sun-kissed golden skin beneath copper glitter creating warm molten metal tones, glitter shifting from deep copper to bright bronze to warm gold in sunset light, windswept long dark wavy hair catching sunset, expression goddess-like and confident. Wearing: dense copper holographic glitter covering entire body as sole garment, glitter burning like liquid sunset metal, gladiator sandals lacing up glitter-dusted calves, gold long almond nails. Environment: Santorini cliff edge at golden hour, white architecture and iconic blue dome church behind, Aegean sea glittering amber below. Lighting: golden hour warm backlight from setting Aegean sun — copper glitter igniting into liquid fire in sunset — every glitter facet burning amber and gold, windswept hair backlit and glowing. Style: copper glitter Santorini sunset goddess editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, copper glitter Santorini grade, portrait 2:3 vertical.",
        "environment": "Santorini cliff edge at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_purple_monaco_night": {
        "tier": "HOF",
        "subject": "Eastern European bombshell, mid-20s, super glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Eastern European bombshell, mid-20s, super glamour physique — impossibly tiny corseted waist, extremely wide round heavy hips, maximum pinup hourglass — entire body covered in dense deep violet purple holographic glitter from neck to toe, porcelain pale skin beneath purple glitter creating ethereal amethyst tones, glitter shifting from deep violet to electric purple to pink as light catches, long jet black wavy hair cascading dramatically, expression half-lidded and devastating. Wearing: dense purple holographic glitter covering entire body as sole garment, glitter creating amethyst goddess effect, gold metallic stiletto heels, deep red long almond nails. Environment: Monaco luxury terrace at night, Mediterranean sea glittering below, superyachts illuminated in harbor, Monaco city lights purple and gold in distance. Lighting: strong rim backlight from Monaco nightscape, purple holographic glitter refracting city lights into violet and gold explosions across dramatic hourglass curves. Style: purple glitter Monaco night bombshell editorial. Shot on Sony A7R V 50mm f/1.4, 8K UHD, purple glitter Monaco grade, portrait 2:3 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco nightscape rim backlight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_red_void_colombian": {
        "tier": "HOF",
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — extreme hourglass, explosively wide dramatic round hips, impossibly tiny waist, thick powerful thighs — entire body covered in dense crimson red holographic glitter from neck to toe, bronzed Latin skin beneath red glitter creating smoldering fire tones, glitter shifting from deep blood red to electric crimson to burning orange as light catches, long dark wavy hair wild and dramatic, expression Latin fire and fierce dominance. Wearing: dense crimson red holographic glitter covering entire body as sole garment, red glitter on dramatic hourglass creating maximum impact, extreme black stiletto heels, red long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight from above, crimson red glitter blazing in single beam against total darkness — body like living flame against black void — deep shadows carving extreme hourglass. Style: crimson glitter Colombian fire goddess void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, red glitter void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K",
    },
    "bodyglitter_ice_blue_void_ballerina": {
        "tier": "HOF",
        "subject": "Korean beauty, early 20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, early 20s, ballerina physique — slender elongated figure, graceful elegant posture, visible shoulder blade definition, dancer's poised carriage — entire body covered in dense ice blue and white holographic glitter from neck to toe, porcelain pale skin beneath ice glitter creating ethereal frozen goddess tones, glitter shifting from icy white to electric blue to pale violet, elegant updo with gold hairpin dusted in matching ice glitter, expression serene and ethereal. Wearing: dense ice blue holographic glitter covering entire body as sole garment, glitter creating frozen crystal goddess effect on slender ballerina frame, extreme nude stiletto heels elongating legs, nude long almond nails dusted in ice glitter. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: soft beauty dish even flattering illumination from front, cool blue edge light from sides — ice glitter refracting into white and blue crystal explosions across slender figure — pale skin and ice glitter creating self-luminous ethereal glow against darkness. Style: ice blue glitter Korean ballerina void editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, ice glitter void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "soft beauty dish with cool blue edge light",
        "style": "Chanel classic luxury elegance",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K",
    },
'''

# 앵커 찾아서 삽입
ANCHOR = '# 2026-07-16'
if ANCHOR not in content:
    # 앵커가 없으면 파일 끝의 } 앞에 삽입
    last_brace = content.rfind('\n}')
    if last_brace == -1:
        print("삽입 위치를 찾을 수 없습니다.")
        exit(1)
    new_content = (
        content[:last_brace] +
        IREZUMI_BLOCK +
        GLITTER_BLOCK +
        content[last_brace:]
    )
else:
    new_content = content.replace(
        ANCHOR,
        IREZUMI_BLOCK + GLITTER_BLOCK + '\n    ' + ANCHOR
    )

with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

# 검증
try:
    ast.parse(new_content)
    print("패치 완료 - 문법 OK")
    print("추가된 카테고리:")
    print("  - 이레즈미 용+파도 6종")
    print("  - 이레즈미 봉황+국화 6종")
    print("  - 이레즈미 잉어+벚꽃 3종 (생성된 것만)")
    print("  - 이레즈미 학+모란 4종")
    print("  - 이레즈미 호랑이+대나무 5종")
    print("  - 바디글리터 11종")
except SyntaxError as e:
    print(f"문법 오류 발생: {e}")
    print("백업에서 복원하세요.")
