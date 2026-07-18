# -*- coding: utf-8 -*-
"""
F. 뱀+연꽃 (10종) + G. 파도+후지산 (8종) 패치 스크립트
- presets/ JSON 18개 생성
- core/presets_meta.py 에 카테고리 블록 추가
- core/hof_tier.py 에 HOF 키 추가
"""

import os, json, ast, re

BASE = r"C:\Dev\LumineX"
PRESETS_DIR = os.path.join(BASE, "presets")
META_PATH   = os.path.join(BASE, "core", "presets_meta.py")
HOF_PATH    = os.path.join(BASE, "core", "hof_tier.py")

# ── 1. JSON 데이터 ───────────────────────────────────────────────────────────

PRESETS = {
    # ── F. 뱀+연꽃 ──────────────────────────────────────────────────────────
    "irezumi_snake_lotus_black_glam_void": {
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — body fully covered in Japanese irezumi tattoos: massive coiling serpent wrapping entire body from ankles to neck with scales rendered in obsessive detail, lotus flowers blooming between snake coils filling every gap from thigh to shoulder, tattoos as the only covering — jet black afro voluminous and commanding, expression fierce and untouchable. Wearing: tattoos only, black stiletto heels elongating inked powerful legs, black long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight, deep shadows carving hourglass definition, high gloss body oil making snake scales and lotus petals electric against deep skin. Style: Black goddess irezumi snake void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian snake grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Black goddess irezumi snake void editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "irezumi_snake_lotus_vs_angel_bali": {
        "subject": "Southeast Asian beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Southeast Asian beauty, mid-20s, Victoria's Secret Angel body — slender yet curved, warm golden skin, graceful posture — body fully covered in Japanese irezumi tattoos: massive coiling serpent wrapping entire body from ankles to neck, lotus flowers in full bloom filling every gap between snake coils, tattoo ink in deep black with subtle jade green highlights — long dark hair adorned with tropical flowers, expression serene and divine. Wearing: tattoos only, barefoot with jade toe nails, long jade almond nails. Environment: Bali ancient temple at golden hour, stone carvings, tropical foliage, incense smoke. Lighting: golden hour dappled light through temple canopy, tattoo ink catching warm amber light. Style: Valentino exotic editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, jade snake temple grade, portrait 2:3 vertical.",
        "environment": "Bali ancient temple at golden hour",
        "lighting": "golden hour dappled light through temple canopy",
        "style": "Valentino exotic editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "irezumi_snake_lotus_colombian_rio": {
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — impossibly curvaceous, powerfully round hips, sculpted waist, warm caramel skin — body fully covered in Japanese irezumi tattoos: massive coiling serpent wrapping entire body from ankles to neck with scales in obsessive detail, vibrant lotus flowers blooming between snake coils, tattoo ink in deep black with crimson red accent highlights — elaborate feathered headpiece, expression joyful and magnetic. Wearing: tattoos only, gold platform heels, long crimson stiletto nails. Environment: Rio de Janeiro carnival parade at night, colorful floats, confetti explosion. Lighting: carnival stage spotlights warm gold, tattoo ink blazing in carnival light. Style: bold carnival luxury editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, snake carnival grade, portrait 2:3 vertical.",
        "environment": "Rio de Janeiro carnival parade at night",
        "lighting": "carnival stage spotlights warm gold",
        "style": "bold carnival luxury editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },
    "irezumi_snake_lotus_ballerina_paris": {
        "subject": "Korean beauty, early 20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, early 20s, ballerina physique — slender elongated figure, graceful elegant posture, porcelain pale skin — body fully covered in Japanese irezumi tattoos: elegant serpent coiling from ankles upward with refined scale detail, lotus flowers in delicate bloom filling every gap, tattoo ink in deep black with soft purple accent highlights complementing pale skin — elegant ballet chignon with pearl hairpin, expression serene and ethereal. Wearing: tattoos only, rose gold satin pointe shoes, long pale pink almond nails. Environment: Paris rooftop at dusk, Eiffel Tower glittering in distance, warm city glow. Lighting: Paris golden hour warm backlight, tattoo ink catching soft amber light against pale skin. Style: Chanel classic luxury elegance. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, snake ballerina paris grade, portrait 2:3 vertical.",
        "environment": "Paris rooftop at dusk",
        "lighting": "Paris golden hour warm backlight",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "irezumi_snake_lotus_fitness_strobe": {
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — powerful muscular definition, sculpted abs, strong athletic shoulders — body fully covered in Japanese irezumi tattoos: massive coiling serpent wrapping entire body with scales amplifying muscular definition, lotus flowers filling every gap between snake coils, tattoo ink in deep black with electric blue accent highlights — hair slicked back, expression fierce and powerful. Wearing: tattoos only, black stiletto heels, long black stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: harsh direct strobe, tattoo ink exploding against muscular definition, deep shadows carving physique against void. Style: Balmain power glamour. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, snake fitness void grade, portrait 2:3 vertical.",
        "environment": "pure black void strobe",
        "lighting": "harsh direct strobe",
        "style": "Balmain power glamour",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD"
    },
    "irezumi_snake_lotus_runway_tokyo": {
        "subject": "Korean runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, early 20s, slim runway physique 185cm+ — impossibly tall and lean, sharp angular bone structure, ethereal pale skin — body fully covered in Japanese irezumi tattoos: elegant serpent coiling from ankles to neck with precise scale detail, lotus flowers filling every gap, tattoo ink in deep black with electric neon purple accent highlights — sleek dark hair in architectural updo, expression otherworldly and commanding. Wearing: tattoos only, transparent platform heels, long electric purple stiletto nails. Environment: Tokyo Shibuya crossing at night, neon reflections on wet pavement. Lighting: multi-colored neon edge glow, tattoo ink refracting neon colors across pale skin. Style: Balenciaga avant-garde futuristic editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, snake runway tokyo grade, portrait 2:3 vertical.",
        "environment": "Tokyo Shibuya crossing at night",
        "lighting": "multi-colored neon edge glow",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },
    "irezumi_snake_lotus_milf_monaco": {
        "subject": "European beauty, early 30s, MILF glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European beauty, early 30s, MILF glamour physique — mature voluptuous curves, confident presence, luminous fair skin — body fully covered in Japanese irezumi tattoos: mature coiling serpent wrapping entire body with obsessive scale detail, lotus flowers in full bloom filling every gap, tattoo ink in deep black with gold accent highlights complementing mature elegance — sleek auburn hair in elegant updo, expression confident and seductive. Wearing: tattoos only, gold stiletto heels, long gold almond nails. Environment: Monaco luxury terrace at night, Mediterranean lights, yacht harbor. Lighting: Monaco nightscape warm rim backlight, tattoo ink catching warm gold light against fair skin. Style: Valentino red carpet luxury editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, snake milf monaco grade, portrait 2:3 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco nightscape warm rim backlight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "irezumi_snake_lotus_mature_onsen": {
        "subject": "Japanese beauty, early 30s, mature luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, early 30s, mature luxury glamour physique — graceful sophisticated curves, refined elegance, luminous warm skin — body fully covered in Japanese irezumi tattoos: elegant coiling serpent with refined scale detail wrapping entire body, lotus flowers in serene bloom filling every gap, tattoo ink in deep black with warm amber accent highlights — sleek dark hair pinned up with gold kanzashi, expression serene and commanding. Wearing: tattoos only, barefoot with gold toe rings, long gold almond nails. Environment: Budapest thermal bath, mineral waters, classical columns, steam. Lighting: volumetric steam fog warm amber, tattoo ink glowing through steam against warm skin. Style: Harper's Bazaar sensual fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, snake onsen mature grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog warm amber",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "irezumi_snake_lotus_sports_cape_town": {
        "subject": "Black African goddess, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, sports glamour physique — athletic powerful build, sculpted definition, deep luminous rich skin — body fully covered in Japanese irezumi tattoos: powerful coiling serpent wrapping entire body with scales amplifying athletic definition, lotus flowers filling every gap between snake coils, tattoo ink in deep black with cobalt blue accent highlights creating electric contrast against deep skin — natural afro with cobalt accessories, expression powerful and magnetic. Wearing: tattoos only, cobalt blue stiletto heels, long cobalt stiletto nails. Environment: Cape Town clifftop at sunset, Atlantic Ocean, Table Mountain. Lighting: dramatic sunset warm orange backlight, tattoo ink blazing against deep skin and sunset sky. Style: Vogue Italia high-fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, snake cape town grade, portrait 2:3 vertical.",
        "environment": "Cape Town clifftop at sunset",
        "lighting": "dramatic sunset warm orange backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "irezumi_snake_lotus_vs_angel_aurora": {
        "subject": "Scandinavian beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian beauty, mid-20s, Victoria's Secret Angel body — slender yet curved, ethereal fair skin, luminous Nordic presence — body fully covered in Japanese irezumi tattoos: elegant coiling serpent wrapping entire body with precise scale detail, lotus flowers in ethereal bloom filling every gap, tattoo ink in deep black with electric violet accent highlights creating extraordinary contrast against fair skin — platinum blonde hair flowing freely, expression ethereal and otherworldly. Wearing: tattoos only, nude stiletto heels, long violet almond nails. Environment: Iceland glacier, northern lights aurora, vast dark sky. Lighting: aurora borealis purple and green curtain of light, tattoo ink catching aurora colors against fair skin. Style: Alexander McQueen dramatic fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, snake aurora nordic grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier, northern lights aurora",
        "lighting": "aurora borealis purple and green curtain of light",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },

    # ── G. 파도+후지산 ─────────────────────────────────────────────────────────
    "irezumi_wave_fuji_black_glam_void": {
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — body fully covered in Japanese irezumi tattoos: massive crashing Great Wave filling entire torso and arms with obsessive foam detail, Mount Fuji rising majestically on the chest between wave crests, wave patterns coiling down both legs to ankles — jet black afro voluminous and commanding, expression fierce and untouchable. Barefoot, long black stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight, deep shadows carving hourglass definition, high gloss body oil making wave foam and Fuji silhouette electric against deep skin. Style: Black goddess irezumi wave void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian wave grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Black goddess irezumi wave void editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "irezumi_wave_fuji_vs_angel_santorini": {
        "subject": "European beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: European beauty, mid-20s, Victoria's Secret Angel body — slender yet curved, luminous fair skin, graceful posture — body fully covered in Japanese irezumi tattoos: dramatic crashing Great Wave sweeping entire body from ankles to shoulders with obsessive foam and water detail, Mount Fuji's snow-capped peak rising on upper chest, deep indigo blue wave ink creating extraordinary contrast against fair skin — long dark hair flowing freely with white floral pins, expression serene and divine. Barefoot, long deep indigo almond nails. Environment: Santorini whitewashed terrace at golden hour, blue domes, Aegean Sea panorama, warm amber light. Lighting: golden hour warm backlight, indigo wave ink catching Mediterranean light against fair skin. Style: Valentino Mediterranean luxury editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, indigo wave santorini grade, portrait 2:3 vertical.",
        "environment": "Santorini whitewashed terrace at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Valentino Mediterranean luxury editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "irezumi_wave_fuji_runway_neon": {
        "subject": "Korean runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, early 20s, slim runway physique 185cm+ — impossibly tall and lean, sharp angular bone structure, ethereal pale skin — body fully covered in Japanese irezumi tattoos: explosive Great Wave crashing across entire body with electric cyan and deep black ink, Mount Fuji silhouette on chest glowing with neon edge, wave patterns spiraling down both legs — sleek dark hair in razor-sharp architectural updo, expression cold and otherworldly. Barefoot, long electric cyan stiletto nails. Environment: Tokyo Shibuya crossing at night in rain, neon reflections on wet pavement, glowing signs. Lighting: multi-colored neon cyan and magenta edge glow, wave ink refracting neon colors across pale skin, wet pavement reflections doubling the tattoo. Style: Balenciaga avant-garde futuristic editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, cyan wave neon grade, portrait 2:3 vertical.",
        "environment": "Tokyo Shibuya crossing at night in rain",
        "lighting": "multi-colored neon cyan and magenta edge glow",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },
    "irezumi_wave_fuji_sports_onsen": {
        "subject": "Japanese beauty, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, sports glamour physique — athletic powerful build, sculpted definition, warm luminous skin — body fully covered in Japanese irezumi tattoos: powerful Great Wave surging across entire body amplifying athletic muscle definition, Mount Fuji rising serenely on chest above the wave chaos, deep black ink with warm amber highlight accents — sleek dark hair pinned up, expression powerful and serene. Barefoot with gold toe rings, long deep teal almond nails. Environment: Budapest thermal bath, mineral steam rising, classical stone columns, candlelight. Lighting: volumetric steam fog warm amber, tattoo ink glowing through steam, candlelight catching wave foam detail. Style: Harper's Bazaar athletic sensual editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, wave onsen sports grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog warm amber",
        "style": "Harper's Bazaar athletic sensual editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "irezumi_wave_fuji_colombian_versailles": {
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — impossibly curvaceous, powerfully round hips, sculpted waist, warm caramel skin — body fully covered in Japanese irezumi tattoos: grand sweeping Great Wave engulfing entire body with rich deep blue and gold accent ink, Mount Fuji crowned in gold on upper chest, wave patterns wrapping around powerful hips and thighs with maximum density — elaborate gold hair updo with ornate pins, expression regal and magnetic. Gold stiletto heels, long gold stiletto nails. Environment: Palace of Versailles Hall of Mirrors, golden chandeliers, baroque grandeur. Lighting: warm golden chandelier light, gold accent tattoo ink blazing against caramel skin in Versailles grandeur. Style: Versace baroque luxury editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, gold wave versailles grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "warm golden chandelier light",
        "style": "Versace baroque luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "irezumi_wave_fuji_fitness_strobe": {
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — powerful muscular definition, sculpted abs, strong athletic shoulders, fair skin — body fully covered in Japanese irezumi tattoos: explosive Great Wave crashing across muscular body with wave foam following every muscle contour, Mount Fuji silhouette on chest framed by wave crests, deep black ink with electric white highlight accents — hair slicked back tight, expression fierce and powerful. Black stiletto heels, long black stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: harsh direct strobe flash, wave ink exploding against muscular definition, deep shadows carving physique, foam highlights blazing white against dark ink. Style: Balmain power glamour editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, wave fitness strobe grade, portrait 2:3 vertical.",
        "environment": "pure black void strobe",
        "lighting": "harsh direct strobe flash",
        "style": "Balmain power glamour editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD"
    },
    "irezumi_wave_fuji_mature_kyoto": {
        "subject": "Japanese beauty, early 30s, mature luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, early 30s, mature luxury glamour physique — graceful sophisticated curves, refined elegance, luminous warm skin — body fully covered in Japanese irezumi tattoos: serene undulating Great Wave flowing across entire body with refined detail, Mount Fuji standing tall and majestic on chest, deep black ink with soft silver-grey accent highlights evoking mist and rain — sleek dark hair pinned up with silver kanzashi ornaments, expression serene and commanding. Barefoot with silver toe rings, long silver almond nails. Environment: Kyoto bamboo path in rain, soft grey light, mist, ancient stone lanterns. Lighting: diffused Kyoto rain light, silver accent tattoo ink catching misty grey tones, soft shadows. Style: Vogue Japan refined elegance editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver wave kyoto grade, portrait 2:3 vertical.",
        "environment": "Kyoto bamboo path in rain",
        "lighting": "diffused Kyoto rain light",
        "style": "Vogue Japan refined elegance editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "irezumi_wave_fuji_ballerina_aurora": {
        "subject": "European ballerina, early 20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European ballerina, early 20s, ballerina physique — slender elongated figure, graceful elegant posture, porcelain pale skin — body fully covered in Japanese irezumi tattoos: elegant sweeping Great Wave coiling upward from feet through torso in graceful arcs, Mount Fuji on chest with aurora-colored ink highlights of violet and teal, wave patterns flowing down both legs to pointe shoe ribbons — ballet chignon with silver hairpin, expression ethereal and otherworldly. Rose gold satin pointe shoes, long violet almond nails. Environment: Iceland glacier field, northern lights aurora sweeping purple and green across vast dark sky. Lighting: aurora borealis violet and teal curtain of light bathing pale skin, wave ink catching aurora colors, glacial blue ambient. Style: Alexander McQueen dramatic romantic editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora wave ballerina grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier field, northern lights aurora",
        "lighting": "aurora borealis violet and teal curtain of light",
        "style": "Alexander McQueen dramatic romantic editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
}

# ── HOF / SS 분류 ─────────────────────────────────────────────────────────────

HOF_KEYS = {
    "irezumi_snake_lotus_black_glam_void",
    "irezumi_snake_lotus_ballerina_paris",
    "irezumi_snake_lotus_runway_tokyo",
    "irezumi_snake_lotus_vs_angel_aurora",
    "irezumi_wave_fuji_black_glam_void",
    "irezumi_wave_fuji_vs_angel_santorini",
    "irezumi_wave_fuji_runway_neon",
    "irezumi_wave_fuji_colombian_versailles",
    "irezumi_wave_fuji_fitness_strobe",
    "irezumi_wave_fuji_ballerina_aurora",
}

SS_KEYS = {
    "irezumi_snake_lotus_vs_angel_bali",
    "irezumi_snake_lotus_colombian_rio",
    "irezumi_snake_lotus_sports_cape_town",
    "irezumi_wave_fuji_sports_onsen",
}

# 보류(재생성 필요) — 등록은 하되 HOF/SS 제외
# irezumi_snake_lotus_fitness_strobe
# irezumi_snake_lotus_milf_monaco
# irezumi_snake_lotus_mature_onsen
# irezumi_wave_fuji_mature_kyoto

# ── 2. presets_meta.py 삽입 블록 ─────────────────────────────────────────────

SNAKE_LOTUS_KEYS = [
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

WAVE_FUJI_KEYS = [
    "irezumi_wave_fuji_black_glam_void",
    "irezumi_wave_fuji_vs_angel_santorini",
    "irezumi_wave_fuji_runway_neon",
    "irezumi_wave_fuji_sports_onsen",
    "irezumi_wave_fuji_colombian_versailles",
    "irezumi_wave_fuji_fitness_strobe",
    "irezumi_wave_fuji_mature_kyoto",
    "irezumi_wave_fuji_ballerina_aurora",
]

META_BLOCK = '''
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
'''

# ── 3. 실행 ───────────────────────────────────────────────────────────────────

def step1_create_jsons():
    print("=== Step 1: JSON 파일 생성 ===")
    created = 0
    for key, data in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{key}.json")
        if os.path.exists(path):
            print(f"  SKIP (exists): {key}.json")
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  CREATED: {key}.json")
        created += 1
    print(f"  총 {created}개 생성 완료\n")


def step2_patch_meta():
    print("=== Step 2: presets_meta.py 패치 ===")
    with open(META_PATH, "r", encoding="utf-8-sig") as f:
        content = f.read()

    if "PRESETS_IREZUMI_SNAKE_LOTUS" in content:
        print("  이미 패치됨 — SKIP\n")
        return

    # 파일 끝에 추가
    with open(META_PATH, "a", encoding="utf-8") as f:
        f.write("\n" + META_BLOCK)
    print("  PRESETS_IREZUMI_SNAKE_LOTUS + PRESETS_IREZUMI_WAVE_FUJI 추가 완료\n")


def step3_patch_hof():
    print("=== Step 3: hof_tier.py 패치 ===")
    with open(HOF_PATH, "r", encoding="utf-8-sig") as f:
        content = f.read()

    new_keys = [k for k in HOF_KEYS if f'"{k}"' not in content]
    if not new_keys:
        print("  이미 모든 HOF 키 존재 — SKIP\n")
        return

    insert_block = "\n    # 2026-07-18 이레즈미 F/G HOF\n"
    for k in sorted(new_keys):
        insert_block += f'    "{k}",\n'

    # HOF_TIER = { 다음 줄에 삽입
    new_content = content.replace("HOF_TIER = {", "HOF_TIER = {" + insert_block, 1)

    with open(HOF_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  {len(new_keys)}개 HOF 키 추가 완료\n")


def step4_validate():
    print("=== Step 4: 문법 검증 ===")
    for path, name in [(META_PATH, "presets_meta.py"), (HOF_PATH, "hof_tier.py")]:
        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                src = f.read()
            ast.parse(src)
            print(f"  {name}: OK")
        except SyntaxError as e:
            print(f"  {name}: SYNTAX ERROR — {e}")
    print()


def step5_count():
    print("=== Step 5: JSON 파일 수 확인 ===")
    snake = len([f for f in os.listdir(PRESETS_DIR) if f.startswith("irezumi_snake_lotus_")])
    wave  = len([f for f in os.listdir(PRESETS_DIR) if f.startswith("irezumi_wave_fuji_")])
    total = len([f for f in os.listdir(PRESETS_DIR) if f.endswith(".json")])
    print(f"  irezumi_snake_lotus_*.json : {snake}개")
    print(f"  irezumi_wave_fuji_*.json   : {wave}개")
    print(f"  presets/ 전체 JSON         : {total}개\n")


if __name__ == "__main__":
    step1_create_jsons()
    step2_patch_meta()
    step3_patch_hof()
    step4_validate()
    step5_count()
    print("=== 완료 — 이제 git add / commit / push 진행하세요 ===")
