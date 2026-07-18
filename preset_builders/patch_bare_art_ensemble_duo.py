# -*- coding: utf-8 -*-
"""
✨ Bare Art Ensemble 카테고리 신설 + 듀오 배치 1~3 패치
- presets/ JSON 25개 생성
- core/presets_meta.py 에 BARE_ART_ENSEMBLE 카테고리 추가
- core/hof_tier.py 에 HOF 20종 추가
"""

import os, json, ast

BASE       = r"C:\Dev\LumineX"
PRESETS_DIR = os.path.join(BASE, "presets")
META_PATH   = os.path.join(BASE, "core", "presets_meta.py")
HOF_PATH    = os.path.join(BASE, "core", "hof_tier.py")

# ── JSON 데이터 ───────────────────────────────────────────────────────────────

PRESETS = {

    # ── 배치 1: 이레즈미×글리터 ───────────────────────────────────────────────
    "duo_irezumi_dragon_glitter_gold_void": {
        "subject": "Black African goddess + Colombian Latina goddess duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women side by side. LEFT: Black African goddess, mid-20s, Black glamour hourglass physique — deep rich skin — body fully covered in Japanese irezumi tattoos: massive dragon coiling entire body from ankles to neck, deep black ink with blazing gold highlights, dragon claw gripping hip, flames erupting from shoulders. RIGHT: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — warm caramel skin — body fully covered in 24K gold ultra-fine body glitter: maximum density gold coating every inch, liquid molten gold effect following every powerful curve. LEFT: gold platform heels, long gold stiletto nails. RIGHT: gold stiletto heels, long gold stiletto nails. Both: full body high-gloss oil, sleek updos. Environment: pure black void, seamless obsidian backdrop. Lighting: dual spotlight — warm amber on dragon gold ink left, blazing gold on glitter right — dragon flames and glitter curves creating unified fire energy in void. Style: Balmain power duo void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, dragon gold glitter void grade, portrait 4:5 vertical.",
        "environment": "pure black void",
        "lighting": "dual spotlight warm amber and blazing gold",
        "style": "Balmain power duo void editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_wave_glitter_indigo_santorini": {
        "subject": "Japanese ballerina + Scandinavian VS Angel duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing back to back on Santorini terrace. LEFT facing camera: Japanese beauty, early 20s, ballerina physique — luminous warm skin — body fully covered in Japanese irezumi tattoos: Great Wave and Mount Fuji across entire body, deep indigo blue ink with white foam highlights. RIGHT facing away: Scandinavian beauty, mid-20s, VS Angel body — porcelain fair skin — body fully covered in deep indigo and silver ultra-fine body glitter: ocean-blue glitter coating entire back from neck to ankles, glitter shifting indigo-silver-teal in sunlight. LEFT: rose gold pointe shoes, long indigo nails. RIGHT: silver stiletto heels, long silver nails. Environment: Santorini whitewashed terrace at golden hour, blue domes, Aegean Sea panorama stretching behind both women. Lighting: golden hour warm backlight — indigo wave ink and indigo glitter both catching identical Mediterranean light creating seamless duality. Style: Valentino Mediterranean duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, wave indigo santorini duo grade, portrait 4:5 vertical.",
        "environment": "Santorini whitewashed terrace at golden hour",
        "lighting": "golden hour warm backlight",
        "style": "Valentino Mediterranean duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_irezumi_phoenix_glitter_crimson_shibuya": {
        "subject": "Korean runway goddess + European VS Angel duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women walking toward camera in heavy rain. LEFT: Korean runway goddess, early 20s, 185cm+ slim runway physique — ethereal pale skin — body fully covered in Japanese irezumi tattoos: blazing phoenix rising from ankles with wings fully spread across chest, deep black ink with electric crimson feather highlights. RIGHT: European VS Angel, mid-20s, slender curved physique — luminous fair skin — body fully covered in crimson and rose gold ultra-fine body glitter: fire gradient glitter coating every inch, glitter catching rain drops creating exploding spark effect. LEFT: transparent platform heels, long crimson nails. RIGHT: rose gold stiletto heels, long rose gold nails. Both: rain soaked, hair wind-blown. Environment: Tokyo Shibuya crossing at night in heavy rain, neon signs blazing red and pink, wet pavement doubling both women. Lighting: red-crimson neon edge glow — phoenix ink and glitter both catching identical crimson neon. Style: Balenciaga avant-garde rain duo editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, phoenix crimson rain grade, portrait 4:5 vertical.",
        "environment": "Tokyo Shibuya crossing at night in heavy rain",
        "lighting": "red-crimson neon edge glow",
        "style": "Balenciaga avant-garde rain duo editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },
    "duo_irezumi_koi_glitter_coral_maldives": {
        "subject": "Southeast Asian VS Angel + Mixed race athletic duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women side by side. LEFT: Southeast Asian beauty, mid-20s, VS Angel body — warm golden skin — body fully covered in Japanese irezumi tattoos: enormous koi fish swimming upward across entire body, brilliant crimson and gold scale highlights, maple leaves swirling around hips. RIGHT: Mixed race beauty, mid-20s, athletic curved physique — luminous warm skin — body fully covered in coral and rose gold ultra-fine body glitter: tropical sunset gradient glitter from coral at ankles to rose gold at shoulders, bioluminescent micro-dots scattered across collarbone. LEFT: barefoot, long coral nails. RIGHT: nude stiletto heels, long rose gold nails. Both: tropical flowers in hair, full body oil. Environment: Maldives overwater bungalow at sunset, turquoise lagoon, coral reef visible below crystal water. Lighting: Maldives golden hour — koi crimson scales and coral glitter both catching identical warm sunset. Style: Valentino tropical luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, koi coral maldives duo grade, portrait 4:5 vertical.",
        "environment": "Maldives overwater bungalow at sunset",
        "lighting": "Maldives golden hour warm backlight",
        "style": "Valentino tropical luxury duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_irezumi_snake_glitter_emerald_versailles": {
        "subject": "European MILF + Middle Eastern super glamour duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women facing each other, hands almost touching. LEFT: European MILF goddess, early 30s, voluptuous mature curves — luminous fair skin — body fully covered in Japanese irezumi tattoos: massive coiling snake wrapping entire body with obsessive scale detail, deep black ink with emerald green accent highlights, snake head rising at collarbone. RIGHT: Middle Eastern beauty, mid-20s, super glamour hourglass — olive skin — body fully covered in emerald and forest green ultra-fine body glitter: jewel-tone emerald glitter coating every inch, glitter so dense skin reads as living malachite, gold micro-flecks scattered throughout. LEFT: emerald stiletto heels, long emerald nails. RIGHT: gold stiletto heels, long gold nails. Both: elaborate gold hair accessories, full body oil. Environment: Palace of Versailles Hall of Mirrors, golden chandeliers, baroque grandeur, mirror reflections multiplying both women infinitely. Lighting: warm chandelier gold — emerald snake ink and emerald glitter both catching identical baroque light, mirrors reflecting the green duality endlessly. Style: Versace baroque luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, snake emerald versailles duo grade, portrait 4:5 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "warm golden chandelier light",
        "style": "Versace baroque luxury duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_peacock_glitter_teal_monaco": {
        "subject": "Japanese mature + Colombian Latina duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side on Monaco terrace. LEFT: Japanese mature beauty, early 30s, graceful sophisticated curves — luminous warm skin — body fully covered in Japanese irezumi tattoos: magnificent peacock spreading full plumage across chest and back, wisteria vines cascading down arms and legs, deep black ink with electric teal and violet peacock eye highlights. RIGHT: Colombian Latina goddess, mid-20s, curvaceous reggaeton physique — warm caramel skin — body fully covered in electric teal and peacock blue ultra-fine body glitter: iridescent teal glitter coating every inch, shifting teal-violet-gold with every movement. LEFT: teal stiletto heels, long teal nails. RIGHT: gold platform heels, long violet nails. Both: sleek updos with gold accessories, full body oil. Environment: Monaco luxury terrace at night, Mediterranean harbor lights, superyachts, city glow. Lighting: Monaco warm nightscape — peacock teal ink and teal glitter both catching harbor light in identical spectrum. Style: Dolce & Gabbana Mediterranean luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, peacock teal monaco duo grade, portrait 4:5 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco warm nightscape rim lighting",
        "style": "Dolce & Gabbana Mediterranean luxury duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_skull_glitter_obsidian_kyoto": {
        "subject": "European runway + Korean runway dark duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women walking through rain side by side. LEFT: European runway goddess, early 20s, 185cm+ slim runway physique — porcelain pale skin — body fully covered in Japanese irezumi tattoos: dark skull and chrysanthemum motif covering entire body, deep black ink with deep violet accent highlights, skulls on chest and hips, chrysanthemums filling every gap. RIGHT: Korean beauty, early 20s, slim runway physique — ethereal pale skin — body fully covered in obsidian black and deep violet ultra-fine body glitter: dark glitter coating every inch with violet bioluminescent micro-dots, skin reading as living dark cosmos. LEFT: black platform heels, long violet nails. RIGHT: black stiletto heels, long black nails. Both: severe architectural updos, full body oil, rain soaked. Environment: Kyoto ancient temple path in heavy rain, stone lanterns, bamboo, mist, deep night atmosphere. Lighting: cool blue-violet rain light — skull ink and obsidian glitter both absorbing and refracting identical violet tones. Style: Alexander McQueen dark editorial duo. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, skull obsidian kyoto rain duo grade, portrait 4:5 vertical.",
        "environment": "Kyoto ancient temple path in heavy rain",
        "lighting": "cool blue-violet rain light",
        "style": "Alexander McQueen dark editorial duo",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_irezumi_samurai_glitter_silver_tokyo": {
        "subject": "Japanese athletic + Scandinavian VS Angel duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side facing camera. LEFT: Japanese beauty, mid-20s, athletic toned physique — luminous warm skin — body fully covered in Japanese irezumi tattoos: samurai armor pattern covering entire body in obsessive detail, lacquer black and deep red ink with silver metallic highlights, armor chest plate across torso, scale patterns down both legs. RIGHT: Scandinavian VS Angel, mid-20s, slender ethereal physique — porcelain fair skin — body fully covered in pure platinum silver ultra-fine body glitter: mirror-finish silver glitter coating every inch, skin reading as liquid chrome. LEFT: red stiletto heels, long silver nails. RIGHT: silver stiletto heels, long platinum nails. Both: sleek severe updos, full body oil. Environment: Tokyo Shibuya at night, neon reflections on wet pavement. Lighting: multi-colored neon — samurai silver ink and platinum glitter both amplifying neon spectrum, wet pavement below doubling both women. Style: Balenciaga power editorial duo. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, samurai silver tokyo duo grade, portrait 4:5 vertical.",
        "environment": "Tokyo Shibuya at night wet pavement",
        "lighting": "multi-colored neon reflection",
        "style": "Balenciaga power editorial duo",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },

    # ── 배치 2: 이레즈미×바디페인팅 ──────────────────────────────────────────
    "duo_irezumi_dragon_klimt_versailles": {
        "subject": "Black African goddess + Middle Eastern super glamour duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women facing camera side by side. LEFT: Black African goddess, mid-20s, Black glamour hourglass physique — deep rich skin — body fully covered in Japanese irezumi tattoos: massive dragon coiling entire body with obsessive gold and black ink detail, flames erupting from shoulders. RIGHT: Middle Eastern super glamour goddess, late 20s, ultra-voluptuous curves — olive luminous skin — body fully covered in Klimt gold body paint: intricate 24K gold leaf Art Nouveau patterns coating entire body, geometric Byzantine motifs across chest and hips, gold so dense skin becomes living mosaic. LEFT: gold platform heels, long gold nails. RIGHT: gold stiletto heels, long gold nails. Both: sleek architectural updos, full body high-gloss oil. Environment: Palace of Versailles Hall of Mirrors, golden chandeliers blazing, baroque grandeur. Lighting: warm chandelier gold — dragon gold ink left and Klimt gold paint right catching identical baroque light, mirrors multiplying both women endlessly. Style: Versace ultra-luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, dragon klimt versailles duo grade, portrait 4:5 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "warm golden chandelier light",
        "style": "Versace ultra-luxury duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_phoenix_vangogh_aurora": {
        "subject": "European fitness goddess + Scandinavian VS Angel duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing back to back on Iceland glacier. LEFT facing camera: European fitness goddess, mid-20s, powerful muscular definition — fair skin — body fully covered in Japanese irezumi tattoos: blazing phoenix rising from ankles with wings fully spread across chest and shoulders, deep black ink with electric crimson and violet feather highlights amplifying every muscle. RIGHT facing away: Scandinavian VS Angel, mid-20s, slender ethereal physique — porcelain fair skin — body fully covered in Van Gogh Starry Night body paint: swirling cobalt blue and gold impasto brushstrokes coating entire back from neck to ankles, night sky spirals following every graceful contour. LEFT: black stiletto heels, long crimson nails. RIGHT: black stiletto heels, long cobalt nails. Both: wind-blown hair, full body oil. Environment: Iceland glacier field at night, northern lights aurora exploding across vast dark sky. Lighting: aurora borealis bathing both — crimson phoenix ink catching violet aurora left, Van Gogh cobalt swirls merging with aurora right. Style: Alexander McQueen dramatic duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, phoenix vangogh aurora duo grade, portrait 4:5 vertical.",
        "environment": "Iceland glacier field at night, northern lights aurora",
        "lighting": "aurora borealis violet and green curtain",
        "style": "Alexander McQueen dramatic duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_irezumi_wave_pollock_void": {
        "subject": "Korean runway goddess + Colombian Latina duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women side by side facing camera. LEFT: Korean runway goddess, early 20s, 185cm+ slim runway physique — ethereal pale skin — body fully covered in Japanese irezumi tattoos: explosive Great Wave crashing across entire body with electric indigo and black ink, Mount Fuji silhouette on chest. RIGHT: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — warm caramel skin — body fully covered in Pollock action painting body paint: chaotic drip and splatter of electric cyan, magenta, gold across every inch of body, paint splashes following powerful curves. LEFT: transparent platform heels, long indigo nails. RIGHT: gold stiletto heels, long gold nails. Both: sleek updos, full body oil. Environment: pure black void, seamless obsidian backdrop. Lighting: dual cold-warm spotlight — cool blue on wave indigo ink left, warm gold on Pollock splatter right — black void making both body arts explode with maximum contrast. Style: Balenciaga avant-garde duo void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, wave pollock void duo grade, portrait 4:5 vertical.",
        "environment": "pure black void",
        "lighting": "dual cold-warm spotlight",
        "style": "Balenciaga avant-garde duo void editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_koi_klimt_silver_budapest": {
        "subject": "Japanese mature + European MILF duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Japanese mature beauty, early 30s, graceful sophisticated curves — luminous warm skin — body fully covered in Japanese irezumi tattoos: enormous koi fish swimming upward across entire body, brilliant crimson and gold scale highlights, cherry blossoms filling every gap. RIGHT: European MILF goddess, early 30s, voluptuous mature curves — luminous fair skin — body fully covered in Klimt silver body paint: intricate silver leaf Art Nouveau patterns coating entire body, flowing organic lines across chest and hips, silver-grey and white creating ethereal moonlight mosaic. LEFT: gold stiletto heels, long gold nails. RIGHT: silver stiletto heels, long silver nails. Both: elaborate hair accessories, full body oil, steam rising. Environment: Budapest thermal bath, mineral steam rising, classical stone columns, candlelight. Lighting: warm amber candlelight — koi crimson and gold scales blazing left, silver Klimt patterns catching candlelight right. Style: Harper's Bazaar mature luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, koi klimt budapest duo grade, portrait 4:5 vertical.",
        "environment": "Budapest thermal bath mineral steam",
        "lighting": "warm amber candlelight",
        "style": "Harper's Bazaar mature luxury duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_irezumi_snake_mucha_paris": {
        "subject": "European runway + Korean ballerina duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women facing each other on Paris rooftop, hands almost touching. LEFT: European runway goddess, early 20s, 185cm+ slim runway physique — porcelain pale skin — body fully covered in Japanese irezumi tattoos: elegant serpent coiling from ankles to neck with obsessive scale detail, deep black ink with soft violet accent highlights, lotus flowers filling every gap. RIGHT: Korean ballerina, early 20s, slender elongated physique — porcelain pale skin — body fully covered in Mucha Art Nouveau body paint: flowing organic decorative patterns coating entire body in warm gold and blush tones, ornate botanical borders around shoulders and hips. LEFT: transparent heels, long violet nails. RIGHT: rose gold pointe shoes, long blush nails. Both: elaborate hair ornaments, full body oil. Environment: Paris rooftop at blue hour, Eiffel Tower glittering in distance, warm amber city glow below cool blue sky. Lighting: Paris blue hour — snake violet ink catching cool blue ambient left, Mucha warm gold catching amber city glow right. Style: Chanel romantic luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, snake mucha paris duo grade, portrait 4:5 vertical.",
        "environment": "Paris rooftop at blue hour Eiffel Tower",
        "lighting": "Paris blue hour cool ambient and amber city glow",
        "style": "Chanel romantic luxury duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_peacock_kandinsky_monaco": {
        "subject": "Japanese mature + Middle Eastern super glamour duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side on Monaco terrace. LEFT: Japanese mature beauty, early 30s, graceful sophisticated curves — luminous warm skin — body fully covered in Japanese irezumi tattoos: magnificent peacock spreading full plumage across chest and back, wisteria cascading down both arms and legs, electric teal and violet ink. RIGHT: Middle Eastern beauty, mid-20s, super glamour hourglass — olive skin — body fully covered in Kandinsky abstract body paint: bold geometric circles and dynamic lines coating entire body in electric teal, cobalt, crimson and gold. LEFT: teal stiletto heels, long teal nails. RIGHT: gold platform heels, long cobalt nails. Both: sleek updos with gold accessories, full body oil. Environment: Monaco luxury terrace at night, Mediterranean harbor lights. Lighting: Monaco warm nightscape — peacock teal ink and Kandinsky teal geometry both catching harbor light in identical spectrum. Style: Versace Mediterranean luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, peacock kandinsky monaco duo grade, portrait 4:5 vertical.",
        "environment": "Monaco luxury terrace at night",
        "lighting": "Monaco warm nightscape harbor lights",
        "style": "Versace Mediterranean luxury duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_skull_dali_kyoto": {
        "subject": "European runway + Scandinavian VS Angel dark surrealist duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women walking side by side through Kyoto rain. LEFT: European runway goddess, early 20s, 185cm+ slim runway physique — porcelain pale skin — body fully covered in Japanese irezumi tattoos: skull and chrysanthemum motif covering entire body, deep black ink with deep violet accent, skulls on chest and hips. RIGHT: Scandinavian VS Angel, mid-20s, slender ethereal physique — luminous fair skin — body fully covered in Salvador Dalí surrealist body paint: melting clocks dripping across shoulders, distorted dreamscape figures across torso, desert landscapes on legs, deep ochre and violet surreal tones. LEFT: black platform heels, long violet nails. RIGHT: silver heels, long silver nails. Both: severe architectural updos, rain soaked, full body oil. Environment: Kyoto ancient temple path in heavy rain, stone torii gates, bamboo forest, stone lanterns. Lighting: cool blue-violet rain light — skull violet ink and Dalí violet surreal paint both catching identical cold light, rain drops catching violet across both women. Style: Alexander McQueen dark surrealist duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, skull dali kyoto rain duo grade, portrait 4:5 vertical.",
        "environment": "Kyoto ancient temple path in heavy rain torii gates",
        "lighting": "cool blue-violet rain light",
        "style": "Alexander McQueen dark surrealist duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },

    # ── 배치 3: 글리터×바디페인팅 ─────────────────────────────────────────────
    "duo_glitter_gold_klimt_void": {
        "subject": "Black African goddess gold glitter + Middle Eastern black Klimt duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women side by side facing camera. LEFT: Black African goddess, mid-20s, Black glamour hourglass physique — deep rich skin — body fully covered in 24K gold ultra-fine body glitter: maximum density gold coating every inch, liquid molten gold effect, every powerful curve blazing. RIGHT: Middle Eastern super glamour goddess, late 20s, ultra-voluptuous curves — olive luminous skin — body fully covered in Klimt body paint in deep charcoal and black tones with gold line work: photographic negative Klimt effect, Art Nouveau patterns coating entire body. LEFT: gold stiletto heels, long gold nails. RIGHT: black stiletto heels, long black nails. Both: sleek architectural updos, full body oil. Environment: pure black void, seamless obsidian backdrop. Lighting: single dramatic overhead spotlight splitting — warm gold blazing on glitter left, cool silver on Klimt black right — gold and black Klimt in perfect cosmic duality. Style: Vogue Italia cosmic duality void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, gold klimt void duality grade, portrait 4:5 vertical.",
        "environment": "pure black void",
        "lighting": "single dramatic overhead spotlight splitting gold and silver",
        "style": "Vogue Italia cosmic duality void editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_glitter_crimson_vangogh_aurora": {
        "subject": "Colombian Latina crimson glitter + European VS Angel Starry Night duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing back to back on Iceland glacier. LEFT facing camera: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — warm caramel skin — body fully covered in deep crimson and ruby red ultra-fine body glitter: fire gradient glitter from deep burgundy at ankles blazing to scarlet at shoulders, every powerful curve a living ember. RIGHT facing away: European VS Angel, mid-20s, slender curved physique — porcelain fair skin — body fully covered in Van Gogh Starry Night body paint: swirling cobalt blue and gold impasto brushstrokes coating entire back from neck to ankles, night sky spirals following every graceful curve. LEFT: crimson stiletto heels, long crimson nails. RIGHT: black stiletto heels, long cobalt nails. Both: wind-blown hair, full body oil. Environment: Iceland glacier field at night, northern lights aurora exploding in violet, green, teal. Lighting: aurora borealis — crimson glitter catching warm violet aurora left creating living fire, Van Gogh cobalt swirls merging with aurora sky right. Style: Alexander McQueen dramatic duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, crimson vangogh aurora duo grade, portrait 4:5 vertical.",
        "environment": "Iceland glacier field at night northern lights aurora",
        "lighting": "aurora borealis violet and teal",
        "style": "Alexander McQueen dramatic duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_glitter_silver_pollock_shibuya": {
        "subject": "Korean runway silver glitter + Black African fitness Pollock duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women walking toward camera in heavy rain. LEFT: Korean runway goddess, early 20s, 185cm+ slim runway physique — ethereal pale skin — body fully covered in pure platinum silver ultra-fine body glitter: mirror-finish silver coating every inch, skin crystallized moonlight. RIGHT: Black African fitness goddess, mid-20s, powerful muscular definition — deep rich skin — body fully covered in Pollock action painting body paint: chaotic drip and splatter of electric silver, white, and electric blue across deep skin, paint following every muscle contour. LEFT: silver platform heels, long silver nails. RIGHT: silver stiletto heels, long silver nails. Both: severe updos, rain soaked. Environment: Tokyo Shibuya crossing at night in heavy rain, neon signs, wet pavement doubling both women. Lighting: cool silver-white neon edge glow — platinum glitter and Pollock silver drips both catching identical neon. Style: Balenciaga avant-garde rain duo editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, silver pollock shibuya duo grade, portrait 4:5 vertical.",
        "environment": "Tokyo Shibuya crossing at night in heavy rain",
        "lighting": "cool silver-white neon edge glow",
        "style": "Balenciaga avant-garde rain duo editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },
    "duo_glitter_teal_mucha_maldives": {
        "subject": "Scandinavian teal glitter + Japanese ballerina Mucha duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Scandinavian VS Angel, mid-20s, slender ethereal physique — luminous fair skin — body fully covered in deep ocean teal and aquamarine ultra-fine body glitter: tropical sea gradient from deep teal at ankles shifting to bright aquamarine at shoulders, bioluminescent micro-dots scattered like underwater stars. RIGHT: Japanese ballerina, early 20s, slender elongated physique — warm luminous skin — body fully covered in Mucha Art Nouveau body paint: flowing organic botanical patterns coating entire body in warm ivory and gold tones, water lily motifs across chest and hips. LEFT: barefoot, long teal nails. RIGHT: rose gold pointe shoes, long blush nails. Both: tropical flowers in hair, full body oil. Environment: Maldives overwater bungalow at sunset, turquoise lagoon, coral reef visible below crystal water. Lighting: Maldives golden hour — teal glitter catching turquoise water reflections, Mucha warm gold catching amber sunset. Style: Valentino tropical luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, teal mucha maldives duo grade, portrait 4:5 vertical.",
        "environment": "Maldives overwater bungalow at sunset turquoise lagoon",
        "lighting": "Maldives golden hour warm backlight",
        "style": "Valentino tropical luxury duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_glitter_obsidian_dali_versailles": {
        "subject": "European fitness obsidian constellation glitter + Colombian Dali duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women facing each other, hands almost touching. LEFT: European fitness goddess, mid-20s, powerful muscular definition — fair skin — body fully covered in jet obsidian black ultra-fine body glitter with gold constellation micro-dots: deep space black glitter coating every inch, gold star-map patterns mapping constellations across collarbone and muscle contours. RIGHT: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — warm caramel skin — body fully covered in Salvador Dalí surrealist body paint: melting clocks dripping across powerful shoulders, dreamscape desert landscapes on torso, distorted perspective figures on legs, deep ochre and violet surreal tones. LEFT: black stiletto heels, long black nails. RIGHT: gold platform heels, long gold nails. Both: elaborate gold hair accessories, full body oil. Environment: Palace of Versailles Hall of Mirrors, golden chandeliers, baroque grandeur, mirror reflections multiplying both women. Lighting: warm chandelier gold — obsidian glitter absorbing light left creating anti-chandelier darkness, Dalí ochre blazing right in baroque warmth. Style: Versace surrealist luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian dali versailles duo grade, portrait 4:5 vertical.",
        "environment": "Palace of Versailles Hall of Mirrors",
        "lighting": "warm golden chandelier light baroque",
        "style": "Versace surrealist luxury duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_glitter_violet_kandinsky_kyoto": {
        "subject": "Japanese mature violet glitter + Scandinavian Kandinsky duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women walking side by side through Kyoto rain. LEFT: Japanese mature beauty, early 30s, graceful sophisticated curves — luminous warm skin — body fully covered in deep violet and amethyst ultra-fine body glitter: jewel-tone violet coating every inch, glitter shifting violet-purple-indigo with rain drops catching light as individual prisms. RIGHT: Scandinavian beauty, mid-20s, VS Angel body — porcelain fair skin — body fully covered in Kandinsky abstract body paint: bold geometric circles and dynamic lines coating entire body in electric violet, cobalt, crimson with gold accents. LEFT: violet stiletto heels, long violet nails. RIGHT: gold heels, long cobalt nails. Both: severe architectural updos, rain soaked, full body oil. Environment: Kyoto ancient temple path in heavy rain, stone torii gates, bamboo forest, stone lanterns. Lighting: cool violet rain light — amethyst glitter and Kandinsky violet geometry both catching identical cool tones, lanterns providing warm counterpoint. Style: Alexander McQueen dark luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, violet kandinsky kyoto duo grade, portrait 4:5 vertical.",
        "environment": "Kyoto ancient temple path in heavy rain torii gates bamboo",
        "lighting": "cool violet rain light with warm lantern counterpoint",
        "style": "Alexander McQueen dark luxury duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_glitter_emerald_vangogh_budapest": {
        "subject": "Brazilian fitness emerald glitter + European MILF Van Gogh Almond Blossom duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Brazilian fitness goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in deep emerald and forest green ultra-fine body glitter: jewel-tone emerald coating every inch, gold micro-flecks scattered throughout, every muscle contour a living malachite sculpture. RIGHT: European MILF goddess, early 30s, voluptuous mature curves — luminous fair skin — body fully covered in Van Gogh Almond Blossom body paint: delicate white and pale blue blossoms coating entire body, dark branch structures following mature curves, painterly impasto texture creating living botanical garden. LEFT: gold stiletto heels, long emerald nails. RIGHT: silver stiletto heels, long white nails. Both: elaborate hair accessories, full body oil, steam rising. Environment: Budapest thermal bath, mineral steam rising, classical stone columns, warm candlelight. Lighting: warm amber candlelight — emerald glitter blazing warm gold left, Van Gogh pale blossoms catching amber glow right — steam fog creating dreamy botanical unity. Style: Harper's Bazaar mature luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, emerald vangogh budapest duo grade, portrait 4:5 vertical.",
        "environment": "Budapest thermal bath mineral steam candlelight",
        "lighting": "warm amber candlelight with steam fog",
        "style": "Harper's Bazaar mature luxury duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },

    # ── 기존 검증 5종 ─────────────────────────────────────────────────────────
    "duo_irezumi_glitter_aurora": {
        "subject": "Scandinavian wave irezumi + Japanese glitter aurora back-to-back duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women standing back to back. LEFT facing camera: Scandinavian VS Angel beauty, early 20s, slender ethereal physique — porcelain fair skin — body fully covered in Japanese irezumi tattoos: Great Wave and Mount Fuji across entire body with electric violet ink highlights glowing against fair skin. RIGHT facing away: Japanese beauty, early 20s, ballerina physique — luminous warm skin — body fully covered in iridescent silver and violet body glitter: ultra-fine glitter coating entire back from neck to ankles like liquid aurora. Both: rose gold satin pointe shoes, long violet almond nails. Environment: Iceland glacier at night, northern lights aurora exploding across sky. Lighting: aurora borealis violet and green curtain bathing both women. Style: Alexander McQueen dramatic romantic editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora twin grade, portrait 4:5 vertical.",
        "environment": "Iceland glacier at night northern lights aurora",
        "lighting": "aurora borealis violet and green",
        "style": "Alexander McQueen dramatic romantic editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
    "duo_irezumi_snake_dragon_monaco": {
        "subject": "European MILF snake irezumi + Middle Eastern dragon irezumi Monaco duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women facing each other, bodies angled in, hands almost touching. LEFT: European MILF goddess, early 30s, voluptuous mature curves — luminous fair skin — body fully covered in Japanese irezumi tattoos: massive coiling SNAKE wrapping entire body with obsessive scale detail, deep black ink with crimson red accent highlights, snake head rising at collarbone fangs bared. RIGHT: Middle Eastern beauty, mid-20s, super glamour hourglass — olive luminous skin — body fully covered in Japanese irezumi tattoos: massive DRAGON wrapping entire body with gold and deep black ink, dragon claw reaching across hip. LEFT: gold stiletto heels, long crimson stiletto nails. RIGHT: gold platform heels, long gold stiletto nails. Both: full body high-gloss oil. Environment: Monaco luxury terrace at night, Mediterranean harbor superyachts. Lighting: dramatic warm Monaco nightscape rim backlight — crimson snake ink blazing left, gold dragon ink blazing right. Style: Versace ultra-luxury power duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, snake dragon monaco duality grade, portrait 4:5 vertical.",
        "environment": "Monaco luxury terrace at night Mediterranean harbor",
        "lighting": "dramatic warm Monaco nightscape rim backlight",
        "style": "Versace ultra-luxury power duo editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_irezumi_wave_phoenix_shibuya": {
        "subject": "Korean wave irezumi + Black African phoenix irezumi Shibuya rain duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women walking toward camera side by side, wet pavement reflections doubling their bodies below. LEFT: Korean runway goddess, early 20s, 185cm+ slim runway physique — ethereal pale skin — body fully covered in Japanese irezumi tattoos: explosive Great Wave crashing across entire body with electric cyan ink, Mount Fuji glowing neon on chest. RIGHT: Black African goddess, mid-20s, power fitness physique — deep rich skin — body fully covered in Japanese irezumi tattoos: blazing Phoenix rising from ankles to shoulders with wings spread across chest, deep black ink with electric crimson and gold feather highlights. LEFT: transparent platform heels, long cyan stiletto nails. RIGHT: black stiletto heels, long gold stiletto nails. Both: sleek architectural updos, full body oil, rain soaked. Environment: Tokyo Shibuya crossing at night in heavy rain, neon signs reflecting in wet pavement. Lighting: multi-colored neon cyan and crimson edge glow — wave ink and phoenix ink each catching different neon colors. Style: Balenciaga avant-garde power duo editorial. Shot on Sony A7R V 50mm f/1.4 ISO 100, 8K UHD, wave phoenix shibuya rain grade, portrait 4:5 vertical.",
        "environment": "Tokyo Shibuya crossing at night in heavy rain",
        "lighting": "multi-colored neon cyan and crimson edge glow",
        "style": "Balenciaga avant-garde power duo editorial",
        "quality": "Sony A7R V 50mm f/1.4 ISO 100, 8K UHD"
    },
    "duo_glitter_gold_obsidian_void": {
        "subject": "Black African gold glitter + Scandinavian obsidian black glitter void duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women facing camera, bodies pressed together, inside arms intertwined. LEFT: Black African goddess, mid-20s, Black glamour hourglass physique — deep rich skin — body fully covered in 24K gold ultra-fine body glitter: maximum density gold coating every inch creating liquid molten gold effect. RIGHT: Scandinavian VS Angel beauty, mid-20s, slender ethereal physique — porcelain fair skin — body fully covered in jet black ultra-fine body glitter: obsidian black micro-glitter coating every inch with silver constellation micro-dots. Both: barefoot, LEFT gold long stiletto nails, RIGHT silver long stiletto nails, full body oil. Environment: pure black void, seamless obsidian backdrop. Lighting: single overhead dramatic spotlight splitting center — LEFT warm gold light making gold glitter blaze like sun, RIGHT cold silver moonlight making black glitter reveal constellation depth. Style: Vogue Italia duality goddess editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, gold obsidian goddess void grade, portrait 4:5 vertical.",
        "environment": "pure black void",
        "lighting": "single overhead spotlight splitting warm gold and cold silver",
        "style": "Vogue Italia duality goddess editorial",
        "quality": "Hasselblad H6D 80mm f/2.8, 8K UHD"
    },
    "duo_glitter_fire_ice_cape_town": {
        "subject": "Colombian fire glitter + Japanese ice glitter Cape Town duo",
        "prompt": "Professional fashion photograph, full body shot. TWO women back to back, both looking outward over Atlantic horizon. LEFT: Colombian Latina goddess, mid-20s, Colombian reggaeton physique — warm caramel skin — body fully covered in crimson red and molten orange ultra-fine body glitter: fire gradient from deep crimson at ankles fading to blazing orange at shoulders, every powerful curve blazing like lava. RIGHT: Japanese beauty, early 20s, ballerina physique — luminous warm skin — body fully covered in ice blue and silver ultra-fine body glitter: glacier blue at ankles fading to silver-white at shoulders, glitter coating so fine skin looks crystallized. LEFT: gold stiletto heels, long crimson stiletto nails. RIGHT: silver stiletto heels, long ice blue almond nails. Both: full body oil, hair wind-blown dramatically. Environment: Cape Town clifftop at dramatic sunset, Table Mountain silhouette, Atlantic Ocean crashing below, blazing orange and deep purple sky splitting perfectly. Lighting: sunset splits perfectly — LEFT warm orange sunset light making fire glitter erupt, RIGHT cool blue shadow making ice glitter crystallize. Style: Vogue Italia high-fashion dramatic duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, fire ice duality cape town grade, portrait 4:5 vertical.",
        "environment": "Cape Town clifftop at dramatic sunset Table Mountain",
        "lighting": "sunset splits warm orange left and cool blue shadow right",
        "style": "Vogue Italia high-fashion dramatic duo editorial",
        "quality": "Phase One XF IQ4 110mm f/2.8, 8K UHD"
    },
}

# ── HOF / SS 분류 ─────────────────────────────────────────────────────────────

HOF_KEYS = {
    # 배치1 HOF
    "duo_irezumi_dragon_glitter_gold_void",
    "duo_irezumi_wave_glitter_indigo_santorini",
    "duo_irezumi_snake_glitter_emerald_versailles",
    "duo_irezumi_skull_glitter_obsidian_kyoto",
    # 배치2 HOF
    "duo_irezumi_phoenix_vangogh_aurora",
    "duo_irezumi_wave_pollock_void",
    "duo_irezumi_koi_klimt_silver_budapest",
    "duo_irezumi_snake_mucha_paris",
    "duo_irezumi_skull_dali_kyoto",
    # 배치3 HOF
    "duo_glitter_gold_klimt_void",
    "duo_glitter_crimson_vangogh_aurora",
    "duo_glitter_teal_mucha_maldives",
    "duo_glitter_obsidian_dali_versailles",
    "duo_glitter_violet_kandinsky_kyoto",
    "duo_glitter_emerald_vangogh_budapest",
    # 기존 검증 HOF
    "duo_irezumi_glitter_aurora",
    "duo_irezumi_snake_dragon_monaco",
    "duo_irezumi_wave_phoenix_shibuya",
    "duo_glitter_gold_obsidian_void",
    "duo_glitter_fire_ice_cape_town",
}

SS_KEYS = {
    "duo_irezumi_phoenix_glitter_crimson_shibuya",
    "duo_irezumi_koi_glitter_coral_maldives",
    "duo_irezumi_peacock_glitter_teal_monaco",
    "duo_irezumi_samurai_glitter_silver_tokyo",
    "duo_irezumi_dragon_klimt_versailles",
    "duo_irezumi_peacock_kandinsky_monaco",
    "duo_glitter_silver_pollock_shibuya",
}

# ── presets_meta.py 카테고리 블록 ─────────────────────────────────────────────

ALL_KEYS = list(PRESETS.keys())

META_BLOCK = '''
# 2026-07-18 ✨ Bare Art Ensemble 카테고리 신설 (듀오 25종)
PRESETS_BARE_ART_ENSEMBLE_DUO = {
''' + ''.join(f'    "{k}": {{}},\n' for k in ALL_KEYS) + '''}
'''

CATEGORY_ENTRY = '''
    "✨ Bare Art Ensemble": [
        # 듀오 — 이레즈미×글리터
        "duo_irezumi_dragon_glitter_gold_void",
        "duo_irezumi_wave_glitter_indigo_santorini",
        "duo_irezumi_phoenix_glitter_crimson_shibuya",
        "duo_irezumi_koi_glitter_coral_maldives",
        "duo_irezumi_snake_glitter_emerald_versailles",
        "duo_irezumi_peacock_glitter_teal_monaco",
        "duo_irezumi_skull_glitter_obsidian_kyoto",
        "duo_irezumi_samurai_glitter_silver_tokyo",
        # 듀오 — 이레즈미×바디페인팅
        "duo_irezumi_dragon_klimt_versailles",
        "duo_irezumi_phoenix_vangogh_aurora",
        "duo_irezumi_wave_pollock_void",
        "duo_irezumi_koi_klimt_silver_budapest",
        "duo_irezumi_snake_mucha_paris",
        "duo_irezumi_peacock_kandinsky_monaco",
        "duo_irezumi_skull_dali_kyoto",
        # 듀오 — 글리터×바디페인팅
        "duo_glitter_gold_klimt_void",
        "duo_glitter_crimson_vangogh_aurora",
        "duo_glitter_silver_pollock_shibuya",
        "duo_glitter_teal_mucha_maldives",
        "duo_glitter_obsidian_dali_versailles",
        "duo_glitter_violet_kandinsky_kyoto",
        "duo_glitter_emerald_vangogh_budapest",
        # 기존 검증
        "duo_irezumi_glitter_aurora",
        "duo_irezumi_snake_dragon_monaco",
        "duo_irezumi_wave_phoenix_shibuya",
        "duo_glitter_gold_obsidian_void",
        "duo_glitter_fire_ice_cape_town",
    ],
'''

# ── 실행 ─────────────────────────────────────────────────────────────────────

def step1_create_jsons():
    print("=== Step 1: JSON 파일 생성 ===")
    created = 0
    for key, data in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{key}.json")
        if os.path.exists(path):
            print(f"  SKIP: {key}.json")
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  CREATED: {key}.json")
        created += 1
    print(f"  총 {created}개 생성\n")


def step2_patch_meta():
    print("=== Step 2: presets_meta.py 패치 ===")
    with open(META_PATH, "r", encoding="utf-8-sig") as f:
        content = f.read()

    if "Bare Art Ensemble" in content:
        print("  이미 패치됨 — SKIP\n")
        return

    # PRESET_CATEGORIES 딕셔너리 마지막 } 앞에 카테고리 항목 삽입
    # 파일 끝에 별도 딕셔너리 추가
    with open(META_PATH, "a", encoding="utf-8") as f:
        f.write("\n" + META_BLOCK)

    # PRESET_CATEGORIES 안에 카테고리 키 추가
    # 마지막 } 찾아서 앞에 삽입
    with open(META_PATH, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # PRESET_CATEGORIES 딕셔너리의 마지막 닫는 } 앞에 카테고리 삽입
    target = '"🫧 Mycelium Glamour":'
    if target in content and "Bare Art Ensemble" not in content:
        # Mycelium Glamour 블록 끝 찾기 — 그 뒤에 추가
        insert_pos = content.rfind("\n}")  # 마지막 } 앞
        new_content = content[:insert_pos] + "\n" + CATEGORY_ENTRY + content[insert_pos:]
        with open(META_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("  ✨ Bare Art Ensemble 카테고리 추가 완료\n")
    else:
        print("  카테고리 삽입 위치 탐색 실패 — 수동 추가 필요\n")


def step3_patch_hof():
    print("=== Step 3: hof_tier.py 패치 ===")
    with open(HOF_PATH, "r", encoding="utf-8-sig") as f:
        content = f.read()

    new_keys = [k for k in HOF_KEYS if f'"{k}"' not in content]
    if not new_keys:
        print("  이미 모든 HOF 키 존재 — SKIP\n")
        return

    insert_block = "\n    # 2026-07-18 Bare Art Ensemble 듀오 HOF\n"
    for k in sorted(new_keys):
        insert_block += f'    "{k}",\n'

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
    print("=== Step 5: 파일 수 확인 ===")
    duo = len([f for f in os.listdir(PRESETS_DIR) if f.startswith("duo_")])
    total = len([f for f in os.listdir(PRESETS_DIR) if f.endswith(".json")])
    print(f"  duo_*.json     : {duo}개")
    print(f"  presets/ 전체  : {total}개\n")


if __name__ == "__main__":
    step1_create_jsons()
    step2_patch_meta()
    step3_patch_hof()
    step4_validate()
    step5_count()
    print("=== 완료 — git add / commit / push 진행하세요 ===")
