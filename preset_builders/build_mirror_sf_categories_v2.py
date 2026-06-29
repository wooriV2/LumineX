"""
LumineX — 🪞 거울&반사 글래머 + 🧬 SF&바이오펑크 신설 스크립트
JSON 내장형 단일 파일 — preset_builders/ 에 저장 후 실행

작업:
1. presets/ 에 JSON 48종 생성
2. dashboard.py PRESET_CATEGORIES에 두 카테고리 추가
"""

import json
import os

LUMINEX_ROOT   = r"C:\Dev\LumineX"
PRESETS_DIR    = os.path.join(LUMINEX_ROOT, "presets")
DASHBOARD_PATH = os.path.join(LUMINEX_ROOT, "dashboard.py")

# ════════════════════════════════════════════════════════
# 🪞 거울&반사 글래머 JSON 데이터
# ════════════════════════════════════════════════════════

MIRROR_PRESETS = {

    # G1 클래식미러
    "infinity_mirror_goddess": {
        "tag": "Infinity Mirror Goddess",
        "subject": "a goddess-like female model standing inside an infinite mirror corridor, multiplied into endless reflections",
        "body": "long limbs, perfect symmetry, commanding presence multiplied infinitely",
        "outfit": "sleek silver latex catsuit, reflecting every mirror surface",
        "material": "liquid silver latex, mirror-polished finish",
        "environment": "infinity mirror tunnel, endless reflections stretching to vanishing point, silver and white tones",
        "lighting": "cold white studio strobes, mirrored light multiplication, overexposed highlights",
        "style": "avant-garde fashion editorial, Vogue conceptual, architectural surrealism",
        "quality": "shot on Hasselblad X2D, ultra-sharp reflections, portrait 2:3 vertical"
    },
    "hall_of_mirrors_glam": {
        "tag": "Hall of Mirrors Glam",
        "subject": "a regal female model posing inside Versailles Hall of Mirrors, surrounded by hundreds of reflections",
        "body": "statuesque elegant figure, aristocratic posture, presence commanding every reflection",
        "outfit": "gold baroque couture gown, ornate embroidery catching chandelier light",
        "material": "gold silk brocade, jeweled embellishments, heavy baroque construction",
        "environment": "Versailles Hall of Mirrors, gilded arched mirrors, crystal chandeliers, golden baroque interior",
        "lighting": "candlelit chandeliers, warm gold ambient, reflections multiplying light infinitely",
        "style": "royal fashion editorial, Vogue Paris, historical luxury campaign",
        "quality": "shot on Phase One XT, cinematic golden grade, portrait 2:3 vertical"
    },
    "obsidian_mirror_ritual": {
        "tag": "Obsidian Mirror Ritual",
        "subject": "a mystical female model gazing into a massive obsidian mirror, dark reflection warped and powerful",
        "body": "dark dramatic figure, intense gaze, ritual stillness",
        "outfit": "black latex bodysuit with obsidian jewelry, ritualistic harness details",
        "material": "pure black latex, volcanic obsidian accessories, matte-gloss contrast",
        "environment": "dark ceremonial chamber, single obsidian mirror slab, smoke and candlelight, ancient stone walls",
        "lighting": "single flame source, dramatic chiaroscuro, obsidian surface absorbing and reflecting simultaneously",
        "style": "dark fashion editorial, occult luxury, Dazed & Confused conceptual",
        "quality": "shot on Sony A1, deep shadow detail, portrait 2:3 vertical"
    },
    "venetian_mirror_boudoir": {
        "tag": "Venetian Mirror Boudoir",
        "subject": "a sensual female model in an opulent Venetian boudoir, surrounded by antique mirrors with silver patina",
        "body": "soft curves, languid sensual pose, effortless opulence",
        "outfit": "sheer ivory silk robe, delicate lace lingerie, pearls",
        "material": "silk organza, antique lace, natural pearl strands",
        "environment": "Venetian palazzo boudoir, mercury glass mirrors with aged patina, velvet chaise, candlelight",
        "lighting": "warm candlelight, mercury mirror reflection with golden haze, soft romantic diffusion",
        "style": "intimate luxury editorial, Pirelli Calendar, old-world glamour",
        "quality": "shot on Leica M11, warm film-like rendering, portrait 2:3 vertical"
    },
    "cheval_mirror_reveal": {
        "tag": "Cheval Mirror Reveal",
        "subject": "a striking female model standing before a full-length cheval mirror, her reflection showing a different angle simultaneously",
        "body": "elongated figure, two views revealed at once, dual perspective power",
        "outfit": "structured black power suit, open back revealing spine, front and back contrast",
        "material": "Italian wool crepe, sharp tailoring, minimal hardware",
        "environment": "minimalist white studio, single cheval mirror, polished concrete floor, harsh directional light",
        "lighting": "single side strobe, harsh editorial light, strong shadow-to-highlight ratio",
        "style": "editorial power fashion, Celine campaign aesthetic, architectural minimalism",
        "quality": "shot on Hasselblad H6D, crisp editorial rendering, portrait 2:3 vertical"
    },
    "broken_mirror_multiplied": {
        "tag": "Broken Mirror Multiplied",
        "subject": "a fierce female model surrounded by shattered mirror fragments, each shard reflecting a different pose simultaneously",
        "body": "dynamic powerful stance, energy radiating through broken reflections",
        "outfit": "silver mirror-fragment encrusted bodysuit, crystalline shards as jewelry",
        "material": "mirror glass mosaic on stretch base, crystalline embellishments",
        "environment": "dark studio floor covered in broken mirror shards, fragments suspended mid-air, fractured light explosion",
        "lighting": "multiple strobes refracted through broken glass, prismatic light shards, chaotic brilliance",
        "style": "high-concept fashion art, Alexander McQueen editorial, destruction beauty",
        "quality": "shot on Canon EOS R5, freeze-motion fragments sharp, portrait 2:3 vertical"
    },

    # G2 수면반사
    "mercury_lake_reflection": {
        "tag": "Mercury Lake Reflection",
        "subject": "a ethereal female model standing on a perfectly still lake at dawn, her reflection indistinguishable from reality",
        "body": "tall slender figure, symmetrical pose designed for perfect water reflection",
        "outfit": "silver liquid-metal gown, flowing into water's edge seamlessly",
        "material": "liquid metallic silk, mercury-toned fabric dissolving into reflection",
        "environment": "glassy alpine lake at dawn, mirror-perfect water surface, mist at horizon, mountains reflected",
        "lighting": "pre-dawn blue hour, soft diffused sky light, reflection doubling every element",
        "style": "ethereal fashion editorial, National Geographic luxury, reflection surrealism",
        "quality": "shot on Phase One IQ4, tack-sharp reflection symmetry, portrait 2:3 vertical"
    },
    "salt_flat_sky_merge": {
        "tag": "Salt Flat Sky Merge",
        "subject": "a powerful female model standing on Bolivian salt flats, sky and earth merging in perfect reflection below her",
        "body": "commanding figure appearing to float between two skies, legs dissolving into reflection",
        "outfit": "white structural couture, blending with salt flat white, sky-colored accents",
        "material": "architectural white silk, rigid sculptural construction, transparent elements",
        "environment": "Salar de Uyuni at golden hour, water-thin reflective layer, infinite horizon, clouds mirrored below",
        "lighting": "golden hour horizontal light, sky reflection from below, surreal double-exposure reality",
        "style": "surreal fashion photography, impossible landscape editorial, Tim Walker aesthetic",
        "quality": "shot on Hasselblad X2D, infinite depth of field, landscape 3:2"
    },
    "rain_puddle_city_invert": {
        "tag": "Rain Puddle City Invert",
        "subject": "a chic female model stepping over a puddle reflecting the entire city skyline upside-down beneath her heels",
        "body": "dynamic stride, confident urban energy, reflection world beneath her feet",
        "outfit": "sleek black trench coat, patent leather boots, minimalist city chic",
        "material": "water-resistant gabardine, patent PVC boots, silver hardware",
        "environment": "rainy city street at night, neon signs reflected in puddles, inverted skyline below, rain-slicked pavement",
        "lighting": "neon reflections in wet pavement, city glow from below, rain-diffused streetlights",
        "style": "urban editorial, Helmut Newton street glamour, noir city fashion",
        "quality": "shot on Leica Q3, cinematic rain atmosphere, portrait 2:3 vertical"
    },
    "flooded_temple_mirror": {
        "tag": "Flooded Temple Mirror",
        "subject": "a goddess female model standing in a flooded ancient temple, stone columns reflected perfectly in ankle-deep water",
        "body": "divine statuesque presence, hieratic pose, deity-like stillness above water",
        "outfit": "draped white goddess gown, wet hem dissolving into reflection, gold laurel crown",
        "material": "wet white linen, gold leaf accessories, ancient textile weight",
        "environment": "flooded Greco-Roman temple ruin, column reflections in still water, golden hour through open roof",
        "lighting": "shaft of golden light from above, water reflection amplifying warmth, ancient stone shadow contrast",
        "style": "mythological fashion editorial, Pirelli Calendar, ancient world luxury",
        "quality": "shot on Canon EOS R3, golden tone cinematic grade, portrait 2:3 vertical"
    },
    "infinity_pool_edge_reflect": {
        "tag": "Infinity Pool Edge Reflect",
        "subject": "a stunning female model perched at infinity pool edge, ocean horizon and her reflection merging into seamless blue",
        "body": "long lean figure, poolside confidence, body and reflection forming perfect symmetry",
        "outfit": "metallic azure one-piece swimsuit, wet and gleaming, poolside jewelry",
        "material": "metallic spandex, wet-look finish, gold accessories",
        "environment": "cliff-edge infinity pool, Maldives or Santorini, ocean merging with pool at horizon, cerulean blue",
        "lighting": "midday tropical sun, water reflection shimmer, turquoise light from below",
        "style": "luxury resort campaign, Sports Illustrated, azure infinity editorial",
        "quality": "shot on Sony A9 III, vibrant tropical color grade, portrait 2:3 vertical"
    },
    "morning_dew_skin_reflection": {
        "tag": "Morning Dew Skin Reflection",
        "subject": "a close-up beauty model with morning dew droplets on skin, each droplet containing a tiny reflected landscape",
        "body": "flawless skin surface, droplets as tiny mirrors across collarbone and shoulders",
        "outfit": "bare skin, single dewdrop pearl necklace, minimal natural beauty",
        "material": "skin as canvas, water droplets, natural pearl",
        "environment": "misty morning garden, soft fog, green bokeh background, golden first light",
        "lighting": "soft dawn sidelight, each droplet refracting light into spectrum, macro beauty lighting",
        "style": "macro beauty editorial, Vogue beauty, skin-as-landscape concept",
        "quality": "shot on Canon 100mm macro, hyper-detailed skin texture, portrait 2:3 vertical"
    },

    # G3 유리&프리즘
    "glass_box_all_angles": {
        "tag": "Glass Box All Angles",
        "subject": "a powerful female model enclosed in a transparent glass cube, visible from all angles simultaneously",
        "body": "geometric precise poses, body as sculpture within glass architecture",
        "outfit": "transparent PVC structured bodysuit, architectural glass-like construction",
        "material": "crystal clear PVC, glass-effect rigid panels, invisible seaming",
        "environment": "pure white studio, glass cube installation, multiple camera angles visible, reflections on all six faces",
        "lighting": "360-degree even studio lighting, glass refracting light into subtle prisms, clean shadowless white",
        "style": "conceptual art fashion, Comme des Garçons editorial, body-as-object concept",
        "quality": "shot on Hasselblad H6D, maximum clarity glass detail, portrait 2:3 vertical"
    },
    "prism_light_body_split": {
        "tag": "Prism Light Body Split",
        "subject": "a striking female model with a giant crystal prism splitting white light across her body into full spectrum rainbow",
        "body": "lean athletic figure, body as canvas for prismatic light painting",
        "outfit": "white minimal bodysuit, bare skin areas receiving spectrum light",
        "material": "white matte stretch fabric, skin as light receptor",
        "environment": "dark studio, single crystal prism installation, rainbow spectrum projected across body and background",
        "lighting": "single white beam through prism, full RGB spectrum split, dark void background",
        "style": "science-art fashion editorial, physics-beauty concept, Nick Knight aesthetic",
        "quality": "shot on Phase One XT, color spectrum precision, portrait 2:3 vertical"
    },
    "crystal_cave_skin_facets": {
        "tag": "Crystal Cave Skin Facets",
        "subject": "a mystical female model inside a giant crystal geode cave, surrounded by faceted crystal walls reflecting her infinitely",
        "body": "otherworldly presence, skin appearing crystalline, faceted light on body",
        "outfit": "crystal-encrusted bodysuit, geode-inspired jewelry, raw crystal crown",
        "material": "Swarovski crystal mesh, raw amethyst and quartz accessories",
        "environment": "interior of giant crystal geode, purple amethyst and white quartz walls, reflective facets everywhere",
        "lighting": "inner crystal luminescence, faceted reflections creating kaleidoscopic body light",
        "style": "fantasy fashion editorial, geological luxury, Alexander McQueen supernatural",
        "quality": "shot on Sony A1, crystal facet sharpness, portrait 2:3 vertical"
    },
    "two_way_mirror_watcher": {
        "tag": "Two Way Mirror Watcher",
        "subject": "a commanding female model standing at a two-way mirror, seeing her reflection while being observed from the dark side",
        "body": "confrontational pose, direct gaze into mirror, awareness of being watched",
        "outfit": "sleek dark power suit, architectural cut, dominance through tailoring",
        "material": "black wool crepe, sharp structured tailoring, minimal hardware",
        "environment": "interrogation-room aesthetic, one bright side with model, dark observation side visible through glass",
        "lighting": "harsh overhead fluorescent on model side, darkness on observer side, psychological light contrast",
        "style": "noir psychological fashion, Helmut Newton power dynamic, conceptual tension editorial",
        "quality": "shot on Leica M11, high contrast noir rendering, portrait 2:3 vertical"
    },
    "window_rain_double": {
        "tag": "Window Rain Double",
        "subject": "a melancholic female model at a rain-streaked window, her reflection ghosting over the wet city outside",
        "body": "contemplative pose, double image created by glass reflection, inside and outside merging",
        "outfit": "sheer silk slip dress, intimate indoor softness contrasting rainy exterior",
        "material": "silk charmeuse, soft draping, delicate strap construction",
        "environment": "apartment window in heavy rain, city lights blurred through wet glass, ghost reflection layering interior over exterior",
        "lighting": "warm interior lamp glow, cold rainy blue from outside, double-exposure window reflection",
        "style": "moody intimate editorial, Nan Goldin aesthetic, rain-window poetry",
        "quality": "shot on Leica Q3, film grain, double exposure portrait 2:3 vertical"
    },
    "soap_bubble_dome": {
        "tag": "Soap Bubble Dome",
        "subject": "a whimsical female model surrounded by giant soap bubbles, each one reflecting a distorted fisheye view of her",
        "body": "playful ethereal presence, multiple distorted reflections across bubble surfaces",
        "outfit": "iridescent holographic mini dress, bubble-like sheen, pastel rainbow",
        "material": "holographic PVC, iridescent stretch fabric, rainbow light effect",
        "environment": "white studio filled with giant soap bubbles, each bubble reflecting iridescent rainbow and model distortion",
        "lighting": "soft diffused studio light, iridescent bubble refraction, rainbow spectrum everywhere",
        "style": "whimsical luxury editorial, Comme des Garçons playful, bubble surrealism",
        "quality": "shot on Canon EOS R5, bubble surface sharpness, portrait 2:3 vertical"
    },

    # G4 크롬&메탈
    "chrome_sphere_world": {
        "tag": "Chrome Sphere World",
        "subject": "a glamorous female model holding a giant chrome sphere reflecting the entire world around her in fisheye distortion",
        "body": "powerful stance, chrome sphere held aloft, entire environment captured in its surface",
        "outfit": "chrome mirror latex catsuit, matching the sphere surface perfectly",
        "material": "mirror-finish chrome latex, liquid metal appearance, perfectly reflective",
        "environment": "dramatic landscape or studio, chrome sphere reflecting everything in miniature fisheye world",
        "lighting": "multiple light sources all reflected in sphere, model and environment simultaneously visible",
        "style": "surrealist fashion editorial, Man Ray modernism, chrome universe concept",
        "quality": "shot on Phase One IQ4, chrome reflection detail, portrait 2:3 vertical"
    },
    "polished_obsidian_floor": {
        "tag": "Polished Obsidian Floor",
        "subject": "a fierce female model standing on a perfectly polished black obsidian floor, her reflection razor-sharp beneath her",
        "body": "elongated figure, legs extending into perfect reflection below, doubled silhouette",
        "outfit": "architectural black leather structured coat, knife-edge tailoring, obsidian jewelry",
        "material": "black calfskin leather, architectural boning, volcanic obsidian accessories",
        "environment": "vast polished black obsidian floor, minimal dark space, reflection stretching endlessly below",
        "lighting": "single overhead spotlight, reflection as sharp as reality, dark void surrounding",
        "style": "architectural power fashion, Celine dark editorial, obsidian void concept",
        "quality": "shot on Hasselblad X2D, obsidian reflection perfection, portrait 2:3 vertical"
    },
    "supercar_chrome_reflect": {
        "tag": "Supercar Chrome Reflect",
        "subject": "a sensual female model draped over a chrome supercar hood, her body reflected and distorted across curved metal surface",
        "body": "curves echoed in chrome car body, human form and machine form in dialogue",
        "outfit": "silver liquid-metal mini dress, automotive glamour, chrome accessories",
        "material": "metallic liquid jersey, chrome-plated hardware, mirror finish accessories",
        "environment": "underground parking or racetrack, chrome supercar as reflective prop, industrial luxury",
        "lighting": "dramatic side light catching chrome curves, body and car reflection merging, high contrast",
        "style": "automotive luxury fashion, Helmut Newton car editorial, speed-glamour concept",
        "quality": "shot on Canon EOS R3, chrome surface detail, landscape 3:2"
    },
    "liquid_metal_pool": {
        "tag": "Liquid Metal Pool",
        "subject": "an otherworldly female model standing in a shallow pool of liquid mercury, her reflection rippling in metallic liquid",
        "body": "statuesque figure, legs disappearing into mercury surface, surreal material interaction",
        "outfit": "mercury-toned liquid metal bodysuit, seamlessly matching the pool surface",
        "material": "silver liquid metal fabric, mercury-effect finish, body becoming liquid",
        "environment": "surreal studio space, shallow pool of mercury-like liquid metal, ripples creating warped reflections",
        "lighting": "overhead silver-toned light, mercury surface catching and distorting all light, metallic ambiance",
        "style": "surrealist fashion concept, Thierry Mugler futurism, liquid metal universe",
        "quality": "shot on Phase One XT, liquid metal surface rendering, portrait 2:3 vertical"
    },
    "foil_room_crush": {
        "tag": "Foil Room Crush",
        "subject": "a bold female model inside a room entirely lined with crumpled silver foil, thousands of distorted reflections covering every surface",
        "body": "commanding presence, multiplied and distorted across every crumpled foil facet",
        "outfit": "crumpled silver foil mini dress, matching room installation, wearable sculpture",
        "material": "metallic foil construction, crumpled texture, silver mylar",
        "environment": "room entirely covered in crumpled silver mylar foil, ceiling floor walls all reflective chaos",
        "lighting": "single strobe creating chaotic foil reflections everywhere, silver light explosion",
        "style": "Andy Warhol Silver Factory aesthetic, installation art fashion, chaotic mirror concept",
        "quality": "shot on Sony A1, foil texture chaos, portrait 2:3 vertical"
    },
    "mirrored_skyscraper_facade": {
        "tag": "Mirrored Skyscraper Facade",
        "subject": "a powerful female model pressed against a mirrored glass skyscraper facade, city and clouds reflected across her body",
        "body": "urban goddess scale, body merging with building reflection, architecture as outfit",
        "outfit": "minimal structured black bodysuit, city reflection becoming her clothing",
        "material": "matte black stretch, clean lines allowing building reflection to dominate",
        "environment": "mirrored glass skyscraper exterior, city skyline reflected across building facade, clouds moving in glass",
        "lighting": "urban daylight, city reflection on glass overwhelming everything, scale of architecture",
        "style": "urban architectural fashion, Helmut Newton scale editorial, city-as-fashion concept",
        "quality": "shot on Phase One IQ4, architectural scale portrait, portrait 2:3 vertical"
    },
}

# ════════════════════════════════════════════════════════
# 🧬 SF&바이오펑크 JSON 데이터
# ════════════════════════════════════════════════════════

SF_PRESETS = {

    # G1 크라이오&실험실
    "cryo_emergence_wet": {
        "tag": "Cryo Emergence Wet",
        "subject": "a striking female model emerging from a cryogenic pod, soaking wet with ice crystals dissolving on skin",
        "body": "awakening from frozen stasis, condensation covering every surface, ice melting on skin",
        "outfit": "torn cryogenic survival suit, skin visible through frost damage, minimal and functional",
        "material": "distressed thermal fabric, ice crystal accretion, frozen condensation on skin",
        "environment": "cryogenic facility, steam venting, pod doors open, blue emergency lighting, ice on all surfaces",
        "lighting": "blue emergency strobe light, cryo steam backlight, cold clinical fluorescence",
        "style": "sci-fi fashion editorial, Alien aesthetic, cryogenic emergence concept",
        "quality": "shot on Sony A1, ice crystal detail on skin, portrait 2:3 vertical"
    },
    "specimen_amber_suspended": {
        "tag": "Specimen Amber Suspended",
        "subject": "a beautiful female model suspended inside a giant amber-like resin block, perfectly preserved like an ancient specimen",
        "body": "frozen perfect pose, suspended in translucent amber medium, insect-in-amber concept at human scale",
        "outfit": "minimal white lab specimen garment, preserved in amber transparency",
        "material": "translucent amber resin surrounding body, white cotton within",
        "environment": "scientific specimen display, giant amber block backlit, museum of impossible specimens",
        "lighting": "amber backlight through resin, warm orange internal glow, specimen case illumination",
        "style": "sci-fi art concept, natural history museum subverted, preserved beauty editorial",
        "quality": "shot on Hasselblad X2D, amber translucency rendering, portrait 2:3 vertical"
    },
    "clean_room_latex_protocol": {
        "tag": "Clean Room Latex Protocol",
        "subject": "a clinical female model in a pharmaceutical clean room, full latex protocol suit with glass visor, sterile authority",
        "body": "precise controlled movements, clinical authority, sterile environment dominance",
        "outfit": "white latex hazmat-chic suit, clear visor helmet, sterile gloves, protocol perfection",
        "material": "white surgical latex, polycarbonate visor, sterile sealed construction",
        "environment": "pharmaceutical clean room, white sealed walls, UV sterilization lights, airlock visible",
        "lighting": "harsh white fluorescent, UV purple sterilization strips, shadowless clinical light",
        "style": "clinical sci-fi fashion, pharmaceutical luxury editorial, sterile dominance concept",
        "quality": "shot on Canon EOS R5, clinical white rendering, portrait 2:3 vertical"
    },
    "gene_sequencer_data_skin": {
        "tag": "Gene Sequencer Data Skin",
        "subject": "a futuristic female model with DNA sequence data projected across her entire skin surface, becoming living data",
        "body": "lean scientific beauty, skin as data display, genetic code made visible",
        "outfit": "black minimal bodysuit, skin the primary canvas for DNA projection",
        "material": "matte black stretch, skin receiving genetic data projection",
        "environment": "genetic research lab, gene sequencer machine, holographic DNA helix displays, blue data projections",
        "lighting": "blue DNA data projection across skin, green sequence readouts, dark lab ambiance",
        "style": "biotech fashion editorial, science-beauty fusion, genetic identity concept",
        "quality": "shot on Phase One XT, data projection on skin precision, portrait 2:3 vertical"
    },
    "quarantine_protocol_breach": {
        "tag": "Quarantine Protocol Breach",
        "subject": "a fierce female model tearing through a quarantine containment barrier, plastic sheeting wrapping dramatically around her",
        "body": "explosive energy breaking through containment, plastic sheeting as dynamic fashion element",
        "outfit": "black tactical bodysuit beneath torn quarantine plastic, biohazard aesthetic",
        "material": "black stretch tactical fabric, torn plastic sheeting wrapping, biohazard tape accents",
        "environment": "quarantine zone breach, yellow hazard tape, plastic sheeting tearing, red alarm lights",
        "lighting": "red emergency alarm strobes, yellow hazard light, dramatic breach moment",
        "style": "apocalyptic fashion editorial, post-pandemic aesthetic, containment breach drama",
        "quality": "shot on Sony A9 III, motion freeze plastic tear, portrait 2:3 vertical"
    },
    "petri_dish_giant_macro": {
        "tag": "Petri Dish Giant Macro",
        "subject": "a miniaturized female model inside a giant petri dish, surrounded by growing culture medium, scale subverted",
        "body": "human figure dwarfed by scientific scale, specimen perspective reversed",
        "outfit": "iridescent bacterial culture colors on skin as body paint, organism aesthetic",
        "material": "bioluminescent body paint in culture medium colors, agar-like texture references",
        "environment": "giant petri dish environment, culture medium terrain, microscope light from above, lab scale inverted",
        "lighting": "overhead microscope illumination, culture medium iridescence, clinical yet biological",
        "style": "scale-subversion art fashion, scientific surrealism, biology-beauty concept",
        "quality": "shot on Hasselblad X2D, macro-to-human scale rendering, portrait 2:3 vertical"
    },

    # G2 심해&유기체
    "abyssal_pressure_glam": {
        "tag": "Abyssal Pressure Glam",
        "subject": "a powerful female model at deep ocean abyssal depth, bioluminescent creatures surrounding her, pressure suit torn open",
        "body": "deep sea goddess, pressure of the abyss in her bearing, darkness adapted beauty",
        "outfit": "deep sea pressure suit partially open, bioluminescent accents, abyssal fashion",
        "material": "dark rubber pressure suit, bioluminescent fiber optic accents, deep ocean materials",
        "environment": "deep ocean abyss, complete darkness except bioluminescence, deep sea creatures, crushing pressure aesthetic",
        "lighting": "bioluminescent creature glow only, deep blue-black darkness, point source organic lights",
        "style": "deep sea sci-fi editorial, oceanic horror glamour, abyssal beauty concept",
        "quality": "shot on Phase One XT, bioluminescence in darkness, portrait 2:3 vertical"
    },
    "mycelium_web_consumed": {
        "tag": "Mycelium Web Consumed",
        "subject": "a beautiful female model being consumed by white mycelium fungal network, threads growing across her skin organically",
        "body": "body becoming part of fungal network, mycelium threads mapping body contours",
        "outfit": "minimal flesh-toned bodysuit, mycelium threads as the primary covering",
        "material": "skin-colored base, white mycelium thread installation across body",
        "environment": "dark forest floor, mycelium network spreading from body into environment, decay and growth",
        "lighting": "undergrowth filtered light, mycelium threads catching light against dark background, organic illumination",
        "style": "organic horror fashion, fungi consumption concept, nature-body merger editorial",
        "quality": "shot on Canon 100mm macro, mycelium thread detail, portrait 2:3 vertical"
    },
    "coral_organism_absorption": {
        "tag": "Coral Organism Absorption",
        "subject": "a serene female model being absorbed into a giant coral reef organism, coral growing across skin in living jewelry",
        "body": "body merging with reef organism, coral branches growing from shoulders and arms",
        "outfit": "bare skin with living coral growing as organic couture, ocean creature symbiosis",
        "material": "living coral prosthetics, sea anemone textures, reef organism aesthetics",
        "environment": "underwater coral reef, warm tropical shallow water, coral organism host environment",
        "lighting": "tropical underwater caustic light patterns, coral fluorescence under UV, warm shallow water light",
        "style": "underwater fashion art, reef symbiosis concept, marine biology luxury",
        "quality": "shot on underwater housing Canon R5, coral texture detail, portrait 2:3 vertical"
    },
    "carnivorous_plant_trap": {
        "tag": "Carnivorous Plant Trap",
        "subject": "a dangerous female model emerging from the mouth of a giant Venus flytrap-like plant, plant as throne and trap",
        "body": "predatory beauty, plant trap as power accessory, hunter not prey despite apparent capture",
        "outfit": "green latex bodysuit with plant vein patterns, carnivorous plant aesthetic",
        "material": "deep green latex, organic vein pattern printing, plant-flesh hybrid aesthetic",
        "environment": "giant carnivorous plant environment, trigger hairs, digestive fluid, botanical horror",
        "lighting": "green botanical filtered light, bioluminescent digestive glow, predatory plant drama",
        "style": "botanical horror fashion, plant predator concept, dark nature editorial",
        "quality": "shot on Hasselblad X2D, plant texture and skin contrast, portrait 2:3 vertical"
    },
    "symbiote_second_skin": {
        "tag": "Symbiote Second Skin",
        "subject": "a fierce female model with an alien symbiote organism covering half her body, alien and human in perfect merger",
        "body": "half human half symbiote, body boundary dissolved by alien organism merger",
        "outfit": "black liquid alien symbiote covering half body organically, tendrils and alien texture",
        "material": "liquid black symbiote organism aesthetic, alien bio-material, living dark texture",
        "environment": "urban environment with alien contamination spread, symbiote tendrils on walls",
        "lighting": "dramatic split light, human side warm, symbiote side cold alien blue, merger at center",
        "style": "sci-fi body horror fashion, alien symbiosis concept, dark superhero editorial",
        "quality": "shot on Sony A1, symbiote texture detail, portrait 2:3 vertical"
    },
    "jellyfish_bloom_float": {
        "tag": "Jellyfish Bloom Float",
        "subject": "an ethereal female model floating among a bloom of giant bioluminescent jellyfish, tentacles as translucent fashion",
        "body": "weightless floating figure, jellyfish as living couture surrounding her",
        "outfit": "translucent jellyfish-inspired organza gown, bioluminescent accents, bell and tentacle silhouette",
        "material": "translucent organza layers, bioluminescent fiber optics woven in, jellyfish bell structure",
        "environment": "deep water jellyfish bloom, blue bioluminescent darkness, hundreds of jellyfish surrounding",
        "lighting": "jellyfish bioluminescence only, blue and purple organic light, deep water darkness",
        "style": "underwater fashion art, marine creature couture, bioluminescent beauty editorial",
        "quality": "shot on underwater Phase One, jellyfish translucency rendering, portrait 2:3 vertical"
    },

    # G3 트랜스휴먼
    "cyborg_partial_reveal": {
        "tag": "Cyborg Partial Reveal",
        "subject": "a beautiful female model with cyborg augmentations partially revealed, skin peeling to show mechanical interior",
        "body": "human beauty with mechanical skeleton visible, organic and machine in elegant coexistence",
        "outfit": "torn fitted garment revealing cyborg panel, skin and chrome contrast",
        "material": "fitted garment with strategic tears, chrome mechanical interior, skin-chrome boundary",
        "environment": "sleek tech laboratory or urban environment, human-machine integration context",
        "lighting": "LED lighting from mechanical interior, warm skin light contrasting cold chrome, dual-nature illumination",
        "style": "cyberpunk fashion editorial, human-machine aesthetic, Ghost in the Shell inspired",
        "quality": "shot on Canon EOS R5, skin-chrome boundary detail, portrait 2:3 vertical"
    },
    "neural_lace_crown": {
        "tag": "Neural Lace Crown",
        "subject": "a transcendent female model wearing a neural lace interface crown, data streams visible flowing from mind to air",
        "body": "elevated consciousness beauty, neural interface as ultimate power accessory",
        "outfit": "minimal white bodysuit, neural lace headpiece as primary statement piece",
        "material": "white minimal stretch, gold neural lace wire crown, holographic data stream effects",
        "environment": "neural interface laboratory, holographic data displays, brain-computer interface aesthetic",
        "lighting": "holographic data blue light, neural activity visualization glow, cold tech ambiance",
        "style": "transhumanist fashion, neural interface editorial, consciousness-expansion concept",
        "quality": "shot on Phase One XT, neural lace detail, portrait 2:3 vertical"
    },
    "exoskeleton_stripped": {
        "tag": "Exoskeleton Stripped",
        "subject": "a powerful female model wearing a partially stripped military exoskeleton, human power amplified by machine",
        "body": "strength amplified by exoskeleton frame, human body as core of mechanical power suit",
        "outfit": "stripped tactical exoskeleton over minimal bodysuit, exposed mechanical joints, power aesthetic",
        "material": "military-grade titanium exoskeleton, black tactical underlayer, exposed hydraulics",
        "environment": "military research facility or post-apocalyptic urban, exoskeleton deployment context",
        "lighting": "harsh military lighting, exoskeleton edge light, power and authority illumination",
        "style": "military sci-fi fashion, exosuit editorial, female power amplification concept",
        "quality": "shot on Sony A9 III, exoskeleton mechanical detail, portrait 2:3 vertical"
    },
    "prosthetic_art": {
        "tag": "Prosthetic Art",
        "subject": "a stunning female model with avant-garde artistic prosthetic limbs, disability transformed into high fashion statement",
        "body": "prosthetic limbs as couture accessories, human form redefined and elevated",
        "outfit": "haute couture gown designed around prosthetic aesthetic, prosthetics as primary design element",
        "material": "carbon fiber artistic prosthetics, luxury gown fabric, prosthetic-couture integration",
        "environment": "high fashion studio or runway, prosthetics celebrated as design feature",
        "lighting": "high fashion studio lighting, prosthetic surface catching directional light, beauty in difference",
        "style": "inclusive high fashion, Vogue disability empowerment, prosthetic as couture editorial",
        "quality": "shot on Hasselblad X2D, prosthetic texture and fabric contrast, portrait 2:3 vertical"
    },
    "spine_tech_implant": {
        "tag": "Spine Tech Implant",
        "subject": "a dominant female model showing her back, spine replaced by visible glowing tech implant ridge, power from within",
        "body": "back as primary canvas, spine implant as power architecture, strength made visible",
        "outfit": "backless gown revealing entire spine implant, front hidden elegance back tech reveal",
        "material": "front elegant fabric, bare back with tech spine implant, LED spine glow",
        "environment": "dark elegant interior or tech environment, spine glow as ambient light source",
        "lighting": "spine implant as primary light source, back-lit tech glow, dark surrounding space",
        "style": "transhumanist luxury fashion, spine augmentation editorial, power-within concept",
        "quality": "shot on Sony A1, spine implant glow detail, portrait 2:3 vertical"
    },
    "synthetic_skin_tear": {
        "tag": "Synthetic Skin Tear",
        "subject": "an unsettling female model with synthetic skin peeling away to reveal different skin beneath, layers of identity",
        "body": "skin as mask peeling away, multiple identity layers, android-human boundary dissolving",
        "outfit": "white minimal dress, synthetic skin peeling as primary garment concept",
        "material": "prosthetic synthetic skin appliances, layered skin effect, identity material",
        "environment": "clinical white studio, identity examination context, psychological space",
        "lighting": "clinical white light, skin layer shadows highlighting peeling edges, identity revelation",
        "style": "body horror fashion art, identity concept editorial, Cronenberg body horror aesthetic",
        "quality": "shot on Canon 100mm macro, skin layer detail, portrait 2:3 vertical"
    },

    # G4 바이러스&뮤테이션
    "mutation_bloom": {
        "tag": "Mutation Bloom",
        "subject": "a beautiful female model with flowers blooming from her skin as mutations, organic beauty emerging from body",
        "body": "body as garden, flowers growing from skin as beautiful mutation, nature breaking through",
        "outfit": "minimal base, flowers erupting through fabric as living mutation couture",
        "material": "torn minimal fabric, fresh flowers as skin growths, organic material erupting",
        "environment": "clinical space or wild garden, mutation emergence context, before-after boundary",
        "lighting": "soft natural light for flowers, clinical cold for mutation context, beauty-horror duality",
        "style": "organic mutation fashion, body horror beauty, Nick Knight flower editorial",
        "quality": "shot on Canon 100mm macro, flower-from-skin detail, portrait 2:3 vertical"
    },
    "toxic_spore_cloud": {
        "tag": "Toxic Spore Cloud",
        "subject": "a dangerous female model releasing toxic spore clouds from her body, environmental hazard as fashion statement",
        "body": "spore release as power, toxic beauty, environmental threat embodied",
        "outfit": "biohazard chic bodysuit, spore release vents integrated as design, toxic glamour",
        "material": "chemical-resistant aesthetic fabric, spore vent hardware, biohazard color palette",
        "environment": "post-industrial environment, toxic spore cloud filling space, yellow-green danger color",
        "lighting": "toxic yellow-green spore illumination, hazard warning color light, environmental danger glow",
        "style": "post-apocalyptic fashion, toxic beauty editorial, environmental hazard glamour",
        "quality": "shot on Sony A1, spore cloud and skin detail, portrait 2:3 vertical"
    },
    "infection_glam": {
        "tag": "Infection Glam",
        "subject": "a striking female model with beautiful bioluminescent infection patterns spreading across her skin, disease as art",
        "body": "infection patterns as body art, disease made beautiful, pathogen aesthetic",
        "outfit": "sheer white medical garment, infection glow visible through fabric, patient-predator duality",
        "material": "sheer white medical cotton, bioluminescent infection visible beneath, clinical white",
        "environment": "isolation ward or clinical space, infection spread visualization, medical horror context",
        "lighting": "bioluminescent infection glow from skin, clinical fluorescent contrast, infection light from within",
        "style": "medical horror fashion, infection art editorial, disease-beauty concept",
        "quality": "shot on Phase One XT, bioluminescent skin pattern detail, portrait 2:3 vertical"
    },
    "virus_pattern_body": {
        "tag": "Virus Pattern Body",
        "subject": "a powerful female model with viral protein structure patterns covering her entire body as intricate body art",
        "body": "viral geometry mapping body contours, pathogen structure as body decoration",
        "outfit": "black minimal bodysuit, viral protein geometry projected or painted across body",
        "material": "matte black base, viral capsid geometry body paint in gold and white",
        "environment": "dark research environment, viral magnification displays surrounding, microscope aesthetic",
        "lighting": "cold blue scientific light, viral pattern gold catching light, research lab ambiance",
        "style": "scientific body art, virology meets fashion, electron microscope beauty",
        "quality": "shot on Hasselblad X2D, viral pattern body art precision, portrait 2:3 vertical"
    },
    "metamorphosis_editorial": {
        "tag": "Metamorphosis Editorial",
        "subject": "a transforming female model mid-metamorphosis, chrysalis material splitting to reveal evolved form within",
        "body": "mid-transformation frozen, old form splitting to reveal new, metamorphosis as fashion",
        "outfit": "chrysalis casing splitting open, evolved form wearing emergence as garment",
        "material": "chrysalis biomaterial splitting, new skin beneath, transformation material",
        "environment": "nature or studio, metamorphosis moment frozen, evolution context",
        "lighting": "warm transformation light from within chrysalis, evolution glow, emergence light",
        "style": "metamorphosis concept fashion, evolution editorial, butterfly emergence as luxury",
        "quality": "shot on Canon EOS R5, metamorphosis material detail, portrait 2:3 vertical"
    },
    "alien_host_glam": {
        "tag": "Alien Host Glam",
        "subject": "a glamorous female model as willing alien organism host, alien presence visible beneath skin and through eyes",
        "body": "human beauty as vessel, alien consciousness visible through eyes and skin movement",
        "outfit": "high fashion gown with alien organic accents, host-parasite couture",
        "material": "luxury fabric with alien organic growths, bioluminescent alien accents",
        "environment": "first contact aesthetic, alien organism integration environment, dual-world setting",
        "lighting": "alien bioluminescence from beneath skin, human fashion lighting contrast, two-nature illumination",
        "style": "alien encounter fashion, host organism editorial, sci-fi luxury concept",
        "quality": "shot on Phase One IQ4, alien-under-skin glow detail, portrait 2:3 vertical"
    },
}

# ── 카테고리 순서 ─────────────────────────────────────────
MIRROR_ORDER = [
    "infinity_mirror_goddess", "hall_of_mirrors_glam", "obsidian_mirror_ritual",
    "venetian_mirror_boudoir", "cheval_mirror_reveal", "broken_mirror_multiplied",
    "mercury_lake_reflection", "salt_flat_sky_merge", "rain_puddle_city_invert",
    "flooded_temple_mirror", "infinity_pool_edge_reflect", "morning_dew_skin_reflection",
    "glass_box_all_angles", "prism_light_body_split", "crystal_cave_skin_facets",
    "two_way_mirror_watcher", "window_rain_double", "soap_bubble_dome",
    "chrome_sphere_world", "polished_obsidian_floor", "supercar_chrome_reflect",
    "liquid_metal_pool", "foil_room_crush", "mirrored_skyscraper_facade",
]

SF_ORDER = [
    "cryo_emergence_wet", "specimen_amber_suspended", "clean_room_latex_protocol",
    "gene_sequencer_data_skin", "quarantine_protocol_breach", "petri_dish_giant_macro",
    "abyssal_pressure_glam", "mycelium_web_consumed", "coral_organism_absorption",
    "carnivorous_plant_trap", "symbiote_second_skin", "jellyfish_bloom_float",
    "cyborg_partial_reveal", "neural_lace_crown", "exoskeleton_stripped",
    "prosthetic_art", "spine_tech_implant", "synthetic_skin_tear",
    "mutation_bloom", "toxic_spore_cloud", "infection_glam",
    "virus_pattern_body", "metamorphosis_editorial", "alien_host_glam",
]


def write_jsons():
    written = 0
    for name, data in MIRROR_PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        written += 1
    for name, data in SF_PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        written += 1
    print(f"✅ JSON {written}종 생성 완료 → presets/")
    return written


def patch_dashboard():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 거울&반사 블록
    mirror_lines = [
        '\n    "\U0001fa9e 거울 & 반사 글래머": [',
        "        # G1 클래식미러",
    ]
    for p in MIRROR_ORDER[:6]:
        mirror_lines.append(f'        "{p}",')
    mirror_lines.append("        # G2 수면반사")
    for p in MIRROR_ORDER[6:12]:
        mirror_lines.append(f'        "{p}",')
    mirror_lines.append("        # G3 유리&프리즘")
    for p in MIRROR_ORDER[12:18]:
        mirror_lines.append(f'        "{p}",')
    mirror_lines.append("        # G4 크롬&메탈")
    for p in MIRROR_ORDER[18:]:
        mirror_lines.append(f'        "{p}",')
    mirror_lines.append("    ],")
    mirror_block = "\n".join(mirror_lines)

    # SF&바이오펑크 블록
    sf_lines = [
        '\n    "\U0001f9ec SF & 바이오펑크": [',
        "        # G1 크라이오&실험실",
    ]
    for p in SF_ORDER[:6]:
        sf_lines.append(f'        "{p}",')
    sf_lines.append("        # G2 심해&유기체")
    for p in SF_ORDER[6:12]:
        sf_lines.append(f'        "{p}",')
    sf_lines.append("        # G3 트랜스휴먼")
    for p in SF_ORDER[12:18]:
        sf_lines.append(f'        "{p}",')
    sf_lines.append("        # G4 바이러스&뮤테이션")
    for p in SF_ORDER[18:]:
        sf_lines.append(f'        "{p}",')
    sf_lines.append("    ],")
    sf_block = "\n".join(sf_lines)

    # 앵커: 듀오 글래머 닫힘 뒤에 삽입
    anchor = '"👯 듀오 글래머":'
    if anchor not in content:
        print("⚠️  앵커 없음 — PRESET_CATEGORIES 마지막 카테고리 키 확인 필요")
        return

    duo_pos = content.find(anchor)
    close_pos = content.find("\n    ],", duo_pos)
    if close_pos == -1:
        print("⚠️  듀오 글래머 블록 닫힘 위치를 찾을 수 없습니다")
        return

    insert_pos = close_pos + len("\n    ],")
    content = content[:insert_pos] + mirror_block + "\n" + sf_block + content[insert_pos:]

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ dashboard.py PRESET_CATEGORIES 패치 완료")
    print(f"   🪞 거울&반사 글래머 {len(MIRROR_ORDER)}종")
    print(f"   🧬 SF&바이오펑크 {len(SF_ORDER)}종")


if __name__ == "__main__":
    write_jsons()
    patch_dashboard()

    print("\n📋 PowerShell 검증:")
    for key in ["infinity_mirror_goddess", "cryo_emergence_wet",
                "alien_host_glam", "mirrored_skyscraper_facade"]:
        print(f'  Select-String -Path dashboard.py -Pattern "{key}"')
