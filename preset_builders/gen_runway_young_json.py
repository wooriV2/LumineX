# -*- coding: utf-8 -*-
import json, os

OUTPUT_DIR = "presets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRESETS = {
    # ── Runway Slim 19종 ──────────────────────────────────
    "runway_korean_slim_void_studio": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim runway figure, impossibly long legs and neck, mid-20s, Korean features, luminous porcelain skin, severe sleek center-part jet-black hair to mid-back, sharp editorial cheekbones, cold high fashion expression",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim runway figure, impossibly long legs and neck, mid-20s, Korean features, luminous porcelain skin, severe sleek center-part jet-black hair to mid-back, sharp editorial cheekbones, cold high fashion expression. Wearing: ultra-minimal white micro structured bodysuit, architectural panel construction barely covering slim extreme tall frame, white patent thigh-high platform stiletto boots 6-inch heel, single massive sculptural silver ear piece only. Environment: black infinity studio, single hard overhead spot, pure editorial void. Lighting: single hard overhead spot, extreme tall slim silhouette as white architectural form against void. Style: Korean runway 185cm+ void studio high fashion editorial. Shot on Hasselblad X2D, 8K UHD, void runway grade, portrait 2:3 vertical.",
        "environment": "black infinity studio",
        "lighting": "single hard overhead spot",
        "style": "Korean runway void studio editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD, void runway grade"
    },
    "runway_korean_slim_paris_window": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, luminous porcelain skin in Paris morning light, severe sleek center-part platinum-dyed hair",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs, mid-20s, Korean features, luminous porcelain skin in Paris morning light, severe sleek center-part platinum-dyed hair, sharp cheekbones, cold distant haute couture expression. Wearing: ultra-minimal ivory silk micro slip, spaghetti straps barely visible on slim frame, slip micro-length on extreme long legs, clear platform stiletto mules 6-inch on Paris parquet floor, single architectural pearl drop earring only. Environment: Haussmann Paris apartment, floor-to-ceiling tall French windows, zinc rooftops view, morning gold. Lighting: Paris morning gold from windows side-lighting extreme tall figure, ivory silk catching morning gold. Style: Korean runway 185cm+ Paris window haute couture editorial. Shot on Phase One XF IQ4, 8K UHD, Paris runway grade, portrait 2:3 vertical.",
        "environment": "Haussmann Paris apartment",
        "lighting": "Paris morning gold from windows",
        "style": "Korean runway Paris window haute couture editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_milan_catwalk": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, legs that never end, mid-20s, Korean features, porcelain skin, severe sleek center-part black hair razor-cut to jawline",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, legs that never end, mid-20s, Korean features, porcelain skin, severe sleek center-part black hair razor-cut to jawline, razor cheekbones, cold catwalk expression. Wearing: ultra-minimal black micro corset-structured runway top barely covering slim chest, black micro shorts high-cut maximum leg exposure on extreme long legs, black patent thigh-high platform stiletto boots 6-inch on Milan runway, single massive architectural chrome ear sculpture. Environment: Milan Fashion Week runway, white runway, fashion crowd both sides blur, designer backdrop, runway overhead spots. Lighting: runway overhead spots hard from above, porcelain skin in hard fashion light, extreme long legs endless on white runway. Style: Korean runway 185cm+ Milan catwalk micro editorial. Shot on Hasselblad X2D, 8K UHD, Milan runway grade, portrait 2:3 vertical.",
        "environment": "Milan Fashion Week runway",
        "lighting": "runway overhead spots hard from above",
        "style": "Korean runway Milan catwalk editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_tokyo_shibuya_rain": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs in Tokyo neon rain, mid-20s, Korean features, luminous porcelain skin in neon light, sleek silver-dyed center-part hair",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs in Tokyo neon rain, mid-20s, Korean features, luminous porcelain skin in neon light, sleek silver-dyed center-part hair, sharp cold editorial expression. Wearing: ultra-minimal holographic iridescent micro bodysuit, cut to maximum leg exposure on extreme long thighs, clear holographic thigh-high platform stiletto boots 6-inch in Shibuya puddles, single holographic ear cuff. Environment: Shibuya crossing midnight, full neon saturation, rain puddles reflecting rainbow below extreme long boots, crowds with umbrellas blurred. Lighting: full Shibuya neon rainbow + puddle reflection from below, porcelain skin in neon color wash, holographic bodysuit exploding every neon. Style: Korean runway 185cm+ Shibuya rain holographic editorial. Shot on Phase One XF IQ4, 8K UHD, Shibuya runway grade, portrait 2:3 vertical.",
        "environment": "Shibuya crossing midnight",
        "lighting": "full Shibuya neon rainbow + puddle reflection",
        "style": "Korean runway Shibuya rain holographic editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_dubai_penthouse": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, legs to the ceiling, late-20s, Korean features, warm honey-porcelain skin in Dubai gold",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, legs to the ceiling, late-20s, Korean features, warm honey-porcelain skin in Dubai gold, severe center-part platinum blonde hair, cold commanding expression. Wearing: ultra-minimal gold metallic micro string bikini top, tiny triangles on slim frame barely existing, matching micro thong, gold chrome thigh-high platform stiletto boots 6-inch on Dubai penthouse terrace, single gold architectural ear cuff. Environment: Dubai penthouse terrace, Burj Khalifa dominating frame, city blazing gold below, infinity pool edge reflecting Burj. Lighting: Burj Khalifa gold ambient from behind + pool reflection upward + hard key, honey-porcelain skin in Dubai gold. Style: Korean runway 185cm+ Dubai penthouse gold night editorial. Shot on Hasselblad X2D, 8K UHD, Dubai runway grade, portrait 2:3 vertical.",
        "environment": "Dubai penthouse terrace",
        "lighting": "Burj Khalifa gold ambient",
        "style": "Korean runway Dubai penthouse gold night editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_nyc_rooftop": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, warm porcelain skin, severe slicked-back jet-black hair",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, warm porcelain skin, severe slicked-back jet-black hair, sharp editorial expression cold as NYC night. Wearing: ultra-minimal black micro bikini, absolute minimum on slim tall frame, black patent thigh-high platform stiletto boots 6-inch on NYC rooftop, single diamond drop earring, diamond anklet. Environment: NYC rooftop at night, Empire State Building lit directly behind tall figure, Manhattan grid gold below, water tower silhouettes. Lighting: NYC city gold + Empire State spotlight from behind, porcelain skin in NYC warm gold. Style: Korean runway 185cm+ NYC rooftop night editorial. Shot on Phase One XF IQ4, 8K UHD, NYC runway grade, portrait 2:3 vertical.",
        "environment": "NYC rooftop at night",
        "lighting": "NYC city gold + Empire State spotlight",
        "style": "Korean runway NYC rooftop night editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_seoulforest_spring": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, early-20s, Korean features, natural luminous porcelain skin in spring dappled light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, early-20s, Korean features, natural luminous porcelain skin in spring dappled light, severe sleek center-part dark hair, expression cool and distant in spring forest. Wearing: ultra-minimal white sheer micro dress, completely see-through fabric barely covering slim tall frame, visible micro white bikini underneath through sheer, clear platform stiletto mules 6-inch on forest path, single cherry blossom pin in hair. Environment: Seoul Forest in full spring bloom, cherry and forsythia in bloom, dappled spring light through young leaves, forest path. Lighting: spring forest dappled from above through canopy, porcelain skin in green-gold spring dapple. Style: Korean runway 185cm+ Seoul spring forest sheer editorial. Shot on Hasselblad X2D, 8K UHD, Seoul spring runway grade, portrait 2:3 vertical.",
        "environment": "Seoul Forest spring bloom",
        "lighting": "spring forest dappled light",
        "style": "Korean runway Seoul spring forest sheer editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_icelandic_glacier": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, cold alabaster skin in glacier light, ice-blonde dyed center-part hair",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, cold alabaster skin in glacier light, ice-blonde dyed center-part hair, expression cold as glacier. Wearing: ultra-minimal silver chrome micro string bikini, silver triangles on slim alabaster frame, silver chrome thigh-high platform stiletto boots 6-inch on glacier ice, single crystal drop earring. Environment: Iceland glacier, massive blue-white ice walls behind, crevasses of deep blue ice, glacier silence total. Lighting: glacier ice blue-white ambient from ice walls all around + cold overcast above, alabaster skin in glacier ice-blue. Style: Korean runway 185cm+ Iceland glacier ice-blue editorial. Shot on Phase One XF IQ4, 8K UHD, glacier runway grade, portrait 2:3 vertical.",
        "environment": "Iceland glacier",
        "lighting": "glacier ice blue-white ambient",
        "style": "Korean runway Iceland glacier editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_amalfi_cliff": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs on Amalfi cliff, late-20s, Korean features, warm golden Mediterranean skin",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs on Amalfi cliff, late-20s, Korean features, warm golden Mediterranean skin, long dark hair in Mediterranean wind, expression coastal and commanding. Wearing: ultra-minimal cobalt blue micro string bikini, tiny on slim tall frame, cobalt blue patent platform stiletto wedge 5-inch on cliff path, single gold ear cuff, gold anklet. Environment: Amalfi Coast cliff path, dramatic cliffside dropping to turquoise Tyrrhenian Sea below, colorful Amalfi village on cliff behind, lemon trees. Lighting: Mediterranean noon direct from above + turquoise sea reflection upward, golden Mediterranean skin in dual light. Style: Korean runway 185cm+ Amalfi Coast cliff Mediterranean editorial. Shot on Phase One XF IQ4, 8K UHD, Amalfi runway grade, portrait 2:3 vertical.",
        "environment": "Amalfi Coast cliff path",
        "lighting": "Mediterranean noon + turquoise sea reflection",
        "style": "Korean runway Amalfi cliff Mediterranean editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_berlin_underground": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure as weapon in dark space, mid-20s, Korean features, porcelain skin cold in strobe light, severe architectural silver bob",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure as weapon in dark space, mid-20s, Korean features, porcelain skin cold in strobe light, severe architectural silver bob, cold industrial expression. Wearing: ultra-minimal black PVC micro bodysuit, bodysuit cut extreme high on endless long legs, black chrome thigh-high platform stiletto boots 6-inch on concrete floor, chrome chain harness over bodysuit, chrome geometric ear cuffs. Environment: Berlin underground techno club, raw concrete industrial, strobe cutting darkness, fog machine ground level. Lighting: strobe hard white cutting through dark + ground fog diffusing, porcelain skin in strobe cuts, silver bob catching strobe as silver flash. Style: Korean runway 185cm+ Berlin underground industrial editorial. Shot on Hasselblad X2D, 8K UHD, Berlin runway grade, portrait 2:3 vertical.",
        "environment": "Berlin underground techno club",
        "lighting": "strobe hard white + ground fog",
        "style": "Korean runway Berlin underground industrial editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_bali_temple_gold": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, 22 years old, Korean features, warm golden skin in Bali temple amber",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, 22 years old, Korean features, warm golden skin in Bali temple amber, long straight dark hair with frangipani flower, expression serene and commanding. Wearing: ultra-minimal gold micro string bikini, tiny gold triangles on slim young frame, gold platform stiletto sandal 5-inch on Bali stone path, layered gold chains, gold coin drop earrings. Environment: Bali Hindu temple, intricate stone carved walls with moss, temple lanterns warm amber, incense smoke, tropical flowers. Lighting: temple lantern warm amber, golden-honey young skin in Bali amber, gold bikini on temple gold total palette. Style: Korean runway 185cm+ 22 Bali temple gold editorial. Shot on Phase One XF IQ4, 8K UHD, Bali runway grade, portrait 2:3 vertical.",
        "environment": "Bali Hindu temple",
        "lighting": "temple lantern warm amber",
        "style": "Korean runway Bali temple gold editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_kyoto_autumn": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, luminous porcelain skin in autumn dappled light, severe sleek center-part platinum hair",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, luminous porcelain skin in autumn dappled light, severe sleek center-part platinum hair, expression serene and distant in autumn beauty. Wearing: ultra-minimal cream silk micro slip dress, spaghetti straps invisible on slim frame, dress riding micro-length on endless long legs, clear platform stiletto mules 6-inch on Kyoto stone path, single maple leaf in hair, tiny pearl studs. Environment: Kyoto autumn, maples blazing red-orange-gold, stone path through autumn tunnel, ancient temple gate visible, fallen leaves. Lighting: Kyoto autumn dappled from canopy in red-gold-orange, porcelain skin in warm autumn dapple. Style: Korean runway 185cm+ Kyoto autumn cream editorial. Shot on Hasselblad X2D, 8K UHD, Kyoto autumn runway grade, portrait 2:3 vertical.",
        "environment": "Kyoto autumn maples",
        "lighting": "Kyoto autumn dappled red-gold-orange",
        "style": "Korean runway Kyoto autumn editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_palawan_karst": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Filipino-Korean mixed features, warm golden-honey skin",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Filipino-Korean mixed features, warm golden-honey skin, long straight dark hair in sea wind, expression coastal commanding. Wearing: ultra-minimal white micro string bikini, micro thong, clear platform stiletto wedge mules 5-inch on white Palawan sand, single delicate gold anklet, tiny gold studs. Environment: El Nido Palawan, dramatic limestone karst cliffs towering above and behind extreme tall figure, turquoise lagoon water, hidden beach total. Lighting: Palawan tropical noon direct from above + turquoise lagoon reflection upward, golden-honey skin in tropical dual. Style: Korean runway 185cm+ Palawan karst beach editorial. Shot on Phase One XF IQ4, 8K UHD, Palawan runway grade, portrait 2:3 vertical.",
        "environment": "El Nido Palawan limestone karst",
        "lighting": "tropical noon + turquoise lagoon reflection",
        "style": "Korean runway Palawan karst beach editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_aurora_finland": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure under aurora, mid-20s, Korean features, porcelain skin cold in aurora light, ice-white center-part hair",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure under aurora, mid-20s, Korean features, porcelain skin cold in aurora light, ice-white center-part hair, awe-struck cold expression. Wearing: ultra-minimal silver micro string bikini, silver on porcelain slim frame, silver chrome thigh-high platform stiletto boots 6-inch on Finland snow, silver fox fur stole draped extreme tall shoulders only. Environment: Finnish Lapland wilderness, massive aurora borealis green-purple filling sky above extreme tall figure, frozen lake reflection, pine silhouettes. Lighting: aurora green-purple from sky filling everything + snow reflection below, porcelain skin in aurora color wash. Style: Korean runway 185cm+ Finland aurora silver editorial. Shot on Hasselblad X2D, 8K UHD, Finland aurora runway grade, portrait 2:3 vertical.",
        "environment": "Finnish Lapland aurora borealis",
        "lighting": "aurora green-purple + snow reflection",
        "style": "Korean runway Finland aurora silver editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_sahara_wind": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure on sand dune crest, mid-20s, Korean features, golden-tan skin in Sahara sunset",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure on sand dune crest, mid-20s, Korean features, golden-tan skin in Sahara sunset, long straight dark hair streaming horizontal in desert wind, expression fierce and free. Wearing: ultra-minimal burnt orange micro string bikini, micro thong, gold platform sandal wedge 5-inch on dune crest, layered gold chains, gold drop earrings. Environment: Sahara desert at golden sunset, massive orange sand dune crests, sun touching horizon blazing, camel silhouette in distance. Lighting: Sahara setting sun from horizon + sand reflection below, golden-tan skin in extreme warm orange. Style: Korean runway 185cm+ Sahara sunset wind editorial. Shot on Phase One XF IQ4, 8K UHD, Sahara runway grade, portrait 2:3 vertical.",
        "environment": "Sahara desert golden sunset",
        "lighting": "Sahara setting sun + sand reflection",
        "style": "Korean runway Sahara sunset wind editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_seychelles_granite": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, warm golden-honey skin in Indian Ocean light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure towering over Seychelles granite, mid-20s, Korean features, warm golden-honey skin in Indian Ocean light, long dark hair wild in ocean wind, expression commanding. Wearing: ultra-minimal turquoise micro string bikini, tiny turquoise against golden skin and pink granite, bare feet on smooth pink granite, single turquoise drop earring, turquoise anklet. Environment: Seychelles Anse Source d'Argent, massive smooth pink granite boulders, turquoise Indian Ocean between granite gaps, palm fronds. Lighting: Seychelles golden afternoon + turquoise ocean reflection between granite, golden skin in dual light. Style: Korean runway 185cm+ Seychelles pink granite editorial. Shot on Hasselblad X2D, 8K UHD, Seychelles runway grade, portrait 2:3 vertical.",
        "environment": "Seychelles Anse Source d'Argent",
        "lighting": "Seychelles golden afternoon + ocean reflection",
        "style": "Korean runway Seychelles pink granite editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_tattoo_collarbone_void": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure, collarbone and sternum tattoo fine-line geometric mandala, mid-20s, Korean features, porcelain skin cold",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure, collarbone and sternum tattoo — fine-line geometric mandala spreading from sternum across both collarbones as natural necklace effect, mid-20s, Korean features, porcelain skin cold, severe black hair architectural bun, cold haughty expression. Wearing: ultra-minimal black micro string bikini, thin strings disappearing on slim frame, collarbone tattoo as sole jewelry, black patent thigh-high platform stiletto boots 6-inch, no other accessories. Environment: pure white infinity studio, single overhead hard spot. Lighting: hard overhead spot + white bounce below, porcelain skin in white bilateral, sternum tattoo as editorial jewelry in hard light. Style: Korean runway 185cm+ collarbone tattoo white void editorial. Shot on Phase One XF IQ4, 8K UHD, white void runway grade, portrait 2:3 vertical.",
        "environment": "pure white infinity studio",
        "lighting": "hard overhead spot + white bounce",
        "style": "Korean runway collarbone tattoo white void editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "runway_korean_slim_newyork_snowstorm": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure in NYC snowstorm, mid-20s, Korean features, porcelain skin cold in snowstorm",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure in NYC snowstorm, mid-20s, Korean features, porcelain skin cold in snowstorm, severe slicked-back platinum hair, fierce cold expression — immune to blizzard. Wearing: ultra-minimal black micro string bikini, absolute minimum against snowstorm, black patent thigh-high platform stiletto boots 6-inch in snow-wet NYC sidewalk, single crystal drop earring. Environment: NYC winter blizzard, snow falling heavy, 5th Avenue storefronts in snow behind, yellow taxi blurred, streetlamps in snow haze. Lighting: NYC snowstorm diffused cold from overcast + streetlamp warm from street, porcelain skin in cold-warm contrast. Style: Korean runway 185cm+ NYC blizzard cold editorial. Shot on Hasselblad X2D, 8K UHD, NYC blizzard runway grade, portrait 2:3 vertical.",
        "environment": "NYC winter blizzard 5th Avenue",
        "lighting": "snowstorm diffused cold + streetlamp warm",
        "style": "Korean runway NYC blizzard editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "runway_korean_slim_crystal_gala": {
        "subject": "Korean runway goddess, 185cm+ extreme tall slim figure at crystal gala, mid-20s, Korean features, luminous porcelain skin in chandelier prism light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean runway goddess, 185cm+ extreme tall slim figure at crystal gala, mid-20s, Korean features, luminous porcelain skin in chandelier prism light, elaborate silver-white architectural updo with crystal pins, regal cold expression. Wearing: ultra-minimal crystal micro gown, crystal fringe barely covering slim tall figure, crystal platform stiletto heels 6-inch on marble ballroom floor, massive crystal drop earrings, crystal body chain. Environment: grand European ballroom, massive crystal chandelier directly above extreme tall figure, gilded walls, mirror panels multiplying, marble floor reflecting. Lighting: crystal chandelier from above scattering prismatic light in all directions + marble reflection from below. Style: Korean runway 185cm+ crystal gala chandelier editorial. Shot on Phase One XF IQ4, 8K UHD, crystal gala runway grade, portrait 2:3 vertical.",
        "environment": "grand European ballroom crystal chandelier",
        "lighting": "crystal chandelier prismatic + marble reflection",
        "style": "Korean runway crystal gala chandelier editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },

    # ── Young Adult 20종 ──────────────────────────────────
    "young_korean_jeju_sunrise": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, natural dewy porcelain skin in sunrise warmth",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, natural dewy porcelain skin in sunrise warmth, long straight dark hair loose in morning breeze, pure natural minimal makeup, expression pure joy and wonder at sunrise. Wearing: ultra-minimal white micro string bikini, bare feet on Jeju volcanic rock at Seongsan Ilchulbong, single delicate gold anklet, tiny gold stud earrings. Environment: Seongsan Ilchulbong at sunrise, dramatic volcanic crater, sun rising from East Sea horizon blazing orange-pink-gold, turquoise sea far below, morning mist. Lighting: Jeju sunrise from horizon blazing + sea reflection pink below, dewy 20-year porcelain skin in pure sunrise. Style: Korean young adult 20 Jeju Seongsan sunrise pure editorial. Shot on Hasselblad X2D, 8K UHD, Jeju sunrise young grade, portrait 2:3 vertical.",
        "environment": "Seongsan Ilchulbong Jeju sunrise",
        "lighting": "Jeju sunrise + sea reflection pink",
        "style": "Korean young adult Jeju sunrise editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_studio_black_minimal": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure with subtle curves just emerging, Korean features, luminous porcelain skin",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure with subtle curves just emerging, Korean features, luminous porcelain skin, long straight jet-black hair sleek center-part, sharp eyes, bold red lip on young face, fierce debut expression. Wearing: ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch, single silver geometric ear cuff only. Environment: black infinity studio, single hard overhead spot, pure editorial void. Lighting: single hard overhead spot, luminous porcelain young skin in hard chiaroscuro. Style: Korean young adult 21 debut studio editorial. Shot on Phase One XF IQ4, 8K UHD, debut studio grade, portrait 2:3 vertical.",
        "environment": "black infinity studio",
        "lighting": "single hard overhead spot chiaroscuro",
        "style": "Korean young adult debut studio editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_pool_pastel": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, natural golden-porcelain skin in pool light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, natural golden-porcelain skin in pool light, long dark hair wet and sleek from pool, natural fresh makeup, playful joyful expression. Wearing: ultra-minimal pastel pink micro string bikini, micro thong, clear platform stiletto wedge mules 4-inch at pool edge, delicate gold chain, tiny heart stud earrings. Environment: luxury resort pool, pastel blue water, pink and white poolside furniture, tropical flowers, afternoon golden light. Lighting: afternoon sun direct + pastel blue pool reflection below, golden-porcelain 20-year skin in dual. Style: Korean young adult 20 pastel pool summer editorial. Shot on Hasselblad X2D, 8K UHD, pastel pool young grade, portrait 2:3 vertical.",
        "environment": "luxury resort pool pastel",
        "lighting": "afternoon sun + pastel blue pool reflection",
        "style": "Korean young adult pastel pool summer editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_cherry_blossom": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect figure, Korean features, natural luminous porcelain skin in cherry blossom light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect figure, Korean features, natural luminous porcelain skin in cherry blossom light, long dark wavy hair with petals caught in it, pure natural no-makeup makeup, expression pure innocent spring joy. Wearing: ultra-minimal blush pink micro slip dress, spaghetti straps, dress floating on slim young figure, white platform sandal mules 4-inch, cherry blossom branch in hair, tiny pearl studs. Environment: Korean cherry blossom park at peak bloom, pink blossom canopy above, petals falling like snow. Lighting: cherry blossom pink diffused from canopy — total pink floral diffusion, blush skin in pink blossom light. Style: Korean young adult 20 cherry blossom pure editorial. Shot on Phase One XF IQ4, 8K UHD, cherry blossom young grade, portrait 2:3 vertical.",
        "environment": "Korean cherry blossom park",
        "lighting": "cherry blossom pink diffused total",
        "style": "Korean young adult cherry blossom editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_neon_first_night": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm honey-porcelain skin in Hongdae neon",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm honey-porcelain skin in Hongdae neon, long straight dark hair with neon-dyed pink tips, sharp liner, glossy pink lip, excited fierce young expression. Wearing: ultra-minimal neon pink micro string bikini, micro thong, clear holographic thigh-high platform stiletto boots 5-inch on Hongdae street, neon pink mini crossbody bag, silver small hoops. Environment: Hongdae at midnight, indie club street, neon and LED art, street art murals, young crowd blur, puddles reflecting neon. Lighting: Hongdae neon pink-purple + puddle reflection below, honey-porcelain 21-year skin in neon wash. Style: Korean young adult 21 Hongdae first night editorial. Shot on Hasselblad X2D, 8K UHD, Hongdae neon young grade, portrait 2:3 vertical.",
        "environment": "Hongdae midnight neon street",
        "lighting": "Hongdae neon pink-purple + puddle reflection",
        "style": "Korean young adult Hongdae first night editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_maldives_first_trip": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, warm golden-porcelain skin glowing in Maldives sun",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, warm golden-porcelain skin glowing in Maldives sun, long straight dark hair in ocean breeze, smile wide and genuine, expression of pure 20-year joy at paradise. Wearing: ultra-minimal sky blue micro string bikini, micro thong, bare feet on overwater bungalow deck, single gold anklet, tiny gold studs. Environment: Maldives overwater bungalow, turquoise Indian Ocean surrounding, coral visible through crystal water. Lighting: Maldives midday direct from above + turquoise ocean reflection upward, golden-porcelain young skin in tropical dual. Style: Korean young adult 20 Maldives first trip editorial. Shot on Phase One XF IQ4, 8K UHD, Maldives young grade, portrait 2:3 vertical.",
        "environment": "Maldives overwater bungalow",
        "lighting": "Maldives midday + turquoise ocean reflection",
        "style": "Korean young adult Maldives first trip editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_tokyo_first_solo": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure, Korean features, luminous porcelain skin, Harajuku youth aesthetic",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, luminous porcelain skin, long dark hair with colorful hair clip accessories — Harajuku youth aesthetic, expression excited and fierce first-adult solo travel. Wearing: ultra-minimal white micro string bikini, micro thong, white platform sneaker boots 5-inch on Harajuku street, colorful micro shoulder bag, stacked bracelets on both wrists, tiny star earrings. Environment: Harajuku Takeshita Street, colorful fashion shops, youth crowd, crepe shops. Lighting: Harajuku afternoon dappled through street + colorful shop sign ambient, porcelain 21-year skin in Harajuku color wash. Style: Korean young adult 21 Tokyo Harajuku first solo editorial. Shot on Hasselblad X2D, 8K UHD, Harajuku young grade, portrait 2:3 vertical.",
        "environment": "Harajuku Takeshita Street Tokyo",
        "lighting": "Harajuku afternoon + colorful shop signs",
        "style": "Korean young adult Tokyo Harajuku first solo editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_paris_first_europe": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, luminous porcelain skin in Paris morning light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, luminous porcelain skin in Paris morning light, long dark waves loose in morning Paris air, expression of pure wonder and joy — first time in Europe at 20. Wearing: ultra-minimal cream micro slip dress, thin straps, dress barely covering slim young figure, cream platform stiletto mules 4-inch on Paris stone path, small pearl studs, delicate gold necklace. Environment: Champ de Mars Paris, Eiffel Tower directly behind at golden morning, Parisian couples in background. Lighting: Paris morning golden from side, porcelain 20-year skin in Paris golden warmth. Style: Korean young adult 20 Paris Eiffel first Europe editorial. Shot on Phase One XF IQ4, 8K UHD, Paris young grade, portrait 2:3 vertical.",
        "environment": "Champ de Mars Paris Eiffel Tower",
        "lighting": "Paris morning golden side light",
        "style": "Korean young adult Paris Eiffel first Europe editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_tattoo_first_wrist": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm honey-porcelain skin, first tattoo delicate fine-line moon and stars on right wrist",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm honey-porcelain skin, long dark hair loose and free, natural fresh makeup, expression confident and proud — just got her first tattoo. First tattoo: delicate fine-line moon and stars on right wrist. Wearing: ultra-minimal beige micro string bikini, micro thong, beige platform sandal mules 4-inch on Seoul café street, wrist tattoo prominently displayed, tiny gold studs. Environment: Seoul Bukchon or Insadong café street, hanok wall behind, autumn leaves, warm café amber glow. Lighting: Seoul café street warm afternoon + café amber, honey-porcelain 21-year skin in warm glow. Style: Korean young adult 21 first wrist tattoo Seoul café editorial. Shot on Hasselblad X2D, 8K UHD, Seoul café young grade, portrait 2:3 vertical.",
        "environment": "Seoul Bukchon café street hanok",
        "lighting": "Seoul café street warm afternoon + amber",
        "style": "Korean young adult first wrist tattoo Seoul editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_bali_first_solo": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect figure, Korean features, warm honey skin golden from first week in Bali sun",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect figure, Korean features, warm honey skin golden from first week in Bali sun, long dark hair with flower tucked in, expression of pure free-spirited 20-year happiness. Wearing: ultra-minimal gold micro string bikini, micro thong, bare feet on Bali beach sand, handmade Bali woven anklet, small lotus stud earrings. Environment: Bali beach at sunset, temple silhouette on cliff in background, golden sand, palm trees, Bali sunset orange-pink sky. Lighting: Bali golden sunset from horizon, honey-golden young skin in warm Bali gold. Style: Korean young adult 20 Bali first solo trip golden editorial. Shot on Phase One XF IQ4, 8K UHD, Bali young grade, portrait 2:3 vertical.",
        "environment": "Bali beach sunset temple silhouette",
        "lighting": "Bali golden sunset",
        "style": "Korean young adult Bali first solo golden editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_gym_first_gains": {
        "subject": "Korean young adult goddess, 21 years old, figure beginning to show first real gym results, slim with just-emerging ab definition",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, figure beginning to show first real gym results — slim with just-emerging ab definition, Korean features, warm honey-porcelain skin, dark hair in gym ponytail, expression proud and confident. Wearing: ultra-minimal black micro sports bikini, black chrome platform stiletto boots 6-inch on gym floor, single silver arm band. Environment: home gym with full-length mirror, dumbbells visible, natural afternoon light through window. Lighting: natural afternoon from window + mirror reflection, honey-porcelain 21-year skin in natural light. Style: Korean young adult 21 first gym gains mirror editorial. Shot on Hasselblad X2D, 8K UHD, gym young grade, portrait 2:3 vertical.",
        "environment": "home gym full-length mirror",
        "lighting": "natural afternoon window + mirror reflection",
        "style": "Korean young adult first gym gains editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_summer_busan": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, warm golden-tan skin from Busan summer beach",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, warm golden-tan skin from Busan summer beach, long dark hair wild in sea breeze, smile wide and radiant. Wearing: ultra-minimal bright yellow micro string bikini, micro thong, bare feet in Haeundae sand, yellow anklet, tiny gold hoop earrings. Environment: Haeundae Beach Busan, crowd of summer beachgoers blurred behind, turquoise East Sea waves, Gwangan Bridge visible in distance. Lighting: Busan midday direct from above + sea reflection, golden-tan 20-year skin in summer dual. Style: Korean young adult 20 Busan Haeundae summer editorial. Shot on Phase One XF IQ4, 8K UHD, Busan summer young grade, portrait 2:3 vertical.",
        "environment": "Haeundae Beach Busan Gwangan Bridge",
        "lighting": "Busan midday + sea reflection",
        "style": "Korean young adult Busan Haeundae summer editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_tattoo_ankle_jeju": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm golden porcelain skin, ankle tattoo tiny wave pattern",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm golden porcelain skin kissed by Jeju sun, long dark hair in ocean wind, delicate ankle tattoo — tiny wave pattern wrapping right ankle. Wearing: ultra-minimal white micro string bikini, bare feet on Jeju black volcanic rock, single gold chain on tattooed ankle, tiny gold hoops. Environment: Jeju Island volcanic coastline, black basalt columns, turquoise East Sea crashing below. Lighting: Jeju midday coastal + ocean reflection upward, golden-porcelain 21-year skin in coastal dual. Style: Korean young adult 21 ankle tattoo Jeju volcanic coast editorial. Shot on Hasselblad X2D, 8K UHD, Jeju ankle tattoo young grade, portrait 2:3 vertical.",
        "environment": "Jeju Island volcanic coastline basalt",
        "lighting": "Jeju midday coastal + ocean reflection",
        "style": "Korean young adult ankle tattoo Jeju volcanic editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_midnight_rooftop_seoul": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm porcelain skin in Seoul night air",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm porcelain skin in Seoul night air, long dark hair slightly wild from dancing, makeup slightly smudged — 21-year-old after first real night out, expression fierce and alive and free. Wearing: ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch on Seoul rooftop, black leather micro crossbody, silver small hoop earrings. Environment: Seoul rooftop at 3AM, Han River glowing below, Seoul skyline blazing gold, Namsan Tower behind. Lighting: Seoul city gold ambient from panorama + hint of pre-dawn blue on horizon, porcelain 21-year skin in warm-cool contrast. Style: Korean young adult 21 first Seoul midnight rooftop editorial. Shot on Phase One XF IQ4, 8K UHD, Seoul midnight young grade, portrait 2:3 vertical.",
        "environment": "Seoul rooftop 3AM Han River Namsan",
        "lighting": "Seoul city gold + pre-dawn blue horizon",
        "style": "Korean young adult Seoul midnight rooftop editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_nyc_first_american": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, luminous porcelain skin in NYC neon",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, luminous porcelain skin in NYC neon, long dark hair in NYC wind, expression overwhelmed and fierce and alive — first time in New York at 20. Wearing: ultra-minimal white micro string bikini, white platform stiletto boots 5-inch in Times Square, tiny American flag pin, silver small studs. Environment: Times Square full neon explosion, massive LED billboards in all directions, yellow taxis, NYC crowd energy. Lighting: Times Square full LED neon from all billboard directions, porcelain 20-year skin in neon color saturation. Style: Korean young adult 20 NYC Times Square first America editorial. Shot on Hasselblad X2D, 8K UHD, NYC young grade, portrait 2:3 vertical.",
        "environment": "Times Square NYC LED billboards",
        "lighting": "Times Square full LED neon all directions",
        "style": "Korean young adult NYC Times Square first America editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_campus_spring": {
        "subject": "Korean young adult goddess, 20 years old, first year of university, slim perfect figure, Korean features, natural luminous porcelain skin in spring campus light",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, first year of university, slim perfect figure, Korean features, natural luminous porcelain skin in spring campus light, long dark waves with cute clips, expression bright and youthful. Wearing: ultra-minimal white micro string bikini, white mini platform sneakers 4-inch on campus path, small campus tote bag, stacked friendship bracelets, tiny star studs. Environment: Korean university campus in spring, cherry blossom trees along campus path, students in background, spring afternoon gold. Lighting: spring afternoon golden dappled through cherry blossoms, porcelain 20-year skin in spring cherry gold. Style: Korean young adult 20 university campus spring first year editorial. Shot on Phase One XF IQ4, 8K UHD, campus spring young grade, portrait 2:3 vertical.",
        "environment": "Korean university campus spring cherry blossoms",
        "lighting": "spring afternoon golden dappled",
        "style": "Korean young adult campus spring first year editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_tattoo_shoulder_okinawa": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm golden skin from Okinawa sun, shoulder tattoo delicate fine-line crane",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm golden skin from Okinawa sun, long dark hair in tropical breeze, expression fierce and proud. Shoulder tattoo: delicate fine-line crane on left shoulder blade. Wearing: ultra-minimal turquoise micro string bikini — micro top revealing shoulder tattoo, micro thong, bare feet in white Okinawa sand, simple gold anklet. Environment: Okinawa Emerald Beach, turquoise sea, white sand. Lighting: Okinawa midday direct + turquoise sea reflection, golden 21-year skin in tropical dual. Style: Korean young adult 21 shoulder crane tattoo Okinawa editorial. Shot on Hasselblad X2D, 8K UHD, Okinawa young grade, portrait 2:3 vertical.",
        "environment": "Okinawa Emerald Beach turquoise",
        "lighting": "Okinawa midday + turquoise sea reflection",
        "style": "Korean young adult shoulder crane tattoo Okinawa editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_debut_red_carpet": {
        "subject": "Korean young adult goddess, 21 years old, slim perfect figure on red carpet debut, Korean features, luminous porcelain skin under red carpet flash",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old, slim perfect figure on red carpet debut, Korean features, luminous porcelain skin under red carpet flash, long dark hair in perfect waves, bold red lip, fierce debut expression. Wearing: ultra-minimal silver crystal micro gown barely covering debut figure, silver platform stiletto heels 6-inch on red carpet, crystal drop earrings, crystal body chain. Environment: awards show red carpet, camera flash from all directions, press photographers, red carpet velvet. Lighting: camera flash multi-directional explosion + overhead red carpet spots, porcelain 21-year skin in flash constellation. Style: Korean young adult 21 debut red carpet crystal editorial. Shot on Phase One XF IQ4, 8K UHD, red carpet debut young grade, portrait 2:3 vertical.",
        "environment": "awards show red carpet press photographers",
        "lighting": "camera flash multi-directional + red carpet spots",
        "style": "Korean young adult debut red carpet crystal editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
    "young_korean_first_snowfall_seoul": {
        "subject": "Korean young adult goddess, 20 years old, slim perfect figure, Korean features, luminous porcelain skin in Seoul first snow",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 20 years old, slim perfect figure, Korean features, luminous porcelain skin in Seoul first snow, long dark hair with snowflakes caught in it, expression of pure childlike wonder. Wearing: ultra-minimal white micro string bikini, white platform stiletto boots 5-inch in Seoul snow, white fluffy ear muffs only. Environment: Seoul street in first winter snow, Gyeongbok Palace gate visible through snowfall, traditional lanterns lit warm amber through snow. Lighting: Seoul overcast snow-diffused cold white + palace lantern warm amber, porcelain 20-year skin in cold-warm contrast. Style: Korean young adult 20 Seoul first snow palace editorial. Shot on Hasselblad X2D, 8K UHD, Seoul snow young grade, portrait 2:3 vertical.",
        "environment": "Seoul Gyeongbok Palace first snow",
        "lighting": "snow-diffused cold white + palace lantern amber",
        "style": "Korean young adult Seoul first snow palace editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD"
    },
    "young_korean_21_birthday_gold": {
        "subject": "Korean young adult goddess, 21 years old — her birthday, slim perfect figure, Korean features, luminous golden-porcelain skin under party lights",
        "prompt": "Professional fashion photograph, full body shot. Model: Korean young adult goddess, 21 years old — her birthday, slim perfect figure, Korean features, luminous golden-porcelain skin under party lights, long dark hair in perfect waves, bold coral lip, expression of fierce joy. Wearing: ultra-minimal gold sequin micro string bikini, micro thong, gold chrome thigh-high platform stiletto boots 6-inch, gold chain belt, '21' tiny diamond pendant necklace, gold ear cuffs. Environment: luxury Seoul rooftop party, balloon installation in gold and white, Han River panorama below, confetti in air, friends blurred celebrating behind. Lighting: party golden warm from balloon lights above + Han River city ambient below, golden-porcelain 21-year skin blazing in birthday gold. Style: Korean young adult 21 birthday party gold commanding editorial. Shot on Phase One XF IQ4, 8K UHD, birthday gold young grade, portrait 2:3 vertical.",
        "environment": "luxury Seoul rooftop party Han River",
        "lighting": "party golden balloon lights + Han River city ambient",
        "style": "Korean young adult 21 birthday gold party editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD"
    },
}

count = 0
for key, data in PRESETS.items():
    path = os.path.join(OUTPUT_DIR, f"{key}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    count += 1

print(f"JSON 생성 완료: {count}종")
