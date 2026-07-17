# -*- coding: utf-8 -*-
import json, os

OUTPUT_DIR = 'presets'
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRESETS = [
    ("bodyglitter_bronze_kyoto_rain", {
        "subject": "Japanese beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, Victoria's Secret Angel body — slender yet curved, long lean legs, sculpted shoulders — entire body covered in dense bronze metallic glitter from neck to toe, warm copper-bronze glitter creating ancient goddess tones, glitter shifting from dark bronze to molten gold at light angles, glossy black hair pinned up with bronze hairpin, expression mysterious and alluring. Wearing: dense bronze glitter covering entire body as sole garment, barefoot with bronze nail polish on toes, long bronze almond nails. Environment: rain-soaked Kyoto alley at night, ancient wooden temples, paper lanterns glowing amber. Lighting: volumetric rain fog warm amber lantern glow, bronze glitter refracting into scattered gold sparks across wet skin. Style: bronze glitter Kyoto rain editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, bronze rain grade, portrait 2:3 vertical.",
        "environment": "rain-soaked Kyoto alley at night",
        "lighting": "volumetric rain fog warm amber lantern",
        "style": "Dolce and Gabbana Italian glamour",
        "quality": "Leica SL2 50mm f/1.4 Summilux, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_platinum_paris_rooftop", {
        "subject": "French European beauty, early 30s, luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: French European beauty, early 30s, luxury glamour physique — elegant curves, refined bone structure, long sculpted legs — entire body covered in dense platinum silver glitter from neck to toe, ultra-high-shine platinum glitter creating futuristic goddess tones, glitter shifting from silver-white to icy platinum at light angles, sleek blonde chignon with platinum hair accessories, expression sophisticated and untouchable. Wearing: dense platinum glitter covering entire body as sole garment, extreme nude stiletto heels, long platinum stiletto nails. Environment: Paris rooftop at dusk, Eiffel Tower glittering in distance, warm city glow. Lighting: Paris golden hour warm backlight, platinum glitter refracting into scattered silver-white explosions. Style: Chanel platinum Paris rooftop editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, platinum dusk grade, portrait 2:3 vertical.",
        "environment": "Paris rooftop at dusk",
        "lighting": "Paris golden hour warm backlight",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_black_void_fitness", {
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — powerful muscular definition, sculpted abs, strong athletic shoulders — entire body covered in dense black holographic glitter from neck to toe, jet black glitter with holographic rainbow micro-shifts creating dark goddess tones, glitter catching light in prismatic bursts against sculpted muscle definition, sleek dark hair in tight bun, expression fierce and powerful. Wearing: dense black holographic glitter covering entire body as sole garment, black stiletto heels, long black stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: harsh direct strobe, black glitter exploding into holographic rainbow prismatic bursts against void. Style: Balmain power glamour editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, black holographic void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "harsh direct strobe",
        "style": "Balmain power glamour",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_jade_bali_temple", {
        "subject": "Southeast Asian beauty, mid-20s, Victoria's Secret Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Southeast Asian beauty, mid-20s, Victoria's Secret Angel body — slender curved figure, warm golden skin tones, graceful posture — entire body covered in dense jade green glitter from neck to toe, deep emerald-jade glitter creating ancient goddess tones, glitter shifting from forest green to luminous jade at light angles, long dark hair adorned with tropical flowers, expression serene and divine. Wearing: dense jade glitter covering entire body as sole garment, barefoot with jade nail polish, long jade almond nails. Environment: Bali ancient temple at golden hour, stone carvings, tropical foliage, incense smoke. Lighting: golden hour dappled light through temple canopy, jade glitter refracting into scattered emerald sparks. Style: Valentino exotic editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, jade temple grade, portrait 2:3 vertical.",
        "environment": "Bali ancient temple at golden hour",
        "lighting": "golden hour dappled temple light",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_teal_amalfi_cliff", {
        "subject": "Mixed race exotic beauty, mid-20s, VS Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, VS Angel body — slender yet curved, sun-kissed exotic skin, long lean legs — entire body covered in dense teal holographic glitter from neck to toe, deep teal-turquoise glitter creating Mediterranean goddess tones, glitter shifting from ocean teal to electric blue-green at light angles, wavy sun-kissed hair flowing freely, expression confident and free. Wearing: dense teal glitter covering entire body as sole garment, nude stiletto heels, long teal almond nails. Environment: Amalfi Coast cliff edge at golden hour, Mediterranean sea glittering below, lemon trees. Lighting: golden hour warm backlight, teal glitter refracting into turquoise and blue crystal bursts. Style: Sports Illustrated swimsuit editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, teal amalfi grade, portrait 2:3 vertical.",
        "environment": "Amalfi Coast cliff edge at golden hour",
        "lighting": "golden hour warm Mediterranean backlight",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_coral_rio_carnival", {
        "subject": "Brazilian goddess, mid-20s, Brazilian carnival physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Brazilian goddess, mid-20s, Brazilian carnival physique — impossibly curvaceous, powerfully round hips, sculpted waist, radiant warm brown skin — entire body covered in dense coral-orange glitter from neck to toe, vibrant coral glitter creating carnival goddess tones, glitter shifting from warm coral to electric orange at light angles, elaborate feathered headpiece in coral and gold, expression joyful and magnetic. Wearing: dense coral glitter covering entire body as sole garment, gold platform heels, long coral stiletto nails. Environment: Rio de Janeiro carnival parade, colorful floats, confetti, city night lights. Lighting: carnival stage lighting warm amber and gold, coral glitter refracting into scattered orange sparks. Style: bold carnival luxury editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, coral carnival grade, portrait 2:3 vertical.",
        "environment": "Rio de Janeiro carnival parade at night",
        "lighting": "carnival stage lighting warm amber",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_lavender_tokyo_shibuya", {
        "subject": "Korean runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, early 20s, slim runway physique 185cm+ — impossibly tall and lean, sharp angular bone structure, ethereal pale skin — entire body covered in dense lavender holographic glitter from neck to toe, soft violet-lavender glitter creating dreamy goddess tones, glitter shifting from pale lavender to electric violet at light angles, pastel purple hair in sleek updo, expression otherworldly and ethereal. Wearing: dense lavender glitter covering entire body as sole garment, transparent platform heels, long lavender stiletto nails. Environment: Shibuya crossing at night, neon reflections on wet pavement. Lighting: multi-colored neon edge glow with lavender dominant, lavender glitter refracting into violet and pink sparks. Style: Balenciaga avant-garde futuristic editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, lavender neon grade, portrait 2:3 vertical.",
        "environment": "Shibuya crossing at night",
        "lighting": "multi-colored neon edge glow lavender dominant",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_champagne_versailles_mature", {
        "subject": "French European beauty, early 30s, luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: French European beauty, early 30s, luxury glamour physique — sophisticated curves, refined elegance, luminous fair skin — entire body covered in dense champagne gold glitter from neck to toe, warm champagne-gold glitter creating opulent goddess tones, glitter shifting from pale gold to warm champagne at light angles, sleek champagne blonde updo with pearl accessories, expression regal and commanding. Wearing: dense champagne glitter covering entire body as sole garment, champagne satin stiletto heels, long champagne almond nails. Environment: Palace of Versailles Hall of Mirrors, golden candlelight, gilded mirrors. Lighting: Versailles chandelier warm gold light, champagne glitter refracting into scattered gold and pearl bursts. Style: Chanel haute couture editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, champagne versailles grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "Versailles chandelier warm gold light",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_cobalt_cape_town", {
        "subject": "Black African goddess, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, sports glamour physique — athletic power, sculpted definition, deep rich luminous skin — entire body covered in dense cobalt blue glitter from neck to toe, electric cobalt-blue glitter creating ocean goddess tones, glitter shifting from deep navy to electric cobalt at light angles, natural afro adorned with blue flowers, expression powerful and proud. Wearing: dense cobalt glitter covering entire body as sole garment, royal blue stiletto heels, long cobalt stiletto nails. Environment: Cape Town clifftop at sunset, Atlantic Ocean, Table Mountain silhouette. Lighting: dramatic sunset warm orange backlight contrasting cobalt glitter, creating electric blue-orange contrast. Style: Vogue Italia high-fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, cobalt cape grade, portrait 2:3 vertical.",
        "environment": "Cape Town clifftop at sunset",
        "lighting": "dramatic sunset warm orange backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_crimson_vegas_strip", {
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — impossibly curvaceous, powerfully thick thighs, sculpted waist, warm caramel skin — entire body covered in dense crimson red glitter from neck to toe, deep blood-crimson glitter creating dangerous goddess tones, glitter shifting from dark crimson to electric ruby at light angles, sleek dark hair in dramatic updo, expression seductive and magnetic. Wearing: dense crimson glitter covering entire body as sole garment, red stiletto heels, long crimson stiletto nails. Environment: Las Vegas Strip at night, casino neon lights, electric billboards. Lighting: Vegas neon warm red and gold dominant, crimson glitter refracting into ruby and scarlet sparks. Style: Versace campaign bold luxury glamour. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, crimson vegas grade, portrait 2:3 vertical.",
        "environment": "Las Vegas Strip at night",
        "lighting": "Vegas neon warm red and gold dominant",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_white_void_ballerina_korean", {
        "subject": "Korean beauty, early 20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, early 20s, ballerina physique — slender elongated figure, graceful elegant posture, porcelain pale skin — entire body covered in dense pure white holographic glitter from neck to toe, luminous white glitter creating angelic goddess tones, glitter creating soft prismatic rainbow shifts at light angles, elegant white updo with pearl hairpin, expression serene and divine. Wearing: dense white glitter covering entire body as sole garment, white satin pointe shoes, long white almond nails. Environment: pure white minimalist studio, seamless white backdrop. Lighting: soft beauty dish even flattering illumination, white glitter refracting into soft rainbow prismatic halos. Style: Chanel classic luxury elegance. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, white void ballerina grade, portrait 2:3 vertical.",
        "environment": "pure white minimalist studio",
        "lighting": "soft beauty dish even illumination",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_orange_marrakech", {
        "subject": "Middle Eastern beauty, mid-20s, hot glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern beauty, mid-20s, hot glamour physique — voluptuous curves, warm olive skin, magnetic presence — entire body covered in dense orange-gold glitter from neck to toe, vibrant saffron-orange glitter creating Moroccan goddess tones, glitter shifting from warm orange to molten gold at light angles, dark hair adorned with gold Moroccan headpiece, expression exotic and alluring. Wearing: dense orange glitter covering entire body as sole garment, gold anklet and barefoot, long gold almond nails. Environment: Marrakech luxury riad, Moroccan lanterns, mosaic tile courtyard, rose petals. Lighting: Moroccan lantern warm amber and orange, orange glitter refracting into scattered gold and saffron sparks. Style: Gucci eclectic maximalism. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, saffron marrakech grade, portrait 2:3 vertical.",
        "environment": "Marrakech luxury riad courtyard",
        "lighting": "Moroccan lantern warm amber and orange",
        "style": "Gucci eclectic maximalism",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_magenta_new_york_loft", {
        "subject": "Eastern European bombshell, mid-20s, super glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Eastern European bombshell, mid-20s, super glamour physique — ultra-curvaceous hourglass, powerful presence, luminous fair skin — entire body covered in dense magenta-pink glitter from neck to toe, electric hot magenta glitter creating pop art goddess tones, glitter shifting from deep magenta to electric pink at light angles, sleek platinum blonde hair in dramatic blowout, expression bold and commanding. Wearing: dense magenta glitter covering entire body as sole garment, hot pink stiletto heels, long magenta stiletto nails. Environment: New York loft at night, floor-to-ceiling windows, Manhattan skyline. Lighting: warm Manhattan city glow, magenta glitter refracting into pink and violet sparks against city lights. Style: Tom Ford bold glamour editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, magenta manhattan grade, portrait 2:3 vertical.",
        "environment": "New York loft at night, Manhattan skyline",
        "lighting": "warm Manhattan city glow",
        "style": "Tom Ford bold glamour editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_green_forest_goddess", {
        "subject": "Scandinavian beauty, mid-20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian beauty, mid-20s, ballerina physique — slender graceful figure, ethereal fair skin, otherworldly presence — entire body covered in dense forest green glitter from neck to toe, deep emerald-forest glitter creating nature goddess tones, glitter shifting from dark forest green to electric lime at light angles, long blonde hair adorned with forest flowers and leaves, expression ethereal and magical. Wearing: dense green glitter covering entire body as sole garment, barefoot, long green almond nails. Environment: enchanted forest at dawn, ancient trees, morning mist, dappled sunlight. Lighting: soft dappled dawn light through forest canopy, green glitter refracting into emerald and lime sparks. Style: Alexander McQueen dramatic fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, forest goddess grade, portrait 2:3 vertical.",
        "environment": "enchanted forest at dawn",
        "lighting": "soft dappled dawn light through forest canopy",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_bronze_fitness_strobe", {
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — powerful muscular definition, sculpted abs, strong athletic shoulders, sun-bronzed skin — entire body covered in dense bronze metallic glitter from neck to toe, warm copper-bronze glitter amplifying muscular definition, glitter shifting from dark bronze to molten copper at light angles, hair slicked back, expression fierce and powerful. Wearing: dense bronze glitter covering entire body as sole garment, bronze stiletto heels, long bronze stiletto nails. Environment: pure black void. Lighting: harsh direct strobe, bronze glitter exploding into copper and gold sparks against void, muscular definition carved by deep shadows. Style: Balmain power glamour editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, bronze strobe grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "harsh direct strobe",
        "style": "Balmain power glamour",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_platinum_void_black_glam", {
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — entire body covered in dense platinum silver glitter from neck to toe, ultra-high-shine platinum glitter creating electric contrast against deep skin, glitter shifting from silver-white to icy platinum at light angles, voluminous afro with platinum hair accessories, expression fierce and untouchable. Wearing: dense platinum glitter covering entire body as sole garment, chrome stiletto heels, long platinum stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: dramatic chiaroscuro single spotlight, platinum glitter creating electric silver explosions against deep skin and void. Style: Vogue Italia high-fashion editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, platinum void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_gold_onsen_mature", {
        "subject": "Japanese beauty, early 30s, mature luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, early 30s, mature luxury glamour physique — graceful sophisticated curves, refined elegance, luminous warm skin — entire body covered in dense gold metallic glitter from neck to toe, warm molten gold glitter creating imperial goddess tones, glitter shifting from deep gold to luminous amber at light angles, sleek dark hair pinned up with gold kanzashi, expression serene and commanding. Wearing: dense gold glitter covering entire body as sole garment, barefoot with gold toe rings, long gold almond nails. Environment: Budapest thermal bath, mineral waters, classical columns, steam. Lighting: volumetric steam fog warm amber, gold glitter refracting into molten amber and gold bursts through steam. Style: Harper's Bazaar sensual fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, gold onsen grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog warm amber",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_silver_cape_town_sports", {
        "subject": "Black African goddess, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, sports glamour physique — athletic powerful build, sculpted definition, deep luminous rich skin — entire body covered in dense silver metallic glitter from neck to toe, high-shine silver glitter creating electric contrast against deep skin, glitter shifting from chrome silver to icy white at light angles, natural afro with silver accessories, expression powerful and magnetic. Wearing: dense silver glitter covering entire body as sole garment, silver stiletto heels, long silver stiletto nails. Environment: Cape Town clifftop at golden hour, Atlantic Ocean, Table Mountain. Lighting: warm golden sunset backlight, silver glitter refracting into scattered chrome and white sparks against deep skin. Style: Vogue Italia high-fashion editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, silver cape grade, portrait 2:3 vertical.",
        "environment": "Cape Town clifftop at golden hour",
        "lighting": "warm golden sunset backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_rose_gold_maldives", {
        "subject": "Mixed race exotic beauty, mid-20s, VS Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, VS Angel body — slender yet curved, warm exotic skin, luminous presence — entire body covered in dense rose gold glitter from neck to toe, soft rose-gold glitter creating romantic goddess tones, glitter shifting from blush pink to warm gold at light angles, flowing rose-tinted waves with rose gold hair accessories, expression radiant and romantic. Wearing: dense rose gold glitter covering entire body as sole garment, rose gold stiletto heels, long rose gold almond nails. Environment: Maldives overwater bungalow at sunset, crystal turquoise water, pink sky. Lighting: Maldives golden sunset with pink cloud reflections, rose gold glitter refracting into warm pink and gold sparks. Style: Sports Illustrated swimsuit editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, rose gold maldives grade, portrait 2:3 vertical.",
        "environment": "Maldives overwater bungalow at sunset",
        "lighting": "Maldives golden sunset pink sky reflections",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_blue_void_runway", {
        "subject": "Korean runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, early 20s, slim runway physique 185cm+ — impossibly tall and lean, sharp angular bone structure, ethereal pale skin — entire body covered in dense electric blue holographic glitter from neck to toe, intense electric blue glitter creating futuristic goddess tones, glitter shifting from deep sapphire to electric cyan at light angles, sleek dark hair in architectural updo, expression otherworldly and commanding. Wearing: dense blue holographic glitter covering entire body as sole garment, transparent platform heels, long electric blue stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: dramatic chiaroscuro with electric blue edge light, blue glitter refracting into cyan and sapphire crystal explosions against void. Style: Balenciaga avant-garde futuristic editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, electric blue void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro electric blue edge light",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_emerald_kyoto_rain", {
        "subject": "Japanese beauty, mid-20s, hot glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, mid-20s, hot glamour physique — voluptuous curves, warm skin, magnetic sensual presence — entire body covered in dense emerald green glitter from neck to toe, deep forest-emerald glitter creating enchanted goddess tones, glitter shifting from dark emerald to electric green at light angles, sleek dark hair adorned with green kanzashi pins, expression mysterious and alluring. Wearing: dense emerald glitter covering entire body as sole garment, black stiletto heels, long emerald almond nails. Environment: rain-soaked Kyoto alley at night, ancient temples, amber lanterns. Lighting: volumetric rain fog warm amber lantern, emerald glitter refracting into scattered green and gold sparks through rain. Style: Dolce and Gabbana Italian glamour. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, emerald kyoto grade, portrait 2:3 vertical.",
        "environment": "rain-soaked Kyoto alley at night",
        "lighting": "volumetric rain fog warm amber lantern",
        "style": "Dolce and Gabbana Italian glamour",
        "quality": "Leica SL2 50mm f/1.4 Summilux, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_purple_aurora_nordic", {
        "subject": "Scandinavian beauty, mid-20s, VS Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian beauty, mid-20s, VS Angel body — slender yet curved, ethereal fair skin, luminous Nordic presence — entire body covered in dense deep purple holographic glitter from neck to toe, rich violet-purple glitter creating aurora goddess tones, glitter shifting from deep indigo to electric violet at light angles, platinum blonde hair flowing freely, expression ethereal and otherworldly. Wearing: dense purple holographic glitter covering entire body as sole garment, nude stiletto heels, long violet almond nails. Environment: Iceland glacier, northern lights aurora, vast dark sky. Lighting: aurora borealis purple and green curtain of light, purple glitter refracting into violet and indigo crystal explosions against aurora. Style: Alexander McQueen dramatic fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, purple aurora grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier northern lights",
        "lighting": "aurora borealis purple and green curtain",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_copper_void_milf", {
        "subject": "European beauty, early 30s, MILF glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European beauty, early 30s, MILF glamour physique — mature voluptuous curves, confident presence, luminous fair skin with natural maturity — entire body covered in dense copper metallic glitter from neck to toe, warm rich copper glitter creating goddess tones, glitter shifting from dark bronze-copper to electric rose-gold at light angles, sleek auburn hair in elegant updo, expression confident and seductive. Wearing: dense copper glitter covering entire body as sole garment, copper stiletto heels, long copper almond nails. Environment: pure black void, seamless obsidian backdrop. Lighting: dramatic chiaroscuro warm spotlight, copper glitter creating warm rose-gold and copper explosions against void. Style: Vogue Italia high-fashion editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, copper void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro warm spotlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_silver_dubai_milf", {
        "subject": "European beauty, early 30s, MILF glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European beauty, early 30s, MILF glamour physique — mature voluptuous curves, confident powerful presence, luminous fair skin — entire body covered in dense silver metallic glitter from neck to toe, high-shine silver glitter creating contemporary goddess tones, glitter shifting from chrome to icy white at light angles, sleek silver-blonde hair in dramatic blowout, expression commanding and magnetic. Wearing: dense silver glitter covering entire body as sole garment, silver stiletto heels, long silver stiletto nails. Environment: Dubai luxury penthouse rooftop at night, city skyline. Lighting: strong rim backlight from Dubai city glow, silver glitter refracting into chrome and white sparks against cityscape. Style: Versace campaign bold luxury glamour. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, silver dubai grade, portrait 2:3 vertical.",
        "environment": "Dubai luxury penthouse rooftop at night",
        "lighting": "strong rim backlight from Dubai city glow",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_gold_rio_carnival", {
        "subject": "Brazilian goddess, mid-20s, Brazilian carnival physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Brazilian goddess, mid-20s, Brazilian carnival physique — impossibly curvaceous, powerfully round hips, radiant warm brown skin — entire body covered in dense gold metallic glitter from neck to toe, molten gold glitter creating carnival queen tones, glitter shifting from deep gold to electric amber at light angles, elaborate gold feathered headpiece, expression joyful and magnetic. Wearing: dense gold glitter covering entire body as sole garment, gold platform heels, long gold stiletto nails. Environment: Rio de Janeiro carnival parade, colorful floats, confetti explosion. Lighting: carnival stage spotlights warm gold, gold glitter refracting into amber and gold explosions. Style: bold carnival luxury editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, gold carnival grade, portrait 2:3 vertical.",
        "environment": "Rio de Janeiro carnival parade at night",
        "lighting": "carnival stage spotlights warm gold",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_rose_gold_dubai_sports", {
        "subject": "Middle Eastern beauty, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern beauty, mid-20s, sports glamour physique — athletic curves, sculpted definition, warm olive skin — entire body covered in dense rose gold glitter from neck to toe, soft rose-gold glitter creating contemporary goddess tones, glitter shifting from blush to warm gold at light angles, sleek dark hair in tight ponytail, expression fierce and athletic. Wearing: dense rose gold glitter covering entire body as sole garment, rose gold stiletto heels, long rose gold stiletto nails. Environment: Dubai luxury penthouse rooftop at night, skyline panorama. Lighting: strong rim backlight from Dubai city glow, rose gold glitter refracting into pink and gold sparks. Style: Versace campaign bold luxury glamour. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, rose gold dubai grade, portrait 2:3 vertical.",
        "environment": "Dubai luxury penthouse rooftop at night",
        "lighting": "strong rim backlight from Dubai city glow",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_blue_santorini_mature", {
        "subject": "French European beauty, early 30s, luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: French European beauty, early 30s, luxury glamour physique — sophisticated mature curves, refined elegance, luminous fair skin — entire body covered in dense sapphire blue holographic glitter from neck to toe, deep sapphire-blue glitter creating Mediterranean goddess tones, glitter shifting from deep navy to electric sapphire at light angles, sleek dark blonde updo with sapphire accessories, expression regal and commanding. Wearing: dense blue holographic glitter covering entire body as sole garment, navy stiletto heels, long sapphire almond nails. Environment: Santorini cliff edge at golden hour, Aegean Sea, whitewashed buildings. Lighting: golden hour warm backlight with Aegean blue reflections, blue glitter refracting into sapphire and cyan sparks. Style: Valentino red carpet luxury editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, sapphire santorini grade, portrait 2:3 vertical.",
        "environment": "Santorini cliff edge at golden hour",
        "lighting": "golden hour warm backlight Aegean blue",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_silver_aurora_runway", {
        "subject": "Scandinavian beauty, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian beauty, early 20s, slim runway physique 185cm+ — impossibly tall and lean, angular Nordic bone structure, ethereal fair skin — entire body covered in dense silver holographic glitter from neck to toe, icy silver glitter creating arctic goddess tones, glitter shifting from chrome to iridescent white-blue at light angles, platinum straight hair flowing freely, expression ethereal and otherworldly. Wearing: dense silver holographic glitter covering entire body as sole garment, transparent platform heels, long silver stiletto nails. Environment: Iceland glacier, northern lights aurora, vast dark sky. Lighting: aurora borealis green and white curtain, silver glitter refracting into icy white and green aurora-tinted explosions. Style: Alexander McQueen dramatic fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver aurora grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier northern lights",
        "lighting": "aurora borealis green and white curtain",
        "style": "Alexander McQueen dramatic fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_gold_versailles_colombian", {
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — impossibly curvaceous, powerfully round hips, warm caramel skin — entire body covered in dense gold metallic glitter from neck to toe, imperial molten gold glitter creating baroque goddess tones, glitter shifting from deep gold to electric amber at light angles, sleek dark hair in elaborate updo with gold accessories, expression regal and magnetic. Wearing: dense gold glitter covering entire body as sole garment, gold stiletto heels, long gold stiletto nails. Environment: Palace of Versailles Hall of Mirrors, golden candlelight, gilded architecture. Lighting: Versailles chandelier warm gold, gold glitter refracting into molten amber and gold explosions against gilded mirrors. Style: Versace campaign bold luxury glamour. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, gold versailles grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "Versailles chandelier warm gold light",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_rainbow_void_fitness", {
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — powerful muscular definition, sculpted abs, strong athletic build — entire body covered in dense rainbow holographic glitter from neck to toe, prismatic rainbow glitter refracting across muscular definition, glitter shifting through full spectrum at every light angle, hair slicked back, expression fierce and powerful. Wearing: dense rainbow holographic glitter covering entire body as sole garment, black stiletto heels, long holographic stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: harsh direct strobe, rainbow glitter exploding into full-spectrum prismatic bursts across muscular definition against void. Style: Balmain power glamour editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, rainbow strobe grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "harsh direct strobe",
        "style": "Balmain power glamour",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_emerald_monaco_milf", {
        "subject": "European beauty, early 30s, MILF glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European beauty, early 30s, MILF glamour physique — mature voluptuous curves, sophisticated elegance, luminous fair skin — entire body covered in dense emerald green glitter from neck to toe, deep forest-emerald glitter creating opulent goddess tones, glitter shifting from dark forest to electric emerald at light angles, sleek dark hair in elegant chignon with emerald accessories, expression confident and seductive. Wearing: dense emerald glitter covering entire body as sole garment, emerald green stiletto heels, long emerald almond nails. Environment: Monaco luxury terrace at night, Mediterranean lights, yacht harbor. Lighting: Monaco nightscape warm rim backlight, emerald glitter refracting into scattered green sparks against Monaco lights. Style: Valentino red carpet luxury editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, emerald monaco grade, portrait 2:3 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco nightscape warm rim backlight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_copper_rio_carnival", {
        "subject": "Brazilian goddess, mid-20s, Brazilian carnival physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Brazilian goddess, mid-20s, Brazilian carnival physique — impossibly curvaceous, powerfully round hips, radiant warm brown skin — entire body covered in dense copper metallic glitter from neck to toe, warm rich copper glitter amplifying warm skin tones, glitter shifting from dark bronze-copper to electric rose-gold at light angles, elaborate copper feathered headpiece, expression joyful and magnetic. Wearing: dense copper glitter covering entire body as sole garment, copper platform heels, long copper stiletto nails. Environment: Rio de Janeiro carnival parade, colorful floats, confetti. Lighting: carnival stage warm amber spotlights, copper glitter refracting into rose-gold and copper explosions. Style: bold carnival luxury editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, copper carnival grade, portrait 2:3 vertical.",
        "environment": "Rio de Janeiro carnival parade at night",
        "lighting": "carnival stage warm amber spotlights",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_silver_marrakech_sports", {
        "subject": "Middle Eastern beauty, mid-20s, sports glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern beauty, mid-20s, sports glamour physique — athletic curves, sculpted definition, warm olive skin — entire body covered in dense silver metallic glitter from neck to toe, high-shine silver glitter creating stark contrast against warm olive skin, glitter shifting from chrome to icy white at light angles, dark hair adorned with silver Moroccan headpiece, expression powerful and exotic. Wearing: dense silver glitter covering entire body as sole garment, silver stiletto heels, long silver stiletto nails. Environment: Marrakech luxury riad, Moroccan lanterns, mosaic tile. Lighting: Moroccan lantern warm amber contrasting silver glitter, creating warm-cool contrast. Style: Gucci eclectic maximalism. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver marrakech grade, portrait 2:3 vertical.",
        "environment": "Marrakech luxury riad",
        "lighting": "Moroccan lantern warm amber",
        "style": "Gucci eclectic maximalism",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_gold_cape_town_black_glam", {
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — entire body covered in dense gold metallic glitter from neck to toe, imperial gold glitter creating extraordinary contrast against deep skin, glitter shifting from deep gold to electric amber at light angles, voluminous natural afro with gold accessories, expression fierce and regal. Wearing: dense gold glitter covering entire body as sole garment, gold stiletto heels, long gold stiletto nails. Environment: Cape Town clifftop at sunset, Atlantic Ocean, Table Mountain. Lighting: dramatic sunset warm orange backlight, gold glitter refracting into amber and gold explosions against deep skin and sunset sky. Style: Vogue Italia high-fashion editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, gold cape grade, portrait 2:3 vertical.",
        "environment": "Cape Town clifftop at sunset",
        "lighting": "dramatic sunset warm orange backlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_blue_bali_temple", {
        "subject": "Southeast Asian beauty, mid-20s, hot glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Southeast Asian beauty, mid-20s, hot glamour physique — voluptuous curves, warm golden skin, magnetic sensual presence — entire body covered in dense sapphire blue holographic glitter from neck to toe, electric sapphire glitter creating tropical goddess tones, glitter shifting from deep navy to electric cyan at light angles, dark hair adorned with tropical flowers and blue gems, expression serene and divine. Wearing: dense blue holographic glitter covering entire body as sole garment, barefoot with blue toe nails, long sapphire almond nails. Environment: Bali ancient temple at golden hour, stone carvings, incense smoke, tropical flowers. Lighting: golden hour dappled light through temple canopy, blue glitter refracting into cyan and sapphire sparks. Style: Valentino exotic editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, sapphire bali grade, portrait 2:3 vertical.",
        "environment": "Bali ancient temple at golden hour",
        "lighting": "golden hour dappled temple light",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_purple_void_black_glam", {
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — entire body covered in dense deep purple holographic glitter from neck to toe, rich violet-purple glitter creating extraordinary contrast against deep skin, glitter shifting from deep indigo to electric violet at light angles, voluminous afro with purple accessories, expression fierce and untouchable. Wearing: dense purple holographic glitter covering entire body as sole garment, purple stiletto heels, long violet stiletto nails. Environment: pure black void, seamless obsidian backdrop. Lighting: dramatic chiaroscuro single spotlight, purple glitter creating violet and indigo explosions against deep skin and void. Style: Vogue Italia high-fashion editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, purple void grade, portrait 2:3 vertical.",
        "environment": "pure black void",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_red_marrakech_colombian", {
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — impossibly curvaceous, powerfully round hips, warm caramel skin — entire body covered in dense crimson red glitter from neck to toe, deep blood-red glitter creating passionate goddess tones, glitter shifting from dark crimson to electric scarlet at light angles, sleek dark hair adorned with red rose and gold headpiece, expression fiery and magnetic. Wearing: dense red glitter covering entire body as sole garment, red stiletto heels, long crimson stiletto nails. Environment: Marrakech luxury riad, Moroccan lanterns, rose petals. Lighting: Moroccan lantern warm amber and red, red glitter refracting into ruby and scarlet sparks. Style: Gucci eclectic maximalism. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, red marrakech grade, portrait 2:3 vertical.",
        "environment": "Marrakech luxury riad",
        "lighting": "Moroccan lantern warm amber and red",
        "style": "Gucci eclectic maximalism",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_ice_blue_onsen_mature", {
        "subject": "Japanese beauty, early 30s, mature luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Japanese beauty, early 30s, mature luxury glamour physique — graceful sophisticated curves, refined elegance, luminous warm skin — entire body covered in dense ice blue holographic glitter from neck to toe, icy blue glitter creating ethereal contrast against warm skin, glitter shifting from pale ice to electric azure at light angles, sleek dark hair in elegant updo with jade pin, expression serene and commanding. Wearing: dense ice blue holographic glitter covering entire body as sole garment, barefoot with pale blue toe nails, long ice blue almond nails. Environment: Budapest thermal bath, mineral waters, classical architecture, steam. Lighting: volumetric steam fog cool blue-tinted ambient, ice blue glitter refracting into white and blue crystal bursts through steam. Style: Harper's Bazaar sensual fashion editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, ice blue onsen grade, portrait 2:3 vertical.",
        "environment": "Budapest thermal bath",
        "lighting": "volumetric steam fog cool blue ambient",
        "style": "Harper's Bazaar sensual fashion editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_silver_versailles_runway", {
        "subject": "Eastern European bombshell, mid-20s, super glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Eastern European bombshell, mid-20s, super glamour physique — ultra-curvaceous hourglass, powerful presence, luminous fair skin — entire body covered in dense silver metallic glitter from neck to toe, high-shine silver glitter creating baroque goddess tones, glitter shifting from chrome to icy white at light angles, dramatic platinum updo with silver crown accessories, expression regal and commanding. Wearing: dense silver glitter covering entire body as sole garment, silver stiletto heels, long silver stiletto nails. Environment: Palace of Versailles Hall of Mirrors, candlelight, gilded architecture. Lighting: Versailles chandelier warm gold contrasting silver glitter, creating warm-cool baroque contrast. Style: Versace campaign bold luxury glamour. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, silver versailles grade, portrait 2:3 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "Versailles chandelier warm gold light",
        "style": "Versace campaign bold luxury glamour",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_gold_tokyo_runway", {
        "subject": "Korean runway goddess, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, early 20s, slim runway physique 185cm+ — impossibly tall and lean, sharp angular bone structure, ethereal pale skin — entire body covered in dense gold metallic glitter from neck to toe, warm molten gold glitter creating futuristic goddess tones, glitter shifting from deep gold to electric amber at light angles, sleek dark hair in architectural updo with gold accessories, expression otherworldly and commanding. Wearing: dense gold glitter covering entire body as sole garment, gold platform heels, long gold stiletto nails. Environment: Tokyo Shibuya crossing at night, neon reflections on wet pavement. Lighting: multi-colored neon with gold dominant, gold glitter refracting into amber and warm sparks against neon backdrop. Style: Balenciaga avant-garde futuristic editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, gold tokyo grade, portrait 2:3 vertical.",
        "environment": "Tokyo Shibuya crossing at night",
        "lighting": "multi-colored neon gold dominant",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_rose_gold_amalfi_ballerina", {
        "subject": "Korean beauty, early 20s, ballerina physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean beauty, early 20s, ballerina physique — slender elongated figure, graceful elegant posture, porcelain pale skin — entire body covered in dense rose gold glitter from neck to toe, soft rose-gold glitter creating romantic goddess tones on delicate ballerina frame, glitter shifting from blush pink to warm gold at light angles, elegant ballet chignon with rose gold pins, expression serene and graceful. Wearing: dense rose gold glitter covering entire body as sole garment, rose gold satin pointe shoes, long rose almond nails. Environment: Amalfi Coast cliff edge at golden hour, Mediterranean sea, lemon groves. Lighting: golden hour warm Mediterranean backlight, rose gold glitter refracting into warm pink and gold sparks. Style: Chanel classic luxury elegance. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, rose gold amalfi grade, portrait 2:3 vertical.",
        "environment": "Amalfi Coast cliff edge at golden hour",
        "lighting": "golden hour warm Mediterranean backlight",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_blue_monaco_colombian", {
        "subject": "Colombian Latina goddess, mid-20s, Colombian reggaeton physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — impossibly curvaceous, powerfully round hips, warm caramel skin — entire body covered in dense royal blue holographic glitter from neck to toe, deep royal blue glitter creating regal goddess tones, glitter shifting from deep navy to electric cobalt at light angles, sleek dark hair in dramatic updo with sapphire accessories, expression regal and magnetic. Wearing: dense blue holographic glitter covering entire body as sole garment, royal blue stiletto heels, long sapphire stiletto nails. Environment: Monaco luxury terrace at night, Mediterranean lights, yacht harbor. Lighting: Monaco nightscape warm rim backlight, blue glitter refracting into cobalt and sapphire sparks against Monaco lights. Style: Valentino red carpet luxury editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, royal blue monaco grade, portrait 2:3 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco nightscape warm rim backlight",
        "style": "Valentino red carpet luxury editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_purple_marrakech_mature", {
        "subject": "Middle Eastern beauty, early 30s, mature luxury glamour physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Middle Eastern beauty, early 30s, mature luxury glamour physique — sophisticated voluptuous curves, regal presence, warm olive skin — entire body covered in dense deep purple glitter from neck to toe, rich royal purple glitter creating exotic goddess tones, glitter shifting from deep indigo to electric violet at light angles, dark hair adorned with amethyst and gold Moroccan headpiece, expression regal and mysterious. Wearing: dense purple glitter covering entire body as sole garment, purple stiletto heels, long amethyst almond nails. Environment: Marrakech luxury riad, Moroccan lanterns, intricate tilework, rose petals. Lighting: Moroccan lantern warm amber contrasting deep purple glitter. Style: Gucci eclectic maximalism. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, purple marrakech grade, portrait 2:3 vertical.",
        "environment": "Marrakech luxury riad",
        "lighting": "Moroccan lantern warm amber",
        "style": "Gucci eclectic maximalism",
        "quality": "Phase One XF IQ4 110mm f/2.8 ISO 50, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_red_dubai_black_glam", {
        "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
        "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich skin — entire body covered in dense crimson red glitter from neck to toe, deep blood-red glitter creating electric contrast against deep skin, glitter shifting from dark crimson to electric scarlet at light angles, sleek afro with red accessories, expression fierce and magnetic. Wearing: dense red glitter covering entire body as sole garment, red stiletto heels, long crimson stiletto nails. Environment: Dubai luxury penthouse rooftop at night, city skyline. Lighting: strong rim backlight from Dubai city glow, red glitter refracting into scarlet and crimson explosions against deep skin and city lights. Style: Vogue Italia high-fashion editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, red dubai grade, portrait 2:3 vertical.",
        "environment": "Dubai luxury penthouse rooftop at night",
        "lighting": "strong rim backlight from Dubai city glow",
        "style": "Vogue Italia high-fashion editorial",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_ice_blue_paris_runway", {
        "subject": "French European beauty, early 20s, slim runway physique 185cm+",
        "prompt": "Professional fashion photograph, full body shot. Model: French European beauty, early 20s, slim runway physique 185cm+ — impossibly tall and lean, angular sharp bone structure, luminous fair skin — entire body covered in dense ice blue holographic glitter from neck to toe, icy blue glitter creating ethereal frozen goddess tones, glitter shifting from pale ice to electric azure at light angles, sleek platinum blonde in dramatic chignon, expression otherworldly and commanding. Wearing: dense ice blue holographic glitter covering entire body as sole garment, transparent platform heels, long ice blue stiletto nails. Environment: Paris rooftop at dusk, Eiffel Tower in distance, warm city glow. Lighting: Paris golden hour warm contrasting ice blue glitter, creating warm-cool contrast. Style: Chanel classic luxury elegance. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, ice blue paris grade, portrait 2:3 vertical.",
        "environment": "Paris rooftop at dusk",
        "lighting": "Paris golden hour warm backlight",
        "style": "Chanel classic luxury elegance",
        "quality": "Hasselblad H6D 80mm f/2.8 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_gold_maldives_vs_angel", {
        "subject": "Mixed race exotic beauty, mid-20s, VS Angel body",
        "prompt": "Professional fashion photograph, full body shot. Model: Mixed race exotic beauty, mid-20s, VS Angel body — slender yet curved, warm exotic sun-kissed skin, luminous tropical presence — entire body covered in dense gold metallic glitter from neck to toe, molten gold glitter creating tropical goddess tones, glitter shifting from deep gold to electric amber at light angles, flowing sun-kissed waves with gold shell accessories, expression radiant and free. Wearing: dense gold glitter covering entire body as sole garment, gold stiletto sandals, long gold almond nails. Environment: Maldives overwater bungalow at sunset, crystal turquoise water, golden sky. Lighting: Maldives golden sunset warm backlight, gold glitter refracting into amber and gold explosions. Style: Sports Illustrated swimsuit editorial. Shot on Canon EOS R5 85mm f/1.2 ISO 100, 8K UHD, gold maldives grade, portrait 2:3 vertical.",
        "environment": "Maldives overwater bungalow at sunset",
        "lighting": "Maldives golden sunset warm backlight",
        "style": "Sports Illustrated swimsuit editorial",
        "quality": "Canon EOS R5 85mm f/1.2 ISO 100, hyperrealistic photography, 8K"
    }),
    ("bodyglitter_silver_tokyo_fitness", {
        "subject": "European fitness goddess, mid-20s, power fitness physique",
        "prompt": "Professional fashion photograph, full body shot. Model: European fitness goddess, mid-20s, power fitness physique — powerful muscular definition, sculpted abs, strong athletic build — entire body covered in dense silver metallic glitter from neck to toe, high-shine silver glitter amplifying muscular definition, glitter shifting from chrome to icy white at light angles, sleek hair in tight bun, expression fierce and powerful. Wearing: dense silver glitter covering entire body as sole garment, black platform heels, long silver stiletto nails. Environment: Tokyo Shibuya crossing at night, neon reflections on wet pavement. Lighting: multi-colored neon with silver reflecting all colors, silver glitter refracting into prismatic rainbow sparks from neon sources. Style: Balenciaga avant-garde futuristic editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, silver tokyo grade, portrait 2:3 vertical.",
        "environment": "Tokyo Shibuya crossing at night",
        "lighting": "multi-colored neon silver reflecting all",
        "style": "Balenciaga avant-garde futuristic editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, hyperrealistic photography, 8K"
    }),
]

# HOF 목록
HOF_KEYS = {
    "bodyglitter_platinum_paris_rooftop",
    "bodyglitter_black_void_fitness",
    "bodyglitter_coral_rio_carnival",
    "bodyglitter_cobalt_cape_town",
    "bodyglitter_platinum_void_black_glam",
    "bodyglitter_purple_aurora_nordic",
    "bodyglitter_gold_rio_carnival",
    "bodyglitter_gold_cape_town_black_glam",
    "bodyglitter_red_dubai_black_glam",
    "bodyglitter_gold_maldives_vs_angel",
}

saved = 0
for key, data in PRESETS:
    path = os.path.join(OUTPUT_DIR, f'{key}.json')
    if os.path.exists(path):
        print(f"SKIP: {key}")
        continue
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    saved += 1
    print(f"저장: {key}")

print(f"\n완료! {saved}종 저장 (총 {len(PRESETS)}종)")
print(f"HOF: {len(HOF_KEYS)}종")
